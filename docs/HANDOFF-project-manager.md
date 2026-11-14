# Handoff: The Project Manager's Notebook (Series 2, Book 3)

Status as of 2026-11-14: **Proposal. Nothing built. Owner decisions needed in section 9.**

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

New note fields: `pmbok=dict(domain=, focus=, processes=[…], principles=[…], older="…")`, `dial`, `file_page`.
New generated pages: the **PMBOK map** (`/project/map/`) and the **project file** (`/project/file/`).

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

## 9. Decisions needed (owner)

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
