# Larder casebook

The running case study for **The Solution Architect's Notebook**. Every note's “situation”, template card
and example uses these facts. Add to this file whenever a note invents something new, and never contradict
it. Book 1 (architect, Ana) and book 2 (product, Grace) run in parallel from October 2025; book 3 (project, Sanne) from
January 2026; book 4 (client, Mo) from March 2026. The public version is the case file page, `public/larder/index.html`,
built from `content/larder/casefile.py`.

## The company

- **Larder** is a grocery delivery start-up founded in 2024 in **Amsterdam**.
- Customers order in the app or on the web; orders are picked in a **dark store** (a small warehouse
  closed to the public) and delivered by **couriers on e-bikes**.
- Two promises: **express** (within 30 minutes) and **slots** (a chosen one-hour window, same or next day).
- Growth plan, agreed with investors in September 2025 (a condition of the Series B):
  **six cities by the end of 2027**: Amsterdam (live), **Rotterdam** (launch 27 April 2026),
  Utrecht, The Hague, Eindhoven and **Antwerp** (Belgium: the first city abroad).

## History

| When | What happened |
| --- | --- |
| Mar 2024 | Femke and Jasper (co-founder, first CTO) found Larder in Amsterdam. Jasper writes Larder Core. |
| Jun 2024 | First dark store, **Noord**, opens: about 300 orders a day. |
| Nov 2024 | Second store, **Zuid**, opens after **5 months** of code changes (everything assumed one store). |
| Apr 2025 | **King's Day**: checkout times out for **40 minutes** at 5× peak. |
| Jul 2025 | 4,000 orders a day. **6 %** of orders end in a refund ticket, mostly substitutions. |
| Aug 2025 | Jasper leaves to start another company. Nobody else knows why Larder Core looks the way it does. |
| Sep 2025 | **Series B** closes, on one condition: **six cities by the end of 2027**. |
| Oct 2025 | **Ana** (solution architect, 6 Oct) and **Grace** (product owner, 13 Oct) join. Series 2 starts here. |

## People

| Name | Role | Cares about |
| --- | --- | --- |
| Femke | CEO and co-founder | the six-city plan, the investors, the brand |
| Marco | CFO | cost per order, cloud bill, cash runway |
| Priya | Head of Product | conversion, the app experience, the roadmap |
| Joost | Head of Operations | dark stores, pickers, couriers, on-time delivery |
| Lena | Legal and data protection officer (DPO) | GDPR, contracts, Belgian rules |
| Sam | Customer support lead | refunds, complaints, the support tool |
| Tomás | Manager, dark store Amsterdam-Noord | pickers, the picker app, stock counts |
| **Ana** | **Solution architect** (joined 6 October 2025; narrator of book 1) | that the platform can grow to six cities without a rewrite |
| **Grace** | **Product owner, ordering & customer app** (joined 13 October 2025; narrator of book 2) | customers getting what they ordered; fears building the wrong thing fast |
| Ben | Tech lead, orders team | |
| Cho | Engineer, payments | |
| Dee | Tech lead, mobile apps | |
| Eli | Platform and operations engineer | |
| Jasper | Co-founder and first CTO (left August 2025) | appears only in old code, old chats and old decisions |
| Sanne | Delivery manager (joins January 2026; narrator of book 3) | the Rotterdam launch: dates, risks, dependencies |
| Mo | Key account manager, Larder for Business (joins March 2026; narrator of book 4) | Korenwolf, the first business client |
| Noor | Product designer, ordering & customer apps (joins 9 February 2026) | the moments customers feel; part of Grace's product trio with Ben |

Grace came from a hotel-booking start-up. She owns the **ordering journey and the customer apps**: basket,
checkout, slots and **substitutions**; her team is Ben's orders team plus Dee's mobile team. She reports to Priya.
Ana and Grace start in the same month, learn Larder from opposite sides, and meet in the same workshops: the
same events appear in both books (Ana's notebook asks “how do we build it?”, Grace's asks “should we, and for whom?”).

Engineering: **14 engineers** in October 2025 (three product teams + platform), hiring to about 22 by 2027.

## Larder for Business and Korenwolf (the client, for book 4)

- **Larder for Business**: weekly restocking of office pantries (fruit, snacks, drinks, coffee), delivered
  07:00–09:00 by van from the dark stores, invoiced monthly. Femke's idea for a second revenue line with
  predictable volume.
- **Korenwolf Group** (fictional): an insurance and pensions company, about **2,400 staff** in three offices
  (Amsterdam HQ, Rotterdam, Utrecht).
  - **Hanna**, Head of Workplace: the sponsor; wants happy staff and no complaints to the board.
  - **Ruben**, procurement: the contract, the price and the service levels; compares Larder with the old caterer.
- Timeline: met at a facilities trade fair (January 2026) → **pilot** at Amsterdam HQ (May 2026) →
  **three-office contract** (September 2026): 98 % complete deliveries, delivered by 09:00, monthly report →
  first hard renewal talk (2027).
- Why it matters for the other books: B2B orders are large, scheduled and invoiced, which stretches the
  ordering model (Grace), the architecture (Ana) and the Rotterdam plan (Sanne).

## Numbers (October 2025, Amsterdam)

