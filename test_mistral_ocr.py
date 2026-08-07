import json
import os
import sys
import urllib.request
import urllib.error

BASE = "https://api.mistral.ai/v1"
OCR_MODELS = [
    "mistral-ocr-2503",
    "mistral-ocr-2505",
    "mistral-ocr-2512",
    "mistral-ocr-4-0",
    "mistral-ocr-latest",
]

TINY_PNG_B64 = (
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
)


def _req(path, key, payload=None):
    url = BASE + path
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, dict(r.headers), json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode()
        except Exception:
            body = ""
        return e.code, dict(e.headers), body


def check_models(key):
    status, headers, body = _req("/models", key)
    if status != 200:
        return None, status, body
    ids = {m.get("id") for m in body.get("data", [])}
    return ids, status, body


def probe_ocr(key, model):
    payload = {
        "model": model,
        "document": {
            "type": "image_url",
            "image_url": f"data:image/png;base64,{TINY_PNG_B64}",
        },
    }
    status, headers, body = _req("/ocr", key, payload)
    info = {"model": model, "http": status}
    if status == 200:
        info["result"] = "OK — يعمل"
        pages = body.get("pages", [])
        info["pages"] = len(pages)
    else:
        try:
            msg = json.loads(body).get("message", body) if isinstance(body, str) else body
        except Exception:
            msg = body
        info["result"] = f"فشل — {msg}"
    for h in ("x-ratelimit-limit-page", "x-ratelimit-remaining-page",
              "x-ratelimit-limit", "x-ratelimit-remaining",
              "x-ratelimit-limit-requests", "x-ratelimit-remaining-requests"):
        for k, v in headers.items():
            if k.lower() == h:
                info[h] = v
    return info


def main():
    key = os.environ.get("MISTRAL_API_KEY", "").strip()
    if not key:
        print(json.dumps({"error": "MISTRAL_API_KEY missing"}, ensure_ascii=False))
        sys.exit(2)

    report = {"auth": "ok", "models_listed": None, "ocr": []}

    ids, status, body = check_models(key)
    if ids is None:
        report["auth"] = f"failed http={status}: {str(body)[:200]}"
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(1)
    report["models_listed"] = sorted(m for m in ids if "ocr" in m.lower())

    for m in OCR_MODELS:
        report["ocr"].append(probe_ocr(key, m))

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
