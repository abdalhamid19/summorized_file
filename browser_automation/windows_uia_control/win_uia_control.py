import argparse
import ctypes
import ctypes.wintypes
import json
import sys
import time
from pathlib import Path

from pywinauto import Desktop, mouse
from pywinauto.keyboard import send_keys

BROWSER_WINDOW_CLASS = "Chrome_WidgetWin_1"
ADDRESS_BAR_MARKERS = ("address", "omnibox", "العناوين", "البحث")
DEFAULT_ACTION_DELAY_MS = 120


class CommandError(Exception):
    pass


class SetupError(Exception):
    pass


def emit_event(event_record):
    print(json.dumps(event_record, ensure_ascii=False), flush=True)


def process_image(process_id):
    kernel32 = ctypes.windll.kernel32
    process = kernel32.OpenProcess(0x1000, False, process_id)
    if not process:
        return ""
    try:
        buffer = ctypes.create_unicode_buffer(1024)
        size = ctypes.wintypes.DWORD(1024)
        query = ctypes.windll.kernel32.QueryFullProcessImageNameW
        query(process, 0, buffer, ctypes.byref(size))
        return buffer.value
    finally:
        kernel32.CloseHandle(process)


def orbita_windows(title_filter):
    desktop = Desktop(backend="uia")
    found = []
    for window in desktop.windows():
        try:
            info = window.element_info
            if info.class_name != BROWSER_WINDOW_CLASS:
                continue
            title = window.window_text()
        except Exception:
            continue
        if "orbita" not in process_image(info.process_id).lower():
            continue
        if title_filter and title_filter.casefold() not in title.casefold():
            continue
        found.append(window)
    return found


def require_window(title_filter):
    windows = orbita_windows(title_filter)
    if not windows:
        raise CommandError(
            "لا توجد نافذة Orbita مطابقة؛ تأكد أن المتصفح مفتوح وحدد --window بعنوان جزء من النافذة"
        )
    return windows[0]


def window_report(window):
    info = window.element_info
    rectangle = window.rectangle()
    return {
        "title": window.window_text(),
        "pid": info.process_id,
        "rect": {"left": rectangle.left, "top": rectangle.top,
                 "right": rectangle.right, "bottom": rectangle.bottom},
        "minimized": bool(window.is_minimized()),
    }


def focus_window(window):
    try:
        window.set_focus()
    except Exception as error:
        raise CommandError(f"تعذر تفعيل النافذة ({error})") from error
    time.sleep(DEFAULT_ACTION_DELAY_MS / 1000)


def tab_items(window):
    try:
        return window.descendants(control_type="TabItem")
    except Exception as error:
        raise CommandError(f"تعذر قراءة التبويبات ({error})") from error


def tab_report(window):
    report = []
    for index, tab in enumerate(tab_items(window)):
        try:
            selected = bool(tab.is_selected())
        except Exception:
            selected = False
        report.append({"index": index, "title": tab.window_text(), "selected": selected})
    return report


def address_bar(window):
    for element in window.descendants(control_type="Edit"):
        name = element.element_info.name or ""
        if any(marker.casefold() in name.casefold() for marker in ADDRESS_BAR_MARKERS):
            return element
    edits = window.descendants(control_type="Edit")
    if not edits:
        raise CommandError("لم أجد شريط العناوين في النافذة")
    return edits[0]


def element_value(element):
    try:
        value = element.get_value()
        if value:
            return value
    except Exception:
        pass
    return element.element_info.name or element.window_text() or ""


def read_url(window):
    return element_value(address_bar(window))


CLEAR_SEQUENCE = "{END}{BACKSPACE 400}"


def type_into(element, text, clear=True):
    try:
        element.click_input()
        if clear:
            element.type_keys(CLEAR_SEQUENCE)
        element.type_keys(text, with_spaces=True)
    except Exception as error:
        raise CommandError(f"تعذر الكتابة في العنصر ({error})") from error
    time.sleep(DEFAULT_ACTION_DELAY_MS / 1000)


def open_address(window, text, after_keys):
    bar = address_bar(window)
    try:
        bar.click_input()
        bar.type_keys(CLEAR_SEQUENCE)
        bar.type_keys(text, with_spaces=True)
        bar.type_keys(after_keys)
    except Exception as error:
        raise CommandError(f"تعذر الكتابة في شريط العناوين ({error})") from error
    time.sleep(1.5)


def find_by_name(window, name, control_type=None, partial=False):
    candidates = []
    for control in (control_type,) if control_type else (
        "Button", "Hyperlink", "Edit", "Text", "MenuItem", "TabItem", "Document", "CheckBox"
    ):
        try:
            found = window.descendants(control_type=control)
        except Exception:
            continue
        candidates.extend(found)
        for candidate in candidates:
            try:
                label = candidate.element_info.name or ""
            except Exception:
                continue
            if label == name or label.casefold() == name.casefold():
                return candidate
    if not partial:
        return None
    wanted = name.casefold()
    for candidate in candidates:
        try:
            label = candidate.element_info.name or ""
        except Exception:
            continue
        if wanted in label.casefold():
            return candidate
    return None


