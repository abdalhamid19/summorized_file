import base64
import json
import urllib.error
import urllib.request
from pathlib import Path

from .ocr import OcrCandidate

MISTRAL_API_URL = "https://api.mistral.ai/v1/ocr"
DEFAULT_MODEL = "mistral-ocr-4-0"
TIMEOUT_SECONDS = 120


class MistralOcrError(RuntimeError):
    pass


def is_configured(api_key: str) -> bool:
    return bool(api_key and api_key.strip())


def _encode_image(image_path: Path) -> str:
    return base64.b64encode(image_path.read_bytes()).decode("ascii")


def ocr_page(image_path: Path, api_key: str, model: str = DEFAULT_MODEL) -> OcrCandidate:
    if not is_configured(api_key):
        raise MistralOcrError("MISTRAL_API_KEY غير مضبوط")
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
            body = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise MistralOcrError(f"HTTP {exc.code}: {detail[:200]}") from exc
    except urllib.error.URLError as exc:
        raise MistralOcrError(f"فشل الاتصال: {exc.reason}") from exc

    pages = body.get("pages") or []
    text = "\n\n".join(page.get("markdown", "") for page in pages).strip()
    return OcrCandidate(name=f"mistral_{model}", text=text, score=0, low_confidence_words=())
