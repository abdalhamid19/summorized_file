import argparse
import os
import sys
from typing import List
from .extractor import YouTubeTranscriptExtractor
from .formatters import TranscriptFormatter
from .utils import ensure_dir, sanitize_filename


def configure_system_streams() -> None:
    """Configures stdout/stderr encodings for cross-platform compatibility."""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            try:
                stream.reconfigure(encoding="utf-8")
            except Exception:
                pass


def build_argument_parser() -> argparse.ArgumentParser:
    """Constructs and returns the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="YouTube Transcript Extractor - أداة استخراج التفريغ النصي من فيديوهات يوتيوب"
    )
    parser.add_argument("url", help="رابط فيديو يوتيوب أو معرف الفيديو (URL or Video ID)")
    parser.add_argument(
        "-f",
        "--format",
        choices=["txt", "json", "srt", "md"],
        default="txt",
        help="صيغة الملف الناتج (txt, json, srt, md)",
    )
    parser.add_argument(
        "-l",
        "--lang",
        default="ar,en",
        help="اللغات المفضلة بالترتيب مفصولة بفاصلة (مثال: ar,en)",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        default="output",
        help="المجلد الناتج لحفظ ملفات التفريغ (افتراضي: output/)",
    )
    parser.add_argument(
        "--list-langs",
        action="store_true",
        help="عرض اللغات المتوفرة للفيديو فقط دون استخراج",
    )
    return parser


def parse_language_preferences(lang_str: str) -> List[str]:
    """Splits comma-separated language strings into a clean list."""
    return [lang.strip() for lang in lang_str.split(",") if lang.strip()]


def display_available_languages(extractor: YouTubeTranscriptExtractor) -> None:
    """Fetches and displays available languages for the video."""
    print("🔍 جاري فحص اللغات المتاحة للفيديو...")
    languages = extractor.list_languages()
    if not languages:
        print("⚠️ لم يتم العثور على لغات تفريغ متوفرة عبر API.")
        return

    print("📋 اللغات المتاحة:")
    for item in languages:
        source_label = "توليد تلقائي" if item["is_generated"] else "يدوي"
        print(f"  - [{item['language_code']}] {item['language']} ({source_label})")


def save_transcript_file(
    content: str, output_dir: str, title: str, file_format: str
) -> str:
    """Saves formatted transcript string to disk and returns absolute path."""
    ensure_dir(output_dir)
    filename = f"{sanitize_filename(title)}.{file_format}"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    return os.path.abspath(output_path)


def process_extraction(extractor: YouTubeTranscriptExtractor, args: argparse.Namespace) -> None:
    """Executes full transcript extraction, formatting, and saving."""
    print("🔄 جاري جلب معلومات الفيديو والتفريغ النصي...")
    metadata = extractor.fetch_metadata()
    title = metadata.get("title", f"video_{extractor.video_id}")
    print(f"🎬 عنوان الفيديو: {title}")

    preferred_languages = parse_language_preferences(args.lang)
    transcript = extractor.get_transcript(preferred_languages)
    print(f"✅ تم جلب {len(transcript)} مقطع نصي بنجاح.")

    formatted_content = TranscriptFormatter.format(
        fmt=args.format,
        transcript=transcript,
        title=title,
        video_id=extractor.video_id,
    )

    abs_path = save_transcript_file(
        content=formatted_content,
        output_dir=args.output_dir,
        title=title,
        file_format=args.format.lower(),
    )

    print("🎉 تم حفظ التفريغ النصي بنجاح في:")
    print(f"📁 {abs_path}")


def main() -> None:
    configure_system_streams()
    parser = build_argument_parser()
    args = parser.parse_args()

    try:
        extractor = YouTubeTranscriptExtractor(args.url)
        print(f"📌 معرف الفيديو (Video ID): {extractor.video_id}")

        if args.list_langs:
            display_available_languages(extractor)
            return

        process_extraction(extractor, args)

    except Exception as error:
        print(f"❌ خطأ: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

