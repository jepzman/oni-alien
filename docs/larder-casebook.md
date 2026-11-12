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
| 0007 | Send orders to delivery via a transactional outbox | 2026-03-14 | Accepted |
| 0008 | Dispatch as a service: Ordering publishes events, no sync calls (from RFC-003) | 2026-03-27 | Accepted |
| 0009 | Second payment provider for cards + iDEAL, manual switch-over, live by 1 Sep 2026 (~€900/month) | 2026-04-02 | Accepted |
| 0010 | Run Dispatch on the managed container service | 2026-04-08 | Accepted |
| 0011 | Run the Korenwolf pilot on manual standing orders | 2026-04-15 | Superseded by 0014 |
| 0012 | Routing Engine A (open source, self-hosted) for Dispatch | 2026-05-26 | Accepted (on watch, Sep 2026) |
| 0013 | Buy a billing service for Larder for Business invoices | 2026-06-08 | Accepted |
| 0014 | Scheduled orders on business accounts, in Ordering | 2026-09-21 | Proposed |

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
