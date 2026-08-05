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
    args = parser.parse_args()

    job = OcrJob(page_count=args.pages)
    if args.pdf is not None:
        job = replace(job, pdf_path=args.pdf)
    if args.output is not None:
        job = replace(job, output_path=args.output)
    return job


def main() -> None:
    force_utf8_stdout()
    job = build_job_from_args()
    print(f"PDF: {job.pdf_path}")
    print(f"Output: {job.output_path}")
    report = run(job)
    print()
    print(quality.format_report(report))


if __name__ == "__main__":
    main()
