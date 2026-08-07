import re
from dataclasses import dataclass

EXPECTED_PHRASES = {
    "بسم الله / البسملة": lambda t: any(x in t for x in ("بسم", "الرحمن", "الرحيم")),
    "الحمد لله رب العالمين": lambda t: "الحمد لله" in t and "العالمين" in t,
    "محمد": lambda t: "محمد" in t,
    "البركة": lambda t: "البركة" in t,
    "الأعراف": lambda t: "الأعراف" in t,
    "نوح / الاستغفار": lambda t: "الاستغفار" in t or "نوح" in t,
    "المقدمة / مباحث": lambda t: "مباحث" in t or "المقدمة" in t,
    "أمين بن عبدالله": lambda t: "أمين" in t and "الشقاوي" in t,
    "حقوق الطبع": lambda t: "حقوق الطبع" in t,
    "صلة الأرحام": lambda t: "الأرحام" in t,
    "مباحث الرسالة": lambda t: "مباحث الرسالة" in t,
    "تعريف البركة": lambda t: "تعريف البركة" in t,
    "موانع البركة": lambda t: "موانع البركة" in t,
}

ARABIC_LETTER = re.compile(r"[؀-ۿ]")
DIACRITICS = re.compile(r"[ً-ْٰـ]")
MIN_ARABIC_WORD_RATIO = 0.85


def _strip_diacritics(text: str) -> str:
    return DIACRITICS.sub("", text)


@dataclass(frozen=True)
class QualityReport:
    phrase_results: dict
    arabic_word_ratio: float
    line_count: int
    word_count: int

    @property
    def passed_checks(self) -> int:
        return sum(self.phrase_results.values())

    @property
    def total_checks(self) -> int:
        return len(self.phrase_results)

    @property
    def is_high_quality(self) -> bool:
        return self.passed_checks == self.total_checks and self.arabic_word_ratio >= MIN_ARABIC_WORD_RATIO


def verify(text: str) -> QualityReport:
    normalized = _strip_diacritics(text)
    phrase_results = {name: check(normalized) for name, check in EXPECTED_PHRASES.items()}
    lines = [line for line in text.split("\n") if line.strip() and not line.startswith("#")]
    words = " ".join(lines).split()
    arabic_words = sum(1 for word in words if ARABIC_LETTER.search(word))
    ratio = arabic_words / max(len(words), 1)
    return QualityReport(
        phrase_results=phrase_results,
        arabic_word_ratio=ratio,
        line_count=len(lines),
        word_count=len(words),
    )


def format_report(report: QualityReport) -> str:
    lines = [f"[{'OK' if ok else 'FAIL'}] {name}" for name, ok in report.phrase_results.items()]
    lines.append(f"النتيجة: {report.passed_checks}/{report.total_checks}")
    lines.append(f"أسطر: {report.line_count} | كلمات: {report.word_count}")
    lines.append(f"نسبة الكلمات العربية: {report.arabic_word_ratio:.1%}")
    lines.append("جودة عالية" if report.is_high_quality else "تحتاج مراجعة")
    return "\n".join(lines)
