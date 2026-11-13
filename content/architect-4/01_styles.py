# Series 2 · The Solution Architect's Notebook · Vol. 4 · Integration styles.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Choosing an Integration Style
is_problem = Doodle(760, 280, "Doodle of the first WMS B meeting in March 2027. The vendor offers four ways in: a shared database view, a nightly file, an API and webhooks. Ben wants the database view because it's quickest; Eli wants webhooks; Joost only wants stock to be right. Nobody has compared the styles against what Larder needs.",
                    "Four ways into WMS B, three favourites, and nobody has compared them against what Larder needs.")
for i, (t, who, f) in enumerate([("database view", "Ben: quickest", "pink"), ("nightly file", "", "paper"), ("API", "", "paper"), ("webhooks", "Eli", "blue")]):
    is_problem.box(20 + i * 186, 40, 166, 80, t, f, sub=who or " ", size=16)
is_problem.box(200, 160, 360, 60, "Joost: “just get stock right”", "y", size=15)
is_problem.note(380, 262, "styles chosen by taste, not by need", "red")

is_analogy = Doodle(760, 250, "Doodle of four ways two neighbours can share information: a shared notebook on the fence both write in, a letter in the post each night, a phone call when you need an answer, and a doorbell that rings when something happens. Each fits a different need.",
                     "Neighbours can share a notebook, post a letter, phone, or ring a doorbell. Each fits a different need.")
for i, (ic, t, s, f) in enumerate([("ledger", "shared notebook", "both write in it", "pink"), ("envelope", "nightly letter", "batch", "paper"), ("phone", "phone call", "ask, wait", "blue"), ("bell", "doorbell", "it happened", "green")]):
    x = 14 + i * 188
    is_analogy.icon(ic, x + 60, 14, 1.0)
    is_analogy.box(x, 96, 172, 80, t, f, sub=s, size=15, subsize=14)
is_analogy.note(380, 222, "each fits a different need", "pen")

is_how = Doodle(760, 370, "Larder's comparison for WMS B, 8 March 2027, by need. Stock changes must reach Larder within a minute: webhooks (events). Larder must tell WMS B about goods received and orders to pick, and know it worked: the API (request and response). Finance needs a daily reconciliation of every stock movement: a nightly file. The shared database view is ruled out: it couples Larder to WMS B's tables. Decision, ADR 0018: all three styles, each for one need, behind the Stock module's single adapter.",
                 "Pick the style per need, not per system: events for “it changed”, API for “do this”, a file for “all of yesterday”.")
for i, (need, style, f) in enumerate([("stock changed (< 1 min)", "webhooks → events", "green"), ("pick this, goods received", "API, request + reply", "blue"),
                                      ("all of yesterday, for finance", "nightly file", "paper"), ("read their tables", "✗ shared database", "pink")]):
    y = 16 + i * 74
    is_how.box(14, y, 340, 60, need, "y", size=15, rx=6)
    is_how.arrow(358, y + 30, 404, y + 30)
    is_how.box(408, y, 338, 60, style, f, size=15, rx=6, stroke="red" if f == "pink" else "")
is_how.note(380, 330, "ADR 0018 · all behind the Stock module's one adapter", "pen", size=17)

