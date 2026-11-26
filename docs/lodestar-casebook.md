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
| Tariq Rahman (he/him) | senior engineer, Leeds | tech lead from 5 Feb 2029 (V-05), after Hana rotates off. |

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

## Vol. 3 · Digging Up the Legacy (Sep 2027 → Feb 2028)

- **MAVIS inventory** (4 Oct): 4.1m lines COBOL, 1,214 programs (449 never ran in 12 months · 498 rarely · 267
  nightly), 386 batch jobs, 412 tables, 84 copybooks; 61 programs touch addresses.
- **Bert's book** (from 14 Oct): questions via Lottie, Bert's hours 10:00–12:00, 64 pages by 10 Dec; successors Lottie,
  Marta, Asif. Bert credited on page 1 of the discovery report.
- **Golden master** (27 Oct): CUSTBL07 (1999), 10,000 accounts; 3 hidden rules: R5 vacant properties, **R7 pro-rata
  standing charge rounds half down** (kept for wave 1, DL-021), R11 Welsh flag (fixed).
- **Change capture spike** (4–15 Oct, note dated 21 Oct): log capture ≈ 40 s for 9 core tables (licence ≈ £85k/yr);
  18 % of tables lack reliable timestamps; snapshots 24 h. An EBCDIC £ sign caught by a test.
- **Halvorsen spec v1.2** (2 Nov): 42 fields (+ address line 4), 6 undocumented behaviours written down (B1: town not
  upper-case → silently dropped), 58 contract tests, version in every file header.
- **The 02:10 job** (9 Nov): 14 steps; step 9 **ADDRFIX** (2003, lookup table from 2011) rewrites Northern postcodes;
  step 12 **COPYMTR** feeds Gareth's meter system (a hidden consumer; Kofi added to IA-01).
- **Data profile** (19 Nov, all 380,000 wave 1 accounts): validity **31 %** fail (117,800); duplicates 4.2 %; meter
  mismatches 2.9 %; missing PSR flags 0.6 %. Opened before 2005: 48 % fail; after 2015: 6 %. The April sample came from
  accounts opened after 2015. Bert hand-checked 30.
- **Strangler plan** (30 Nov): one system-of-record flag per account, a router, a nightly back-feed for 7 MAVIS
  processes, 14-day rollback per wave, nightly reconciliation. Pilot area: **Ashgrove** (20,000 accounts, 340 staff households).
