import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit

from playwright.sync_api import Error as PlaywrightError, TimeoutError as PlaywrightTimeout
from playwright.sync_api import sync_playwright

DEFAULT_PORT = 9222
DEFAULT_TIMEOUT_MS = 15000
LICENSE_FILE_NAME = "orbita.config"
LICENSE_CACHE_DIR = Path(
    os.environ.get("LOCALAPPDATA", str(Path.home()))
) / "gologin-orbita-license"
PROFILE_PATTERN = re.compile(r'--user-data-dir="?([^"\s]+)"?')
DEBUG_FLAGS = (
    "--remote-debugging-port",
    "--remote-debugging-pipe",
    "--remote-allow-origins",
)
CHILD_FLAG = "--type="
POWERSHELL_QUERY = (
    "Get-CimInstance Win32_Process -Filter \"Name='chrome.exe'\" | "
    "Where-Object { $_.CommandLine -like '*orbita*' -or $_.CommandLine -like '*gologin*' } | "
    "Select-Object ProcessId, ExecutablePath, CommandLine | ConvertTo-Json -Compress"
)


class CommandError(Exception):
    pass


class SetupError(Exception):
    pass


def emit_event(event_record):
    print(json.dumps(event_record, ensure_ascii=False), flush=True)


def safe_host(url):
    try:
        return urlsplit(url).hostname or ""
    except ValueError:
        return ""


def validate_url(url):
    if url == "about:blank":
        return
    try:
        parsed = urlsplit(url)
    except ValueError as error:
        raise CommandError("رابط غير صالح") from error
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise CommandError("استخدم رابط http/https أو about:blank")
    if parsed.username is not None or parsed.password is not None:
        raise CommandError("لا تستخدم رابطًا يتضمن بيانات اعتماد")


def validate_selector(selector):
    if not isinstance(selector, str) or not selector.strip():
        raise CommandError("المحدّد selector مطلوب كسلسلة غير فارغة")
    return selector


def controller_arguments():
    parser = argparse.ArgumentParser(
        description="التحكم في متصفح GoLogin (Orbita) عبر بروتوكول CDP"
    )
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="منفذ التصحيح")
    parser.add_argument(
        "--profile",
        type=Path,
        help="مسار مجلد بروفايل GoLogin، ويُكتشف تلقائيًا إذا تُرك فارغًا",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT_MS,
        help="مهلة انتظار العناصر بالمللي ثانية",
    )
    parser.add_argument(
        "--wait-token",
        type=int,
        default=180,
        help="مدة انتظار رمز تشغيل Orbita الذي يكتبه GoLogin قبل التشغيل، بالثواني",
    )
    parser.add_argument(
        "--no-restart",
        action="store_true",
        help="لا تغلق البروفايل الجاري؛ ارتبط فقط إذا كان يفتح منفذ التصحيح",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="اعرض أمر إعادة التشغيل دون تنفيذ أي تغيير",
    )
    return parser.parse_args()


def running_orbita_processes():
    result = subprocess.run(
        ["powershell", "-NoProfile", "-NonInteractive", "-Command", POWERSHELL_QUERY],
        capture_output=True,
        text=True,
        timeout=90,
    )
    if result.returncode != 0:
        raise SetupError(f"تعذر قراءة عمليات Orbita ({result.stderr.strip()})")
    payload = result.stdout.strip()
    if not payload:
        return []
    parsed = json.loads(payload)
    return parsed if isinstance(parsed, list) else [parsed]


def profile_directory(command_line):
    match = PROFILE_PATTERN.search(command_line)
    return match.group(1) if match else ""


def root_process(processes, wanted_profile):
    candidates = [item for item in processes if CHILD_FLAG not in item.get("CommandLine", "")]
    if wanted_profile:
        wanted = str(Path(wanted_profile)).lower()
        candidates = [
            item for item in candidates if profile_directory(item["CommandLine"]).lower() == wanted
        ]
    if not candidates:
        raise SetupError(
            "لم أجد بروفايل Orbita قيد التشغيل لهذا المسار؛ افتح البروفايل من GoLogin أولًا"
        )
    return candidates[0]


