from pathlib import Path

import fitz

from .config import RENDER_ZOOM


def render_pdf_pages(
    pdf_path: Path,
    pages_dir: Path,
    page_count: int,
    zoom: int = RENDER_ZOOM,
    skip_existing: bool = True,
) -> list[Path]:
    pages_dir.mkdir(parents=True, exist_ok=True)
    image_paths = []
    with fitz.open(pdf_path) as document:
        total = min(page_count, len(document))
        matrix = fitz.Matrix(zoom, zoom)
        for index in range(total):
            image_path = pages_dir / f"page_{index + 1}.png"
            if skip_existing and image_path.exists() and image_path.stat().st_size > 0:
                image_paths.append(image_path)
                continue
            pixmap = document[index].get_pixmap(matrix=matrix)
            pixmap.save(image_path)
            image_paths.append(image_path)
    return image_paths
