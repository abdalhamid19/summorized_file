import sys, io, os, subprocess, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

tess = r'C:\Users\QUANTUM\miniconda3\Library\bin\tesseract.exe'
tessdata = r'C:\Users\QUANTUM\miniconda3\Library\share\tessdata'
img_dir = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\pages_png'
tmp_dir = r'C:\Users\QUANTUM\AppData\Local\Temp\opencode\ocr_tmp'
out_dir = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\tess_out'
os.makedirs(tmp_dir, exist_ok=True)
os.makedirs(out_dir, exist_ok=True)

env = os.environ.copy()
env['TESSDATA_PREFIX'] = tessdata

for i in range(1, 6):
    src = os.path.join(img_dir, f'page_{i}.png')
    tmp_img = os.path.join(tmp_dir, f'page_{i}.png')
    shutil.copy2(src, tmp_img)
    out_base = os.path.join(tmp_dir, f'out_{i}')
    print(f'Tesseract OCR page {i}...')
    result = subprocess.run(
        [tess, tmp_img, out_base, '-l', 'ara', '--psm', '3'],
        env=env, capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    if result.returncode != 0:
        print(f'  ERROR: {result.stderr}')
    else:
        txt_tmp = out_base + '.txt'
        size = os.path.getsize(txt_tmp) if os.path.exists(txt_tmp) else 0
        print(f'  OK ({size} bytes)')
        if size > 0:
            dst = os.path.join(out_dir, f'page_{i}.txt')
            shutil.copy2(txt_tmp, dst)

print('Done')
