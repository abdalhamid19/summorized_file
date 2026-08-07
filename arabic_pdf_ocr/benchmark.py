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


def _find_best_match(text: str, canonical: str) -> str | None:
    normalized_canonical = quran_db.normalize(canonical)
    keywords = [k for k in normalized_canonical.split()[:2] if k]
    candidates = [
        line for line in text.split("\n")
        if all(quran_db.normalize(k) in quran_db.normalize(line) for k in keywords)
    ]
    if not candidates:
        return None
    return min(candidates, key=lambda line: character_error_rate(canonical, line))


def check_verses(text: str) -> list[VerseCheck]:
    normalized_text = quran_db.normalize(text)
    results = []
    for label, surah_name, ayah in KNOWN_REFERENCES:
        canonical = quran_db.verse_by_reference(f"{surah_name}: {ayah}")
        if canonical is None:
            results.append(VerseCheck(label, found=False, cer=1.0))
            continue
        words = [w for w in quran_db.normalize(canonical).split() if len(w) >= 2]
        if not words:
            results.append(VerseCheck(label, found=False, cer=1.0))
            continue
        present = sum(1 for w in words if w in normalized_text)
        coverage = present / len(words)
        results.append(VerseCheck(label, found=coverage >= 0.5, cer=1.0 - coverage))
    return results


def format_cer_report(checks: list[VerseCheck]) -> str:
    lines = []
    for check in checks:
        coverage = 1.0 - check.cer
        lines.append(f"  {check.label}: تغطية معيارية={coverage:.0%}")
    valid = [c for c in checks if c.found]
    if valid:
        avg = sum(1.0 - c.cer for c in valid) / len(valid)
        lines.append(f"  متوسط التغطية المعيارية (آيات): {avg:.0%}")
    return "\n".join(lines)
