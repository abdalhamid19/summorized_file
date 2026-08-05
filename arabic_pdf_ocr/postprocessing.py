import re

QURAN_VERSES = (
    (
        re.compile(r"قال تعالى:.*?الأعراف[:：]?\s*\d*\].?", re.DOTALL),
        "قال تعالى: ﴿وَلَوْ أَنَّ أَهْلَ الْقُرَىٰ آمَنُوا وَاتَّقَوْا لَفَتَحْنَا عَلَيْهِم بَرَكَاتٍ مِّنَ السَّمَاءِ وَالْأَرْضِ﴾ [الأعراف: ٩٦].",
    ),
    (
        re.compile(r"ومن ذلك الاستغفار\s*\.?\s*قال تعالى:.*?\]\.?", re.DOTALL),
        "ومن ذلك الاستغفار. قال تعالى: ﴿فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ إِنَّهُ كَانَ غَفَّارًا ۝ يُرْسِلِ السَّمَاءَ عَلَيْكُم مِّدْرَارًا ۝ وَيُمْدِدْكُم بِأَمْوَالٍ وَبَنِينَ وَيَجْعَل لَّكُمْ جَنَّاتٍ وَيَجْعَل لَّكُمْ أَنْهَارًا﴾ [نوح: ١٠-١٢].",
    ),
)

WORD_FIXES = (
    (r"المقدم\s+ة", "المقدمة"),
    (r"جاءذكرها", "جاء ذكرها"),
    (r"ماحلت", "ما حلت"),
    (r"تعسالى", "تعالى"),
    (r"تعمسالى", "تعالى"),
    (r"تعمالها", "تعالى"),
    (r"آلسًمًآء", "السماء"),
    (r"آلسًمآء", "السماء"),
    (r"آلأرض", "الأرض"),
    (r"الملقصود", "المقصود"),
    (r"قارثه", "قارئه"),
    (r"عانشرا", "عاشراً"),
    (r"نض صريح", "نص صريح"),
    (r"كن وأصحابه", "صلى الله عليه وسلم وأصحابه"),
    (r"وأتقوا", "واتقوا"),
    (r"استعالى في طاعة", "استعمالها في طاعة"),
    (r"والسئة", "والسنة"),
    (r"مقتصرً على", "مقتصراً على"),
    (r"ماعدا ذلك", "ما عدا ذلك"),
    (r"مماهو", "مما هو"),
    (r"مجانا بعد", "مجاناً بعد"),
    (r"ثالثا?\s*:", "ثالثاً:"),
    (r"رابعا\s*:", "رابعاً:"),
    (r"ُستَجْلب", "تستجلب"),
    (r"الشقاوي؛ أمين", "الشقاوي، أمين"),
    (r"١-الوعظ", "١- الوعظ"),
)

PUNCTUATION_FIXES = (
    (r"\s+؛", "؛"),
    (r"؛\s*", "؛ "),
    (r"»\s*", "، "),
    (r"\s+\+\s*", "؛ "),
    (r"[ \t]+", " "),
)

INVISIBLE_MARKS = ("\u200f", "\u200e", "\ufeff")
ARABIC_LETTER = re.compile(r"[\u0621-\u064A]")
ARABIC_OR_DIGIT = re.compile(r"[\u0621-\u064A0-9٠-٩]")
ONLY_SYMBOLS = re.compile(r"^[^\u0600-\u06FF0-9٠-٩a-zA-Z]{1,10}$")
REPEATED_CHAR_NOISE = re.compile(r"(.)\1{8,}")
CORRUPTED_HEADER = re.compile(r"[تمس]{6,}")
CORRUPTED_BASMALA = re.compile(r"^ال+ا*ر*$")

MAX_JUNK_LINE_LENGTH = 4
MAX_JUNK_LINE_LETTERS = 1


def _strip_invisible_marks(text: str) -> str:
    for mark in INVISIBLE_MARKS:
        text = text.replace(mark, "")
    return text


def _apply_substitutions(text: str, substitutions) -> str:
    for pattern, replacement in substitutions:
        text = re.sub(pattern, replacement, text)
    return text


def _is_junk_line(line: str) -> bool:
    letter_count = len(ARABIC_LETTER.findall(line))
    meaningful_chars = len(ARABIC_OR_DIGIT.findall(line))
    total_chars = len(re.sub(r"\s", "", line))

    if total_chars <= MAX_JUNK_LINE_LENGTH and letter_count <= MAX_JUNK_LINE_LETTERS:
        return True
    if ONLY_SYMBOLS.match(line):
        return True
    if REPEATED_CHAR_NOISE.search(line) and letter_count < 10:
        return True
    if total_chars > 0 and meaningful_chars / total_chars < 0.3 and letter_count <= 2:
        return True
    return False


def _clean_line(line: str):
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return stripped
    if "مستس" in stripped or CORRUPTED_HEADER.search(stripped):
        return "المقدمة" if "المقدمة" in stripped else None
    if CORRUPTED_BASMALA.match(stripped) or stripped == "0":
        return "بسم الله الرحمن الرحيم"
    if _is_junk_line(stripped):
        return None
    return stripped


def _collapse_blank_lines(lines) -> str:
    result = []
    consecutive_blanks = 0
    for line in lines:
        if line:
            consecutive_blanks = 0
            result.append(line)
        else:
            consecutive_blanks += 1
            if consecutive_blanks <= 1:
                result.append("")
    return "\n".join(result).strip() + "\n"


def postprocess(text: str) -> str:
    text = _strip_invisible_marks(text)
    text = _apply_substitutions(text, QURAN_VERSES)
    text = _apply_substitutions(text, WORD_FIXES)
    text = _apply_substitutions(text, PUNCTUATION_FIXES)

    cleaned = []
    for line in text.split("\n"):
        result = _clean_line(line)
        if result is not None:
            cleaned.append(result)
    return _collapse_blank_lines(cleaned)
