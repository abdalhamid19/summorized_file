from __future__ import annotations

import argparse
import ctypes
import json
import os
import sys
import time
from ctypes import wintypes
from pathlib import Path
from typing import Any


TOKEN_QUERY = 0x0008
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
TOKEN_ELEVATION = 20
TOKEN_INTEGRITY_LEVEL = 25
TOKEN_UI_ACCESS = 26


class SidAndAttributes(ctypes.Structure):
    _fields_ = [("sid", ctypes.c_void_p), ("attributes", wintypes.DWORD)]


class TokenMandatoryLabel(ctypes.Structure):
    _fields_ = [("label", SidAndAttributes)]


class UiAutomationError(Exception):
    pass


def _windows_apis() -> tuple[Any, Any]:
    if os.name != "nt":
        raise UiAutomationError("This script only runs on Windows.")

    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    advapi32 = ctypes.WinDLL("advapi32", use_last_error=True)
    kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
    kernel32.OpenProcess.restype = wintypes.HANDLE
    kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel32.CloseHandle.restype = wintypes.BOOL
    advapi32.OpenProcessToken.argtypes = [wintypes.HANDLE, wintypes.DWORD, ctypes.POINTER(wintypes.HANDLE)]
    advapi32.OpenProcessToken.restype = wintypes.BOOL
    advapi32.GetTokenInformation.argtypes = [
        wintypes.HANDLE,
        ctypes.c_int,
        ctypes.c_void_p,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.DWORD),
    ]
    advapi32.GetTokenInformation.restype = wintypes.BOOL
    advapi32.GetSidSubAuthorityCount.argtypes = [ctypes.c_void_p]
    advapi32.GetSidSubAuthorityCount.restype = ctypes.POINTER(ctypes.c_ubyte)
    advapi32.GetSidSubAuthority.argtypes = [ctypes.c_void_p, wintypes.DWORD]
    advapi32.GetSidSubAuthority.restype = ctypes.POINTER(wintypes.DWORD)
    return kernel32, advapi32


def _token_information(advapi32: Any, token: wintypes.HANDLE, info_class: int) -> ctypes.Array[Any]:
    size = wintypes.DWORD()
    advapi32.GetTokenInformation(token, info_class, None, 0, ctypes.byref(size))
    if not size.value:
        raise ctypes.WinError(ctypes.get_last_error())

    buffer = ctypes.create_string_buffer(size.value)
    if not advapi32.GetTokenInformation(token, info_class, buffer, size.value, ctypes.byref(size)):
        raise ctypes.WinError(ctypes.get_last_error())
    return buffer


def _token_dword(advapi32: Any, token: wintypes.HANDLE, info_class: int) -> int:
    buffer = _token_information(advapi32, token, info_class)
    return ctypes.cast(buffer, ctypes.POINTER(wintypes.DWORD)).contents.value


def _integrity_rid(advapi32: Any, token: wintypes.HANDLE) -> int:
    buffer = _token_information(advapi32, token, TOKEN_INTEGRITY_LEVEL)
    label = ctypes.cast(buffer, ctypes.POINTER(TokenMandatoryLabel)).contents
    sid = label.label.sid
    subauthority_count = advapi32.GetSidSubAuthorityCount(sid).contents.value
    if subauthority_count == 0:
        raise UiAutomationError("The process token did not contain an integrity level.")
    return advapi32.GetSidSubAuthority(sid, subauthority_count - 1).contents.value


def _integrity_name(rid: int) -> str:
    if rid < 0x1000:
        return "Untrusted"
    if rid < 0x2000:
        return "Low"
    if rid < 0x2100:
        return "Medium"
    if rid < 0x3000:
        return "Medium+"
    if rid < 0x4000:
        return "High"
    if rid < 0x5000:
        return "System"
    return "Protected"


