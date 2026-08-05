# summorized_file

## arabic_pdf_ocr

حزمة لاستخراج النص العربي من ملفات PDF ذات الخطوط المخصصة (CID) عبر OCR.

### الاستخدام

```bash
python -m arabic_pdf_ocr                          # الإعدادات الافتراضية (أول 5 صفحات)
python -m arabic_pdf_ocr --pages 10               # عدد صفحات مخصص
python -m arabic_pdf_ocr --pdf book.pdf --output book.md
python tests\test_quality.py                      # التحقق من جودة الناتج
```

### البنية

| الملف | المسؤولية |
|---|---|
| `config.py` | المسارات والثوابت و`OcrJob` |
| `renderer.py` | تحويل صفحات PDF إلى صور PNG (PyMuPDF) |
| `preprocessing.py` | تحسين الصور (تباين/حدة/تحويل ثنائي) |
| `ocr.py` | تشغيل Tesseract بأربع استراتيجيات واختيار الأفضل بالتقييم |
| `postprocessing.py` | تصحيح أخطاء OCR وتنقية الأسطر المشوهة |
| `quality.py` | التحقق من الجودة عبر عبارات معروفة ونسبة الكلمات العربية |
| `pipeline.py` | تنسيق الخطوات من PDF إلى Markdown |

### المتطلبات

- Tesseract مع `ara.traineddata` (يُثبَّت عبر `conda install -c conda-forge tesseract`)
- `pip install pymupdf pillow`

## transcribe_audio.py

تفريغ صوتي عربي عبر Whisper API مع تقسيم الملفات الطويلة إلى مقاطع.
