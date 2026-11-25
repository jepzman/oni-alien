# Handoff: Jef's Notes (start here)

Status as of **2026-11-17**. Books 1 and 2 are complete (six volumes each). **Book 3, *The Project Manager's Notebook*
(Sanne, the PMBOK Guide), is complete (six volumes)**: vols. 5 (Stakeholders, Risk: Antwerp) and 6 (tailoring, methods, growing) deployed together from branch `ccr-98bbf05d-6dvq28`; vols. 1–2 deployed in PR #24; vols. 3 (Scope, Schedule) and
4 (Finance, Resources) merged together after it. Vols. 5–6 are planned. `main` is the deployed branch; work on a branch and open a PR to `main`.

Read in this order:
1. This file: state, next steps, how to build/verify/deploy, gotchas.
2. `docs/larder-casebook.md`: the story's facts (source of truth for every Series 2 note).
3. The plan for the book you're writing:
   - Book 1 (Ana, architect): `docs/HANDOFF-solution-architect.md`
   - Book 2 (Grace, product owner): `docs/HANDOFF-product-owner.md`
   - **Book 3 (Sanne, project manager): `docs/HANDOFF-project-manager.md`** ← the book in progress; start at its section 16
   - Book 5 (Eli, IT operations): `docs/HANDOFF-it-operations.md` (complete, six volumes; section 12)

## 1. What's on the shelf

| Shelf | Journal key | Title | Notes |
| --- | --- | --- | --- |
| Series 1 (patterns) | `distributed`, `frontend`, `data`, `testing`, `security`, `cloud` | Vols. 1–6 | 111 |
| Series 1 (patterns) | `ddd` | Vol. 7 · Domain-Driven Design (with then &amp; now boxes) | 18 |
| Series 1 (patterns) | `inside-app` | Vol. 8 · Inside the Application (with then &amp; now boxes) | 18 |
| Series 1 (patterns) | `pipelines` | Vol. 9 · Data Pipelines &amp; Analytics (then &amp; now on 7 notes) | 18 |
| Series 2 · case file | `/larder/` (not a journal) | Meet Larder | history, cast, books, story timeline |
| Series 2 · Book 1 (Ana) | `architect-1` | From Requirements to Architecture | 15 |
| Series 2 · Book 1 (Ana) | `architect-2` | Decisions & Trade-offs | 15 (Mar → Sep 2026) |
| Series 2 · Book 1 (Ana) | `architect-3` | Communicating Architecture | 15 (Oct 2026 → Feb 2027) |
| Series 2 · Book 1 (Ana) | `architect-4` | Integration & the Enterprise Landscape | 15 (Mar → Sep 2027) |
| Series 2 · Book 1 (Ana) | `architect-5` | Designing for Qualities | 15 (Oct 2027 → Mar 2028) |
| Series 2 · Book 1 (Ana) | `architect-6` | Delivery, Governance & Influence | 15 (Apr → Sep 2028) |
| Series 2 · Book 2 (Grace) | `product-1` | Discovering the Problem | 15 |
| Series 2 · Book 2 (Grace) | `product-2` | Deciding What to Build | 15 (Jan → Apr 2026) |
| Series 2 · Book 2 (Grace) | `product-3` | From Idea to Backlog | 15 (Feb → Jun 2026) |
| Series 2 · Book 2 (Grace) | `product-4` | Measuring & Learning | 15 (May → Oct 2026) |
| Series 2 · Book 2 (Grace) | `product-5` | Stakeholders & Influence | 15 (Oct 2026 → Mar 2027) |
| Series 2 · Book 2 (Grace) | `product-6` | Growing the Product | 15 (Apr → Dec 2027) |

| Series 2 · Book 3 (Sanne) | `project-1` | The Lay of the Land (PMBOK foundations) | 15, 4 with deep dives (Jan → Feb 2026) |
| Series 2 · Book 3 (Sanne) | `project-2` | Starting, Steering, Closing (Governance) | 15, 4 with deep dives (Feb → May 2026) |
| Series 2 · Book 3 (Sanne) | `project-3` | What, and By When (Scope, Schedule) | 15, 4 going deeper (Feb → Apr 2026) |
| Series 2 · Book 3 (Sanne) | `project-4` | Money and People (Finance, Resources) | 15, 4 going deeper (Jan → May 2026) |
| Series 2 · Book 3 (Sanne) | `project-5` | People Outside, and Surprises (Stakeholders, Risk) | 15, 4 going deeper (Oct 2026 → Oct 2027, Antwerp) |
| Series 2 · Book 3 (Sanne) | `project-6` | Making It Yours (tailoring, methods, growing) | 15, 4 going deeper (Sep 2027 → Sep 2028) |

