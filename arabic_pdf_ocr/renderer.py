from pathlib import Path

import fitz

from .config import RENDER_ZOOM


def render_pdf_pages(pdf_path: Path, pages_dir: Path, page_count: int, zoom: int = RENDER_ZOOM) -> list[Path]:
    pages_dir.mkdir(parents=True, exist_ok=True)
    image_paths = []
    with fitz.open(pdf_path) as document:
        matrix = fitz.Matrix(zoom, zoom)
        for index in range(min(page_count, len(document))):
            pixmap = document[index].get_pixmap(matrix=matrix)
            image_path = pages_dir / f"page_{index + 1}.png"
            pixmap.save(image_path)
            image_paths.append(image_path)
    return image_paths
