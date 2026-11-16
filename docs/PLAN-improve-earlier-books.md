# Plan: improve the earlier books

Plan of 2026-11-15, **approved by the owner** (decisions in section 7). Progress is in section 8.

It covers everything that is finished: Series 1, the six design-pattern volumes (93 notes), and the two practitioner
books, Book 1 (Ana, 90 notes) and Book 2 (Grace, 90 notes).

The plan has three layers, cheapest first: **A** fixes made once in the generator, **B** section updates to existing
notes, **C** new pages, new notes and new volumes.

## 1. What the audit found

Measured on `main` with a script over every content file (`content/<key>/*.py`).

### All 303 notes

| Finding | Numbers | Why it matters |
| --- | --- | --- |
| “Related notes” are plain text | 1,219 references, **0 are links** | The reader sees “Quality attribute scenarios (vol. 1)” and cannot click it. |
| The `rev` field is never used | 0 notes | Updated notes have no visible “revised” mark. |

### Series 1: design patterns

| Finding | Numbers | Why it matters |
| --- | --- | --- |
| No “try it” | 0 of 93 notes; every Series 2 note has one | The reader reads about a pattern and never uses it. |
| Recall-only quizzes | 4 questions per note | “Which pattern fits here?” is the skill; no question tests it. |
| Depth is all or nothing | 16 notes have a full ten-chapter deep dive, 77 have nothing beyond the note | Many patterns need one more step, not thirty minutes. |
| Shortest notes on the shelf | about 280–320 words of prose per note (Cloud 281, Testing 288); Series 2 has 350–450 | Vols. 4 and 6 are the first candidates for added depth. |
| No link to the Larder story | 0 links from a pattern to the note where Ana uses it | ADR 0007 is the outbox pattern in real use; the outbox note doesn't say so. |
| No link to the cheat sheets | 0 links | Indexing and the SQL card, Health Checks and the Kubernetes card don't know about each other. |
| Two hand-made notes | Circuit Breaker and Saga are HTML files, not data | Every generator change in this plan would skip them. |
| Extra notes announced, not written | 14 titles in the future log, plus Vol. 7 | The shelf promises them. |

### Series 2: Books 1 and 2

| Finding | Numbers | Why it matters |
| --- | --- | --- |
| No cheat sheet links | 0 links from 180 notes | The NFR Checklist note and the NFR cheat sheet don't know about each other. |
| Recall-only quizzes | 4 questions per note; Book 3 has 5, two of them situational | Situational questions test judgment, which is what these books teach. |
| No “going deeper” chapters | 0 of 180 notes; Book 3 has 4 per volume | Key notes (ADR, C4, A/B tests) stop at the same depth as minor ones. |
| “Meanwhile” links thin out | Book 2: 15 in vol. 1, then 4, 3, 1, 3, 4 | The two books share scenes in every volume; later volumes rarely show it. |
| Template cards are scattered | 180 cards, no collected page; Book 3 has `/rotterdam/` | Ana's 29 ADRs and Grace's one-pagers would work as a sample document set. |
| No one-page map of a book | Book 3 has `/pmbok/` | No way to see “the whole job” and jump to a note. |
| Later volumes are shorter | Book 1: 452 words of prose in vol. 2 → 363 in vol. 6; Book 2: 439 → 350 | Vols. 5–6 are the first candidates for added depth. |

Not measured, to check while editing: whether each collection of Books 1–2 has a narrator's mistake (a Book 3 rule),
the wording of facts that Book 3 later made more exact (Rotterdam budget, milestones), and whether the tools and
sources named in Series 1 notes are still current.

## 2. Layer A: fix once, every note gains

Generator work in `scripts/build_notes.py`. No note is rewritten.

1. **Link the related notes.** Resolve each `related` entry to a note by title (across all journals), render it as a
   link, and print the ones that don't resolve so they can be fixed by hand. Entries may stay as text if no note exists.
2. **Convert the two hand-made notes** (Circuit Breaker, Saga) to data files like the other 91, same URLs, so they get
   every change below. Compare the pages before and after.
3. **Link to deep dives and cheat sheets.** Extend the `DEEPER` map so Ana's notes point at the matching deep dive
   (Event-Driven Integration → Reliable Messaging, Migration Planning → Zero-Downtime Change, Failure Mode Analysis →
   The Resilience Stack), and add an “on a card →” line for cheat sheets in both series (NFR Checklist → NFR
   Checklists; Indexing, Keyset Pagination → SQL; Health Checks, Autoscaling → Docker & Kubernetes).
