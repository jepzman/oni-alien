# Series 2 · The Solution Architect's Notebook · Vol. 4 · Boundaries.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 Anti-Corruption Layer
ac_problem = Doodle(760, 280, "Doodle of March 2027, two weeks into the WMS B work. WMS B's words are spreading into Larder: Ordering has started storing WMS B's article_id, Fulfilment talks about waves, and a picker screen shows bin codes. Larder's own model, products, store locations and pick lists, is being replaced by the vendor's.",
                    "Two weeks in, the vendor's words are spreading: article_id in Ordering, “waves” in Fulfilment, bin codes on a picker screen.")
ac_problem.box(20, 30, 220, 200, None, "y")
ac_problem.head(130, 60, "WMS B", size=18)
for i, t in enumerate(["article", "bin", "wave"]):
    ac_problem.text(130, 100 + i * 36, t, size=16)
for i, (mod, leak) in enumerate([("Ordering", "article_id"), ("Fulfilment", "“waves”"), ("picker app", "bin codes")]):
    y = 30 + i * 74
    ac_problem.box(440, y, 300, 60, f"{mod}: {leak}", "pink", size=15, stroke="red")
    ac_problem.arrow(244, 130, 436, y + 30, color="red", dash=True)
ac_problem.note(380, 264, "the vendor's model is taking over ours", "red")

ac_analogy = Doodle(760, 250, "Doodle of an embassy interpreter. Delegations speak their own languages; the interpreter at the border of the meeting translates both ways, so nobody has to learn the other language and nothing gets lost in a half-understood word.",
                     "An embassy interpreter: each side keeps its own language; translation happens at the border.")
ac_analogy.box(20, 60, 220, 90, "delegation A", "blue", sub="its own language")
ac_analogy.box(290, 50, 180, 110, "interpreter", "green", sub="both ways")
ac_analogy.box(520, 60, 220, 90, "delegation B", "y", sub="its own language")
ac_analogy.arrow(244, 105, 286, 105, both=True)
ac_analogy.arrow(474, 105, 516, 105, both=True)
ac_analogy.note(380, 220, "nobody learns the other's language", "pen")

ac_how = Doodle(760, 360, "Larder's anti-corruption layer for WMS B, inside the Stock module's adapter. WMS B's article becomes a Larder product; a bin becomes a store location; a wave becomes a pick batch; WMS B's units of measure become items. WMS B webhooks are translated into stock.changed events in Larder's terms. Nothing outside the adapter mentions WMS B. A fitness function fails the build if any other module imports the WMS B client.",
                 "Translate at the border, both ways. Inside Larder, nobody says “article”, “bin” or “wave”.")
ac_how.box(14, 20, 220, 260, None, "y")
ac_how.head(124, 52, "WMS B", size=18)
for i, t in enumerate(["article", "bin", "wave", "unit of measure"]):
    ac_how.text(124, 98 + i * 44, t, size=15)
ac_how.box(270, 20, 220, 260, None, "green", stroke="green")
ac_how.head(380, 52, "ACL (adapter)", size=17)
for i in range(4):
    ac_how.arrow(300, 92 + i * 44, 460, 92 + i * 44)
ac_how.box(526, 20, 220, 260, None, "blue")
ac_how.head(636, 52, "Larder", size=18)
for i, t in enumerate(["product", "store location", "pick batch", "items"]):
    ac_how.text(636, 98 + i * 44, t, size=15)
ac_how.note(380, 318, "fitness function: only the adapter imports the WMS B client", "pen", size=16)
ac_how.note(380, 344, "webhooks → stock.changed, in Larder's words", "green", size=16)

