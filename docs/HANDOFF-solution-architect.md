# Handoff: The Solution Architect's Notebook (Series 2, Book 1)

Status as of 2026-11-13: **Vols. 1–5 written and deployed (15 notes each).**

- Shareable plan (Claude Docs, private until shared by the owner): https://claude.ai/artifact/GF641a5WavDf4mpNx8bKH1
- Sample chapter (draft, unlisted): `public/architect-2/notes/adr.html` — preview with `npm run serve`, then open http://localhost:8080/architect-2/notes/adr.html
- Content of the sample: `content/architect-2/01_recording.py`

This file is self-contained: a new session can build the series from it without the doc.

## 1. What the series is

The design-pattern shelf (Vols. 1–6, 93 notes) is Series 1. Series 2 is a set of notebooks on the work
*around* the code. Book 1 is **The Solution Architect's Notebook**: six volumes × 15 notes, written in
the same eight-section note format, adapted for work whose output is decisions and documents.
Books 2–4 (Product Management, Project Management, Client Management) are announced in the future log
and should reuse everything built here.

## 2. Volumes and topics (★ = write first)

| Vol. | Title | Collections → notes |
| --- | --- | --- |
| 1 | From Requirements to Architecture | **Understanding the problem**: Stakeholder Map ★, Business Drivers & Goals, System Context Diagram ★, Domain Discovery (Event Storming) · **Requirements that shape architecture**: Architecturally Significant Requirements ★, Quality Attribute Scenarios ★, Constraints vs Assumptions, NFR Checklist · **First shapes**: Architecture Styles Compared, Modular Monolith First, Bounded Contexts ★, Walking Skeleton · **Validating early**: Spike vs Prototype vs PoC, Fitness Functions, Risk-Storming |
| 2 | Decisions & Trade-offs | **Recording decisions**: Architecture Decision Records ★ (DONE, sample), Decision Log, RFCs & Design Docs, Decision Rights (RACI/DACI) · **Choosing well**: Options Analysis ★, Trade-off Sliders, One-way vs Two-way Doors ★, Last Responsible Moment · **Big choices**: Build vs Buy vs Open Source ★, Technology Evaluation, Choosing a Cloud Service Model, Technology Radar · **Living with decisions**: Technical Debt Register, Exit Plans & Reversibility, Revisiting Decisions |
| 3 | Communicating Architecture | **Diagrams**: C4 Model ★, Views & Viewpoints (4+1), Sequence & Flow Diagrams, Deployment Diagrams · **Documents**: Architecture One-Pager ★, arc42 Template, Docs as Code, Solution Design Document Done Right · **Conversations**: Whiteboard Sessions, Presenting to Executives ★, Explaining Trade-offs to Non-Engineers, Architecture Katas · **Keeping it current**: Living Diagrams, Architecture Roadmap, Glossary & Ubiquitous Language |
| 4 | Integration & the Enterprise Landscape | **Integration styles**: Choosing an Integration Style ★, API-First Design, Event-Driven Integration, Batch & File Transfer · **Boundaries**: Anti-Corruption Layer ★, Backend for Frontend, API Versioning Strategy, Canonical Data Model (and its traps) · **The landscape**: Capability Map ★, Application Portfolio (TIME), Data Ownership & Master Data, Identity Federation & SSO · **Changing the landscape**: Strangler Fig Migration ★, Transition Architectures, SaaS & Vendor Integration |
| 5 | Designing for Qualities (done) | **Size & speed**: Back-of-the-Envelope Estimation ★, Capacity Planning, Load Profiles, Performance Budgets · **Availability**: Availability Maths ★, Failure Mode Analysis, DR Tiers, When to Go Multi-Region · **Security & compliance**: Security Architecture Review ★, Data Classification & Residency, Compliance by Design · **Cost & balance**: Total Cost of Ownership ★, Cost-Aware Architecture, Green Software, Quality Attribute Utility Tree |
| 6 | Delivery, Governance & Influence | **Architecture in delivery**: Just-Enough Up-Front Design ★, Evolutionary Architecture, The Architecture Backlog · **Governance**: Architecture Principles ★, Guardrails Not Gates ★, Lightweight Architecture Review, Golden Paths · **Risk & transition**: Risk Register, Migration Planning, Go-Live Readiness, Handover to Operations · **Influence**: Influencing Without Authority ★, Negotiating with Stakeholders, Discovery Workshops, Growing Other Architects |