4. **“Seen at Larder” links.** A new line on a pattern note that points to the Series 2 note where the pattern is
   used in the story (Transactional Outbox → Ana's ADR note; Strangler Fig, Feature Flags, Canary, SLOs, Multitenancy
   and others). A small table in the generator, rendered on both sides, like `meanwhile`.
5. **A “revised” mark.** Use the existing `rev` field: a small stamp in the title block and a line on the volume index
   (“revised Dec 2026: quiz, going deeper”), so returning readers see what changed.
6. **Fill in the “meanwhile” links** for Books 1–2, vols. 3–6, and add Sanne's side where Book 3 shares a scene. Source:
   the casebook sections per volume. Target: 4–6 per volume.

## 3. Layer B: section updates to Series 1 (93 notes)

The patterns keep their short, quick-reference shape and their gains vs losses chart. No dial: it suits documents and
ceremonies, not patterns.

| # | Update | Scope | Size |
| --- | --- | --- | --- |
| S1 | **Situational quiz question**: one “which pattern, and why not the other?” or “what breaks first?” question per note | all 93 notes | 93 questions |
| S2 | **Try it**: a 15–30 minute hands-on exercise at the end of each note (break it, then fix it with the pattern) | all 93 notes | 93 exercises |
| S3 | **Going deeper chapter**: an intro and three or four numbered parts with their own figures | 3 or 4 per volume, 18–24 chapters | the largest item |
| S4 | **Depth pass on Testing and Cloud**: a second example or figure where a note is thin | about 15 notes | after S1–S3 |
| S5 | **Freshness pass**: check the `tools` and `sources` lists of every note; replace what is out of date | all 93 notes | small per note |

**Going deeper candidates (S3).** A note that already has a full ten-chapter deep dive does not get an in-note chapter;
its “go deeper →” link is enough. Notes marked ² are Season 2 deep-dive candidates: the in-note chapter comes first and
the full dive, if written later, takes over from it.

| Vol. | Candidates |
| --- | --- |
| 1 Distributed | API Gateway · Service Discovery · Sidecar & Service Mesh · Sharding ² |
| 2 Frontend | State Machines · SSR & Hydration ² · Micro-Frontends · Optimistic UI |
| 3 Data | Indexing ² · Optimistic Locking · Change Data Capture · Multitenancy ² |
| 4 Testing | Test Doubles · Contract Testing · Property-Based Testing · Flaky Test Quarantine |
| 5 Security | OAuth 2.0 with PKCE ² · Threat Modelling · Envelope Encryption · Supply-Chain Hygiene |
| 6 Cloud | Infrastructure as Code · SLOs & Error Budgets ² · Autoscaling · Incident Response & Postmortems |

## 4. Layer B: section updates to Books 1 and 2 (180 notes)

Each item carries Book 3's better ideas back.

| # | Update | Scope | Size |
| --- | --- | --- | --- |
| B1 | **Situational quiz question**: one “what does Ana / Grace do?” question per note, added to the four recall ones | all 180 notes | 180 questions |
| B2 | **Going deeper chapter** on the key notes | 3 or 4 per volume, 36–48 chapters | the largest item |
| B3 | **Light / standard / heavy dial**, added under the T-chart (not replacing it) on notes that are documents or ceremonies | about 20 notes per book | 40 dials |
| B4 | **Narrator's mistake**: one note per collection where the technique was skipped or overdone and what it cost | where missing | to be counted |
| B5 | **Depth pass on vols. 5–6** of both books: a second worked example or figure where a note is thin | about 20 notes | after B1–B2 |

**Going deeper candidates (B2).** The first three per volume are the firm picks; the fourth is written if the note has
enough for a chapter.

| Vol. | Book 1 (Ana) | Book 2 (Grace) |
| --- | --- | --- |
| 1 | Quality Attribute Scenarios · Bounded Contexts · Risk-Storming · *Event Storming* | Customer Interviews · Opportunity Solution Tree · North Star Metric · *Jobs to Be Done* |
| 2 | Architecture Decision Records · Options Analysis · Build vs Buy · *One-way vs Two-way Doors* | RICE & ICE Scoring · Cost of Delay · Business Case One-Pager · *Now / Next / Later Roadmap* |
| 3 | C4 Model · Solution Design Document · Presenting to Executives · *arc42 Template* | Story Mapping · User Stories that Work · Launch Checklist · *Example Mapping* |
| 4 | Choosing an Integration Style · Strangler Fig Migration · Data Ownership · *API Versioning Strategy* | A/B Tests · Cohorts & Retention Curves · OKRs · *Sample Size & Test Duration* |
| 5 | Availability Maths · Capacity Planning · Total Cost of Ownership · *Failure Mode Analysis* | The One-Page PRD · Negotiating Scope · Delivering Bad News · *When the Date Is Fixed* |
| 6 | Architecture Principles · Guardrails Not Gates · Go-Live Readiness · *Migration Planning* | Pricing Experiments · B2B vs B2C Products · Platform Thinking · *Product Sense* |

