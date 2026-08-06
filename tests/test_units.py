import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from arabic_pdf_ocr import postprocessing, quality, quran_db, benchmark, quran_fix, spellfix
from arabic_pdf_ocr.ocr import score_text


class TestPostprocessing:
    def test_fixes_split_ta_marbuta(self):
        assert "المقدمة" in postprocessing.postprocess("المقدم ة")

    def test_fixes_joined_words(self):
        assert "جاء ذكرها" in postprocessing.postprocess("جاءذكرها")

    def test_fixes_taala_corruption(self):
        assert "تعسالى" not in postprocessing.postprocess("قال تعسالى شيء")

    def test_removes_junk_lines(self):
        result = postprocessing.postprocess("نص عربي سليم وجيد\nغٍِ\nنص آخر جيد")
        assert "غٍِ" not in result
        assert "نص عربي سليم وجيد" in result

    def test_replaces_known_verse_alaraf(self):
        text = "قال تعالى: ل( وَلَوَ أن هل الْقرّئ ءَامَنُواً عله بركتو [ الأعراف:46] ."
        result = postprocessing.postprocess(text)
        assert "﴿وَلَوْ أَنَّ أَهْلَ الْقُرَىٰ آمَنُوا" in result
        assert "[الأعراف: ٩٦]" in result

    def test_replaces_known_verse_nuh(self):
        text = "ومن ذلك الاستغفار . قال تعالى: فقلت آستغفروا ربكم [ نوح ]."
        result = postprocessing.postprocess(text)
        assert "﴿فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ" in result

    def test_collapses_blank_lines(self):
        result = postprocessing.postprocess("سطر أول جيد\n\n\n\n\nسطر ثان جيد")
        assert "\n\n\n" not in result

    def test_strips_invisible_marks(self):
        result = postprocessing.postprocess("نص\u200f عربي\u200e جيد\ufeff")
        assert "\u200f" not in result and "\u200e" not in result

    def test_prophet_symbol_كن(self):
        result = postprocessing.postprocess("من حياة النبي كن وأصحابه")
        assert "كن" not in result
        assert "أصحابه" in result

    def test_prophet_symbol_number(self):
        result = postprocessing.postprocess("عن النبي 48 قال")
        assert "48" not in result

    def test_digit_noise_line_removed(self):
        result = postprocessing.postprocess("نص جيد\nار 3 2 9 7 2 مي اي\nنص آخر")
        assert "3 2 9 7 2" not in result

    def test_heavy_tashkeel_stripped(self):
        dense = "بَآَرَكُ الله لك وَيَأَرَكَ عَلَيْكَ"
        result = postprocessing.postprocess(dense)
        assert "\u064b" not in result or result.count("\u064b") < dense.count("\u064b")


class TestScoreText:
    def test_empty_scores_zero(self):
        assert score_text("") == 0
        assert score_text("   ") == 0

    def test_arabic_scores_higher_than_junk(self):
        assert score_text("الحمد لله رب العالمين") > score_text("!@#$%^&*()")

    def test_known_phrase_bonus(self):
        base = score_text("نص عربي طويل للاختبار فقط")
        with_phrase = score_text("نص عربي طويل للاختبار فقط البركة")
        assert with_phrase > base


class TestQualityVerify:
    def test_full_text_passes(self):
        text = (
            "بسم الله الرحمن الرحيم الحمد لله رب العالمين محمد البركة "
            "الأعراف الاستغفار مباحث الرسالة أمين الشقاوي حقوق الطبع "
            "صلة الأرحام تعريف البركة موانع البركة"
        )
        report = quality.verify(text)
        assert report.passed_checks == report.total_checks
        assert report.is_high_quality

    def test_missing_phrase_fails(self):
        report = quality.verify("نص عربي لا يحتوي شيئاً من المطلوب")
        assert report.passed_checks < report.total_checks
        assert not report.is_high_quality

    def test_report_format_mentions_counts(self):
        report = quality.verify("البركة")
        formatted = quality.format_report(report)
        assert "النتيجة" in formatted and "نسبة" in formatted


class TestQuranDb:
    def test_verse_lookup(self):
        assert quran_db.verse(7, 96) is not None
        assert "ٱتَّقَو" in quran_db.verse(7, 96)

    def test_parse_arabic_digits(self):
        assert quran_db.parse_reference("الأعراف: ٩٦") == (7, 96)
        assert quran_db.parse_reference("نوح: 10") == (71, 10)

    def test_parse_invalid(self):
        assert quran_db.parse_reference("كتاب: 5") is None
        assert quran_db.parse_reference("بدون نقطتين") is None

    def test_verse_by_reference(self):
        assert quran_db.verse_by_reference("الأعراف: ٩٦") is not None


class TestBenchmark:
    def test_cer_zero_for_identical(self):
        ref = quran_db.verse(7, 96)
        assert benchmark.character_error_rate(ref, ref) == 0.0

    def test_cer_high_for_different(self):
        ref = quran_db.verse(7, 96)
        assert benchmark.character_error_rate(ref, "نص مختلف تماما") > 0.5


class TestQuranFix:
    def test_replaces_cited_verse(self):
        text = "قال تعالى ﴿ولو ان اهل القرى امنوا﴾ [الأعراف: ٩٦]."
        fixed = quran_fix.fix_cited_verses(text)
        assert "ٱتَّقَو" in fixed or "اتقو" in fixed

    def test_keeps_unknown_citation(self):
        text = "﴿شيء ما هنا﴾ [كتاب: ٥]."
        assert quran_fix.fix_cited_verses(text) == text


class TestSpellfix:
    def test_edit_distance_one(self):
        assert spellfix._edit_distance_one("البركة", "البركه")
        assert not spellfix._edit_distance_one("البركة", "مختلف")

    def test_no_false_corrections(self):
        text = " ".join(["البركة"] * 30)
        _, suggestions = spellfix.correct(text)
        assert suggestions == {}