Rule: don't repeat pattern-shelf notes (CQRS, saga, SLOs, threat modelling, IaC…). Architect notes cover
*when and why* to choose them and link the pattern note for *how*.

## 3. Note format (what's already implemented)

Same eight sections and data shape as `content/<journal>/*.py` notes, with these journal options
(all implemented in `scripts/build_notes.py`, see the `architect-2` entry in `JOURNALS`):

| Option | Effect |
| --- | --- |
| `problem_h2="The situation"` | Section 1 is a project scene from the Larder case study |
| `map_caption`, `map_col` | “Translating it to the job” / “On the project” |
| `related_h3="Related notes"` | — |
| note `code` with `plain=True` | Template card: no syntax highlighting (Markdown templates) |
| note `try_it` | “Try it” exercise box after the quiz |
| `title_block=True`, `book=…` | Engineer's title block (book, vol., sheet, rev., drawn by) at the end of each note |
| note `rev` | Revision letter in the title block (default “A”) |
| `fonts="Architects+Daughter"` | Extra Google Font loaded only for this journal |
| `draft=True` | Rendered to `public/<key>/` but **not** on the landing shelf, not in `journals.json`, no PDFs |

Ratings: `ARCHITECT_ATTRS` — Clarity, Stakeholder alignment, Decision speed, Risk reduction,
Adaptability, Traceability, Cost awareness, Low overhead (high = light), Team autonomy.

**Running case study:** every note uses **Larder**, a grocery delivery start-up growing from one city to
six (Rotterdam launch, orders → delivery via Postgres outbox, see ADR 0007 in the sample). Keep a
`docs/larder-casebook.md` with the facts you invent so notes stay consistent.

## 4. Style (implemented as `.theme-architect` in `public/assets/bujo.css`)

Drafting sheet, vibrant version (owner asked for more colour and depth):

- Paper: warm white #FFFDF7 on a sand desk #EFE6D6, a faint cobalt blueprint grid (24 px minor,
  120 px major), a double frame inset 14 px, and a small stack of sheets drawn underneath (shadow).
- Palette: ink #24211E · vivid orange accent #EE6A2F · teal gains #0E9A8A · red losses #D64545 ·
  cobalt pen #2753C9 · yellow highlighter rgba(255, 214, 0, .45) · tapes in orange, teal and yellow.
- Fonts: Architects Daughter for `--f-letter` (titles, section heads); body fonts unchanged.
- Marks: leader line with a dot under the title; “REV A” tag and a paperclip on the TL;DR; circled
  section numbers on a highlighter swipe; orange drop cap.
- Depth and doodles: every figure is taped on like a photo (tilted ±0.3°, tape in rotating colours);
  desk doodles around the sheet (`sheet_doodles=True` → `SHEET_DOODLES` in `build_notes.py`): a coffee
  ring, a drafting compass, a pencil on a ruler. Hidden under 760 px; coffee ring and stack hidden in print.
- Template card with a “TEMPLATE” tab and ruled lines; dashed “try it” box; title block.
- Dark mode and print variants included. Cover (not yet used): charcoal #2E3440, copper band #C27C4E.

## 5. Build checklist for the next session

1. [x] Open questions decided (section 6).
2. [x] **Series support on the landing page**: add `series` to journals (1 = patterns, 2 = practitioner
       notebooks); render a second shelf “Series 2 · The Practitioner's Notebooks” under the first, with
       covers using `--cover-architect` / `--band-architect` and labels “book 1 · vol. N”.