**Dial candidates (B3).** ADR, RFCs, arc42, Solution Design Document, Technology Radar, Architecture Review, Risk
Register, Go-Live Readiness; PRD, Roadmaps, OKRs, Quarterly Product Review, Definition of Ready & Done, Launch Checklist.

## 5. Layer C: new pages, new notes, new volumes

### 5.1 Series 1: extra notes and Vol. 7

The future log already names these. The plan is to write them as one batch per volume, each with the updated shape
(situational question, try it), and to add each to its volume's index and PDF.

| Vol. | Extra notes |
| --- | --- |
| 1 Distributed | Strangler Fig · Backpressure · Consistent Hashing |
| 2 Frontend | Debounce & Throttle · Web Workers · Offline-First Sync |
| 3 Data | Upserts · Bitemporal Data · Vector Indexes |
| 4 Testing | Fuzzing · Visual Regression · Chaos Experiments |
| 5 Security | Passkeys · Signed Webhooks · Rate-Limited Login |
| 6 Cloud | Chaos Engineering · Service Catalogues · Progressive Delivery |

**Vol. 7 · AI App Patterns** (already on the shelf as planned): retrieval-augmented generation, agents and tools,
evaluation, guardrails, cost-aware LLM apps. It is written in the updated shape from the start. Its collection list
is a separate proposal when its turn comes.

Also from the future log, unchanged: a one-page printable cheat sheet per collection, and deep dives season 2.

### 5.2 Series 2: new pages (generated, like Book 3's)

1. **The Larder architecture file** (`/larder-architecture/`): every template card of Book 1 in order, with the ADR log
   0001–0029 as its spine. `render_project_file()` already does this for Book 3; it needs a second file prefix and a title.
2. **The Larder product file** (`/larder-product/`): Grace's cards: strategy on a page, the roadmap, PRDs, test plans, reviews.
3. **A map per book**: “the architect's job on one page” and “the product owner's job on one page”: the questions of
   the job, grouped by phase, each linked to its note. Same layout as `/pmbok/`, no external standard needed.
4. **The Series 2 timeline** (already in the future log): every Larder note of all three books on one timeline, filtered
   by narrator. The case file `TIMELINE` has the data.

### 5.3 Book 1, Vol. 7: Teams, Data & AI (15 notes, after Book 3 is complete)

Topics the six volumes don't cover. Story: October 2028 → mid 2029, after the sixth city, Ana as lead architect.

- **Teams and the system**: Conway's Law · Team Topologies · Cognitive Load and Platform Teams · Inner Source
- **Data for decisions**: Operational vs Analytical Data · Data Products and Contracts · Reporting Architecture · Data Quality Ownership
- **AI in the architecture**: Where a Model Fits · Build, Buy or Call a Model · Evaluating an AI Feature · Human in the Loop
- **Running what you designed**: Observability by Design · SLOs as Requirements · From Incident to Architecture Change

### 5.4 Book 2, Vol. 7: Growth, Money & AI (15 notes, after Book 3 is complete)

Story: 2028, Larder Plus (a subscription) and the return of Femke's recipe idea, parked in Vol. 1.

- **Getting and keeping customers**: Onboarding & Activation · Habit Loops · Churn Interviews · Win-Back
- **The money side**: Unit Economics (CAC, LTV, payback) · Pricing & Packaging · Subscriptions · Positioning
- **Going to market**: Competitor Analysis · Working with Marketing · Launch Tiers
- **AI as a product feature**: When a Model Earns Its Place · Judging AI Quality · Dark Patterns & Ethics · A Research Repository

Both volumes need the usual per-volume work: casebook section, case file timeline entries, meanwhile links, shelf cover
(automatic), README and handoff updates. The AI notes of the three Vol. 7s link each other instead of repeating:
Series 1 has the patterns, Ana where a model fits in the system, Grace whether it earns its place.

## 6. Order of work

