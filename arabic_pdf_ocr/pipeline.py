from . import ocr, postprocessing, quality, renderer
from .config import OcrJob, TESSERACT_EXE

PAGE_HEADER = "# الصفحة"


def preflight_check(job: OcrJob) -> None:
    if not job.pdf_path.exists():
        raise FileNotFoundError(f"ملف PDF غير موجود: {job.pdf_path}")
    if not TESSERACT_EXE.exists():
        raise FileNotFoundError(
            f"Tesseract غير موجود: {TESSERACT_EXE}\n"
            "ثبّته عبر: conda install -c conda-forge tesseract"
        )


def run(job: OcrJob) -> quality.QualityReport:
    preflight_check(job)
    image_paths = renderer.render_pdf_pages(job.pdf_path, job.pages_dir, job.page_count)

    markdown_pages = []
    for page_number, image_path in enumerate(image_paths, start=1):
        best = ocr.ocr_page(image_path, job.temp_dir, page_number)
        print(f"  page {page_number}: best={best.name} score={best.score}")
        cleaned = postprocessing.postprocess(best.text)
        markdown_pages.append(f"{PAGE_HEADER} {page_number}\n\n{cleaned}")

    job.output_path.write_text("\n".join(markdown_pages), encoding="utf-8")
    return quality.verify(job.output_path.read_text(encoding="utf-8"))
