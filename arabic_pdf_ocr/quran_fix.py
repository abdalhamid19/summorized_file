import re

from . import quran_db

VERSE_MARKER = re.compile(r"(قال تعالى|قال الله تعالى|قال سبحانه|﴿|لقوله تعالى|قوله تعالى)")
MATCH_CER_THRESHOLD = 0.45
_verse_index = None

CITATION = re.compile(
    r"﴿(?P<quote>[^﴾]{10,400})﴾\s*\[(?P<ref>[^\]]{2,40})\]"
)

QUOTE_BEFORE_BRACKET = re.compile(
    r"(?P<quote>[«\"'“”]?)(?P<body>[^.\n]{10,400}?)\s*\[(?P<ref>[^\]]{2,40})\]"
)


def _replacement_for(ref_text: str):
    ref_text = ref_text.strip().rstrip("]،. ")
    parsed = quran_db.parse_reference(ref_text)
    if parsed is None:
        return None
    surah, ayah = parsed
    canonical = quran_db.verse(surah, ayah)
    if canonical is None:
        return None
    return canonical, surah, ayah


def fix_cited_verses(text: str) -> str:
    def repl(match: re.Match) -> str:
        found = _replacement_for(match.group("ref"))
        if found is None:
            return match.group(0)
        canonical, surah, ayah = found
        return f"﴿{canonical}﴾ [{ref_label(surah, ayah)}]"

    return CITATION.sub(repl, text)


def ref_label(surah: int, ayah: int) -> str:
    for name, number in quran_db.SURAH_NAMES.items():
        if number == surah and len(name) > 2:
            return f"{name}: {ayah}"
    return f"{surah}:{ayah}"


def fix_inline_citations(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        match = QUOTE_BEFORE_BRACKET.search(line)
        if match:
            found = _replacement_for(match.group("ref"))
            if found is not None:
                canonical, surah, ayah = found
                prefix = line[: match.start("body")]
                suffix = line[match.end():]
                quote_open = match.group("quote") or ""
                line = f"{prefix}﴿{canonical}﴾ [{ref_label(surah, ayah)}]{suffix}"
                lines.append(line)
                continue
        lines.append(line)
    return "\n".join(lines)


def _build_index():
    global _verse_index
    if _verse_index is None:
        from collections import defaultdict
        index = defaultdict(set)
        data = quran_db._load()
        for (surah, ayah), text in data.items():
            for word in set(quran_db.normalize(text).split()):
                if len(word) >= 3:
                    index[word].add((surah, ayah))
        _verse_index = index
    return _verse_index


def _best_verse_match(line: str):
    normalized = quran_db.normalize(line)
    words = [w for w in normalized.split() if len(w) >= 3]
    if len(words) < 4:
        return None
    index = _build_index()
    from collections import Counter
    hits = Counter()
    for word in words:
        for key in index.get(word, ()):  # candidate verses sharing this word
            hits[key] += 1
    if not hits:
        return None
    ranked = hits.most_common(5)
    best_key, best_overlap = ranked[0]
    second_overlap = ranked[1][1] if len(ranked) > 1 else 0
    if best_overlap < 5 or best_overlap < second_overlap * 1.5:
        return None
    canonical = quran_db.verse(*best_key)
    return canonical, best_key


def fix_verses_by_content(text: str) -> str:
    lines = []
    for line in text.split("\n"):
        stripped = line.strip()
        if VERSE_MARKER.search(stripped) and "﴿" not in stripped and len(stripped) >= 20:
            match = _best_verse_match(stripped)
            if match is not None:
                canonical, (surah, ayah) = match
                lead = stripped[: stripped.find("(") ] if "(" in stripped else ""
                lines.append(f"{lead}﴿{canonical}﴾ [{ref_label(surah, ayah)}].")
                continue
        lines.append(line)
    return "\n".join(lines)
