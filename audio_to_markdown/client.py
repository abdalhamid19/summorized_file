import time
from pathlib import Path

import requests

from . import config

RETRYABLE_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
BASE_WAIT_SECONDS = 5
MAX_WAIT_SECONDS = 120
ERROR_BODY_PREVIEW_CHARS = 300


class RequestFailedError(RuntimeError):
    pass


def backoff_seconds(attempt: int) -> int:
    return min(2 ** attempt * BASE_WAIT_SECONDS, MAX_WAIT_SECONDS)


def is_retryable(status_code: int) -> bool:
    return status_code in RETRYABLE_STATUS_CODES


def post_with_retry(
    url: str,
    *,
    headers: dict,
    payload: dict = None,
    upload_path: Path = None,
    upload_fields: dict = None,
    description: str,
) -> dict:
    for attempt in range(1, config.MAX_RETRIES + 1):
        try:
            response = _send_once(
                url, headers=headers, payload=payload,
                upload_path=upload_path, upload_fields=upload_fields,
            )
        except requests.RequestException as exc:
            _wait_before_retry(attempt, f"Network error ({exc})")
            continue
        if response.status_code == 200:
            return response.json()
        if is_retryable(response.status_code):
            _wait_before_retry(attempt, f"HTTP {response.status_code} ({description})")
            continue
        raise RequestFailedError(f"API error {response.status_code}: {response.text[:ERROR_BODY_PREVIEW_CHARS]}")
    raise RequestFailedError(f"Request failed after {config.MAX_RETRIES} retries: {description}")


def _send_once(
    url: str,
    *,
    headers: dict,
    payload: dict,
    upload_path: Path,
    upload_fields: dict,
) -> requests.Response:
    if upload_path is not None:
        with open(upload_path, "rb") as audio:
            files = {"file": (upload_path.name, audio, "audio/mpeg")}
            return requests.post(
                url, headers=headers, files=files, data=upload_fields,
                timeout=config.REQUEST_TIMEOUT,
            )
    return requests.post(url, headers=headers, json=payload, timeout=config.REQUEST_TIMEOUT)


def _wait_before_retry(attempt: int, reason: str) -> None:
    wait = backoff_seconds(attempt)
    print(f"  {reason}, retry {attempt}/{config.MAX_RETRIES} in {wait}s")
    time.sleep(wait)