Book 3, *The Project Manager's Notebook*, covers the whole PMBOK Guide (eighth edition): plan, decisions and build notes in
`docs/HANDOFF-project-manager.md`. It adds the PMBOK map page (`/pmbok/`), a PMBOK tag on each note, the light / standard /
heavy dial, deep dives and the Rotterdam project file (`/rotterdam/`).

Planned: nothing left in Books 1–2 (`PLANNED_2` and `PLANNED_PRODUCT` are empty), nothing in Book 3 (`PLANNED_PROJECT` is empty),
Series 1 Vol. 10 AI App Patterns (`PLANNED`), Book 4 (Mo: client management, Korenwolf) in the future log.

**Series 1 Vol. 7 · Domain-Driven Design** (18 Nov 2026, branch `ccr-9390f8f0-wl14yb`): 18 notes in `content/ddd/`, skin `theme-ddd`,
ratings `CODE_ATTRS`, and a new **then &amp; now** box on every note (`then_now`, verdicts in `VERDICTS`). The owner chose to
continue Series 1 rather than start a new series, and moved AI App Patterns to Vol. 9. **Vol. 8 · Inside the Application** followed
on the same branch (`content/inside-app/`, skin `theme-app`): SOLID, the patterns inside your ORM, ports and adapters,
vertical slices, functional core, four classic GoF notes and a museum of retired patterns. Both volumes: `docs/PLAN-code-design.md`.
Also fixed: a related note with the same slug in another volume was silently not linked (`related_items`); three older
links now work (Ana's Strangler Fig ↔ Vol. 1, Sanne's Risk Register → Ana's).

**Series 1 Vol. 9 · Data Pipelines & Analytics** (25 Nov 2026, branch `ccr-6c2fb384-1vaty7`): 18 notes in `content/pipelines/`
(four files, one per collection), skin `theme-pipelines` (green-bar printout: bands, sprocket holes, VT323 titles, “RUN COMPLETE”
stamp), ratings `PIPELINE_ATTRS`, cover `copier` on a `greenbar` cloth. The owner moved it ahead of AI App Patterns (now Vol. 10),
kept the homeware-shop example from deep dive 12 and the proposed look. Then &amp; now boxes on seven notes, without the journal-wide
`then_now` flag (only some notes are old ideas). Deep dive 12 links back from incremental extract, idempotent loads and layered zones.
Plan: `docs/PLAN-data-pipelines.md`.

**Series 3 · Deep dives** started on 14 Nov 2026: Season 1 is written (`/deep-dives/<slug>/`), and Season 2 has begun with Sign-in, Tokens & Sessions, Replication, Failover & Leader Election, Sharding & Partitioning, Indexes & Query Plans, Rendering on the Web and From App Database to Warehouse, History in the Warehouse, One Number Everywhere, Data Quality & Pipeline Observability (plan for the data-engineering run, and the Data Warehouse cheat sheet: `docs/PLAN-data-pipelines.md`). Season 1: Saga, Reliable Messaging, The Resilience Stack, Event Sourcing & CQRS
Caching and Zero-Downtime Change, all deployed. Working branch `claude/design-patterns-deep-dive-ggw0on`. Read `docs/HANDOFF-deep-dives.md` for the plan and format.

## 1b. In progress: improving the earlier books (2026-11-16)

Plan: `docs/PLAN-improve-earlier-books.md` (approved 15 Nov; progress in its section 8). Branch `ccr-5ac82ff1-8gn15m`.
Series 1 is revised: linked related notes, seen-at-Larder and cheat-sheet asides, a situational question and a try it on
all 93 notes, 24 going-deeper chapters (4 per volume, in `content/<key>/deeper.py`), and new covers (sticker + printed
cloth, `COVER_ART`). 18 extra notes (3 per volume, `content/<key>/05_extra.py`) are on the branch. Next: the freshness pass, then Vol. 7.

## 2. Next steps (owner's decisions)

1. **Open item:** the owner reported Grace's cover and pages looked broken right after PR #7. Locally they render
   fine; the likely cause was a stale cached `bujo.css`, fixed in PR #8 (content-hash `?v=` on assets). **Ask the owner
   to confirm** it now looks right; if not, ask for a screenshot (the sandbox can't open github.io).
2. **Books 1 and 2 are complete** (PR #16 deployed both Vol. 6s).
3. **Book 3 is complete** (sections 17–18 of `docs/HANDOFF-project-manager.md`). Next: the Book 3 cheat sheets (PMBOK 8 on one
   page, earned value, critical path) and Book 4 (Mo, client management). Three questions are waiting for the owner there
   (section 13.1): check PMBOK names against the guide, full ten-chapter deep dives for key items, and a look at the live pages. Book 4 (Mo, client management) is in the future log; they should reuse the casebook, the case file timeline and the meanwhile links.
   New journal keys get their shelf cover automatically (CSS matches `book--architect-*` / `book--product-*`).
4. For each new volume: add every note to the case file `TIMELINE` (`content/larder/casefile.py`, tag `"1"`, `"2"` or `"3"`),
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
4. PDFs: in the cloud sandbox run `CHROMIUM_PATH=/opt/pw-browsers/chromium npm run pdf` (the pinned Playwright can't
   find its own browser there). `PDF_JOURNALS=testing,data` limits a local run. PDFs are not committed.
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

### Added on 2026-11-16 (Series 1 revisions)

- Add to a finished note through `content/<key>/revisions.py` or `deeper.py` (`REVISIONS = {slug: {...}}`), not by editing
  the note: `quiz_add` appends (tagged “what would you do?”), any other field replaces. Hand-made notes get the same blocks
  injected by `stamp_handmade`.
- Text in content is raw HTML: escape example markup (`&lt;img …&gt;`). A raw `<img onerror=…>` in a try it ran on the page.
- A build prints related entries that match no note (`[links]`); add a `RELATED_ALIASES` entry when a note exists under another name.
- After resolving a merge, grep `public/assets/*.css` for `<<<<<<<` / `=======`: a stray marker silently drops the next rule.

### Added on 2026-11-15 (Book 3)

- A local preview for checks: `cd public && python3 -m http.server 8765` (run it in the background; it stops after a while).
  Playwright is pre-installed: `require('playwright')`, `chromium.launch()` with no options.
- Shell commands that combine a heredoc with file moves can be refused by the sandbox's removal check. Write scripts with
  the file tool and run them; don't delete scratch folders.
- Before deploying, **fetch and merge `main`**: other sessions merge to it too. The generated `public/` files conflict by
  the hundred; resolve the source conflict (`scripts/build_notes.py`), rebuild, `git add -A`.
- A deploy renders only the PDFs that changed (fingerprints in `.pdf-cache/manifest.json`, kept in the Actions cache), so most deploys take a few minutes. A stylesheet change, a change to `scripts/build-pdf.mjs`, a Playwright upgrade or an evicted cache means a full rebuild (about 15 minutes). Force one with “Run workflow” → “Render every PDF again”. To render only chosen PDFs, edit `pdf-build.json` at the root: `rebuild` lists journal keys (or single PDF paths) that are always rendered; `only_listed: true` renders nothing else and copies every other PDF from the cache, even if its page changed (those stay marked out of date, and the run log lists them as “kept, out of date”). Set `only_listed` back to `false` to catch up. Check with `npm run pdf -- --dry-run`. The run does not appear in the Actions list for the
  first seconds after a merge.
- Doodle text: use `Doodle.row()` for rows of boxes; with 5 boxes keep labels under 12 characters, with 4 under 15.
- **Doodle font sizes are fixed by the stylesheet** (`.t` 19px, `.t-head` 21px, `.t-s` 21px): the `size=` argument has
  never changed what the browser shows, in any book. For a dense figure, create it with `Doodle(..., exact=True)` and the
  sizes become inline styles that do apply (added 16 Nov; off by default, so older figures are unchanged). Book 3 Vol. 3
  uses it on its network drawings, the WBS tree and the acceptance log.

## 6. Recent PRs

| PR | What |
| --- | --- |
| #5 | Book 1 Vol. 1 (Ana) + Series 2 shelf + ADR sample |
| #6 | Case file, Grace/Sanne/Mo/Korenwolf, template-card and T-chart fixes |
| #7 | Book 2 Vol. 1 (Grace), product skin, Meanwhile links |
| #8 | Content-hash version tags on assets (stale stylesheet after deploys) |
| #9 | Book 1 Vol. 2 (Ana): 14 notes, timeline, casebook ADRs 0008–0014 |
| #10 | Book 2 Vol. 2 (Grace): 15 notes, timeline, casebook facts |
| #11 | Book 1 Vol. 3 (Ana) + shelf cover fix for later volumes |
| #12 | Product skin: cork desk and index-card rules (they never rendered before) |
| #13 | Book 2 Vol. 3 (Grace): 15 notes, Noor, timeline, casebook facts |
| #14 | Book 1 Vol. 4 (Ana, ADRs 0018–0024) + Book 2 Vol. 4 (Grace): 30 notes, timeline, casebook |
| #15 | Book 1 Vol. 5 (Ana, ADRs 0025–0026) + Book 2 Vol. 5 (Grace): 30 notes, timeline, casebook |
| #16 | Book 1 Vol. 6 (Ana, ADRs 0027–0029) + Book 2 Vol. 6 (Grace): 30 notes; both books complete |
| #17–#23 | Cheat sheets, the Deep dives series (six ten-chapter pages), landing page with spine shelves (other sessions) |
| #24 | Book 3 Vols. 1–2 (Sanne): 30 notes, PMBOK map, Rotterdam project file, binder skin, Book 3 spine shelf |