def split_invocation(command_line):
    executable, _, arguments = command_line.partition(" ")
    return executable.strip().strip('"'), arguments.strip()


def strip_debug_flags(arguments):
    cleaned = arguments
    for flag in DEBUG_FLAGS:
        cleaned = re.sub(rf'{re.escape(flag)}=\S+\s*', "", cleaned)
        cleaned = re.sub(rf'(?:^|\s){re.escape(flag)}\s*', " ", cleaned)
    return " ".join(cleaned.split())


def build_command(process, port):
    executable, arguments = split_invocation(process["CommandLine"])
    fingerprint_arguments = strip_debug_flags(arguments)
    command = (
        f'"{executable}" {fingerprint_arguments} '
        f"--remote-debugging-port={port} --remote-allow-origins=*"
    )
    return executable, command


def stop_browser(process_id):
    subprocess.run(
        ["taskkill", "/PID", str(process_id), "/T", "/F"],
        capture_output=True,
        text=True,
        timeout=60,
    )


def wait_for_debug_port(port, timeout_seconds=45):
    endpoint = f"http://127.0.0.1:{port}/json/version"
    deadline = time.monotonic() + timeout_seconds
    last_error = "لم يستجب المتصفح"
    while time.monotonic() < deadline:
        try:
            with urllib.request.urlopen(endpoint, timeout=4) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.URLError, OSError, ValueError) as error:
            last_error = str(error)
            time.sleep(1)
    raise SetupError(f"لم يُفتح منفذ التصحيح {port} ({last_error})")


def port_in_use(port):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=3):
            return True
    except (urllib.error.URLError, OSError):
        return False


def license_cache_path(profile_directory_path):
    return LICENSE_CACHE_DIR / f"{Path(profile_directory_path).name}.config"


def store_license(profile_directory_path, payload):
    LICENSE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cached = license_cache_path(profile_directory_path)
    cached.write_bytes(payload)
    return cached


def cache_license(profile_directory_path):
    live_license = Path(profile_directory_path) / LICENSE_FILE_NAME
    if not live_license.is_file():
        return None
    return store_license(profile_directory_path, live_license.read_bytes())


def usable_license_payload(payload):
    if len(payload.strip()) < 32:
        return False
    try:
        return bool(json.loads(payload))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return False


def wait_for_run_token(profile_directory_path, seconds):
    live_license = Path(profile_directory_path) / LICENSE_FILE_NAME
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        try:
            payload = live_license.read_bytes()
        except OSError:
            time.sleep(0.001)
            continue
        if usable_license_payload(payload):
            return store_license(profile_directory_path, payload)
        time.sleep(0.001)
    return None


def restore_license(profile_directory_path):
    live_license = Path(profile_directory_path) / LICENSE_FILE_NAME
    if live_license.is_file():
        return None
    cached = license_cache_path(profile_directory_path)
    if not cached.is_file():
        raise SetupError("ملف orbita.config غير محفوظ؛ شغّل البروفايل من GoLogin مرة واحدة أثناء عمل السكربت")
    shutil.copy2(cached, live_license)
    return cached


def discover_process(arguments, seconds):
    deadline = time.monotonic() + seconds
    while True:
        try:
            return root_process(running_orbita_processes(), arguments.profile)
        except SetupError:
            if time.monotonic() >= deadline:
                raise
            time.sleep(1)


def start_orbita(arguments, process, port):
    executable, command = build_command(process, port)
    if not Path(executable).is_file():
        raise SetupError("ملف Orbita التنفيذي المحدد غير موجود")
    profile_path = profile_directory(process["CommandLine"])
    if arguments.dry_run:
        emit_event({"event": "dryRun", "command": command, "profile": profile_path})
        return None
    cached = cache_license(profile_path)
    if cached is None:
        emit_event({
            "event": "waitingForStart",
            "seconds": arguments.wait_token,
            "instruction": "أوقف البروفايل من GoLogin ثم شغّله مرة أخرى؛ السكربت ينتظر رمز التشغيل",
        })
        cached = wait_for_run_token(profile_path, arguments.wait_token)
        if cached is None:
            raise SetupError("لم يُلتقط رمز التشغيل؛ شغّل البروفايل من GoLogin مرة أخرى أثناء عمل السكربت")
        process = root_process(running_orbita_processes(), arguments.profile)
    emit_event({"event": "restarting", "pid": process["ProcessId"], "license": str(cached)})
    stop_browser(process["ProcessId"])
    time.sleep(2)
    restore_license(profile_path)
    subprocess.Popen(command, close_fds=True)
    return wait_for_debug_port(port)


