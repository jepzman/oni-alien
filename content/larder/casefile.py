# Series 2 · the Larder case file: the company every Series 2 book follows.
# Facts must match docs/larder-casebook.md (the source of truth).

LEAD = ("Every notebook in Series 2 follows one company: <b>Larder</b>, a grocery delivery start-up in Amsterdam that has just "
        "promised its investors <span class=\"hl\">six cities by the end of 2027</span>. Each book sees the same story through "
        "different eyes: the architect's, the product owner's, the project manager's and the account manager's. Read this page "
        "first, or come back to it whenever a note mentions someone you don't remember.")

PREMISE = """  <p>Larder delivers groceries from <b>dark stores</b>: small warehouses closed to the public, where <b>pickers</b> fill each order
  from the shelves. <b>Couriers on e-bikes</b> take it to the door. Customers order in the app or on the web, with two promises:
  <b>express</b> (within 30 minutes) and <b>slots</b> (a chosen one-hour window).</p>
  <p>The business works. The software is held together by habit. Everything runs in <b>Larder Core</b>, one app written in a hurry
  by a co-founder who has since left. Now the money has arrived, and with it a deadline.</p>"""

# (when, what) for the history timeline
HISTORY = [
    ("Mar 2024", "Femke and Jasper found Larder in Amsterdam. Jasper, the first CTO, writes <b>Larder Core</b>."),
    ("Jun 2024", "The first dark store, <b>Noord</b>, opens: about 300 orders a day."),
    ("Nov 2024", "The second store, <b>Zuid</b>, opens after <b>five months</b> of code changes: everything assumed one store."),
    ("Apr 2025", "<b>King's Day</b>: checkout times out for <b>40 minutes</b> at five times the normal peak."),
    ("Jul 2025", "4,000 orders a day, and <b>6 %</b> of them end in a refund ticket, mostly over substitutions."),
    ("Aug 2025", "Jasper leaves. Nobody else knows why Larder Core looks the way it does."),
    ("Sep 2025", "The <b>Series B</b> closes, on one condition: <b>six cities by the end of 2027</b>."),
    ("Oct 2025", "<b>Ana</b> joins as the first solution architect, and <b>Grace</b> as product owner. Series 2 starts here."),
]

# (value, label, note) stat tiles: October 2025
STATS = [
    ("2", "dark stores", "Noord and Zuid, ~2,500 products each"),
    ("4,000", "orders a day", "average basket €38"),
    ("88 %", "express on time", "target 95 %"),
    ("€4.10", "cost per order", "target €2.80"),
    ("6 %", "orders refunded", "mostly substitutions"),
    ("14", "engineers", "three teams + platform"),
]

DRIVERS = [
    ("Open cities fast", "a new city in 8 weeks or less (Zuid took 20)"),
    ("Keep the promise", "95 % of express orders on time (today 88 %)"),
    ("Unit economics", "cost per order down to €2.80 (today €4.10)"),
    ("Stay trusted", "no lost orders, no double charges, GDPR-clean, ready for Belgium"),
]

# (initial, name, role, cares, fears, books, avatar colour)
CAST = [
    ("A", "Ana", "Solution architect · joins 6 Oct 2025", "a platform that grows to six cities without a rewrite", "decisions nobody can explain a year later", "narrates book 1", "pen"),
    ("G", "Grace", "Product owner, ordering &amp; apps · joins 13 Oct 2025", "customers getting what they ordered", "building the wrong thing, fast", "narrates book 2", "green"),
    ("F", "Femke", "CEO and co-founder", "the six-city plan, the investors, the brand", "missing the Series B promise", "books 1–4", "mustard"),
    ("P", "Priya", "Head of Product · Grace's manager", "conversion, the app, the roadmap", "a roadmap nobody believes", "books 1–3", "mustard"),
    ("M", "Marco", "CFO", "cost per order, the cloud bill, cash", "a surprise invoice", "books 1–4", "mustard"),
    ("J", "Joost", "Head of Operations", "dark stores, pickers, couriers, on-time %", "a slower picking line", "books 1–3", "mustard"),
    ("L", "Lena", "Legal and data protection officer", "GDPR, contracts, Belgian rules", "a breach, or an unsigned contract", "books 1, 4", "mustard"),
    ("T", "Tomás", "Manager, dark store Noord", "his pickers, the picker app, the Wi-Fi", "pickers standing idle", "books 1–2", "mustard"),
    ("S", "Sam", "Customer support lead", "refunds, complaints, the helpdesk", "another week of refunds by hand", "books 1–2", "mustard"),
    ("B", "Ben · Cho · Dee · Eli", "Orders lead · payments · mobile lead · platform", "shipping without breaking Larder Core", "the next King's Day", "books 1–3", "mustard"),
    ("S", "Sanne", "Delivery manager · joins Jan 2026", "the Rotterdam launch: dates, risks, dependencies", "a launch date nobody believes", "narrates book 3", "red"),
    ("M", "Mo", "Key account manager, Larder for Business · joins Mar 2026", "Korenwolf, the first business client", "losing the account at renewal", "narrates book 4", "red"),
    ("H", "Hanna · Ruben", "Korenwolf: Head of Workplace · procurement", "happy staff / a fair price and firm service levels", "complaints to the board / overpaying", "book 4", "soft"),
]

