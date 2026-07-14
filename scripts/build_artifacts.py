from pathlib import Path
from urllib.request import urlopen, Request
from PIL import Image
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / 'assets' / 'brand'
DOCS = ROOT / 'docs'
BRAND.mkdir(parents=True, exist_ok=True)
DOCS.mkdir(parents=True, exist_ok=True)

ASSETS = {
    'revel-candidate-journey-vertical-source.png': 'https://www.revelit.com/wp-content/uploads/2025/03/Vertical-Candidate-Journey-1.png',
    'revel-home-hero-1.jpg': 'https://www.revelit.com/wp-content/uploads/2024/06/Home-Hero-Slide-Background-1.jpg',
    'revel-home-hero-2.jpg': 'https://www.revelit.com/wp-content/uploads/2024/06/Home-Hero-Slide-Background-2.jpg',
    'revel-home-hero-3.jpg': 'https://www.revelit.com/wp-content/uploads/2024/06/Home-Hero-Slide-Background-3.jpg',
}
for name, url in ASSETS.items():
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 candidate-campaign-build'})
    with urlopen(req, timeout=60) as response:
        (BRAND / name).write_bytes(response.read())

source = Image.open(BRAND / 'revel-candidate-journey-vertical-source.png').convert('RGBA')
crop = source.crop((450, 1560, 660, 1685))
crop.save(BRAND / 'revel-logo-source-crop.png')
transparent = []
for r, g, b, _ in crop.getdata():
    transparent.append((r, g, b, 255 if r + g + b > 361 else 0))
logo = Image.new('RGBA', crop.size)
logo.putdata(transparent)
logo.save(BRAND / 'revel-logo-white-transparent.png')

PDFS = {
    'resume.html': 'Russell-Dudek-Revel-IT-Resume.pdf',
    'cover-letter.html': 'Russell-Dudek-Revel-IT-Cover-Letter.pdf',
    'interview-brief.html': 'Russell-Dudek-Revel-IT-Interview-Brief.pdf',
    '120-day-plan.html': 'Russell-Dudek-Revel-IT-120-Day-Plan.pdf',
    'ai-yield-review.html': 'Russell-Dudek-Revel-IT-AI-Yield-Review.pdf',
}
for source_html, output_pdf in PDFS.items():
    HTML(filename=str(ROOT / source_html), base_url=str(ROOT)).write_pdf(str(DOCS / output_pdf))