STYLE = dict(
    slug="integration-style",
    kicker="a.k.a. “notebook, letter, phone or doorbell”",
    tldr="There are four basic ways for systems to share information: a <b>shared database</b>, <b>file transfer</b>, <b>remote calls</b> (APIs) and <b>messaging</b> (events). Each fits a different need. Choose <b>per need, not per system</b>: “tell me when it changes” wants events; “do this and tell me if it worked” wants an API; “all of yesterday” wants a file; a shared database almost always couples you too tightly. One integration can, and often should, use more than one style.",
    chips=[("Family", "integration styles"), ("Origin", "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003)"), ("Lives in", "the ADR for each integration"), ("Pairs with", "anti-corruption layer, event-driven integration, batch &amp; file transfer")],
    problem_side="Larder, 8 March 2027",
    problem="""  <p class="lead">The warehouse move to <b>WMS B</b> (ADR 0016) starts with an integration meeting. The vendor offers four ways in: a <b>database view</b>, a <b>nightly file</b>, an <b>API</b> and <b>webhooks</b>. Ben likes the database view (“quickest”); Eli likes webhooks; Joost just wants stock to be right. <span class="hl-pink">Each person picks by taste</span>, and nobody has written down what Larder actually needs from WMS B.</p>
  <ul>
    <li>One style for everything forces some needs into the wrong shape.</li>
    <li>The quickest option (a shared database) creates the tightest coupling.</li>
    <li>The style is picked before the needs are listed.</li>
  </ul>""",
    problem_figs=[is_problem],
    analogy_side="four ways to share with a neighbour",
    analogy="""  <p>Two neighbours can share information four ways: a <b>shared notebook</b> on the fence they both write in (until one tears out a page), a <b>letter</b> in the post each night (everything at once, a day late), a <b>phone call</b> when one needs an answer now, or a <b>doorbell</b> that rings when something happens. Sensible neighbours use several, each for what it's good at.</p>""",
    analogy_figs=[is_analogy],
    map=[("The shared notebook", "Shared database: both systems use the same tables"),
         ("A nightly letter", "File transfer: a batch, on a schedule"),
         ("A phone call", "Remote call (API): ask and wait for the answer"),
         ("A doorbell", "Messaging (events): “this happened”"),
         ("Using several", "One integration, a style per need")],
    how_side="list the needs, pick a style per need",
    how="""  <p>Ana listed what Larder needs from WMS B and picked per need. <b>Stock changes</b> must arrive within a minute: <b>webhooks</b>, turned into Larder events. Larder must <b>tell WMS B</b> what to pick and what arrived, and know it worked: the <b>API</b>. Finance needs <b>all of yesterday's movements</b> to reconcile: a <b>nightly file</b>. The database view was ruled out: Larder would depend on WMS B's tables. All three sit behind the Stock module's one adapter (ADR 0018).</p>""",
    how_figs=[is_how],
    steps=[("List the needs first", "What must flow, in which direction, how fast, and what happens if it fails."),
           ("Match each need to a style", "Changed → events. Do this → API. All of a period → file. Shared tables → almost never."),
           ("Check the vendor's options", "What they really support, with limits (rate, size, retries)."),
           ("Mix styles where needed", "One integration often needs two or three."),
           ("Hide it behind one adapter", "So the rest of the system sees one interface."),
           ("Record it", "An ADR per integration: needs, styles, why not the others.")],
    vocab=[("Shared database", "Two systems reading and writing the same tables."),
           ("File transfer", "Exchanging files on a schedule (batch)."),
           ("Remote procedure call", "Calling another system and waiting for the answer (APIs)."),
           ("Messaging", "Sending messages or events through a broker or webhooks."),
           ("Coupling", "How much one system depends on another's internals."),
           ("Webhook", "An HTTP call a system makes to you when something happens.")],
    code=dict(file="docs/adr/0018-wms-b-integration.md", note="ADR 0018, the needs table", plain=True, src="""
# 18. Integrate WMS B with a style per need, behind the Stock adapter
Status: Accepted · 2027-03-08 · Driver: Ana · with Eli, Ben, Cho (finance flows), Joost

| Need                                   | Direction  | Speed     | Style                  |
|----------------------------------------|------------|-----------|------------------------|
| Stock level changed                    | WMS → us   | < 1 min   | webhooks → stock.changed |
| Pick list for an order; goods received | us → WMS   | seconds   | API (request + reply)  |
| All stock movements of the day         | WMS → us   | by 06:00  | nightly file (SFTP)    |
| Read WMS B's tables directly           | —          | —         | rejected: couples us to |
|                                        |            |           | their schema           |

Consequences: three mechanisms to run; one adapter in the Stock module hides them
(as ADR 0005 did for StockPilot). Webhooks can be missed → the nightly file reconciles.
"""),
    tools="tools: the Enterprise Integration Patterns catalogue (enterpriseintegrationpatterns.com); OpenAPI for APIs, AsyncAPI for events, plain SFTP or object storage for files.",
    gains=["<b>Each need gets the right shape</b>: speed, confirmation, completeness.",
           "<b>Loose coupling</b>: no shared tables.",
           "<b>Safety nets</b>: the nightly file catches missed events.",
           "<b>Clear reasoning</b> in the ADR.",
           "<b>Swappable later</b> behind one adapter."],
    losses=["<b>Several mechanisms</b> to build and run.",
            "<b>More to monitor</b>: webhooks, API, files.",
            "<b>Consistency between styles</b> needs care.",
            "<b>More upfront thinking</b> than “just use the API”."],
    baseline="Each line compares <b>picking one integration style by taste</b> to <b>listing the needs and choosing a style per need, behind one adapter</b>.",
    ratings=[(2, 4, "The ADR says which style serves which need."),
             (2, 4, "Joost's need (stock right) drove the choice."),
             (3, 4, "A needs table settles the debate quickly."),
             (2, 4, "Missed events are caught by the nightly file."),
             (2, 5, "No shared tables; everything behind one adapter."),
             (2, 4, "ADR 0018 records needs and styles."),
             (3, 3, "Three mechanisms cost a little more to run."),
             (3, 3, "More to build than one style."),
             (3, 4, "Teams use the adapter, not WMS B directly.")],
    pitfalls=[("Shared database as a shortcut", "Reading the vendor's tables.", "never couple to another system's schema."),
              ("One style for all", "Polling the API every second for changes.", "events for changes; API for commands."),
              ("No reconciliation", "A missed webhook means wrong stock forever.", "a periodic full comparison (the nightly file)."),
              ("Style before needs", "“We'll use webhooks” before listing needs.", "list needs, then match styles.")],
    use=["Every new integration with another system or vendor.",
         "Reviewing an integration that keeps breaking.",
         "Vendor selection: which styles do they support?",
         "Replacing a shared-database integration."],
    skip=["Calls inside one module.",
          "Trivial one-off data loads."],
    related=["<b>Anti-corruption layer</b> (this volume)", "<b>Event-driven integration</b> (this volume)", "<b>Batch &amp; file transfer</b> (this volume)", "<b>Publish–subscribe</b> (patterns, Vol. 1)"],
    quiz=[("What are the four integration styles?", "Shared database, file transfer, remote calls (APIs), messaging (events)."),
          ("Which style fits “tell me when stock changes”?", "Messaging: events, here via webhooks."),
          ("Why was the database view rejected?", "It couples Larder to WMS B's internal tables."),
          ("Why keep the nightly file if there are webhooks?", "To reconcile: webhooks can be missed.")],
    try_it="Pick an integration you own. List every need (what, which direction, how fast, what if it fails) in a table, and write the best style next to each. Compare with what you use today and circle the mismatches.",
    remember="Notebook, letter, phone or <span class=\"hl\">doorbell</span>: pick a style <span class=\"hl\">per need</span>.",
    sources=["Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003).",
             "Martin Fowler, “Integration Database” and “Application Database” (martinfowler.com).",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed. (2021), on integration.",
             "AsyncAPI and OpenAPI specifications."],
)

