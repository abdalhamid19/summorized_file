import os
import sys
import io
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv(PROJECT_ROOT / ".env")

MINICONDA_ROOT = Path(os.environ.get("MINICONDA_ROOT", r"C:\Users\QUANTUM\miniconda3"))
WORK_ROOT = Path(os.environ.get("OCR_WORK_ROOT", PROJECT_ROOT / "main_obsidian" / "دين" / "التزكية" / "البركة"))
TEMP_ROOT = Path(os.environ.get("OCR_TEMP_ROOT", r"C:\Users\QUANTUM\AppData\Local\Temp\opencode\ocr_tmp"))

DEFAULT_PDF = WORK_ROOT / "ar_Albarakah.pdf"
DEFAULT_OUTPUT = WORK_ROOT / "ar_Albarakah.md"

TESSERACT_EXE = MINICONDA_ROOT / "Library" / "bin" / "tesseract.exe"
TESSDATA_DIR = MINICONDA_ROOT / "Library" / "share" / "tessdata"

MISTRAL_API_KEY = os.environ.get("MISTRAL_API_KEY", "")
MISTRAL_MODEL = os.environ.get("MISTRAL_OCR_MODEL", "mistral-ocr-4-0")


def _parse_api_keys() -> tuple:
    raw = os.environ.get("MISTRAL_API_KEYS", "")
    keys = [k.strip() for k in raw.split(",") if k.strip()]
    if not keys and MISTRAL_API_KEY:
        keys = [MISTRAL_API_KEY]
    return tuple(dict.fromkeys(keys))


MISTRAL_API_KEYS = _parse_api_keys()

RENDER_ZOOM = 4
TESSERACT_LANGUAGE = "ara"
IMAGE_DPI = (300, 300)


@dataclass(frozen=True)
class OcrJob:
    pdf_path: Path = DEFAULT_PDF
    output_path: Path = DEFAULT_OUTPUT
    pages_dir: Path = field(default_factory=lambda: WORK_ROOT / "pages_png")
    temp_dir: Path = TEMP_ROOT
    page_count: int = 5
    skip_existing_renders: bool = True
    engine: str = "mistral"
    mistral_api_key: str = MISTRAL_API_KEY
    mistral_api_keys: tuple = MISTRAL_API_KEYS
    mistral_model: str = MISTRAL_MODEL


def force_utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower() == "utf-8":
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
