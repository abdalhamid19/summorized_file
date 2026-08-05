# summorized_file

## arabic_pdf_ocr

حزمة لاستخراج النص العربي من ملفات PDF ذات الخطوط المخصصة (CID) عبر OCR.

### الاستخدام

```bash
python -m arabic_pdf_ocr                          # الإعدادات الافتراضية (أول 5 صفحات)
python -m arabic_pdf_ocr --pages 10               # عدد صفحات مخصص
python -m arabic_pdf_ocr --pdf book.pdf --output book.md
python -m pytest tests\ -v                        # اختبارات الوحدة
python tests\test_quality.py                      # فحص جودة الناتج الحالي
```

### البنية

| الملف | المسؤولية |
|---|---|
| `config.py` | المسارات والثوابت و`OcrJob` |
| `renderer.py` | تحويل صفحات PDF إلى صور PNG (PyMuPDF) |
| `preprocessing.py` | تحسين الصور (تباين/حدة/تحويل ثنائي) |
| `ocr.py` | تشغيل Tesseract بأربع استراتيجيات متوازية واختيار الأفضل |
| `postprocessing.py` | تصحيح أخطاء OCR وتنقية الأسطر المشوهة |
| `quality.py` | التحقق من الجودة عبر عبارات معروفة ونسبة الكلمات العربية |
| `pipeline.py` | فحوصات ما قبل التشغيل + تنسيق الخطوات |

### المتطلبات

- Tesseract مع `ara.traineddata`: `conda install -c conda-forge tesseract`
- حزم Python: `pip install -r requirements.txt`

### متغيرات البيئة

| المتغير | الافتراضي |
|---|---|
| `MINICONDA_ROOT` | `C:\Users\QUANTUM\miniconda3` |
| `OCR_WORK_ROOT` | `main_obsidian/دين/التزكية/البركة` |
| `OCR_TEMP_ROOT` | `%TEMP%\opencode\ocr_tmp` |

## transcribe_audio.py

تفريغ صوتي عربي عبر Whisper API مع تقسيم الملفات الطويلة إلى مقاطع.
