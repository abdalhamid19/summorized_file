import argparse
from dataclasses import replace
from pathlib import Path

from . import quality
from .config import OcrJob, force_utf8_stdout
from .pipeline import run


def build_job_from_args() -> OcrJob:
    parser = argparse.ArgumentParser(prog="arabic_pdf_ocr")
    parser.add_argument("--pdf", type=Path, default=None)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--pages", type=int, default=5)
    parser.add_argument("--engine", choices=["mistral", "tesseract"], default="mistral",
                        help="محرك OCR الأساسي (الافتراضي mistral)")
    parser.add_argument("--mistral-model", default=None, help="مثال: mistral-ocr-4-0")
    parser.add_argument("--force-render", action="store_true", help="أعد تصيير الصفحات حتى إن وُجدت")
    args = parser.parse_args()

    job = OcrJob(page_count=args.pages, skip_existing_renders=not args.force_render, engine=args.engine)
    if args.pdf is not None:
        job = replace(job, pdf_path=args.pdf)
    if args.output is not None:
        job = replace(job, output_path=args.output)
    if args.mistral_model is not None:
        job = replace(job, mistral_model=args.mistral_model)
    return job


def main() -> int:
    force_utf8_stdout()
    job = build_job_from_args()
    print(f"PDF: {job.pdf_path}")
    print(f"Output: {job.output_path}")
    report = run(job)
    print()
    print(quality.format_report(report))
    return 0 if report.is_high_quality else 1


if __name__ == "__main__":
    raise SystemExit(main())