# (book, title, narrator, period, status, summary, link or None)
BOOKS = [
    ("Book 1", "The Solution Architect's Notebook", "Ana", "Oct 2025 →", "vols. 1–2 out",
     "How Ana turns a one-line brief into an architecture that can grow to six cities: understanding the problem, finding the "
     "requirements that matter, choosing first shapes, testing risky ideas early, then recording decisions and living with them.",
     "../architect-1/index.html"),
    ("Book 2", "The Product Owner's Notebook", "Grace", "Oct 2025 →", "vols. 1–2 out",
     "The same months through Grace's eyes: what customers really need, why substitutions cost 6 % of orders, which bets to make, "
     "how to say no to the loudest idea, and how to know if anything worked. Many scenes are the same meetings Ana is in.",
     "../product-1/index.html"),
    ("Book 3", "The Project Manager's Notebook", "Sanne", "Jan 2026 →", "planned",
     "Sanne runs the Rotterdam launch: a fixed date, a signed lease, three teams, two vendors and one risky integration. Planning, "
     "estimates, dependencies, risks and status reports that tell the truth.",
     None),
    ("Book 4", "The Client Manager's Notebook", "Mo", "Mar 2026 →", "planned",
     "Larder for Business wins its first client, Korenwolf Group. Mo learns to manage expectations, scope changes, service levels, "
     "monthly reports and a hard renewal, with Hanna and Ruben on the other side of the table.",
     None),
]

KORENWOLF = """  <p>Femke wants a second revenue line with predictable volume: <b>Larder for Business</b>, weekly restocking of office pantries
  (fruit, snacks, drinks, coffee), delivered by van between 07:00 and 09:00 and invoiced monthly.</p>
  <p>The first client is <b>Korenwolf Group</b> (fictional), an insurance and pensions company with about <b>2,400 staff</b> in
  Amsterdam, Rotterdam and Utrecht. <b>Hanna</b>, Head of Workplace, wants happy staff. <b>Ruben</b>, from procurement, wants a fair
  price and firm service levels, and compares everything with the old caterer.</p>
  <p class="aside">met at a trade fair in January 2026 → pilot at the Amsterdam office in May → a three-office contract in September
  (98 % complete deliveries, by 09:00, a monthly report) → the first hard renewal talk in 2027. Big, scheduled, invoiced orders
  stretch Grace's ordering flow, Ana's architecture and Sanne's Rotterdam plan.</p>"""