# ------------------------------------------------------------------ 02 API-First Design
af_problem = Doodle(760, 280, "Doodle of March 2027: Korenwolf's facilities team wants to order pantry top-ups from their own facilities system. Ben's team starts coding an API from Larder's internal order model. Korenwolf's IT sees it only when it's finished: field names they don't understand, no cost centre, and a different idea of an order.",
                    "Built from the inside out, shown when finished: the client can't use it.")
af_problem.box(20, 40, 300, 90, "Ben's team", "blue", sub="codes from the internal model")
af_problem.arrow(326, 85, 430, 85, label="4 weeks", lx=378, ly=72)
af_problem.box(436, 30, 304, 110, "Korenwolf IT", "pink", sub="“no cost centre? what's a pick_ref?”", stroke="red", subsize=14)
af_problem.note(380, 200, "the contract was an afterthought", "red", size=20)

af_analogy = Doodle(760, 250, "Doodle of a new building's floor plan agreed with the tenants before construction: where the doors, sockets and windows go. Changing the plan costs an eraser; changing the built wall costs a builder.",
                     "Agree the floor plan with the tenants before building: an eraser now, or a builder later.")
af_analogy.icon("frame", 40, 50, 1.4)
af_analogy.box(170, 50, 270, 90, "the plan", "green", sub="change it: an eraser")
af_analogy.box(470, 50, 270, 90, "the built wall", "pink", sub="change it: a builder")
af_analogy.note(450, 210, "agree the plan with the people who'll live there", "pen")

af_how = Doodle(760, 360, "Larder's API-first process for the Business API, March 2027. One: write the contract first as an OpenAPI file, in the client's words: standing orders, cost centres, deliveries. Two: review it with Korenwolf's IT and Mo, as a pull request. Three: publish a mock server so Korenwolf can build against it immediately. Four: build the real thing to pass the same contract tests. Two weeks of contract work, then both sides built in parallel.",
                 "Contract first, reviewed with the client, a mock to build against, and the real thing tested against the same contract.")
for i, (t, s, f) in enumerate([("1 · contract", "OpenAPI, client's words", "y"), ("2 · review", "Korenwolf IT + Mo", "blue"), ("3 · mock", "they build now", "paper"), ("4 · build", "same contract tests", "green")]):
    x = 10 + i * 188
    af_how.box(x, 40, 172, 100, t, f, sub=s, size=17, subsize=13)
    if i < 3:
        af_how.arrow(x + 174, 90, x + 186, 90)
af_how.box(80, 190, 600, 80, None, "paper", dash=True)
af_how.text(380, 222, "POST /business/v1/standing-orders", "t-head", size=16)
af_how.text(380, 250, "{ office, cost_centre, items[], delivery_window }", size=15)
af_how.note(380, 318, "2 weeks on the contract, then both sides in parallel", "pen", size=17)