ACL = dict(
    slug="anti-corruption-layer",
    kicker="a.k.a. “the embassy interpreter”",
    tldr="When you integrate with a system whose model differs from yours, its words and shapes tend to <b>leak</b> into your code until you're speaking the vendor's language everywhere. An <b>anti-corruption layer</b> is a thin translation layer at the border: it turns their concepts into yours (and back), so the rest of your system <b>never sees the other model</b>. Keep it in <b>one place</b>, and enforce that nothing else talks to the other system directly.",
    chips=[("Family", "boundaries"), ("Origin", "Eric Evans, <i>Domain-Driven Design</i> (2003)"), ("Lives in", "the integrating module's adapter, guarded by a fitness function"), ("Pairs with", "bounded contexts, integration style, strangler fig")],
    problem_side="Larder, 22 March 2027",
    problem="""  <p class="lead">Two weeks into the WMS B work, Ana reviews a few pull requests and finds the vendor's words everywhere. <b>Ordering</b> has started storing WMS B's <code>article_id</code>; <b>Fulfilment</b> talks about “waves”; a <b>picker screen</b> shows bin codes. <span class="hl-pink">The vendor's model is replacing Larder's own</span>: products, store locations, pick lists. In two years, leaving WMS B would mean rewriting half the system.</p>
  <ul>
    <li>Vendor concepts leak into every module that touches them.</li>
    <li>Your own domain language erodes, and with it, clarity.</li>
    <li>Every leak is another place to change when you leave.</li>
  </ul>""",
    problem_figs=[ac_problem],
    analogy_side="the embassy interpreter",
    analogy="""  <p>At a meeting between two delegations, an <b>interpreter</b> sits at the border of the conversation and translates both ways. Each side keeps speaking its <b>own language</b>; nobody has to learn the other's, and nothing gets lost in a half-understood word. If one delegation changes, only the interpreter needs to adapt.</p>""",
    analogy_figs=[ac_analogy],
    map=[("The interpreter", "The anti-corruption layer in the Stock adapter"),
         ("Delegation A's language", "WMS B's model: article, bin, wave"),
         ("Delegation B's language", "Larder's model: product, store location, pick batch"),
         ("Translating both ways", "Commands out, webhooks in"),
         ("A new delegation", "Leaving WMS B: replace only the interpreter")],
    how_side="translate at the border, both ways",
    how="""  <p>The Stock module already had the only StockPilot adapter (ADR 0005); Ana made the WMS B adapter an explicit <b>anti-corruption layer</b>. It translates <b>article → product</b>, <b>bin → store location</b>, <b>wave → pick batch</b>, WMS B's units → items, and turns webhooks into <code>stock.changed</code> in Larder's terms. The three leaks were rewritten; a fitness function now fails the build if any other module imports the WMS B client.</p>""",
    how_figs=[ac_how],
    steps=[("Name both models", "List the other system's concepts and yours, side by side."),
           ("Put one adapter at the border", "In the module that owns the integration; nowhere else."),
           ("Translate both ways", "Their concepts to yours on the way in; yours to theirs on the way out."),
           ("Publish in your own terms", "Events and APIs out of the adapter use only your language."),
           ("Guard the border", "A fitness function: nothing else imports the vendor client."),
           ("Review for leaks", "Search for the vendor's words in code reviews and docs.")],
    vocab=[("Anti-corruption layer", "A translation layer protecting your model from another system's."),
           ("Leak", "Another system's concepts appearing in your code."),
           ("Adapter", "Code that connects your system to another, in one place."),
           ("Bounded context", "An area where a model and its words have one meaning."),
           ("Published language", "The shared format both sides agree on at the border."),
           ("Translation", "Mapping one model's concepts to another's.")],
    code=dict(file="core/stock/adapters/wms_b/translate.py", note="part of the translation, shortened", plain=True, src="""
# The only place in Larder that knows WMS B's words.  (ADR 0018, fitness function FF-07)

def to_stock_changed(webhook: dict) -> StockChanged:
    \"\"\"WMS B 'article.qty.updated' → Larder 'stock.changed'.\"\"\"
    product = products.by_wms_article(webhook["article"]["code"])
    location = locations.by_wms_bin(webhook["bin"]["id"])
    items = units.to_items(webhook["qty"], webhook["uom"])   # e.g. 2 CRATE → 24 items
    return StockChanged(product_id=product.id, store_id=location.store_id,
                        location=location.code, available=items, source="wms_b")

def to_wms_pick_wave(batch: PickBatch) -> dict:
    \"\"\"Larder pick batch → WMS B 'wave'.\"\"\"
    return {"wave_ref": batch.id, "lines": [
        {"article": products.wms_article(l.product_id), "qty": l.items, "uom": "EA"}
        for l in batch.lines]}
"""),
    tools="tools: a module boundary and an adapter package; import-linter or ArchUnit rules to keep vendor clients inside it; contract tests against the vendor sandbox.",
    gains=["<b>Your language stays yours</b>: products, not articles.",
           "<b>Leaving is cheap</b>: replace the adapter only.",
           "<b>Vendor changes stay local</b>.",
           "<b>Clearer code</b> for everyone outside the adapter.",
           "<b>Enforceable</b> with a fitness function."],
    losses=["<b>Translation code</b> to write and test.",
            "<b>Some concepts don't map neatly</b> (units of measure).",
            "<b>A little latency</b> and indirection.",
            "<b>Temptation to bypass</b> “just this once”."],
    baseline="Each line compares <b>using the vendor's model wherever it's needed</b> to <b>an anti-corruption layer translating at the border, with nothing else talking to the vendor</b>.",
    ratings=[(2, 5, "Larder's code speaks Larder's language."),
             (3, 3, "Mostly an engineering concern."),
             (3, 3, "Neutral."),
             (2, 4, "Vendor changes can't ripple through the system."),
             (2, 5, "Leaving WMS B means replacing one adapter."),
             (3, 4, "One file says how every concept maps."),
             (2, 4, "The exit plan's cost stays low."),
             (3, 3, "Translation code to maintain."),
             (2, 4, "Teams use Larder's events, not the vendor's API.")],
    pitfalls=[("Leaky adapter", "The adapter passes WMS B objects straight through.", "translate every field into your model."),
              ("Several adapters", "Ordering and Fulfilment each call WMS B.", "one adapter, guarded by a fitness function."),
              ("Vendor words in events", "<code>stock.changed</code> carries <code>article_id</code>.", "publish only your own terms."),
              ("Forcing a fit", "Pretending units of measure are always items.", "translate explicitly; record the odd cases.")],
    use=["Integrating with vendors and SaaS.",
         "Legacy systems you're migrating away from.",
         "Partners whose model differs from yours.",
         "Any external model you don't control."],
    skip=["Two contexts that really share a language.",
          "Short-lived integrations you'll delete soon."],
    related=["<b>Bounded contexts</b> (Vol. 1)", "<b>Strangler fig migration</b> (this volume)", "<b>Exit plans &amp; reversibility</b> (Vol. 2)", "<b>Choosing an integration style</b> (this volume)"],
    quiz=[("What does an anti-corruption layer protect?", "Your own model and language from another system's."),
          ("Where should it live?", "In one adapter, in the module that owns the integration."),
          ("How do you stop it being bypassed?", "A fitness function that fails the build if others import the vendor client."),
          ("What changes when you leave the vendor?", "Only the adapter.")],
    try_it="Search your codebase for one vendor's names (their field names, their concepts). Count the modules they appear in. Pick the integration with the most leaks and sketch the single adapter and translation table that would contain them.",
    remember="Keep an <span class=\"hl\">interpreter</span> at the border. Nobody inside learns the <span class=\"hl\">vendor's</span> language.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), “Anti-Corruption Layer”.",
             "Vaughn Vernon, <i>Implementing Domain-Driven Design</i> (2013), context mapping.",
             "Microsoft Azure Architecture Center, “Anti-corruption Layer pattern”.",
             "Sam Newman, <i>Monolith to Microservices</i> (2019)."],
)

