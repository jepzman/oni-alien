# Margin Notes

A shelf of student bullet journals on software design patterns. Every note covers the problem a pattern solves, a real-life analogy with doodles, how it works, gains vs losses, nine ratings, common pitfalls, when to use it, and a self-check quiz.

Live site: https://jepzman.github.io/oni-alien/

| Volume | Journal | Notes | Paper / palette | Ratings |
|---|---|---|---|---|
| 1 | Distributed Design Patterns (`/distributed/`) | 18 | dot grid, mustard / sage / dusty pink | architecture characteristics (simplicity, cost, deployability, testability, scalability, elasticity, fault tolerance, performance, evolvability) |
| 2 | Frontend Design Patterns (`/frontend/`) | 15 | square grid, lavender / teal / coral | frontend qualities (simplicity, reusability, testability, maintainability, performance, bundle size, accessibility, developer experience, team scalability) |

The landing page (`/`) shows the shelf, planned volumes and a “future log” of upcoming work.

## Layout

- `public/`: the static site (deployed as is)
  - `index.html`: the landing page (generated)
  - `<journal>/index.html`, `<journal>/all.html`, `<journal>/notes/*.html`: each journal (generated, except the hand-made Vol. 1 notes `circuit-breaker.html` and `saga.html`)
  - `assets/notebook.css` (base), `assets/bujo.css` (bullet journal skin + journal themes), `assets/notebook.js`
  - `journals.json`: everything the PDF script needs (generated)
  - `notes/*.html`, `all.html`: redirects from the old Vol. 1 URLs
- `content/<journal>/*.py`: note content as data, including the doodles
- `scripts/build_notes.py`: journal configs (`JOURNALS`, `PLANNED`, `FUTURE_LOG`) and the page templates
- `scripts/doodle.py`: the hand-drawn SVG helpers, icon library and code highlighter
- `scripts/build-pdf.mjs`: builds `public/<journal>/pdf/` (one PDF per note + the whole journal) with Playwright

## Editing

```bash
python3 scripts/build_notes.py      # after changing content/ or a journal config
npm install && npm run pdf          # optional: build the PDFs locally
npm run serve                       # preview on http://localhost:8080
```

- **Add a pattern:** add it to the journal's `catalogue` in `scripts/build_notes.py`, write its data in `content/<journal>/` (copy an existing note), and run the build.
- **Add a journal:** add an entry to `JOURNALS` (key, vol, title, theme, collections, catalogue, attrs), create `content/<key>/`, add a theme block in `assets/bujo.css` and cover colours (`--cover-<key>`, `--band-<key>`), and remove it from `PLANNED`.
- **Update plans:** edit `PLANNED` and `FUTURE_LOG`.

## Publishing (GitHub Pages)

`.github/workflows/pages.yml` runs on every push to `main`: it installs Chromium, builds the PDFs for every journal, checks every page and PDF exists, and deploys `public/` to GitHub Pages. PDFs are not committed. You can also run it from the Actions tab (“Run workflow”).