API_FIRST = dict(
    slug="api-first",
    kicker="a.k.a. “agree the floor plan first”",
    tldr="When an API is built first and described afterwards, it mirrors the builder's internals, and clients find out too late. <b>API-first</b> reverses the order: write the <b>contract</b> (OpenAPI) first, in the <b>consumer's language</b>; <b>review it with the consumers</b>; publish a <b>mock</b> so they can start building; then implement and test against the <b>same contract</b>. Changing a contract costs an edit; changing a shipped API costs everyone.",
    chips=[("Family", "integration styles"), ("Origin", "contract-first design; OpenAPI (formerly Swagger, 2011–); “API design first” practice"), ("Lives in", "an OpenAPI file in the repo, reviewed as a pull request"), ("Pairs with", "API versioning strategy, backend for frontend, solution design document")],
    problem_side="Larder, 15 March 2027",
    problem="""  <p class="lead">Korenwolf's facilities team wants to top up pantry orders from <b>their own facilities system</b>, not by emailing Mo. Ben's team starts building an API straight from Larder's internal order model. Four weeks later Korenwolf's IT sees it for the first time: field names like <code>pick_ref</code>, <b>no cost centre</b>, and a different idea of what an order is. <span class="hl-pink">The contract was an afterthought</span>, and now it has to change.</p>
  <ul>
    <li>Inside-out APIs expose internal names and shapes.</li>
    <li>Consumers find problems after the work is done.</li>
    <li>Both sides work in sequence instead of in parallel.</li>
  </ul>""",
    problem_figs=[af_problem],
    analogy_side="the floor plan",
    analogy="""  <p>Before a building goes up, the <b>floor plan</b> is agreed with the people who'll live there: where the doors, sockets and windows go. Moving a door on the plan costs an <b>eraser</b>; moving it in a built wall costs a <b>builder</b>. And while the walls go up, the tenants can already order furniture that fits.</p>""",
    analogy_figs=[af_analogy],
    map=[("The floor plan", "The OpenAPI contract"),
         ("The tenants", "Korenwolf's IT and Mo"),
         ("Moving a door on paper", "Editing the contract in review"),
         ("Ordering furniture early", "Korenwolf building against the mock"),
         ("The building inspector", "Contract tests on the real implementation")],
    how_side="contract, review, mock, build",
    how="""  <p>Ana and Ben restarted with the contract: <code>/business/v1</code> in Korenwolf's words (standing orders, cost centres, offices, delivery windows), opened as a pull request with Korenwolf's IT lead and Mo as reviewers. A <b>mock server</b> went up the same week, so Korenwolf built their side in parallel. The real API passed the same contract tests and went live in May (ADR 0019).</p>""",
    how_figs=[af_how],
    steps=[("Name the consumers and their tasks", "Who calls it, to do what, in their words."),
           ("Write the contract first", "OpenAPI: resources, fields, errors, examples. No code yet."),
           ("Review it with consumers", "As a pull request; their names for things win."),
           ("Publish a mock", "Generated from the contract, so they can build now."),
           ("Implement against the contract", "Contract tests in CI; the contract is the source of truth."),
           ("Version from day one", "<code>/v1</code> in the path, and a policy for changes.")],
    vocab=[("API-first", "Designing the contract before the implementation."),
           ("Contract", "The agreed description of an API: endpoints, fields, errors."),
           ("OpenAPI", "A standard format for describing HTTP APIs."),
           ("Mock server", "A fake API generated from the contract."),
           ("Contract test", "A test that the implementation matches the contract."),
           ("Consumer", "A system or team that calls the API.")],
    code=dict(file="api/business/openapi.yaml", note="the start of the Business API contract (excerpt)", plain=True, src="""
openapi: 3.1.0
info: { title: Larder Business API, version: 1.0.0 }
paths:
  /business/v1/standing-orders:
    post:
      summary: Create or replace an office's weekly standing order
      requestBody:
        content:
          application/json:
            schema: { $ref: "#/components/schemas/StandingOrder" }
            example:
              office: KW-AMS-HQ
              cost_centre: "4100-FAC"
              delivery_window: { day: TUE, from: "07:00", to: "09:00" }
              items: [ { sku: "FRT-APPLE-1KG", quantity: 12 } ]
      responses:
        "201": { description: Created }
        "422": { description: Unknown office, item or cost centre }
"""),
    tools="tools: OpenAPI with an editor (Stoplight, Swagger Editor), mock servers (Prism), contract tests (Schemathesis, Dredd, Pact for consumer-driven contracts), linting (Spectral).",
    gains=["<b>Consumers shape the API</b> in their language.",
           "<b>Problems found on paper</b>, not after building.",
           "<b>Parallel work</b> via the mock.",
           "<b>One source of truth</b>: the contract.",
           "<b>Docs for free</b>, generated from the contract."],
    losses=["<b>Upfront time</b> before code starts.",
            "<b>Contract and code can drift</b> without tests.",
            "<b>Over-design</b> if every field is debated.",
            "<b>Needs consumers available</b> to review."],
    baseline="Each line compares <b>building an API from the internal model and describing it afterwards</b> to <b>a contract written first, reviewed with consumers, mocked, then implemented against tests</b>.",
    ratings=[(2, 5, "The API speaks Korenwolf's language."),
             (2, 5, "Korenwolf's IT and Mo reviewed it before any code."),
             (3, 4, "Disagreements settled on paper."),
             (2, 4, "Mismatches found in review, not after release."),
             (3, 4, "The contract is versioned from day one."),
             (2, 4, "The contract and ADR 0019 are in the repo."),
             (3, 3, "Neutral."),
             (3, 3, "Two weeks of contract work up front."),
             (2, 4, "Both sides build in parallel.")],
    pitfalls=[("Contract after code", "The OpenAPI file is generated from the implementation.", "write it first; generate code or tests from it."),
              ("Internal names", "<code>pick_ref</code>, <code>ord_ln</code>.", "use the consumer's words."),
              ("No mock", "Consumers wait for the real thing.", "publish a mock the day the contract is agreed."),
              ("No contract tests", "Code and contract drift apart.", "test the implementation against the contract in CI.")],
    use=["APIs used by other teams or clients.",
         "Partner and B2B integrations.",
         "When consumers and providers can build in parallel.",
         "Public or long-lived APIs."],
    skip=["Internal calls inside one module.",
          "Throwaway prototypes."],
    related=["<b>API versioning strategy</b> (this volume)", "<b>Backend for frontend</b> (this volume)", "<b>Solution design document done right</b> (Vol. 3)", "<b>Consumer-driven contracts</b> (patterns, Vol. 4)"],
    quiz=[("What's written first in API-first design?", "The contract (e.g. an OpenAPI file), before any implementation."),
          ("Whose language should the contract use?", "The consumer's."),
          ("What does a mock server allow?", "Consumers to build against the API before it's implemented."),
          ("How do you keep code and contract aligned?", "Contract tests in CI.")],
    try_it="For the next API another team will call, write the OpenAPI contract with one example per endpoint before any code. Open it as a pull request with the consumer as reviewer, publish a mock, and note what changed in review.",
    remember="Agree the <span class=\"hl\">floor plan</span> with the tenants. An <span class=\"hl\">eraser</span>, not a builder.",
    sources=["OpenAPI Initiative, OpenAPI Specification 3.1.",
             "Arnaud Lauret, <i>The Design of Web APIs</i> (2019).",
             "James Higginbotham, <i>Principles of Web API Design</i> (2021).",
             "Pact documentation, consumer-driven contract testing."],
)

