import sys, io, os, fitz
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.pdf'
out_dir = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\pages_png'
os.makedirs(out_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(min(5, len(doc))):
    page = doc[i]
    mat = fitz.Matrix(3, 3)  # 3x zoom for better OCR
    pix = page.get_pixmap(matrix=mat)
    img_path = os.path.join(out_dir, f'page_{i+1}.png')
    pix.save(img_path)
    print(f'Saved page {i+1}: {img_path} ({pix.width}x{pix.height})')
doc.close()
