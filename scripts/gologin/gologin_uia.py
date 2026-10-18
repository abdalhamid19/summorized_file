import argparse
import json
import re
import sys
import time

from pywinauto import Application, Desktop


EMAIL_PATTERN = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")
LONG_NUMBER_PATTERN = re.compile(r"\b\d{6,}\b")
SENSITIVE_CONTROL_TYPES = {"Edit", "ComboBox", "Document", "Password"}


def clean_name(control):
    info = control.element_info
    if info.control_type in SENSITIVE_CONTROL_TYPES:
        return "[value omitted]"
    name = info.name or ""
    name = EMAIL_PATTERN.sub("[email redacted]", name)
    return LONG_NUMBER_PATTERN.sub("[number redacted]", name)


def get_window():
    candidates = []
    for control in Desktop(backend="uia").windows(visible_only=True):
        try:
            info = control.element_info
            if re.search(r"gologin", info.name or "", re.IGNORECASE):
                candidates.append(control)
        except Exception:
            continue
    if not candidates:
        raise RuntimeError("No visible GoLogin window was found.")
    target = candidates[0]
    app = Application(backend="uia").connect(process=target.element_info.process_id)
    window = app.window(handle=target.handle)
    window.wait("exists visible ready", timeout=15)
    return window.wrapper_object()