3. [x] Keys are `architect-1`, `architect-2`, … (decided). Rename keys if wanted (`architect-1` … `architect-6`; URLs `/architect-N/`). Keys must stay flat:
       page depth assumptions (`../`) break with nested folders.
4. [~] For each volume (Vols. 1–4 done): add the `JOURNALS` entry (copy `architect-2`, remove `draft=True` when ready),
       full 15-note catalogue, write `content/architect-N/01_….py` … `04_….py` (4 collections).
5. [x] Write `docs/larder-casebook.md` first, then Vol. 1 (done), then Vol. 2 (ADR note already done).
6. [x] Update `PLANNED` / `FUTURE_LOG`, README volume table.
7. [ ] Verify (same routine used for Vols. 3–6):
       - build: `python3 scripts/build_notes.py`
       - doodles: screenshot every `figure.fig svg` and review them as contact sheets; fix overlaps
       - phone width 375 px: no element wider than the viewport (long inline `<code>` is the usual culprit)
       - light, dark and print look right
       - PDFs: `npm run pdf`. In the cloud sandbox the pinned Playwright 1.48 can't find its browser;
         run a copy of `scripts/build-pdf.mjs` with `chromium.launch({ executablePath: '/opt/pw-browsers/chromium' })`
       - the workflow's “every page and PDF exists” check (see `.github/workflows/pages.yml`)
8. [ ] Commit on the working branch, push, open a PR to `main`, merge = deploy to GitHub Pages and the
       Cloudflare Worker mirror. Only deploy when the owner asks.

## 6. Decisions (accepted by the owner, 2026-11-12)

- **Vol. 7 · AI App Patterns stays** in Series 1, planned for December.
- **One book, six volumes**, matching the existing shelf and covers.
- **Use the Larder case study** throughout; keep `docs/larder-casebook.md` as the source of truth.
- **Books 2–4 each get their own skin** (as Vols. 1–6 do), sharing the title block and “Try it” box.
- **Keep the sample chapter unlisted** (`draft=True`) until Vol. 1 is written; launch them together.

## 7. Vol. 1 notes on the build (2026-11-12)

- Content: `content/architect-1/01_understanding.py` … `04_validating.py`; Larder facts in `docs/larder-casebook.md`
  (Vol. 1 runs October 2025 → January 2026; ADRs 0001–0006 are referenced but only 0007 is written out).
- Journal flags: `series=2` puts a journal on the second shelf; `in_progress=True` labels the cover “N notes · in progress”.
  `PLANNED_2` lists the planned Series 2 volumes. `draft=True` still works for unlisted drafts.
- Doodle text width in this skin: headings ≈ 0.65 × font size per character, body ≈ 0.5 ×, scribbles ≈ 0.45 ×.
  Budget box widths with that, and check every figure on a contact sheet.
- Vol. 2 done: see section 9.

## 8. The case file and book 2 (2026-11-12)

- **Case file** (`/larder/`, “Meet Larder”, first on the Series 2 shelf): premise, history, October 2025 numbers, goals and
  drivers, Larder for Business, the cast, the four books with summaries, and a story timeline with every note pinned to its
  date. Data: `content/larder/casefile.py` (add each new note to `TIMELINE`). Rendered by `render_casefile()`.
- **“The story so far”** box on each Series 2 book index: the journal's `story` field.
- **Book 2 narrator: Grace**, product owner for ordering and the customer apps, joins 13 October 2025 (Ana: 6 October).
  Same meetings as Ana, other side: “should we, and for whom?”. Book 3: Sanne (delivery manager, Jan 2026, Rotterdam
  launch). Book 4: Mo (key account manager, Mar 2026) and the client **Korenwolf Group** (Hanna, Ruben). All in the casebook.
- Fixed: template-card headers no longer overlap on phones; wide templates fit the card; the gains/losses divider is
  hidden when stacked and joins the underlines on wide screens (all journals).

## 9. Vol. 2 notes on the build (2026-11-12)

