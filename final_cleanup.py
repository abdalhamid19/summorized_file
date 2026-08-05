"""Final cleanup: remove junk, fix known Quranic verses, polish body text."""
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Fix known Quranic verses (standard text, clearly identified by context)
# Al-A'raf 96
text = re.sub(
    r'قال تعالى:.*?الأعراف[:：]?\s*\d*\].?',
    'قال تعالى: ﴿وَلَوْ أَنَّ أَهْلَ الْقُرَىٰ آمَنُوا وَاتَّقَوْا لَفَتَحْنَا عَلَيْهِم بَرَكَاتٍ مِّنَ السَّمَاءِ وَالْأَرْضِ﴾ [الأعراف: ٩٦].',
    text,
    flags=re.DOTALL
)

# Nuh 10-12 (spans multiple lines after الاستغفار)
text = re.sub(
    r'ومن ذلك الاستغفار\s*\.?\s*قال تعالى:.*?\]\.?',
    'ومن ذلك الاستغفار. قال تعالى: ﴿فَقُلْتُ اسْتَغْفِرُوا رَبَّكُمْ إِنَّهُ كَانَ غَفَّارًا ۝ يُرْسِلِ السَّمَاءَ عَلَيْكُم مِّدْرَارًا ۝ وَيُمْدِدْكُم بِأَمْوَالٍ وَبَنِينَ وَيَجْعَل لَّكُمْ جَنَّاتٍ وَيَجْعَل لَّكُمْ أَنْهَارًا﴾ [نوح: ١٠-١٢].',
    text,
    flags=re.DOTALL
)

# Fix remaining body text errors
fixes = [
    (r'استعالى في طاعة', 'استعمالها في طاعة'),
    (r'والسئة', 'والسنة'),
    (r'مقتصرً على', 'مقتصراً على'),
    (r'ماعدا ذلك', 'ما عدا ذلك'),
    (r'مماهو', 'مما هو'),
    (r'مجانا بعد', 'مجاناً بعد'),
    (r'ثالثا?\s*:', 'ثالثاً:'),
    (r'ثالثا?\s*:', 'ثالثاً:'),  # ensure
    (r'رابعا\s*:', 'رابعاً:'),
    (r'ُستَجْلب', 'تستجلب'),
    (r'الشقاوي؛ أمين', 'الشقاوي، أمين'),
    (r'١-الوعظ', '١- الوعظ'),
]

for pat, rep in fixes:
    text = re.sub(pat, rep, text)

# Clean line by line
cleaned = []
for line in text.split('\n'):
    s = line.strip()
    if not s:
        cleaned.append('')
        continue
    if s.startswith('#'):
        cleaned.append(s)
        continue
    # Drop junk lines
    arabic = len(re.findall(r'[\u0600-\u06FF]', s))
    digits = len(re.findall(r'[0-9٠-٩]', s))
    total = len(re.sub(r'\s', '', s))
    # pure noise
    if total <= 4 and arabic + digits <= 2:
        continue
    if re.match(r'^[^\u0600-\u06FF0-9٠-٩a-zA-Z]{1,10}$', s):
        continue
    # long noise strings of repeated chars
    if re.search(r'(.)\1{8,}', s) and arabic < 10:
        continue
    # header garbage like "تت المقدمة مم]ةماستتمست..."
    if 'مستس' in s or re.search(r'[تمس]{6,}', s):
        if 'المقدمة' in s:
            cleaned.append('المقدمة')
            continue
        continue
    # "اللاللار" basmalah garbage -> fix to basmalah
    if re.match(r'^ال+ا*ر*$', s) or s in ('اللاللار', '0'):
        if 'بسم' not in '\n'.join(cleaned[-3:]):
            cleaned.append('بسم الله الرحمن الرحيم')
        continue
    cleaned.append(s)

# Collapse excess blank lines
result = []
blank = 0
for line in cleaned:
    if not line:
        blank += 1
        if blank <= 1:
            result.append('')
    else:
        blank = 0
        result.append(line)

final = '\n'.join(result).strip() + '\n'

with open(path, 'w', encoding='utf-8') as f:
    f.write(final)

print('Final cleanup done')
print(f'Chars: {len(final)}')