# Story timeline: (sort key, month label, [(text, href or None, book tag)]). Book tags: "s" story event, "1" book 1, "2" book 2 …
TIMELINE = [
    ("2025-10", "Oct 2025", [("Ana and Grace join", None, "s"), ("Stakeholder map", "../architect-1/notes/stakeholder-map.html", "1"),
                             ("Customer interviews, 14–24 Oct", "../product-1/notes/customer-interviews.html", "2"),
                             ("Event storming, 21 Oct", "../architect-1/notes/event-storming.html", "1"),
                             ("Business drivers, 24 Oct", "../architect-1/notes/business-drivers.html", "1"),
                             ("Jobs to be done, 27 Oct", "../product-1/notes/jobs-to-be-done.html", "2"),
                             ("Proto-personas, 29 Oct", "../product-1/notes/proto-personas.html", "2"),
                             ("System context", "../architect-1/notes/system-context.html", "1")]),
    ("2025-11", "Nov 2025", [("ASRs, 3 Nov", "../architect-1/notes/asr.html", "1"),
                             ("Journey map, 3 Nov", "../product-1/notes/journey-map.html", "2"),
                             ("Quality scenarios, 5 Nov", "../architect-1/notes/quality-attribute-scenarios.html", "1"),
                             ("Problem statement, 7 Nov", "../product-1/notes/problem-statements.html", "2"),
                             ("NFR checklist, 10 Nov", "../architect-1/notes/nfr-checklist.html", "1"),
                             ("Opportunity tree, 10 Nov", "../product-1/notes/opportunity-solution-tree.html", "2"),
                             ("Assumption map, 12 Nov", "../product-1/notes/assumption-mapping.html", "2"),
                             ("Outcomes over outputs, 17 Nov", "../product-1/notes/outcomes-over-outputs.html", "2"),
                             ("Bounded contexts", "../architect-1/notes/bounded-contexts.html", "1"),
                             ("StockPilot spike, 19 Nov", "../architect-1/notes/spike-prototype-poc.html", "1"),
                             ("North star, 19 Nov", "../product-1/notes/north-star-metric.html", "2"),
                             ("Constraints &amp; assumptions, 24 Nov", "../architect-1/notes/constraints-assumptions.html", "1"),
                             ("Leading vs lagging, 24 Nov", "../product-1/notes/leading-lagging.html", "2"),
                             ("Baseline, 26 Nov", "../product-1/notes/baseline.html", "2")]),
    ("2025-12", "Dec 2025", [("Hypothesis H1, 1 Dec", "../product-1/notes/hypotheses.html", "2"),
                             ("Fake door, 3–17 Dec", "../product-1/notes/fake-door.html", "2"),
                             ("Risk-storming, 4 Dec", "../architect-1/notes/risk-storming.html", "1"),
                             ("Styles compared", "../architect-1/notes/architecture-styles.html", "1"),
                             ("Modular monolith, ADR 0002, 8 Dec", "../architect-1/notes/modular-monolith.html", "1"),
                             ("Concierge test at Noord, 8–19 Dec", "../product-1/notes/concierge-mvp.html", "2")]),
    ("2026-01", "Jan 2026", [("Sanne joins; Femke meets Korenwolf at a trade fair", None, "s"),
                             ("Prototype test, 13–22 Jan", "../product-1/notes/prototype-testing.html", "2"),
                             ("Walking skeleton, 15 Jan", "../architect-1/notes/walking-skeleton.html", "1"),
                             ("Fitness functions", "../architect-1/notes/fitness-functions.html", "1"),
                             ("Strategy on a page, 19–26 Jan", "../product-2/notes/strategy-on-a-page.html", "2")]),
    ("2026-02", "Feb 2026", [("RICE scoring for Q2, 2 Feb", "../product-2/notes/rice-ice-scoring.html", "2"),
                             ("Now / next / later roadmap, 6 Feb", "../product-2/notes/now-next-later.html", "2"),
                             ("Sizing Larder for Business, 9 Feb", "../product-2/notes/opportunity-sizing.html", "2"),
                             ("Cost of delay: the flag goes first, 9 Feb", "../product-2/notes/cost-of-delay.html", "2"),
                             ("Business case for approvals, 12 Feb", "../product-2/notes/business-case.html", "2"),
                             ("Kano survey, 16–20 Feb", "../product-2/notes/kano-model.html", "2"),
                             ("Saying no to recipe ideas, 25 Feb", "../product-2/notes/saying-no.html", "2")]),
    ("2026-03", "Mar 2026", [("Mo joins", None, "s"),
                             ("Request triage starts, 2 Mar", "../product-2/notes/request-triage.html", "2"),
                             ("Rotterdam app scope (MoSCoW), 3 Mar", "../product-2/notes/moscow.html", "2"),
                             ("Roadmap vs release plan, 9 Mar", "../product-2/notes/roadmap-vs-release-plan.html", "2"),
                             ("Testing Femke's banner, 10–17 Mar", "../product-2/notes/hippo.html", "2"),
                             ("ADR 0007: the outbox, 14 Mar", "../architect-2/notes/adr.html", "1"),
                             ("Decision log, 16 Mar", "../architect-2/notes/decision-log.html", "1"),
                             ("RFC-003: Dispatch as a service, 18–27 Mar", "../architect-2/notes/rfcs-design-docs.html", "1"),
                             ("DACI for a second PSP, 23 Mar", "../architect-2/notes/decision-rights.html", "1"),
                             ("Outcome roadmap for the board, 23 Mar", "../product-2/notes/outcome-roadmaps.html", "2"),
                             ("Opportunity cost of office ordering, 25 Mar", "../product-2/notes/opportunity-cost.html", "2"),
                             ("Rotterdam trade-off sliders, 31 Mar", "../architect-2/notes/trade-off-sliders.html", "1")]),
    ("2026-04", "Apr 2026", [("Dispatch on managed containers, ADR 0010, 8 Apr", "../architect-2/notes/cloud-service-model.html", "1"),
                             ("31 decisions sorted into doors, 9 Apr", "../architect-2/notes/one-way-two-way-doors.html", "1"),
                             ("Approvals live in Amsterdam, 13 Apr", None, "s"),
                             ("Korenwolf pilot options, ADR 0011, 13 Apr", "../architect-2/notes/options-analysis.html", "1"),
                             ("Bets, not promises, for the board, 16 Apr", "../product-2/notes/bets-not-promises.html", "2"),
                             ("Antwerp decision calendar, 20 Apr", "../architect-2/notes/last-responsible-moment.html", "1"),
                             ("Rotterdam opens, 27 Apr", None, "s")]),
    ("2026-05", "May 2026", [("Korenwolf pilot, Amsterdam office, from 4 May", None, "s"),
                             ("Routing engine bake-off, 11–22 May", "../architect-2/notes/technology-evaluation.html", "1")]),
    ("2026-06", "Jun 2026", [("Buy business billing, ADR 0013, 8 Jun", "../architect-2/notes/build-vs-buy.html", "1"),
                             ("Technical debt register, 15 Jun", "../architect-2/notes/tech-debt-register.html", "1"),
                             ("First Larder tech radar, 22 Jun", "../architect-2/notes/technology-radar.html", "1")]),
    ("2026-07", "Jul 2026", [("StockPilot exit plan, 6 Jul", "../architect-2/notes/exit-plans.html", "1")]),
    ("2026-09", "Sep 2026", [("Korenwolf signs for three offices", None, "s"),
                             ("Decision review, ADR 0014 proposed, 21 Sep", "../architect-2/notes/revisiting-decisions.html", "1")]),
    ("2027", "2027", [("Utrecht, The Hague, Eindhoven", None, "s"), ("Antwerp: the first city abroad", None, "s"), ("Korenwolf renewal", None, "s")]),
]