# ------------------------------------------------------------------ 06 Backend for Frontend
bff_problem = Doodle(760, 280, "Doodle of June 2027. The customer app's order screen makes seven calls to Larder Core over 4G and takes 2.8 seconds. The new business portal for office managers needs a completely different shape of data. Every change for one client risks breaking another, because all three clients share one general-purpose API.",
                     "Seven calls on 4G for one screen, a portal that needs other shapes, and one general API serving all.")
bff_problem.icon("phone", 30, 30, 1.6)
bff_problem.box(120, 30, 220, 80, "order screen", "pink", sub="7 calls · 2.8 s", stroke="red")
bff_problem.box(120, 140, 220, 80, "business portal", "y", sub="other shapes")
bff_problem.box(440, 80, 300, 90, "one general API", "blue", sub="Larder Core")
bff_problem.arrow(344, 70, 436, 115)
bff_problem.arrow(344, 180, 436, 135)
bff_problem.note(380, 262, "every change risks another client", "red")

bff_analogy = Doodle(760, 250, "Doodle of a restaurant kitchen with three pass windows: one for the dining room, plated beautifully; one for takeaway, packed in boxes; one for room service, on trays with covers. Same kitchen and food; each window prepares it for where it's going.",
                      "One kitchen, three windows: plated for the dining room, boxed for takeaway, on trays for room service.")
bff_analogy.icon("kitchen", 30, 70, 1.2)
for i, (t, s, f) in enumerate([("dining room", "plated", "y"), ("takeaway", "boxed", "blue"), ("room service", "on trays", "green")]):
    bff_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s)
bff_analogy.note(450, 210, "same food, shaped for where it goes", "pen")

bff_how = Doodle(760, 360, "Larder's backends for frontends from 7 June 2027. The mobile BFF, owned by Dee's team, gives the customer app one call per screen with small payloads. The business portal BFF, owned by Ben's team, serves office managers. The picker app keeps its own offline sync. Behind them, Larder Core's module APIs and Dispatch stay general. The order screen drops from seven calls and 2.8 seconds to one call and 0.6 seconds. ADR 0022.",
                  "One small backend per kind of client, owned by that client's team. The core stays general.")
for i, (t, s, f) in enumerate([("customer app", "Dee's team", "y"), ("business portal", "Ben's team", "y"), ("picker app", "offline sync", "y")]):
    bff_how.box(14 + i * 248, 14, 236, 70, t, f, sub=s)
for i, (t, f) in enumerate([("mobile BFF", "green"), ("portal BFF", "green"), ("sync service", "paper")]):
    bff_how.box(34 + i * 248, 116, 196, 56, t, f, size=16)
    bff_how.arrow(132 + i * 248, 88, 132 + i * 248, 112)
    bff_how.arrow(132 + i * 248, 176, 380, 222)
bff_how.box(160, 226, 440, 64, "Larder Core modules · Dispatch", "blue", size=16)
bff_how.note(380, 322, "order screen: 7 calls, 2.8 s → 1 call, 0.6 s", "green", size=17)
bff_how.note(380, 348, "ADR 0022", "pen", size=16)