def inspect(limit):
    window = get_window()
    controls = window.descendants()
    rows = []
    for index, control in enumerate(controls):
        if len(rows) >= limit:
            break
        try:
            info = control.element_info
            if not control.is_visible():
                continue
            rect = control.rectangle()
            rows.append(
                {
                    "index": index,
                    "control_type": info.control_type,
                    "name": clean_name(control),
                    "auto_id": EMAIL_PATTERN.sub("[email redacted]", info.automation_id or ""),
                    "class_name": info.class_name or "",
                    "enabled": control.is_enabled(),
                    "rect": {
                        "left": rect.left,
                        "top": rect.top,
                        "right": rect.right,
                        "bottom": rect.bottom,
                    },
                }
            )
        except Exception:
            rows.append(
                {
                    "index": index,
                    "control_type": "unavailable",
                    "name": "",
                    "auto_id": "",
                    "class_name": "",
                    "enabled": False,
                    "rect": None,
                }
            )
    result = {
        "status": "tree-read",
        "window_title": window.element_info.name,
        "process_id": window.element_info.process_id,
        "window_handle": window.handle,
        "total_controls": len(controls),
        "returned_controls": len(rows),
        "sensitive_values_read": False,
        "controls": rows,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def visible_controls(window):
    for control in window.descendants():
        try:
            if control.is_visible():
                yield control
        except Exception:
            continue


def control_row(index, control):
    info = control.element_info
    rect = control.rectangle()
    return {
        "index": index,
        "control_type": info.control_type,
        "name": clean_name(control),
        "auto_id": EMAIL_PATTERN.sub("[email redacted]", info.automation_id or ""),
        "enabled": control.is_enabled(),
        "rect": {
            "left": rect.left,
            "top": rect.top,
            "right": rect.right,
            "bottom": rect.bottom,
        },
    }


def account_area_group(window):
    for control in visible_controls(window):
        try:
            info = control.element_info
            rect = control.rectangle()
            if (
                info.control_type == "Group"
                and 5 <= rect.left <= 20
                and 40 <= rect.top <= 60
                and 200 <= rect.width() <= 250
                and 30 <= rect.height() <= 50
            ):
                return control
        except Exception:
            continue
    return None


def menu_snapshot(window):
    rows = []
    for index, control in enumerate(visible_controls(window)):
        try:
            row = control_row(index, control)
            rect = row["rect"]
            if row["name"] and rect["left"] < 340 and rect["top"] < 520:
                rows.append(row)
        except Exception:
            continue
        if len(rows) >= 80:
            break
    return rows


def open_account_menu():
    window = get_window()
    target = account_area_group(window)
    if target is None:
        print(json.dumps({"status": "account-control-not-found"}, ensure_ascii=False, indent=2))
        return 2
    target.click_input()
    deadline = time.monotonic() + 5
    rows = []
    while time.monotonic() < deadline:
        rows = menu_snapshot(window)
        if any(re.search(r"\b(log\s?out|sign\s?out|logout|signout)\b", row["name"], re.I) for row in rows):
            print(json.dumps({"status": "account-menu-open", "controls": rows}, ensure_ascii=False, indent=2))
            return 0
        time.sleep(0.25)
    print(json.dumps({"status": "menu-not-confirmed", "controls": rows}, ensure_ascii=False, indent=2))
    return 1


def sign_out():
    window = get_window()
    target = None
    for control in visible_controls(window):
        try:
            info = control.element_info
            name = clean_name(control).strip()
            if info.control_type in {"Button", "MenuItem", "Text"} and re.fullmatch(
                r"(?:log\s?out|sign\s?out|logout|signout)", name, re.I
            ):
                target = control
                break
        except Exception:
            continue
    if target is None:
        print(json.dumps({"status": "sign-out-control-not-found", "controls": menu_snapshot(window)}, ensure_ascii=False, indent=2))
        return 2
    target.click_input()
    deadline = time.monotonic() + 15
    last_rows = []
    while time.monotonic() < deadline:
        last_rows = menu_snapshot(window)
        names = " ".join(row["name"] for row in last_rows)
        if re.search(r"\b(sign\s?in|log\s?in|welcome back)\b", names, re.I):
            print(json.dumps({"status": "login-screen-visible", "controls": last_rows}, ensure_ascii=False, indent=2))
            return 0
        if re.search(r"\b(cancel|confirm|are you sure)\b", names, re.I):
            print(json.dumps({"status": "confirmation-screen-visible", "controls": last_rows}, ensure_ascii=False, indent=2))
            return 1
        time.sleep(0.3)
    print(json.dumps({"status": "sign-out-result-unconfirmed", "controls": last_rows}, ensure_ascii=False, indent=2))
    return 1


def sign_up_snapshot(window):
    rows = []
    for index, control in enumerate(visible_controls(window)):
        try:
            row = control_row(index, control)
            if row["name"] and re.search(
                r"sign\s?up|create|register|email|password|already have|terms|continue",
                row["name"],
                re.I,
            ):
                rows.append(row)
        except Exception:
            continue
        if len(rows) >= 80:
            break
    return rows


def open_sign_up():
    window = get_window()
    target = None
    for control in visible_controls(window):
        try:
            info = control.element_info
            name = clean_name(control).strip()
            if info.control_type == "Hyperlink" and re.search(
                r"sign\s?up", name, re.I
            ):
                target = control
                break
        except Exception:
            continue
    if target is None:
        print(json.dumps({"status": "sign-up-link-not-found"}, ensure_ascii=False, indent=2))
        return 2
    target.click_input()
    deadline = time.monotonic() + 12
    rows = []
    while time.monotonic() < deadline:
        rows = sign_up_snapshot(window)
        title = EMAIL_PATTERN.sub("[email redacted]", window.element_info.name or "")
        if re.search(r"sign\s?up|create account|register", title, re.I) or any(
            re.search(r"create account|already have|terms", row["name"], re.I)
            for row in rows
        ):
            print(json.dumps({"status": "sign-up-form-visible", "window_title": title, "controls": rows}, ensure_ascii=False, indent=2))
            return 0
        time.sleep(0.3)
    print(json.dumps({"status": "sign-up-form-not-confirmed", "window_title": window.element_info.name, "controls": rows}, ensure_ascii=False, indent=2))
    return 1


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    inspect_parser = subparsers.add_parser("inspect")
    inspect_parser.add_argument("--limit", type=int, default=500)
    subparsers.add_parser("open-account-menu")
    subparsers.add_parser("sign-out")
    subparsers.add_parser("open-sign-up")
    args = parser.parse_args()
    if args.command == "inspect" and args.limit < 1:
        parser.error("--limit must be at least 1")
    try:
        if args.command == "inspect":
            inspect(args.limit)
        elif args.command == "open-account-menu":
            return open_account_menu()
        elif args.command == "open-sign-up":
            return open_sign_up()
        else:
            return sign_out()
    except Exception as exc:
        print(f"GoLogin UI inspection failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
