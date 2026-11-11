# Margin Notes

A student's bullet journal on distributed design patterns: 18 notes in five collections (resilience, data consistency, communication, scaling data, coordination). Each note covers the problem, a real-life analogy with doodles, how the pattern works, gains vs losses, nine architecture ratings, common pitfalls, when to use it, and a self-check quiz.

Live site: https://jepzman.github.io/oni-alien/

## Layout

- `public/`: the static site (deployed as is)
  - `index.html`: the journal index (generated)
  - `all.html`: every note on one page for "Export as PDF" (generated; `all.html?print` opens the print dialog)
  - `notes/*.html`: one page per pattern
  - `assets/notebook.css`, `assets/bujo.css`: base styles and the bullet journal skin
  - `notes.json`: list of notes used by the PDF script (generated)
- `content/*.py`: note content as data, including the doodles
- `scripts/build_notes.py`: renders `content/` into `public/notes/`, plus `index.html`, `all.html`, `notes.json`
- `scripts/build-pdf.mjs`: builds `public/pdf/` (one PDF per note + the whole notebook) with Playwright

`circuit-breaker.html` and `saga.html` are hand-made pages; every other note is generated.

## Editing

```bash
python3 scripts/build_notes.py      # after changing content/ or the catalogue
npm install && npm run pdf          # optional: build the PDFs locally
npm run serve                       # preview on http://localhost:8080
```

To add a pattern: add it to `CATALOGUE` in `scripts/build_notes.py`, write its data in a `content/*.py` file (copy an existing note), and run the build.

## Publishing (GitHub Pages)

`.github/workflows/pages.yml` runs on every push to `main` (and to the current working branch): it installs Chromium, builds the PDFs, checks every page and PDF exists, and deploys `public/` to GitHub Pages. PDFs are not committed; the workflow builds them. You can also run it from the Actions tab ("Run workflow").

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
