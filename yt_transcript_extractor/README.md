# YouTube Transcript Extractor (أداة استخراج تفريغ فيديوهات يوتيوب)

أداة احترافية باللغة العربية والإنجليزية لاستخراج التفريغ النصي (Subtitles / Transcript) من أي فيديو يوتيوب مع دعم خيارات التنسيق المتعددة (TXT, JSON, SRT, Markdown) والبحث التلقائي عن اللغات المتاحة.

## 🚀 المميزات
- استخراج التفريغ النصي من فيديوهات يوتيوب بجميع اللغات المتوفرة (يدوية أو توليد تلقائي).
- استخراج التوقيتات وتنسيق الوقت بصيغ دقيقة (`MM:SS` أو `HH:MM:SS`).
- دعم التصدير بصيغ مختلفة: `TXT`, `JSON`, `SRT`, `Markdown`.
- دعم واجهة السطر البرمجي (CLI) سهلة الاستخدام.
- معالجة تلقائية واستراتيجية fallback باستخدام `youtube-transcript-api` و `yt-dlp`.

## 📦 التثبيت والاستخدام
```bash
pip install -r requirements.txt
python -m yt_transcript_extractor.cli "https://www.youtube.com/watch?v=N1H-2WthmsQ" --format md --lang ar
```
