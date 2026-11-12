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
| 0007 | Send orders to delivery via a transactional outbox (Vol. 2 sample) | 2026-03-14 | Accepted |

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
