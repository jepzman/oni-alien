# Lodestar casebook (Series 5 · On the Client's Floor)

The source of truth for every fact in Series 5. MetroVolt's inside story (people, reorgs, dates) belongs to Series 4,
*The Darkside of the Corporation* (`docs/HANDOFF-darkside.md`); this file adds what the vendor side sees and must not
contradict it. Update it with every volume. Plan: `docs/PLAN-vendor-side.md`.

## The companies

- **MetroVolt Electric Corporation**: the city's electricity distributor. 6,200 staff in **The Grid**, a 31-storey tower.
  2.3 million domestic customer accounts and about 61,000 business accounts. Currency £.
- **MAVIS**: MetroVolt's customer information system, written in-house in **1997**. COBOL on a mainframe, about 4 million
  lines, nightly batch. Feeds billing through a file at **02:10** every night.
- **Halvorsen Systems**: MetroVolt's billing vendor since 2016 (renewed automatically in 2020 and 2024). Account director
  **Sven Aldous** (he/him), brings biscuits.
- **Project Orion**: launched by Lord Varnish in **January 2024** (£3m, 12 months promised; engineers said 24 months,
  £5m). Delivery partner: **Vexmoor Consulting**. Four leads. 18 months late and £2.4m over by November 2026; quietly
  cancelled in **January 2027**. Total spent about £5.4m. Left behind: a half-built “Orion data hub” and the term
  “Golden Customer Record”.
- **Vexmoor Consulting**: a large consultancy (about 40,000 people worldwide). Partner **Oliver Thane** (he/him), analyst
  **Bea** (she/her). From May 2027 Rupert Thorne's advisers on Project Horizon.
- **Wrenfield Digital**: an 80-person consultancy in Leeds, founded by **Graham Wren** in 2011. Revenue about £9m a year;
  Lodestar would add about £5m over 18 months. Largest previous project: Pennine Housing Group's tenancy system (2025).

## Wrenfield's team

| Who | Role | Facts |
| --- | --- | --- |
| **Ines Duarte** (she/her) | lead solution architect, narrator | 15 years in-house at Aldermoor Water; joined Wrenfield in 2025. Keeps a notebook; writes the 23:00 note. |
| Callum Reid (he/him) | engagement manager | plan, budget, status reports; runs the bid. |
| Hana Sato (she/her) | tech lead | Wrenfield's best engineer; a named key person in the contract. |
| Bilal Khan (he/him) | business analyst, data | wrote the data-quality assumption with Ines. |
| Oskar Lind (he/him) | test lead | distrusts every test environment. |
| Lottie Marsh (she/her) | junior engineer | first client project; asks the obvious questions. |
| Vivian Locke (she/her) | account director (sales) | promised Priya “all your customers off MAVIS in twelve months” over dinner on 19 Jan 2027. |
| Graham Wren (he/him) | founder and managing director | needs the deal, then the margin. |

## MetroVolt's people (new in Series 5)

| Who | Role |
| --- | --- |
| Elaine Corbett (she/her) | Lodestar programme director. Orion's last programme manager; survived it. |
| Hollis Wade (he/him) | Head of IT Architecture; chairs the design authority. |
| Desmond Rook (he/him) | procurement lead for Lodestar. Questions in writing only. |
| Anjali Rao (she/her) | MetroVolt legal counsel on the Lodestar contract. |
| Nkem Adebayo (she/her) | finance business partner, Customer Operations. |
| Kofi Asante (he/him) | head of metering, in Gareth Pound's Network Assets. |
| Bert Ogundipe (he/him) | MAVIS's senior COBOL programmer, 31 years at MetroVolt; retires in 2029. |

