import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

md_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'

with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('=' * 60)
print('اختبار الجودة الحالية - تحليل الأخطاء')
print('=' * 60)

# 1. Known phrases that MUST appear correctly (ground truth checks)
known_checks = {
    'بسم الله الرحمن الرحيم (البسملة)': ['بسم', 'الرحمن', 'الرحيم'],
    'الحمد لله رب العالمين': ['الحمد', 'لله', 'رب', 'العالمين'],
    'محمد': ['محمد'],
    'البركة': ['البركة'],
    'الأعراف :٩٦': ['الأعراف'],
    'نوح': ['نوح'],
    'المقدمة': ['المقدمة'],
}

print('\n[1] فحص العبارات المعروفة (يجب أن تظهر بشكل صحيح):')
for name, keywords in known_checks.items():
    found = all(k in text for k in keywords)
    status = 'OK' if found else 'FAIL'
    missing = [k for k in keywords if k not in text]
    print(f'  [{status}] {name}' + (f' - مفقود: {missing}' if missing else ''))

# 2. Common OCR error patterns in Arabic
print('\n[2] أنماط الأخطاء الشائعة:')
patterns = {
    'مسافة قبل ة (مثل "المقدم ة")': re.findall(r'\S+ ة', text),
    'حروف مد مشوهة (ً بعد ا)': re.findall(r'اذ?\S*ً', text)[:5],
    'كلمات ملتصقة خاطئة (جاءذكرها)': re.findall(r'جاء\S+', text),
    'أرقام مشوهة': re.findall(r'[٠-٩]+[،,][٠-٩]+', text)[:5],
    'تعالى مشوهة': re.findall(r'تع\S*ال\S*', text),
    'السماء مشوهة': re.findall(r'آ?لس\S*م\S*اء', text),
}
for name, matches in patterns.items():
    count = len(matches)
    print(f'  [{count}] {name}: {matches[:3]}')

# 3. Statistics
print('\n[3] إحصائيات عامة:')
lines = [l for l in text.split('\n') if l.strip() and not l.startswith('#')]
words = ' '.join(lines).split()
print(f'  عدد الأسطر: {len(lines)}')
print(f'  عدد الكلمات: {len(words)}')
short_words = [w for w in words if len(w) == 1]
print(f'  كلمات من حرف واحد (مؤشر خطأ): {len(short_words)} - {short_words[:10]}')

# 4. Check diacritic corruption
print('\n[4] فحص التشكيل المشوه:')
bad_tashkeel = re.findall(r'[ً-ْ]{2,}', text)
print(f'  تسلسلات تشكيل متعددة: {len(bad_tashkeel)} - {bad_tashkeel[:5]}')

print('\n' + '=' * 60)
print('الخلاصة: الناتج الحالي يحتوي على أخطاء تحتاج محرك OCR أقوى')
print('=' * 60)
