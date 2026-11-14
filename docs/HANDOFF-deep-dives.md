# Plan: Series 3 · Deep Dives

Status **2026-11-14**: format approved and built. Written: **01 Saga** (`/deep-dives/saga/`, 26 min),
**02 Reliable Messaging** (`/deep-dives/reliable-messaging/`, 29 min) and **03 The Resilience Stack**
(`/deep-dives/resilience-stack/`, 30 min). 01 and 02 are live (PR #21); 03 is on the branch, not deployed.
Next: 04 Event Sourcing & CQRS.

**Length rule (owner, 14 Nov): every deep dive is about a 30-minute full read**, which is roughly 5,800–6,200
words. The build prints the reading time in the page's fact bar; check it before committing.

Owner's decisions (13 Nov): annotated-textbook style; keep the Season 1 list for now; each dive keeps its
note's own example (no Larder); one long page with a chapter strip, with easy navigation on phones.

## 1. The idea

A Series 1 note answers “what is this pattern and when do I use it?” in about 2,400 words.
A deep dive answers **“what happens when I actually build and run it?”** in about 6,000 words (a 30-minute read).
It starts where the note stops, never repeats it (chapter 1 is a 60-second recap with a link back),
and follows one concrete example from the note all the way through.

Not every note gets one. A topic qualifies when it has **(a)** real failure modes that need timelines,
**(b)** more than one serious variant, and **(c)** an operations story (testing, monitoring, repair).

## 2. Proposed titles

Several dives merge notes that only make sense together.

**Season 1 (recommended six)**

| # | Deep dive | Builds on | Why it is big enough |
| --- | --- | --- | --- |
| 01 | **Saga** | distributed 05 | crash recovery, timeouts, isolation anomalies, orchestration vs choreography, repair |
| 02 | **Reliable Messaging** (“exactly-once is a lie”) | distributed 06, 07, 11, 12 · data CDC | outbox relay vs CDC, ordering, duplicates, poison messages, dead-letter queues, replay |
| 03 | **The Resilience Stack** | distributed 01–04 | how timeout, retry, breaker, bulkhead and rate limit interact; retry budgets; tuning with numbers; load shedding |
| 04 | **Event Sourcing & CQRS** | distributed 08, 09 | event versioning, snapshots, projections and rebuilds, read-your-writes, GDPR erasure |
| 05 | **Caching** | distributed 17 · frontend server-state cache | invalidation strategies, stampedes, TTL maths, write-through/behind, cache layers, consistency bugs |
| 06 | **Zero-Downtime Change** | data expand–contract · cloud blue-green, canary, feature flags | one schema change followed through every deploy step; backfills; rollback at each stage |

**Season 2 (candidates)**

| Deep dive | Builds on |
| --- | --- |
| Replication, Failover & Leader Election | distributed 16, 18 (lag, split brain, fencing tokens, quorum) |
| Sharding & Partitioning | distributed 15 · data partitioning (key choice, hot shards, resharding, consistent hashing) |
| Indexes & Query Plans | data indexing, N+1, keyset pagination (reading EXPLAIN, composite order, write cost) |
| Sign-in, Tokens & Sessions | security OAuth+PKCE, short-lived tokens (every redirect, refresh rotation, revocation, attacks) |
| Observability & SLOs | cloud observability, SLOs, postmortems (from one alert to root cause) |
| Rendering on the Web | frontend SSR/hydration, islands, code splitting (one page measured four ways) |
| Multitenancy | data multitenancy · security least privilege (isolation models, noisy neighbours, per-tenant migration) |

## 3. Chapter template (flexible: 8–10 chapters, pick what the topic needs)

1. **The note in sixty seconds**: recap table + link back; what this dive adds.
2. **The real mechanism**: the part the note simplified (state, storage, protocol), with the actual tables/messages.
3. **Failure drills** *(signature section)*: 4–6 cards, each `Timeline → Tempting mistake → Why → What saves you → Rule`.
4. **The hard problem**: the one deep concept of the topic (saga: isolation; caching: invalidation; resilience: interaction).
5. **Variants side by side**: the same example built each way, same drills run against each, then a decision table.
6. **Numbers**: timeouts, sizes, limits; a worked calculation.
7. **Testing it**: what to unit test, what to fault-inject, contract tests.
8. **Running it**: three metrics, one dashboard, a repair runbook.
9. **Tools**: what off-the-shelf products give you, mapped to the chapters; what they leave to you.
10. **Lab + review checklist**: a design exercise with a model answer; a one-page card (reuses the cheat sheet layout).

## 4. What keeps a long page easy to read

- **Gist box** opening every chapter (2–3 sentences). Reading only the gists and the drill rules is the 6-minute version.
- **Skim / full toggle**: skim hides everything except gists, tables, drill outcomes and rules.
- **One example for the whole dive**, taken from the note (saga: order 42, two mugs, $49).
- **Checkpoint** after each chapter: 2 questions with hidden answers.
- A figure or table at least every ~300 words; sentences short; one idea per sub-heading.
- Sticky chapter strip; each chapter is linkable; reading time shown per chapter.
- Each chapter also exports as its own PDF, plus the whole dive.

## 5. Style: “the annotated textbook”

The notes are a student's handwritten journal. The deep dive is **the printed textbook the same student annotated**:

- Body in a reading serif (Literata, 18px, ~66 characters). Handwriting is tiring at 8,000 words, so it is
  kept for what a pencil would do: margin notes, figure labels, captions, drill rules, chapter tags.
- Display headings keep Amatic SC, mustard highlighter, sage and dusty pink from Vol. 1, so the shelf still reads as one family.
- Margin notes sit in a right-hand margin on desktop and inline (dotted rule) on phones.
- Doodles reuse `scripts/doodle.py`.
- Alternatives considered: (b) keep the full handwritten skin, split into many short pages: cheapest, but
  long reading in Patrick Hand is hard; (c) lab-manual skin (numbered experiments): fits the drills, loses the family look.

## 6. How it is built

- Content: `content/deep-dives/<slug>.py` defines `DIVE` (title, `no`, `notes`, `chapters`). Each chapter has
  `id`, `nav` (short name for the strip and dock), `title`, `gist`, `body` (HTML) and optional `check` questions.
- Helpers injected into content files (from `scripts/dive.py`): `tbl()`, `drill()`, `mn()` margin note, `full()`
  (hidden in skim mode), `code()`, `fig()` (raw SVG using the `bx`/`ln`/`lbl` classes), `checklist()`.
- `scripts/dive.py` renders the page; `scripts/build_notes.py` has `DIVES`, the landing shelf (`#deep-dives`),
  the `journals.json` entry (so the workflow builds the PDF) and the “go deeper →” link on notes listed in `notes`
  (the hand-made `saga.html` and `circuit-breaker.html` have that link typed in).
- Styles `public/assets/dive.css`, script `public/assets/dive.js`. The page does not load `notebook.css`/`bujo.css`.
- Reading times are computed from word counts (200 words a minute), per chapter and for skim mode.
- `dive.render_preview(d, css, js)` returns one self-contained file for sharing a draft.

**Navigation.** Wide screens: sticky chapter strip with the current chapter highlighted, progress line, skim button.
Phones (≤ 760 px): a bottom dock with previous / next arrows and a middle button showing “3 / 10 · Failure drills”;
tapping it opens a chapter sheet (titles, minutes, skim toggle, top of page). Every chapter ends with a
“next chapter” link, chapter 3 has jump chips for the five drills, and the contents list works without JavaScript.

**Skim mode** shows gists, figures, tables, drill timelines, fixes and rules, and checklists; it hides prose,
margin notes and code. The choice is remembered in the browser.

## 7. Next

1. Owner reviews Saga on a phone and on desktop; adjust the format before writing more.
2. Then one dive per PR, in the Season 1 order (04 Event Sourcing & CQRS next). For each: write the content file,
   add its name to `DIVES`, build, and run the verify routine in `docs/HANDOFF.md` §4 (figures, 375 px, dark, PDF).
3. Ideas not built: per-chapter PDFs, a printable one-page checklist card, Doodle-style wobbly figures.
