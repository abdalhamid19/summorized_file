import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = PROJECT_ROOT / ".env"


def load_env() -> None:
    if not ENV_FILE.exists():
        return
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip())


load_env()

AUDIO_FILE = Path(os.environ.get(
    "AUDIO_FILE",
    str(PROJECT_ROOT / "audio_transcribe" / "نحو.mp3"),
))
WORK_DIR = Path(os.environ.get("AUDIO_WORK_DIR", str(PROJECT_ROOT / "audio_transcribe" / "work")))
OUTPUT_MD = Path(os.environ.get(
    "OUTPUT_MD",
    str(PROJECT_ROOT / "audio_transcribe" / "نحو.md"),
))

COHERE_API_KEY = os.environ.get("COHERE_API_KEY", "")
TRANSCRIBE_MODEL = os.environ.get("COHERE_TRANSCRIBE_MODEL", "cohere-transcribe-arabic-07-2026")
AUDIT_MODEL = os.environ.get("COHERE_AUDIT_MODEL", "command-a-03-2025")

TRANSCRIBE_URL = "https://api.cohere.com/v2/audio/transcriptions"
CHAT_URL = "https://api.cohere.com/v2/chat"

CHUNK_SECONDS = int(os.environ.get("CHUNK_SECONDS", "420"))
AUDIO_BITRATE = os.environ.get("AUDIO_BITRATE", "48k")
MAX_FILE_MB = 24
REQUEST_TIMEOUT = 600
MAX_RETRIES = 5
AUDIT_BLOCK_WORDS = int(os.environ.get("AUDIT_BLOCK_WORDS", "1500"))
