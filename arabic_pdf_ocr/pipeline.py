from . import benchmark, ocr, postprocessing, quality, quran_fix, renderer, spellfix
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
    image_paths = renderer.render_pdf_pages(
        job.pdf_path,
        job.pages_dir,
        job.page_count,
        skip_existing=job.skip_existing_renders,
    )

    markdown_pages = []
    review = []
    for page_number, image_path in enumerate(image_paths, start=1):
        best = ocr.ocr_page(image_path, job.temp_dir, page_number)
        print(f"  page {page_number}: best={best.name} score={best.score} low_conf={len(best.low_confidence_words)}")
        cleaned = postprocessing.postprocess(best.text)
        cleaned = quran_fix.fix_cited_verses(cleaned)
        cleaned = quran_fix.fix_inline_citations(cleaned)
        markdown_pages.append(f"{PAGE_HEADER} {page_number}\n\n{cleaned}")
        if best.low_confidence_words:
            sample = ", ".join(f"{w.text}({w.confidence:.0f})" for w in best.low_confidence_words[:8])
            review.append(f"- صفحة {page_number}: {len(best.low_confidence_words)} كلمة ضعيفة — {sample}")

    full_text = "\n".join(markdown_pages)
    corrected, suggestions = spellfix.correct(full_text)
    job.output_path.write_text(corrected, encoding="utf-8")

    review_path = job.output_path.with_name(job.output_path.stem + "_review.md")
    report_lines = [
        "# تقرير المراجعة",
        "",
        f"## آيات القرآن (CER)",
        benchmark.format_cer_report(benchmark.check_verses(corrected)),
        "",
        f"## تصحيحات إملائية مقترحة ({len(suggestions)})",
    ]
    report_lines += [f"- {k} → {v}" for k, v in list(suggestions.items())[:50]]
    report_lines += ["", "## صفحات تحتاج مراجعة (ثقة منخفضة)"]
    report_lines += review if review else ["- لا شيء"]
    review_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    return quality.verify(corrected)
