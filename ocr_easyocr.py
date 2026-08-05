import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import easyocr
from PIL import Image
import numpy as np

img_dir = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\pages_png'
out_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'

print('Initializing EasyOCR for Arabic...')
reader = easyocr.Reader(['ar'], gpu=False)

md = []
for i in range(1, 6):
    img_path = os.path.join(img_dir, f'page_{i}.png')
    print(f'OCR page {i} from {img_path}')
    pil_img = Image.open(img_path).convert('RGB')
    img_array = np.array(pil_img)
    results = reader.readtext(img_array, paragraph=False, detail=1)
    md.append(f'# الصفحة {i}\n\n')
    lines = {}
    for item in results:
        if len(item) == 3:
            bbox, text, conf = item
        elif len(item) == 2:
            bbox, text = item
        else:
            continue
        y_center = (bbox[0][1] + bbox[2][1]) / 2
        line_y = round(y_center / 30) * 30
        lines.setdefault(line_y, []).append((bbox[0][0], text))
    for y in sorted(lines.keys()):
        parts = sorted(lines[y], key=lambda x: x[0])
        line_text = ' '.join(p[1] for p in parts)
        md.append(line_text + '\n')
    md.append('\n')

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(''.join(md))

print('Done. Saved to', out_path)
