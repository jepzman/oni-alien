# Jef’s Notes

A shelf of student bullet journals on software design patterns. Every note covers the problem a pattern solves, a real-life analogy with doodles, how it works, gains vs losses, nine ratings, common pitfalls, when to use it, and a self-check quiz.

Live site: https://jepzman.github.io/oni-alien/

| Volume | Journal | Notes | Paper / palette | Ratings |
|---|---|---|---|---|
| 1 | Distributed Design Patterns (`/distributed/`) | 18 | dot grid, mustard / sage / dusty pink | architecture characteristics (simplicity, cost, deployability, testability, scalability, elasticity, fault tolerance, performance, evolvability) |
| 2 | Frontend Design Patterns (`/frontend/`) | 15 | square grid, lavender / teal / coral | frontend qualities (simplicity, reusability, testability, maintainability, performance, bundle size, accessibility, developer experience, team scalability) |
| 3 | Data & Database Patterns (`/data/`) | 15 | ledger paper (ruled lines, double red margin), ledger green / burnt orange / sky blue | database qualities (simplicity, read speed, write speed, integrity, scalability, storage cost, query flexibility, operability, evolvability) |
| 4 | Testing Patterns (`/testing/`) | 15 | lab notebook ("+" cross grid, PASS stamp), raspberry / pass green / amber | test-suite qualities (simplicity, fast feedback, confidence, reliability, isolation, maintainability, realism, cost, scalability) |
| 5 | Security Patterns (`/security/`) | 15 | field dossier (manila, security-envelope crosshatch, redaction-bar titles, CONFIDENTIAL stamp), steel blue / crimson / khaki | security qualities (simplicity, usability, confidentiality, integrity, availability, containment, auditability, cost, developer experience) |
| 6 | Cloud & DevOps Patterns (`/cloud/`) | 15 | isometric grid paper (dimension-line titles, status pill), cobalt / sky / signal yellow | operations qualities (simplicity, delivery speed, release safety, reliability, scalability, recoverability, observability, cost, developer experience) |

**Series 2 · The Practitioner's Notebooks.** Book 1 is *The Solution Architect's Notebook* (drafting-sheet skin `theme-architect`: blueprint grid, Architects Daughter, orange / teal / cobalt, a title block on every sheet). Every note follows one case study, Larder: the public **case file** (`/larder/`, built from `content/larder/casefile.py`) introduces the company, its history, goals, cast, books and a story timeline, and each Series 2 book index opens with a “story so far” box (the journal's `story` field). The facts live in `docs/larder-casebook.md`; the plan for the book is `docs/HANDOFF-solution-architect.md`.

| Book · vol. | Journal | Notes | Ratings |
|---|---|---|---|
| 1 · 1 | From Requirements to Architecture (`/architect-1/`) | 15 | architect ratings (clarity, stakeholder alignment, decision speed, risk reduction, adaptability, traceability, cost awareness, low overhead, team autonomy) |
| 1 · 2 | Decisions & Trade-offs (`/architect-2/`) | 1 of 15 (in progress) | architect ratings |

The landing page (`/`) shows two shelves (Series 1: design patterns; Series 2: practitioner's notebooks, with `series=2` in `JOURNALS`), planned volumes (`PLANNED`, `PLANNED_2`) and a “future log” of upcoming work.

## Handoff

Start with `docs/HANDOFF.md`: current state, next steps, how to build, verify and deploy.

## Layout

- `public/`: the static site (deployed as is)
  - `index.html`: the landing page (generated)
  - `<journal>/index.html`, `<journal>/all.html`, `<journal>/notes/*.html`: each journal (generated, except the hand-made Vol. 1 notes `circuit-breaker.html` and `saga.html`)
  - `assets/notebook.css` (base), `assets/bujo.css` (bullet journal skin + journal themes), `assets/notebook.js`
  - `journals.json`: everything the PDF script needs (generated)
  - `notes/*.html`, `all.html`: redirects from the old Vol. 1 URLs
- `content/<journal>/*.py`: note content as data, including the doodles
- `scripts/build_notes.py`: journal configs (`JOURNALS`, `PLANNED`, `FUTURE_LOG`) and the page templates
- `scripts/doodle.py`: the hand-drawn SVG helpers (including `table()` for database tables), icon library and code highlighter (JS/TS, Python and SQL keywords)
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

`.github/workflows/pages.yml` runs on every push to `main`: it installs Chromium, builds the PDFs for every journal, checks every page and PDF exists, and deploys `public/` to GitHub Pages and to the Cloudflare Worker mirror (https://oni-alien.jepzman.workers.dev/, via `wrangler.jsonc`; needs the `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` repository secrets, and is skipped without them). PDFs are not committed. You can also run it from the Actions tab (“Run workflow”).
