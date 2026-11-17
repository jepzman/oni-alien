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
| Jonas | Product owner, Larder for Business (joins 3 January 2028; takes over from Grace by 28 February 2028) | office managers, service levels, renewals |

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
| 0027 | Ordering owns its own database; others use events and the Ordering API | 2028-04-21 | Accepted (done 21 Aug 2028) |
| 0028 | Managed search for the catalogue (go with changes) | 2028-05-19 | Accepted |
| 0029 | A third payment method (led by Cho) | 2028-09 | Accepted |

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

## Book 2, Vol. 6: Grace's facts (April → December 2027)

- **City playbook** (5 Apr, for Utrecht 12 Apr): configuration vs local, a launch rhythm, five daily numbers; Utrecht app
  work 6 days (Rotterdam: 6 weeks); week 1 tickets 2.9 per 100; 2nd orders 46 %. v2 The Hague (Jun), v3 Antwerp (Oct).
- **Business portal** (live May; review 7 Jun): skip, change, add, see next delivery until 16:00 the day before;
  approvals above budget; 80 % of changes in the portal by week 4; Mo's re-typing 12 h → 2 h a week; invoice fixes 9 → 1.
- **Larder Plus pricing** (14 Jun–12 Jul): survey of 1,100 (acceptable €5–€9); new sign-ups A €6.99 / B €7.99, first
  month free; sign-up 3.4 % vs 3.1 %; revenue per visitor +6 % at €7.99 → €7.99 (A's 610 members keep €6.99 for 12
  months). 1 Sep: 5,400 members, ordering 34 % more often.
- **B2B vs B2C** (5 Jul): one ordering core, two front doors. Four office clients (Korenwolf + three).
- **Substitution platform** (19 Jul): owned by Ben's team; customers: consumer app, portal, Plus, picker app; three
  copies retired by Oct.
- **Localisation** (2 Aug): French shipped in May; 40 Antwerp households tested in July and September; Belgian VAT
  (6 %/21 %), Bancontact first, fr-BE and nl-BE by native writers; Antwerp week 1: 2.4 tickets per 100.
- **Accessibility** (16 Aug): 41 issues; swap timer fixed (announce at 1:00 and 0:00; "more time"); 5 disabled testers;
  all fixed by Nov; "more time" used by 6 % of all customers.
- **Product-led growth** (from 6 Sep): first-order welcome and guaranteed slot (2nd order ≤ 30 days 41 → 49 %); Plus
  offered after the 2nd good order (trial → paid 62 %); give €10 / get €10 (12 % of new customers); paid cost per new
  customer −18 %.
- **Korenwolf Mondays** (13 Sep): stock reserved at 20:00 the evening before for every business account's standing
  orders, picked first from 06:00; Korenwolf Mondays 96.8 → 99.1 %. Renewal signed December 2027.
- **Service levels in the portal** (4 Oct): live status, automatic monthly report (contract definition), automatic
  credits (10 % of a missed delivery); Mo's report work 2 days/month → 0; Korenwolf Q4 99.0 %.