# ------------------------------------------------------------------ 03 Event-Driven Integration
ev_problem = Doodle(760, 280, "Doodle of the week after Utrecht opened in April 2027. Ordering renamed a field in the order placed event, from store to store_id. Nine consumers read that event. Billing broke silently for two days; nobody knew who consumed what.",
                    "One renamed field in order.placed, nine consumers, and billing broken silently for two days.")
ev_problem.box(20, 100, 200, 80, "order.placed", "y", sub="store → store_id")
for i in range(9):
    x, y = 300 + (i % 3) * 150, 30 + (i // 3) * 74
    ev_problem.box(x, y, 130, 50, "billing ✗" if i == 4 else f"consumer {i + 1}", "pink" if i == 4 else "paper", size=14, rx=6, stroke="red" if i == 4 else "")
ev_problem.line("M286 30 Q 276 30 276 50 V 120 Q 276 140 266 140 Q 276 140 276 160 V 230 Q 276 250 286 250", thin=True)
ev_problem.arrow(224, 140, 262, 140, dash=True)
ev_problem.note(530, 270, "nobody knew who consumed what", "red")

ev_analogy = Doodle(760, 250, "Doodle of a newspaper and its subscribers. The paper publishes; it doesn't know every reader. But it keeps its sections in the same place, announces changes in advance, and never moves the TV listings without warning.",
                     "A newspaper publishes to readers it doesn't know, so it keeps the format stable and announces changes.")
ev_analogy.icon("newspaper", 40, 50, 1.6)
for i, (t, s, f) in enumerate([("same sections", "stable format", "green"), ("notice of changes", "in advance", "y"), ("reader list", "who subscribes", "blue")]):
    ev_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, size=16, subsize=14)
ev_analogy.note(450, 210, "publish freely, change carefully", "pen")

ev_how = Doodle(760, 360, "Larder's event rules from 19 April 2027. Every event has an owner, a schema in a schema registry and a page in the event catalogue listing its consumers. Changes must be backward compatible: add optional fields, never rename or remove; a breaking change means a new event version published alongside the old one for three months. CI checks compatibility against the registry before a producer can deploy.",
                 "Owner, schema registry, catalogue of consumers, compatible changes only, and CI that checks before deploy.")
for i, (t, s, f) in enumerate([("owner", "one team per event", "y"), ("registry", "every schema, versioned", "blue"), ("catalogue", "who consumes what", "green")]):
    ev_how.box(14 + i * 248, 20, 236, 90, t, f, sub=s)
ev_how.box(14, 140, 360, 120, None, "green")
ev_how.head(194, 172, "allowed", size=17)
ev_how.text(194, 206, "add an optional field", size=15)
ev_how.text(194, 234, "add a new event", size=15)
ev_how.box(386, 140, 360, 120, None, "pink")
ev_how.head(566, 172, "breaking → new version", size=17)
ev_how.text(566, 206, "rename · remove · retype", size=15)
ev_how.text(566, 234, "v1 and v2 side by side, 3 months", size=15)
ev_how.note(380, 300, "CI checks compatibility before a producer deploys", "pen", size=17)
ev_how.note(380, 334, "ADR 0020", "green", size=17)