def click_element(element):
    rectangle = element.rectangle()
    if rectangle.width() <= 0 or rectangle.height() <= 0:
        raise CommandError("العنصر المحدد بلا مساحة على الشاشة")
    x = (rectangle.left + rectangle.right) // 2
    y = (rectangle.top + rectangle.bottom) // 2
    mouse.move(coords=(x, y))
    time.sleep(DEFAULT_ACTION_DELAY_MS / 1000)
    mouse.click(button="left", coords=(x, y))
    time.sleep(DEFAULT_ACTION_DELAY_MS / 1000)


def document_text(window, limit):
    try:
        documents = window.descendants(control_type="Document")
    except Exception as error:
        raise CommandError(f"تعذر قراءة محتوى الصفحة ({error})") from error
    for document in documents:
        try:
            texts = document.descendants(control_type="Text")
        except Exception:
            continue
        chunks = [item.element_info.name.strip() for item in texts
                  if item.element_info.name and item.element_info.name.strip()]
        if chunks:
            return "\n".join(chunks)[:limit]
    for document in documents:
        try:
            text = document.window_text()
        except Exception:
            continue
        if text and text.strip():
            return text.strip()[:limit]
    return window_text(window, limit)


def window_text(window, limit):
    chunks = []
    for control_type in ("Text", "Hyperlink", "Button"):
        try:
            elements = window.descendants(control_type=control_type)
        except Exception:
            continue
        for element in elements:
            label = element.element_info.name
            if label and label.strip():
                chunks.append(label.strip())
        if chunks:
            break
    if not chunks:
        raise CommandError("محتوى الصفحة غير متاح عبر شجرة الوصول")
    return "\n".join(chunks)[:limit]


def controller_arguments():
    parser = argparse.ArgumentParser(
        description="التحكم في نافذة GoLogin المفتوحة عبر أتمتة واجهة ويندوز"
    )
    parser.add_argument(
        "--window",
        default="",
        help="جزء من عنوان النافذة المطلوبة لتحديد البروفايل",
    )
    parser.add_argument(
        "--commands",
        type=Path,
        help="ملف UTF-8 يحتوي على أوامر JSON Lines بدل القراءة من الإدخال القياسي",
    )
    parser.add_argument(
        "--delay",
        type=int,
        default=DEFAULT_ACTION_DELAY_MS,
        help="مهلة Settle بعد كل إجراء بالمللي ثانية",
    )
    return parser.parse_args()


