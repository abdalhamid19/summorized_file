import re
from dataclasses import dataclass

from . import quran_db

KNOWN_REFERENCES = (
    ("الأعراف: ٩٦", "الأعراف", 96),
    ("نوح: ١٠", "نوح", 10),
    ("نوح: ١١", "نوح", 11),
    ("نوح: ١٢", "نوح", 12),
)


def levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        a, b = b, a
    previous = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        current = [i]
        for j, cb in enumerate(b, 1):
            current.append(min(current[-1] + 1, previous[j] + 1, previous[j - 1] + (ca != cb)))
        previous = current
    return previous[-1]


def character_error_rate(reference: str, hypothesis: str) -> float:
    reference = quran_db.normalize(reference)
    hypothesis = quran_db.normalize(hypothesis)
    if not reference:
        return 0.0
    return levenshtein(reference, hypothesis) / len(reference)


@dataclass(frozen=True)
class VerseCheck:
    label: str
    found: bool
    cer: float


def _find_verse_like(text: str, keywords) -> str | None:
    for line in text.split("\n"):
        if all(k in line for k in keywords):
            return line
    return None


def check_verses(text: str) -> list[VerseCheck]:
    results = []
    for label, surah_name, ayah in KNOWN_REFERENCES:
        canonical = quran_db.verse_by_reference(f"{surah_name}: {ayah}")
        if canonical is None:
            results.append(VerseCheck(label, found=False, cer=1.0))
            continue
        core = quran_db.normalize(canonical).split()[:4]
        line = _find_verse_like(text, [quran_db.normalize(k) for k in core[:2]])
        if line is None:
            results.append(VerseCheck(label, found=False, cer=1.0))
            continue
        results.append(VerseCheck(label, found=True, cer=character_error_rate(canonical, line)))
    return results


def format_cer_report(checks: list[VerseCheck]) -> str:
    lines = []
    for check in checks:
        if check.found:
            lines.append(f"  {check.label}: CER={check.cer:.1%}")
        else:
            lines.append(f"  {check.label}: غير موجودة")
    valid = [c for c in checks if c.found]
    if valid:
        avg = sum(c.cer for c in valid) / len(valid)
        lines.append(f"  متوسط CER (آيات): {avg:.1%}")
    return "\n".join(lines)
