from pathlib import Path

from PIL import Image, ImageEnhance, ImageOps

from .config import IMAGE_DPI

CONTRAST_FACTOR = 1.5
SHARPNESS_FACTOR = 1.3
AUTOCONTRAST_CUTOFF_ENHANCE = 1
AUTOCONTRAST_CUTOFF_BINARIZE = 2
BINARIZE_THRESHOLD = 160
DESKEW_MAX_ANGLE = 3.0
DESKEW_DELTA = 0.5


def _load_grayscale(source: Path) -> Image.Image:
    return Image.open(source).convert("L")


def _projection_score(image: Image.Image) -> float:
    width, height = image.size
    pixels = image.load()
    score = 0.0
    for y in range(height):
        row_ink = sum(1 for x in range(0, width, 4) if pixels[x, y] < 128)
        if y > 0:
            score += abs(row_ink - prev_ink)
        prev_ink = row_ink
    return score


def deskew(image: Image.Image) -> Image.Image:
    best_angle = 0.0
    best_score = -1.0
    angle = -DESKEW_MAX_ANGLE
    while angle <= DESKEW_MAX_ANGLE + 1e-9:
        rotated = image.rotate(angle, resample=Image.BICUBIC, expand=False, fillcolor=255)
        score = _projection_score(rotated)
        if score > best_score:
            best_score = score
            best_angle = angle
        angle += DESKEW_DELTA
    if abs(best_angle) < 0.25:
        return image
    return image.rotate(best_angle, resample=Image.BICUBIC, expand=False, fillcolor=255)


def enhance(source: Path, destination: Path) -> Path:
    image = ImageOps.autocontrast(_load_grayscale(source), cutoff=AUTOCONTRAST_CUTOFF_ENHANCE)
    image = deskew(image)
    image = ImageEnhance.Contrast(image).enhance(CONTRAST_FACTOR)
    image = ImageEnhance.Sharpness(image).enhance(SHARPNESS_FACTOR)
    image.save(destination, dpi=IMAGE_DPI)
    return destination


def binarize(source: Path, destination: Path) -> Path:
    image = ImageOps.autocontrast(_load_grayscale(source), cutoff=AUTOCONTRAST_CUTOFF_BINARIZE)
    image = deskew(image)
    image = image.point(lambda pixel: 255 if pixel > BINARIZE_THRESHOLD else 0)
    image.save(destination, dpi=IMAGE_DPI)
    return destination
