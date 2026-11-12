# Handoff: The Solution Architect's Notebook (Series 2, Book 1)

Status as of 2026-11-12: **planned, sample chapter built, nothing deployed.**

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
| 5 | Designing for Qualities | **Size & speed**: Back-of-the-Envelope Estimation ★, Capacity Planning, Load Profiles, Performance Budgets · **Availability**: Availability Maths ★, Failure Mode Analysis, DR Tiers, When to Go Multi-Region · **Security & compliance**: Security Architecture Review ★, Data Classification & Residency, Compliance by Design · **Cost & balance**: Total Cost of Ownership ★, Cost-Aware Architecture, Green Software, Quality Attribute Utility Tree |
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

Drafting sheet: warm tracing paper, double frame inset 14 px, no grid; Architects Daughter for
`--f-letter`; graphite #2B2B2B, terracotta accent #C0643B, slate teal gains #2F7A78, brick losses
#B23A2E, sand tape; leader-line-with-dot title mark; “REV A” tag on the TL;DR; circled section numbers;
template card with a “TEMPLATE” tab and ruled lines; dashed “try it” box; title block. Dark mode and
print variants included. Cover (not yet used): charcoal #2E3440, copper band #C27C4E.

## 5. Build checklist for the next session

1. [ ] Decide the open questions (section 6) with the owner.
2. [ ] **Series support on the landing page**: add `series` to journals (1 = patterns, 2 = practitioner
       notebooks); render a second shelf “Series 2 · The Practitioner's Notebooks” under the first, with
       covers using `--cover-architect` / `--band-architect` and labels “book 1 · vol. N”.
3. [ ] Rename keys if wanted (`architect-1` … `architect-6`; URLs `/architect-N/`). Keys must stay flat:
       page depth assumptions (`../`) break with nested folders.
4. [ ] For each volume: add the `JOURNALS` entry (copy `architect-2`, remove `draft=True` when ready),
       full 15-note catalogue, write `content/architect-N/01_….py` … `04_….py` (4 collections).
5. [ ] Write `docs/larder-casebook.md` first, then Vol. 1, then Vol. 2 (ADR note already done).
6. [ ] Update `PLANNED` / `FUTURE_LOG`, README volume table.
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

## 6. Open questions

- Keep Vol. 7 · AI App Patterns in Series 1, or end Series 1 at Vol. 6?
- One book with six volumes (as planned) or six thinner books? (Affects shelf layout only.)
- Is the fictional Larder case study welcome, or should examples stay generic?
- Should Books 2–4 (Product, Project, Client Management) get their own paper styles, or share the
  drafting sheet with a different palette?
- Publish the sample chapter publicly as a teaser (remove `draft=True`) or keep it unlisted?