BFF = dict(
    slug="backend-for-frontend",
    kicker="a.k.a. “three pass windows, one kitchen”",
    tldr="One general-purpose API serving every client becomes a compromise: chatty for mobile, wrong-shaped for portals, and risky to change. A <b>backend for frontend</b> (BFF) is a small backend <b>per kind of client</b>, shaped for exactly what that client's screens need, and <b>owned by that client's team</b>. The core services stay general; each BFF composes them. Use it when clients really differ, and keep BFFs thin: shaping, not business rules.",
    chips=[("Family", "boundaries"), ("Origin", "Sam Newman, “Backends For Frontends” (2015), from SoundCloud"), ("Lives in", "one small service per client type, owned by that client's team"), ("Pairs with", "API-first design, API versioning, modular monolith")],
    problem_side="Larder, 7 June 2027",
    problem="""  <p class="lead">Larder's clients have multiplied: the customer apps, the picker app, and since May a <b>business portal</b> where office managers manage standing orders. All share one general API in Larder Core. The customer app's <b>order screen</b> makes <b>seven calls</b> over 4G and takes <b>2.8 seconds</b>; the portal needs completely different shapes; and <span class="hl-pink">every change for one client risks breaking another</span>.</p>
  <ul>
    <li>Mobile screens make many calls and download data they don't use.</li>
    <li>Each client's needs pull the shared API in different directions.</li>
    <li>Client teams wait on the core team for every shape change.</li>
  </ul>""",
    problem_figs=[bff_problem],
    analogy_side="three pass windows",
    analogy="""  <p>A hotel kitchen has three <b>pass windows</b>: one for the <b>dining room</b> (plated), one for <b>takeaway</b> (boxed), one for <b>room service</b> (on covered trays). Same kitchen, same food; each window prepares it for where it's going. Nobody plates a takeaway order and boxes it again at the door.</p>""",
    analogy_figs=[bff_analogy],
    map=[("The kitchen", "Larder Core's modules and Dispatch"),
         ("Pass windows", "One BFF per kind of client"),
         ("Plated, boxed, on trays", "Payloads shaped per client: one call per screen"),
         ("The waiter for each window", "The client team owning its BFF"),
         ("The same food", "Business rules stay in the core")],
    how_side="one backend per client type",
    how="""  <p>ADR 0022 created two BFFs: a <b>mobile BFF</b> owned by Dee's team, with one endpoint per screen, and a <b>portal BFF</b> owned by Ben's team for office managers. The picker app kept its offline sync service. Business rules stayed in the core modules; BFFs only compose and shape. The order screen went from <b>seven calls and 2.8 s</b> to <b>one call and 0.6 s</b>, and Dee's team now changes its own screens without waiting.</p>""",
    how_figs=[bff_how],
    steps=[("Check the clients really differ", "Different screens, networks, users and release rhythms."),
           ("One BFF per kind of client", "Not per screen, not per team; per client type."),
           ("Give it to the client team", "They change it with their screens."),
           ("Keep it thin", "Compose and shape; no business rules."),
           ("Keep the core general", "Module APIs stay client-agnostic."),
           ("Measure the win", "Calls per screen, payload size, time to first render.")],
    vocab=[("BFF", "Backend for frontend: a backend shaped for one kind of client."),
           ("Chatty API", "One that needs many calls to build one screen."),
           ("Composition", "Combining data from several services into one response."),
           ("Thin layer", "Code that shapes data but holds no business rules."),
           ("General-purpose API", "One API trying to serve every client."),
           ("Over-fetching", "Downloading data the client doesn't use.")],
    code=dict(file="docs/adr/0022-backends-for-frontends.md", note="ADR 0022, decision and rules", plain=True, src="""
# 22. One backend for each kind of client
Status: Accepted · 2027-06-07 · Driver: Ana · with Dee, Ben, Eli

Decision    mobile BFF  (customer apps)     owner: Dee's team
            portal BFF  (business portal)   owner: Ben's team
            picker app keeps its offline sync service
Rules       - BFFs compose and shape; business rules stay in Core modules
            - one endpoint per screen where it helps; payloads only what's shown
            - BFFs call module APIs, never module tables
            - a new BFF needs a new kind of client, not a new screen
Measure     order screen: 7 calls / 2.8 s on 4G → 1 call / 0.6 s (June 2027)
"""),
    tools="tools: a small web service per client (the same stack as Core keeps ops simple); GraphQL is an alternative for some teams; API gateways can host thin BFFs.",
    gains=["<b>Fast screens</b>: one call, small payloads.",
           "<b>Client teams move alone</b>.",
           "<b>Core stays general</b> and stable.",
           "<b>Changes for one client</b> can't break another.",
           "<b>Clear ownership</b> per client type."],
    losses=["<b>More services</b> to run.",
            "<b>Duplicated composition</b> across BFFs.",
            "<b>Business logic creeps in</b> if not watched.",
            "<b>Overkill</b> for one or two similar clients."],
    baseline="Each line compares <b>one general API serving every client</b> to <b>a thin backend per kind of client, owned by that client's team, over general core services</b>.",
    ratings=[(3, 4, "Each BFF reads like its screens."),
             (3, 3, "Mostly between engineering teams."),
             (2, 4, "Client teams decide their own shapes."),
             (2, 4, "Changes can't break other clients."),
             (2, 4, "Clients change without core changes."),
             (3, 3, "ADR 0022 records the rules."),
             (3, 3, "Two more services, small ones."),
             (3, 3, "More to run, less to coordinate."),
             (1, 5, "Dee's team no longer waits on the core team.")],
    pitfalls=[("Business rules in the BFF", "Refund logic in the mobile BFF.", "keep rules in the core; BFFs shape only."),
              ("A BFF per screen", "Twelve tiny backends.", "one per kind of client."),
              ("Owned by the core team", "Client teams still wait.", "the client team owns its BFF."),
              ("BFF reading tables", "Bypassing the modules.", "call module APIs only.")],
    use=["Clients with very different needs (mobile, web portal, partners).",
         "Chatty mobile screens on slow networks.",
         "Client teams that release independently.",
         "When the general API keeps growing special cases."],
    skip=["One client, or clients that need the same shapes.",
          "Small teams where one API is easy to adapt."],
    related=["<b>API-first design</b> (this volume)", "<b>API versioning strategy</b> (this volume)", "<b>Modular monolith first</b> (Vol. 1)", "<b>API gateway</b> (patterns, Vol. 1)"],
    quiz=[("What is a BFF?", "A thin backend shaped for one kind of client, owned by that client's team."),
          ("What should a BFF not contain?", "Business rules: those stay in the core."),
          ("How many BFFs?", "One per kind of client, not per screen."),
          ("What improved for the order screen?", "From seven calls and 2.8 s to one call and 0.6 s.")],
    try_it="Pick your slowest mobile screen. Count the calls it makes and the bytes it downloads versus what it shows. Sketch the single endpoint a BFF would offer for it, and estimate the saving before deciding.",
    remember="One <span class=\"hl\">kitchen</span>, a pass window per <span class=\"hl\">client</span>. Rules stay in the kitchen.",
    sources=["Sam Newman, “Pattern: Backends For Frontends” (samnewman.io, 2015).",
             "Phil Calçado, “The Back-end for Front-end Pattern (BFF)” (2015).",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed. (2021).",
             "Microsoft Azure Architecture Center, “Backends for Frontends pattern”."],
)

