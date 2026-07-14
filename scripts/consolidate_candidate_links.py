from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CAMPAIGN_URL = "https://russelldudek.github.io/reveal/"
CAMPAIGN_LABEL = "russelldudek.github.io/reveal/"

html_files = [
    ROOT / "resume.html",
    ROOT / "cover-letter.html",
    ROOT / "interview-brief.html",
    ROOT / "120-day-plan.html",
    ROOT / "ai-yield-review.html",
]

old_link_pair = (
    '<a href="https://russelldudek.github.io/">russelldudek.github.io</a> · '
    '<a href="https://github.com/russelldudek">github.com/russelldudek</a>'
)
new_campaign_link = f'<a href="{CAMPAIGN_URL}">{CAMPAIGN_LABEL}</a>'

for path in html_files:
    text = path.read_text(encoding="utf-8")
    text = text.replace(old_link_pair, new_campaign_link)
    text = text.replace(
        "The materials are available through my portfolio at <strong>russelldudek.github.io</strong>.",
        "The complete hiring-team campaign is available at <strong>russelldudek.github.io/reveal/</strong>.",
    )
    path.write_text(text, encoding="utf-8")

for path in (ROOT / "audit" / "pdf-text").glob("*.txt"):
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        "russelldudek.github.io · github.com/russelldudek",
        CAMPAIGN_LABEL,
    )
    text = text.replace(
        "are available through my portfolio at russelldudek.github.io.",
        "complete hiring-team campaign is available at russelldudek.github.io/reveal/.",
    )
    path.write_text(text, encoding="utf-8")

readme = ROOT / "README.md"
text = readme.read_text(encoding="utf-8")
text = re.sub(
    r"## Publication target\n.*?(?=\n## Independence)",
    "## Hiring-team site\n"
    "The campaign is published from the `reveal` repository and uses one candidate-facing URL: "
    "`https://russelldudek.github.io/reveal/`. General portfolio and GitHub profile links are "
    "intentionally omitted from the application documents.\n",
    text,
    flags=re.S,
)
readme.write_text(text, encoding="utf-8")

(ROOT / "campaign-audit.md").write_text(
    """# Campaign Audit

Audit date: July 14, 2026

## Current classification
**Campaign state: published to the hiring-team-facing `reveal` repository; live-route verification remains required.**

The complete campaign source, official Revel IT identity package, responsive website, interaction code, audits, and five generated PDFs are committed to the `reveal` repository's `main` branch. The single hiring-team-facing campaign URL is `https://russelldudek.github.io/reveal/`; general portfolio and GitHub profile links have been removed from the application documents and public PDF-text audit copies.

## Completed checks
- Manifest: passed on `main`
- Evidence integrity: passed
- Official identity and asset provenance: passed
- Color-token provenance: passed
- Typography decision: passed
- Independent-candidate distinction: passed
- Visual experience: passed in rendered review
- Role-derived motion and scenario interaction: passed
- Keyboard scenario navigation: passed
- Reduced-motion treatment: passed
- Responsive source/render review: 24 route-and-viewport checks passed across desktop, laptop, tablet, and mobile
- Horizontal overflow: zero findings after tablet and mobile recomposition
- Document footer collisions: zero findings
- Broken local links and images: zero findings
- Resume pagination and page-one balance: passed
- Cover-letter pagination: passed
- PDF visual review: passed
- Public source and PDF confidentiality scan: zero restricted internal-process-name matches
- Candidate-link consolidation: passed; only `https://russelldudek.github.io/reveal/` remains as the GitHub Pages destination
- UX psychology: passed after replacing an unsupported percentage display with a clearly labeled 100-point illustrative retained-value index
- Smart baseline and reset: passed
- Value-before-ask, meaningful participation, contextual comparison, cost-of-inaction, and dark-pattern review: passed

## Publication boundary
The campaign cannot be classified as complete until:
1. GitHub Pages is confirmed from `main` and `/ (root)` for the existing `reveal` repository;
2. live routes, reciprocal document links, motion, responsive states, and PDF downloads are verified against the final published head.

## Job posting
Supplied in chat; no public job-posting URL was supplied or independently verified.
""",
    encoding="utf-8",
)

for path in [*html_files, ROOT / "README.md", ROOT / "campaign-audit.md", *(ROOT / "audit" / "pdf-text").glob("*.txt")]:
    text = path.read_text(encoding="utf-8")
    if 'href="https://russelldudek.github.io/"' in text:
        raise SystemExit(f"Legacy portfolio URL remains in {path.relative_to(ROOT)}")
    if "github.com/russelldudek" in text:
        raise SystemExit(f"General GitHub profile remains in {path.relative_to(ROOT)}")

Path(__file__).unlink()
