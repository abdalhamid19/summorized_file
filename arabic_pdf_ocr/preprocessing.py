from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

from .config import IMAGE_DPI

CONTRAST_FACTOR = 1.5
SHARPNESS_FACTOR = 1.3
AUTOCONTRAST_CUTOFF_ENHANCE = 1
AUTOCONTRAST_CUTOFF_BINARIZE = 2
BINARIZE_THRESHOLD = 160


def _load_grayscale(source: Path) -> Image.Image:
    return Image.open(source).convert("L")


def enhance(source: Path, destination: Path) -> Path:
    image = ImageOps.autocontrast(_load_grayscale(source), cutoff=AUTOCONTRAST_CUTOFF_ENHANCE)
    image = ImageEnhance.Contrast(image).enhance(CONTRAST_FACTOR)
    image = ImageEnhance.Sharpness(image).enhance(SHARPNESS_FACTOR)
    image.save(destination, dpi=IMAGE_DPI)
    return destination


def binarize(source: Path, destination: Path) -> Path:
    image = ImageOps.autocontrast(_load_grayscale(source), cutoff=AUTOCONTRAST_CUTOFF_BINARIZE)
    image = image.point(lambda pixel: 255 if pixel > BINARIZE_THRESHOLD else 0)
    image.save(destination, dpi=IMAGE_DPI)
    return destination