def connect_to_browser(port):
    playwright = sync_playwright().start()
    try:
        browser = playwright.chromium.connect_over_cdp(f"http://127.0.0.1:{port}")
    except PlaywrightError as error:
        playwright.stop()
        raise SetupError(f"تعذر الاتصال بالمتصفح ({error})") from error
    if not browser.contexts:
        playwright.stop()
        raise SetupError("المتصفح المتصل لا يحتوي على جلسة صفحات")
    return playwright, browser


class OrbitaSession:
    def __init__(self, browser, timeout_ms):
        self.browser = browser
        self.context = browser.contexts[0]
        self.timeout_ms = timeout_ms
        self.active_index = 0

    def pages(self):
        return self.context.pages

    def active_page(self):
        pages = self.pages()
        if not pages:
            raise CommandError("لا توجد نوافذ مفتوحة في المتصفح")
        self.active_index = max(0, min(self.active_index, len(pages) - 1))
        return pages[self.active_index]

    def locator(self, selector):
        validate_selector(selector)
        return self.active_page().locator(selector).first

    def command_timeout(self, command):
        requested = command.get("timeout")
        if requested is None:
            return self.timeout_ms
        if not isinstance(requested, int) or requested <= 0:
            raise CommandError("timeout يجب أن يكون رقمًا صحيحًا أكبر من صفر")
        return requested

    def tab_report(self):
        return [
            {
                "index": index,
                "active": index == self.active_index,
                "url": page.url,
                "host": safe_host(page.url),
                "title": page.title(),
            }
            for index, page in enumerate(self.pages())
        ]

    def run(self, command):
        action = command.get("action")
        if action == "status":
            return {"status": self.status()}
        if action == "list":
            return {"tabs": self.tab_report()}
        if action == "select":
            index = command.get("index")
            if not isinstance(index, int) or not 0 <= index < len(self.pages()):
                raise CommandError("index خارج نطاق النوافذ المفتوحة")
            self.active_index = index
            return {"selected": index, "tabs": self.tab_report()}
        if action == "open":
            return self.open_tab(command)
        if action == "navigate":
            return self.navigate(command)
        if action == "reload":
            self.active_page().reload(timeout=self.command_timeout(command))
            return {"reloaded": safe_host(self.active_page().url)}
        if action == "back":
            self.active_page().go_back(timeout=self.command_timeout(command))
            return {"url": self.active_page().url}
        if action == "forward":
            self.active_page().go_forward(timeout=self.command_timeout(command))
            return {"url": self.active_page().url}
        if action == "click":
            self.locator(command.get("selector")).click(timeout=self.command_timeout(command))
            return {"clicked": command["selector"]}
        if action == "fill":
            self.locator(command.get("selector")).fill(
                str(command.get("value", "")), timeout=self.command_timeout(command)
            )
            return {"filled": command["selector"]}
        if action == "press":
            self.locator(command.get("selector")).press(
                str(command.get("key", "")), timeout=self.command_timeout(command)
            )
            return {"pressed": command["key"]}
        if action == "text":
            text = self.locator(command.get("selector")).inner_text(
                timeout=self.command_timeout(command)
            )
            return {"text": text}
        if action == "wait":
            self.locator(command.get("selector")).wait_for(
                state=command.get("state", "visible"), timeout=self.command_timeout(command)
            )
            return {"visible": command["selector"]}
        if action == "eval":
            expression = command.get("expression")
            if not isinstance(expression, str) or not expression.strip():
                raise CommandError("expression مطلوب لتقييم JavaScript")
            return {"result": self.active_page().evaluate(expression)}
        if action == "screenshot":
            return self.screenshot(command)
        if action == "cookies":
            urls = command.get("urls")
            cookies = self.context.cookies(urls if isinstance(urls, list) else None)
            return {
                "cookies": [
                    {"name": item["name"], "domain": item["domain"], "path": item["path"]}
                    for item in cookies
                ]
            }
        raise CommandError(
            "الأوامر المتاحة: status, list, select, open, navigate, reload, back, forward, "
            "click, fill, press, text, wait, eval, screenshot, cookies, quit"
        )

    def status(self):
        return {
            "orbitaVersion": self.browser.version,
            "connected": self.browser.is_connected(),
            "tabs": len(self.pages()),
            "activeIndex": self.active_index,
        }

    def open_tab(self, command):
        url = str(command.get("url", ""))
        validate_url(url)
        page = self.context.new_page()
        if url != "about:blank":
            page.goto(url, timeout=self.command_timeout(command))
        self.active_index = len(self.pages()) - 1
        return {"opened": page.url, "host": safe_host(page.url), "index": self.active_index}

    def navigate(self, command):
        url = str(command.get("url", ""))
        validate_url(url)
        if url != "about:blank":
            self.active_page().goto(url, timeout=self.command_timeout(command))
        else:
            self.active_page().evaluate("window.location.assign('about:blank')")
        return {"url": self.active_page().url, "host": safe_host(self.active_page().url)}

    def screenshot(self, command):
        raw_path = command.get("path", "orbita_screenshot.png")
        target = Path(str(raw_path)).expanduser().resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        self.active_page().screenshot(
            path=str(target), full_page=bool(command.get("fullPage", False))
        )
        return {"screenshot": str(target)}


