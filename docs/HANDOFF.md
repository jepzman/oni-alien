# Handoff: Jef's Notes (start here)

Status as of **2026-11-12, 14:20 UTC**. Everything below is merged to `main` and deployed (last deploy: PR #8).
Working branch: `claude/design-patterns-notebook-site-6p22em` (even with `main` apart from this file).

Read in this order:
1. This file: state, next steps, how to build/verify/deploy, gotchas.
2. `docs/larder-casebook.md`: the story's facts (source of truth for every Series 2 note).
3. The plan for the book you're writing:
   - Book 1 (Ana, architect): `docs/HANDOFF-solution-architect.md`
   - Book 2 (Grace, product owner): `docs/HANDOFF-product-owner.md`

## 1. What's on the shelf

| Shelf | Journal key | Title | Notes |
| --- | --- | --- | --- |
| Series 1 (patterns) | `distributed`, `frontend`, `data`, `testing`, `security`, `cloud` | Vols. 1–6 | 93 |
| Series 2 · case file | `/larder/` (not a journal) | Meet Larder | history, cast, books, story timeline |
| Series 2 · Book 1 (Ana) | `architect-1` | From Requirements to Architecture | 15 |
| Series 2 · Book 1 (Ana) | `architect-2` | Decisions & Trade-offs | **1 of 15** (ADR), `in_progress=True` |
| Series 2 · Book 2 (Grace) | `product-1` | Discovering the Problem | 15 |

Planned: Book 1 vols. 3–6 (`PLANNED_2`), Book 2 vols. 2–6 (`PLANNED_PRODUCT`), Series 1 Vol. 7 AI App Patterns
(`PLANNED`), Books 3–4 (Sanne: project management; Mo: client management, Korenwolf) in the future log.

## 2. Next steps (owner's decisions)

1. **Open item:** the owner reported Grace's cover and pages looked broken right after PR #7. Locally they render
   fine; the likely cause was a stale cached `bujo.css`, fixed in PR #8 (content-hash `?v=` on assets). **Ask the owner
   to confirm** it now looks right; if not, ask for a screenshot (the sandbox can't open github.io).
2. **Alternate volumes between the books.** Next: **Ana's Vol. 2, Decisions & Trade-offs**: write the other 14 notes
   (catalogue in `docs/HANDOFF-solution-architect.md` §2), March 2026 onward in the story; then drop `in_progress`.
3. Then **Grace's Vol. 2, Deciding What to Build** (`product-2`; topics in `docs/HANDOFF-product-owner.md` §2).
   Seeds already planted: the parked ML recipe idea (Femke) → “Saying No”; Korenwolf pilot (May 2026).
4. For each new volume: add every note to the case file `TIMELINE` (`content/larder/casefile.py`, tag `"1"` or `"2"`),
   add `meanwhile` links where the two books share a scene, record new facts in the casebook, update the future log.
5. Deploy only when the owner asks (see §4).

## 3. How it's built

- `python3 scripts/build_notes.py` renders everything from `content/<key>/*.py` and the `JOURNALS` list.
- Series 2 journal fields: `series=2`, `book`, `book_no`, `narrator`, `brand`, `story` (the “story so far” box),
  `title_block`, `sheet_doodles` (`True`/`"architect"` or `"product"`), `theme`, `fonts`, `in_progress`, `draft`.
- Note fields beyond Series 1: `problem_h2="The situation"`, `code` with `plain=True` (template card), `try_it`,
  `meanwhile=[(journal_key, slug, line_here, line_there)]` (renders on both notes), `rev`.
- Skins in `public/assets/bujo.css`: `.theme-architect` (drafting sheet), `.theme-product` (product board),
  `.casefile`, `.story`, `.meanwhile`; covers `--cover-architect`, `--cover-product`, `.book--casefile`.
- Asset links get `?v=<content hash>` automatically (`asset()` in `build_notes.py`); the two hand-made Vol. 1 notes
  are re-stamped on every build. Never hard-code `assets/bujo.css` in a template.

## 4. Verify and deploy (the routine every volume used)

1. Build. Then screenshot **every figure** and review them as contact sheets (Playwright: open each note, screenshot
   each `figure.fig svg`, stack them with PIL). Fix overlaps.
   - Doodle text widths in these skins: headings ≈ **0.65 × font size** per character, body ≈ 0.5 ×, scribbles ≈ 0.45 ×.
     Budget box widths with that; split long labels into label + `sub`.
2. Phone check at 375 px on every new page: nothing wider than the viewport.
3. Light and dark mode on the index, one note and the landing shelf.
4. PDFs: the pinned Playwright 1.48 can't find its browser in the cloud sandbox. Run a copy of
   `scripts/build-pdf.mjs` with `chromium.launch({ executablePath: '/opt/pw-browsers/chromium' })` and `root` pointed
   at `public/` (and `NODE_PATH=$(npm root -g)`). PDFs are not committed.
5. The workflow's check: every page and PDF in `public/journals.json` exists.
6. Commit on the working branch, push, open a PR to `main`, merge when the owner asks: the merge **is** the deploy
   (`.github/workflows/pages.yml` → GitHub Pages + the Cloudflare Worker mirror). Watch the run with the GitHub
   Actions tools; it takes about 4–6 minutes.

## 5. Gotchas from this session

- The sandbox cannot reach `jepzman.github.io` (DNS fails, also through the web-fetch helper). Verify locally and
  through the Actions run; ask the owner for screenshots of the live site.
- Write multi-line Python fix-up scripts to a file (scratchpad) instead of a bash heredoc when the text has quotes
  or apostrophes; heredoc quoting broke one edit.
- When writing doodles, avoid placeholder constructs (`x if False else y`); write the final call directly.
- Keep Series 1 pages unchanged unless fixing a shared bug (the gains/losses divider fix touched all journals, on purpose).
- The story's dates and numbers must match the casebook exactly (e.g. 6.2 % baseline, 23,000 perfect orders/week,
  Rotterdam opens 27 Apr 2026, ADR 0002 on 8 Dec 2025).

## 6. Recent PRs

| PR | What |
| --- | --- |
| #5 | Book 1 Vol. 1 (Ana) + Series 2 shelf + ADR sample |
| #6 | Case file, Grace/Sanne/Mo/Korenwolf, template-card and T-chart fixes |
| #7 | Book 2 Vol. 1 (Grace), product skin, Meanwhile links |
| #8 | Content-hash version tags on assets (stale stylesheet after deploys) |
