import sys, io, os, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url = 'https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe'
out_path = r'C:\Users\QUANTUM\Downloads\tesseract\setup.exe'

os.makedirs(os.path.dirname(out_path), exist_ok=True)

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=600) as resp:
    total = resp.length if resp.length else 0
    print(f'Downloading {total} bytes...')
    with open(out_path, 'wb') as f:
        while True:
            chunk = resp.read(65536)
            if not chunk:
                break
            f.write(chunk)

print(f'Done. File size: {os.path.getsize(out_path)}')
