import os
import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

from . import preprocessing
from .config import TESSDATA_DIR, TESSERACT_EXE, TESSERACT_LANGUAGE

ARABIC_CHAR_PATTERN = re.compile(r"[\u0600-\u06FF]")
JUNK_CHAR_PATTERN = re.compile(r"[^\u0600-\u06FF\s0-9٠-٩a-zA-Z.,;:؟!،؛«»\-\(\)\[\]/﴿﴾۝]")

KNOWN_PHRASES = (
    "الحمد لله",
    "البركة",
    "قال تعالى",
    "المقدمة",
    "مباحث الرسالة",
    "بسم الله",
    "أمين بن عبدالله",
    "حقوق الطبع",
)

ARABIC_SCORE_WEIGHT = 2
JUNK_SCORE_WEIGHT = 5
PHRASE_BONUS = 50
MAX_PARALLEL_STRATEGIES = 4

STRATEGIES = (
    ("enh_psm3", "enhanced", 3),
    ("enh_psm6", "enhanced", 6),
    ("bin_psm3", "binarized", 3),
    ("orig_psm3", "source", 3),
)


@dataclass(frozen=True)
class OcrCandidate:
    name: str
    text: str
    score: int


def _tesseract_env() -> dict:
    env = os.environ.copy()
    env["TESSDATA_PREFIX"] = str(TESSDATA_DIR)
    return env


def run_tesseract(image_path: Path, output_base: Path, page_segmentation_mode: int) -> str:
    result = subprocess.run(
        [str(TESSERACT_EXE), str(image_path), str(output_base), "-l", TESSERACT_LANGUAGE, "--psm", str(page_segmentation_mode)],
        env=_tesseract_env(),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode != 0:
        return ""
    text_path = output_base.with_suffix(".txt")
    if not text_path.exists():
        return ""
    return text_path.read_text(encoding="utf-8")


def score_text(text: str) -> int:
    if not text.strip():
        return 0
    arabic_chars = len(ARABIC_CHAR_PATTERN.findall(text))
    junk_chars = len(JUNK_CHAR_PATTERN.findall(text))
    word_count = len(text.split())
    phrase_bonus = sum(PHRASE_BONUS for phrase in KNOWN_PHRASES if phrase in text)
    return arabic_chars * ARABIC_SCORE_WEIGHT - junk_chars * JUNK_SCORE_WEIGHT + word_count + phrase_bonus


def _ascii_safe_copy(source: Path, temp_dir: Path, page_number: int) -> Path:
    destination = temp_dir / f"page_{page_number}_src.png"
    shutil.copy2(source, destination)
    return destination


def _prepare_images(source: Path, temp_dir: Path, page_number: int) -> dict:
    return {
        "enhanced": preprocessing.enhance(source, temp_dir / f"page_{page_number}_enh.png"),
        "binarized": preprocessing.binarize(source, temp_dir / f"page_{page_number}_bin.png"),
        "source": source,
    }


def _run_strategy(name: str, image: Path, psm: int, temp_dir: Path, page_number: int) -> OcrCandidate:
    text = run_tesseract(image, temp_dir / f"{name}_{page_number}", psm)
    return OcrCandidate(name=name, text=text, score=score_text(text))


def ocr_page(image_path: Path, temp_dir: Path, page_number: int) -> OcrCandidate:
    temp_dir.mkdir(parents=True, exist_ok=True)
    source = _ascii_safe_copy(image_path, temp_dir, page_number)
    images = _prepare_images(source, temp_dir, page_number)

    with ThreadPoolExecutor(max_workers=MAX_PARALLEL_STRATEGIES) as executor:
        futures = [
            executor.submit(_run_strategy, name, images[variant], psm, temp_dir, page_number)
            for name, variant, psm in STRATEGIES
        ]
        candidates = [future.result() for future in futures]

    return max(candidates, key=lambda candidate: candidate.score)
