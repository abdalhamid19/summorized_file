# AGENTS.md

## أوامر أساسية

```bash
python -m arabic_pdf_ocr                      # OCR كامل عبر Mistral (الافتراضي، 5 صفحات)
python -m arabic_pdf_ocr --pages 10           # عدد صفحات مخصص
python -m arabic_pdf_ocr --engine tesseract   # محرك Tesseract المحلي (احتياطي)
python -m pytest tests\ -v                    # تشغيل الاختبارات
python tests\test_quality.py                  # فحص جودة الناتج الحالي
```

## المتطلبات

- **Mistral OCR (أساسي)**: `MISTRAL_API_KEYS` (مفصولة بفواصل، تبديل تلقائي عند فشل أي مفتاح) في البيئة أو `.env`. النموذج `mistral-ocr-4-0` (لا تستخدم `mistral-ocr-latest` — مكسور).
- Tesseract مع `ara.traineddata` (احتياطي): `conda install -c conda-forge tesseract`
- حزم Python: `pip install -r requirements.txt`

## بنية المشروع

- `arabic_pdf_ocr/` — حزمة OCR (config / renderer / preprocessing / ocr / mistral_engine / postprocessing / quality / pipeline)
- `tests/` — اختبارات الوحدة وفحص الجودة
- `transcribe_audio.py` — تفريغ صوتي عبر Whisper API
- `main_obsidian/` — ملفات العمل (PDF + النواتج)

## قواعد

- لا تضف تعليقات إلا بطلب صريح.
- المسارات تُضبط عبر متغيرات البيئة: `MINICONDA_ROOT`, `OCR_WORK_ROOT`, `OCR_TEMP_ROOT`, `MISTRAL_API_KEY`, `MISTRAL_OCR_MODEL`.