EVENTS = dict(
    slug="event-driven-integration",
    kicker="a.k.a. “the newspaper and its readers”",
    tldr="Events let a producer announce “this happened” without knowing who listens, which is exactly what makes them easy to break. Treat events as <b>published contracts</b>: every event has an <b>owner</b>, a <b>schema in a registry</b>, and a <b>catalogue entry</b> listing its consumers. Allow only <b>backward-compatible changes</b> (add optional fields); a breaking change means a <b>new version</b> published alongside the old one for a while. Let <b>CI check compatibility</b> before a producer deploys.",
    chips=[("Family", "integration styles"), ("Origin", "event-driven architecture; schema registries (Confluent, 2015–); AsyncAPI (2017–)"), ("Lives in", "the schema registry and docs/events/, one page per event"), ("Pairs with", "integration style, canonical data model, transactional outbox")],
    problem_side="Larder, 19 April 2027",
    problem="""  <p class="lead">Utrecht opened on 12 April; the city work had added more consumers to Larder's events. Then Ordering <b>renamed one field</b> in <code>order.placed</code>, from <code>store</code> to <code>store_id</code>, a tidy-up. <b>Nine consumers</b> read that event. <b>Billing</b> failed silently for two days: business invoices missed their store, and nobody noticed until Mo's monthly check. <span class="hl-pink">Nobody knew who consumed what.</span></p>
  <ul>
    <li>Producers don't know their consumers, so they can't warn them.</li>
    <li>Schemas live in code, so changes aren't reviewed as contracts.</li>
    <li>Breaks are silent: events still flow, just wrong.</li>
  </ul>""",
    problem_figs=[ev_problem],
    analogy_side="the newspaper",
    analogy="""  <p>A newspaper publishes to readers it doesn't know. So it keeps its <b>sections in the same place</b>, announces format changes <b>in advance</b>, and keeps a <b>subscriber list</b>. It can add a new supplement any day; it doesn't move the TV listings to the sports pages overnight.</p>""",
    analogy_figs=[ev_analogy],
    map=[("The newspaper", "The producer: Ordering, owner of order.placed"),
         ("Readers", "The nine consumers"),
         ("Sections in the same place", "A stable schema in the registry"),
         ("A new supplement", "An added optional field, or a new event"),
         ("The subscriber list", "The event catalogue: who consumes what")],
    how_side="contracts, a registry, compatible changes",
    how="""  <p>ADR 0020 set the rules. Every event has <b>one owner</b>, a schema in a <b>schema registry</b> and a page in the <b>event catalogue</b> listing its consumers. Only <b>backward-compatible</b> changes are allowed; a rename means <code>order.placed.v2</code>, published alongside v1 for three months while consumers move. <b>CI checks compatibility</b> against the registry, so the <code>store_id</code> rename would now fail the build.</p>""",
    how_figs=[ev_how],
    steps=[("Give every event an owner", "The producing team owns the schema and its changes."),
           ("Register every schema", "In a schema registry (Avro, JSON Schema, Protobuf), versioned."),
           ("Catalogue the consumers", "One page per event: owner, schema, consumers, examples."),
           ("Allow compatible changes only", "Add optional fields; never rename, remove or retype."),
           ("Version breaking changes", "New version alongside the old; a dated end for the old one."),
           ("Check in CI", "Compatibility check before a producer can deploy.")],
    vocab=[("Event", "A record that something happened, published for others."),
           ("Producer / consumer", "Who publishes / who listens."),
           ("Schema registry", "A store of event schemas with compatibility checks."),
           ("Backward compatible", "Old consumers keep working after the change."),
           ("Event catalogue", "The list of events, owners and consumers."),
           ("AsyncAPI", "A format for describing event-driven APIs.")],
    code=dict(file="docs/events/order.placed.md", note="event catalogue page (excerpt)", plain=True, src="""
# order.placed                        owner: Ordering (Ben) · schema: registry, v1 + v2

Meaning     A customer or business order was accepted at checkout.
Published   via the outbox (ADR 0007) to topic orders.placed
Versions    v1 (field: store)     deprecated 19 Apr 2027, removed 19 Jul 2027
            v2 (field: store_id)  current
Consumers   Fulfilment · Dispatch · Billing · Stock · Customer Care · Analytics ·
            Business reports · Notifications · Fraud checks   (9; Billing on v1 until 3 May)
Rules       compatible changes only (add optional fields); CI checks the registry
Example     { "order_id": "o_81c2", "store_id": "UTR-1", "total": 41.80, ... }
"""),
    tools="tools: a schema registry (Confluent Schema Registry, Apicurio, AWS Glue), AsyncAPI for docs, an event catalogue (EventCatalog, Backstage), compatibility checks in CI.",
    gains=["<b>No silent breaks</b>: incompatible changes fail CI.",
           "<b>Producers know their consumers</b>.",
           "<b>Safe evolution</b>: add fields freely; version breaks.",
           "<b>Onboarding</b>: one page per event.",
           "<b>Loose coupling kept loose</b>."],
    losses=["<b>Registry and CI checks</b> to set up.",
            "<b>Two versions at once</b> during migrations.",
            "<b>Catalogue upkeep</b> as consumers change.",
            "<b>Slower tidy-ups</b>: renames need a version."],
    baseline="Each line compares <b>events as fields in code, changed freely by producers</b> to <b>events as owned, registered contracts with a consumer catalogue and compatibility checks</b>.",
    ratings=[(2, 4, "One page per event says what it means and who uses it."),
             (3, 3, "Mostly between engineering teams."),
             (3, 3, "Neutral."),
             (1, 5, "Breaking changes fail the build."),
             (2, 4, "Fields can be added safely; versions for breaks."),
             (2, 4, "Versions and consumers on record."),
             (3, 3, "Neutral."),
             (3, 3, "A registry and a CI step to run."),
             (2, 4, "Teams change events without coordinating every time.")],
    pitfalls=[("Unowned events", "Anyone edits order.placed.", "one owner per event."),
              ("Silent renames", "A tidy-up breaks billing.", "renames are breaking: new version."),
              ("Forever versions", "v1, v2 and v3 all live for years.", "a dated end for old versions."),
              ("No consumer list", "Nobody to warn.", "catalogue consumers; ask on subscribe.")],
    use=["Events consumed by more than one team.",
         "Integrations with vendors via webhooks turned into events.",
         "Growing event-driven systems.",
         "After the first silent break."],
    skip=["Events inside one module.",
          "Short-lived prototypes."],
    related=["<b>Choosing an integration style</b> (this volume)", "<b>Canonical data model (and its traps)</b> (this volume)", "<b>Transactional outbox</b> (patterns, Vol. 1)", "<b>Architecture decision records</b> (Vol. 2)"],
    quiz=[("What makes events easy to break?", "Producers don't know their consumers, and changes look like internal tidy-ups."),
          ("Which changes are backward compatible?", "Adding optional fields or new events."),
          ("How do you make a breaking change?", "Publish a new version alongside the old one, with a dated end."),
          ("What would have caught the store_id rename?", "A compatibility check against the schema registry in CI.")],
    try_it="List your three most-used events. For each, write the owner and every consumer you can find, then register the schema and add a compatibility check to the producer's CI. Count how many consumers nobody knew about.",
    remember="Publish like a <span class=\"hl\">newspaper</span>: keep the sections still, announce changes, know your <span class=\"hl\">readers</span>.",
    sources=["Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003).",
             "Martin Fowler, “What do you mean by Event-Driven?” (2017).",
             "Confluent documentation, “Schema Evolution and Compatibility”.",
             "AsyncAPI Initiative, AsyncAPI Specification."],
)

