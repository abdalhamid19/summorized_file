import os
import sys
import argparse
from .extractor import YouTubeTranscriptExtractor
from .formatters import TranscriptFormatter
from .utils import sanitize_filename, ensure_dir

def main():
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    if hasattr(sys.stderr, "reconfigure"):
        try:
            sys.stderr.reconfigure(encoding="utf-8")
        except Exception:
            pass

    parser = argparse.ArgumentParser(
        description="YouTube Transcript Extractor - أداة استخراج التفريغ النصي من فيديوهات يوتيوب"
    )
    parser.add_argument("url", help="رابط فيديو يوتيوب أو معرف الفيديو (URL or Video ID)")
    parser.add_argument(
        "-f", "--format",
        choices=["txt", "json", "srt", "md"],
        default="txt",
        help="صيغة الملف الناتج (txt, json, srt, md)"
    )
    parser.add_argument(
        "-l", "--lang",
        default="ar,en",
        help="اللغات المفضلة بالترتيب مفصولة بفاصلة (مثال: ar,en)"
    )
    parser.add_argument(
        "-o", "--output-dir",
        default="output",
        help="المجلد الناتج لحفظ ملفات التفريغ (افتراضي: output/)"
    )
    parser.add_argument(
        "--list-langs",
        action="store_true",
        help="عرض اللغات المتوفرة للفيديو فقط دون استخراج"
    )

    args = parser.parse_args()

    try:
        extractor = YouTubeTranscriptExtractor(args.url)
        print(f"📌 معرف الفيديو (Video ID): {extractor.video_id}")

        if args.list_langs:
            print("🔍 جاري فحص اللغات المتاحة للفيديو...")
            langs = extractor.list_languages()
            if not langs:
                print("⚠️ لم يتم العثور على لغات تفريغ متوفرة عبر API.")
            else:
                print("📋 اللغات المتاحة:")
                for l in langs:
                    gen_str = "توليد تلقائي" if l['is_generated'] else "يدوي"
                    print(f"  - [{l['language_code']}] {l['language']} ({gen_str})")
            return

        print("🔄 جاري جلب معلومات الفيديو والتفريغ النصي...")
        metadata = extractor.fetch_metadata()
        title = metadata.get("title", f"video_{extractor.video_id}")
        print(f"🎬 عنوان الفيديو: {title}")

        preferred_languages = [lang.strip() for lang in args.lang.split(",") if lang.strip()]
        transcript = extractor.get_transcript(preferred_languages)

        print(f"✅ تم جلب {len(transcript)} مقطع نصي بنجاح.")

        # Formatting
        fmt = args.format.lower()
        if fmt == "json":
            content = TranscriptFormatter.to_json(transcript, title=title, video_id=extractor.video_id)
        elif fmt == "srt":
            content = TranscriptFormatter.to_srt(transcript)
        elif fmt == "md":
            content = TranscriptFormatter.to_markdown(transcript, title=title, video_id=extractor.video_id)
        else:
            content = TranscriptFormatter.to_txt(transcript, title=title, video_id=extractor.video_id)

        # Save to file
        ensure_dir(args.output_dir)
        filename = f"{sanitize_filename(title)}.{fmt}"
        output_path = os.path.join(args.output_dir, filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"🎉 تم حفظ التفريغ النصي بنجاح في:")
        print(f"📁 {os.path.abspath(output_path)}")

    except Exception as e:
        print(f"❌ خطأ: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
