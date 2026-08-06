import re

from . import quran_db

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
