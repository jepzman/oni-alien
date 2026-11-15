# Plan: improve the earlier books

Proposal of 2026-11-15. Nothing here is built yet. It covers the two finished practitioner books, Book 1 (Ana, 90 notes)
and Book 2 (Grace, 90 notes), with a short part on the Series 1 pattern volumes (93 notes).

The plan has three layers, cheapest first: **A** fixes made once in the generator, **B** section updates to existing
notes, **C** new notes and a seventh volume per book. Owner's decisions are in section 6.

## 1. What the audit found

Measured on `main` with a script over every content file (`content/<key>/*.py`).

| Finding | Numbers | Why it matters |
| --- | --- | --- |
| “Related notes” are plain text | 1,219 references in 303 notes, **0 are links** | The reader sees “Quality attribute scenarios (vol. 1)” and cannot click it. |
| Books 1–2 never link the cheat sheets | 0 links from 180 notes | The NFR Checklist note and the NFR cheat sheet don't know about each other. |
| Books 1–2 have recall-only quizzes | 4 questions per note; Book 3 has 5, two of them situational | Situational questions test judgment, which is what these books teach. |
| Books 1–2 have no “going deeper” chapters | 0 of 180 notes; Book 3 has 4 per volume | Key notes (ADR, C4, A/B tests) stop at the same depth as minor ones. |
| “Meanwhile” links thin out | Book 2: 15 in vol. 1, then 4, 3, 1, 3, 4 | The two books share scenes in every volume; later volumes rarely show it. |
| Template cards are scattered | 180 cards, no collected page; Book 3 has `/rotterdam/` | Ana's 29 ADRs and Grace's one-pagers would work as a sample document set. |
| No one-page map of a book | Book 3 has `/pmbok/` | No way to see “the whole job” and jump to a note. |
| Later volumes are shorter | Book 1: 452 words of prose in vol. 2 → 363 in vol. 6; Book 2: 439 → 350 | Vols. 5–6 are the first candidates for added depth. |
| The `rev` field is never used | 0 notes | Updated notes have no visible “revised” mark. |

Not measured, to check while editing: whether each collection of Books 1–2 has a narrator's mistake (a Book 3 rule),
and the wording of facts that Book 3 later made more exact (Rotterdam budget, milestones).

## 2. Layer A: fix once, every note gains

Generator work in `scripts/build_notes.py`. No note is rewritten.

1. **Link the related notes.** Resolve each `related` entry to a note by title (across all journals), render it as a
   link, and print the ones that don't resolve so they can be fixed by hand. Entries may stay as text if no note exists.
2. **Link to deep dives and cheat sheets from Series 2.** Extend the `DEEPER` map so Ana's notes point at the matching
   deep dive (Event-Driven Integration → Reliable Messaging, Migration Planning → Zero-Downtime Change, Failure Mode
   Analysis → The Resilience Stack) and add a “on a card →” line for cheat sheets (NFR Checklist → NFR Checklists).
3. **A “revised” mark.** Use the existing `rev` field: a small stamp in the title block and a line on the volume index
   (“revised Dec 2026: quiz, going deeper”), so returning readers see what changed.
4. **Fill in the “meanwhile” links** for Books 1–2, vols. 3–6, and add Sanne's side where Book 3 shares a scene. Source:
   the casebook sections per volume. Target: 4–6 per volume.

## 3. Layer B: section updates to the 180 notes

Each item carries Book 3's better ideas back. One volume is done first as a sample (see section 5).

| # | Update | Scope | Size |
| --- | --- | --- | --- |
| B1 | **Situational quiz question**: one “what does Ana / Grace do?” question per note, added to the four recall ones | all 180 notes | 180 questions |
| B2 | **Going deeper chapter** on the key notes: an intro and three or four numbered parts with their own figures | 3 per volume, 36 chapters | the largest item |
| B3 | **Light / standard / heavy dial**, added under the T-chart (not replacing it) on notes that are documents or ceremonies | about 20 notes per book | 40 dials |
| B4 | **Narrator's mistake**: one note per collection where the technique was skipped or overdone and what it cost | where missing | to be counted |
| B5 | **Depth pass on vols. 5–6** of both books: a second worked example or figure where a note is thin | about 20 notes | after B1–B2 |

**Going deeper candidates (B2).**

- Book 1: Quality Attribute Scenarios, Bounded Contexts, Risk-Storming · Architecture Decision Records, Options Analysis,
  Build vs Buy · C4 Model, Solution Design Document, Presenting to Executives · Choosing an Integration Style, Strangler
  Fig Migration, Data Ownership · Availability Maths, Capacity Planning, Total Cost of Ownership · Architecture
  Principles, Guardrails Not Gates, Go-Live Readiness.
