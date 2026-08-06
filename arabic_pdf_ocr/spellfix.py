import re
from collections import Counter

from . import quran_db

ARABIC_WORD = re.compile(r"[\u0621-\u064A][\u0621-\u064Aً-ْ]*")
MIN_COMMON_FREQUENCY = 10
MAX_RARE_FREQUENCY = 2
FREQUENCY_RATIO = 5


def build_vocabulary(text: str) -> Counter:
    words = ARABIC_WORD.findall(text)
    normalized = [quran_db.normalize(w) for w in words if len(w) >= 3]
    return Counter(normalized)


def _edit_distance_one(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False
    if a == b:
        return False
    if len(a) == len(b):
        diffs = [i for i, (x, y) in enumerate(zip(a, b)) if x != y]
        return len(diffs) == 1
    longer, shorter = (a, b) if len(a) > len(b) else (b, a)
    for i in range(len(longer)):
        if longer[:i] + longer[i + 1:] == shorter:
            return True
    return False


def suggest_corrections(text: str) -> dict:
    vocab = build_vocabulary(text)
    common = {w for w, c in vocab.items() if c >= MIN_COMMON_FREQUENCY}
    suggestions = {}
    for word, count in vocab.items():
        if count > MAX_RARE_FREQUENCY or len(word) < 4:
            continue
        for candidate in common:
            if candidate == word:
                continue
            if abs(len(candidate) - len(word)) > 1:
                continue
            if vocab[candidate] < count * FREQUENCY_RATIO:
                continue
            if _edit_distance_one(word, candidate):
                suggestions[word] = candidate
                break
    return suggestions


def apply_corrections(text: str, suggestions: dict) -> str:
    if not suggestions:
        return text

    def repl(match: re.Match) -> str:
        word = match.group(0)
        normalized = quran_db.normalize(word)
        return suggestions.get(normalized, word)

    return ARABIC_WORD.sub(repl, text)


def correct(text: str) -> tuple[str, dict]:
    suggestions = suggest_corrections(text)
    return apply_corrections(text, suggestions), suggestions