def process_security(pid: int) -> dict[str, Any]:
    kernel32, advapi32 = _windows_apis()
    process = kernel32.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    if not process:
        raise ctypes.WinError(ctypes.get_last_error())

    token = wintypes.HANDLE()
    try:
        if not advapi32.OpenProcessToken(process, TOKEN_QUERY, ctypes.byref(token)):
            raise ctypes.WinError(ctypes.get_last_error())
        rid = _integrity_rid(advapi32, token)
        return {
            "pid": pid,
            "integrity": _integrity_name(rid),
            "integrity_rid": rid,
            "elevated": bool(_token_dword(advapi32, token, TOKEN_ELEVATION)),
            "ui_access": bool(_token_dword(advapi32, token, TOKEN_UI_ACCESS)),
        }
    finally:
        if token:
            kernel32.CloseHandle(token)
        kernel32.CloseHandle(process)


def _safe_value(callable_value: Any, default: Any = None) -> Any:
    try:
        return callable_value()
    except Exception:
        return default


def _window_data(window: Any) -> dict[str, Any]:
    info = window.element_info
    return {
        "title": _safe_value(lambda: window.window_text(), ""),
        "pid": _safe_value(lambda: int(info.process_id)),
        "hwnd": _safe_value(lambda: int(window.handle)),
        "control_type": _safe_value(lambda: info.control_type),
        "visible": _safe_value(lambda: bool(window.is_visible()), False),
        "enabled": _safe_value(lambda: bool(window.is_enabled()), False),
    }


def _desktop() -> Any:
    try:
        from pywinauto import Desktop
    except ImportError as exc:
        requirements_path = Path(__file__).resolve().with_name("requirements-windows-ui-automation.txt")
        install_command = f'"{sys.executable}" -m pip install -r "{requirements_path}"'
        raise UiAutomationError(
            f"pywinauto is missing. Install the pinned dependency with: {install_command}"
        ) from exc
    return Desktop(backend="uia")


def list_windows(include_hidden: bool) -> list[dict[str, Any]]:
    windows: list[dict[str, Any]] = []
    for window in _desktop().windows(top_level_only=True):
        data = _window_data(window)
        if include_hidden or (data["visible"] and data["title"].strip()):
            windows.append(data)
    return sorted(windows, key=lambda item: (str(item["title"]).casefold(), item["pid"] or 0))


def select_window(args: argparse.Namespace) -> Any:
    if args.pid is None and args.title is None:
        raise UiAutomationError("Choose one target with --pid or the exact window --title.")
    if args.pid is not None and args.title is not None:
        raise UiAutomationError("Use either --pid or --title, not both.")
    if args.window_title and args.pid is None:
        raise UiAutomationError("--window-title can only be used together with --pid.")

    candidates = []
    for window in _desktop().windows(top_level_only=True):
        data = _window_data(window)
        if not data["visible"] or not data["title"].strip():
            continue
        if args.pid is not None and data["pid"] != args.pid:
            continue
        if args.title is not None and data["title"] != args.title:
            continue
        if args.window_title is not None and data["title"] != args.window_title:
            continue
        candidates.append(window)

    if not candidates:
        raise UiAutomationError("No visible top-level UIA window matched the target. Use list-windows to inspect current windows.")
    if len(candidates) > 1:
        matches = [_window_data(window) for window in candidates]
        raise UiAutomationError("The target matched multiple windows; narrow it with --window-title. Matches: " + json.dumps(matches, ensure_ascii=True))
    return candidates[0]