- Book 2: Customer Interviews, Opportunity Solution Tree, North Star Metric · RICE & ICE, Cost of Delay, Business Case
  One-Pager · Story Mapping, User Stories that Work, Launch Checklist · A/B Tests, Cohorts & Retention, OKRs · The
  One-Page PRD, Negotiating Scope, Delivering Bad News · Pricing Experiments, B2B vs B2C, Platform Thinking.

**Dial candidates (B3).** ADR, RFCs, arc42, Solution Design Document, Technology Radar, Architecture Review, Risk
Register, Go-Live Readiness; PRD, Roadmaps, OKRs, Quarterly Product Review, Definition of Ready & Done, Launch Checklist.

## 4. Layer C: new pages, new notes, a seventh volume

### 4.1 New pages (generated, like Book 3's)

1. **The Larder architecture file** (`/larder-architecture/`): every template card of Book 1 in order, with the ADR log
   0001–0029 as its spine. `render_project_file()` already does this for Book 3; it needs a second file prefix and a title.
2. **The Larder product file** (`/larder-product/`): Grace's cards: strategy on a page, the roadmap, PRDs, test plans, reviews.
3. **A map per book**: “the architect's job on one page” and “the product owner's job on one page”: the questions of
   the job, grouped by phase, each linked to its note. Same layout as `/pmbok/`, no external standard needed.
4. **The Series 2 timeline** (already in the future log): every Larder note of all three books on one timeline, filtered
   by narrator. The case file `TIMELINE` has the data.

### 4.2 Book 1, Vol. 7: Teams, Data & AI (proposal, 15 notes)

Topics the six volumes don't cover. Story: October 2028 → mid 2029, after the sixth city, Ana as lead architect.

- **Teams and the system**: Conway's Law · Team Topologies · Cognitive Load and Platform Teams · Inner Source
- **Data for decisions**: Operational vs Analytical Data · Data Products and Contracts · Reporting Architecture · Data Quality Ownership
- **AI in the architecture**: Where a Model Fits · Build, Buy or Call a Model · Evaluating an AI Feature · Human in the Loop
- **Running what you designed**: Observability by Design · SLOs as Requirements · From Incident to Architecture Change

### 4.3 Book 2, Vol. 7: Growth, Money & AI (proposal, 15 notes)

Story: 2028, Larder Plus (a subscription) and the return of Femke's recipe idea, parked in Vol. 1.

- **Getting and keeping customers**: Onboarding & Activation · Habit Loops · Churn Interviews · Win-Back
- **The money side**: Unit Economics (CAC, LTV, payback) · Pricing & Packaging · Subscriptions · Positioning
- **Going to market**: Competitor Analysis · Working with Marketing · Launch Tiers
- **AI as a product feature**: When a Model Earns Its Place · Judging AI Quality · Dark Patterns & Ethics · A Research Repository

Both volumes need the usual per-volume work: casebook section, case file timeline entries, meanwhile links, shelf cover
(automatic), README and handoff updates. They are independent of Book 3's vols. 3–6.

### 4.4 Series 1 (pattern volumes)

Layer A covers them (related links). The extra notes already in the future log stay as planned (Strangler Fig,
Backpressure, Consistent Hashing; Upserts, Bitemporal Data, Vector Indexes; Fuzzing, Visual Regression, Chaos
Experiments). No section changes are proposed: these notes are short on purpose and the deep dives carry the depth.

## 5. Order of work

| Step | What | Deploys as |
| --- | --- | --- |
| 1 | Layer A, all four items | one PR; every volume improves at once |
| 2 | **Sample**: B1–B4 on `architect-2` (Decisions & Trade-offs), with the `rev` mark; owner reviews | one PR |
| 3 | B1–B4 on the other five volumes of Book 1, then the architecture file and the book map | one PR per two volumes |
| 4 | The same for Book 2, starting with `product-4` (Measuring & Learning) | one PR per two volumes |
| 5 | B5, the depth pass on vols. 5–6 | one PR |
| 6 | The Series 2 timeline page | one PR |
| 7 | Vol. 7 of each book, if wanted | one PR each |

Verification for every step is the routine in `docs/HANDOFF.md` section 4: figures on contact sheets, 375 px, light and
dark, every listed page exists. Rule kept: existing URLs, slugs and story facts do not change; text is added, not replaced.

## 6. Decisions for the owner

1. **Which comes first: this plan or Book 3 vols. 3–6?** Recommended: step 1 now (small, improves 303 notes), then
   Book 3 vol. 3, then steps 2–6 between Book 3 volumes.
2. **Going deeper in Books 1–2:** three per volume (recommended), or fewer?
3. **The dial:** add it under the T-chart on document and ceremony notes only (recommended), on every note, or not at all?
4. **Seventh volumes:** both (recommended, after Book 3 is complete), one, or keep the books at six and put the new
   topics into Book 4 and later books?
5. **Vol. 7 topics:** the lists in 4.2 and 4.3 are first drafts. Anything to add or drop?