| Step | What | Deploys as |
| --- | --- | --- |
| 1 | Layer A, all six items | one PR; every volume improves at once |
| 2 | Book 3, Vol. 3 (its own plan: `docs/HANDOFF-project-manager.md` section 13) | one PR |
| 3 | **Sample, Series 2**: B1–B4 on `architect-2` (Decisions & Trade-offs), with the `rev` mark; owner reviews | one PR |
| 4 | **Sample, Series 1**: S1–S3 and S5 on `data` (Data & Database Patterns), plus its three extra notes; owner reviews | one PR |
| 5 | B1–B4 on the other five volumes of Book 1, then the architecture file and the book map | one PR per two volumes |
| 6 | The same for Book 2, starting with `product-4` (Measuring & Learning) | one PR per two volumes |
| 7 | S1–S3, S5 and the extra notes on the other five pattern volumes | one PR per volume |
| 8 | The depth passes (S4, B5) and the Series 2 timeline page | one PR each |
| 9 | Series 1 Vol. 7, then Vol. 7 of Books 1 and 2, after Book 3 is complete | one PR each |

Steps 3–8 fit between Book 3's volumes; the order between them can change.

Verification for every step is the routine in `docs/HANDOFF.md` section 4: figures on contact sheets, 375 px, light and
dark, every listed page exists. Rules kept: existing URLs, slugs and story facts do not change; text is added, not
replaced; Series 1 notes stay short, with the depth in the new chapter, not in the first eight sections.

## 7. Decisions (owner, 2026-11-15)

| # | Question | Decision |
| --- | --- | --- |
| 1 | Which comes first, this plan or Book 3 vols. 3–6? | Layer A now, then Book 3 vol. 3, then the section updates between Book 3 volumes. |
| 2 | Going deeper chapters per volume | **3 or 4 per volume**, in all three shelves. |
| 3 | The dial in Books 1–2 | Under the T-chart, on document and ceremony notes only. |
| 4 | Seventh volumes | Both books get one, after Book 3 is complete. |
| 5 | Design patterns | **Included** (sections 3 and 5.1). |
| 6 | Vol. 7 topics for Books 1 and 2 | The lists in sections 5.3 and 5.4, as drafted. |
| 7 | Series 1 extra notes, the open slots | Frontend: Web Workers and Offline-First Sync. Security: Rate-Limited Login. Cloud: Progressive Delivery (automated checks and rollback, building on Canary). |
| 8 | Going deeper picks | The candidate tables in sections 3 and 4, as drafted; the fourth pick per volume is written if the note has enough for a chapter. |

The owner approved the plan on 2026-11-15 (“do your recommendation”). The work starts later, at step 1 of section 6.

## 8. Progress

### 2026-11-16: Series 1 (design patterns), first pass

| Item | State |
| --- | --- |
| A1 related notes are links | **done** for all 303 notes (about 1,200 of 1,219 entries; 19 name topics with no note yet and stay text; the build prints them) |
| A2 hand-made notes | **done differently**: Circuit Breaker and Saga stay hand-made; the build injects the new blocks between `<!-- gen:… -->` markers (idempotent) |
| A3 deep-dive and cheat-sheet links | **done**: `CARD_LINKS` in `build_notes.py` (“on a card →”) |
| A4 seen at Larder | **done**, automatic: every Series 2 related entry that names a pattern shows on that pattern (38 links on 26 notes) |
| A5 revised mark | **done**: `revised=(month, what)` on a note, `REVISION_NOTE` on the volume index |
| A6 meanwhile links (Books 1–2) | not started |
| S1 situational question | **done**, 93 of 93 (tagged “what would you do?”) |
| S2 try it | **done**, 93 of 93 |
| S3 going deeper | **sample done on `data`**: Indexing, Optimistic Locking, Change Data Capture, Multitenancy (4 chapters, 9 figures). Owner reviews before the other five volumes |
| S4 depth pass, S5 freshness pass | not started |
| 5.1 extra notes, Vol. 7 | not started |

How it is built: additions live in `content/<key>/revisions.py` (quiz_add, try_it, revised) and `content/<key>/deeper.py`
(deep_dive), merged into the notes by `load_content`; the original note files are unchanged. Several files may add to one note.

Also fixed on the way: leftover merge markers in `bujo.css` that hid the deep-dive cover colours and Book 3's binder colours
on the live site; deep-dive covers restyled as a printed textbook; long words in quiz answers no longer widen phone pages.

Next for Series 1: owner reviews the `data` sample, then going deeper for the other five volumes (candidates in section 3),
then the extra notes (5.1). Cover artwork: three options mocked up (sticker, printed cloth, both); waiting for the owner.