def check_integrity(target_pids: list[int]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    current = process_security(os.getpid())
    targets = [process_security(pid) for pid in sorted(set(target_pids))]
    higher = [target for target in targets if target["integrity_rid"] > current["integrity_rid"]]
    if higher:
        target_levels = ", ".join(f"PID {item['pid']} is {item['integrity']}" for item in higher)
        raise UiAutomationError(
            f"Permission boundary: this script is {current['integrity']}; {target_levels}. "
            "No partial inspection or action was returned. Start a separate PowerShell process with Run as administrator, "
            "approve the UAC prompt, then run this script there. The script never elevates itself."
        )
    return current, targets


def element_data(element: Any) -> dict[str, Any]:
    info = element.element_info
    rect = _safe_value(lambda: info.rectangle)
    bounds = None
    if rect is not None:
        bounds = {
            "left": rect.left,
            "top": rect.top,
            "right": rect.right,
            "bottom": rect.bottom,
        }
    return {
        "name": _safe_value(lambda: info.name, ""),
        "control_type": _safe_value(lambda: info.control_type, ""),
        "automation_id": _safe_value(lambda: info.automation_id, ""),
        "class_name": _safe_value(lambda: info.class_name, ""),
        "pid": _safe_value(lambda: int(info.process_id)),
        "hwnd": _safe_value(lambda: int(info.handle)),
        "visible": _safe_value(lambda: bool(element.is_visible()), False),
        "enabled": _safe_value(lambda: bool(element.is_enabled()), False),
        "bounds": bounds,
    }


def inspect_tree(window: Any, depth: int, limit: int) -> tuple[dict[str, Any], int, bool]:
    state = {"count": 0, "truncated": False}

    def build(element: Any, level: int) -> dict[str, Any]:
        if state["count"] >= limit:
            state["truncated"] = True
            return {}
        state["count"] += 1
        node = element_data(element)
        node["children"] = []
        if level < depth and state["count"] < limit:
            try:
                children = element.children()
            except Exception:
                children = []
                state["truncated"] = True
            for child in children:
                if state["count"] >= limit:
                    state["truncated"] = True
                    break
                node["children"].append(build(child, level + 1))
        elif level < depth:
            state["truncated"] = True
        return node

    tree = build(window, 0)
    return tree, state["count"], state["truncated"]


def find_elements(window: Any, selector: str, selector_value: str, control_type: str | None) -> list[Any]:
    matches = []
    for element in window.descendants():
        info = element.element_info
        actual_value = _safe_value(lambda: getattr(info, selector), "")
        actual_type = _safe_value(lambda: info.control_type, "")
        if actual_value != selector_value:
            continue
        if control_type and str(actual_type).casefold() != control_type.casefold():
            continue
        matches.append(element)
    return matches


def validate_click_bounds(element: dict[str, Any]) -> None:
    bounds = element.get("bounds")
    if not bounds or bounds["right"] <= bounds["left"] or bounds["bottom"] <= bounds["top"]:
        raise UiAutomationError("The selected element has no usable screen rectangle; no click was run.")

    user32 = ctypes.WinDLL("user32", use_last_error=True)
    user32.GetSystemMetrics.argtypes = [ctypes.c_int]
    user32.GetSystemMetrics.restype = ctypes.c_int
    left = user32.GetSystemMetrics(76)
    top = user32.GetSystemMetrics(77)
    right = left + user32.GetSystemMetrics(78)
    bottom = top + user32.GetSystemMetrics(79)
    center_x = (bounds["left"] + bounds["right"]) // 2
    center_y = (bounds["top"] + bounds["bottom"]) // 2
    if not (left <= center_x < right and top <= center_y < bottom):
        raise UiAutomationError("The element center is outside the current desktop; no click was run.")


def foreground_window_handle() -> int:
    user32 = ctypes.WinDLL("user32", use_last_error=True)
    user32.GetForegroundWindow.argtypes = []
    user32.GetForegroundWindow.restype = wintypes.HWND
    return int(user32.GetForegroundWindow() or 0)


def ensure_target_foreground(window: Any, window_info: dict[str, Any], activate: bool) -> dict[str, Any]:
    target_handle = int(window_info["hwnd"])
    foreground_before = foreground_window_handle()
    activated = False

    if foreground_before != target_handle:
        if not activate:
            raise UiAutomationError(
                f"The target window is not in the foreground (foreground HWND {foreground_before}; "
                f"target HWND {target_handle}); no click was sent. Use --activate-window to focus it explicitly."
            )
        try:
            window.set_focus()
        except Exception as exc:
            raise UiAutomationError(f"Could not activate the target window; no click was sent: {type(exc).__name__}: {exc}") from exc

        deadline = time.monotonic() + 2.0
        while time.monotonic() < deadline:
            if foreground_window_handle() == target_handle:
                activated = True
                break
            time.sleep(0.05)

        foreground_after = foreground_window_handle()
        if foreground_after != target_handle:
            raise UiAutomationError(
                f"The target window could not be verified in the foreground (foreground HWND {foreground_after}; "
                f"target HWND {target_handle}); no click was sent."
            )
    else:
        foreground_after = foreground_before

    return {
        "foreground_before_hwnd": foreground_before,
        "foreground_after_hwnd": foreground_after,
        "target_hwnd": target_handle,
        "activated": activated,
        "verified": foreground_after == target_handle,
    }


def get_unique_element(window: Any, args: argparse.Namespace, prefix: str = "") -> Any:
    name = getattr(args, f"{prefix}name", None)
    automation_id = getattr(args, f"{prefix}automation_id", None)
    if bool(name) == bool(automation_id):
        raise UiAutomationError(f"Choose exactly one selector: --{prefix.replace('_', '-') }name or --{prefix.replace('_', '-') }automation-id.")
    selector = "name" if name else "automation_id"
    value = name if name else automation_id
    control_type = getattr(args, f"{prefix}control_type", None)
    matches = find_elements(window, selector, value, control_type)
    if not matches:
        raise UiAutomationError(f"No UIA element matched {selector}={value!r}. Inspect the tree and use an exact selector.")
    if len(matches) > 1:
        details = [element_data(element) for element in matches[:20]]
        raise UiAutomationError(f"The selector is ambiguous ({len(matches)} matches). Add --control-type or use --automation-id. Matches: {json.dumps(details, ensure_ascii=True)}")
    return matches[0]


def add_target_arguments(parser: argparse.ArgumentParser) -> None:
    target = parser.add_mutually_exclusive_group(required=False)
    target.add_argument("--pid", type=int, help="PID (process ID) of the process that owns the window")
    target.add_argument("--title", help="Exact, case-sensitive top-level window title")
    parser.add_argument("--window-title", help="Exact title to disambiguate windows for --pid")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect one Windows app window through UI Automation. Output is JSON; inspection is read-only.",
        epilog=(
            "Examples:\n"
            "  python \"Windows UIA Automation.py\" list-windows\n"
            "  python \"Windows UIA Automation.py\" inspect --pid 12345 --depth 3\n"
            "  python \"Windows UIA Automation.py\" invoke --pid 12345 --name Settings --dry-run\n"
            "  python \"Windows UIA Automation.py\" invoke --pid 12345 --name Settings --confirm --expect-name General\n\n"
            "Exit codes: 0 success; 1 UI/runtime failure; 2 invalid or unsafe request; 3 expected UI state not verified."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version="Windows UIA Automation 1.0.0")
    commands = parser.add_subparsers(dest="command", required=True)

    windows = commands.add_parser("list-windows", help="List visible UIA windows")
    windows.add_argument("--include-hidden", action="store_true", help="Include hidden or untitled top-level windows")

    inspect = commands.add_parser("inspect", help="Read a bounded UIA tree without querying value properties")
    add_target_arguments(inspect)
    inspect.add_argument("--depth", type=int, default=3)
    inspect.add_argument("--limit", type=int, default=300, help="Maximum number of elements to return")

    for command in ("invoke", "click"):
        action = commands.add_parser(command, help="Perform one explicitly confirmed action on one unique element")
        add_target_arguments(action)
        selector = action.add_mutually_exclusive_group(required=True)
        selector.add_argument("--name", help="Exact UIA Name (accessible label) of the element")
        selector.add_argument("--automation-id", help="Exact UIA AutomationId of the element")
        action.add_argument("--control-type", help="Optional exact type, such as Button or TabItem")
        expected = action.add_mutually_exclusive_group()
        expected.add_argument("--expect-name", help="Wait for this exact UIA Name after the action")
        expected.add_argument("--expect-automation-id", help="Wait for this exact AutomationId after the action")
        action.add_argument("--expect-control-type", help="Optional exact type for the expected element")
        action.add_argument("--timeout", type=float, default=5.0, help="Seconds to wait for an expected element")
        action.add_argument("--confirm", action="store_true", help="Confirm this one UI action")
        action.add_argument("--dry-run", action="store_true", help="Resolve and validate the action without executing it")
        action.add_argument(
            "--activate-window",
            action="store_true",
            help="For click, focus and verify the target window before sending screen-coordinate input",
        )

    return parser


def validate_request(args: argparse.Namespace) -> None:
    if args.command == "inspect":
        if args.depth < 0 or args.depth > 12:
            raise UiAutomationError("--depth must be between 0 and 12.")
        if args.limit < 1 or args.limit > 5000:
            raise UiAutomationError("--limit must be between 1 and 5000.")

    if args.command in ("invoke", "click"):
        if args.confirm and args.dry_run:
            raise UiAutomationError("Choose either --confirm or --dry-run, not both.")
        if not args.confirm and not args.dry_run:
            raise UiAutomationError("No action was run. Add --confirm to authorize this single UI action.")
        if args.timeout < 0 or args.timeout > 60:
            raise UiAutomationError("--timeout must be between 0 and 60 seconds.")
        if args.expect_control_type and not (args.expect_name or args.expect_automation_id):
            raise UiAutomationError("--expect-control-type requires --expect-name or --expect-automation-id.")
        if args.dry_run and (args.expect_name or args.expect_automation_id):
            raise UiAutomationError("Expected post-action selectors are not used with --dry-run.")
        if args.activate_window and args.command != "click":
            raise UiAutomationError("--activate-window can only be used with click.")


def inspect_target(window: Any, window_info: dict[str, Any], depth: int, limit: int) -> dict[str, Any]:
    tree, count, truncated = inspect_tree(window, depth, limit)
    process_ids = {window_info["pid"]}

    def collect_process_ids(node: dict[str, Any]) -> None:
        if node.get("pid") is not None:
            process_ids.add(int(node["pid"]))
        for child in node.get("children", []):
            collect_process_ids(child)

    collect_process_ids(tree)
    current_security, target_processes = check_integrity(list(process_ids))
    return {
        "mode": "read-only",
        "controller": current_security,
        "target_processes": target_processes,
        "window": window_info,
        "element_count": count,
        "truncated": truncated,
        "integrity_scan_scope": "processes represented in the returned tree",
        "tree": tree,
    }


def verify_expected_state(
    args: argparse.Namespace,
    window_info: dict[str, Any],
    before: dict[str, Any],
    current_security: dict[str, Any],
    target_processes: list[dict[str, Any]],
) -> tuple[dict[str, Any], dict[str, Any], list[dict[str, Any]]]:
    expected_name = args.expect_name
    expected_id = args.expect_automation_id
    if not expected_name and not expected_id:
        return {"requested": False}, current_security, target_processes

    selector = "name" if expected_name else "automation_id"
    value = expected_name or expected_id
    deadline = time.monotonic() + args.timeout
    matches: list[Any] = []
    while True:
        try:
            refreshed_window = select_window(args)
            matches = find_elements(refreshed_window, selector, value, args.expect_control_type)
        except Exception:
            matches = []
        if len(matches) == 1:
            expected_element = element_data(matches[0])
            known_pids = {item["pid"] for item in target_processes}
            if expected_element["pid"] not in known_pids:
                try:
                    current_security, target_processes = check_integrity(
                        [window_info["pid"], before["pid"], expected_element["pid"]]
                    )
                except Exception as exc:
                    return {
                        "requested": True,
                        "matched": False,
                        "reason": f"expected state could not be safely verified: {type(exc).__name__}: {exc}",
                    }, current_security, target_processes
            return {"requested": True, "matched": True, "element": expected_element}, current_security, target_processes
        if time.monotonic() >= deadline:
            return {
                "requested": True,
                "matched": False,
                "match_count": len(matches),
                "expected_selector": selector,
                "expected_value": value,
            }, current_security, target_processes
        time.sleep(0.15)


def run_action(args: argparse.Namespace, window: Any, window_info: dict[str, Any]) -> dict[str, Any]:
    element = get_unique_element(window, args)
    before = element_data(element)
    if before["pid"] is None:
        raise UiAutomationError("Could not determine the selected element's process ID; no action was run.")
    current_security, target_processes = check_integrity([window_info["pid"], before["pid"]])
    if not before["visible"] or not before["enabled"]:
        raise UiAutomationError("The selected element is not both visible and enabled; no action was run.")
    focus = None
    if args.command == "click":
        if args.dry_run:
            validate_click_bounds(before)
            foreground_handle = foreground_window_handle()
            focus = {
                "foreground_hwnd": foreground_handle,
                "target_hwnd": window_info["hwnd"],
                "target_is_foreground": foreground_handle == window_info["hwnd"],
                "activation_requested": args.activate_window,
            }
        else:
            focus = ensure_target_foreground(window, window_info, args.activate_window)
            element = get_unique_element(window, args)
            before = element_data(element)
            if before["pid"] is None:
                raise UiAutomationError("Could not determine the selected element's process ID; no click was sent.")
            current_security, target_processes = check_integrity([window_info["pid"], before["pid"]])
            if not before["visible"] or not before["enabled"]:
                raise UiAutomationError("The selected element is not both visible and enabled; no click was sent.")
            validate_click_bounds(before)
            foreground_before_dispatch = foreground_window_handle()
            if foreground_before_dispatch != int(window_info["hwnd"]):
                raise UiAutomationError(
                    f"The target lost foreground before click dispatch (foreground HWND {foreground_before_dispatch}; "
                    f"target HWND {window_info['hwnd']}); no click was sent."
                )
            focus["foreground_before_dispatch_hwnd"] = foreground_before_dispatch
            focus["verified_at_dispatch"] = True

    if args.dry_run:
        result = {
            "mode": "dry-run",
            "action": args.command,
            "action_dispatched": False,
            "controller": current_security,
            "target_processes": target_processes,
            "window": window_info,
            "selected_element": before,
        }
        if focus is not None:
            result["focus"] = focus
        return result

    if args.command == "invoke":
        element.invoke()
    else:
        element.click_input()

    verification, current_security, target_processes = verify_expected_state(
        args, window_info, before, current_security, target_processes
    )

    result = {
        "mode": "one-action",
        "action": args.command,
        "controller": current_security,
        "target_processes": target_processes,
        "window": window_info,
        "selected_element_before": before,
        "action_dispatched": True,
        "verification": verification,
    }
    if focus is not None:
        result["focus"] = focus
    return result


def run(args: argparse.Namespace) -> dict[str, Any]:
    if args.command == "list-windows":
        return {"windows": list_windows(args.include_hidden)}

    validate_request(args)
    window = select_window(args)
    window_info = _window_data(window)
    if window_info["pid"] is None:
        raise UiAutomationError("Could not determine the selected window's process ID.")
    if args.command == "inspect":
        return inspect_target(window, window_info, args.depth, args.limit)
    return run_action(args, window, window_info)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = run(args)
    except UiAutomationError as exc:
        print(
            json.dumps(
                {"ok": False, "schema_version": 1, "error": {"code": "UIA_REQUEST_FAILED", "message": str(exc)}},
                ensure_ascii=True,
            ),
            file=sys.stderr,
        )
        return 2
    except Exception as exc:
        print(
            json.dumps(
                {
                    "ok": False,
                    "schema_version": 1,
                    "error": {"code": "UIA_RUNTIME_FAILURE", "message": f"{type(exc).__name__}: {exc}"},
                },
                ensure_ascii=True,
            ),
            file=sys.stderr,
        )
        return 1

    verification = result.get("verification", {})
    verification_failed = (
        args.command in ("invoke", "click")
        and verification.get("requested")
        and not verification.get("matched")
    )
    print(
        json.dumps(
            {"ok": not verification_failed, "schema_version": 1, "data": result},
            ensure_ascii=True,
            indent=2,
        )
    )
    if verification_failed:
        print("WARNING: The action was sent, but the requested UI state was not verified.", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
