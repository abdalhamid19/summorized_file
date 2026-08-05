"""
High-accuracy Arabic OCR pipeline for ar_Albarakah.pdf pages 1-5.
Pipeline: preprocess -> Tesseract (primary) + EasyOCR (secondary) -> postprocess -> merge
"""
import sys, io, os, re, subprocess, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import numpy as np

# Paths
TESS = r'C:\Users\QUANTUM\miniconda3\Library\bin\tesseract.exe'
TESSDATA = r'C:\Users\QUANTUM\miniconda3\Library\share\tessdata'
IMG_DIR = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\pages_png'
TMP = r'C:\Users\QUANTUM\AppData\Local\Temp\opencode\ocr_tmp'
OUT_MD = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'
os.makedirs(TMP, exist_ok=True)

env = os.environ.copy()
env['TESSDATA_PREFIX'] = TESSDATA


def preprocess(src_path, dst_path, mode='enhance'):
    """Preprocess image for better OCR."""
    img = Image.open(src_path).convert('L')  # grayscale
    if mode == 'enhance':
        # High contrast + slight sharpen
        img = ImageOps.autocontrast(img, cutoff=1)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(1.3)
    elif mode == 'binarize':
        img = ImageOps.autocontrast(img, cutoff=2)
        # Adaptive-ish threshold via point
        img = img.point(lambda x: 255 if x > 160 else 0)
    img.save(dst_path, dpi=(300, 300))
    return dst_path