- **Telling order** (8–14 Dec): Bert → Elaine → Priya + Nkem (Priya: “Option B. And I'll tell Rupert myself.”) → Hollis,
  Kofi → steering. **Discovery report D4** on 14 Dec: two front pages, 6 findings, options A/B/C, recommendation B.
- **Security reviews**: requested 6 Oct (week 14, planned week 2); passed 12 Jan 2028; finding S3: PSR flags →
  field-level encryption, 2 roles, access logged.
- **ADR-0019** (19 Jan 2028, DL-028): Hollis chooses **MetroBus** (2014 integration bus, 15-minute polling) over log
  capture; Wrenfield's dissent recorded; +3 weeks; −£85k/yr.
- **Migration plan** (25 Jan): pilot 5 Jun; rehearsals 15 Apr, 15 Jul, 26 Aug; 12 Customer Ops exception-desk staff;
  window Sat 18:00 → Sun 08:00, target 11 h.
- **Design authority** (9 Feb, DL-030): approved with 4 conditions (PSR encryption, MetroBus delay alerts, performance
  test by July, Kofi's sign-off on meter fields). **M2 accepted; £720,000 invoiced.**
- **CR-007**: submitted 14 Dec at £1.1m, +4 months (£247k + £310k + £180k + £363k); agreed **11 Feb 2028 at £700k,
  +3 months** (Customer Ops cleanses ≈ 40 %: −£99k; MetroBus: −£85k; self-service portal → wave 2: −£216k). Rates
  unchanged. **Baseline v2.0** (DL-031): pilot **Mon 5 Jun 2028**, wave 1 night **Sat 23 Sep 2028**.

## Vol. 4 · Delivery Under Fire (Mar → Sep 2028)

- **RAID** (3 Apr): 214 rows → top 12, backlog 161, closed 41; Mondays 09:45, 15 min, with Elaine.
- **Rehearsal 1** (8 Apr): 98.1 % reconciled (R7 missing in the back-feed; fixed by 28 Apr).
- **Status #38** (14 Apr): first RED; four measures (burn-up −2.4 weeks, tests 39 %, reconciliation 98.1 %, 7 sev 1–2);
  overall colour = the worst measure (Schedule 7 Annex B.2).
- **Side-door work** (20 Apr): 23 requests in 6 weeks = 41 days; 9 to the change pool (£58k), 11 to wave 2, 3 declined;
  a front-door form in #lodestar.
- **Environments** (9 May): 31 % of test days lost Mar–Apr; booking calendar, masked 2028 MAVIS copy; 9 % by July.
- **Halvorsen triage** (16 May): 3.1 % rejected; Halvorsen's test system on parser v1.1; fixed 25 May; IA-01 v1.2.
- **Acceleration review** (24 May): Vexmoor asks for source code; terms of reference from Priya; evidence pack;
  supervised walkthrough (background IP, §12); report 21 Jun: “achievable, with risk”. House rule: no comment on Vexmoor.
- **Pilot** live Mon 5 Jun; M3 rejected 23 Jun (exceptions 0.8 % > 0.5 %); accepted **3 Jul** (0.3 %).
- **Steering ambush** (28 Jun): Oliver's “9 weeks behind” (measured against baseline v1.0); real slip 2 weeks; written
  answer 30 Jun; new rule: papers circulated 2 working days before (Schedule 7 §2.7).
- **Plan v2.3** (3 Jul, DL-047): velocity 38 not 45; bulk address edit and MI screen → wave 2; +1 engineer; 9 days of
  buffer shown (4 used by the night).
- **Escalation E-006** (10 Jul): performance environment; pilot servers on 22 and 29 Jul; passed with 18 % headroom.
- **UAT** (from 3 Jul, triage 27 Jul): 412 items → 188 defects, 161 changes (19 to the pool, £41k), 41 duplicates,
  22 not reproducible; Rosa and Oskar triage Mon/Wed/Fri.
- **X-07** (8 Aug): Gareth's ten years of meter history; interim: readable in MAVIS; CR-019 (≈ £140k) for wave 2.
- **Margin** (18 Aug): 19 % at bid → 9 % forecast; levers +£69k → 10 % (floor 15 %); rehearsal 3 kept.
- **Rehearsal 3** (26 Aug): 10 h 40 (target 11 h); runbook v3, 312 steps; point of no return 04:30.
- **Go / no-go** (6 Sep, DL-058): 13 of 14 green; C9 99.97 % (3 accounts); GO with condition (3 accounts excluded);
  Horizon assurance's dissent recorded.
- **Wave 1 night** (Sat 23 → Sun 24 Sep): CP1 23:00 and CP2 02:10 on time; 04:10 MetroBus queue full (back-feed +
  migration) → 22 minutes; CP3 04:52; **live 07:40**; 379,997 accounts; 1,206 exceptions (0.32 %), cleared Sunday 19:10;
  night log at 08:15 (14 lessons). Monday's billing run fine; first bills, no complaints. Hana worked 19 hours.

## Vol. 5 · Other People's Politics (Oct 2028 → Jan 2029)

- **Signals** (Oct): “Ascend readiness” series chaired by Rupert, without Priya; Gareth's team to floor 20; Vexmoor in
  Rupert's lift. Ines briefs Rupert's office through Elaine; never speculates.
- **Sponsor change** (7 Nov 2028): Priya → Rupert; variation V-04, DL-071. Day 1 thank Priya; week 1 a one-page brief;
  week 2 learn what Rupert measures (cost out, Ascend targets, no surprises); baseline v2.0, change pool, phase 2
  timetable re-confirmed in writing.
- **Gareth / meter data**: IA-02, a meter data service owned by Network Assets, signed 30 Nov.
- **Board slide** (30 Nov board): Lord Varnish's title “Lodestar: the Orion foundation delivers”; Ines sends facts
  (379,997 customers, 0.32 %, no billing complaints, MAVIS batch −16 %), credits and “built on lessons from earlier
  programmes”. He keeps the facts.
- **Saying no**: free wave 2 design during hypercare declined; CR-021 readiness sprint £42k, 4–15 Dec; the readiness
  pack given to every bidder.
- **Hypercare** review 21 Nov; **M5 accepted 22 Nov 2028** (warranty starts).
- **Football box** (Dec) declined; thank-you letters instead. **Floor 19**: Vexmoor's Ascend team moves in on 11 Dec;
  floor rules (clean, private, off-site bid work, never poach or fish).
- **Run team**: Asif, Marta, Kemi (MetroVolt); pairs Asif ↔ Bilal, Marta ↔ Hana, Kemi ↔ Oskar. Team agreement v2,
  13 Dec (urgent requests via Ines or Callum; 08:00–19:00 unless severity 1).
- **The lift** (14 Dec): “40 roles in spring”, “phase 2 budget cut?”; not repeated. February announcement: 36 roles,
  phase 2 budget unchanged.
- **The numbers** (16 Jan 2029): Rupert asks Wrenfield to sign “£1.9m a year realised”; realised ≈ £210k a year
  (£1.9m when all waves are done). Refused in his office at 16:20 and in writing at 17:12; reply 19:40 “Use your wording”.
- **Champions**: Elaine, Rosa, Gareth. Elaine declares a relationship; a second marker is assigned.
- **Phase 2 tender** opens 5 Mar 2029.

## Vol. 6 · The Cost and the Ending (Jan → Jun 2029)

- **Hana** (1:1, Wed 10 Jan 2029, room 19C): worked/booked 1.5 since Aug; leave 15–26 Jan; reduced hours 29 Jan–2 Feb;
  **rotates off Lodestar on Mon 5 Feb** to a smaller Leeds client. Key-personnel consent: Elaine, 10 Jan (§6.3);
  variation **V-05** names **Tariq Rahman** (he/him, senior engineer, Leeds) tech lead; Bilal is his backup.
  Hana's 14 handover pages (“ask for help sooner”). Callum also wasn't sleeping.
- **Ines's own limits** (from 22 Jan): ≈ 400 late notes since Feb 2027, times 21:00 → 23:30; 3 hotel nights a week,
  Fridays in Leeds, phone off 21:00 (severity 1 only), notebook closes 22:00. Delegated: Callum (phase 2 commercial),
  Bilal (data estimates), Lottie (lessons session).
- **Pace policy v1** (2 Feb): Lodestar averaged 9.1 h/day worked vs 7.5 booked, ≈ 2,900 unpaid hours (≈ 390 days);
  measure (> 1.15 for 3 weeks → a conversation), cap 45 h, TOIL within a month, recovery weeks, plan at 85 %;
  ≈ +6 % on the phase 2 price (bid §5.4).
- **Walk-away conditions** signed 14 Feb (Ines, Callum, Graham): margin ≥ 15 %; liability capped at contract value;
  never absorb data-quality risk; plan at 85 %.
- **Warranty** 22 Nov 2028 → 20 Feb 2029 (Schedule 9): 37 reports = 14 defects, 15 changes (9 to the pool, £22k; 6 to
  wave 2), 8 not ours. W-29 arrears report 22 s vs < 30 s → change, tuned to 4 s as recorded goodwill (≈ £6k).
  **WC-01** signed by Elaine Fri 23 Feb.
- **Knowledge transfer** (§11.2, Schedule 10): shadow 12–23 Feb, reverse shadow 26 Feb–9 Mar; 11 runbooks by the run
  team; 4 drills (Kemi fixed the bad Halvorsen file in 41 min); certificate signed Fri 9 Mar by Kemi, Marta, Asif,
  countersigned by Hollis. “I'd take the call at three.”
- **Joint lessons** Thu 15 Mar, room 27B, facilitator Lottie; 24 people incl. Sven (Halvorsen) and Bea (Vexmoor);
  Desmond's rules (no phase 2 talk, notes to every bidder); 63 stickies → 5 lessons (L1 Desmond, L2 Sven, L3 Hollis,
  L4 Kemi, from Bea's note, L5 Elaine).
- **Handbook v1.0** Fri 23 Mar: 22 pages; 12 of 74 decisions (DL-001…DL-074, e.g. DL-012, DL-047, DL-062), 9 debts;
  Hollis adopts it as the supplier handover template.
- **Phase 2 bid** submitted Wed 4 Apr 2029, 11:40: waves 2–4, ≈ 1.9 m accounts, 28 months, wave 2 live Jun 2030,
  **£9.4m**, margin 15 %; evaluation 60 % quality / 40 % price; Hana “may rejoin for wave 3; her decision”.
- **Orals** Thu 26 Apr (Wrenfield 10:00, Vexmoor 14:00); decision promised by 15 Jun. Both plans told to the team
  Mon 30 Apr (win: mobilise 2 Jul; lose: 3 months' exit assistance, handover to Vexmoor, nobody redundant).
  May: **Halvorsen wins the billing re-tender**, IA-01 unchanged.
- **Case study** v3 approved Wed 6 Jun by Elaine and Anjali (§18), held until after the award; headline “Lodestar
  wave 1: 379,997 customers, one long night, and what we learned”.
- **BAFO** request Thu 24 May: −12 %, “absorb” data risk, unlimited liability. Fails 3 of 4 conditions. Reply Fri
  1 Jun 10:15: −4 % (business portal → wave 4), shared data-quality pot £400k, cap as wave 1, “we would rather
  withdraw”. Graham: “Send it. I mean it.” Desmond, 4 Jun: “Received. Noted.”
- **Leaving well**: promises 47 of 47 closed by Thu 14 Jun; room 19C cleared (§16.4); 31 thank-you letters.
  **Lottie** is offered a job on Kemi's run team (public advert, §17.2); undecided.
- **Ascend 2030** memo, Tue 12 Jun 2029 (Darkside). Ines's ten rules (13 Jun).
- **Last day** Fri 15 Jun 2029: pass V-0417 (No. 0417, renewed 26 times); kettle to Yusuf, Bert's bound book to Bert,
  plant to Rosa. 17:05 Elaine: “A quick word, in room 27A.” The series ends at 17:09 as Ines knocks.
- **Open, on purpose**: the phase 2 decision; Hana's return; Lottie's choice. Wave 1's contract ends 30 Jun 2029.

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
