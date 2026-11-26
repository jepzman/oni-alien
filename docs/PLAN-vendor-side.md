# Plan: On the Client's Floor (Series 5) · the vendor architect's notebook

Status as of **2026-11-25: plan approved; a sample note is up for review (section 12). Writing has not started.**
Owner's decisions are in section 11.

The idea (owner, 25 Nov): a new series where the architect and team are a **vendor**, working for **MetroVolt**: a
difficult electricity distribution company with plenty of difficult people, legacy applications, office politics, a
competing vendor and a lot of stress.

Read first, for facts and format:
- `docs/HANDOFF-darkside.md`: MetroVolt, its cast, its history and its timeline (Series 4). That series is the
  source of truth for everything inside MetroVolt. This plan reuses it and must not contradict it.
- `docs/HANDOFF-solution-architect.md` and `docs/HANDOFF-it-operations.md`: the Series 2 note format this series
  builds on.

## 1. What the series is

*On the Client's Floor: Notes from the Vendor Side.* A practitioner's notebook in the Series 2 tradition (one story, one
narrator, a technique per note, a template to copy and a try it), but written **from the other side of the contract**.
Ana at Larder was the client's own architect. Here the architect is the outsider: she is paid by the hour, has a visitor
badge, has to bid for the work before she can do it, and can be replaced by a cheaper firm at the next renewal.

It teaches what no architecture course covers: reading a tender, estimating in fog, writing assumptions that protect
you, statements of work and change control, finding your way into a 30-year-old legacy estate, multi-vendor blame,
honest status reports, client politics you can see but not touch, and keeping a team sane on a fixed-price deal.

| | Series 2 (Larder) | Series 4 (Darkside) | **Series 5 (On the Client's Floor)** |
| --- | --- | --- | --- |
| Narrator | the client's own staff | a MetroVolt insider (the Chronicler) | **a vendor's lead architect** |
| Company | a young start-up | MetroVolt (satire) | **MetroVolt (realistic), seen from outside** |
| Subject | practice inside a company | people and survival | **architecture, delivery and politics across a contract** |
| Voice | calm study notes | gothic, deflated by footnotes | **calm and practical, with dry humour and visible stress** |
| A note is | one technique | one creature or curse | **one problem a vendor team meets, and how to handle it** |

**The two MetroVolt series share one world.** Darkside shows MetroVolt from the inside as satire. On the Client's Floor
shows the same company from outside, played straight. The same people appear (Lord Varnish, Ottoline Grey, Gareth
Pound, Priya Nair, Pip, Vexmoor Consulting, Halvorsen Systems), the same events happen on the same dates, and notes
link both ways (section 8).

## 2. The story

**The setup.** MetroVolt runs its 2.3 million customer accounts on **MAVIS**, a customer information system built
in-house in **1997** (COBOL on a mainframe, about 4 million lines, nightly batch). Billing has run on **Halvorsen
Systems** since 2016, fed by MAVIS through a file at 02:10 every night. In January 2024 Lord Varnish launched
**Project Orion** to replace both; Vexmoor Consulting was its delivery partner. By November 2026 Orion was 18 months
late, £2.4m over budget and on its fourth lead (Darkside Act I). It was **quietly cancelled in January 2027**.

The problem didn't go away: 11,400 smart meters are still not reporting (63 days on average), the regulator wants a
plan, and MAVIS's last two COBOL specialists retire within three years. So in **February 2027** MetroVolt goes to
tender for **Project Lodestar**: a new customer platform that replaces MAVIS in waves and connects smart-meter data to
Halvorsen billing.

**The vendor.** **Wrenfield Digital**, an 80-person consultancy in Leeds. Good engineers, a thin bench, and nothing
this size on its books before. Lodestar would be a third of next year's revenue.

**The arc.** Ines and her team win Lodestar against Vexmoor (who built half of Orion) and Halvorsen (the incumbent who
wants the whole thing). They sign just before MetroVolt's **Project Horizon** reorg (May 2027, led by Rupert Thorne with
Vexmoor as advisers) moves Lodestar under the transformation office. From then on the losing bidder is advising the client
on the winner's project. They dig into MAVIS and find it worse than anyone said, re-price honestly, survive a watermelon
status report, a steering committee ambush, a multi-vendor blame war over the 02:10 file, a go-live, the loss of their
sponsor and one team member's burnout. At the end they bid for phase 2 against Vexmoor. **The series ends open, on a cliffhanger** (section 11): the
phase 2 decision is not given.