# ------------------------------------------------------------------ 07 API Versioning Strategy
av_problem = Doodle(760, 280, "Doodle of June 2027. Korenwolf wants deliveries to several addresses per office and a cost centre per line. Ben's first change to the Business API would rename delivery_address to deliveries and break Korenwolf's facilities system overnight. Two other offices have started using the API too.",
                    "One “small” change would break Korenwolf's system overnight, and two more clients now use the API.")
av_problem.box(20, 40, 320, 90, "Business API v1", "blue", sub="live since May")
av_problem.arrow(344, 85, 420, 85, color="red", label="rename a field", lx=382, ly=164)
av_problem.box(426, 30, 314, 110, "3 clients' systems", "pink", sub="break overnight", stroke="red")
av_problem.note(380, 200, "no policy for changing a published API", "red", size=19)

av_analogy = Doodle(760, 250, "Doodle of a power socket standard. New appliances can add features, but the plug stays the same. When a country changes the standard, it announces a date years ahead, sells adapters, and old sockets keep working until then.",
                     "Sockets: new appliances add features, the plug stays; a new standard comes with a date and adapters.")
av_analogy.icon("plug", 40, 50, 1.6)
for i, (t, s, f) in enumerate([("same plug", "add features freely", "green"), ("new standard", "announced years ahead", "y"), ("adapters", "until the date", "blue")]):
    av_analogy.box(170 + i * 196, 60, 180, 84, t, f, sub=s, subsize=13)
av_analogy.note(450, 210, "change without stranding anyone", "pen")

av_how = Doodle(760, 360, "Larder's API versioning policy, 21 June 2027. Within a version, only additive changes: new optional fields like a cost centre per line, new endpoints. A breaking change, like several delivery addresses per office, means a new major version, v2, in the path. v1 keeps working for twelve months after v2 ships; clients get six months' notice and a Sunset header; usage telemetry shows who still calls v1, and Mo talks to each one.",
                 "Add freely within a version; break only in a new one; run both, announce the end, and watch who's left.")
av_how.box(14, 20, 360, 150, None, "green")
av_how.head(194, 52, "v1: additive only", size=17)
for i, t in enumerate(["+ lines[].cost_centre (optional)", "+ GET /offices", "no renames, no removals"]):
    av_how.text(194, 90 + i * 28, t, size=14)
av_how.box(386, 20, 360, 150, None, "y")
av_how.head(566, 52, "v2: breaking change", size=17)
for i, t in enumerate(["deliveries[] per office", "new path /business/v2", "shipped September"]):
    av_how.text(566, 90 + i * 28, t, size=14)
av_how.line("M60 230 H700")
for x, t in [(60, "v2 ships"), (300, "6 months' notice"), (700, "v1 off (+12 mo)")]:
    av_how.line(f"M{x} 220 V240")
    av_how.note(x, 266, t, "pen", anchor={60: "start", 700: "end"}.get(x, "middle"), size=15)
av_how.note(380, 314, "Sunset header · telemetry: who still calls v1 · Mo calls each", "pen", size=15)
av_how.note(380, 342, "breaking = rename, remove, retype, change meaning", "red", size=15)