def parse_command(raw_command):
    try:
        command = json.loads(raw_command)
    except json.JSONDecodeError as error:
        raise CommandError("صيغة JSON غير صالحة") from error
    if not isinstance(command, dict):
        raise CommandError("يجب أن يكون الأمر كائن JSON")
    return command


def execute_action(session, command):
    if command.get("action") == "quit":
        emit_event({"event": "detaching"})
        return False
    emit_event({"event": "result", **session.run(command)})
    return True


def serve_commands(session):
    emit_event({"event": "ready", **session.status()})
    for raw_command in sys.stdin:
        if not raw_command.strip():
            continue
        try:
            if not execute_action(session, parse_command(raw_command)):
                return
        except CommandError as error:
            emit_event({"event": "error", "message": str(error)})
        except PlaywrightTimeout as error:
            emit_event({"event": "error", "message": f"انتهت المهلة ({error})"})
        except PlaywrightError as error:
            emit_event({"event": "error", "message": f"فشل أمر المتصفح ({error})"})


def prepare_browser(arguments):
    if port_in_use(arguments.port):
        emit_event({"event": "attaching", "port": arguments.port})
        return "", wait_for_debug_port(arguments.port)
    if arguments.no_restart:
        raise SetupError(
            f"لا يوجد متصفح يستمع على المنفذ {arguments.port}؛ أعد التشغيل بدون --no-restart"
        )
    process = discover_process(arguments, arguments.wait_token)
    profile_path = profile_directory(process["CommandLine"])
    version = start_orbita(arguments, process, arguments.port)
    return profile_path, version


def main():
    arguments = controller_arguments()
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    try:
        profile_path, version = prepare_browser(arguments)
    except SetupError as error:
        print(f"تعذر تجهيز المتصفح: {error}", file=sys.stderr)
        return 2
    if arguments.dry_run:
        return 0
    emit_event(
        {
            "event": "started",
            "port": arguments.port,
            "orbitaVersion": version.get("Browser"),
            "webSocket": version.get("webSocketDebuggerUrl"),
            "profile": profile_path,
        }
    )
    try:
        playwright, browser = connect_to_browser(arguments.port)
    except SetupError as error:
        print(f"تعذر الاتصال بالمتصفح: {error}", file=sys.stderr)
        return 2
    session = OrbitaSession(browser, arguments.timeout)
    try:
        serve_commands(session)
    finally:
        try:
            browser.close()
        finally:
            playwright.stop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())