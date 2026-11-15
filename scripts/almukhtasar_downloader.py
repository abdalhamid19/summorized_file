from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import requests


API_URL = "https://read.tafsir.one/get.php"
VIEWER_URL = "https://read.tafsir.one/almukhtasar"
TERMS_URL = "https://mokhtasr.com/fa/pages/terms-and-conditions"
DEFAULT_OUTPUT = (
    Path(__file__).resolve().parents[1]
    / "main_obsidian"
    / "دين"
    / "تفسير"
    / "المختصر في التفسير - نسخة شخصية"
)


class DownloadError(Exception):
    pass


def fetch_payload(session: requests.Session, number: int, ayah: int) -> dict[str, object]:
    params = {"uth": "", "src": "almukhtasar", "s": number, "a": ayah}
    for attempt in range(3):
        try:
            response = session.get(API_URL, params=params, timeout=30)
        except requests.RequestException as exc:
            if attempt == 2:
                raise DownloadError(f"تعذر الاتصال أثناء جلب السورة {number}: {exc}") from exc
            time.sleep(2**attempt)
            continue

        if response.status_code in (403, 429):
            raise DownloadError(
                f"رفض الموقع الطلب (HTTP {response.status_code}) عند السورة {number}، الآية {ayah}. "
                "أوقفت الجلب؛ أعد المحاولة لاحقًا دون تجاوز القيود."
            )
        if response.status_code >= 500:
            if attempt == 2:
                raise DownloadError(f"تعطل الموقع (HTTP {response.status_code}) عند السورة {number}.")
            time.sleep(2**attempt)
            continue
        if not response.ok:
            raise DownloadError(f"فشل طلب السورة {number} (HTTP {response.status_code}).")

        try:
            payload = response.json()
        except requests.JSONDecodeError as exc:
            raise DownloadError(f"استجابة غير مفهومة للسورة {number}، الآية {ayah}.") from exc
        if not isinstance(payload, dict) or not isinstance(payload.get("data"), str):
            raise DownloadError(f"لم يُعثر على نص التفسير للسورة {number}، الآية {ayah}.")
        if not payload["data"].strip():
            raise DownloadError(f"استجابة ناقصة للسورة {number}، الآية {ayah}.")
        return payload

    raise DownloadError(f"تعذر جلب السورة {number}.")


def fetch_surah(session: requests.Session, number: int, delay: float) -> dict[str, object]:
    sections: list[str] = []
    seen_starts: dict[int, list[object]] = {}
    requested_ayah = 1
    ayah_count = 0

    while True:
        if requested_ayah > 1 and delay:
            time.sleep(delay)
        payload = fetch_payload(session, number, requested_ayah)
        start = int(payload.get("ayahs_start", requested_ayah))
        ayahs = payload.get("ayahs")
        if not isinstance(ayahs, list):
            ayah = payload.get("ayah")
            ayahs = [ayah] if isinstance(ayah, str) and ayah else []
        if not ayahs:
            raise DownloadError(f"لا توجد آيات في استجابة السورة {number}، الآية {requested_ayah}.")
        if start in seen_starts:
            if seen_starts[start] != ayahs:
                raise DownloadError(f"تكررت بداية المقطع مع اختلاف محتواه في السورة {number}.")
            break
        if start != requested_ayah:
            raise DownloadError(f"فجوة في ترقيم المقاطع عند السورة {number}، الآية {requested_ayah}.")

        seen_starts[start] = ayahs
        sections.append(str(payload["data"]).strip())
        ayah_count += len(ayahs)
        next_ayah = start + len(ayahs)
        if next_ayah <= requested_ayah:
            raise DownloadError(f"لم يتقدم الترقيم أثناء جلب السورة {number}.")
        requested_ayah = next_ayah

    return {"data": "\n\n".join(sections), "ayah_count": ayah_count}


def surah_title(data: str, number: int) -> str:
    first_line = data.splitlines()[0] if data.splitlines() else ""
    match = re.match(r"\*\s*سورة\s+(.+?)(?:\s+(?:مكية|مدنية)\b.*)?$", first_line)
    if match:
        return match.group(1).strip()
    return f"السورة {number}"


def safe_filename(title: str) -> str:
    cleaned = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "-", title).strip(" .-")
    return cleaned or "سورة"