class WindowSession:
    def __init__(self, title_filter, delay_ms):
        self.title_filter = title_filter
        self.delay_ms = delay_ms

    def window(self):
        return require_window(self.title_filter)

    def run(self, command):
        action = command.get("action")
        if action == "windows":
            return {"windows": [window_report(item) for item in orbita_windows(self.title_filter)]}
        if action == "focus":
            window = self.window()
            focus_window(window)
            return {"focused": window_report(window)}
        if action == "tabs":
            return {"tabs": tab_report(self.window())}
        if action == "select-tab":
            return self.select_tab(command)
        if action == "url":
            return {"url": read_url(self.window())}
        if action == "navigate":
            window = self.window()
            open_address(window, str(command.get("url", "")), "{ENTER}")
            return {"url": read_url(window)}
        if action == "search":
            window = self.window()
            open_address(window, str(command.get("query", "")), "{ENTER}")
            return {"url": read_url(window)}
        if action == "click":
            return self.click(command)
        if action == "click-name":
            return self.click_by_name(command)
        if action == "type":
            return self.fill(command)
        if action == "keys":
            return self.send_hotkeys(command)
        if action == "scroll":
            return self.scroll(command)
        if action == "page-text":
            limit = command.get("limit", 4000)
            if not isinstance(limit, int) or limit <= 0:
                raise CommandError("limit يجب أن يكون رقمًا صحيحًا أكبر من صفر")
            return {"text": document_text(self.window(), limit)}
        if action == "screenshot":
            return self.screenshot(command)
        raise CommandError(
            "الأوامر المتاحة: windows, focus, tabs, select-tab, url, navigate, search, "
            "click, click-name, type, keys, scroll, page-text, screenshot, quit"
        )

    def select_tab(self, command):
        window = self.window()
        tabs = tab_items(window)
        if not tabs:
            raise CommandError("لا توجد تبويبات في النافذة")
        index = command.get("index")
        name = command.get("name")
        if isinstance(index, int):
            if not 0 <= index < len(tabs):
                raise CommandError("index خارج نطاق التبويبات")
            target = tabs[index]
        elif isinstance(name, str) and name:
            match = [tab for tab in tabs if name.casefold() in (tab.window_text() or "").casefold()]
            if not match:
                raise CommandError("لا يوجد تبويب بهذا الاسم")
            target = match[0]
        else:
            raise CommandError("حدد index أو name للتبويب")
        focus_window(window)
        try:
            target.select()
        except Exception:
            click_element(target)
        time.sleep(self.delay_ms / 1000)
        return {"selected": target.window_text()}

    def click(self, command):
        window = self.window()
        focus_window(window)
        x, y = command.get("x"), command.get("y")
        if not isinstance(x, int) or not isinstance(y, int):
            raise CommandError("click يتطلب إحداثيين x و y صحيحين")
        if command.get("relative", False):
            rectangle = window.rectangle()
            x, y = rectangle.left + x, rectangle.top + y
        button = command.get("button", "left")
        if button not in ("left", "right", "middle"):
            raise CommandError("button يجب أن يكون left أو right أو middle")
        mouse.move(coords=(x, y))
        time.sleep(0.05)
        mouse.click(button=button, coords=(x, y))
        time.sleep(self.delay_ms / 1000)
        return {"clicked": {"x": x, "y": y, "button": button}}

    def click_by_name(self, command):
        name = command.get("name")
        if not isinstance(name, str) or not name:
            raise CommandError("click-name يتطلب اسم عنصر")
        control_type = command.get("controlType")
        partial = bool(command.get("partial", False))
        window = self.window()
        focus_window(window)
        element = find_by_name(window, name, control_type, partial)
        if element is None:
            raise CommandError(
                f"لم أجد عنصرًا باسم {name}"
                + ("؛ جرّب partial=true أو النقر بالإحداثيات" if not partial else "")
            )
        click_element(element)
        return {"clicked": name}

    def fill(self, command):
        window = self.window()
        text = str(command.get("text", ""))
        clear = command.get("clear", True)
        name = command.get("name")
        if isinstance(name, str) and name:
            element = find_by_name(window, name, command.get("controlType"),
                                   bool(command.get("partial", False)))
            if element is None:
                raise CommandError(f"لم أجد عنصرًا باسم {name}")
        else:
            element = address_bar(window)
        type_into(element, text, clear=bool(clear))
        return {"typed": len(text), "into": (element.element_info.name or "address bar")}

    def send_hotkeys(self, command):
        window = self.window()
        keys = str(command.get("keys", ""))
        if not keys:
            raise CommandError("keys يتطلب نص مفاتيح مثل {ENTER} أو ^l")
        name = command.get("name")
        if isinstance(name, str) and name:
            element = find_by_name(window, name, command.get("controlType"),
                                   bool(command.get("partial", False)))
            if element is None:
                raise CommandError(f"لم أجد عنصرًا باسم {name}")
            try:
                element.click_input()
                element.type_keys(keys)
            except Exception as error:
                raise CommandError(f"تعذر إرسال المفاتيح ({error})") from error
        else:
            focus_window(window)
            send_keys(keys)
        time.sleep(self.delay_ms / 1000)
        return {"sent": keys}

    def scroll(self, command):
        window = self.window()
        focus_window(window)
        amount = command.get("amount", -600)
        if not isinstance(amount, int):
            raise CommandError("amount يجب أن يكون رقمًا صحيحًا")
        mouse.scroll(coords=(window.rectangle().left + window.rectangle().width() // 2,
                             window.rectangle().top + window.rectangle().height() // 2),
                     wheel_dist=int(amount))
        time.sleep(self.delay_ms / 1000)
        return {"scrolled": amount}

    def screenshot(self, command):
        raw_path = command.get("path", "orbita_window.png")
        target = Path(str(raw_path)).expanduser().resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        window = self.window()
        if window.is_minimized():
            raise CommandError("النافذة مصغرة؛ نفّذ focus أولًا")
        image = window.capture_as_image()
        image.save(target)
        return {"screenshot": str(target), "size": {"width": image.width, "height": image.height}}


def parse_command(raw_command):
    try:
        command = json.loads(raw_command)
    except json.JSONDecodeError as error:
        raise CommandError("صيغة JSON غير صالحة") from error
    if not isinstance(command, dict):
        raise CommandError("يجب أن يكون الأمر كائن JSON")
    return command


def serve_commands(session, source):
    emit_event({"event": "ready", "windows": [window_report(item)
                                              for item in orbita_windows(session.title_filter)]})
    for raw_command in source:
        if not raw_command.strip():
            continue
        try:
            command = parse_command(raw_command)
            if command.get("action") == "quit":
                emit_event({"event": "detaching"})
                return
            emit_event({"event": "result", **session.run(command)})
        except CommandError as error:
            emit_event({"event": "error", "message": str(error)})
        except Exception as error:
            emit_event({"event": "error", "message": f"{type(error).__name__}: {error}"})


def command_source(arguments):
    if arguments.commands is None:
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")
        return sys.stdin
    if not arguments.commands.is_file():
        raise SetupError("ملف الأوامر المحدد غير موجود")
    return arguments.commands.read_text(encoding="utf-8").splitlines()


def main():
    arguments = controller_arguments()
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    session = WindowSession(arguments.window, arguments.delay)
    try:
        source = command_source(arguments)
    except SetupError as error:
        print(f"تعذر قراءة الأوامر: {error}", file=sys.stderr)
        return 2
    try:
        serve_commands(session, source)
    except KeyboardInterrupt:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())