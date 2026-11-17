# Handoff: The Project Manager's Notebook (Series 2, Book 3)

Status as of 2026-11-17: **Vols. 1–4 are written and deployed (PR #24 and PR #29). Vol. 5 is written (section 17), on
branch `ccr-98bbf05d-6dvq28`, not yet merged. Vol. 6 is planned in detail in section 16.4: start there.** Decisions in section 9;
what was built in section 10.

Story facts: `docs/larder-casebook.md` (source of truth) and the public case file `/larder/`.
Earlier plans, for comparison: `docs/HANDOFF-solution-architect.md`, `docs/HANDOFF-product-owner.md`.

## 1. What the book is, and what changes

Book 3 of Series 2. Narrator: **Sanne**, delivery manager at Larder, who joins in January 2026 and inherits the
Rotterdam launch (date fixed by the store lease: 27 April 2026). Ana's notebook asks *“how do we build it?”*,
Grace's asks *“should we, and for whom?”*, Sanne's asks ***“by when, for how much, and what could stop us?”***

**Goal:** the complete PMBOK Guide, easy to digest. That is a different job from Books 1 and 2:

| | Books 1–2 | Book 3 |
| --- | --- | --- |
| Topics chosen by | what the narrator found useful | **the standard**: every principle, domain and process is covered |
| A note is | one technique | **one question a project manager must answer**, which covers 1–3 PMBOK processes and their main tools |
| The reader checks progress on | the volume index | a **PMBOK map** page: every item of the guide → the note that covers it |
| Example data | new numbers per note | **one project file that grows**: the same Rotterdam numbers run from charter to closing report |

**Deep dives** (owner's addition, 2026-11-14): key items get a chapter-like deep dive inside their note, after
“How it solves it”: an intro and three or four numbered parts with their own figures. The note stays short for a first
read; the deep dive is for when you need more (worked examples, how to choose, what goes wrong). Three to five per volume.

Kept from Books 1–2: the eight-section note, the Larder scene, the analogy with doodles, the template card,
“try it”, the quiz, the “meanwhile” boxes, the case file timeline, nine ratings, one PDF per volume.

Rule (as before): don't repeat notes from other books. Link instead. Sanne's stakeholder notes link Ana's stakeholder
map; her charter links Grace's business case one-pager; her risk register links Ana's risk-storming and Grace's
pre-mortem; her scope notes link Grace's MoSCoW and story mapping.

## 2. The spine: PMBOK Guide, Eighth Edition

The eighth edition (PMI, November 2025) is the current one: **6 principles, 7 performance domains, 5 focus areas,
40 processes**, plus tailoring and the models, methods and artifacts.

- Principles: adopt a holistic view · focus on value · embed quality · be an accountable leader · integrate
  sustainability · build an empowered culture.
- Performance domains (processes): Governance (9) · Scope (6) · Schedule (3) · Finance (4) · Stakeholders (7) ·
  Resources (5) · Risk (6).
- Focus areas: initiating · planning · executing · monitoring and controlling · closing.

**Check before writing:** the names above come from PMI's public pages and secondary guides. The exact wording of the
six principles and the names of the 13 Stakeholders and Risk processes must be checked against the guide itself.
The owner needs a copy (PMI members get the PDF).

Many readers learned an older edition, so every note carries a one-line **“in older editions”** tag (6th: 10 knowledge
areas, 49 processes; 7th: 12 principles, 8 domains), and the PMBOK map has an edition crosswalk.

**Copyright:** PMBOK is PMI's. Every explanation, table and figure is written in our own words and drawn from scratch:
no copied definitions, no ITTO tables, no PMI figures. Process and domain names are used as names only. Each book page
carries a footer: independent study notes, not affiliated with or endorsed by PMI.

## 3. Writing style

1. **Plain words first, PMBOK words second.** The title is the question; the official term is the kicker.
   “How long will it take?” · *a.k.a. Develop Schedule*. A reader who never opens the guide can still follow.
2. **A PMBOK tag on every note** (in the title block): domain · focus area · process(es) · principle. This is what
   makes “complete” visible, and it is how the map page is generated.
3. **“Need → do → get” instead of ITTO tables.** One doodle strip per note: what Sanne has in hand, what she does
   with it, what comes out. Three or four items each, the ones that matter, in our own words.
4. **One project file that grows.** The template card in each note is a real page of the Rotterdam file, and the
   numbers carry over: the charter's budget is the baseline in the budget note and the BAC in the earned value note.
   A new **project file page** (like the case file) collects every card: a full sample set of project documents.
5. **Worked numbers for every formula.** Critical path, three-point estimates, earned value, expected monetary value:
   Sanne does the sum by hand with Rotterdam's numbers, step by step, then the formula is named.
6. **“Light, standard, heavy”: the tailoring dial.** Each note shows how the same process looks on a small adaptive
   piece of work, on Rotterdam (hybrid), and on a heavy predictive one. This teaches tailoring in every note and
   stops the book from reading as “fill in all 40 forms”.
7. **Sanne makes mistakes.** The casebook already has one (she told Joost approvals would be in Rotterdam at launch).
   Each collection has a note where the process was skipped or overdone and what it cost.
8. **Situational quiz questions.** “The lease date can't move and the internet line is six weeks late. What does
   Sanne do first?” This is how the PMP exam asks, and it tests judgment, not recall.
9. **Same voice as before:** first person, short sentences, everyday English, a term is explained the first time it
   appears, dates and numbers in every scene.

## 4. Note format

Same data shape as Books 1–2, with these options:

| Section | Books 1–2 | Book 3 |
| --- | --- | --- |
| 1 The situation | a Larder scene | same, with the question Sanne has to answer |
| 2 Analogy | doodle + mapping table | same |
| 3 How it works | doodle + steps | the **need → do → get** strip + steps |
| 4 Template card | `code` with `plain=True` | **a page of the project file** (same field, plus `file_page` for its order in the file) |
| 5 Gains vs losses | T-chart | **light / standard / heavy** (new `dial` field); the T-chart stays for technique notes |
| 6 Ratings | nine ratings | nine project ratings (below) |
| 7 Pitfalls | list | same, with Sanne's own mistake where there is one |
| 8 When to use, quiz | recall questions | **situational** questions |

New note fields: `pmbok=dict(covers=, domains=[…], focus=[…], principles=[…], older="…")`, `dial`, `deep_dive`
(and `file_page` from Vol. 2). New generated pages: the **PMBOK map** (`/pmbok/`) and, from Vol. 2, the **project file**.

**Ratings: `PROJECT_ATTRS`** (proposal):

| Rating | Question | Meaning |
| --- | --- | --- |
| Value focus | serves the outcome? | Keeps the project aimed at the benefit, not the paperwork. |
| Predictability | dates and costs hold? | Forecasts get closer to what happens. |
| Risk reduction | fewer surprises? | Finds trouble while it is cheap. |
| Transparency | true status visible? | Anyone can see where the project really is. |
| Stakeholder confidence | they trust the plan? | Sponsors and partners believe the updates. |
| Team ownership | team decides and commits? | The people doing the work own the plan. |
| Adaptability | easy to change course? | Change is absorbed without chaos. |
| Quality built in | right first time? | Problems are prevented, not inspected out. |
| Low overhead | light to run? | Time and ceremony it takes. High = light. |

## 5. Volumes

Volumes follow the **domains** (so the book matches the guide and works as a reference); each volume uses the Larder
project that shows its domain best. Six volumes, 13–15 notes each, about 85 notes.

| Vol. | Title | PMBOK | Story | Collections → notes (first draft) |
| --- | --- | --- | --- | --- |
| 1 | The Lay of the Land | principles, life cycles, focus areas, tailoring | Jan 2026: Sanne's first weeks; Rotterdam has a date and no plan | **What a project is**: Project, Product or Operations?, The Value Delivery System, What a Project Manager Does, The PMO · **Six principles** (one note each) · **Ways of working**: Predictive, Adaptive, Hybrid, The Five Focus Areas, Tailoring, The Project Environment |
| 2 | Starting, Steering, Closing | Governance (9) | Rotterdam, Jan → Jun 2026 | **Starting**: The Project Charter ★, The Sponsor, Phase Gates and Go / No-Go · **One plan**: The Project Management Plan, Baselines, The Sourcing Strategy (make, buy, contract types) · **Running it**: Directing the Work, Quality Assurance vs Control, Lessons Learned that Get Used, Issue Log · **Steering**: Status Reports that Tell the Truth, Change Control, Escalation · **Closing**: Closing a Project or Phase, The Handover |
| 3 | What, and By When | Scope (6), Schedule (3) | Rotterdam: the store fit-out (predictive) and the app (adaptive) | **Scope**: Requirements, The Scope Statement, Work Breakdown Structure ★, Acceptance and Sign-off, Scope Creep · **Estimating**: Analogous, Parametric and Bottom-up, Three-Point Estimates, Estimating with the Team · **Schedule**: Dependencies and the Network Diagram, Critical Path ★, Float, Gantt Charts and Milestones, Crashing and Fast-Tracking, Release and Iteration Plans, Burn Charts |
| 4 | Money and People | Finance (4), Resources (5) | 2027: Utrecht (April) and The Hague (June), two projects, one team | **Money**: Cost Estimates, The Budget and Its Reserves, Earned Value ★ (two notes: where are we, where will we end), Funding and Cash Flow, Payback and NPV · **People and things**: RACI, Getting the Team, Resource Levelling, Team Stages, Leading without Authority, Conflict, Motivation, Physical Resources (vans, fridges, lead times) |
| 5 | People Outside, and Surprises | Stakeholders (7), Risk (6) | Antwerp, 2027: a new country, Belgian rules, new partners | **Stakeholders**: The Stakeholder Register, Power and Interest (links Ana), The Engagement Matrix, The Communications Plan, Managing Expectations, Running Meetings · **Risk**: The Risk Register ★, Probability and Impact, Expected Monetary Value, Simulation in Plain Words, Risk Responses (threats and opportunities), Contingency vs Management Reserve, Risks vs Issues, Risk Reviews |
| 6 | Making It Yours | tailoring, models, methods, artifacts; the newer topics | End 2027: Eindhoven, the sixth city, run from the playbook | **Tailoring**: Tailoring a Whole Project, The City Launch Playbook, Projects, Programmes and Portfolios · **Newer topics**: AI in Project Work, Sustainability, Benefits Realisation · **Growing**: Servant Leadership, Ethics, Growing as a Project Manager, Handing Over |

Process coverage is exact only once the map is filled in against the guide (section 2). Where two “Plan … Management”
processes say the same thing, they share one note, and the map shows both.

## 6. Cheat sheets (the shelf already exists)

Formula-heavy and map-like content suits the laminated cards better than a note:

1. **PMBOK 8 on one page**: 6 principles, 7 domains, 5 focus areas, the 40 processes as a grid.
2. **Edition crosswalk**: 6th → 7th → 8th.
3. **Earned value**: every formula, with one worked example.
4. **Critical path**: forward pass, backward pass, float.

## 7. Skin proposal: the project binder

- Desk: slate grey; sheets are punched binder pages with ring holes down the left edge.
- **Seven divider tabs, one colour per domain**, used on every note, the index, the map and the project file.
- A five-step strip in the title block for the focus area (initiating → closing), the current step filled in.
- Marks: a red / amber / green status stamp, Gantt bars as section rules, a wall-calendar motif on the index.
- Font for titles: a neat block hand (e.g. Patrick Hand SC); body fonts unchanged.
- Cover on the shelf: navy with an amber band.

## 8. Build checklist

1. [ ] Owner answers section 9; owner has the eighth edition to check names against.
2. [ ] `PROJECT_ATTRS`, the `project-1` journal entry, `.theme-project` skin and cover.
3. [ ] `pmbok`, `dial`, `file_page` fields; the tag in the title block; the PMBOK map and project file pages.
4. [ ] Sample note; owner reviews look and voice.
5. [ ] Vol. 1; then one volume at a time, each with casebook facts, case file `TIMELINE` entries (tag `"3"`),
       meanwhile links to Ana's and Grace's notes, and the map updated.
6. [ ] Cheat sheets alongside the volume they belong to.
7. [ ] Verify as before (contact sheets, 375 px, light / dark, PDFs), PR, deploy when asked.

## 9. Decisions (owner, 2026-11-14: “do your recommendation”, plus deep dives)

All eight recommendations below are accepted: eighth edition, volumes by domain, practitioner's notebook with situational
quizzes, the light / standard / heavy dial, the binder skin, the nine ratings, six volumes. The owner added **deep-dive
chapters for key items** (section 1). Critical Path stays the recommended sample for the formula-heavy style; it is in Vol. 3.

The questions as they were asked:

1. **Edition:** eighth as the spine, with “in older editions” tags (recommended), or seventh / sixth?
2. **Volume order:** by domain (recommended, section 5), or by life cycle (initiating → closing)?
3. **Purpose:** practitioner's notebook with situational quizzes (recommended), or a PMP exam-prep book (adds exam
   tips, mock questions and formula drills to every note)?
4. **Section 5 of the note:** replace gains vs losses with the light / standard / heavy dial (recommended)?
5. **Skin:** the project binder (section 7)?
6. **Ratings:** the nine in section 4?
7. **Sample note:** Critical Path (recommended: it has a doodle, a sum and a template, so it tests every new element),
   or The Project Charter?
8. **Size:** six volumes of 13–15 notes (about 85), or fewer, larger notes?

## 10. Vol. 1 notes on the build (2026-11-14)

- `project-1` journal, “The Lay of the Land”; content in `content/project-1/01_what.py` (4 notes), `02_principles.py` (6),
  `03_ways.py` (5). Story: 12 January → 25 February 2026. Facts: casebook, “Book 3, Vol. 1”.
- The plan's list changed a little: **What Must I Keep an Eye On?** (the seven domains) was added; the value delivery system
  and the PMO kept; “What a Project Manager Does” became **What Is My Job Here?**. Titles are the questions; the official
  term is the kicker and the `covers` line of the PMBOK tag.
- **Deep dives** (4): What Is It All For? (benefits map, benefit owners, when to stop) · Plan It All, or Learn As We Go?
  (five questions, what holds a hybrid together, the four life cycles) · What Do I Do When? (the domain × focus-area grid)
  · How Much Process Do We Need? (four steps, five dials, what can't be tailored away, reviewing the fit).
  Mark a note in the journal's `deep_dives` set so the index and the map show the “+ deep dive” tag.
- Generator (`scripts/build_notes.py`): `PROJECT_ATTRS`, `PMBOK_DOMAINS`, `PMBOK_FOCUS`, `PMI_NOTE`; `pmbok_tag()`,
  `dial_block()`, `deep_dive_block()`, `render_pmbok_map()`; journal fields `pmbok=True`, `deep_dives`, `first_law`,
  `disclaimer`; `PLANNED_PROJECT`; `PROJECT_DOODLES`. `Doodle.row()` (a row of equal boxes, optional arrows) in `doodle.py`.
- **PMBOK map**: `content/pmbok/map.py` → `/pmbok/`. It lists principles, domains (with process **counts** only), focus areas,
  foundations, every note by volume, and an edition crosswalk. **Process names are not printed yet**: add each domain's
  names when its volume is written and they have been checked against the guide.
- Skin `.theme-project` (the binder): slate desk, ring holes, a margin line, block-capital titles (Patrick Hand SC), divider-tab
  section numbers, bulldog-clip figures, `--dom-*` colours for the seven domain tabs. Cover: navy with an amber band.
- Meanwhile links: focus on value ↔ Grace's strategy on a page; build quality in ↔ Ana's walking skeleton; let the team
  decide ↔ Grace's product trio; life cycles ↔ Grace's now / next / later.
- Case file: Book 3 card links to vol. 1; 15 timeline entries (tag `"3"`, red ✎). Landing: a Book 3 shelf row with the map.
- Verified: all 54 figures on contact sheets, 375 px on every new page, light and dark. PDFs are built by the workflow.
- **Not verified:** wording against the eighth edition itself. The six principle names, the domain names and the process
  counts (9 / 6 / 3 / 4 / 7 / 5 / 6) come from PMI's public pages and study guides. The focus-area grid in the deep dive is
  marked as an illustration. Check both against the guide before deploying, or soon after.
- Next: Vol. 2, Starting, Steering, Closing (Governance, 9 processes). Start the **project file** page there (charter first)
  and the first cheat sheet (PMBOK 8 on one page). Open story threads are listed at the end of the casebook section.

## 11. Vol. 2 notes on the build (2026-11-15)

- `project-2` journal, “Starting, Steering, Closing”: the **Governance** domain, all nine processes. Content in
  `content/project-2/01_starting_plan.py` (6 notes), `02_running.py` (6), `03_closing.py` (3). Story: 19 February → 22 May 2026,
  the Rotterdam launch from charter to closing report. Facts: casebook, “Book 3, Vol. 2”.
- Process → notes (also on the map): Initiate Project or Phase → charter, who decides, gates · Integrate and Align Project
  Plans → the plan, baselines · Plan Sourcing Strategy → sourcing · Manage Project Execution → directing the work, issue log ·
  Manage Quality Assurance → quality review · Manage Project Knowledge → lessons · Monitor and Control Project Performance →
  status, escalation · Assess and Implement Changes → change control · Close Project or Phase → gates, handover, closing.
- **Deep dives** (4): charter (business case vs charter vs plan; the retro-charter) · the plan (six cross-checks) · status
  (colour rules, a forecast sum, monitoring vs controlling, the watermelon) · change control (five steps, the seven-question
  impact check, approve / reject / defer).
- **The Rotterdam project file** (`/rotterdam/`, `render_project_file()`): every template card whose `file` starts with
  `rotterdam/` or `larder/`, from all `pmbok` journals, in book order (28 pages now). No extra field is needed: name a card's
  file `rotterdam/NN-name.md` and it appears. Linked from the journal index, the map and the shelf.
- **PMBOK map**: `PROCESSES` in `content/pmbok/map.py` now lists Governance's nine processes with focus area, plain words and
  notes. A caption says the names come from public summaries and should be checked against the guide. The PMBOK tag on a
  note shows a `processes` row (note field `pmbok["processes"]`).
- Sanne's mistakes, as planned: the 9 March misread (baselines), ten days of an unowned issue (issue log), status colours
  with no rules (status). The missed internet line ties to Ana's Vol. 2 fact (ordered 30 March).
- Money was made consistent across both volumes: cold room and fridges are €78k including the €14k door upgrade.
- Verified as Vol. 1: figures on contact sheets, 375 px, light and dark, every listed page exists.
- **Still not verified against the guide:** the nine Governance process names and their focus areas.
- Next: Vol. 3, What, and By When (Scope 6, Schedule 3). It returns to January–April 2026 for the worked examples (the
  work breakdown of the 71 must-haves, estimates, the fit-out's network and critical path, the release plan), so the
  project file gains scope and schedule pages with the same numbers. Sample deep dives: work breakdown structure, critical
  path, three-point estimates. The first cheat sheets (PMBOK 8 on one page; critical path) fit here.

## 12. Merge with main and deploy (2026-11-15)

- Main had gained a separate format, **Deep dives** (`/deep-dives/`, ten chapters, thirty minutes each) and a landing page
  with books stored spine-out. To avoid two things with one name, the in-note chapter of Book 3 is now called
  **“Going deeper”** on the site (index tag “+ goes deeper”). The field is still `deep_dive` and the journal set `deep_dives`.
- Book 3 has its own spine shelf on the landing page (`spine_shelf(..., "sanne", ...)`), with the PMBOK map as its first spine.
- Open question for the owner: should key PMBOK items (critical path, earned value, risk) also get a full ten-chapter
  deep dive in the Deep dives series? The in-note chapters don't replace that format.

## 13. Start here: state and next steps (2026-11-15)

### 13.1 Waiting for the owner

1. **PMBOK names.** Nothing was checked against the eighth edition itself. To check: the six principle names
   (`content/pmbok/map.py`, `PRINCIPLES`), the seven domain names and process counts 9 / 6 / 3 / 4 / 7 / 5 / 6 (`DOMAINS`),
   the nine Governance process names and their focus areas (`PROCESSES`), and the grid in the “What Do I Do When?” chapter
   (marked as an illustration). Fix the data file and the notes' `pmbok` tags, rebuild, redeploy.
2. **Full deep dives?** The owner asked for “deep-dive-like chapters for key items”. What exists is the lighter in-note
   “Going deeper” chapter. Asked on 15 Nov whether key PMBOK items (critical path, earned value, risk) should also get a
   ten-chapter page in the Deep dives series (`content/deep-dives/`, `scripts/dive.py`). No answer yet. Don't build one unasked.
3. **A look at the live pages**: `/project-1/`, `/project-2/`, `/pmbok/`, `/rotterdam/` and the Book 3 spine shelf on the
   landing page. The sandbox can't open github.io; only the workflow result was confirmed.

### 13.2 What exists (all on `main`)

| Thing | Where |
| --- | --- |
| Vol. 1, The Lay of the Land (15) | `content/project-1/` → `/project-1/` |
| Vol. 2, Starting, Steering, Closing (15) | `content/project-2/` → `/project-2/` |
| PMBOK map | `content/pmbok/map.py` → `/pmbok/` (`render_pmbok_map`) |
| Rotterdam project file (28 pages) | generated from template cards → `/rotterdam/` (`render_project_file`) |
| Journals, ratings, planned volumes | `scripts/build_notes.py`: `JOURNALS` (`project-1`, `project-2`), `PROJECT_ATTRS`, `PLANNED_PROJECT`, `SPINE_TITLES` |
| Skin and components | `public/assets/bujo.css`: `.theme-project`, `.pmbok`, `.dial`, `.deep`, `.dom-*`, `.pmbokmap`, `.projectfile` |
| Story facts | `docs/larder-casebook.md`: “Book 3, Vol. 1” and “Book 3, Vol. 2” |

### 13.3 How to write the next volume (written for Vol. 3; the same steps held for it, so reuse them for Vol. 4)

1. Branch from `main`. Read the two casebook sections for Book 3 and section 5 of this file (the volume table).
2. Add the `project-3` journal to `JOURNALS` (copy `project-2`; next term: `"Summer term · 2029"`, a start date in May 2029),
   remove vol. 3 from `PLANNED_PROJECT`, add `"project-3"` to `SPINE_TITLES`, set `deep_dives`.
3. Write `content/project-3/*.py`. Copy a note from `content/project-2/02_running.py` for the shape. Every note needs
   `pmbok=dict(covers=, domains=[…], processes=[…], principles=[…], focus=[…], older=)`, a `dial` (three tuples) and a
   template card named `rotterdam/NN-name.md` (continue the numbering from 16) so it joins the project file.
4. Story: it goes **back into January–April 2026**, the same launch, for the scope and schedule work behind what Vol. 2
   showed. Facts already fixed that Vol. 3 must use: 71 must-haves (6 app Musts from 3 March); milestones 3, 17, 20, 24,
   27 April; the 4 February planning session; fit-out by a builder (fixed price, handover 3 April, electrical inspection);
   cold room ordered 13 February with 8 weeks' lead time; first 15 pickers start 30 March; stocking 6–17 April; Grace's
   release plan of 9 March (R1 30 Mar, R2 13 Apr, R3 Rotterdam → June); must-haves done per week (casebook).
   New facts to invent and record: the work breakdown of the 71 must-haves by workstream, the estimates behind them, the
   fit-out's task network with durations (it must give a critical path that ends on 3 April and shows why 5 days of delay
   mattered on 23 March), float on the non-critical tasks.
5. Suggested notes (15): Scope: Plan for Scope · Requirements · The Scope Statement · Work Breakdown Structure ★ ·
   Acceptance and Sign-off (Validate Scope) · Scope Creep (Monitor and Control Scope). Estimating: Analogous, Parametric,
   Bottom-up · Three-Point Estimates ★ · Estimating with the Team. Schedule: Dependencies and the Network Diagram ·
   Critical Path ★ · Float and Buffers · Gantt Charts and Milestones · Crashing and Fast-Tracking · Release and Iteration
   Plans with Burn Charts. ★ = “going deeper”. Link, don't repeat: Grace's story mapping, thin slices, MoSCoW, roadmap vs
   release plan; Ana's last responsible moment.
6. Add the Scope and Schedule processes to `PROCESSES` in `content/pmbok/map.py` and link the Vol. column in `DOMAINS`.
   Names from public summaries: Scope: Plan Scope Management, Elicit and Analyze Requirements, Define Scope, Develop Scope
   Structure, Monitor and Control Scope, Validate Scope. Schedule: Plan Schedule Management, Develop Schedule, Monitor and
   Control Schedule. (Unverified, like Governance.)
7. Case file `TIMELINE` entries (tag `"3"`), a casebook section “Book 3, Vol. 3”, meanwhile links, README and both handoffs.
8. Cheat sheets that fit this volume (`content/cheatsheets/`, add to `CHEATSHEETS`): PMBOK 8 on one page; critical path.
9. Verify (section 4 of `docs/HANDOFF.md`): every figure on contact sheets, 375 px, light and dark, listed pages exist.
   Then merge `main`, PR, and deploy only when the owner asks.

### 13.4 Conventions that held for both volumes

- Title = the question; kicker = the official term. Third person, present tense, dates and numbers in every scene.
- One mistake of Sanne's per collection, told plainly.
- Quiz: three recall questions, two situational ones (“what does Sanne do?”).
- Numbers carry: budget €380k (fit-out €226k, equipment €48k, people €60k, marketing €40k, reserve €20k → €0.4k),
  final cost €379.6k. Check any new sum against the casebook before writing it into a card.
- Own words only; no PMI text, tables or figures. The PMI disclaimer is in the footer of every Book 3 page.

## 14. Vol. 3 notes on the build (2026-11-16)

- `project-3` journal, “What, and By When”: the **Scope** (6) and **Schedule** (3) domains. Content in
  `content/project-3/01_scope.py` (4 notes), `02_estimating.py` (3), `03_schedule.py` (5), `04_control.py` (3).
  The story goes back over **February → April 2026**: the work behind Vol. 2's plan. Facts: casebook, “Book 3, Vol. 3”.
- Process → notes (also on the map): Plan Scope Management + Plan Schedule Management → “How Will We Pin It Down?” ·
  Elicit and Analyze Requirements → requirements · Define Scope → scope statement · Develop Scope Structure → WBS ·
  Develop Schedule → the three estimating notes and five schedule notes · Monitor and Control Schedule → tracking ·
  Validate Scope → acceptance · Monitor and Control Scope → scope creep.
- **Going deeper** (4): WBS (nouns not verbs, the 100 % rule and three checks, the dictionary, WBS vs story map) ·
  three-point estimates (formulas, odds, adding estimates, limits) · critical path (both passes by hand, calendars,
  paths that change) · schedule tracking (milestone trend chart, burn-up, range forecast, float).
- **One worked example** runs through notes 08–12: the builder's 12-activity network (in the casebook). Its numbers were
  checked by a script: critical path 25 working days; C/D 4 days' float; the 23 March slip (+2 working days on G) gives
  8 April only because the builder doesn't work on Easter Monday. Keep that calendar fact if you touch the network.
- Sanne's mistakes: skipping the supplier small-print check (WBS: the internet line), anchoring the estimate (4 Feb),
  a bar chart with no links (12 Feb), no owner for the yes on extras (scope creep).
- **Vol. 2 corrected** while writing: one weekend of builder's work (28–29 March), not two; the 10 April quiz counts
  (4, 6, 5); the 27 March deep-dive counts (7, 4, 4). Casebook updated to match.
- New helper: `Doodle(..., exact=True)` (see `docs/HANDOFF.md` §5). Used on five dense Vol. 3 figures only.
- Project file: 43 pages (vols. 1–3). Map: Scope and Schedule rows filled, Vol. 3 linked.
- Verified: 53 figures on contact sheets, every new page at 375 px, light and dark, page-level views. PDFs left to the
  workflow. **Not verified against the guide**: the nine Scope and Schedule process names (from public summaries).
- **Next: Vol. 4, “Money and People”** (Finance 4 processes, Resources 5). Open threads are at the end of the casebook's
  “Book 3, Vol. 3”. Suggested “going deeper”: the budget and its reserves, earned value, resource levelling. Earned value
  can use the fit-out network and the €148k fixed price, so the numbers stay one example. Cheat sheets that fit: earned
  value; critical path (from this volume).

## 15. Vol. 4 notes on the build (2026-11-16)

- `project-4` journal, “Money and People”: the **Finance** (4) and **Resources** (5) domains. Content in
  `content/project-4/01_money.py` (8 notes) and `02_people.py` (7). Story: **January → May 2026**, the same Rotterdam
  launch, a third pass. Section 5's table had planned Utrecht and The Hague for this volume; staying with Rotterdam kept
  every number one example (the budget, earned value and the closing cost all reconcile). Facts: casebook, “Book 3, Vol. 4”.
- Process → notes: Plan Financial Management → money rules · Estimate Costs → cost estimates · Develop Budget → budget and
  reserves, cash flow · Monitor and Control Finances → committed and spent, earned value, forecasting, payback ·
  Plan Resource Management → RACI · Estimate Resources → people from demand · Acquire Resources → where they come from ·
  Lead the Team → leading without authority, team conflict · Monitor and Control Resourcing → levelling, availability.
- **Going deeper** (4): budget and reserves · earned value · resource levelling · leading without authority.
- The money reconciles across all four volumes: see the comment block at the top of `01_money.py`. **Vol. 2 corrected**:
  committed €335k (27 Feb, 13 Mar) and €355.5k (27 Mar), because the equipment order of 23 Feb had been left out.
- Sanne's mistakes: 20 % on signing without checking the payment run (cash) · “€61k spent” when €335k was committed ·
  borrowing Noord's pickers on King's Day · planning Eli at 100 % on Rotterdam.
- Dense figures use `Doodle(..., exact=True)`. 49 figures checked on contact sheets; 375 px; every listed page exists.
- **Not verified against the guide**: the nine Finance and Resources process names (from public summaries).
- **Next: Vol. 5, “People Outside, and Surprises”** (Stakeholders 7, Risk 6). Open threads are at the end of the
  casebook's “Book 3, Vol. 4”. The risk notes can reuse the three-point estimates (Vol. 3) and the reserve (Vol. 4);
  a Monte Carlo note can use the fit-out network. Antwerp (September 2027) is the natural setting for stakeholders abroad.

## 16. Handoff: Vols. 5 and 6 (2026-11-17)

Read this section, then 13.3 (the steps) and 13.4 (the conventions). Sections 14–15 explain what the last two volumes
added to the toolkit. The story facts are in `docs/larder-casebook.md`; the Book 3 sections there end with open threads.

### 16.1 Where Book 3 stands

| Vol. | Key | Domains | Notes | State |
| --- | --- | --- | --- | --- |
| 1 · The Lay of the Land | `project-1` | foundations, principles | 15 | live (PR #24) |
| 2 · Starting, Steering, Closing | `project-2` | Governance (9) | 15 | live (PR #24) |
| 3 · What, and By When | `project-3` | Scope (6), Schedule (3) | 15 | live (PR #29) |
| 4 · Money and People | `project-4` | Finance (4), Resources (5) | 15 | live (PR #29; deploy run 43813764513 succeeded) |
| 5 · People Outside, and Surprises | `project-5` | Stakeholders (7), Risk (6) | 15 | written (section 17) |
| 6 · Making It Yours | `project-6` | tailoring, models, methods, artefacts, newer topics | 15 planned | this section |

After Vol. 5, all **40 processes** are covered (9 + 6 + 3 + 4 + 5 + 7 + 6). Vol. 6 adds no processes: it covers the
guide's chapters around them (tailoring, models / methods / artefacts, the newer topics) and closes the book.

Still waiting for the owner (unchanged from 13.1): the PMBOK names have never been checked against the guide; no answer
on full ten-chapter deep dives for key items; nobody has looked at the live Book 3 pages.

### 16.2 Rules that held for Vols. 1–4 (keep them)

- **One worked example per volume, reconciled by script.** Vols. 2–4 all used the Rotterdam launch, so every number
  agrees. Write the numbers into a comment block at the top of the first content file (as `content/project-4/01_money.py`
  does) and check sums, dates and weekdays with a short Python script before writing prose. Weekdays matter:
  27 April 2026 is a Monday and King's Day; Easter Monday 6 April 2026 is a day off for the builder.
- **Fix earlier volumes when you find a contradiction**, and say so in the casebook section and the PR. Vols. 3 and 4
  each corrected Vol. 2 (one weekend, not two; committed €335k / €355.5k).
- **One mistake of Sanne's per collection**, told plainly, with what it cost and how she fixed the cause.
- **Template cards are project-file pages**: `file="rotterdam/NN-name.md"` (Vol. 4 ended at 45). For the Antwerp and
  Eindhoven volumes use a new prefix (see 16.3) and extend `render_project_file()` so its title and lead name more than
  one project (it now says “The Rotterdam Project File”; rename the page to “The Project File” and group by project, or
  add a second page; decide before the first Vol. 5 card).
- **Figures**: plain rows and boxes render with the stylesheet's fixed sizes (heads 21px, body 19px; the `size=`
  argument has no effect). Charts, tables and grids use `Doodle(..., exact=True)` so the sizes apply. Check every figure
  on contact sheets (scripts in section 4 of `docs/HANDOFF.md`).
- **Meanwhile links** go both ways automatically; four to six per volume.
- Process names on the map are **unverified** (public summaries); keep the caption.

### 16.3 Vol. 5, “People Outside, and Surprises”: Stakeholders and Risk

**Setting: the Antwerp launch, October 2026 → October 2027.** It's the first city abroad and the one launch where the
risk register matters most, and the other books already fix its shape. Sanne runs Utrecht (12 Apr 2027) and The Hague
(14 Jun 2027) from the playbook in the background; Antwerp is the project. Use the prefix `antwerp/NN-name.md` for its
cards, numbering from 01.

**Facts already fixed by other books (don't contradict):**
- Antwerp planning date **September 2027** (not committed, Apr 2026). Decision calendar: store lease by **Dec 2026**
  (Femke), Belgian invoices and VAT by **Mar 2027** (Marco), French and Dutch in the apps by **May 2027** (Grace),
  courier contracts by **May 2027** (Joost), **Bancontact** by **Jul 2027** (Cho).
- French shipped in **May 2027**; **40 Antwerp households** tested in **July and September**; Belgian VAT 6 % / 21 %;
  fr-BE and nl-BE by native writers (Grace, Vol. 6 of Book 2, `content/product-6/01_markets.py`).
- **ADR 0024** (2 Aug 2027): the Antwerp test found **212 products** disagreeing across Catalogue, WMS B and billing.
- **Antwerp opened Mon 18 Oct 2027, slipped from September**; week 1: 2.4 tickets per 100. Eindhoven opened 22 Nov 2027.
- Ana's first architecture kata (19 Jan 2027) was “Larder in Antwerp”. Ana's capacity plan (18 Oct 2027) assumed it.

**One gap to fill on purpose: why Antwerp slipped.** No book says. Vol. 5 should make it a **risk that was on the
register and was managed badly**, so the volume has its central story. Recommended: the city's **permit for the
store's cooling plant and night-time deliveries** (Antwerp is not Rotterdam; different rules, a different language of
officialdom). Sanne's stakeholder mistake: she treated the city's permit office as a form to fill, not a stakeholder,
and the risk sat on the register rated “low” with no owner and no response. Planned opening **Mon 13 Sep 2027**, actual
**Mon 18 Oct 2027** (five weeks). It mustn't contradict the data mismatch (ADR 0024, fixed by 30 Sep) or Grace's
testing in September; it doesn't. Record the choice in the casebook.

**Processes (names unverified; earlier searches found the counts, not the names).** Likely, from public summaries of
older editions: Stakeholders: identify stakeholders · plan stakeholder engagement · plan communications · manage
stakeholder engagement · manage communications · monitor stakeholder engagement · monitor communications. Risk: plan
risk management · identify risks · analyse risks · plan risk responses · implement risk responses · monitor risks.
Search again for the eighth edition's exact names before filling `PROCESSES` in `content/pmbok/map.py`.

**Suggested notes (15), with the titles earlier volumes already promise in bold.** Earlier volumes link to
“Contingency vs management reserve”, “Simulation in plain words” and “Risks vs issues” as plain text; either use those
phrases in the kickers or update those `related` lines (grep for `(vol. 5)` in `content/project-*`).

| # | Title (the question) | Covers | Antwerp scene |
| --- | --- | --- | --- |
| 1 | Who Cares About This? | identify stakeholders, the register | landlord, city permit office, food-safety agency (FAVV-AFSCA), neighbours, Belgian couriers, Bancontact provider, local suppliers |
| 2 | Who Matters Most, and How Much? ★ | power / interest, engagement matrix (current vs desired) | the permit office rated “keep informed” when it should have been “manage closely” (Sanne's mistake) |
| 3 | Who Hears What, and When? | communications plan | Dutch for the city, French for some customers, English inside Larder |
| 4 | How Do We Keep Them With Us? | managing engagement and expectations | the neighbours' meeting Rotterdam never had (Rotterdam told them on 2 Mar, late) |
| 5 | Are We Being Understood? | managing communications, meetings that work | a Belgian supplier meeting that agreed nothing |
| 6 | Different Country, Different Rules | stakeholders abroad: language, culture, regulators | Lena and a Belgian lawyer; the permit language |
| 7 | Are They Still With Us? | monitoring engagement | the engagement matrix re-scored monthly |
| 8 | How Will We Handle Risk? | plan risk management: appetite, scales, owners | Femke's appetite for a five-week slip vs a second rent month |
| 9 | What Could Happen? ★ | identify risks, the risk register, opportunities | the register in Nov 2026; the permit risk scored low (the mistake, again) |
| 10 | How Likely, and How Bad? | qualitative analysis, probability × impact | re-scored after a call with a Belgian builder |
| 11 | What Is It Worth? | expected monetary value; **contingency vs management reserve** | sizing Antwerp's reserve from EMV (Vol. 4 sized Rotterdam's by doubling a list) |
| 12 | What If We Ran It a Thousand Times? ★ | **simulation in plain words** (Monte Carlo) | the opening date as a range: P50, P80; script it, record the seed |
| 13 | What Do We Do About It? ★ | responses: avoid, transfer, mitigate, accept; exploit, enhance, share; escalate | the permit: a local agent (transfer), early drawings (mitigate) |
| 14 | Did We Do What We Said? | implementing responses, owners, triggers | the response that had no owner |
| 15 | Is the List Still True? | monitoring risks; **risks vs issues** | the permit risk becomes an issue in July; the slip; the lesson into the playbook v3 (Oct) |

Collections: “Who's involved” (1–4), “Abroad” (5–7), “What could happen” (8–12), “Doing something about it” (13–15).
Going deeper ★: the engagement matrix, the risk register, simulation, risk responses.
Meanwhile links: Ana's stakeholder map and risk-storming (`architect-1`), Ana's risk register (`architect-6`),
Grace's pre-mortem (`product-3`), Grace's localisation and launching a new city (`product-6`).
New characters (add to the casebook's cast if used): Antwerp's store manager; a Belgian lawyer working with Lena.
Money and dates: Antwerp needs its own budget, written as Rotterdam's was (lines, reserve sized from EMV). Invent it
once, reconcile it by script, and keep it in the casebook.

### 16.4 Vol. 6, “Making It Yours”: tailoring, models, methods, artefacts, and growing

**Setting: Eindhoven and the 2028 plan, November 2027 → mid-2028.** Eindhoven opened **22 Nov 2027**, run from the
playbook. The board plan of 20 Mar 2028 is **eight cities and 60,000 orders a day by end 2028**. Ana's Vol. 6 risk
register (`content/architect-6/03_risk.py`, started 24 Apr 2028) already names **Ghent (June 2028; store opening 19 Jun)** and
**Haarlem (September 2028)**; reuse them. Grace hands
part of her area to Jonas in Jan–Feb 2028; Ana's Vol. 6 runs Apr–Sep 2028. Sanne's arc: from running launches to
running the **programme** of 2028 cities, hiring a second project manager under Marco's cap, and handing launches over.
Card prefix: `programme/NN-name.md` (or `eindhoven/`).

**Titles earlier volumes promise:** “Tailoring a whole project”, “The city launch playbook”, “benefits realisation”
(grep `(vol. 6)`).

| # | Title | Covers | Scene |
| --- | --- | --- | --- |
| 1 | How Light Can We Go? | **tailoring a whole project** | Eindhoven: the playbook, one page of tailoring, half the meetings |
| 2 | Can a Launch Be a Recipe? ★ | **the city launch playbook** (v1 Utrecht, v2 The Hague, v3 Antwerp, v4 Eindhoven) | what changed after each city |
| 3 | One Project, or Many? | projects, programmes and portfolios | eight cities in 2028: Sanne's programme board |
| 4 | Did We Get What We Paid For? | **benefits realisation** | Rotterdam's three benefits checked (500 a day met in May 2026; on time; the 8-week playbook) |
| 5 | Which Tools, When? | models (situational leadership, Tuckman, change models), methods (Scrum, Kanban, CPM), choosing among them | the toolbox page |
| 6 | Which Documents Earn Their Keep? | artefacts: the project file reviewed | which of the 58 Rotterdam pages were used again |
| 7 | Can AI Help? ★ | AI in project work (a newer topic in the eighth edition) | summarising status, drafting risks, checking a plan; limits and confidentiality |
| 8 | What Does It Leave Behind? | sustainability in practice | Korenwolf's supplier questionnaire (casebook, carbon, 6 Mar 2028) |
| 9 | Who Helps the Project Managers Now? | the PMO grown up (from Vol. 1's launch desk) | a second PM; templates that are actually reused |
| 10 | Who Serves Whom? | servant leadership in practice | Sanne coaching the new PM through Ghent |
| 11 | What Would You Do? | ethics and professional conduct | pressure to report green before an investor meeting |
| 12 | How Do I Get Better at This? ★ | growing as a project manager (and what certification is for) | Sanne's two-year review |
| 13 | Who Do We Hire? | hiring a project manager | the work-sample interview |
| 14 | Can Someone Else Run This? | handing over a programme | Ghent, then Haarlem, handed to the new PM |
| 15 | What Was It All For? | the book's closing note: the six principles revisited | back to Vol. 1, two years on |

Collections: “Fitting it to the work” (1–4), “Models, methods, artefacts” (5–8), “Growing” (9–15; or split 9–11 and
12–15). Going deeper ★: playbook, AI, growing, plus tailoring a whole project.
Meanwhile links: Grace's hiring a PO and handing over (`product-6`), Ana's growing architects and handover to
operations (`architect-6`), Grace's launching a new city (`product-6`).
Check before writing: the casebook's “Book 2, Vol. 6” and “Book 1, Vols. 5–6” sections for 2027–28 facts (openings,
Jonas, Grace's two-year review, Ana's Ghent register).

### 16.5 When Book 3 is complete (after Vol. 6)

- `PLANNED_PROJECT` empty; case file `BOOKS` card “complete: 6 volumes”; future log: remove the Book 3 line, keep Book 4
  (Mo, client management) as the next book.
- PMBOK map: every row linked; the “Still to come” list disappears by itself when `PLANNED_PROJECT` is empty (check it).
- README, `docs/HANDOFF.md` (status, table, next steps) and this file's status line.
- Cheat sheets not yet made (from section 6): PMBOK 8 on one page; earned value; critical path. They fit after Vol. 6.
- Before deploying: fetch and merge `main` (other sessions merge to it); verify; PR; merge when the owner asks.

## 17. Vol. 5 notes on the build (2026-11-17)

- `project-5` journal, “People Outside, and Surprises”: the **Stakeholders** (7) and **Risk** (6) domains. Content in
  `content/project-5/01_involved.py` (4 notes), `02_abroad.py` (3), `03_could_happen.py` (5), `04_doing.py` (3). Story:
  **the Antwerp launch, 5 Oct 2026 → 18 Oct 2027**. Facts: casebook, “Book 3, Vol. 5”; every number in the comment block at
  the top of `01_involved.py`.
- **The story gap, filled as planned:** Antwerp slipped five weeks (13 Sep → 18 Oct 2027) because of **R-07, the city's
  environmental permit** (cooling plant + deliveries before 07:00, a 30-day public inquiry). The arc runs through the whole
  volume: placed in the wrong box (9 Nov) → scored 3 with owner “builder” (30 Nov) → found by Maarten and Pieter (8 and
  10 Feb, re-scored 16) → responses (22 Feb) → the drawings action had no Larder owner (2 Apr; lodged 19 Apr) → 14 objections
  in the inquiry (22 Jun) → issue I-12 (15 Jul) → option B, open 18 Oct (23 Jul) → permit 6 Sep → playbook v3.
- Process → notes (also on the map): Identify Stakeholders → register, abroad · Plan Stakeholder Engagement → power and
  interest, abroad · Plan Communications Management → communications plan · Manage Stakeholder Engagement → expectations ·
  Manage Communications → meetings · Monitor Stakeholder Engagement + Monitor Communications → monitoring engagement ·
  Plan Risk Management → risk approach · Identify Risks → register · Analyze Risks → probability and impact, EMV, Monte Carlo
  · Plan Risk Responses → responses · Implement Risk Responses → implementing · Monitor Risks → risk monitoring.
  **All 40 processes now have a note.**
- **Process names:** the seven Stakeholders names match a public summary of the eighth edition. The six Risk names are
  **not confirmed** (searches on 17 Nov found the count, not the names); “Analyze Risks” stands for the older qualitative and
  quantitative pair. The map's caption already says to check them against the guide.
- **Going deeper** (4): the engagement matrix (four boxes, C vs D, salience, wrong boxes) · the risk register (cause-event-
  effect, sources, opportunities, five columns) · Monte Carlo (the model, ranges, reading P50 / P80, limits, was 18 Oct in
  the chart) · risk responses (five threat and four opportunity responses, is it worth it, residual and secondary).
- **Simulation**: a seeded script (1,000 runs, seed 2027) gave P50 13 Sep, P80 27 Sep, P90 11 Oct; 97 % of late runs
  permit-driven. Re-runs with lodging fixed at week 7 (P50 20 Sep, P80 11 Oct) and with objections (P50 11 Oct, P80 25 Oct)
  are quoted in the notes. The model is written out in card `antwerp/12-opening-range.md`; re-create it from there.
- **The project file** (`/rotterdam/`, kept for old links) is now **“The Project File”**, grouped by project:
  `PROJECT_FILE_GROUPS` in `scripts/build_notes.py` (Rotterdam: `rotterdam/`, `larder/`; Antwerp: `antwerp/`). 73 pages.
  Vol. 6 adds a group (e.g. `programme/`) with one line there.
- Earlier volumes' plain-text promises (“Contingency vs management reserve”, “Simulation in plain words”, “Risks vs
  issues”) now resolve through the kickers of notes 11, 12 and 15 (`a.k.a. “…”`).
- Sanne's mistakes: the permit office in “keep informed” (stakeholders) · the supplier meeting in English with no agenda
  (abroad) · R-07 scored by Rotterdam's rules with an outside owner (risk) · the response action with no Larder owner (doing).
- Meanwhile links: register ↔ Ana's stakeholder map · abroad ↔ Grace's localisation · risk register ↔ Ana's risk register and
  Grace's pre-mortem · risk monitoring ↔ Grace's launching a new city.
- **Next: Vol. 6, “Making It Yours”** (section 16.4). Open threads at the end of the casebook's “Book 3, Vol. 5”.
