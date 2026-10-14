import argparse
import json
import sys
from pathlib import Path
from urllib.parse import urlsplit

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait

CONTAINERS = {
    "personal": ("Personal", 1),
    "work": ("Work", 2),
    "banking": ("Banking", 3),
    "shopping": ("Shopping", 4),
}


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


def execute_in_chrome_context(driver, javascript, *script_arguments):
    driver.set_context("chrome")
    try:
        return driver.execute_script(javascript, *script_arguments)
    finally:
        driver.set_context("content")


def container_details(container_name):
    container = CONTAINERS.get(container_name.casefold())
    if container is None:
        raise CommandError("الحاوية غير معروفة. المتاح: Personal, Work, Banking, Shopping")
    return container


def select_container_tab(driver, url, container_id):
    existing_handles = set(driver.window_handles)
    opened_container_id = execute_in_chrome_context(
        driver,
        """
        const [url, userContextId] = arguments;
        openWebLinkIn(url, "tab", { userContextId, inBackground: false });
        return Number(gBrowser.selectedTab.getAttribute("usercontextid") || 0);
        """,
        url,
        container_id,
    )
    if opened_container_id != container_id:
        raise CommandError(
            f"معرّف الحاوية المفتوحة {opened_container_id}، والمتوقع {container_id}"
        )
    new_handles = [handle for handle in driver.window_handles if handle not in existing_handles]
    target_handle = new_handles[-1] if new_handles else driver.window_handles[-1]
    driver.switch_to.window(target_handle)
    if url != "about:blank":
        WebDriverWait(driver, 25).until(lambda browser: browser.current_url != "about:blank")


def open_in_container(driver, container_name, url):
    validate_url(url)
    display_name, container_id = container_details(container_name)
    select_container_tab(driver, url, container_id)
    return {"container": display_name, "containerId": container_id, "host": safe_host(driver.current_url)}


def list_tabs(driver):
    return execute_in_chrome_context(
        driver,
        """
        return Array.from(gBrowser.tabs).map((tab, index) => {
          const rawId = tab.getAttribute("usercontextid");
          let host = "";
          try { host = new URL(tab.linkedBrowser.currentURI.spec).hostname; } catch {}
          return {index, containerId: Number(rawId || 0), host};
        });
        """,
    )


def controller_arguments():
    parser = argparse.ArgumentParser(description="التحكم في حاويات Firefox عبر Selenium")
    parser.add_argument("--profile", required=True, type=Path, help="مسار ملف Firefox الشخصي")
    parser.add_argument("--firefox", type=Path, help="مسار firefox.exe عند الحاجة")
    return parser.parse_args()


def start_driver(profile_path, firefox_path):
    profile_path = profile_path.resolve()
    if firefox_path is not None:
        firefox_path = firefox_path.resolve()
    if not profile_path.is_dir():
        raise SetupError("مجلد Firefox الشخصي المحدد غير موجود")
    if firefox_path is not None and not firefox_path.is_file():
        raise SetupError("ملف Firefox التنفيذي المحدد غير موجود")
    options = Options()
    if firefox_path is not None:
        options.binary_location = str(firefox_path)
    options.add_argument("-profile")
    options.add_argument(str(profile_path))
    service = Service(service_args=["--allow-system-access"])
    driver = webdriver.Firefox(service=service, options=options)
    try:
        actual_profile = Path(driver.capabilities.get("moz:profile", "")).resolve()
    except WebDriverException:
        close_driver(driver)
        raise
    if actual_profile != profile_path:
        close_driver(driver)
        raise SetupError("Firefox بدأ بملف شخصي مختلف؛ أُغلقت الجلسة")
    return driver


def parse_command(raw_command):
    try:
        command = json.loads(raw_command)
    except json.JSONDecodeError as error:
        raise CommandError("صيغة JSON غير صالحة") from error
    if not isinstance(command, dict):
        raise CommandError("يجب أن يكون الأمر كائن JSON")
    return command


def execute_action(driver, command):
    action = command.get("action")
    if action == "list":
        emit_event({"event": "tabs", "tabs": list_tabs(driver)})
    elif action == "open":
        opened = open_in_container(
            driver,
            str(command.get("container", "")),
            str(command.get("url", "")),
        )
        emit_event({"event": "opened", **opened})
    elif action == "navigate":
        url = str(command.get("url", ""))
        validate_url(url)
        driver.get(url)
        emit_event({"event": "navigated", "host": safe_host(driver.current_url)})
    elif action == "quit":
        emit_event({"event": "closing"})
        return False
    else:
        raise CommandError("الأوامر المتاحة: list, open, navigate, quit")
    return True


def run_command(driver, raw_command):
    return execute_action(driver, parse_command(raw_command))


def serve_commands(driver):
    emit_event({
        "event": "ready",
        "firefoxVersion": driver.capabilities.get("browserVersion"),
        "geckodriverVersion": driver.capabilities.get("moz:geckodriverVersion"),
        "restoredTabs": len(driver.window_handles),
    })
    for raw_command in sys.stdin:
        if not raw_command.strip():
            continue
        try:
            if not run_command(driver, raw_command):
                return
        except CommandError as error:
            emit_event({"event": "error", "message": str(error)})


def close_driver(driver):
    try:
        driver.quit()
    except WebDriverException as error:
        print(f"تعذر إغلاق جلسة Firefox ({type(error).__name__})", file=sys.stderr)


def main():
    arguments = controller_arguments()
    try:
        driver = start_driver(arguments.profile, arguments.firefox)
    except SetupError as error:
        print(f"تعذر بدء Firefox: {error}", file=sys.stderr)
        return 2
    except WebDriverException as error:
        print(f"تعذر بدء Firefox ({type(error).__name__})", file=sys.stderr)
        return 2
    try:
        serve_commands(driver)
    except WebDriverException as error:
        emit_event({
            "event": "error",
            "message": f"فشل أمر المتصفح ({type(error).__name__}); أُغلقت أداة التحكم",
        })
        return 1
    finally:
        close_driver(driver)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