VERSIONING = dict(
    slug="api-versioning",
    kicker="a.k.a. “same plug, new appliances”",
    tldr="A published API is a promise to systems you don't control. Have a <b>versioning policy</b> before the first breaking change: within a version, only <b>additive</b> changes (new optional fields, new endpoints); a <b>breaking</b> change (rename, remove, retype, change meaning) means a <b>new major version</b>. Run old and new <b>side by side</b>, give a <b>dated end</b> with plenty of notice, signal it in the API (deprecation and sunset headers), and <b>watch who still calls</b> the old one.",
    chips=[("Family", "boundaries"), ("Origin", "semantic versioning (Tom Preston-Werner, 2010); Stripe's API versioning; RFC 8594 Sunset header"), ("Lives in", "a policy page linked from the API docs"), ("Pairs with", "API-first design, event-driven integration, backend for frontend")],
    problem_side="Larder, 21 June 2027",
    problem="""  <p class="lead">The Business API went live in May; Korenwolf and two other offices now order through it. Korenwolf asks for <b>several delivery addresses per office</b> and a <b>cost centre per line</b>. Ben's first change renames <code>delivery_address</code> to <code>deliveries</code>, which would <span class="hl-pink">break three clients' systems overnight</span>. There's no policy for changing a published API, so the fix depends on who notices in review.</p>
  <ul>
    <li>Consumers you don't control can't upgrade on your schedule.</li>
    <li>“Small” renames are breaking changes.</li>
    <li>Without a policy, every change is a negotiation, or an accident.</li>
  </ul>""",
    problem_figs=[av_problem],
    analogy_side="the power socket",
    analogy="""  <p>New appliances add features all the time, but the <b>plug stays the same</b>. When a country changes its socket standard, it announces a <b>date years ahead</b>, sells <b>adapters</b>, and old sockets keep working until then. Nobody wakes up to find their kettle doesn't fit.</p>""",
    analogy_figs=[av_analogy],
    map=[("The same plug", "v1's contract, unchanged"),
         ("New appliance features", "Additive changes: optional fields, new endpoints"),
         ("A new socket standard", "v2, for the breaking change"),
         ("Announced years ahead", "Six months' notice, a Sunset header"),
         ("Adapters until the date", "v1 and v2 side by side for twelve months")],
    how_side="add within, break in a new version",
    how="""  <p>Ana and Ben wrote the policy that week. The <b>cost centre per line</b> went into v1 as an optional field: additive, nobody broke. <b>Several addresses per office</b> changed the meaning of an order, so it became <b>v2</b>, shipped in September. v1 runs for <b>twelve months</b> after v2, with <b>six months' notice</b> before the end and a <code>Sunset</code> header on every response; telemetry shows who still calls v1, and Mo phones each client.</p>""",
    how_figs=[av_how],
    steps=[("Version in the path from day one", "<code>/business/v1</code>: cheap now, priceless later."),
           ("Define breaking", "Rename, remove, retype, make optional required, change meaning."),
           ("Additive within a version", "New optional fields and endpoints; consumers ignore what they don't know."),
           ("Breaking → new major version", "Run both side by side."),
           ("Announce a dated end", "Notice period, deprecation and Sunset headers, docs, a call from the account manager."),
           ("Watch usage", "Telemetry per version and client; don't switch off until it's zero, or agreed.")],
    vocab=[("Breaking change", "A change that makes existing consumers fail."),
           ("Additive change", "A new optional field or endpoint; safe for consumers."),
           ("Major version", "A new version allowed to break the old contract."),
           ("Deprecation", "Announcing that something will be removed."),
           ("Sunset", "The date a version stops working (HTTP Sunset header, RFC 8594)."),
           ("Tolerant reader", "A consumer that ignores fields it doesn't know.")],
    code=dict(file="api/business/VERSIONING.md", note="Larder Business API versioning policy, 21 June 2027", plain=True, src="""
# Business API · versioning policy                              owner: Ben · contact: Mo

1. The major version is in the path: /business/v1, /business/v2.
2. Within a version, only additive changes: new optional fields, new endpoints,
   new enum values documented as "may grow". Clients must ignore unknown fields.
3. Breaking = rename, remove, retype, optional → required, change of meaning.
   Breaking changes ship only in a new major version.
4. Old and new run side by side for 12 months after the new version ships.
5. 6 months before the end: email + Mo calls each client; every v1 response carries
   Deprecation and Sunset headers (RFC 8594).
6. Telemetry per version and client; v1 is switched off only at zero calls or by agreement.

2027: v1 + lines[].cost_centre (Jun, additive) · v2 deliveries[] per office (Sep)
"""),
    tools="tools: path versioning in the API gateway or router; OpenAPI files per version; breaking-change detection (oasdiff, openapi-diff) in CI; Deprecation and Sunset headers; usage analytics per client.",
    gains=["<b>No client broken overnight</b>.",
           "<b>Additive changes ship freely</b>.",
           "<b>Clear rules</b> instead of negotiations.",
           "<b>Planned upgrades</b> with notice.",
           "<b>Visibility</b> of who still uses old versions."],
    losses=["<b>Two versions to run</b> for a year.",
            "<b>Policy overhead</b> for small changes.",
            "<b>Clients still upgrade late</b>.",
            "<b>Tempting to never remove</b> old versions."],
    baseline="Each line compares <b>changing a published API whenever needed, case by case</b> to <b>a policy: additive within a version, breaking only in a new one, side by side with a dated end</b>.",
    ratings=[(2, 4, "The policy says exactly what's breaking."),
             (2, 5, "Clients, Mo and engineering share the same rules."),
             (2, 4, "Additive changes need no negotiation."),
             (1, 5, "Breaking changes can't reach clients unannounced."),
             (2, 4, "The API can still evolve, in versions."),
             (2, 4, "Every version and its end date on record."),
             (3, 3, "Two versions cost a little to run."),
             (3, 3, "A policy and a diff check in CI."),
             (3, 4, "Teams change the API without asking Ana.")],
    pitfalls=[("No version in the path", "The first breaking change has nowhere to go.", "/v1 from day one."),
              ("Renames as tidy-ups", "“Just a better name.”", "renames are breaking: new version or keep both."),
              ("No end date", "v1 runs forever.", "a dated end, announced, with telemetry."),
              ("Silent deprecation", "Clients find out when it stops.", "headers, email, and a call from the account manager.")],
    use=["Any API consumed by systems you don't control.",
         "B2B and partner APIs.",
         "Public APIs.",
         "Before the first breaking change, ideally before launch."],
    skip=["APIs used only by one team that deploys both sides together.",
          "Private calls inside one module."],
    related=["<b>API-first design</b> (this volume)", "<b>Event-driven integration</b> (this volume)", "<b>Backend for frontend</b> (this volume)", "<b>Consumer-driven contracts</b> (patterns, Vol. 4)"],
    quiz=[("Name four kinds of breaking change.", "Rename, remove, retype, optional → required (or change of meaning)."),
          ("What may change within a version?", "Additive changes: new optional fields and endpoints."),
          ("How long did Larder run v1 alongside v2?", "Twelve months, with six months' notice before the end."),
          ("How do you know when v1 can go?", "Telemetry shows zero calls, or each client has agreed.")],
    try_it="Write your API's versioning policy in six lines, using Larder's as a model. Add a breaking-change check (an OpenAPI diff) to CI. Then find out, from logs, every client calling your oldest version.",
    remember="Keep the <span class=\"hl\">plug</span>. A new standard comes with a <span class=\"hl\">date</span> and adapters.",
    sources=["Tom Preston-Werner, Semantic Versioning 2.0.0 (semver.org).",
             "Stripe, “APIs as infrastructure: future-proofing Stripe with versioning” (2017).",
             "E. Wilde, RFC 8594, “The Sunset HTTP Header Field” (2019).",
             "Arnaud Lauret, <i>The Design of Web APIs</i> (2019), on evolving APIs."],
)

