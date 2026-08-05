import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from arabic_pdf_ocr import postprocessing, quality
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
