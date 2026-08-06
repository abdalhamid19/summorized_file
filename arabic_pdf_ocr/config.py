import os
import sys
import io
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MINICONDA_ROOT = Path(os.environ.get("MINICONDA_ROOT", r"C:\Users\QUANTUM\miniconda3"))
WORK_ROOT = Path(os.environ.get("OCR_WORK_ROOT", PROJECT_ROOT / "main_obsidian" / "دين" / "التزكية" / "البركة"))
TEMP_ROOT = Path(os.environ.get("OCR_TEMP_ROOT", r"C:\Users\QUANTUM\AppData\Local\Temp\opencode\ocr_tmp"))

DEFAULT_PDF = WORK_ROOT / "ar_Albarakah.pdf"
DEFAULT_OUTPUT = WORK_ROOT / "ar_Albarakah.md"

TESSERACT_EXE = MINICONDA_ROOT / "Library" / "bin" / "tesseract.exe"
TESSDATA_DIR = MINICONDA_ROOT / "Library" / "share" / "tessdata"

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


def force_utf8_stdout() -> None:
    if sys.stdout.encoding and sys.stdout.encoding.lower() == "utf-8":
        return
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