# ------------------------------------------------------------------ 04 Batch & File Transfer
bf_problem = Doodle(760, 280, "Doodle of finance in May 2027: Marco's team downloads the payment providers' daily settlement files by hand, pastes them into a spreadsheet and matches them with orders. One day a file arrived twice and was counted twice; another day it was late and nobody noticed for a week.",
                    "Settlement files downloaded by hand: one counted twice, one a week late, and nobody noticed.")
bf_problem.icon("receipt", 40, 40, 1.4)
bf_problem.box(140, 40, 260, 80, "download by hand", "paper", sub="2 providers, daily")
bf_problem.box(440, 30, 300, 50, "file twice → counted twice", "pink", size=13, stroke="red")
bf_problem.box(440, 100, 300, 50, "late file → seen a week later", "pink", size=13, stroke="red")
bf_problem.note(380, 220, "the most boring integration, the most expensive errors", "red", size=18)

bf_analogy = Doodle(760, 250, "Doodle of a bank's night safe. Shops drop sealed, numbered bags overnight. In the morning the bank counts each bag once, checks the number against the slip, and calls any shop whose bag didn't arrive.",
                     "A bank's night safe: numbered bags, counted once, checked against the slip, and a call if one is missing.")
bf_analogy.icon("vault", 40, 50, 1.4)
for i, (t, s, f) in enumerate([("numbered bag", "one per shop, per day", "y"), ("counted once", "even if dropped twice", "blue"), ("missing? call", "by 10:00", "pink")]):
    bf_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, size=16, subsize=13)
bf_analogy.note(450, 210, "boring, reliable, checked", "pen")

bf_how = Doodle(760, 360, "Larder's settlement file pipeline, May 2027. Each provider drops a daily file by 05:00. A job picks it up, checks the checksum and the row count in the trailer, and records the file name so the same file is never loaded twice. Rows load into a staging table, then are matched with orders. If a file hasn't arrived by 07:00, an alert goes to finance and on-call. Mismatches go to a short daily report for Marco's team.",
                 "Arrive, check, load once, match, and shout if it's late. Batch done properly is boring.")
for i, (t, s, f) in enumerate([("file by 05:00", "SFTP, per provider", "paper"), ("check", "checksum + row count", "y"), ("load once", "file name recorded", "blue"), ("match", "with orders", "green")]):
    x = 10 + i * 188
    bf_how.box(x, 40, 172, 100, t, f, sub=s, size=16, subsize=13)
    if i < 3:
        bf_how.arrow(x + 174, 90, x + 186, 90)
bf_how.box(14, 180, 360, 80, "late after 07:00?", "pink", sub="alert finance + on-call")
bf_how.box(386, 180, 360, 80, "mismatches", "y", sub="a daily report for Marco")
bf_how.note(380, 310, "idempotent, checked, monitored", "green", size=18)