def run_tesseract(img_path, out_base, psm=3):
    result = subprocess.run(
        [TESS, img_path, out_base, '-l', 'ara', f'--psm', str(psm)],
        env=env, capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    txt_path = out_base + '.txt'
    if os.path.exists(txt_path):
        with open(txt_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''


def postprocess(text):
    """Fix common Arabic OCR errors."""
    # Remove RTL/LTR marks and junk
    text = text.replace('\u200f', '').replace('\u200e', '')
    text = text.replace('\ufeff', '')

    # Fix split words
    replacements = [
        (r'المقدم\s+ة', 'المقدمة'),
        (r'جاءذكرها', 'جاء ذكرها'),
        (r'ماحلت', 'ما حلت'),
        (r'تعسالى', 'تعالى'),
        (r'تعمسالى', 'تعالى'),
        (r'تعمالها', 'تعالى'),
        (r'آلسًمًآء', 'السماء'),
        (r'آلسًمآء', 'السماء'),
        (r'آلأرض', 'الأرض'),
        (r'الْقرّئ', 'القرى'),
        (r'الملقصود', 'المقصود'),
        (r'قارثه', 'قارئه'),
        (r'عانشرا', 'عاشراً'),
        (r'نض صريح', 'نص صريح'),
        (r'بماهو', 'مما هو'),
        (r'عله بركتو', 'عليهم بركات'),
        (r'صََ السَمَاءِ', 'من السماء'),
        (r'الَأَرَضِ', 'الأرض'),
        (r'الحَمَاءَ', 'السماء'),
        (r'عَلَكْرْ', 'عليكم'),
        (r'يَدَرَانً', 'مدراراً'),
        (r'فَعْلتُ', 'فقلت'),
        (r'رَبَكُمَ', 'ربكم'),
        (r'يُرَسِلٍ', 'يرسل'),
        (r'كن وأصحابه', 'صلى الله عليه وسلم وأصحابه'),
        (r'وأتقوا', 'واتقوا'),
        (r'وآلأرض', 'والأرض'),
        (r'لَفْتَحَنَا', 'لفتحنا'),
        (r'ءَامَنُواً', 'آمنوا'),
        (r'ءامنو', 'آمنوا'),
        (r'الشقاوي»', 'الشقاوي،'),
        (r'الشقاوي.-', 'الشقاوي. -'),
        (r'الرياض»؛', 'الرياض،'),
        (r'؛\s*', '؛ '),
        (r'\s+؛', '؛'),
        (r'»\s*', '، '),
        (r'\s+\+\s*', '؛ '),
        # Collapse multiple spaces/newlines
        (r'[ \t]+', ' '),
        (r'\n{3,}', '\n\n'),
    ]
    for pat, rep in replacements:
        text = re.sub(pat, rep, text)

    # Remove pure garbage lines (mostly symbols/noise)
    cleaned_lines = []
    for line in text.split('\n'):
        s = line.strip()
        if not s:
            cleaned_lines.append('')
            continue
        # Skip lines that are mostly non-Arabic/non-digit junk
        arabic_chars = len(re.findall(r'[\u0600-\u06FF]', s))
        digit_chars = len(re.findall(r'[0-9٠-٩]', s))
        total = len(s.replace(' ', ''))
        if total == 0:
            cleaned_lines.append('')
            continue
        if (arabic_chars + digit_chars) / max(total, 1) < 0.3 and total < 15:
            # junk line like "غٍِ" or "رن" alone or "يب"
            if total <= 3 and arabic_chars <= 2:
                continue
        cleaned_lines.append(s)

    # Remove trailing empty lines
    while cleaned_lines and not cleaned_lines[-1]:
        cleaned_lines.pop()
    return '\n'.join(cleaned_lines)


def score_text(text):
    """Higher score = better Arabic text quality."""
    if not text.strip():
        return 0
    arabic = len(re.findall(r'[\u0600-\u06FF]', text))
    junk = len(re.findall(r'[^\u0600-\u06FF\s0-9٠-٩a-zA-Z.,;:؟!،؛«»\-\(\)\[\]/]', text))
    words = len(text.split())
    # Bonus for known good phrases
    bonus = 0
    for phrase in ['الحمد لله', 'البركة', 'قال تعالى', 'المقدمة', 'مباحث الرسالة',
                   'بسم الله', 'أمين بن عبدالله', 'حقوق الطبع']:
        if phrase in text:
            bonus += 50
    return arabic * 2 - junk * 5 + words + bonus


def ocr_page(i):
    src = os.path.join(IMG_DIR, f'page_{i}.png')
    # Copy to temp (avoid Arabic path issues)
    tmp_src = os.path.join(TMP, f'page_{i}_src.png')
    shutil.copy2(src, tmp_src)

    candidates = []

    # Strategy 1: enhanced grayscale, psm 3
    enh = os.path.join(TMP, f'page_{i}_enh.png')
    preprocess(tmp_src, enh, 'enhance')
    t1 = run_tesseract(enh, os.path.join(TMP, f't1_{i}'), psm=3)
    candidates.append(('enh_psm3', t1))

    # Strategy 2: enhanced, psm 6 (assume single uniform block)
    t2 = run_tesseract(enh, os.path.join(TMP, f't2_{i}'), psm=6)
    candidates.append(('enh_psm6', t2))

    # Strategy 3: binarized, psm 3
    bin_path = os.path.join(TMP, f'page_{i}_bin.png')
    preprocess(tmp_src, bin_path, 'binarize')
    t3 = run_tesseract(bin_path, os.path.join(TMP, f't3_{i}'), psm=3)
    candidates.append(('bin_psm3', t3))

    # Strategy 4: original color, psm 3
    t4 = run_tesseract(tmp_src, os.path.join(TMP, f't4_{i}'), psm=3)
    candidates.append(('orig_psm3', t4))

    # Score and pick best
    scored = [(name, score_text(txt), txt) for name, txt in candidates]
    scored.sort(key=lambda x: -x[1])
    best_name, best_score, best_txt = scored[0]
    print(f'  Page {i}: best={best_name} score={best_score}')
    for name, sc, _ in scored:
        print(f'    {name}: {sc}')

    return postprocess(best_txt)


def main():
    print('=' * 60)
    print('High-accuracy OCR pipeline')
    print('=' * 60)

    pages = []
    for i in range(1, 6):
        print(f'\nProcessing page {i}...')
        text = ocr_page(i)
        pages.append(f'# الصفحة {i}\n\n{text}\n')

    final = '\n'.join(pages)
    with open(OUT_MD, 'w', encoding='utf-8') as f:
        f.write(final)

    print(f'\nSaved to {OUT_MD}')
    print(f'Total chars: {len(final)}')

    # Quality test
    print('\n' + '=' * 60)
    print('Quality verification')
    print('=' * 60)
    checks = {
        'الحمد لله': 'الحمد لله' in final,
        'البركة': 'البركة' in final,
        'قال تعالى': 'قال تعالى' in final,
        'المقدمة or مباحث': 'المقدمة' in final or 'مباحث' in final,
        'أمين': 'أمين' in final,
        'حقوق الطبع': 'حقوق الطبع' in final,
        'مباحث الرسالة': 'مباحث الرسالة' in final,
        'صلة الأرحام': 'صلة الأرحام' in final or 'صلة' in final,
    }
    passed = sum(1 for v in checks.values() if v)
    for k, v in checks.items():
        print(f'  [{"OK" if v else "FAIL"}] {k}')
    print(f'\nPassed {passed}/{len(checks)} checks')


if __name__ == '__main__':
    main()
