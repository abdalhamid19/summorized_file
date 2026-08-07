import base64
import json
import urllib.error
import urllib.request
from pathlib import Path

from .ocr import OcrCandidate

MISTRAL_API_URL = "https://api.mistral.ai/v1/ocr"
DEFAULT_MODEL = "mistral-ocr-4-0"
TIMEOUT_SECONDS = 120

RETRYABLE_STATUS = {401, 403, 408, 409, 429, 500, 502, 503, 504}


class MistralOcrError(RuntimeError):
    pass


def is_configured(api_key) -> bool:
    if isinstance(api_key, (list, tuple)):
        return any(k and k.strip() for k in api_key)
    return bool(api_key and api_key.strip())


def _encode_image(image_path: Path) -> str:
    return base64.b64encode(image_path.read_bytes()).decode("ascii")


def _request(image_path: Path, api_key: str, model: str) -> dict:
    payload = {
        "model": model,
        "document": {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{_encode_image(image_path)}",
        },
    }
    request = urllib.request.Request(
        MISTRAL_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        error = MistralOcrError(f"HTTP {exc.code}: {detail[:200]}")
        error.status = exc.code
        raise error from exc
    except urllib.error.URLError as exc:
        error = MistralOcrError(f"فشل الاتصال: {exc.reason}")
        error.status = None
        raise error from exc


def ocr_page(image_path: Path, api_keys, model: str = DEFAULT_MODEL) -> OcrCandidate:
    keys = [k for k in (api_keys if isinstance(api_keys, (list, tuple)) else [api_keys]) if k and k.strip()]
    if not keys:
        raise MistralOcrError("لا توجد مفاتيح MISTRAL_API_KEYS مضبوطة")

    last_error = None
    for index, key in enumerate(keys):
        try:
            body = _request(image_path, key, model)
            pages = body.get("pages") or []
            text = "\n\n".join(page.get("markdown", "") for page in pages).strip()
            suffix = f" (مفتاح {index + 1})" if len(keys) > 1 else ""
            return OcrCandidate(name=f"mistral_{model}{suffix}", text=text, score=0, low_confidence_words=())
        except MistralOcrError as exc:
            last_error = exc
            if exc.status in RETRYABLE_STATUS and index < len(keys) - 1:
                print(f"    [تبديل] المفتاح {index + 1} فشل (HTTP {exc.status}) — تجربة التالي")
                continue
            raise

    raise last_error or MistralOcrError("فشلت كل المفاتيح")
