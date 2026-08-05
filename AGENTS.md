# AGENTS.md

## أوامر أساسية

```bash
python -m arabic_pdf_ocr                      # تشغيل OCR كامل (5 صفحات افتراضياً)
python -m arabic_pdf_ocr --pages 10           # عدد صفحات مخصص
python -m pytest tests\ -v                    # تشغيل الاختبارات
python tests\test_quality.py                  # فحص جودة الناتج الحالي
```

## المتطلبات

- Tesseract مع `ara.traineddata`: `conda install -c conda-forge tesseract`
- حزم Python: `pip install -r requirements.txt`

## بنية المشروع

- `arabic_pdf_ocr/` — حزمة OCR (config / renderer / preprocessing / ocr / postprocessing / quality / pipeline)
- `tests/` — اختبارات الوحدة وفحص الجودة
- `transcribe_audio.py` — تفريغ صوتي عبر Whisper API
- `main_obsidian/` — ملفات العمل (PDF + النواتج)

## قواعد

- لا تضف تعليقات إلا بطلب صريح.
- المسارات تُضبط عبر متغيرات البيئة: `MINICONDA_ROOT`, `OCR_WORK_ROOT`, `OCR_TEMP_ROOT`.