**Each volume adds one way of seeing.** Vol. 1: the deal. Vol. 2: the contract. Vol. 3: the legacy. Vol. 4: the delivery.
Vol. 5: the people. Vol. 6: the cost to the team, and the ending.

## 3. Timeline (fits Darkside's dates)

| Date | Lodestar | Darkside, same date |
| --- | --- | --- |
| Jan 2027 | | Orion quietly cancelled (Act I) |
| 3 Feb 2027 | Lodestar tender published: 212 requirements, 6 weeks to respond | Act III winter: Pip on Gareth's meter fix |
| 17 Feb | Wrenfield's bid / no-bid: 6 for, 2 against (Ines against, then for) | |
| 24 Mar | Bid submitted: £4.8m fixed price for wave 1 after £380k time-and-materials discovery | |
| 21 Apr | Orals: Wrenfield, Vexmoor, Halvorsen. Wrenfield shortlisted with Vexmoor | |
| 6 May | Preferred bidder: Wrenfield | **Project Horizon announced** (Act V); Vexmoor are Rupert's advisers |
| May → Jun | Contract paused for "re-approval under Horizon"; letter of intent, Wrenfield works at risk | Horizon role cuts |
| 30 Jun 2027 | Contract signed | |
| 5 Jul | Mobilisation: six Wrenfield people on floor 19; laptops on day 23 | |
| Sep → Dec 2027 | Discovery: MAVIS archaeology; the 02:10 job; 31 % of addresses fail validation | 1 Sep: Horizon's Value Streams live |
| 14 Dec 2027 | Discovery report and change request CR-007: +£1.1m, +4 months | Calibration in room 27A (Act IV) |
| Feb 2028 | CR-007 agreed at +£700k, +3 months, scope trimmed | |
| Mar → Aug 2028 | Build and test; watermelon report (April); Halvorsen interface war (May); steering ambush (June) | Ruth Calloway starts 13 Mar (Act IV) |
| 6 Sep 2028 | Go / no-go for wave 1 (380,000 accounts) | |
| 23 Sep 2028 | Wave 1 cutover night | GridSight launched (Act VI) |
| Oct 2028 → Jan 2029 | Hypercare; sponsor change; wave 2 planning; burnout | |
| Mar 2029 | Phase 2 (waves 2–4) bid against Vexmoor | Halvorsen billing re-tender (Act VI) |
| Jun 2029 | The ending: handover, the last day on floor 19, and the phase 2 envelope unopened | |

## 4. Cast

Pronouns are stated and must stay consistent.

**Wrenfield Digital (the vendor)**

| Character | Role | Notes |
| --- | --- | --- |
| **Ines Duarte** (she/her) | lead solution architect, the **narrator** | 15 years in-house at a water company, joined Wrenfield in 2025. Lodestar is her first big deal on the vendor side. |
| Callum Reid (he/him) | engagement manager | owns plan, budget and the client relationship day to day. Calm in public, spreadsheets at midnight. |
| Hana Sato (she/her) | tech lead | the best engineer at Wrenfield; quietly carries too much (Vol. 6 burnout). |
| Bilal Khan (he/him) | business analyst, data migration | finds the 31 %. |
| Oskar Lind (he/him) | test lead | has never seen a test environment he trusted. |
| Lottie Marsh (she/her) | junior engineer, first client | the reader stand-in: asks the obvious questions. |
| Vivian Locke (she/her) | account director (sales) | promised "twelve months" over dinner before the tender came out. |
| Graham Wren (he/him) | founder and managing director | needs the deal, then needs the margin. |

**MetroVolt (the client).** Existing characters from Darkside keep their roles and dates. New ones:

| Character | Role | Notes |
| --- | --- | --- |
| Elaine Corbett (she/her) | Lodestar programme director | Orion's last programme manager; survived it, trusts no vendor. |
| Hollis Wade (he/him) | head of IT architecture, chairs the design authority | rejects anything he didn't draw. |
| Desmond Rook (he/him) | procurement lead | the rules, the forms, the gifts register. |
| Bert Ogundipe (he/him) | MAVIS's senior COBOL programmer, 31 years at MetroVolt | the person who knows; retires in 2029. |

Existing Darkside cast used here: **Lord Varnish** (Simon, VP of Synergy, Orion's founder), **Priya Nair** (Customer Ops,
then Director of Customer from Oct 2027: Lodestar's first sponsor), **Rupert Thorne** (Horizon), **Gareth Pound** (Network
Assets, owns the meter data and wants Lodestar in his empire), **Ottoline Grey** (Chief of Staff), **Pip** (cameo: the
Orion survivor who warns Ines over coffee). **Vexmoor**: Oliver Thane (partner), Bea (analyst). **Halvorsen**: Sven
Aldous (still brings biscuits). Before writing, check every cameo's role and date against `HANDOFF-darkside.md` and
the `story-act-*.py` files.

## 5. Note format

Kept from Series 2: the scene (dated, with a number), the analogy with doodles, how it works, a template card, try it,
the quiz, nine ratings, related notes, one PDF per volume. Added for the vendor side:

| Part | What it holds |
| --- | --- |
| **Both sides of the table** | the same moment as MetroVolt sees it and as Wrenfield sees it, side by side. The heart of the series. |
| **What the contract says** | the clause that applies (from Lodestar's SOW, which the series writes as it goes: §4 scope, §7 change control, §9 acceptance, §12 key personnel …), in plain words. |
| **Account health: green / amber / red** | replaces gains vs losses: how the same move changes when the relationship is healthy, strained, or at war. |
| **Pressure gauge** | 1–5, how stressful this situation is for the team, with what it costs them (sleep, weekends, trust). |
| **The 23:00 note** | two or three lines from Ines's private notebook at the end of the day. The honest, tired voice; where the stress shows. |
| **Seen in the Grimoire** | when a Darkside creature appears (the Seagull Overlord at steering, the Credit Vampire on a status slide), a link to its entry. |

**Ratings (`VENDOR_ATTRS`)**, for the note's main move, high = good: client trust, team health, margin protected,
scope clarity, technical integrity, risk control, political cover, speed, low overhead.

**Ethics rule.** Notes on politics, rivals and pressure show the clean move working and the dirty move backfiring (as
in Darkside's forbidden spells). The series never teaches bid rigging, poaching client staff against contract terms,
hiding defects or lying in a report. Contract and procurement notes carry a footer: illustrative, not legal advice;
real contracts and public procurement rules differ by country.

## 6. Skin proposal: `theme-vendor`, the site daybook

- **Paper:** a black hardback consultant's daybook, cream pages with faint ruled lines and a date header.
- **Furniture:** a **visitor pass** clipped to the top of every note ("WRENFIELD · VISITOR · ESCORT REQUIRED", with the
  day number on site); a **timesheet strip** in the margin (hours billed vs hours worked: the gap grows in Vol. 4);
  **redline** markup (tracked-changes strikeouts and inserts) on contract boxes; rubber stamps: "CHANGE REQUEST",
  "ACCEPTED SUBJECT TO", "NOT IN SCOPE".
- **Palette:** MetroVolt hi-vis yellow, Wrenfield teal, redline red, pencil grey. Dark mode: the daybook under a desk
  lamp at 23:00.
- **Type:** a clean grotesque for titles, Kalam or Caveat for Ines's handwriting and the 23:00 note, Courier Prime for
  contract clauses.
- **Doodles:** the usual doodle style. The MetroVolt tower (The Grid, 31 storeys) appears from outside, through glass.

## 7. Volumes (6 × 15 notes, ★ = flagship with a longer scene)

### Vol. 1 · Winning the Work (`vendor-1`, Feb → May 2027)
1. Reading a Tender Like an Architect ★ · 2. Bid or No Bid? · 3. Who Wrote This Tender? (requirements copied from
Orion) · 4. Clarification Questions That Win · 5. Solution Design on Two Pages of Facts · 6. Assumptions, Dependencies
and Exclusions ★ · 7. Estimating in Fog (Orion as the reference class) · 8. Fixed Price, Time and Materials, or Capped?
· 9. The Incumbent in the Room (Halvorsen) · 10. Up Against a Big Consultancy (Vexmoor) · 11. When Sales Has Already
Promised · 12. The Orals ★ · 13. References and Site Visits · 14. Best and Final Offer: What Not to Give Away · 15. From
Bid Team to Delivery Team

### Vol. 2 · Signing and Starting (`vendor-2`, May → Sep 2027)
1. The Statement of Work, Clause by Clause ★ · 2. Acceptance Criteria You Can Pass · 3. Change Control That Isn't a War
· 4. The Contract Stalls (Horizon's re-approval) · 5. Letters of Intent and Working at Risk · 6. Day One on the Client's
Floor · 7. Access Purgatory (23 days for a laptop) · 8. Mapping the Client from Outside · 9. The Kick-off That Sets the
Rules ★ · 10. Steering, Design Authority, Working Groups · 11. The Multi-Vendor RACI · 12. Your Client Counterpart
(Elaine) · 13. Working Across Two Companies · 14. The First Status Report · 15. The Baseline ★

### Vol. 3 · Digging Up the Legacy (`vendor-3`, Sep 2027 → Feb 2028)
1. Software Archaeology: Mapping MAVIS ★ · 2. The Person Who Knows (Bert) · 3. Reading Code Nobody Owns · 4. The 02:10
Job · 5. Profiling the Data Before You Move It (the 31 %) · 6. Talking to a Mainframe · 7. The Incumbent's Interface ·
8. A Strangler Plan for a Customer System ★ · 9. The Discovery Report That Changes the Price · 10. Telling a Client
Their System Is Worse Than They Think · 11. The Honest Change Request (CR-007) ★ · 12. Regulated Data and Security
Reviews · 13. Migration in Waves · 14. When the Client Overrules Your Design (Hollis) · 15. Design Authority Day

### Vol. 4 · Delivery Under Fire (`vendor-4`, Mar → Sep 2028)
1. The Watermelon Report ★ · 2. A RAID Log People Read · 3. Scope Creep Through the Side Door · 4. When Another Vendor
Blames You (Halvorsen and the 02:10 file) · 5. The Rival Becomes the Client's Adviser ★ · 6. The Steering Committee
Ambush · 7. Escalating Without Burning the Account · 8. Re-planning a Slipping Programme · 9. Testing in Environments
You Don't Control · 10. The Defect Triage War · 11. When to Read the Contract Aloud · 12. Protecting Margin Without
Cutting Corners · 13. Cutover Planning · 14. Go / No-Go ★ · 15. Wave 1 Night

### Vol. 5 · Other People's Politics (`vendor-5`, Sep 2028 → Jan 2029)
1. Reading the Client's Politics from Outside ★ · 2. Your Sponsor Leaves · 3. The Stakeholder Who Holds the Budget
(Gareth) · 4. Lord Varnish Wants a Slide · 5. Saying No to a Client · 6. Liked or Trusted? · 7. Dinners, Gifts and the
Register · 8. Sharing a Floor with the Rival · 9. When Client Staff Fear You'll Take Their Jobs · 10. Managing Up in Your
Own Firm (Graham and the margin) · 11. Protecting Your Team from the Client ★ · 12. The Client Who Shouts · 13. What
You Hear in the Lift · 14. When the Client Asks You to Change the Numbers ★ · 15. Building a Champion

### Vol. 6 · The Cost and the Ending (`vendor-6`, Jan → Jun 2029)
1. Stress on a Vendor Team ★ · 2. Your Own 23:00 Problem · 3. Sustainable Pace on a Fixed-Price Deal · 4. Rotating
People Off an Account (Hana) · 5. Hypercare and the Hangover · 6. Warranty and the Long Tail · 7. Knowledge Transfer
That Sticks · 8. A Lessons Session Both Sides Attend · 9. The Phase 2 Bid ★ · 10. Losing a Deal Well (or winning one) ·
11. The Case Study and the Reference · 12. The Handover Architecture · 13. When to Walk Away from a Client ★ · 14. What
the Vendor Side Taught Me · 15. The Last Day on Floor 19

## 8. Links to the other shelves

- **Darkside:** "Seen in the Grimoire" on about one note in four (Sacrificial Lamb for Orion's history, Rigged RFP,
  Incumbent Dragon, Bake-Off Arena, Overpromise Golem, Seagull Overlord, Dark Pact, Slow Hex of Burnout …). Add a
  matching "meanwhile, a vendor's view" line on the Darkside entry only if the owner wants Darkside touched.
- **Series 1:** related notes link to the patterns used (Strangler Fig, anti-corruption layer, batch file transfer, CDC,
  idempotent loads); Series 1 notes get a "seen at MetroVolt" line beside "seen at Larder".
- **Book 1 (Ana):** a few notes compare: Ana's ADR with Ines's assumptions log; Ana's architecture review with Hollis's
  design authority. No story crossover with Larder.
- **Cheat sheet (later):** *The Vendor's Contract Card*: SOW sections, change-control flow, pricing models, red-flag
  clauses.

## 9. Extras (once two volumes exist)

1. **The Lodestar file** (`/lodestar/`), like Larder's case file: MetroVolt from outside, the tender, the cast on both
   sides, the timeline, and the **SOW as it grows** (every clause the notes quote, in one document, with redlines by date).
2. **The change log:** every change request (CR-001 …) with cost, days and outcome; the money story of the programme.
3. **The org chart from outside vs inside:** Ines's power map next to Darkside's Map of Hidden Thrones.

## 10. Build notes (when we start)

- Journal keys `vendor-1` … `vendor-6`, content in `content/vendor-N/`, `series=5`, narrator Ines, theme `theme-vendor`.
- New note fields: `both_sides=(client_html, vendor_html)`, `contract=(clause, plain)`, `health=dict(green=, amber=,
  red=)` (renders where gains/losses would), `pressure` (1–5) with `pressure_cost`, `late_note`, `grimoire=[slug]`.
- Facts file: `docs/lodestar-casebook.md`, created with Vol. 1 (dates, money, numbers, the SOW clauses, cast).
- Landing page: a fifth shelf (`PLANNED_VENDOR`), a future-log line, a `book--vendor-*` cover.
- Same verify routine as `docs/HANDOFF.md` §4.

## 11. Owner's decisions (25 Nov 2026)

1. **Title:** *On the Client's Floor* (subtitle: Notes from the Vendor Side).
2. **Tone:** practical Series 2 notes with dry humour and a visible stress line.
3. **World:** the same MetroVolt as Darkside, with the cast and dates shared.
4. **Size:** six volumes × 15 notes.
5. **Ending:** open, or a cliffhanger. Proposal: the last note ends on Friday 15 June 2029. Wrenfield's phase 2 bid
   and Vexmoor's are both in; Ines is packing up floor 19 when Elaine calls her back for “a quick word, in room 27A”.
   Room 27A is where Darkside's calibration happened. The note ends before she opens the door. Loose threads left open:
   Hana's return, Bert's retirement, and whether Pip moves to the client side.
6. **Narrator and vendor:** Ines Duarte and Wrenfield Digital (not objected to; keep unless the owner says otherwise).
7. **Start:** Vol. 1 (the bid), **but not yet**. First, a sample note for look and feel (section 12).

## 12. Sample note for review (25 Nov 2026)

- Page: `public/samples/on-the-clients-floor/index.html` (hand-made, `noindex`, not linked from the shelf; `build_notes.py`
  doesn't touch it). Skin: `public/assets/vendor.css` (`theme-vendor`), loaded on top of `notebook.css` and `bujo.css`.
- Note: Vol. 1 #6, **What Are We Assuming?** (assumptions, dependencies and exclusions), Thu 11 March 2027.
- Shows every new part: the visitor pass, the timesheet strip (booked vs worked, “billable: 0.0”), both sides of the
  table, the redlined contract clause with a stamp, account health (amber is “Lodestar now”), the pressure gauge,
  vendor ratings (`VENDOR_ATTRS`, drawn by `notebook.js`), Seen in the Grimoire, and the 23:00 note. Titles are
  questions, as in Books 3 and 5.
- Facts it adds (record them in the casebook when Vol. 1 starts): bid day 37 of 42; the clarification meeting on
  11 Mar 2027 on floor 19; Vivian's three-line draft; 41 assumptions (8 in the bid, 33 in appendix C);
  **A1-07** (≤ 5 % of records fail the address check, £9,500 per 1 % above it), tested in December 2027
  (31 %, sets up CR-007); D-03 Halvorsen spec by 30 Jul 2027; X-02 the 02:10 batch excluded; SOW §3.2 “absorb”
  struck after three legal calls (draft v0.3, 9 Jun 2027); Ines meets Pip in the lift (“ask for a sample”).
- Checked: desktop light and dark, 375 px phone width (no horizontal scroll).
- Waiting for the owner's review. When the look is approved, move the skin into `bujo.css` (or keep `vendor.css`
  and add it per journal), add the new fields to the renderer (section 10) and start Vol. 1.

## 13. Vols. 1 and 2 written and built (26 Nov 2026)

Owner asked to start with volumes 1 and 2 after approving the sample. Both are written (30 notes) and on the shelf.

- **Content**: `content/vendor-1/` (`01_reading.py`, `02_shaping.py`, `03_competing.py`, `04_closing.py`) and
  `content/vendor-2/` (`01_paper.py`, `02_arriving.py`, `03_together.py`). Facts: `docs/lodestar-casebook.md` (new, the
  source of truth for Series 5; it adds to Darkside's facts and must not contradict them).
- **Renderer**: `scripts/vendor.py` (`render_note`), called from `build_notes.render_note` when a journal has `vendor=True`.
  Journals `vendor-1`, `vendor-2` in `JOURNALS` (`series=5`, `css=("vendor.css",)`, `VENDOR_ATTRS`, `VENDOR_NOTE` footer).
  `head()` takes extra stylesheets per journal (`css`). Planned vols. 3–6 in `PLANNED_VENDOR`.
- **Note fields** (see the docstring in `scripts/vendor.py`): `date` (a `datetime.date`), `meta`, `where`, `pass_kind`
  (`"contractor"` from 4 Aug 2027), optional `timesheet`, `sides`, `sides_after`, `contract`, `health` (`now` = g/a/r),
  `pressure`, optional `grimoire`, `late`. Sections are numbered automatically: situation · both sides · analogy · how it
  works · contract · account health · pressure · ratings · pitfalls (+ Grimoire aside) · when · quiz, then try it,
  remember, the 23:00 note.
- **Skin**: `public/assets/vendor.css` (the daybook, the pass, timesheet, sides, contract redlines and stamp, health,
  gauge, Grimoire aside, 23:00 note, a contractor badge variant, print rules). Covers `book--vendor-*` in `bujo.css`.
- **Landing page**: a new section `#vendor-side` after the Darkside shelf; a future-log line for vols. 3–6.
- The sample page `public/samples/on-the-clients-floor/` now redirects to `vendor-1/notes/assumptions.html`.
- **Related notes**: Series 5 resolves “(this volume)” and “(vol. N)” within its own book first. Notes in other books
  are named by their real titles (e.g. Sanne's “What Exactly Did We Promise?”).
- **Checked**: every figure as contact sheets (fixed overlaps), 375 px phone width on all 30 notes (no horizontal
  scroll), light and dark, the landing shelf and both indexes, and Vol. 1's PDFs rendered locally (the visitor pass
  gets a print rule so it isn't clipped). `pdf-build.json` lists `vendor-1` and `vendor-2` under `rebuild`.
- **Story so far** (dates in the casebook): bid 3 Feb – 6 May 2027 (won, £380k discovery + £4.62m fixed after BAFO);
  Horizon stalls the signature to 30 June; day one 5 July; laptops day 23; kick-off 13 July; IA-01 with Halvorsen;
  first status amber; baseline v1.0 signed 28 Sep 2027 (pilot 6 Mar 2028, wave 1 24 Jun 2028); A1-07 is risk 1 and
  Vexmoor's assurance calls the migration plan “optimistic”.
- **Next**: Vol. 3 · Digging Up the Legacy (discovery, the 31 %, CR-007). Then the Lodestar file extra (section 9).