- Content: `content/architect-2/01_recording.py` (ADR, decision log, RFCs, decision rights), `02_choosing.py` (options
  analysis, trade-off sliders, one-way vs two-way doors, last responsible moment), `03_big.py` (build vs buy, technology
  evaluation, cloud service model, technology radar), `04_living.py` (technical debt register, exit plans, revisiting decisions).
- Story runs **March → September 2026**; every new fact (ADRs 0008–0014, the Korenwolf pilot details, Antwerp's planning date
  of September 2027, StockPilot's per-store pricing letter, 14 → 18 engineers) is in the casebook section “Book 1, Vol. 2”.
- No `meanwhile` links yet: Grace's Vol. 1 ends in January 2026. Suggested pairs for **Grace's Vol. 2** (Jan → Apr 2026):
  Saying No ↔ options analysis (Korenwolf pilot by hand) or one-way doors; Now/Next/Later roadmap ↔ trade-off sliders
  (31 Mar, Grace is in the room; approvals go to Amsterdam first); Cost of delay ↔ last responsible moment; Business case
  one-pager ↔ build vs buy (billing). Write them on Grace's side; the reverse boxes appear on Ana's notes automatically.
- Open threads for later volumes: ADR 0014 (business ordering, proposed Sep 2026), ADR 0012 on watch (Rotterdam 91 % on
  time), StockPilot renewal decision by 31 Dec 2026, Antwerp decision calendar, TD-1 before Utrecht prep (Oct 2026).
- Next for book 1: Vol. 3, Communicating Architecture (after Grace's Vol. 2).

## 10. Vol. 3 notes on the build (2026-11-13)

- `architect-3` journal; content in `content/architect-3/01_diagrams.py`, `02_documents.py`, `03_conversations.py`,
  `04_current.py`. Story runs **October 2026 → February 2027**; facts in the casebook, “Book 1, Vol. 3”, including
  ADRs 0015–0017 and the 2027 planning dates (Utrecht Apr, The Hague Jun, Antwerp Sep, Eindhoven Nov).
- The ADR sample's hypothetical “0015 supersedes 0007” became “0031” so it doesn't clash with the real ADR 0015.
- No `meanwhile` links: Grace's notes don't reach these months yet. Candidates for her Vol. 5–6: Pitching to the CEO ↔
  presenting to executives; Working with the architect ↔ explaining trade-offs; B2B vs B2C (Korenwolf) ↔ glossary or the
  solution design document; Launching a new city ↔ architecture roadmap.
- Next for book 1: Vol. 4, Integration & the Enterprise Landscape (after Grace's Vol. 3).

## 11. Vol. 4 notes on the build (2026-11-13)

- `architect-4` journal; content in `content/architect-4/01_styles.py`, `02_boundaries.py`, `03_landscape.py`,
  `04_changing.py`. Story runs **March → September 2027**; facts in the casebook, “Book 1, Vol. 4”, with ADRs 0018–0024.
- Utrecht (12 Apr) and The Hague (14 Jun) are now actual openings; Antwerp (Sep) and Eindhoven (Nov) stay planning dates.
- No `meanwhile` links: Grace's notes don't reach 2027 yet (her Vol. 6 might: launching a new city ↔ strangler fig or
  capability map; B2B vs B2C ↔ API-first design or API versioning).
- Next for book 1: Vol. 5, Designing for Qualities (after Grace's Vol. 4).

## 12. Vol. 5 notes on the build (2026-11-13)

- `architect-5` journal; content in `content/architect-5/01_size.py`, `02_availability.py`, `03_security.py`,
  `04_cost.py`. The Security & compliance collection has 3 notes (as planned), so the volume has 15.
- Story runs **October 2027 → March 2028**; facts in the casebook, “Book 1, Vol. 5”, with ADRs 0025 (billing off the
  ordering path) and 0026 (one region with triggers, revisits ADR 0017). Antwerp opened 18 Oct 2027, Eindhoven 22 Nov 2027.
- No `meanwhile` links (Grace's notes end in 2027). Reverse references: compliance by design → Grace's “working with
  legal & privacy”.
- Next for book 1: Vol. 6, Delivery, Governance & Influence.