# ------------------------------------------------------------------ 08 Canonical Data Model (and Its Traps)
cd_problem = Doodle(760, 280, "Doodle of a July 2027 proposal: one canonical Larder Order with 140 fields, used by every system: Ordering, WMS B, billing, Dispatch, analytics and the Business API. Everyone would translate to and from it. Ana remembers seeing this at her last company: a model nobody owned, changed by committee, that every team worked around.",
                    "One “Larder Order” with 140 fields for every system. Ana has seen this before.")
cd_problem.box(260, 70, 240, 120, "canonical Order", "pink", sub="140 fields", stroke="red")
for i, (t, x, y) in enumerate([("Ordering", 20, 20), ("WMS B", 20, 110), ("billing", 20, 200), ("Dispatch", 560, 20), ("analytics", 560, 110), ("Business API", 560, 200)]):
    cd_problem.box(x, y, 180, 50, t, "paper", size=15)
    cd_problem.arrow(x + (184 if x < 300 else -4), y + 25, 256 if x < 300 else 504, 130, dash=True)
cd_problem.note(380, 264, "owned by nobody, changed by committee", "red")

cd_analogy = Doodle(760, 250, "Doodle of an attempt at one universal form for every government department: tax, health, driving, passports. It grows to forty pages, every department fills in a fraction, nobody can change it alone, and each department ends up with its own unofficial form anyway.",
                     "One universal form for every department grows to forty pages, and each department keeps its own anyway.")
cd_analogy.icon("directory", 40, 50, 1.5)
cd_analogy.box(170, 50, 280, 100, "the universal form", "pink", sub="40 pages, 10 % used each")
cd_analogy.box(480, 50, 260, 100, "reality", "paper", sub="each keeps its own form")
cd_analogy.note(450, 210, "common to all, right for none", "pen")

cd_how = Doodle(760, 360, "What Larder chose instead, ADR 0023, 5 July 2027. Each bounded context keeps its own model: an order is a basket in Ordering, a pick list in Fulfilment, a drop in Dispatch, an invoice line in billing. Between them, a small published language: three shared events, order placed, stock changed and delivery completed, each with a few fields everyone agrees on, owned and versioned. Translation happens at each context's border.",
                 "Own models inside each context; a small, shared, versioned language between them; translation at the borders.")
for i, (ctx, model) in enumerate([("Ordering", "basket"), ("Fulfilment", "pick list"), ("Dispatch", "drop"), ("billing", "invoice line")]):
    x = 14 + i * 186
    cd_how.box(x, 20, 170, 80, ctx, "blue", sub=model)
cd_how.box(120, 150, 520, 110, None, "green")
cd_how.head(380, 182, "published language: 3 events", size=17)
cd_how.text(380, 214, "order.placed · stock.changed · delivery.completed", size=15)
cd_how.text(380, 240, "few fields · one owner each · versioned", size=15)
for i in range(4):
    cd_how.arrow(99 + i * 186, 104, 250 + i * 87, 146, both=True, dash=True)
cd_how.note(380, 300, "translation at each border (anti-corruption layers)", "pen", size=16)
cd_how.note(380, 328, "ADR 0023: no canonical model", "green", size=16)

