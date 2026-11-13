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
    ("Book 1", "The Solution Architect's Notebook", "Ana", "Oct 2025 → Sep 2028", "complete: 6 volumes",
     "How Ana turns a one-line brief into an architecture that can grow to six cities: understanding the problem, finding the "
     "requirements that matter, choosing first shapes, testing risky ideas early, then recording decisions and living with them.",
     "../architect-1/index.html"),
    ("Book 2", "The Product Owner's Notebook", "Grace", "Oct 2025 → Dec 2027", "complete: 6 volumes",
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
    ("2025-10", "Oct 2025", [('Ana and Grace join', None, 's'),
                             ('Stakeholder map', '../architect-1/notes/stakeholder-map.html', '1'),
                             ('System context', '../architect-1/notes/system-context.html', '1'),
                             ('Customer interviews, 14–24 Oct', '../product-1/notes/customer-interviews.html', '2'),
                             ('Event storming, 21 Oct', '../architect-1/notes/event-storming.html', '1'),
                             ('Business drivers, 24 Oct', '../architect-1/notes/business-drivers.html', '1'),
                             ('Jobs to be done, 27 Oct', '../product-1/notes/jobs-to-be-done.html', '2'),
                             ('Proto-personas, 29 Oct', '../product-1/notes/proto-personas.html', '2')]),
    ("2025-11", "Nov 2025", [('Bounded contexts', '../architect-1/notes/bounded-contexts.html', '1'),
                             ('ASRs, 3 Nov', '../architect-1/notes/asr.html', '1'),
                             ('Journey map, 3 Nov', '../product-1/notes/journey-map.html', '2'),
                             ('Quality scenarios, 5 Nov', '../architect-1/notes/quality-attribute-scenarios.html', '1'),
                             ('Problem statement, 7 Nov', '../product-1/notes/problem-statements.html', '2'),
                             ('NFR checklist, 10 Nov', '../architect-1/notes/nfr-checklist.html', '1'),
                             ('Opportunity tree, 10 Nov', '../product-1/notes/opportunity-solution-tree.html', '2'),
                             ('Assumption map, 12 Nov', '../product-1/notes/assumption-mapping.html', '2'),
                             ('Outcomes over outputs, 17 Nov', '../product-1/notes/outcomes-over-outputs.html', '2'),
                             ('StockPilot spike, 19 Nov', '../architect-1/notes/spike-prototype-poc.html', '1'),
                             ('North star, 19 Nov', '../product-1/notes/north-star-metric.html', '2'),
                             ('Constraints &amp; assumptions, 24 Nov', '../architect-1/notes/constraints-assumptions.html', '1'),
                             ('Leading vs lagging, 24 Nov', '../product-1/notes/leading-lagging.html', '2'),
                             ('Baseline, 26 Nov', '../product-1/notes/baseline.html', '2')]),
    ("2025-12", "Dec 2025", [('Styles compared', '../architect-1/notes/architecture-styles.html', '1'),
                             ('Hypothesis H1, 1 Dec', '../product-1/notes/hypotheses.html', '2'),
                             ('Fake door, 3–17 Dec', '../product-1/notes/fake-door.html', '2'),
                             ('Risk-storming, 4 Dec', '../architect-1/notes/risk-storming.html', '1'),
                             ('Modular monolith, ADR 0002, 8 Dec', '../architect-1/notes/modular-monolith.html', '1'),
                             ('Concierge test at Noord, 8–19 Dec', '../product-1/notes/concierge-mvp.html', '2')]),
    ("2026-01", "Jan 2026", [('Sanne joins; Femke meets Korenwolf at a trade fair', None, 's'),
                             ('Fitness functions', '../architect-1/notes/fitness-functions.html', '1'),
                             ('Prototype test, 13–22 Jan', '../product-1/notes/prototype-testing.html', '2'),
                             ('Walking skeleton, 15 Jan', '../architect-1/notes/walking-skeleton.html', '1'),
                             ('Strategy on a page, 19–26 Jan', '../product-2/notes/strategy-on-a-page.html', '2')]),
    ("2026-02", "Feb 2026", [('RICE scoring for Q2, 2 Feb', '../product-2/notes/rice-ice-scoring.html', '2'),
                             ('Now / next / later roadmap, 6 Feb', '../product-2/notes/now-next-later.html', '2'),
                             ('Sizing Larder for Business, 9 Feb', '../product-2/notes/opportunity-sizing.html', '2'),
                             ('Cost of delay: the flag goes first, 9 Feb', '../product-2/notes/cost-of-delay.html', '2'),
                             ('Product trio: Grace, Noor and Ben, from 9 Feb', '../product-3/notes/product-trio.html', '2'),
                             ('Business case for approvals, 12 Feb', '../product-2/notes/business-case.html', '2'),
                             ('Kano survey, 16–20 Feb', '../product-2/notes/kano-model.html', '2'),
                             ('Story map for approvals, 16 Feb', '../product-3/notes/story-mapping.html', '2'),
                             ('User stories rewritten, 18 Feb', '../product-3/notes/user-stories.html', '2'),
                             ('Thin slices, 23 Feb', '../product-3/notes/thin-slices.html', '2'),
                             ('Saying no to recipe ideas, 25 Feb', '../product-2/notes/saying-no.html', '2'),
                             ('Example mapping, 25 Feb', '../product-3/notes/example-mapping.html', '2')]),
    ("2026-03", "Mar 2026", [('Mo joins', None, 's'),
                             ('Request triage starts, 2 Mar', '../product-2/notes/request-triage.html', '2'),
                             ('MVP or MLP? The swap screen, 2 Mar', '../product-3/notes/mvp-vs-mlp.html', '2'),
                             ('Rotterdam app scope (MoSCoW), 3 Mar', '../product-2/notes/moscow.html', '2'),
                             ('Definitions of ready and done, 4 Mar', '../product-3/notes/definition-ready-done.html', '2'),
                             ('Roadmap vs release plan, 9 Mar', '../product-2/notes/roadmap-vs-release-plan.html', '2'),
                             ("Testing Femke's banner, 10–17 Mar", '../product-2/notes/hippo.html', '2'),
                             ('ADR 0007: the outbox, 14 Mar', '../architect-2/notes/adr.html', '1'),
                             ('Decision log, 16 Mar', '../architect-2/notes/decision-log.html', '1'),
                             ('Pre-mortem for approvals, 16 Mar', '../product-3/notes/pre-mortem.html', '2'),
                             ('Sprint 7 goal, 16 Mar', '../product-3/notes/sprint-goals.html', '2'),
                             ('RFC-003: Dispatch as a service, 18–27 Mar', '../architect-2/notes/rfcs-design-docs.html', '1'),
                             ('DACI for a second PSP, 23 Mar', '../architect-2/notes/decision-rights.html', '1'),
                             ('Outcome roadmap for the board, 23 Mar', '../product-2/notes/outcome-roadmaps.html', '2'),
                             ('Refinement without the marathon, 23 Mar', '../product-3/notes/refinement.html', '2'),
                             ('Opportunity cost of office ordering, 25 Mar', '../product-2/notes/opportunity-cost.html', '2'),
                             ('Rotterdam launch checklist, 30 Mar', '../product-3/notes/launch-checklist.html', '2'),
                             ('Approvals staff test at Noord, 30 Mar', None, 's'),
                             ('Rotterdam trade-off sliders, 31 Mar', '../architect-2/notes/trade-off-sliders.html', '1')]),
    ("2026-04", "Apr 2026", [('Approvals dark launch and rollout, 6–20 Apr', '../product-3/notes/dark-launches.html', '2'),
                             ('Dispatch on managed containers, ADR 0010, 8 Apr', '../architect-2/notes/cloud-service-model.html', '1'),
                             ('31 decisions sorted into doors, 9 Apr', '../architect-2/notes/one-way-two-way-doors.html', '1'),
                             ('Approvals live in Amsterdam, 13 Apr', None, 's'),
                             ('Korenwolf pilot options, ADR 0011, 13 Apr', '../architect-2/notes/options-analysis.html', '1'),
                             ('Bets, not promises, for the board, 16 Apr', '../product-2/notes/bets-not-promises.html', '2'),
                             ('Antwerp decision calendar, 20 Apr', '../architect-2/notes/last-responsible-moment.html', '1'),
                             ('Rotterdam opens, 27 Apr', None, 's')]),
    ("2026-05", "May 2026", [('Korenwolf pilot, Amsterdam office, from 4 May', None, 's'),
                             ('Event tracking plan, 4 May', '../product-4/notes/event-tracking-plan.html', '2'),
                             ('Routing engine bake-off, 11–22 May', '../architect-2/notes/technology-evaluation.html', '1'),
                             ('Rotterdam hypercare ends, 11 May', '../product-3/notes/hypercare.html', '2'),
                             ('Swap funnel, step by step, 18 May', '../product-4/notes/funnels.html', '2')]),
    ("2026-06", "Jun 2026", [('Buy business billing, ADR 0013, 8 Jun', '../architect-2/notes/build-vs-buy.html', '1'),
                             ('Tech debt: 20 % agreed with Ben, 8 Jun', '../product-3/notes/tech-debt-talks.html', '2'),
                             ('Approvals in Rotterdam, comms first, 8 Jun', '../product-3/notes/release-notes.html', '2'),
                             ('Technical debt register, 15 Jun', '../architect-2/notes/tech-debt-register.html', '1'),
                             ('Ticket review, auto-refund closed, 15 Jun', '../product-4/notes/support-tickets-data.html', '2'),
                             ('Sample size for the 3-minute test, 15 Jun', '../product-4/notes/sample-size.html', '2'),
                             ('First Larder tech radar, 22 Jun', '../architect-2/notes/technology-radar.html', '1'),
                             ('A/B test: 3-minute window, 22 Jun', '../product-4/notes/ab-tests.html', '2'),
                             ('Board slide without vanity numbers, 22 Jun', '../product-4/notes/vanity-metrics.html', '2'),
                             ('Q3 OKRs: customers trust every order, 29 Jun', '../product-4/notes/okrs.html', '2')]),
    ("2026-07", "Jul 2026", [('StockPilot exit plan, 6 Jul', '../architect-2/notes/exit-plans.html', '1'),
                             ('Cohorts after a swap, 6 Jul', '../product-4/notes/cohorts-retention.html', '2'),
                             ('Approvals post-launch review, 6 Jul', '../product-4/notes/post-launch-review.html', '2'),
                             ('Reading the window test, 7 Jul', '../product-4/notes/reading-results.html', '2'),
                             ('A health page people open, 13 Jul', '../product-4/notes/dashboards.html', '2'),
                             ('Feedback loop with the stores, 20 Jul', '../product-4/notes/operations-feedback.html', '2')]),
    ("2026-08", "Aug 2026", [('Live updates trip a guardrail, 24 Aug', '../product-4/notes/guardrail-metrics.html', '2')]),
    ("2026-09", "Sep 2026", [('Korenwolf signs for three offices', None, 's'),
                             ('Decision review, ADR 0014 proposed, 21 Sep', '../architect-2/notes/revisiting-decisions.html', '1'),
                             ('Customer advisory panel meets, 21 Sep', '../product-4/notes/advisory-panel.html', '2'),
                             ('Slot waitlist sunset agreed, 21 Sep', '../product-4/notes/killing-a-feature.html', '2')]),
    ("2026-10", "Oct 2026", [('Slot waitlist switched off, 5 Oct', None, 's'),
                             ('A weekly update people read, 5 Oct', '../product-5/notes/product-update.html', '2'),
                             ('C4 diagrams replace eleven, 6 Oct', '../architect-3/notes/c4-model.html', '1'),
                             ('One-page PRD: business standing orders, 12 Oct', '../product-5/notes/one-page-prd.html', '2'),
                             ('Views for Lena, Joost, Ben and Eli, 13 Oct', '../architect-3/notes/views-viewpoints.html', '1'),
                             ('No surprises for Priya, 19 Oct', '../product-5/notes/managing-up.html', '2'),
                             ('Whiteboard: vans in Dispatch, 20 Oct', '../architect-3/notes/whiteboard-sessions.html', '1'),
                             ('The standing-order sequence, 27 Oct', '../architect-3/notes/sequence-flow.html', '1')]),
    ("2026-11", "Nov 2026", [('Standing-orders demo at Noord, 06:00, 2 Nov', '../product-5/notes/demos.html', '2'),
                             ('Deployment diagram after an incident, 3 Nov', '../architect-3/notes/deployment-diagrams.html', '1'),
                             ('Live timeline: privacy agreed with Lena, 9 Nov', '../product-5/notes/legal-privacy.html', '2'),
                             ('Architecture one-pager for the board, 10 Nov', '../architect-3/notes/architecture-one-pager.html', '1'),
                             ('Korenwolf dependency board, 16 Nov', '../product-5/notes/dependencies.html', '2'),
                             ('arc42 skeleton, 17 Nov', '../architect-3/notes/arc42.html', '1'),
                             ('Korenwolf scope agreed, 23 Nov', '../product-5/notes/negotiating-scope.html', '2'),
                             ('Docs as code, 24 Nov', '../architect-3/notes/docs-as-code.html', '1'),
                             ('Order-editing pitch to Femke, 30 Nov', '../product-5/notes/pitching-to-ceo.html', '2')]),
    ("2026-12", "Dec 2026", [('Korenwolf solution design, 1–18 Dec', '../architect-3/notes/solution-design-document.html', '1'),
                             ("Cut line for Korenwolf's go-live, 1 Dec", '../product-5/notes/fixed-date.html', '2'),
                             ('Swap refunds will miss 2 %: told early, 7 Dec', '../product-5/notes/bad-news.html', '2'),
                             ('Warehouse decision for executives, 9 Dec', '../architect-3/notes/presenting-to-executives.html', '1'),
                             ('Checkout down 38 minutes at the Christmas peak, 18 Dec', None, 's')]),
    ("2027-01", "Jan 2027", [('Korenwolf: three offices live', None, 's'),
                             ('Korenwolf live in three offices, 4 Jan', None, 's'),
                             ('Q4 review: 45 minutes, three decisions, 11 Jan', '../product-5/notes/quarterly-review.html', '2'),
                             ('99.99 %? Explaining the trade-off, 12 Jan', '../architect-3/notes/explaining-trade-offs.html', '1'),
                             ('Grace and Ana meet weekly, 12 Jan', '../product-5/notes/working-with-architect.html', '2'),
                             ('The picker app gets its own outcomes, 18 Jan', '../product-5/notes/operations-as-customer.html', '2'),
                             ('First architecture kata: Antwerp, 19 Jan', '../architect-3/notes/architecture-katas.html', '1'),
                             ('Living diagrams find a hidden call, 26 Jan', '../architect-3/notes/living-diagrams.html', '1')]),
    ("2027-02", "Feb 2027", [('Architecture roadmap for 2027, 2 Feb', '../architect-3/notes/architecture-roadmap.html', '1'),
                             ('Glossary after the Korenwolf report, 9 Feb', '../architect-3/notes/glossary.html', '1'),
                             ('Seventeen Korenwolf requests reviewed, 22 Feb', '../product-5/notes/account-managers.html', '2')]),
    ("2027-03", "Mar 2027", [('Capability map for 2027, 1 Mar', '../architect-4/notes/capability-map.html', '1'),
                             ('Larder Plus decided; Grace commits, 1 Mar', '../product-5/notes/disagree-and-commit.html', '2'),
                             ('WMS B: a style per need, ADR 0018, 8 Mar', '../architect-4/notes/integration-style.html', '1'),
                             ('Business API, contract first, 15 Mar', '../architect-4/notes/api-first.html', '1'),
                             ('Anti-corruption layer for WMS B, 22 Mar', '../architect-4/notes/anti-corruption-layer.html', '1'),
                             ('Warehouse move, store by store, 29 Mar', '../architect-4/notes/strangler-fig.html', '1')]),
    ("2027-04", "Apr 2027", [('City playbook for Utrecht, 5 Apr', '../product-6/notes/launching-new-city.html', '2'),
                             ('Utrecht opens, 12 Apr', None, 's'),
                             ('Zuid moves to WMS B, 19 Apr', None, 's'),
                             ('Event contracts after a silent break, 19 Apr', '../architect-4/notes/event-driven-integration.html', '1')]),
    ("2027-05", "May 2027", [('Settlement files done properly, 10 May', '../architect-4/notes/batch-file-transfer.html', '1'),
                             ('One identity per person, ADR 0021, 24 May', '../architect-4/notes/identity-federation.html', '1'),
                             ('Business API live; Noord moves to WMS B, 24 May', None, 's')]),
    ("2027-06", "Jun 2027", [('Backends for frontends, ADR 0022, 7 Jun', '../architect-4/notes/backend-for-frontend.html', '1'),
                             ("Business portal's first month, 7 Jun", '../product-6/notes/business-self-service.html', '2'),
                             ('The Hague opens on WMS B, 14 Jun', None, 's'),
                             ('Larder Plus price test, 14 Jun', '../product-6/notes/pricing-experiments.html', '2'),
                             ('API versioning policy, 21 Jun', '../architect-4/notes/api-versioning.html', '1')]),
    ("2027-07", "Jul 2027", [('No canonical order, ADR 0023, 5 Jul', '../architect-4/notes/canonical-data-model.html', '1'),
                             ('Offices vs households: one core, 5 Jul', '../product-6/notes/b2b-vs-b2c.html', '2'),
                             ('Application portfolio (TIME), 19 Jul', '../architect-4/notes/application-portfolio.html', '1'),
                             ('Substitutions become a platform, 19 Jul', '../product-6/notes/platform-thinking.html', '2'),
                             ('Utrecht moves to WMS B, 26 Jul', None, 's')]),
    ("2027-08", "Aug 2027", [('One master per kind of data, ADR 0024, 2 Aug', '../architect-4/notes/data-ownership.html', '1'),
                             ('Antwerp testers: localised, not translated, 2 Aug', '../product-6/notes/localisation.html', '2'),
                             ('Transition states and old bridges, 16 Aug', '../architect-4/notes/transition-architectures.html', '1'),
                             ('Accessibility audit: 41 issues, 16 Aug', '../product-6/notes/accessibility.html', '2')]),
    ("2027-09", "Sep 2027", [('Vendor integration checklist, 6 Sep', '../architect-4/notes/saas-integration.html', '1'),
                             ('First orders that bring customers back, 6 Sep', '../product-6/notes/product-led-growth.html', '2'),
                             ("Korenwolf's Monday request, 13 Sep", '../product-6/notes/account-needs-vs-vision.html', '2'),
                             ('StockPilot switched off, 15 Sep', None, 's')]),
    ("2027-10", "Oct 2027", [('Will Christmas hold? One page, 4 Oct', '../architect-5/notes/back-of-envelope.html', '1'),
                             ('Service levels in the portal, 4 Oct', '../product-6/notes/service-levels-as-features.html', '2'),
                             ('Security review of business ordering, 11 Oct', '../architect-5/notes/security-architecture-review.html', '1'),
                             ('Six product principles, 11 Oct', '../product-6/notes/product-principles.html', '2'),
                             ('Capacity plan for the peak, 18 Oct', '../architect-5/notes/capacity-planning.html', '1'),
                             ('Antwerp opens, 18 Oct', None, 's'),
                             ("Where are Belgian customers' data? 25 Oct", '../architect-5/notes/data-classification.html', '1'),
                             ("Grace's own Antwerp order, 25 Oct", '../product-6/notes/product-sense.html', '2')]),
    ("2027-11", "Nov 2027", [('Load profiles: the push spike, 1 Nov', '../architect-5/notes/load-profiles.html', '1'),
                             ('Belgian rules as platform features, 8 Nov', '../architect-5/notes/compliance-by-design.html', '1'),
                             ('Two years: a review, 8 Nov', '../product-6/notes/growing-as-po.html', '2'),
                             ('Performance budgets, 15 Nov', '../architect-5/notes/performance-budgets.html', '1'),
                             ('Eindhoven opens, 22 Nov', None, 's'),
                             ('Hiring a business product owner, 22 Nov', '../product-6/notes/hiring-a-po.html', '2'),
                             ('Availability maths for Korenwolf, 29 Nov', '../architect-5/notes/availability-maths.html', '1')]),
    ("2027-12", "Dec 2027", [('Korenwolf renews: 99.8 % a month', None, 's'),
                             ('Failure mode analysis of checkout, 6 Dec', '../architect-5/notes/failure-mode-analysis.html', '1'),
                             ('Handing Larder for Business to Jonas, 13 Dec', '../product-6/notes/handing-over.html', '2'),
                             ('PSP slows; switched in 40 s, 17 Dec', None, 's')]),
    ("2028-01", "Jan 2028", [('DR tiers after a 3 h 40 restore, 10 Jan', '../architect-5/notes/dr-tiers.html', '1'),
                             ('One region, with triggers, ADR 0026, 24 Jan', '../architect-5/notes/multi-region.html', '1')]),
    ("2028-02", "Feb 2028", [('Routing TCO: keep Engine A, 7 Feb', '../architect-5/notes/total-cost-of-ownership.html', '1'),
                             ('Cloud bill €78k → €58k, 21 Feb', '../architect-5/notes/cost-aware-architecture.html', '1')]),
    ("2028-03", "Mar 2028", [('Platform carbon for Korenwolf, 6 Mar', '../architect-5/notes/green-software.html', '1'),
                             ('Utility tree for 2028, 20 Mar', '../architect-5/notes/utility-tree.html', '1')]),
    ("2028-04", "Apr 2028", [('Eight architecture principles, 3 Apr', '../architect-6/notes/architecture-principles.html', '1'),
                             ("Ordering's own database: two weeks of design, 10 Apr", '../architect-6/notes/just-enough-design.html', '1'),
                             ('Guardrails replace the review board, 17 Apr', '../architect-6/notes/guardrails-not-gates.html', '1'),
                             ('2028 risk register, 24 Apr', '../architect-6/notes/risk-register.html', '1')]),
    ("2028-05", "May 2028", [('Golden path for new services, 8 May', '../architect-6/notes/golden-paths.html', '1'),
                             ('First lightweight review: search, 15 May', '../architect-6/notes/lightweight-review.html', '1'),
                             ('How Larder evolves, 22 May', '../architect-6/notes/evolutionary-architecture.html', '1'),
                             ('Ordering migration plan, 29 May', '../architect-6/notes/migration-planning.html', '1')]),
    ("2028-06", "Jun 2028", [('Ghent readiness criteria, 12 Jun', '../architect-6/notes/go-live-readiness.html', '1'),
                             ('Ghent opens, 19 Jun', None, 's')]),
    ("2028-07", "Jul 2028", [('Station lockers discovery workshop, 3 Jul', '../architect-6/notes/discovery-workshops.html', '1'),
                             ('Haarlem date negotiated, 17 Jul', '../architect-6/notes/negotiating-with-stakeholders.html', '1')]),
    ("2028-08", "Aug 2028", [('Retiring the old export, without escalation, 7 Aug', '../architect-6/notes/influencing-without-authority.html', '1'),
                             ('One architecture backlog, 21 Aug', '../architect-6/notes/architecture-backlog.html', '1'),
                             ('Ordering migration done, 21 Aug', None, 's')]),
    ("2028-09", "Sep 2028", [('Ordering handed to the reliability team, 4 Sep', '../architect-6/notes/handover-to-operations.html', '1'),
                             ('Haarlem opens: eight cities, 11 Sep', None, 's'),
                             ('Growing two more architects, 18 Sep', '../architect-6/notes/growing-architects.html', '1')]),
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
