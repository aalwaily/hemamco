# Hemamco Company Limited — Website

Bilingual (English / Arabic) website for **Hemamco Company Limited** (شركة هممكو المحدودة), Dammam, Saudi Arabia.

## Structure

| Path | What it is |
|------|------------|
| `public_html/` | The live website — upload this folder to the hosting server |
| `public_html/*.html` | English pages |
| `public_html/ar/*.html` | Arabic pages (right-to-left) |
| `public_html/assets/css/site.css` | All site styles (including RTL rules) |
| `public_html/assets/js/site.js` | Menu, slider, counters, gallery, lightbox, table search, contact form |
| `public_html/assets/images/site/` | Logo, favicons and photography |
| `public_html/contact.php` | Contact / quote form handler (sends to info@hemamco.com) |
| `tools/` | Page generator — all page content (English + Arabic) lives here |
| `HEMAMCO_Logo_Package_2026-10-27/` | Official logo files in all formats |

## Editing content

The HTML pages are generated. Edit the text in `tools/build_site.py` (page text) or
`tools/data_bi.py` (services, projects, manpower, equipment), then rebuild:

```bash
python3 tools/build_site.py public_html
```

This rewrites all English and Arabic pages. Requires Python 3 only.

## Preview locally

```bash
cd public_html && python3 -m http.server 8000
```

Then open http://localhost:8000 (English) or http://localhost:8000/ar/ (Arabic).
