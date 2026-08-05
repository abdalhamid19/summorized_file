import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from arabic_pdf_ocr import quality
from arabic_pdf_ocr.config import DEFAULT_OUTPUT, force_utf8_stdout


def main() -> None:
    force_utf8_stdout()
    text = DEFAULT_OUTPUT.read_text(encoding="utf-8")
    report = quality.verify(text)
    print(quality.format_report(report))
    sys.exit(0 if report.is_high_quality else 1)


if __name__ == "__main__":
    main()
