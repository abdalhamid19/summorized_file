import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

md_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('=' * 60)
print('اختبار الجودة بعد التحسين')
print('=' * 60)

checks = {
    'بسم الله / البسملة': any(x in text for x in ['بسم', 'الرحمن', 'الرحيم']),
    'الحمد لله رب العالمين': 'الحمد لله' in text and 'العالمين' in text,
    'محمد': 'محمد' in text,
    'البركة': 'البركة' in text,
    'الأعراف': 'الأعراف' in text,
    'نوح / الاستغفار': 'الاستغفار' in text or 'نوح' in text,
    'المقدمة / مباحث': 'مباحث' in text or 'المقدمة' in text,
    'أمين بن عبدالله': 'أمين' in text and 'الشقاوي' in text,
    'حقوق الطبع': 'حقوق الطبع' in text,
    'صلة الأرحام': 'صلة الأرحام' in text or 'الأرحام' in text,
    'مباحث الرسالة': 'مباحث الرسالة' in text,
    'تعريف البركة': 'تعريف البركة' in text,
    'موانع البركة': 'موانع البركة' in text,
}

print('\n[1] فحص العبارات المعروفة:')
ok = 0
for name, passed in checks.items():
    status = 'OK' if passed else 'FAIL'
    if passed: ok += 1
    print(f'  [{status}] {name}')
print(f'  النتيجة: {ok}/{len(checks)}')

print('\n[2] أنماط الأخطاء المتبقية:')
patterns = {
    'مسافة قبل ة': re.findall(r'\S+ ة\b', text),
    'تعالى مشوهة': re.findall(r'تع\S*ال\S*', text),
    'كلمات ملتصقة (جاءذكرها)': re.findall(r'جاءذكرها', text),
    'أسطر قمامة (رموز فقط)': [l for l in text.split('\n') if l.strip() and len(re.findall(r'[\u0600-\u06FF0-9٠-٩]', l)) < 2 and len(l.strip()) <= 5],
}
for name, matches in patterns.items():
    print(f'  [{len(matches)}] {name}: {matches[:5]}')

print('\n[3] إحصائيات:')
lines = [l for l in text.split('\n') if l.strip() and not l.startswith('#')]
words = ' '.join(lines).split()
print(f'  أسطر: {len(lines)} | كلمات: {len(words)} | أحرف: {len(text)}')

# Coherence: consecutive Arabic words ratio
arabic_word_ratio = sum(1 for w in words if re.search(r'[\u0600-\u06FF]', w)) / max(len(words), 1)
print(f'  نسبة الكلمات العربية: {arabic_word_ratio:.1%}')

print('\n' + '=' * 60)
if ok >= 11 and arabic_word_ratio > 0.85:
    print('النتيجة: جودة عالية - النص جاهز للاستخدام')
else:
    print('النتيجة: جودة متوسطة - تحتاج مراجعة يدوية بسيطة')
print('=' * 60)