BATCH = dict(
    slug="batch-file-transfer",
    kicker="a.k.a. “the bank's night safe”",
    tldr="Files on a schedule are the oldest integration style, and still the right one for <b>“all of yesterday”</b>: settlements, reconciliations, reports, bulk loads. Do it properly: a <b>known arrival time</b>, <b>checks</b> (checksum, row count, a trailer), <b>load each file exactly once</b> (record what you've loaded), stage before applying, <b>alert when a file is late or wrong</b>, and report mismatches to the people who act on them.",
    chips=[("Family", "integration styles"), ("Origin", "file transfer, the first of Hohpe and Woolf's integration styles; decades of banking practice"), ("Lives in", "a scheduled job with monitoring, owned by a named team"), ("Pairs with", "integration style, idempotency, SaaS &amp; vendor integration")],
    problem_side="Larder, 10 May 2027",
    problem="""  <p class="lead">Every morning someone in Marco's finance team downloads the two payment providers' <b>settlement files</b> by hand, pastes them into a spreadsheet and matches them with orders. In April one file <b>arrived twice</b> and was counted twice; in May a file was <b>a day late</b> and nobody noticed for a week. <span class="hl-pink">The most boring integration</span> was causing the most expensive errors.</p>
  <ul>
    <li>Manual file handling fails quietly: duplicates, gaps, wrong days.</li>
    <li>Nobody owns “the file didn't come”.</li>
    <li>Batch gets less design attention than APIs, though money flows through it.</li>
  </ul>""",
    problem_figs=[bf_problem],
    analogy_side="the bank's night safe",
    analogy="""  <p>Shops drop their takings in a bank's <b>night safe</b>: sealed, <b>numbered bags</b>, one per shop per day. In the morning the bank <b>counts each bag once</b> (even if a shop dropped it twice by mistake), checks it against the slip, and <b>calls any shop whose bag didn't arrive</b> by 10:00. Nobody finds out at the end of the month.</p>""",
    analogy_figs=[bf_analogy],
    map=[("A numbered bag", "A settlement file with a date and provider in its name"),
         ("Checked against the slip", "Checksum and row count in the trailer"),
         ("Counted once", "File names recorded: never loaded twice"),
         ("A call by 10:00", "An alert if the file isn't there by 07:00"),
         ("The morning count", "Matching settlements with orders, mismatches reported")],
    how_side="arrive, check, load once, alert",
    how="""  <p>Cho and Eli built the pipeline in a week. Providers drop files by <b>05:00</b>; a job checks the <b>checksum and row count</b>, records the file name so it's <b>never loaded twice</b>, stages the rows and matches them with orders. No file by <b>07:00</b> means an alert to finance and on-call. Marco's team now reads a <b>one-page mismatch report</b> instead of building a spreadsheet; the same pattern later took WMS B's nightly stock file.</p>""",
    how_figs=[bf_how],
    steps=[("Agree the contract", "File name pattern, format, columns, trailer with row count, arrival time."),
           ("Check before loading", "Checksum, row count, date in the name, schema."),
           ("Load exactly once", "Record each file processed; ignore repeats."),
           ("Stage, then apply", "Load into a staging table; apply only if checks pass."),
           ("Alert on late or bad files", "A deadline per file; alert the owner and on-call."),
           ("Report mismatches to who acts", "A short daily report, not a dump.")],
    vocab=[("Batch", "Processing a set of records together, on a schedule."),
           ("Settlement file", "A provider's list of payments paid out, per day."),
           ("Idempotent load", "Loading the same file twice has the same effect as once."),
           ("Trailer", "A last line with totals or a row count, for checking."),
           ("Staging table", "A temporary table to check data before applying it."),
           ("Reconciliation", "Matching two records of the same thing.")],
    code=dict(file="jobs/settlements/README.md", note="the settlement file contract and job (excerpt)", plain=True, src="""
# Settlement files · owner: Cho (payments) · alerts: finance + on-call

Arrival     SFTP /in/settlements/ by 05:00 CET, one file per provider per day
Name        {provider}_settlement_{YYYY-MM-DD}.csv     e.g. psp1_settlement_2027-05-09.csv
Trailer     last line: TRAILER,<row_count>,<sum_amount_cents>
Job 05:15   1 already loaded? (processed_files table) → skip, log
            2 checksum, row count and sum match the trailer? → else quarantine + alert
            3 load into staging_settlements; match with orders and refunds
            4 write mismatches to the daily report (finance channel, 08:00)
Deadline    07:00 · no file → alert "psp1 settlement missing for 2027-05-09"
"""),
    tools="tools: SFTP or object storage drops, a scheduler (cron, Airflow, a cloud scheduler), a processed-files table, checksum tools, alerts in your monitoring.",
    gains=["<b>No double counting</b>: each file loaded once.",
           "<b>Missing files noticed</b> by 07:00, not a week later.",
           "<b>Bad files quarantined</b>, not applied.",
           "<b>Finance freed</b> from manual downloads.",
           "<b>A reusable pattern</b> for every file integration."],
    losses=["<b>Latency</b>: yesterday's data, by design.",
            "<b>Another job to run</b> and monitor.",
            "<b>Vendors change formats</b> without warning.",
            "<b>Not for real-time needs</b>."],
    baseline="Each line compares <b>settlement files downloaded and pasted by hand</b> to <b>a scheduled, checked, load-once file pipeline with late-file alerts and a mismatch report</b>.",
    ratings=[(2, 4, "One job, one contract, one report."),
             (2, 4, "Finance and payments agree the file contract."),
             (3, 3, "Neutral."),
             (1, 5, "Duplicates and missing files can't slip through."),
             (3, 3, "Neutral."),
             (2, 4, "Every file processed is recorded."),
             (2, 4, "Money mismatches surface daily."),
             (2, 4, "No manual downloads."),
             (2, 4, "Finance reads a report instead of building one.")],
    pitfalls=[("Loading twice", "The same file counted twice.", "record processed files; skip repeats."),
              ("No deadline", "A missing file noticed a week later.", "an arrival time and an alert."),
              ("Applying unchecked", "A half-written file loaded.", "checksum, row count, staging first."),
              ("Dumping everything", "A 4,000-row report nobody reads.", "report only mismatches, to who acts.")],
    use=["Settlements, reconciliations, reports, bulk loads.",
         "Vendors that only offer files.",
         "Safety nets for event integrations.",
         "Large volumes where real time isn't needed."],
    skip=["Anything that must be seen within minutes: use events.",
          "Commands that need an answer: use an API."],
    related=["<b>Choosing an integration style</b> (this volume)", "<b>SaaS &amp; vendor integration</b> (this volume)", "<b>Idempotency keys</b> (patterns, Vol. 1)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)"],
    quiz=[("When is file transfer the right style?", "For “all of a period”: settlements, reconciliations, bulk loads."),
          ("How do you avoid loading a file twice?", "Record each processed file and skip repeats."),
          ("What's a trailer for?", "A row count and totals to check the file is complete."),
          ("What happens if a file is late?", "An alert at a set deadline, to the owner and on-call.")],
    try_it="Find a file your team or finance receives regularly. Write its contract (name, arrival time, trailer), then check: would a duplicate be loaded twice? Would a missing file be noticed today? Fix the worse of the two.",
    remember="Numbered <span class=\"hl\">bags</span>, counted once, and a <span class=\"hl\">call</span> by 10:00 if one's missing.",
    sources=["Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003), “File Transfer”.",
             "Martin Kleppmann, <i>Designing Data-Intensive Applications</i> (2017), batch processing.",
             "Ralph Kimball and Joe Caserta, <i>The Data Warehouse ETL Toolkit</i> (2004).",
             "Michael Nygard, <i>Release It!</i>, 2nd ed. (2018), on integration points."],
)

NOTES = [STYLE, API_FIRST, EVENTS, BATCH]
