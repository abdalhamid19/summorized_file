import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import pymupdf4llm

pdf_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.pdf'
output_path = r'C:\pc\py\pyreview\summorized_file\main_obsidian\دين\التزكية\البركة\ar_Albarakah.md'

md_text = pymupdf4llm.to_markdown(pdf_path, pages=[0, 1, 2, 3, 4])

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(md_text)

print('Done')
