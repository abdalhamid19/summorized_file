import json
import re
from pathlib import Path

_DATA_PATH = Path(__file__).resolve().parent / "quran.json"

ARABIC_DIACRITICS = re.compile(r"[ً-ْٰۡۢۖۗۘۙۚۛۜ۞ۣ۟۠ۥۦۧۨ۩۪ۭ۫۬ۮۯ۰-۹ـ]")

_cache = None


def _load():
    global _cache
    if _cache is None:
        data = json.loads(_DATA_PATH.read_text(encoding="utf-8"))
        _cache = {
            (surah["id"], verse["id"]): verse["text"]
            for surah in data
            for verse in surah["verses"]
        }
    return _cache


def verse(surah: int, ayah: int) -> str | None:
    return _load().get((surah, ayah))


def normalize(text: str) -> str:
    text = ARABIC_DIACRITICS.sub("", text)
    text = text.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    text = text.replace("ى", "ي").replace("ئ", "ي").replace("ؤ", "و")
    text = text.replace("ة", "ه")
    return re.sub(r"\s+", " ", text).strip()


SURAH_NAMES = {
    "الفاتحة": 1, "البقرة": 2, "آل عمران": 3, "ال عمران": 3, "النساء": 4,
    "المائدة": 5, "الأنعام": 6, "الانعام": 6, "الأعراف": 7, "الاعراف": 7,
    "الأنفال": 8, "الانفال": 8, "التوبة": 9, "يونس": 10, "هود": 11,
    "يوسف": 12, "الرعد": 13, "إبراهيم": 14, "ابراهيم": 14, "الحجر": 15,
    "النحل": 16, "الإسراء": 17, "الاسراء": 17, "الكهف": 18, "مريم": 19,
    "طه": 20, "الأنبياء": 21, "الانبياء": 21, "الحج": 22, "المؤمنون": 23,
    "النور": 24, "الفرقان": 25, "الشعراء": 26, "النمل": 27, "القصص": 28,
    "العنكبوت": 29, "الروم": 30, "لقمان": 31, "السجدة": 32, "الأحزاب": 33,
    "الاحزاب": 33, "سبأ": 34, "سبا": 34, "فاطر": 35, "يس": 36, "الصافات": 37,
    "ص": 38, "الزمر": 39, "غافر": 40, "فصلت": 41, "الشورى": 42,
    "الزخرف": 43, "الدخان": 44, "الجاثية": 45, "الأحقاف": 46, "الاحقاف": 46,
    "محمد": 47, "الفتح": 48, "الحجرات": 49, "ق": 50, "الذاريات": 51,
    "الطور": 52, "النجم": 53, "القمر": 54, "الرحمن": 55, "الواقعة": 56,
    "الحديد": 57, "المجادلة": 58, "الحشر": 59, "الممتحنة": 60, "الصف": 61,
    "الجمعة": 62, "المنافقون": 63, "التغابن": 64, "الطلاق": 65, "التحريم": 66,
    "الملك": 67, "القلم": 68, "الحاقة": 69, "المعارج": 70, "نوح": 71,
    "الجن": 72, "المزمل": 73, "المدثر": 74, "القيامة": 75, "الإنسان": 76,
    "الانسان": 76, "المرسلات": 77, "النبأ": 78, "النبا": 78, "النازعات": 79,
    "عبس": 80, "التكوير": 81, "الانفطار": 82, "المطففين": 83, "الانشقاق": 84,
    "البروج": 85, "الطارق": 86, "الأعلى": 87, "الاعلى": 87, "الغاشية": 88,
    "الفجر": 89, "البلد": 90, "الشمس": 91, "الليل": 92, "الضحى": 93,
    "الشرح": 94, "التين": 95, "العلق": 96, "القدر": 97, "البينة": 98,
    "الزلزلة": 99, "العاديات": 100, "القارعة": 101, "التكاثر": 102,
    "العصر": 103, "الهمزة": 104, "الفيل": 105, "قريش": 106, "الماعون": 107,
    "الكوثر": 108, "الكافرون": 109, "النصر": 110, "المسد": 111,
    "الإخلاص": 112, "الاخلاص": 112, "الفلق": 113, "الناس": 114,
}

ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def parse_reference(ref: str):
    match = re.match(r"^\s*([^:：\[]+?)\s*[:：]\s*([0-9٠-٩]+)\s*$", ref)
    if not match:
        return None
    name = normalize(match.group(1)).strip()
    surah = None
    for key, value in SURAH_NAMES.items():
        if normalize(key) == name:
            surah = value
            break
    if surah is None:
        return None
    ayah = int(match.group(2).translate(ARABIC_DIGITS))
    return surah, ayah


def verse_by_reference(ref: str) -> str | None:
    parsed = parse_reference(ref)
    if parsed is None:
        return None
    surah, ayah = parsed
    return verse(surah, ayah)