- 2 dark stores (Noord, Zuid), about 2,500 products each.
- **4,000 orders a day**; average basket €38.
- Peak: Friday 17:30–19:00, about **1.5 orders/s** and **600 API requests/s** (mostly browsing).
- Campaign days (King's Day, Christmas) reach **5× normal peak**.
- Express on time: **88 %** (target 95 %).
- Cost per order: **€4.10** (target €2.80 by end 2027).
- Six-city target: about **40,000 orders a day** by end 2027.

## Systems (October 2025)

- **Larder Core**: one Django app on PostgreSQL, written by the first two engineers. Shop, orders,
  payments, stock, picking, dispatch and support all live in it, with shared tables everywhere.
- **Customer apps**: iOS and Android (React Native) and a web shop, all calling Larder Core.
- **Picker app**: Android handhelds in the dark stores; needs the store Wi-Fi.
- **StockPilot**: a SaaS warehouse management system (contract runs to **June 2027**); Larder Core syncs
  stock with it every 5 minutes.
- **Payment provider** (an external PSP): cards, iDEAL and Bancontact (needed for Belgium).
- **Courier dispatch**: a cron job in Larder Core that assigns couriers every 30 seconds.
- **Support tool**: a SaaS helpdesk; agents copy order numbers by hand.
- Hosting: one cloud region in the EU (Frankfurt), managed Postgres, no Kafka yet.

## Business drivers (agreed with Femke, Marco and Joost, October 2025)

1. Open a new city in **8 weeks or less** (Amsterdam's second store took 5 months).
2. Reach **95 % express on time**.
3. Cut **cost per order to €2.80**.
4. Stay trusted: no lost orders, no double charges, GDPR-clean, ready for Belgium.

## Requirements and qualities found in Vol. 1

- **ASR 1**: a new city is **configuration, not code**: stores, zones, opening hours, prices, VAT.
- **ASR 2**: the picker app keeps working **30 minutes offline** (Noord's Wi-Fi drops weekly).
- **ASR 3**: checkout p95 **under 800 ms at 5× peak** (King's Day 2025: checkout timed out for 40 minutes).
- **ASR 4**: an order is **never lost or charged twice**, even if a service crashes mid-way.
- **ASR 5**: customer data stays **in the EU**; Belgian invoices follow Belgian VAT rules.
- Constraints: Rotterdam date is fixed (store lease signed); StockPilot stays until June 2027; budget for
  **no more than 4 new hires** in 2026; one cloud region; team skills are Python, Postgres and React Native.
- Assumptions (to check): Rotterdam behaves like Amsterdam; **StockPilot's API can serve six cities**
  (it turned out it **can't**: 10 requests/s per account, found in a spike in November 2025);
  couriers' phones have mobile data all shift.

## Domain (from the event storming, 21 October 2025)

Key events: *Order placed · Payment authorised · Order released to store · Item picked · Item out of stock ·
Substitution offered · Substitution accepted · Order packed · Courier assigned · Order collected ·
Order delivered · Refund issued*. Hot spot: **substitutions** (nobody owned them; support did refunds by hand).

Bounded contexts (Vol. 1, note on bounded contexts): **Catalogue**, **Pricing & Promotions**, **Ordering**,
**Payments**, **Stock**, **Fulfilment** (picking and packing in store), **Dispatch** (couriers and routes),
**Customer Care**. “Order” means a basket in Ordering, a pick list in Fulfilment and a drop in Dispatch.

## First architecture (decided in Vol. 1)

- Keep Larder Core as a **modular monolith**: one module per bounded context, each owning its tables,
  talking through module APIs. Enforced by an import-linter fitness function in CI.
- Extract **Dispatch** as the first separate service (courier locations every 5 s, real-time, different
  scaling).
- **Walking skeleton** for Rotterdam: one test product ordered, paid, picked and delivered end to end in
  a test store “RTM-0” by 15 January 2026.
- Risk-storming (December 2025) top risks: StockPilot rate limit, Rotterdam date, single Postgres at 5×
  peak, payment provider outage at peak, the dispatch cron job.

## ADR log

| No. | Title | Date | Status |
| --- | --- | --- | --- |
| 0001 | Record architecture decisions | 2025-10-20 | Accepted |
| 0002 | Modular monolith; extract Dispatch first | 2025-12-08 | Accepted |
| 0003 | A city is configuration, not code | 2025-12-15 | Accepted |
| 0004 | Picker app is offline-first | 2026-01-12 | Accepted |
| 0005 | Cache StockPilot stock per store, sync by events | 2026-01-26 | Accepted |
| 0006 | Introduce one managed Kafka cluster | 2026-02-23 | Accepted |
| 0007 | Send orders to delivery via a transactional outbox | 2026-03-14 | Accepted |
| 0008 | Dispatch as a service: Ordering publishes events, no sync calls (from RFC-003) | 2026-03-27 | Accepted |
| 0009 | Second payment provider for cards + iDEAL, manual switch-over, live by 1 Sep 2026 (~€900/month) | 2026-04-02 | Accepted |
| 0010 | Run Dispatch on the managed container service | 2026-04-08 | Accepted |
| 0011 | Run the Korenwolf pilot on manual standing orders | 2026-04-15 | Superseded by 0014 |
| 0012 | Routing Engine A (open source, self-hosted) for Dispatch | 2026-05-26 | Accepted (on watch, Sep 2026) |
| 0013 | Buy a billing service for Larder for Business invoices | 2026-06-08 | Accepted |
| 0014 | Scheduled orders on business accounts, in Ordering | 2026-10-05 | Accepted (proposed 21 Sep) |
| 0015 | Vans are a courier type in Dispatch (routes planned the evening before by Engine A) | 2026-11-02 | Accepted |
| 0016 | Move warehouse management from StockPilot to WMS B by Sep 2027, store by store | 2026-12-15 | Accepted |
| 0017 | Protect the critical windows (Friday 17:00–20:00, business 07:00–09:00) instead of a second region | 2027-01-12 | Accepted |
| 0018 | Integrate WMS B with a style per need (webhooks, API, nightly file) behind the Stock adapter | 2027-03-08 | Accepted |
| 0019 | Business API, contract first (OpenAPI), /business/v1 | 2027-03-15 | Accepted (live May 2027) |
| 0020 | Events are owned, registered contracts; compatible changes only, CI checks | 2027-04-19 | Accepted |
| 0021 | One identity per person (SSO, SCIM); federate with business clients | 2027-05-24 | Accepted |
| 0022 | One backend for each kind of client (mobile BFF, portal BFF) | 2027-06-07 | Accepted |
| 0023 | No canonical order model; a small published language instead | 2027-07-05 | Accepted |
| 0024 | One master and one owner per kind of data | 2027-08-02 | Accepted |
| 0025 | Billing off the ordering path: orders accepted, invoice lines queued | 2027-12-06 | Accepted |
| 0026 | One region (three zones), pilot light in a second region, with four triggers (revisits 0017) | 2028-01-24 | Accepted |

## Book 2, Vol. 1: Grace's facts (October 2025 → January 2026)

- **Interviews** (14–24 Oct): 12 customers (6 express, 4 slots, 2 lapsed). Pattern: they don't mind substitutes, they
  mind not being asked (12/12); they find out at the door (10/12); allergies make some swaps unsafe (4/12). “Rik”, 38,
  two kids, one with a dairy allergy: “I don't mind a swap. I mind finding out on the doormat.”
- **Jobs**: J1 express “dinner tonight” (~70 % of orders); J2 slots “the week's shop” (~30 %); J3 emerging “the office
  pantry” (2 of 12 interviews).
- **Proto-personas**: the tonight-dinner parent (6 interviews, high), the Sunday planner (4, medium), the office stocker (2, low).
- **Journey**: express order 17:20 → item out of stock 17:31 → swap without asking 17:33 → door 17:48. Moment of truth: 17:31.
- **Problem statement** (7 Nov) and **outcome**: substitution refund tickets 6 % → 2 % of orders by end Q2 2026; costs
  ≈ €45,000/month; customers with 2+ refund tickets order 30 % less the next month.
- **Opportunity tree** (10 Nov): O1 “let me say yes or no” (chosen solution: approve in app, 2-minute window),
  O2 “tell me before the courier”, O3 “never swap this”, O4 “it should be in stock” (Ana's StockPilot cache).
  Parked: ML recipe ideas (Femke, an investor's suggestion); faster picking screen (Joost's roadmap).
- **North star** (19 Nov): perfect orders per week (complete or accepted swap, on time, no ticket within 7 days):
  ≈ 23,000/week = 82 % (express 79 %, slots 88 %). Inputs: orders/week 28,000; % complete 91 %; % on time 88 %; % no refund 94 %.
- **Baseline** (26 Nov): 400 tickets re-tagged: 6.2 % of October's 124,000 orders (express 7.4 %, slots 3.5 %;
  Noord 6.5 %, Zuid 5.9 %); the helpdesk tag was wrong 38 % of the time. New tag rule live 1 Dec.
- **Fake door** (3–17 Dec): “Larder for your office?”: 21,000 sessions, 140 clicks (0.67 %), 38 left details,
  9 offices with 40+ staff. Femke takes the numbers to the January trade fair (where she meets Korenwolf).
- **Concierge test** (Noord, 8–19 Dec, 17:00–20:00): 412 swaps on 1,960 express orders; 81 % answered < 2 min,
  74 % accepted, 15 % chose no swap, 11 % no answer; swap refund tickets 1.1 % (Zuid 6.8 %); picking +40 s. ≈ 60 agent-hours.
- **Prototype test** (13–22 Jan 2026): 6 customers, 3 pickers. Fixes: big countdown, price difference shown,
  glove-friendly buttons, pickers continue (answer applied at packing), inline “never swap this”.

## Book 1, Vol. 2: Ana's facts (March → September 2026)

- **Decision log** (`docs/decisions/README.md`, 16 Mar): Sanne asks what's still open for Rotterdam; 7 ADRs plus
  19 decisions in chat (11), tickets (5) and meeting notes (3); 6 open with no owner. Reviewed Mondays by Ana and Sanne.
  Lines used: D-19 opening hours (config), D-21 Dispatch (RFC-003), D-22 second PSP, D-24 substitution window (2 min, a
  flag, Grace decided), D-26 where Dispatch runs, D-27 Korenwolf pilot, D-29 picker log library.
- **RFC-003 Dispatch as a service** (Eli + Ben, reviewers Ana, Cho, Sanne; comments 18–25 Mar; accepted 27 Mar → ADR 0008).
  Ben had pictured HTTP calls, Eli events; two weeks of code didn't fit. Rollout: RTM-0 → Rotterdam → Amsterdam the week after.
- **D-22 second PSP** (DACI, 23 Mar): Driver Cho, Approver Marco, Contributors Ana, Lena (veto on data terms), Sam, Joost;
  Informed Femke, Priya, tech leads. Stuck 3 weeks / 4 meetings, decided in 8 days (2 Apr). A 4-hour outage ≈ €60k lost orders.
  Standing decision rights (2026 Q2): inside one module → team; across modules / ADR → Ana + tech leads; > €1,000/month →
  Marco; personal data, contracts → Lena can veto; city launch dates → Femke.
- **Trade-off sliders** for Rotterdam (31 Mar; Femke, Joost, Priya, Sanne, Ana, Grace): launch date 5 (lease) > orders safe,
  paid once 4 > city as configuration 3 (hard-coding allowed if logged as debt) > feature scope 2 (substitution approvals:
  Amsterdam first, Rotterdam in June) > internal tool polish 1. Review the week of 11 May.
- **Doors** (9 Apr): 31 decisions queued for Ana's Thursday meeting (about 8 a week, 2 weeks deep); 24 two-way back to
  teams, 7 one-way.
- **Korenwolf pilot** (options analysis 13 Apr, ADR 0011): weekly pantry restock at Amsterdam HQ, 07:00–09:00 by van from store **Zuid**, from **4 May**, 12 weeks; support enters one standing order a week (~3 h/week);
  Mo's spreadsheet invoices. Scores: by hand 74, flag 56, scheduled orders 68, new service 48.
- **Rotterdam's internet line** was ordered 30 Mar with a 6-week lead time; live mid-May. The store opened on a 4G router
  with the offline-first picker app (ADR 0004).
- **Antwerp planning date: September 2027** (not committed, as of 20 Apr 2026). Decision calendar: store lease by Dec 2026
  (Femke), Belgian invoices/VAT by Mar 2027 (Marco), French and Dutch in the apps by May 2027 (Grace; all text translatable
  from now on), courier contracts by May 2027 (Joost), Bancontact by Jul 2027 (Cho).
- **Dispatch hosting** (ADR 0010): ~60 location messages/s from 300 courier phones (every 5 s), always on 07:00–23:00.
  Larder Core runs on virtual machines Eli patches by hand. Revisit when more than 5 services (3 in Sep 2026).
- **After Rotterdam opened**: express on time 89 % Amsterdam, 84 % Rotterdam (May). Dispatch still ran the 30-second loop.
- **Routing evaluation** (11–22 May, owner Eli): 7 → 4 → 3; bake-off replayed Fri 8 May, Amsterdam, 17:00–19:30, scaled to
  300 couriers. Engine A 1.4 s / 93 % / easy to run / €300; Engine B 0.9 s / 94 % / weak / €300; Service C 1.1 s / 93 % /
  €4,800 a month at six cities. Engine A chosen (ADR 0012); Service C is plan B. Engines are kept anonymous on purpose.
- **Business billing** (ADR 0013, 8 Jun): May's Korenwolf invoice took Mo and Marco 6 hours with 2 VAT errors (pantry goods
  9 %, coffee-machine rental 21 %). Ruben wants invoices per office and cost centre. 3-year cost: build ≈ €112k, buy ≈ €34k
  (€600/month), open source ≈ €59k. Larder keeps "what was delivered"; the billing SaaS owns invoices, VAT, reminders, Peppol.
- **Engineers**: 14 → 18 in Q2 2026 (four hires, the 2026 budget). First **tech radar** 22 Jun 2026 (14 blips; refresh Dec 2026).
- **Technical debt register** (15 Jun): TD-1 three Rotterdam settings hard-coded (before Utrecht prep, Oct); TD-2 Korenwolf
  by hand (~12 h/month); TD-3 Dispatch 30-s loop (July, Engine A); TD-4 outbox polls 2 s (left on purpose); TD-5 picker sync
  conflicts by hand (~12/week at Noord, July); TD-6 four allowed cross-module reads (before any Payments split). 20 % of each sprint.
- **StockPilot** letter (Jul 2026): from the Jul 2027 renewal, pricing per store, ≈ 3× today for 12 stores. Contract ends
  30 Jun 2027, 6 months' notice → decide by 31 Dec 2026. Exit options: WMS B (~3 months' work, 5 months' lead, ≈ 1.4×) or
  Larder's own stock service (~6 months). Marco goes into the autumn renewal talks with a costed alternative (outcome open).
- **Decision review** (21 Sep 2026): peak 2.6 orders/s across two cities; stock mismatch 0.4 %; 3 services; on time
  Amsterdam 93 %, Rotterdam 91 % → ADR 0012 on watch (re-check 19 Oct); Korenwolf signed for three offices → ADR 0014 proposed.

## Book 2, Vol. 2: Grace's facts (January → April 2026)

- **Strategy on a page** (drafted 19 Jan, agreed with Priya 26 Jan): serve tonight-dinner parents and Sunday planners
  (offices later); win with honest substitutions and on-time delivery; three bets for 2026: approvals in the app
  (2-minute window), the "no swaps" flag per item, live order updates; not this year: recipe ideas, meal kits, non-food;
  we'll know by: perfect orders 82 % → 88 % by December 2026, substitution refund tickets 6.2 % → 2 %.
- **RICE** (2 Feb, per quarter; 28,000 orders/week × 13 = 364,000; 21 % have a swap = 76,000): approvals 15,200;
  faster picking screen 9,100 (another outcome → Joost); "no swaps" flag 7,500; live order update 4,750; auto-refund
  button 3,000; recipe ideas 1,500. 23 idea cards on the Q2 wall.
- **Roadmap** (6 Feb): the 2025 Gantt chart (14 features, 9 late) replaced by now / next / later; updated monthly.
- **Sizing Larder for Business** (9 Feb): ~1,500 offices of 50+ staff in Amsterdam and Rotterdam zones × ~120 staff ×
  €5 pantry per person per week × 48 weeks ≈ €43M a year; 2 % by end 2027 = 30 offices ≈ €0.9M; Korenwolf alone ≈ €0.6M;
  consumer orders ≈ €55M a year. Femke's report: office catering NL ≈ €50M. Decision: a pilot, not a team.
- **Cost of delay** (9 Feb): flag ≈ €12k/month, 0.5 month, CD3 24; approvals ≈ €30k/month, 2 months, CD3 15; live
  update ≈ €6k/month, 1 month, CD3 6. Rotterdam app work: fixed date, done by 20 Apr. **Flag live 23 Feb.**
- **Business case** (approved 12 Feb by Priya, Marco consulted): build 8 person-weeks × €6k ≈ €48k; running ≈ 10 s extra
  picking per swap order × ~25k a month ≈ €1.8k/month; benefit ≈ €30k/month; payback ≈ 2 months. Web orders ≈ 20 %.
- **Kano survey** (16–20 Feb, in-app, 212 answers): approvals performance 48 %; flag must-be 41 % (74 % among 38 allergy
  households); live order update attractive 39 %; recipe ideas indifferent 62 %.
- **Saying no** (board 24 Feb; message to Femke 25 Feb): recipe ideas parked; small yes: 3 recipe links in the weekly
  newsletter for 4 weeks; result late March: 2.1 % clicked, 0.3 % added an item → stays parked; review July (Q3 planning).
- **Request triage** (from 2 Mar; Mondays 10:00, 30 min, with Ben and Dee): 47 backlog requests → 9 joined an
  opportunity, 6 quick fixes (Tomás's picker font size, shipped 4 Mar), 21 parked, 11 declined. Sam's auto-refund
  button parked (review 1 Jun).
- **Rotterdam app scope** (MoSCoW, 3 Mar, with Sanne, Joost, Priya): 19 items, 14 Musts → 6 Musts (zones and slots,
  prices and VAT, opening hours, iDEAL and cards, order tracking, store in the app); approvals in Rotterdam a Should.
- **Release plan** (Sanne with Grace, 9 Mar): R1 staff test at Noord 30 Mar (90 %); R2 all Amsterdam express behind a
  flag 13 Apr (80 %); R3 Rotterdam June (moved from 27 Apr after the trade-off sliders on 31 Mar). Sanne had told Joost
  approvals would be in Rotterdam at launch (a misread); corrected 9 Mar.
- **Business banner test** (10–17 Mar, 10 % of app users): order conversion 9.5 % without, 9.1 % with the banner;
  3 leads. Moved to the account menu and newsletter; leads to Mo (18 Mar).
- **Outcome roadmap** for the board (23 Mar): now: refund tickets 6.2 % → 4 % by end June; next: "where is my order?"
  tickets −30 % by end September; later: 3 offices ordering without phoning Mo.
- **Opportunity cost** (25 Mar): Mo asks for office ordering in the app (~4 weeks of Ben's team); it would push
  approvals to mid-May (≈ €30k) and remove Rotterdam's slack. Cheaper yes: the pilot by hand → Ana's options analysis.
- **Approvals live in Amsterdam on 13 April** (R2). First three days: 79 % answered within two minutes.
- **Bets, not promises** (board 16 Apr): approvals (high confidence) 6.2 % → ~3.5 % by end June; flag (medium) ≈ −0.5
  point, signal: used on ≥ 8 % of orders; live updates (low), Q3. Message: 3–4 % by June, 2 % by December. (The November
  target of 2 % by end Q2 is now not expected.)

## Book 1, Vol. 3: Ana's facts (October 2026 → February 2027)

- **Team**: 18 engineers (four hired in 2026); Ana is still the only architect. Tech leads: Ben (orders), Cho
  (payments), Dee (mobile), Eli (platform).
- **Diagrams** (6 Oct): eleven inconsistent wiki diagrams (one still showed Dispatch inside Core) replaced by four C4
  diagrams. Containers: customer apps, picker app, Larder Core, Dispatch (+ Engine A), managed Postgres, managed Kafka;
  external: StockPilot, PSP ×2, billing service, helpdesk.
- **Views** (13 Oct): logical, process, development, physical and a data view for Lena; scenarios S1 express order with a
  swap, S2 Korenwolf's standing order, S3 Noord's Wi-Fi drops.
- **Vans** (whiteboard 13 Oct failed, 20 Oct worked): vans become a courier type in Dispatch, capacity in crates, windows
  07:00–09:00, routes planned the evening before (ADR 0015, Eli).
- **Standing-order bug** (Oct): billing lines were created on "placed"; Korenwolf was invoiced for 3 items never delivered
  (credit notes, Ruben's first complaint). Fixed: billing listens for order.delivered.
- **Incident 29 Oct**: a network rule change cut Dispatch off from Postgres for 25 minutes; couriers assigned by hand.
  Deployment: EU region (Frankfurt), one private network; Dispatch (2–6 copies) and Engine A on managed containers;
  Larder Core on 3 VMs; managed Postgres primary + replica; managed Kafka, 3 brokers; stores on Wi-Fi + 4G backup via VPN.
- **Numbers, November 2026**: ~5,800 orders a day; peak 2.6 orders/s; express on time 94 % Amsterdam, 92 % Rotterdam;
  cost per order €3.60.
- **Docs**: one-pager (10 Nov), arc42 skeleton in docs/architecture/ (17 Nov), docs as code with Structurizr DSL and
  Mermaid (24 Nov).
- **Korenwolf three offices** (contract Sep 2026): service from January 2027. Korenwolf IT's solution design document
  (40-section template) answered in 14 pages, approved 18 Dec. Data held: office managers' names and emails, office
  addresses, order history; no staff data. SSO for office managers. The Utrecht office is served by van from Zuid until
  Larder's Utrecht store opens.
- **Warehouse decision** (2 Dec presentation failed; 9 Dec approved): renew StockPilot ≈ €252k a year (today ≈ €84k);
  WMS B ≈ €118k a year + ≈ €90k migration; own stock service ≈ €60k a year + ≈ €300k. Choice: WMS B, store by store;
  Marco agreed a 3-month bridge with StockPilot (to Sep 2027) at today's price (ADR 0016).
- **Christmas peak**: 18 Dec 2026, 18:05, a database failover took checkout down for 38 minutes (≈ 900 orders lost or
  late). Femke asked for 99.99 %; option B chosen on 12 Jan (≈ €1,500 a month, six weeks; failover under 2 minutes, no
  changes in the critical windows, business orders picked the evening before; ADR 0017). Second region: ≈ €9,000 a month
  + 2 engineers, revisit at Antwerp.
- **Katas**: monthly from 19 Jan 2027; the first brief was Larder in Antwerp.
- **Living diagrams** (26 Jan): first run found a direct HTTP call Customer Care → Dispatch (added Dec) and two unused topics.
- **Planning dates for 2027** (not commitments, 2 Feb): Utrecht April, The Hague June, Antwerp September, Eindhoven
  November. Transition states T1–T3 in docs/architecture/roadmap-2027.md; T3 = load-tested for 40,000 orders a day.
- **Korenwolf January report**: 96.1 % "complete deliveries" counted per crate; per the contract (everything for one
  office on one morning) it was 98.6 %. Glossary written 9 Feb (arc42 section 12).

## Book 2, Vol. 3: Grace's facts (February → June 2026)

- **Noor**, product designer, joins on 9 February 2026. Product trio: Grace (value), Noor (usability), Ben (feasibility):
  a customer interview together every Thursday 16:00, Noord every other Tuesday at peak, the tree on Fridays.
- **Story map** (16 Feb): the approvals backlog had 41 tickets; backbone: item runs out → picker picks a swap →
  customer told → customer decides → picker packs → customer receives; nine new cards found. Rewritten to 17 stories (18 Feb).
- **Slices** (23 Feb): 1 express, one swap, Noord staff (R1, 30 Mar); 2 all Amsterdam express, up to three swaps, price
  difference, answer applied at packing (R2, 13 Apr); 3 slot orders, "never swap" inline (May); 4 Rotterdam and the web
  shop (June). Slice 1 taught that pickers waiting for answers slowed packing (Ben saw it on a store visit).
- **Example map EM-03** (25 Feb): R1 2 minutes to answer; R2 no answer → keep the substitute, unless the customer's
  setting says "refund me if I don't answer"; R3 more than €2 extra → must answer; R4 a flagged allergen → never default.
- **MVP vs MLP** (2 Mar): lovable swap screen (photo, price difference, big countdown) and glove-sized picker buttons;
  viable support table, reports and settings.
- **Definitions of ready and done** (4 Mar), **refinement rhythm** (from 23 Mar: Monday pre-read, three-amigos sessions,
  45-minute Thursday; 18 → ~8 person-hours a week, 2 → 6–8 stories ready), **sprint 7 goal** (16–27 Mar).
- **Pre-mortem** (16 Mar): 37 % of app users have notifications switched off → in-app banner + default when there's no
  answer; answers applied at packing; allergen warning; clearer price wording ("€0.40 more than ordered").
- **Zuid's opening day** (Nov 2024): 340 products without a price, support heard from customers, a push to the wrong area.
- **Rotterdam launch checklist** (from 30 Mar; go / no-go 24 Apr): eight areas with owners; two reds (Saturday slot
  capacity, Dutch help pages) fixed by 26 Apr. Waitlist push to 4,100 people on launch morning. Grace and Ben at the store.
- **Approvals rollout, Amsterdam**: dark (picker side) from 6 Apr; 10 % on 13 Apr, 25 % on 15 Apr, 50 % on 17 Apr,
  100 % on 20 Apr. Guardrails: picking +≤15 s per swap order, answers ≥70 % in 2 min, crash-free ≥99.5 %. Friday 17 Apr:
  Zuid picking +18 s → hold; handheld lag fixed. First week of approvals: 140 support tickets (6.1 per 1,000 approvals).
- **Rotterdam hypercare** (27 Apr–11 May, daily 09:00): orders 310 → 540 a day in week 1; on time 82–86 %; tickets per
  100 orders 7.1 → 2.6. Fixed: three streets missing from zone RTM-2, Saturday slots full by Thursday, an iDEAL error for
  one bank. Exit: tickets < 3 per 100 for two days and no P1 for five days.
- **Tech-debt deal** (8 Jun, Grace and Ben): 20 % of every sprint, ordered by product impact, each item reported with a
  product number. Picker sync conflicts (12/week at Noord) cause wrong swaps packed.
- **Approvals in Rotterdam** (8 Jun): email the day before, intro card on the first swap, "What's new", Sam's macros, a
  briefing for Rotterdam's pickers. First week: 1.4 tickets per 1,000 approvals.

## Book 2, Vol. 4: Grace's facts (May → October 2026)

- **Tracking plan** (4 May, Grace and Dee): four approval events (offered, seen, answered, applied) with the same names on
  iOS, Android and web; "tracking events firing as in the plan" joins the definition of done. Real answer rate in May: 77 %.
- **Swap funnel** (18 May): offered 100 → seen 88 → opened 82 → answered 77 → applied 76. The drop was seen → opened on
  Android (71 % vs iOS 96 %): Android grouped Larder's notifications. Fixed 1 June; answers rose to 82 %.
- **Ticket review** (from 15 Jun, Mondays, Grace and Sam, per 1,000 orders): where is my order 11.2, missing item 6.4,
  late delivery 4.1, swap refund 3.4 (was 6.2), damaged 2.0; contact rate 31 per 1,000 (38 in April). Sam's auto-refund
  button (R-22) closed. Swap refund tickets as % of orders: April 5.1 %, May 4.0 %, June 3.4 %.
- **3-minute window test** (sample size set 15 Jun; ran 22 Jun–6 Jul, Amsterdam): ~1,300 swaps per group, two full weeks.
  Answered 82 % (2 min) vs 88 % (3 min), +6 points (95 % interval +3.8 to +8.2); picking +7 s vs +11 s. Day-three lead
  was 9 points. Shipped 13 Jul.
- **Board slide** (22 Jun): vanity totals (120,000 swaps approved, 180,000 downloads) replaced by swap refunds per 100 orders,
  answered share (82 %) and repeat ordering 8 weeks after a swap (71 %).
- **Q3 OKRs** (set 29 Jun, graded 30 Sep): O "Every customer trusts their order"; KR1 swap refund tickets 3.4 → 2.5 %
  (2.7 %, 0.8); KR2 "where is my order?" −30 % (−31 %, 1.0); KR3 perfect orders 84 → 86 % (85.5 %, 0.75). Slot reminders
  and the payment screen migration dropped.
- **Cohorts** (6 Jul): still ordering 8 weeks after the first swap: refund ticket 58 %, approved swap 71 %, no swap 69 %.
- **Approvals post-launch review** (6 Jul): outcomes as expected (3.4 %, 82 %, +7 s, ≈ €28k a month); effort 11
  person-weeks, not 8 → +30 % buffer for work touching iOS, Android and web.
- **Ordering health page** (13 Jul): north star, four inputs, three guardrails; Mondays 15 min with Priya; twelve
  dashboards archived.
- **Operations feedback loop** (from 20 Jul): idea button on the handhelds, fortnightly 20 min at Noord and Rotterdam,
  "you said, we did" board. 14 items in three weeks; suggestions sorted by similarity (shipped 3 Aug): swaps accepted
  71 % → 78 %. Tomás: "first time anyone wrote back".
- **Live order updates**: round 1 tripped the opt-out guardrail (24 Aug) and wasn't shipped; Noor's redesign (two pushes
  plus an in-app timeline) cut "where is my order?" tickets 31 % with opt-outs +0.2 points. Shipped 21 Sep.
- **Customer advisory panel** (first session 21 Sep): 12 customers (4 dinner parents, 3 Sunday planners, 2 allergy
  households, 2 office managers, 1 lapsed; Amsterdam 8, Rotterdam 4), quarterly 90 min, €25 voucher, a third rotate yearly.
- **Slot waitlist** (built for Rotterdam, June): 1.1 % use, 9 % of those ordered, two bugs, ≈ 2 engineer-days a month.
  Sunset agreed 21 Sep with Priya and Sam; top 12 users offered email slot alerts; switched off 5 Oct, code and data
  deleted by 9 Oct.

## Book 2, Vol. 5: Grace's facts (October 2026 → March 2027)

- **Weekly update** (from 5 Oct, Fridays 16:00): outcomes, shipped (≤ 3 lines), learned, next, asks with names and
  dates. Readers 6 → 24 of 31 in six weeks.
- **One-page PRD** for business standing orders (12 Oct): in for 4 Jan = weekly standing order per office, cost centre
  per invoice line, skip a week; out = self-service editing (spring), API, custom invoice layout. Ruben's 14-page
  requirements became an appendix.
- **Managing up** (19 Oct): shared 1:1 doc with Priya (decisions needed, risks, decisions made, wins); "no surprises".
- **Demo at Noord, 06:00** (2 Nov): Tomás found the van loading list in picking order; fixed 9 Nov.
- **Live timeline privacy** (9–16 Nov, with Lena): courier first name or nickname; map only in the last 10 minutes;
  nothing kept after delivery; couriers told first. Launched on the web on time. Monthly privacy office hour.
- **Dependency board** (from 16 Nov): billing lines (Cho, done 4 Dec), van routes (Eli, slipped 7 → 14 Dec), picking
  from 06:00 (Joost), SSO for office managers (Eli, 18 Dec); cost-centre form removed (built in Ordering).
- **Korenwolf scope** (23 Nov, signed 26 Nov, with Hanna and Ruben): five things for 4 Jan; portal in spring; no
  custom invoice layout. Changes by email to Mo before 08:00 until the portal.
- **Order-editing pitch** (30 Nov): 8 % of express customers place a second order within 30 min (≈ 4,900 a month,
  ≈ €4.50 each ≈ €22k a month). Femke: yes to a test (Amsterdam, February; window closes before release to store).
- **Fixed date** (plan 1 Dec): cut line; above done 11 Dec; Larder's own office orders from 14 Dec; the 18 Dec outage
  cost two days of testing; **Korenwolf live 4 Jan 2027**; first week 98.6 % complete by 09:00.
- **Bad news** (7 Dec forecast ≈ 2.4 % vs the 2 % promised for December): Priya told 7 Dec, Femke 8 Dec, board 14 Dec
  given 2.3–2.5 % and a plan. 63 % of remaining swap refunds were Rotterdam slot orders (41 % notifications off there).
  December ended at 2.4 %; in-app banner + SMS fallback → **2.0 % in March 2027**.
- **Q4 review** (11 Jan, 45 min, two-page pre-read): Q1 bets agreed, editing test confirmed, 2.0 % moved to March.
  Perfect orders 86.1 % in December.
- **Grace ↔ Ana** weekly, Tuesdays 14:00, from 12 Jan (after ADR 0017 clashed with the editing test plan).
- **Picker app as a product** (from 18 Jan, with Joost): 20 % of Dee's team; Tomás as rep. By 31 Mar: wrong swaps
  packed 12 → 1 a week; picking per order 6:40 → 6:05; wrong items 4.2 → 1.8 per 1,000.
- **Account requests** (22 Feb, monthly with Mo): 17 Korenwolf requests → 5 built as settings for all business
  accounts (cost-centre split, approval threshold, delivery photos…), 4 by process, 8 declined.
- **Larder Plus** (Grace's case 22 Feb; Femke decided 1 Mar 2027): free delivery for €7.99/month, launch June 2027;
  Antwerp French release in May. Measures: Plus members order ≥ 30 % more often; 5,000 members by 1 Sep 2027 (check-in).

## Book 1, Vol. 4: Ana's facts (March → September 2027)

- **Capability map** (1 Mar): seven areas; red for 2027: city setup, languages (FR, NL), Belgian rules; yellow: stock,
  vans, business self-service, data.
- **WMS B integration** (ADR 0018): webhooks → stock.changed (< 1 min), API for pick lists and goods received, nightly
  file by 06:00 for finance; database view rejected. Rate limit 20 req/s (Larder queues at 15).
- **Business API** (ADR 0019): contract first (/business/v1, standing orders, cost centres, delivery windows), reviewed
  with Korenwolf's IT and Mo, mock server, live in May 2027. Korenwolf orders from its facilities system; two more office
  clients use it by June. v1 + optional lines[].cost_centre (Jun); v2 with deliveries[] per office ships September;
  v1 runs 12 months after v2, 6 months' notice, Sunset header.
- **Anti-corruption layer** (22 Mar): WMS B article → product, bin → store location, wave → pick batch, units → items;
  fitness function FF-07 keeps the WMS B client inside the Stock adapter.
- **Strangler migration** (plan 29 Mar): router per store; shadow week (≤ 0.5 % diff) → switch → two weeks StockPilot
  read-only. Zuid 19 Apr, Noord 24 May, The Hague opened on WMS B 14 Jun, Rotterdam 21 Jun, Utrecht 26 Jul;
  StockPilot off 15 Sep 2027 (bridge contract ended 30 Sep). **Utrecht opened 12 Apr 2027** (on StockPilot);
  **The Hague opened 14 Jun 2027**.
- **Events** (ADR 0020, 19 Apr): order.placed's field store renamed to store_id broke billing silently for two days
  (9 consumers). Schema registry, catalogue, compatible changes only; order.placed v2, v1 removed 19 Jul.
- **Settlement files** (10 May): two providers' daily files by 05:00, checksum + trailer, loaded once, alert at 07:00,
  mismatch report for finance (one file had been counted twice in April, one noticed a week late in May).
- **Identity** (ADR 0021, 24 May): 14 staff tools; a support leaver kept helpdesk and billing access 3 weeks (Lena's
  review). One IdP, SSO, SCIM for 11 tools; federation with business clients; personal picker badges by July.
- **BFFs** (ADR 0022, 7 Jun): business portal for office managers since May; order screen 7 calls / 2.8 s → 1 / 0.6 s.
- **No canonical model** (ADR 0023, 5 Jul): published language = order.placed, stock.changed, delivery.completed.
- **Application portfolio** (19 Jul): 23 applications ≈ €61k a month; eliminate survey tool, second chat tool, old
  cron, legacy reporting DB (≈ €2.3k a month); migrate StockPilot and Mo's spreadsheet CRM (to a CRM by Dec).
- **Data ownership** (ADR 0024, 2 Aug): Antwerp test found 212 products disagreeing across Catalogue, WMS B and billing
  (names, VAT). Product master = Catalogue (Grace's team), with FR/NL names and VAT category.
- **Transition states** (16 Aug): temporary bridges T1–T3 for the warehouse move (TD-14–16), removed by 30 Sep; sweep
  found three 2026 Dispatch leftovers (courier cron fallback, a Core DB view, a nightly copy job), removed by 30 Sep.
- **Vendor checklist** (6 Sep): billing webhooks silent for 9 hours on 31 Aug (Korenwolf shown unpaid); poll every 15
  min, silence alerts, queue below rate limits, production contract checks, status page alerts.

## Book 1, Vol. 5: Ana's facts (October 2027 → March 2028)

- **Openings**: Antwerp 18 Oct 2027 (slipped from September), Eindhoven 22 Nov 2027. Board plan for 2028 (20 Mar):
  eight cities, 60,000 orders a day by end 2028.
- **Estimate** (4 Oct): December forecast 27,000 orders/day; Friday peak ≈ 0.045 % of the day per second ≈ 12/s
  (today ≈ 5.4/s); design point 5× = 60/s; ≈ 400 API calls and ≈ 30 DB writes per order → 1,800 writes/s vs ≈ 2,400
  measured. Last Christmas the primary was resized in a hurry on 16 Dec 2026.
- **Capacity plan** (18 Oct): DB connections 310/400 (out at 1.3×), DB CPU 55 % (1.8×); pooler 1 Nov, browse replica
  8 Nov, primary one size up 15 Nov, freeze 13 Dec–3 Jan; ≈ €2,100/month more.
- **Load profiles** (1 Nov): mix 78/12/6/4; shapes Friday ramp, push spike (300,000 devices), business morning, soak.
  8 Nov: workers exhausted at 2.6× (home screen per request); 15 Nov: 5× passed, checkout p95 640 ms.
- **Performance budgets** (15 Nov): web home 3.4 s → 2.2 s after lazy-loading languages; budgets 2.5 s, 300 KB JS,
  checkout 800 ms, search 300 ms, picker 1 s; owners Dee, Ben, Eli.
- **Security review** (11 Oct): 11 findings, 3 high (non-expiring business API keys, other office's orders by ID,
  unsigned billing webhooks), fixed by 22 Oct.
- **Data classes** (25 Oct, with Lena): public, internal, confidential, restricted; 14 stores of customer data found;
  product analytics moved to its EU instance by 30 Nov; staging data masked; FF-09 requires a class for new tables.
- **Compliance features** (8 Nov): age checks by city (BE 16 beer/wine, 18 spirits; NL 18) storing yes/no only;
  customer.erasure.requested → 9 systems (3 days/month by hand → 4 hours automatic from 6 Dec); retention per class;
  Belgian structured e-invoices via billing.
- **Availability** (29 Nov): business ordering path 99.69 % → 99.79 % with billing off the path (ADR 0025); measured
  99.81 %. Korenwolf renewal: 99.8 %/month for ordering with credits; 99.9 % joint goal for 2028.
- **FMEA** (6 Dec): top risk PSP slow (RPN 216); 3 s timeout, breaker, automatic switch to PSP B. 17 Dec 2027: PSP A
  slow for 22 min, switched in 40 s, no failed orders.
- **DR tiers** (10 Jan 2028): first full restore took 3 h 40; tiers 1–4 (RTO 15 min / 1 h / 1 day / rebuild); backups
  copied to Paris; 18 Apr drill: 22 min.
- **Multi-region** (ADR 0026, 24 Jan): second region ≈ €300k/year vs expected loss well under €100k; pilot light in
  Paris ≈ €1,200/month, RTO 4 h; triggers: 60k orders/day, region outage > 1 h, a contract requiring it, a non-EU city.
- **Routing TCO** (7 Feb): Engine A ≈ €243k vs managed service ≈ €297k over 3 years; keep Engine A, fund 0.5 engineer.
- **Cloud cost** (21 Feb): cost per order €3.05 at end 2027 (target €2.80); cloud bill €78k → €58k/month; cloud cost
  per order ≈ 9.6 → 7.1 cents.
- **Carbon** (6 Mar): ≈ 9 t CO₂e/year, ≈ 0.9 → 0.6 g per order; answer to Korenwolf's supplier questionnaire.
- **Utility tree** (20 Mar): (H, H) checkout at 5× with 60k/day; new city in 6 weeks by config. Region failover in 1 h
  (M, H) parked; real-time recommendations dropped.
