import time
from itertools import groupby
from pathlib import Path

from . import client, config

SYSTEM_PROMPT = (
    "أنت مدقق لغوي عربي خبير في النحو والصرف. مهمتك تدقيق نص مفرّغ صوتياً (ASR) لمحاضرة "
    "في علم النحو. القواعد الصارمة:\n"
    "1. أعد النص كاملاً جملة بجملة دون حذف أو اختصار أو تلخيص أي جملة أو فكرة أو مثال.\n"
    "2. صحّح أخطاء التعرف الصوتي خاصة في المصطلحات النحوية (المبتدأ، الخبر، الرفع، النصب، "
    "الجر، الإعراب، المرفوعات، المنصوبات...) وصحّح الأخطاء اللغوية الواضحة فقط.\n"
    "3. أضف علامات الترقيم وشكّل ما يحتاج تشكيلاً.\n"
    "4. نظّم النص في Markdown: عناوين عند تغيّر الموضوع، وفقرات، وقوائم للأمثلة والشروط.\n"
    "5. احذف فقط كلام المداخلات الإدارية غير العلمية إن وُجد (مثل: التسجيل، الإرسال، الحضور).\n"
    "6. أعد فقط Markdown النهائي دون أي شرح أو تعليق.\n"
    "تذكّر: يجب أن يكون الناتج بطول النص الأصلي تقريباً، فأي نقص كبير يعني أنك حذفت محتوى وهذا ممنوع."
)

USER_TEMPLATE = (
    "دقّق المقطع التالي من التفريغ الصوتي وأعده بصيغة Markdown منظمة "
    "(المقطع {index} من {total}):\n\n{text}"
)

FALLBACK_MODELS = ["command-a-reasoning-08-2025", "command-a-03-2025"]
MIN_RESPONSE_RATIO = 0.25
SHORT_RESPONSE_WAIT_SECONDS = 10
TEMPERATURE = 0.2
MAX_OUTPUT_TOKENS = 8000
SENTENCE_ENDINGS = (".", "؟", "!", ":", "،")


def collapse_repetitions(text: str, max_repeat: int = 2) -> str:
    kept = []
    for word, group in groupby(text.split()):
        kept.extend([word] * min(len(list(group)), max_repeat))
    return " ".join(kept)


def split_into_blocks(full_text: str, max_words: int = None) -> list[str]:
    max_words = max_words or config.AUDIT_BLOCK_WORDS
    blocks = []
    current = []
    for word in full_text.split():
        current.append(word)
        if len(current) >= max_words and word.endswith(SENTENCE_ENDINGS):
            blocks.append(" ".join(current))
            current = []
    if current:
        blocks.append(" ".join(current))
    return blocks


def audit_all(full_text: str, work_dir: Path = None) -> list[str]:
    work_dir = work_dir or config.WORK_DIR
    audited_dir = work_dir / "audited"
    audited_dir.mkdir(parents=True, exist_ok=True)

    cleaned = collapse_repetitions(full_text)
    if len(cleaned) < len(full_text):
        print(f"Collapsed ASR repetitions: {len(full_text)} -> {len(cleaned)} chars")
    blocks = split_into_blocks(cleaned)
    total = len(blocks)
    print(f"Auditing {total} blocks with {config.AUDIT_MODEL}...")

    return [
        _audit_with_cache(block, index, total, audited_dir)
        for index, block in enumerate(blocks, start=1)
    ]


def _audit_with_cache(block: str, index: int, total: int, audited_dir: Path) -> str:
    out_file = audited_dir / f"block_{index:03d}.md"
    if _is_valid_cache(out_file, block):
        print(f"[{index}/{total}] (cached)")
        return out_file.read_text(encoding="utf-8")

    print(f"[{index}/{total}] Auditing {len(block.split())} words...")
    audited = audit_block(block, index, total)
    out_file.write_text(audited, encoding="utf-8")
    return audited


def _is_valid_cache(out_file: Path, block: str) -> bool:
    return out_file.exists() and out_file.stat().st_size > len(block) // 2


def audit_block(text: str, index: int, total: int) -> str:
    models = [config.AUDIT_MODEL] + [m for m in FALLBACK_MODELS if m != config.AUDIT_MODEL]
    for model_index, model in enumerate(models):
        if model_index > 0:
            print(f"  Falling back to {model}")
        result = _try_audit_with_model(text, index, total, model)
        if result is not None:
            return result
    raise RuntimeError(f"Failed to audit block {index} with all models")


def _try_audit_with_model(text: str, index: int, total: int, model: str) -> str | None:
    for attempt in range(1, config.MAX_RETRIES + 1):
        result = _request_audit(text, index, total, model)
        if result is None:
            return None
        if len(result) >= len(text) * MIN_RESPONSE_RATIO:
            return result
        print(f"  Short response ({len(result)}/{len(text)} chars) from {model}, retry {attempt}/{config.MAX_RETRIES}")
        time.sleep(SHORT_RESPONSE_WAIT_SECONDS)
    return None


def _request_audit(text: str, index: int, total: int, model: str) -> str | None:
    headers = {
        "Authorization": f"Bearer {config.COHERE_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_TEMPLATE.format(index=index, total=total, text=text)},
        ],
        "temperature": TEMPERATURE,
        "max_tokens": MAX_OUTPUT_TOKENS,
    }
    try:
        data = client.post_with_retry(
            config.CHAT_URL, headers=headers, payload=payload, description=model,
        )
    except client.RequestFailedError:
        return None
    return _extract_text(data)


def _extract_text(data: dict) -> str:
    parts = [
        block["text"]
        for block in data["message"]["content"]
        if block.get("type") == "text"
    ]
    return "\n".join(parts).strip()