From Darkside (keep their roles and dates): Priya Nair (she/her, Head of Customer Operations, Lodestar's sponsor;
Director of Customer from Oct 2027), Lord Varnish (Simon, he/him, VP of Synergy, Orion's founder), Rupert Thorne (he/him,
Project Horizon), Gareth Pound (he/him, Network Assets, owns the smart-meter data), Ottoline Grey (she/her, Chief of
Staff), Dame Helena Strand (she/her, CEO), Pip (he/him; joins Priya's Customer Ops as analytics lead on 1 April 2027).

## Vol. 1 · Winning the Work (Feb → May 2027)

- **Wed 3 Feb 2027**: tender for Lodestar published. 96 pages, **212 requirements** (148 must, 64 should). Scoring:
  **quality 60 % / price 40 %** (solution 20, delivery approach 15, legacy and data 10, team 10, social value 5).
  Indicative budget for phase 1: £4m–£6m. Bids due **Wed 24 March, 12:00**. Scope of phase 1: discovery, then
  **wave 1**: move **380,000 domestic accounts** (the Northern district) off MAVIS onto a new customer platform, linked
  to Halvorsen billing. Waves 2–4 (the rest) are phase 2, tendered later.
- Requirements 4.1–4.9 (customer data) reuse Orion's words: “Golden Customer Record”, “the hub”.
- **Wed 17 Feb**: Wrenfield's bid / no-bid. Scorecard 19 / 30 (threshold 18). Vote 6–2; Ines (and Oskar) first against.
  Ines switches with three conditions: paid discovery, Hana named as tech lead, Vivian's twelve months not repeated.
  The bid costs about **110 person-days (≈ £85k)**.
- **Wed 24 Feb**: clarification questions close. **63** questions from all bidders; Wrenfield asked **9**. Answers
  published **Wed 3 March**. Vexmoor's question: “May the supplier reuse the Orion data hub?” Answer: “Bidders may propose
  reuse; no Orion component is mandated.”
- **Tue 2 March**: coffee with Sven Aldous. Halvorsen will support whichever vendor wins with the billing interface, at
  its standard rates (letter of 9 March). Halvorsen is bidding for all of Lodestar itself.
- **Tue 9 March**: solution outline: three options (big-bang replacement, wrap and extend MAVIS, **strangle MAVIS in
  waves**); waves chosen.
- **Thu 11 March**: bidders' meeting on floor 19. Elaine: “Orion's vendor had four assumptions. We paid for every one of
  them.” Pip, in the lift: “ask for a sample. Nobody's looked since 2014.” That night: **41 assumptions**.
- Assumptions (appendix C): **A1-07** no more than 5 % of records fail the address check (sample of 10,000 by 1 April;
  £9,500 per 1 % above 5 %); A1-11 no MAVIS changes during a wave; A2-03 wave 1 = 380,000 domestic accounts; D-03 Halvorsen
  interface spec by 30 July 2027; **D-05** 12 laptops and VPN within 10 working days of start; **D-09** a named MAVIS expert
  three days a week; X-02 rework of the 02:10 batch excluded; X-04 training beyond 40 super-users excluded.
  Eight in the bid, 33 in appendix C.
- **Mon 15 March**: estimate for wave 1, from contract start (discovery included): P50 **11 months**, P80 **14 months**. Reference class:
  Orion (planned 12, cancelled at 36), five UK utility customer-system replacements (14–30 months).
- **Thu 18 March**: commercial model: **£380k time and materials, capped**, for a 14-week discovery; then **£4.8m fixed
  price** for wave 1, paid on five milestones; a rate card for change. Cost to Wrenfield at P50 ≈ £3.4m, at P80 ≈ £3.9m
  (margin 29 % / 19 %). Committed dates: **first 20,000 customers live in month 9, all of wave 1 (380,000) in month 12** after start; effort priced at P80.
- **Mon 22 March**: Vivian, Graham and Ines re-anchor Vivian's dinner promise (“all your customers off MAVIS in twelve months”, repeated by Priya to Lord Varnish): 380,000 in twelve months, the first 20,000 in nine, all 2.3 million in about thirty months, in waves.
- **Wed 24 March, 11:14**: bid submitted (5 bids received in all).
- **Wed 7 April**: Wrenfield, Vexmoor and Halvorsen shortlisted for orals.
- **Wed 21 April**: orals, 90 minutes, room 27B. Panel: Elaine (chair), Priya, Hollis, Nkem, Kofi; Desmond (non-scoring).
  Wrenfield shows a profile of the 10,000-record MAVIS sample (it arrived 1 April): **7.8 %** fail the address check.
  Lord Varnish joins at minute 52 and asks about “synergy with Orion's hub”.
- **Fri 23 April**: reference calls: Pennine Housing Group (Joanne Pryce, she/her, IT director: “they told us about the
  delay in week three”) and Ashby Building Society (mainframe integration, 2024).
- **Wed 28 April**: site visit to Wrenfield in Leeds (Elaine and Hollis). Halvorsen out after orals.
- **Tue 27 April**: best and final offer requested from Wrenfield and Vexmoor: “consider a 10 % reduction”. **Fri 30 April**:
  Wrenfield's BAFO **£4.62m** fixed (−£180k: train-the-trainer instead of 40 super-users, −£120k; warranty 90 → 60 days, −£60k).
  Contingency untouched. Discovery stays £380k.
- **Thu 6 May, 09:00**: MetroVolt all-hands announces **Project Horizon** (Darkside Act V). **11:40**: Wrenfield named
  preferred bidder, “subject to Horizon governance”. Bid-to-delivery handover the next day: **47 promises** in the
  promises register.

## Vol. 2 · Signing and Starting (May → Sep 2027)

- **Mon 10 May – Wed 9 June**: SOW drafting (Desmond, Anjali, Callum, Ines). Draft v0.3 on **9 June**: “absorb” in clause
  3.2 struck after three calls. SOW sections: 1 purpose, 2 scope, 3 assumptions and dependencies, 4 deliverables and
  milestones, 5 acceptance, 6 key personnel, 7 change control, 8 governance, 9 charges and payment, 10 warranty, 11 exit.
- Acceptance (clause 5): test evidence for each milestone; MetroVolt has **10 working days** to accept or reject with
  reasons; silence = deemed acceptance. MetroVolt's first draft said “to MetroVolt's reasonable satisfaction”.
- Change control (clause 7): impact assessment within 10 working days; a **£150k change pool** for changes under £25k,
  approved by Elaine; bigger ones at steering. CR-001 (12 Aug): add MetroVolt's accessibility checker to the pipeline, £8k.
- **Tue 18 May**: Horizon rule: every contract over £1m re-approved by the **Horizon Investment Board**; Vexmoor reviews
  the Lodestar business case. **Tue 22 June**: approved, with a condition: Vexmoor gives “independent assurance” at steering.
- **Fri 21 May**: letter of intent, capped at **£250k**, for mobilisation and discovery preparation, until signature or
  30 June. Wrenfield spends £212k at risk.
- **Wed 30 June**: contract signed. Start **Mon 5 July**.
- **Mon 5 July, day 1**: six on site (Ines, Callum, Hana, Bilal, Oskar, Lottie), room 19C (“the goldfish bowl”), visitor
  passes, escorted to the toilets.
- Access: laptops **day 23 (Tue 27 July)**, VPN Wed 4 Aug, **contractor badges Wed 4 Aug**, MAVIS read access Mon 16 Aug.
  D-05 promised 10 working days. Relief notice RN-01 (30 July): **11 working days**; idle cost ≈ £46k.
- **Tue 13 July**: kick-off, 34 people, the floor 2 auditorium. Lord Varnish opens with the “Lodestar Value Pyramid”.
  Ines walks through the top eight assumptions; “how we disagree” slide.
- Governance: steering monthly (first **Wed 28 July**), chair Priya; members Elaine, Hollis, Nkem, Rupert's delegate,
  Graham, Ines, Callum; Oliver Thane attends as Horizon assurance (no vote). Design authority every other Wednesday,
  chair Hollis. Decision log DL-001 on 28 July.
- **Wed 21 July**: three-firm RACI workshop for the 02:10 file (Sven, Hollis's integration lead, Wrenfield). Interface
  agreement **IA-01** signed 11 Aug.
- Elaine: Thursdays 08:00, café on floor 2. “No surprises” pact on 15 July.
- D-09: Bert is assigned one day a week, not three, until September.
- **Fri 30 July**: first status report: **amber**. First line: “Discovery is 9 working days behind because the team
  cannot log in.” Callum wanted green.
- Team agreement with MetroVolt staff, 9 Aug: MetroVolt's Jira and Confluence, one Teams channel, mixed squads.
- **Tue 28 Sep 2027**: steering signs **baseline v1.0**: charges £5.0m (£380k + £4.62m); discovery ends 10 Dec (was 26 Nov),
  report 14 Dec; pilot (20,000 accounts) live **Mon 6 March 2028**; wave 1 go-live **Sat 24 June 2028**; top-10 risks;
  41 assumptions (A1-07 marked “at risk: sample shows 7.8 %”). Vexmoor's assurance note: “data migration plan optimistic”.

## Later volumes (planned, keep consistent)

Discovery report and CR-007 (14 Dec 2027: +£1.1m, +4 months; agreed Feb 2028 at +£700k, +3 months); the full data
profile shows **31 %** failing the address check; wave 1 go / no-go 6 Sep 2028; cutover night 23 Sep 2028; phase 2 bid
March 2029; the ending in June 2029 (room 27A, a door not yet opened).

## Minor cast and references (Vols. 1–2)

- Yusuf (he/him), MetroVolt IT service desk: chases the laptops; stands up for D-05 at the kick-off.
- Asif (he/him), MetroVolt analyst, data squad · Marta (she/her), MetroVolt engineer, platform squad ·
  Rosa (she/her), MetroVolt tester, testing squad.
- Joanne Pryce (she/her), IT director, Pennine Housing Group (reference) · Tom Hendry (he/him), head of change,
  Ashby Building Society (reference).
- Decision log: DL-001 relief RN-01 (28 Jul) · DL-002 decision map · DL-003 interview list · DL-004 design authority #1 ·
  DL-005 IA-01 signed (11 Aug) · DL-014 baseline v1.0 (28 Sep). Change register: CR-001 accessibility checker £8k
  (12 Aug); CR-002 relief (= RN-01); CN-001 "Golden Customer Record" → "customer record".
- Promises register: 47 lines (P-01 … P-47); P-23 (Ines at the orals, "no change requests for data") corrected with
  Elaine on 9 June; P-38 (Hana "on site every day") clarified as three days.