CANONICAL = dict(
    slug="canonical-data-model",
    kicker="a.k.a. “the universal government form”",
    tldr="A <b>canonical data model</b>, one shared model of “order” or “customer” that every system translates to, sounds like order out of chaos. In practice it often becomes a <b>huge model nobody owns</b>, changed by committee, <b>right for no one</b>, coupling every system to every other. What usually works better: each bounded context keeps <b>its own model</b>, and only a <b>small published language</b> (a few shared events or messages with few fields, owned and versioned) crosses the borders, with translation at each edge.",
    chips=[("Family", "boundaries"), ("Origin", "canonical data model (Hohpe &amp; Woolf, 2003); critiques from DDD (bounded contexts, published language)"), ("Lives in", "an ADR and the event catalogue"), ("Pairs with", "bounded contexts, anti-corruption layer, event-driven integration")],
    problem_side="Larder, 5 July 2027",
    problem="""  <p class="lead">With WMS B, billing, Dispatch, analytics and the Business API all exchanging orders, a new senior engineer proposes a <b>canonical Larder Order</b>: one model, <b>140 fields</b>, that every system translates to and from. It sounds tidy. Ana has seen it before, at her last company: <span class="hl-pink">a model nobody owned</span>, changed by committee, that every team quietly worked around.</p>
  <ul>
    <li>A model for everyone has every field and fits no one.</li>
    <li>Every change needs every team's agreement, so nothing changes.</li>
    <li>Systems become coupled through the shared model.</li>
  </ul>""",
    problem_figs=[cd_problem],
    analogy_side="the universal government form",
    analogy="""  <p>Imagine one <b>universal form</b> for every government department: tax, health, driving, passports. It grows to forty pages; each department fills in a tenth of it; no department can change it alone. Within a year each one has its own unofficial form again, plus a team that copies data from it into the universal one.</p>""",
    analogy_figs=[cd_analogy],
    map=[("The universal form", "A 140-field canonical order"),
         ("Each department's real form", "Each context's own model: basket, pick list, drop"),
         ("Changes by committee", "Every team must agree to every field"),
         ("A short shared slip", "The published language: three small events"),
         ("Clerks copying between forms", "Translation at each context's border")],
    how_side="own models, a small shared language",
    how="""  <p>Ana wrote ADR 0023 with the engineer who proposed it, starting from the problem he wanted to solve (inconsistent order data in analytics). Each context keeps <b>its own model</b>; between them, a small <b>published language</b>: <code>order.placed</code>, <code>stock.changed</code> and <code>delivery.completed</code>, each with a <b>few fields</b> everyone agrees on, owned and versioned in the registry. Analytics builds its own consistent view from those events.</p>""",
    how_figs=[cd_how],
    steps=[("Start from the real problem", "Inconsistent reports? Many integrations? Name it first."),
           ("Keep models per context", "Each bounded context owns its own shape of “order”."),
           ("Agree a small published language", "A few shared events or messages, few fields each."),
           ("Give each shared message an owner", "Versioned in the registry, with compatibility rules."),
           ("Translate at the borders", "Anti-corruption layers in each context."),
           ("Build shared views where needed", "Analytics composes its own view from the events.")],
    vocab=[("Canonical data model", "One shared model all systems translate to."),
           ("Published language", "A small, shared, documented format for exchanging data."),
           ("Bounded context", "An area with its own model and words."),
           ("Lowest common denominator", "A model that fits everyone poorly."),
           ("Semantic coupling", "Systems depending on each other's meanings."),
           ("Context map", "How contexts relate and translate.")],
    code=dict(file="docs/adr/0023-no-canonical-order.md", note="ADR 0023, the decision", plain=True, src="""
# 23. No canonical order model; a small published language instead
Status: Accepted · 2027-07-05 · Driver: Ana · with the proposer, Ben, Eli, analytics

Problem     Order data is inconsistent across systems, especially in analytics.
Rejected    A canonical Larder Order (140 fields) used by every system:
            no single owner, committee changes, couples every system to every other.
Decision    - Each context keeps its own model (basket, pick list, drop, invoice line).
            - Published language, owned and versioned in the registry:
                order.placed (Ordering) · stock.changed (Stock) · delivery.completed (Dispatch)
              each ≤ 15 fields; compatibility rules as ADR 0020.
            - Translation at each border (anti-corruption layers).
            - Analytics builds one consistent order view from the three events.
Revisit     If more than 5 contexts need the same new field, discuss adding it.
"""),
    tools="tools: the schema registry and event catalogue (ADR 0020); context maps from DDD; a data warehouse view built from events for analytics.",
    gains=["<b>Each context keeps a model</b> that fits it.",
           "<b>Shared messages stay small</b> and owned.",
           "<b>Changes stay local</b> to one context.",
           "<b>Analytics still gets consistency</b>, from events.",
           "<b>No committee</b> for every field."],
    losses=["<b>More translation code</b> at the borders.",
            "<b>Some duplication</b> of data across contexts.",
            "<b>Harder to explain</b> than “one model”.",
            "<b>The published language needs governance</b> too."],
    baseline="Each line compares <b>one canonical model every system translates to</b> to <b>a model per context and a small, owned published language between them</b>.",
    ratings=[(2, 4, "Each model fits its context; three shared events are easy to learn."),
             (2, 4, "Analytics' problem solved without a committee."),
             (2, 4, "Changes inside a context need no cross-team approval."),
             (2, 4, "No single model that couples everything."),
             (2, 5, "Contexts evolve independently."),
             (3, 4, "ADR 0023 and the catalogue record the shared language."),
             (3, 3, "Translation code costs a little."),
             (3, 3, "Borders to maintain."),
             (2, 4, "Teams own their models fully.")],
    pitfalls=[("The 140-field model", "Every field anyone ever needed.", "small shared messages, few fields."),
              ("No owner", "The canonical model belongs to everyone.", "one owner per shared message."),
              ("Shared language grows", "Three events become thirty.", "add only what several contexts need; review yearly."),
              ("Ignoring the real problem", "Analytics still inconsistent.", "build the consistent view from events.")],
    use=["When someone proposes “one model for everything”.",
         "Systems with several bounded contexts exchanging data.",
         "Analytics needing consistent views across systems.",
         "Integration platforms with many systems."],
    skip=["A small number of systems that truly share one model.",
          "Industry standards you must use (then translate at the border)."],
    related=["<b>Bounded contexts</b> (Vol. 1)", "<b>Anti-corruption layer</b> (this volume)", "<b>Event-driven integration</b> (this volume)", "<b>Glossary &amp; ubiquitous language</b> (Vol. 3)"],
    quiz=[("Why do canonical models often fail?", "Nobody owns them, changes need everyone's agreement, and they fit no one well."),
          ("What's a published language?", "A small, shared, owned format for exchanging data between contexts."),
          ("What three events form Larder's published language?", "order.placed, stock.changed and delivery.completed."),
          ("How does analytics get consistent orders?", "By building its own view from the shared events.")],
    try_it="If your organisation has (or wants) a canonical model, count its fields and how many each system really uses. Then list the three or four messages that actually need to cross team boundaries, with the fields each needs, and compare.",
    remember="No <span class=\"hl\">universal form</span>. Each desk its own; a short <span class=\"hl\">shared slip</span> between them.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), “Published Language”.",
             "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003), “Canonical Data Model”.",
             "Vaughn Vernon, <i>Domain-Driven Design Distilled</i> (2016), context mapping.",
             "Martin Fowler, “BoundedContext” (martinfowler.com, 2014)."],
)

NOTES = [ACL, BFF, VERSIONING, CANONICAL]