def markdown_for_surah(number: int, payload: dict[str, object], retrieved: date) -> tuple[str, str]:
    data = str(payload["data"]).strip()
    title = surah_title(data, number)
    ayah_count = payload.get("ayah_count", "غير متاح")
    api_url = requests.Request(
        "GET", API_URL, params={"uth": "", "src": "almukhtasar", "s": number, "a": 1}
    ).prepare().url
    content = (
        f"---\ntitle: المختصر في التفسير - سورة {title}\n"
        "tags:\n  - تفسير\n  - المختصر-في-التفسير\n---\n\n"
        f"# سورة {title}\n\n"
        f"عدد الآيات: {ayah_count}\n\n"
        f"{data}\n\n"
        "## المصدر\n\n"
        f"- [التفسير التفاعلي - المختصر]({VIEWER_URL})\n"
        f"- [أول مقطع من بيانات السورة]({api_url})؛ جُلبت المقاطع التالية بالتتابع.\n"
        f"- تاريخ الجلب: {retrieved.isoformat()}\n"
        "- النسخة محلية للاستخدام الشخصي غير التجاري؛ راجع "
        f"[شروط الاستخدام]({TERMS_URL}).\n"
    )
    return title, content


def write_file(path: Path, content: str, overwrite: bool) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_text(encoding="utf-8") == content:
            return False
        if not overwrite:
            return False

    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", newline="\n", dir=path.parent, delete=False
    ) as temp_file:
        temp_file.write(content)
        temp_path = Path(temp_file.name)
    os.replace(temp_path, path)
    return True


def make_index(entries: list[tuple[int, str, str]], retrieved: date) -> str:
    lines = [
        "---",
        "title: المختصر في التفسير - فهرس النسخة الشخصية",
        "tags:",
        "  - تفسير",
        "  - المختصر-في-التفسير",
        "---",
        "",
        "# المختصر في التفسير",
        "",
        "نسخة محلية للاستخدام الشخصي غير التجاري. لا تنشر هذه النسخة أو توزّعها.",
        "",
        f"تاريخ الجلب: {retrieved.isoformat()}",
        "",
        "## السور",
        "",
    ]
    lines.extend(f"- [[{filename.removesuffix('.md')}|سورة {title}]]" for _, title, filename in entries)
    lines.extend(
        [
            "",
            "## المصدر",
            "",
            f"- [التفسير التفاعلي - المختصر]({VIEWER_URL})",
            f"- [شروط الاستخدام]({TERMS_URL})",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="يحفظ نص المختصر في التفسير محليًا للاستخدام الشخصي غير التجاري."
    )
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true", help="جلب السور كلها (114 سورة).")
    selection.add_argument("--surah", type=int, help="رقم سورة واحدة من 1 إلى 114.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="مجلد ملفات Markdown.")
    parser.add_argument("--delay", type=float, default=0.5, help="الفاصل بالثواني بين طلبات المقاطع.")
    parser.add_argument("--overwrite", action="store_true", help="استبدال الملفات الموجودة.")
    args = parser.parse_args()
    if args.surah is not None and not 1 <= args.surah <= 114:
        parser.error("يجب أن يكون رقم السورة بين 1 و114.")
    if args.delay < 0:
        parser.error("يجب ألا يكون --delay سالبًا.")
    return args


def main() -> int:
    args = parse_args()
    numbers = range(1, 115) if args.all else [args.surah]
    retrieved = date.today()
    entries: list[tuple[int, str, str]] = []
    session = requests.Session()
    session.headers.update({"User-Agent": "AlmukhtasarPersonalCopy/1.0"})

    try:
        for number in numbers:
            payload = fetch_surah(session, number, args.delay)
            title, content = markdown_for_surah(number, payload, retrieved)
            filename = f"{number:03d} - {safe_filename(title)}.md"
            written = write_file(args.output / filename, content, args.overwrite)
            entries.append((number, title, filename))
            action = "حُفظت" if written else "أُبقي الملف الموجود دون تعديل"
            print(f"{action}: السورة {number} - {title}")
        if args.all:
            index_written = write_file(
                args.output / "00 - فهرس المختصر في التفسير.md",
                make_index(entries, retrieved),
                args.overwrite,
            )
            if not index_written:
                print("أُبقي الفهرس الموجود دون تعديل")
    except (DownloadError, OSError) as exc:
        print(f"خطأ: {exc}", file=sys.stderr)
        return 1
    finally:
        session.close()

    print(f"اكتمل الحفظ في: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