- **Product principles** (11 Oct): ask don't assume · honest over clever · complete or explained · one product for homes
  and offices · fast for pickers · less but better. Checkout Plus banner removed (#2).
- **Product sense** (25 Oct): Grace orders weekly in a rotating city; Antwerp's French swap message rewritten.
  Prediction log: 31 predictions, 19 right on direction.
- **Two-year review** (8 Nov) and **hiring** (from 22 Nov): Jonas hired as PO for Larder for Business, starts 3 Jan 2028.
- **Handover** (plan 13 Dec): state-of-the-product document, introductions, shadow 3–14 Jan, lead 17 Jan–25 Feb, Grace
  steps out 28 Feb 2028. Grace keeps ordering, apps, Plus, the substitution platform and the 2028 strategy.

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

## Book 1, Vol. 6: Ana's facts (April → September 2028)

- **Organisation**: five product teams, 30 engineers, a reliability team from autumn 2028; Jonas is the business PO.
  Cities: Ghent opened 19 Jun 2028, Haarlem 11 Sep 2028: eight cities by the 28 Sep board.
- **Principles** (3 Apr): eight, statement/rationale/implications; questions to Ana ≈ 15 → 4 a week.
- **Ordering's database** (ADR 0027, design 10–21 Apr): one-way doors decided in two weeks; migration plan 29 May
  (expand, shadow, Eindhoven first on 3 Jul, all cities by 7 Aug, contract 21 Aug); 0 orders lost; 3 quick rollbacks.
- **Guardrails** (17 Apr): review board replaced; review triggers: new data store, vendor, trust boundary, published
  events, principle exception. Lightweight review (from 15 May): ADR 0028, managed search, 4 working days.
- **Golden path** (8 May): `larder new-service`; new service to first deploy 3 weeks → 1 day; 4 of 5 new services on it.
- **Fitness functions** (22 May): FF-01…FF-12, incl. FF-10 cost per 1,000 orders ≤ €70 and FF-11 no reads of another
  module's tables.
- **Risk register** (24 Apr): 12 risks; #1 architecture depends on Ana (4 × 4 → 2 × 4 by Sep).
- **Ghent readiness** (12–16 Jun): one red (Dutch help pages), fixed 18 Jun; opened with no day-one surprise.
- **Station lockers** (workshop 3–4 Jul): pilot with 2 chilled lockers at Utrecht Centraal from 4 Sep, by hand; review 16 Oct.
- **Haarlem** (17 Jul): moved from 4 to 11 Sep, born on the new database; old replica off the same week (≈ €1,900/month).
- **Old order export** (TD-21) retired 2 Oct 2028 without escalation (data team's orders_v2 model; ally: Cho).
- **Architecture backlog** (21 Aug): one list, 20 % of each team, ordered quarterly with Grace and Jonas.
- **Handover** of Ordering to the reliability team: game days 14 and 21 Sep; pager 1 Oct; first incident 9 Oct, 18 min.
- **Architects**: Cho (payments + data) and Dee (mobile + customer apps) grown from May; Cho led ADR 0029 alone in Sep;
  guild every other Thursday; architecture path on the career ladder from Oct.

## Book 3, Vol. 1: Sanne's facts (January → February 2026)

Book 3 follows the PMBOK Guide, eighth edition (6 principles, 7 performance domains, 5 focus areas, 40 processes).
Plan: `docs/HANDOFF-project-manager.md`. Every number below carries into later volumes (the project file grows).

- **Sanne** joins Monday **12 January 2026** as delivery manager. Her last job: fitting out warehouses (all predictive).
  Larder's first project manager. Opening is **15 weeks** away (27 April).
- **Desk sort** (14 Jan): 11 requests → 4 projects (Rotterdam launch, Zuid cold-room replacement, new helpdesk tool for Sam,
  summer courier hiring drive), 3 products (approvals, customer app, picker app), 4 operations.
- **Joost's spreadsheet** “Rotterdam v7”: 140 rows, 31 without an owner.
- **Value chain** (16 Jan, signed by Joost and Femke): outputs = store open and stocked, city set up in the platform,
  ~40 pickers and couriers trained. Benefits: **500 orders a day by the end of May** (owner Joost), **90 % express on time
  by the end of the summer** (Joost), **a launch playbook: next city in ≤ 8 weeks** (Femke). Checked at +4 weeks, +12 weeks
  and the start of Utrecht.
- **Role card** (19 Jan): **Joost is the sponsor**; steering group Femke, Marco, Priya, Joost, fortnightly. Three triggers go to
  Joost: date at risk by more than 3 days, a change over €5,000, a change to what customers get at launch.
- **Environment scan** (21 Jan): cold room and fridges take 8 weeks from order; food-safety registration needed before the
  first delivery (Tomás with Lena); the lease allows no deliveries before 07:30.
- **Whole-launch map** (23 Jan): seven workstreams: store fit-out (Joost), people (Joost), stock and suppliers (Tomás),
  platform set-up (Eli, Ana), apps (Ben, Dee), payments and legal (Cho, Lena), launch marketing (Priya). Orphans found:
  food-safety registration, charging for 40 e-bikes. Opening hours stay 08:00–22:00 at launch (Tomás proposed 07:00–23:00).
  The map had **no line for store IT and internet** (see Ana's Vol. 2: the line was ordered 30 March, too late).
- **Value test** (26 Jan): 71 must-have rows, 47 that help, 22 parked (tote bags, an app animation). Progress is counted as
  must-haves done / 71 (24 on 26 Jan).
- **Quality built in** (28 Jan): nightly script for prices, VAT and zones (Eli); label scanned at the shelf; 20 practice orders
  per new picker at Noord; a weekly end-to-end order through RTM-0; a rehearsal week before go / no-go.
- **First status report** (30 Jan, 12½ weeks to go): **amber**. Commitments: fridge order by 13 Feb (placed 13 Feb), a first
  plan by 20 Feb. **Budget €380k** (fit-out and equipment €260k, hiring and training €60k, launch marketing €40k,
  reserve €20k), confirmed by Marco.
- **Long view** (2 Feb): fridges with doors, +€14k, ≈ €6k a year less electricity → **reserve €20k → €6k**; first deliveries
  07:30; unsold food to a Rotterdam food bank daily from week 1.
- **Planning session** (4 Feb, Ben, Dee, Eli, Tomás, Joost's operations lead): Sanne's own 96-task plan thrown away; the team
  plans and estimates its own work; three decision levels (team, Sanne, sponsor).
- **Approach** (9 Feb): fit-out, people, stock, payments and legal predictive; platform, apps and marketing adaptive (two-week
  sprints). **Shared milestones: fit-out complete 3 Apr, stock on shelves 17 Apr, app ready 20 Apr, go / no-go 24 Apr,
  opening 27 Apr.**
- **Seven tabs** (13 Feb, 10 weeks to go): €61k of €380k spent or committed; amber on scope (→ the MoSCoW session of 3 March),
  stakeholders (neighbours, landlord) and risk (top three: cold-room delivery, hiring on time, StockPilot's rate limit).
- **Tailoring** (18 Feb): one-page charter and plan, top-15 risk list, one-page status on Fridays, one meeting (Thursdays
  09:30, 30 min); no communications plan, procurement plan or earned value. Review of the fit: 20 March.
- **Launch desk** (25 Feb): a supportive PMO of two hours a week (templates, lessons page, launch playbook, a quarterly sheet of
  all projects for Femke); agreed until Utrecht.
- Meanwhile links: focus on value ↔ Grace's strategy on a page; build quality in ↔ Ana's walking skeleton; let the team
  decide ↔ Grace's product trio; plan it all or learn as we go ↔ Grace's now / next / later roadmap.
- Open threads for Vol. 2 (Governance): the charter, the plan of 20 Feb, phase gates around the five milestones, the decision
  log shared with Ana (16 Mar), the scope misread corrected 9 Mar, the tailoring review of 20 Mar and the missed internet line.

## Book 3, Vol. 2: Sanne's facts (February → May 2026)

Vol. 2 covers the Governance domain (nine processes). Every template card is a page of **the Rotterdam project file**
(`/rotterdam/`); the numbers below are that file's numbers.

- **Charter** (19 Feb, signed by Joost and Femke): in = store fitted, stocked, staffed; city in the platform and apps; ~40
  staff trained; launch marketing; two weeks of hypercare. Out = new app features for Rotterdam, Larder for Business, changes
  to Amsterdam. Done when: hypercare exit, handover to the store manager, closing report accepted.
- **Plan on a page** (20 Feb; to the steering group 27 Feb). Budget by line: fit-out **€226k** (builder €148k fixed price;
  cold room and fridges €78k incl. the €14k door upgrade), equipment and store IT **€48k**, people **€60k**, marketing
  **€40k**, reserve **€6k** = €380k. Cross-checks failed on: pickers starting a week after stocking (first group of 15 moved
  to **30 March**), handhelds ordered too late (moved to 23 Feb), no reserve for the top risks (stated as the weak point).
- **Sourcing** (24 Feb): builder fixed price €148k, handover 3 April, €1,000 off per late day (max 10), 5 % retention;
  cold room supply-and-install (ordered 13 Feb, 8 weeks); e-bikes leased by operations; training and city set-up in-house;
  adverts time and materials, cap €12k.
- **Governance** (27 Feb): teams → Sanne → sponsor (the three triggers, answer in 2 working days) → steering group
  (date, total budget, go / no-go, closing). Vetoes: Marco (spend), Lena (contracts, personal data). Steering Fridays:
  27 Feb, 13 Mar, 27 Mar, 10 Apr, 24 Apr, 8 May, 22 May. Sunday opening: not at launch (Joost).
- **Yara**, Rotterdam store manager, starts **2 March 2026** (reports to Joost).
- **Gates** (criteria written 2 Mar): G1 3 Apr fit-out, G2 17 Apr stock, G3 20 Apr app, G4 24 Apr go / no-go (steering group),
  G5 11 May hypercare exit. **G1: go with conditions**: 14 snags, 2 blocking (cold-room door seal, fire-safety sign), fixed by
  7 April; dry goods stocked from 6 April, chilled from 8 April. G4: go with two conditions (Grace's two reds, fixed 26 Apr).
- **Weekly rhythm** (from 5 Mar): Monday decision log with Ana, Thursday 09:30 leads, Friday status. Must-haves done (of 71):
  26 Feb 33 · 5 Mar 34 · 12 Mar 41 · 27 Mar 49 (plan 52) · then +6, +5, +9 a week · 24 Apr 69 · 26 Apr 71.
- **Baseline v1** (13 Mar, steering group): scope signed by Grace (6 app Musts) and Joost (65 others); €335k committed
  (builder 148, cold room 78, equipment 48, recruiting and marketing contracts 61). The 9 March misread (“approvals at launch”) was Sanne restating a promise
  Grace never made. **Baseline v2** on 31 Mar after C-03.
- **Quality review** (20 Mar): the nightly script had failed silently 8–11 March (issue I-05; 212 products listed when it ran
  again); 12 of 15 pickers had done their 20 practice orders; RTM-0's weekly order had caught 2 faults. Next review 17 Apr.
- **Issue log** (from 20 Mar): **I-07 internet line** raised by Eli on 20 Mar, ordered 30 Mar, live 13 May; workaround a 4G
  router with backup SIM (€600). I-09 builder late; I-14 two blocking snags; I-19 / I-20 Grace's two reds. Totals at closing:
  23 raised, 21 closed, 2 handed over (I-21 street numbers in zone RTM-2, I-23 Saturday slots).
- **Escalation** (23 Mar): builder forecast handover 8 April (electrical inspection re-booked). Option B chosen by Joost at
  16:00: work on the weekend of 28–29 March, €5k, handover held on 3 April.
- **Status of 27 Mar**: amber; 49 of 71 done; €355.5k committed; forecast 65 of 71 at 4 a week. Colour rules: schedule red if
  more than 3 days late; scope amber at 4–8 behind the plan line; finance amber when the reserve is in use.
- **Change log**: C-01 fridges with doors +€14k (Marco, 2 Feb) · C-02 weekend work +€5k (Joost, 23 Mar) · C-03 approvals in
  Rotterdam from launch to June (steering group, 31 Mar; same session as Ana's trade-off sliders) · C-04 4G router +€0.6k
  (Sanne, 1 Apr) · C-05 in-store launch event, rejected (Joost) · C-06 second cold-room door, deferred to after opening.
  Reserve: 20 → 6 → 1 → 0.4.
- **Handover** (walk-round 12 May, signed by Yara 15 May): retention released 15 May; Sanne answers within a day until 29 May.
- **Lessons** (18 May): 41 lines → 12 playbook changes, 9 template changes, 20 dropped. Top: store IT is an eighth workstream;
  order long-lead items in week 1; the product owner signs the launch scope.
- **Closing report** (22 May, steering group: closed): opened 27 April; 71 of 71; **€379.6k of €380k**; **590 orders a day in
  week 4** (target 500 by end May: met); on time 84 % in May (target 90 % by end of summer: open, Joost); playbook v1 written.
- Meanwhile links: gates ↔ Grace's launch checklist; baselines ↔ Grace's MoSCoW; directing the work ↔ Ana's decision log;
  change control ↔ Ana's trade-off sliders; handover ↔ Grace's hypercare.
- Open threads for Vol. 3 (Scope and Schedule): goes back into the same months for the 71 must-haves as a work breakdown,
  the estimates behind the 4 February plan, the network and critical path of the fit-out, the release plan of 9 March.

## Book 3, Vol. 3: Sanne's facts (February → April 2026, Scope and Schedule)

Vol. 3 goes back over the same weeks as Vol. 2 for the scope and schedule work behind the plan. Template cards are
project-file pages 16–30. Two Vol. 2 slips were corrected on the way: the builder's extra work was **one weekend
(28–29 March)**, not two; and on 10 April the last three weeks had finished **4, 6 and 5** (not 6, 5 and 9).

- **Estimating session** (4 Feb): Sanne anchored the platform estimate (“Zuid took about two weeks?”) → all said 10.
  Redone as wideband Delphi: 8, 10, 12, 24 (Eli: deposits need their own VAT rate; zone edges cut through streets) →
  round 2: 10, 12, 12, 14. **Apps: 14 Musts = 61 story points; capacity for Rotterdam 8–10 points a sprint** (approvals
  runs alongside) ≈ 7 sprints, 5 available → to Grace → her MoSCoW of 3 Mar: 6 Musts = **26 points ≈ 3 sprints**.
- **First estimates** (5 Feb, answer to Femke: “it fits, with no spare week; the fit-out is the long pole”):
  fit-out analogous from **Zuid (6 weeks, 520 m², incl. 1 week floor re-work)** → Rotterdam **600 m²**: 5–7 weeks;
  stocking parametric **2,500 products × 2½ min ≈ 104 h** (15 person-days) but deliveries over 10 working days;
  training ≈ 50 person-days; platform set-up bottom-up, 9 pieces, 12 days.
- **Cold room**: the supplier quoted “up to 8 weeks”; on ordering (13 Feb) it **confirmed delivery for Fri 27 March**
  (panels leave the factory on the 26th; an earlier date was refused).
- **Three-point** (6 Feb): **Kees**, the builder's site manager: fit-out **22 / 25 / 34** working days (worst: inspection
  re-booked, materials late, slow curing) → PERT **26 ± 2**; P(25) ≈ 31 %, expected Tue 7 Apr, 84 % by Thu 9 Apr.
  Eli: platform **8 / 12 / 24** → 13⅓ ± 2⅔. Weekend work priced on **12 Feb: one weekend ≈ €5,000**.
- **Rules for scope and schedule** (10 Feb): unit = a must-have with owner and “done means”; predictive work in working
  days (Mon–Fri), adaptive in two-week sprints; rolling wave (detail 4 weeks ahead); calendar: **builder off on Easter
  Monday 6 Apr**; **27 April, opening day, is King's Day** (store and couriers work; offices and builders don't).
- **Requirements** (Noord's Friday peak walked; workshop 12 Feb with Tomás, Joost's ops lead, Sam, Lena; Grace's
  prototype findings; Zuid's opening): **96 requirements → 71 must-haves (each traced), 18 “helps”, 7 rejected**.
  Examples: R-08 ≤ 2 pickers waiting at the cold room at peak (→ wider door + layout; second door deferred, C-06);
  R-12 cold room 2–4 °C, alarm > 5 °C for 15 min; R-23 100 % prices + VAT before stocking; R-31 40 e-bikes charged by 07:30
  (three-phase supply, must-have F-09); R-44 buttons ≥ 12 mm; R-57 food-safety registration.
- **Scope statement** (16 Feb): result = a dark store serving zones **RTM-1 to RTM-3**; 8 deliverable groups; hypercare IN;
  a separate Rotterdam landing page OUT (the waitlist page gets a city field; the promo code came back as extra E1).
- **WBS** (17 Feb; app branch cut 6 Mar; baselined 13 Mar): 1.0 project management (no must-haves, ≈ 6 % of effort);
  fit-out 16 · people 9 · stock 10 · platform 12 · apps 6 · payments + legal 9 · marketing 5 · opening + hypercare 4 = 71.
  Fit-out level 3: building works, cold room + fridges, shelving, e-bike charging, **1.1.5 store systems online** (Eli).
  The builder's quote said **“data cabling to the comms cabinet; connectivity by client”**: the internet line was a
  missing work package in 1.1.5 (Sanne's mistake: she skipped the “small print” check). Added 23 Mar; count stays 71.
- **Fit-out network** (with Kees, 19 Feb; working days, day 1 = Mon 2 Mar): A strip-out 3 · B first fix 4 (A) ·
  C plumbing 3 (A) · D screed + curing 7 (C) · E walls, ceiling 5 (B) · F second fix 4 (E) · G inspection 1 (F; booked
  **Tue 24 Mar**) · H paint 3 (G, D) · I cold-room build 3 (D; delivery 27 Mar) · J energise + 48 h test 2 (I, G) ·
  K shelving, fridges, chargers 3 (H) · L snags 2 (K) · handover after J, L. Sanne's first chart (12 Feb) had bars and no
  links (her mistake in the schedule collection).
- **Critical path** (20 Feb): **A-B-E-F-G-H-K-L = 25 days → Fri 3 Apr**. C and D: 4 days' total float (C has no free
  float). I-J: zero float, held by the delivery date. **23 Mar**: inspection re-booked to **Thu 26 Mar** (+2 working
  days) → handover **Wed 8 Apr** (Easter Monday off) = 5 calendar days → escalated → crash: builder works **Sat 28 and
  Sun 29 Mar** on paint (C-02, €5,000 = €2,500 a day) → back to 3 Apr. Afterwards both chains end on day 25.
- **Float** (24 Feb): the plumber asked to start a week late; allowed **two days (starts Mon 9 Mar, done Wed 11 Mar)**,
  leaving two for the screed. No project buffer; feeding buffer for the cold room refused → confirmation call 20 Mar.
- **Three views** (from 20 Feb / 13 Mar): milestone chart for the steering group (6 milestones incl. G5), summary for the
  leads, detailed Gantt for the builder; sprint boards and the burn-up for adaptive teams.
- **Schedule tracking**: must-haves done 26 Feb 33 · 5 Mar 34 · 12 Mar 41 · **19 Mar 45** · 27 Mar 49 (plan 52) · 3 Apr 55 ·
  10 Apr 60 · 17 Apr 69 · 24 Apr 69 · 26 Apr 71; plan line 33 → 71 (26 Feb → 24 Apr). Forecast on 27 Mar: weeks of 7, 4, 4
  → 17 Apr to 3 May. Milestone forecasts: G1 3 Apr except 8 Apr on 23 Mar; G3 app ready off the chart (“mid-May”) on
  20 and 27 Feb, 20 Apr from 6 Mar, 22 Apr on 20–27 Mar, 20 Apr from 3 Apr.
- **Acceptance**: G2 (17 Apr) the scan check was 100 %, but **aisles 14 and 15 carried Noord's aisle codes**; Tomás
  rejected them; relabelled 18–19 Apr; accepted **20 Apr**. Lena accepted payments + legal 13 Apr; Grace the app 20 Apr
  (real orders in RTM-1, -2, -3); Priya marketing 24 Apr.
- **Scope creep** (27 Mar, Sanne's mistake in the control collection): nine unlogged extras since the baseline, ≈ 7
  team-days (5 from Ben, Dee, Eli): E1 promo code (kept) · E2 Friday 21:00–22:00 slot (after opening) · E3 neighbourhood
  names (after) · E4 English shelf labels (kept) · E5 tour video (kept) · E6 store dashboard for Yara (after) · E7 Rotterdam
  test data (kept) · E8 courier route cards (kept) · E9 waitlist email variants (after). Rule: every addition on the extras
  list, decided Thursdays.
- Meanwhile links: requirements ↔ Grace's prototype testing; WBS ↔ Grace's story mapping; critical path ↔ Ana's last
  responsible moment; Gantt and milestones ↔ Grace's roadmap vs release plan; acceptance ↔ Grace's definition of done;
  scope creep ↔ Grace's request triage.
- Open threads for Vol. 4 (Finance and Resources): the €380k budget built bottom-up from the WBS, the reserve (20 → 0.4),
  cash flow of the builder's payments and retention, earned value on the fit-out, hiring 40 people under a cap of four
  new office hires, training at Noord, the electrician crew shared by B and F, the e-bike lease.

## Book 3, Vol. 4: Sanne's facts (January → May 2026, Finance and Resources)

Vol. 4 follows the same launch through its money and its people. Template cards are project-file pages 31–45.
Vol. 2's committed figures were corrected on the way (the €48k of equipment, ordered 23 Feb, had been left out):
**€335k committed on 27 Feb and at the 13 Mar baseline; €355.5k on 27 Mar** (was €287k and €322k).

- **Money rules** (27 Jan, signed by Marco): € excluding VAT; covers external spend and new store staff until opening;
  not Larder's own people's time (≈ 170 person-days, tracked by Marco), the e-bike lease or rent (operations); Sanne may
  commit up to €5,000 within a line, Joost above, Marco vetoes outside the budget; counted as committed, spent, forecast.
- **Cost estimate** (28 Jan, bottom-up against the top-down €380k per city set in Sept 2025): builder €148k (indicative,
  ± 10 %; fixed price 26 Feb at the same figure) · cold room + fridges €64k (firm) · equipment + store IT €48k ·
  people **40 × €1,500** (€500 recruiting + €1,000 paid induction and training) = €60k · marketing €40k → **€360k**.
- **Budget** (30 Jan, confirmed 6 Feb): baseline €360k + **reserve €20k** (risk list ≈ €10k, doubled by Marco for a
  first city); no management reserve. S-curve: end Jan 4 · end Feb 64 · end Mar 238 · end Apr 352 · end May 360 (€k).
- **Cash** (terms table 27 Feb): builder 20 % on signing / 40 % first fix / 35 % handover / 5 % retention (paid 15 May);
  cold room 30 % with order / 70 % on delivery; equipment on delivery, net 30. Sanne agreed 20 % on signing without
  checking Larder's monthly 30-day payment run → Kees: “no money, no start”; Marco paid an exception on Mon 2 Mar.
  Cash paid by month: Jan 4 · Feb 58 · Mar 141 · Apr 129 · May 47.6 = **€379.6k** (planned 4 / 58 / 138 / 132 / 48).
- **Committed** (Sanne said “€61k spent” at the steering group of 27 Feb; it was the recruiting €30k and marketing €31k
  contracts of mid-Feb): committed was **€335k** (+ cold room 78, equipment 48, builder 148).
- **Money table 27 Mar** (budget / committed / spent / forecast, €k): builder 153 / 153 / 96 / 153 · cold room 78 all ·
  equipment 48 / 48.5 / 48.5 / 48.5 · people 60 / 45 / 21 / **62.5** (agency €575 a hire, not €500) · marketing
  40 / 31 / 22 / **37** · total 379 / 355.5 / 265.5 / 379; reserve €1k.
- **Earned value, 20 Mar** (BAC €374k = 360 + the €14k fridge upgrade): **PV 178 · EV 175 · AC 178** → SV −3, CV −3,
  SPI and CPI 0.98, both in the people line (34 of 40 hired). Agency then fixed its fee for the last 6 hires at €500.
- **Forecast**: formula 374 ÷ 0.983 ≈ €380k (the whole reserve); owners' lines on 27 Mar: €379k; actual **€379.6k**:
  fit-out 231 · equipment + IT 49.1 · people 62.5 · marketing 37. The reserve went on C-02 and C-04, not on hiring.
- **Payback** (22 May, Marco): ≈ €4 contribution per order; 550 orders a day assumed from June ≈ €66k a month →
  **paid back about December 2026**. A week earlier for a city ≈ €15k; Utrecht in 8 weeks, not 15, ≈ €100k.
- **RACI** (2 Feb): one A per row; shelving layout → Tomás (A); launch messages → Priya (A), Grace (C).
- **Resource estimate** (10 Feb): ≈ 350 orders a day in the first month; pickers 9 an hour (Noord 6:40 an order) →
  **15 pickers**; couriers 2.5 deliveries an hour → **25 couriers**; 40 e-bikes, 30 handhelds. Joost's first answer:
  “60, like Zuid” (€90k). Second wave (+5 pickers, +12 couriers) for 500 a day, operations budget.
- **Acquiring**: hired via agency 22, job boards 10, referrals 4, internal moves 4; last hire 17 Apr. Marco's cap of
  four salaried central hires in 2026: Rotterdam used one (Sanne). **Borrowed**: Sanne agreed 4 Noord pickers from
  27 Apr with Tomás (30 Mar); Joost caught the King's Day clash (2 Apr) → **2 from Noord + 2 from Zuid, 28 Apr–8 May**.
  Opening day: Rotterdam's own team, Yara and Grace on the floor, Tomás at Noord for King's Day.
- **Levelling** (24 Mar): Eli at **160 %** in the week of 23 Mar (platform 2½ d, RFC-003 1½, on call 1, internet line 1,
  extras 1½, alert fix ½); after: on-call swapped (Ana), Ben does the Dispatch code, alert fix and zone checks moved
  within float, dashboard paused → 80 / 100 / 100 / 100 / 95 / 75 %. Key people planned at 80 % from then on.
- **Leading without authority** (16 Mar): Dee's store-page texts from Priya's team were waiting 9 days; Sanne got them
  next day; Yara's new pickers test approvals for Grace; Dee's team named in the status; both items done 3 Apr.
- **Rehearsal week conflict** (20–24 Apr): Tomás needs no wrong items; Ben no risky changes; rule: log it, triage at
  16:00, code if it can cause a wrong item, else a training note → **14 problems: 4 code fixes (2 caused wrong items),
  7 training notes, 3 parked**.
- **Availability check** (08:30 daily in hypercare; 29 Apr): orders 470 (plan 350); 3 couriers sick → **Zuid lends 3,
  29 Apr–2 May**; 4 e-bikes with flat tyres, lease supplier held to 24 h repair with a credit; 2 handhelds broken (4
  spares left); **second hiring wave pulled forward to 4 May**. Borrowed pickers home on 8 May.
- Meanwhile links: cost estimates ↔ Grace's business case; payback ↔ Ana's total cost of ownership; levelling ↔ Ana's
  RFC-003; leading without authority ↔ Ana's influencing without authority; team conflict ↔ Grace's disagree and commit.
- Open threads for Vol. 5 (Stakeholders and Risk): the neighbours and landlord (not contacted until 2 Mar), the risk
  register's top three (cold-room delivery, hiring on time, StockPilot's limit), the reserve sized from a risk list,
  the rival already in Rotterdam, and Antwerp (September 2027) as the next big launch.

## Book 3, Vol. 5: Sanne's facts (October 2026 → October 2027, Stakeholders and Risk: Antwerp)

Vol. 5 covers the Stakeholders (7) and Risk (6) domains through **the Antwerp launch**, the first city abroad. Template
cards are the **Antwerp** pages of the project file (`antwerp/01`–`15`; the page `/rotterdam/` is now “The Project File”,
grouped by project). Every number below was checked by script (weekdays, sums, the simulation); the block at the top of
`content/project-5/01_involved.py` holds them in one place. **Chosen on purpose (no other book said): why Antwerp
slipped.** It was risk R-07, the city's environmental permit, on the register from November 2026, scored low by people
who knew Rotterdam, with no Larder owner.

- **Project** starts Mon **5 Oct 2026**; sponsor **Femke**; steering group Femke, Marco, Joost, Priya, Lena (first Friday
  monthly). Sanne runs Utrecht (12 Apr 2027) and The Hague (14 Jun 2027) from the playbook alongside.
- **Store**: a former tyre depot in Berchem, **640 m²**, a terrace of **46 houses** behind the loading yard, a school on the
  corner (drop-off 07:30–08:30). Lease signed **Tue 15 Dec 2026**, keys **Tue 1 Jun 2027**.
- **New people**: **Maarten** (Antwerp lawyer, works with Lena from Oct 2026) · **Pieter** (site manager, the Belgian
  builder) · **Hilde** (permit agent, from Mon 8 Mar 2027, €6k) · **Koen** (sales manager, a produce wholesaler at the early
  market) · **Inès** (Antwerp store manager, starts Mon 7 Jun 2027).
- **Stakeholder register** (2 Nov): v0 copied Rotterdam's (14) → **31** from four sources (charter, Rotterdam lessons, a walk
  round on Sat 31 Oct with Joost, Lena + Maarten): Larder 12, partners 8, authorities 5 (permit office, FAVV-AFSCA, fire
  service, VAT office, mobility department), community 6 (46 households, school, shops, **3,100 waitlist**, a rival, press).
- **Grid** (9 Nov, Sanne's mistake in “Who's involved”): permit office placed **keep informed** (power “low”: in Rotterdam
  the cold room needed nothing), owner “builder”; moved to **manage closely**, unaware → supportive, on **8 Feb 2027**.
- **Communications plan** (23 Nov): Dutch (Flemish) for city, landlord, street; French or Dutch by choice for customers;
  English inside Larder; one owner per audience; outside Dutch texts written or checked by a Flemish writer (the first
  landlord letter, drafted in Amsterdam, came back “correct, but blunt”).
- **Neighbours' meeting** (Thu 21 Jan 2027, community centre, 19:00): **28 people** of 46 households + the school's head.
  Raised: lorries before 07:00 **12**, e-bikes on the pavement 9, condenser noise 5, litter 2. Promised: e-bikes by the back
  lane, a named contact, a quarterly meeting, a daily litter walk; lorry times not promised (“answer by 31 March”). The
  lorry concern was logged but **not linked to R-07**. Investor wording (Femke, 25 Jan): “planning date September 2027,
  confirmed when the store's permits are in.”
- **Supplier meetings** (Sanne's mistake in “Abroad”): Wed 3 Feb, English, no agenda → Sanne heard 07:00 and free crates,
  Koen's proposal (12 Feb) said **05:30** and a **€2 deposit** a crate. Re-run Wed 17 Feb in Dutch (agenda Mon 15 Feb,
  read-backs, summary within 24 h, confirmed Thu 18 Feb): deliveries 05:30 at the back door Mon–Sat; €2 deposit credited on
  return; order by 14:00 the day before; a trial week before opening. The 05:30 delivery needs the permit's early hours.
- **Belgian differences** (Mon 8 Feb, Lena, Maarten, Sanne): environmental permit (cooling plant + deliveries before 07:00,
  30-day public inquiry), food-safety registration (Lena), VAT 6 % / 21 % (Marco, Mar), Bancontact (Cho, Jul), staff
  documents in Dutch (Joost), sector pay scales (Joost), courier contracts (Joost + Lena), alcohol 16 / 18 (Grace), structured
  e-invoices (Ana, later). Habits: formal letters; meet the city informally before applying; confirm decisions in writing.
- **Engagement review** monthly from Fri 5 Mar: permit office U → N (pre-application meeting **Thu 11 Mar**); Koen R → S;
  neighbours scored N in May from low attendance (9 at the April meeting) → **14 objections** in the inquiry (closed 22 Jun) →
  R → door to door with Inès **26–30 Jul** → N in Sep; nine came to the opening. Rule from June: no evidence, no score.
  Waitlist emails opened nl 58 % / fr 31 % → French subject lines rewritten → fr 44 % in August.
- **Risk approach** (16 Nov, signed by Femke): appetite ≤ 2 weeks' slip, money within budget + contingency, no rent before
  1 Jun (Femke refused €9k for keys on 1 May); thresholds to Femke: slip > 2 weeks, beyond contingency, score ≥ 20; scales
  P 1–5 (<10 % … >70 %), I 1–5 (<1 week/€2k … >8 weeks/€50k); red ≥ 12; every risk a **Larder** owner; leads review every
  other Thursday. Missing: the price of a week late (≈ €15k contribution + ≈ €2k rent), added to playbook v3.
- **Risk register** (workshop Thu 26 Nov, written Mon 30 Nov; Sanne's mistake in “What could happen”): 23 rows (19 threats,
  4 opportunities). Top: R-02 hiring 9, R-03 builder 9, R-08 couriers 9; **R-07 permit 1 × 3 = 3, owner “builder”**; R-09
  neighbours 2 × 2, no owner. O-01 Rotterdam shelving design (Tomás), O-02 landlord insulation (Femke), O-04 bakery offer.
- **Re-score** (Wed 10 Feb, after Maarten and Pieter: “the permit is yours, not ours; four to six months is normal”): R-07
  → **4 × 4 = 16**, owner Sanne, R-09 merged in as a cause; R-03 → 2 × 3 = 6 (Pieter's second crew); R-08 → 6.
- **Responses** (Mon 22 Feb): avoid (no early deliveries + a smaller plant) rejected by Joost; transfer: Hilde; mitigate:
  city meeting 11 Mar, cooling drawings by **Mon 15 Mar**, lodge by **Fri 26 Mar**; accept the rest with a trigger. Before
  60 % × €40k = €24k, after 30 % × €40k = €12k, responses €8k (agent 6, early drawings 2). R-04 Bancontact escalated to
  Cho's payments roadmap; R-10 rival accepted; O-01 exploited (≈ €6k saved), O-02 enhanced (landlord said no), O-04 shared.
- **Budget** (Mon 1 Mar): builder 160 · cold room + fridges 84 · equipment + IT 52 · people 68 (40 × €1.7k) · marketing
  fr + nl 46 · Belgian set-up 20 = **€430k**; EMV threats 23.1 − opportunities 4.0 = 19.1 → **contingency €20k** (Sanne)
  → €450k; **management reserve €15k** (Femke) → **€465k** authorised.
- **Simulation** (1 Mar, 1,000 runs, **seed 2027**; script with Eli): P10 6 Sep · **P50 13 Sep** (51 %) · **P80 27 Sep** ·
  P90 11 Oct; 18 Oct ≈ P96. Late runs (after 27 Sep) 162, the permit set the date in 157. Steering group Fri 5 Mar: planning
  date stays 13 Sep; investors told “September or early October”; no earlier keys. Re-runs: 9 Apr (lodging 19 Apr) P50 20 Sep,
  P80 11 Oct; July (objections in) P50 11 Oct, P80 25 Oct.
- **The response with no owner** (risk review Fri 2 Apr; Sanne's mistake in “Doing something about it”): drawings owner
  “cooling supplier”, waiting for Larder's 640 m² layout; trigger of 26 Mar watched by nobody. Layout sent Tue 6 Apr,
  drawings Fri 9 Apr, **lodged Mon 19 Apr**, complete Mon 10 May, **public inquiry Mon 24 May–Tue 22 Jun**. Rules: every
  action a task in the plan; every owner at Larder; every trigger in the Friday status with a watcher. Told the steering
  group on Fri 7 May.
- **Risk → issue** (Thu 15 Jul): the city's case officer: 14 objections, change the hours or bring a noise study, no decision
  before September → R-07 closed, **I-12** opened. Extra steering group **Fri 23 Jul**: A wait (rejected), **B deliveries from
  07:00 + an acoustic screen, open Mon 18 Oct (chosen)**, C dry goods only (rejected, Lena). Cost in the project **€27k**
  (staff starts held 11, marketing re-booked 9, installer re-booked 4, screen 3): contingency 14 → 0 (earlier draws: hiring
  4, translation rework 2), management reserve 15 → 2. Outside: rent ≈ €10k, ≈ €75k contribution (5 × €15k).
- **Permit granted Mon 6 Sep** · cold room tested Fri 17 Sep · food-safety visit Wed 29 Sep · stocking 4–15 Oct ·
  **opened Mon 18 Oct 2027**; week 1 2.4 tickets per 100 (Utrecht 2.9). Forecast final cost **€457k** of €465k.
- **Playbook v3** (Oct): regulators are stakeholders (manage closely until the permit is granted); score risks with people who
  have done it in that country; every response action has a Larder owner and a trigger with a watcher; price a week late in
  every appetite statement (≈ €15k + ≈ €2k).
- Meanwhile links: register ↔ Ana's stakeholder map; stakeholders abroad ↔ Grace's localisation; risk register ↔ Ana's risk
  register and Grace's pre-mortem; risk monitoring ↔ Grace's launching a new city (playbook v3).
- Open threads for Vol. 6 (tailoring, models, artefacts, growing): Eindhoven (22 Nov 2027) from playbook v4; the 2028
  programme (eight cities); which of the 73 project-file pages were used again; a second project manager; the Antwerp
  closing report (final cost vs €457k forecast) and its benefits check.

## Book 3, Vol. 6: Sanne's facts (September 2027 → September 2028, tailoring, methods, growing)

Vol. 6 adds no PMBOK processes; it covers tailoring, models / methods / artefacts, the newer topics and the project
manager's growth. Template cards are the **programme** pages of the project file (`programme/01`–`15`).

- **Eindhoven** tailoring sheet Mon **27 Sep 2027** (five dials; keep gates, risk register with Larder owners, store IT in
  week 1, go / no-go; drop communications plan, separate quality review, earned value, Monday decision log; one meeting,
  Thu 09:30; steering note every other Friday; fit check Mon 25 Oct put back a 10-minute call before go / no-go). File
  **20 pages** (Rotterdam 58). Opened **Mon 22 Nov 2027**, eight weeks from the sheet.
- **Artefact review** Mon **6 Dec 2027** (Sanne, Grace): 73 pages → used as is 21 · shortened 14 · merged 12 · not used 26
  → **launch kit of 18 templates**. Nothing deleted.
- **Playbook v4** Mon **13 Dec 2027** (Sanne + Grace merged): v1 Utrecht Apr 2027, v2 The Hague Jun, v3 Antwerp Oct, v4
  Eindhoven; 11 pages shorter than v3 + Grace's; fixed vs local marked; v4.1 after Nadia plans Ghent (Feb); v4.2 adds a
  sustainability line (Mar). Lessons → changes: Rotterdam 41 → 12, Antwerp 33 → 4.
- **Programme Cities 2028** Mon **10 Jan 2028** (Sanne programme manager, sponsor Femke): Ghent, Haarlem, launch office,
  courier renewal; lockers pilot (Ana) outside with one dependency; board every 4 weeks; benefit = eight cities and 60,000
  orders a day by end 2028 (board plan Mon 20 Mar 2028).
- **Rotterdam benefits check** Mon **17 Jan 2028** (Sanne's mistake: the +12-week check of Aug 2026 was never held): 500 a
  day met (590 week 4); 90 % on time missed (86 % Sep 2026, 90 % Nov 2026, after courier wave 2 and the RTM-2 fix, I-21);
  next city ≤ 8 weeks met (Utrecht 15 Feb → 12 Apr 2027, The Hague 8, Eindhoven 8); payback ≈ Dec 2026 forecast, Jan 2027
  actual. Rule in v4: checks at +4 and +12 weeks by the benefit owner, booked before closing. Antwerp +12 weeks 10 Jan
  2028, Eindhoven 14 Feb.
- **Two-year review** Wed **12 Jan 2028** with Joost (Sanne's manager); feedback from Joost, Femke, Grace, Ana, Eli, Yara;
  work on: outside stakeholders, letting go, programme thinking. **PMP passed Fri 21 Apr 2028**. The notebook: ~90 pages.
- **Hiring** (role card Mon 8 Nov 2027): 34 applicants → 9 screening calls → 4 work samples (6–10 Dec; Antwerp's status
  and issue log of 15 Jul 2027, names removed; panel Sanne, Joost, Yara; scoring sheet written 1 Dec) → offer Fri 17 Dec.
  **Nadia** (six years opening stores for a retail chain) starts **Mon 7 Feb 2028**: one of Marco's four central hires for
  2028.
- **Launch office** Tue **1 Feb 2028**: supportive, one mandatory rule (gates, go / no-go); owns playbook + kit, people
  booking, Femke's portfolio sheet, lessons; monthly peer review; kick-off → agreed plan Rotterdam ≈ 35 days, Ghent 14;
  Ghent used 16 of 18 templates; Nadia keeps the kit from April.
- **AI trial** 1 Feb → 10 Mar 2028 (approved assistant, Lena's rules): status 90 → 30 min; Ghent risks 23 suggested, 9
  kept, 2 new, 1 wrong (“no permit needed”); 3 date clashes found. Sanne's mistake Fri **11 Feb**: unchecked draft said
  “Ghent lease signed” (agreed in principle; **signed Thu 2 Mar**). Rules: approved tool; every fact checked; sender owns
  it; say when AI drafted it.
- **Toolbox page** Mon 14 Feb 2028 (with Nadia): tools sorted by question; Ghent uses 9.
- **Coaching Nadia** (Sanne's mistake Fri **25 Feb**: rewrote Nadia's first Ghent status at 22:00); from Mon 28 Feb weekly
  1:1 Tuesdays, three status questions, delegate fit-out, coach Larder and Belgium.
- **Ghent**: pre-application meeting Tue 7 Feb; lease signed Thu 2 Mar; permit lodged Mon 13 Mar, **granted Fri 12 May**
  (deliveries from 07:00 by design, CO₂ cooling, no objections). Sustainability (6–13 Mar; Korenwolf questionnaire
  answered Mon 13 Mar): CO₂ cooling +€7k, ≈ €1.8k a year back; shelving reused from Zuid ≈ €5k saved; batteries back to
  the lease supplier; food bank from week 1. G1 planned Fri 2 Jun, forecast Thu 8 Jun on Mon **22 May** (amber; Femke asked
  for green before the investor update of Thu 25 May; Sanne gave amber with recovery: stocking 12 → 8 days, second shift
  +€2.1k); G1 passed Wed 7 Jun; **opened Mon 19 Jun 2028**.
- **Haarlem handover**: plan Mon 26 Jun; shadow 19–30 Jun; Nadia leads from Mon 3 Jul; **17 Jul** Nadia and Ana move the
  opening 4 → 11 Sep (new ordering database); Sanne's mistake Wed **26 Jul** (agreed the chargers move on the builder's
  call), fixed Fri 28 Jul (letter to every supplier); Sanne steps out Mon 7 Aug; **Haarlem opened Mon 11 Sep 2028**.
- **Closing note** Mon **25 Sep 2028**: eight cities; ≈ 51,000 orders a day in September, on course for 60,000 by December;
  one line for 12 Jan 2026: “the plan is the team's, the truth is yours, and the thing that sets your date is usually
  outside the room.”
- Meanwhile links: tailoring ↔ Ana's just-enough design; playbook ↔ Grace's launching a new city; sustainability ↔ Ana's
  green software; servant leadership ↔ Ana's growing architects; ethics ↔ Grace's bad news; growing ↔ Grace's growing as a
  PO; hiring ↔ Grace's hiring a PO; handover ↔ Grace's handing over and Ana's handover to operations.
- **Book 3 is complete.** Open threads for Book 4 (Mo): Korenwolf's supplier questionnaire (Mar 2028) and the renewal.