# ------------------------------------------------------------------ doodles
cities = Doodle(760, 400, "Doodle map of Larder's six-city plan. Amsterdam, live since 2024, at the top. The Hague and Utrecht in 2027. Rotterdam opens on 27 April 2026. Eindhoven in 2027. Antwerp, in Belgium and the first city abroad, in 2027. Dotted lines connect them to Amsterdam.",
                "Six cities by the end of 2027: one live, one in April 2026, four in 2027, one of them abroad.")
cities.raw('<path class="d d-thin d-dash d-soft" d="M70 40 C 140 120, 150 220, 210 300 S 300 380, 330 392"/>')
cities.note(96, 120, "North Sea", "pen", size=17)
cities.raw('<path class="d d-thin d-dash d-soft" d="M300 300 C 400 296, 500 312, 600 300"/>')
cities.note(640, 296, "NL", "pen", size=16)
cities.note(640, 326, "BE", "pen", size=16)
pins = [("Amsterdam", 330, 60, "live · 2024", "green"), ("The Hague", 210, 150, "2027", "paper"), ("Utrecht", 400, 150, "2027", "paper"),
        ("Rotterdam", 250, 220, "27 Apr 2026", "y"), ("Eindhoven", 470, 270, "2027", "paper"), ("Antwerp", 300, 340, "2027 · abroad", "blue")]
for name, x, y, when, fill in pins:
    cities.icon("pin", x, y - 34, 0.6, fill=fill)
    cities.head(x + 36, y - 10, name, anchor="start", size=17)
    cities.note(x + 36, y + 14, when, "pen", anchor="start", size=16)

two_books = Doodle(760, 250, "Doodle of two notebooks open side by side on one desk, Ana's and Grace's. Both point at the same meeting, the event storming on 21 October. Ana's notebook asks how to build it; Grace's asks whether to build it, and for whom.",
                   "Same meetings, two notebooks: “how do we build it?” and “should we, and for whom?”")
two_books.icon("book", 40, 60, 2.0)
two_books.head(100, 210, "Ana's notebook", size=17)
two_books.note(100, 236, "how do we build it?", "pen", size=17)
two_books.icon("book", 600, 60, 2.0)
two_books.head(660, 210, "Grace's notebook", size=17)
two_books.note(660, 236, "should we? for whom?", "green", size=17)
two_books.box(270, 70, 220, 90, "event storming", "y", sub="21 Oct 2025", size=18, subsize=15)
two_books.arrow(172, 115, 264, 115, dash=True)
two_books.arrow(588, 115, 496, 115, dash=True)
two_books.note(380, 196, "the same scene, seen from both sides", "pen", size=17)
