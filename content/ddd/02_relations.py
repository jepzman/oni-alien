# Vol. 7 · Domain-Driven Design · Between contexts: Context Map, Customer–Supplier & Conformist, Shared Kernel &
# Partnership, Anti-Corruption Layer, Open Host Service & Published Language.

# ------------------------------------------------------------------ 05 Context Map
cm_problem = Doodle(760, 260, "Doodle of an outage nobody saw coming. The Pricing team renames a field in its API on a Tuesday. On Wednesday, Ordering, Promotions and the mobile app all break. Nobody knew they depended on it. The only architecture diagram is a boxes-and-lines picture from two years ago, with no arrows showing who depends on whom.",
                    "Pricing changes a field; three teams break; nobody knew who depended on whom.")
cm_problem.box(290, 30, 180, 70, "Pricing", "blue", sub="renames a field")
for i, t in enumerate(["Ordering", "Promotions", "mobile app"]):
    x = 20 + i * 250
    cm_problem.box(x, 160, 220, 60, t, "pink", stroke="red", size=18)
    cm_problem.arrow(380, 104, x + 110, 156, color="red", dash=True)
cm_problem.note(380, 250, "“we didn't know you used that”", "red")

cm_analogy = Doodle(760, 250, "Doodle of a map of countries showing their relationships: which ones share a border, which trade, which depend on another for water or power, and where there are customs posts. A diplomat reads the map before any negotiation.",
                    "A political map: borders, trade routes, who depends on whom, and where the customs posts are.")
cm_analogy.icon("map", 40, 70, 1.8)
cm_analogy.note(470, 60, "borders between countries", "pen")
cm_analogy.note(470, 105, "who supplies water and power to whom", "pen")
cm_analogy.note(470, 150, "where the customs posts are", "pen")
cm_analogy.note(470, 210, "read it before any negotiation", "green")

cm_how = Doodle(760, 360, "A context map for the online shop. Catalogue is upstream of Ordering with a published language. Ordering and Shipping are partners. Payments is an external provider that Ordering conforms to, through an anti-corruption layer. Pricing and Ordering are customer and supplier. Each line is labelled U for upstream and D for downstream with the relationship pattern.",
                 "Each arrow runs from upstream to downstream and names how the two relate.")
nodes = {"Catalogue": (40, 30, "y"), "Pricing": (520, 30, "blue"), "Ordering": (280, 140, "green"), "Shipping": (40, 250, "paper"), "Payments (ext)": (520, 250, "pink")}
for name, (x, y, f) in nodes.items():
    cm_how.box(x, y, 200, 60, name, f, size=17)
cm_how.arrow(240, 75, 296, 136, label="OHS / PL", lx=230, ly=118, anchor="end")
cm_how.arrow(520, 75, 464, 136, label="customer–supplier", lx=540, ly=118, anchor="start")
cm_how.line("M280 190 L240 250", color="green")
cm_how.note(220, 222, "partnership", "green", anchor="end")
cm_how.arrow(520, 270, 484, 196, label="ACL + conformist", lx=540, ly=234, anchor="start")
cm_how.note(380, 348, "arrows point from upstream (U) to downstream (D)", "pen")

CONTEXT_MAP = dict(
    slug="context-map",
    kicker="a.k.a. “the political map of your system”",
    tldr="Draw <b>every bounded context</b> and, for each pair that talks, <b>how they relate</b>: who is <b>upstream</b> (others depend on it) and who is <b>downstream</b>, and which pattern they use (partnership, customer–supplier, conformist, anti-corruption layer, open host service, shared kernel). The map shows the <b>real dependencies</b>, technical and human, before they break something.",
    chips=[("Family", "strategic design"), ("From", "Evans (2003), ch. 14"), ("Shows", "contexts, dependencies, team relationships"), ("Tools", "Context Mapper, a whiteboard")],
    problem="""  <p class="lead">Contexts and teams depend on each other in ways nobody wrote down, so a change in one <span class="hl-pink">breaks others by surprise</span>.</p>
  <ul>
    <li>A renamed field upstream breaks three teams downstream.</li>
    <li>Nobody knows which team has to agree before a change.</li>
    <li>The architecture diagram shows boxes and lines but not who depends on whom.</li>
  </ul>""",
    problem_figs=[cm_problem],
    analogy_side="a political map",
    analogy="""  <p>A <b>political map</b> shows borders, trade routes, who supplies water and power to whom, and where the customs posts are. A diplomat reads it before any negotiation, because <b>who depends on whom</b> decides what's possible.</p>
  <ul>
    <li>Countries are <b>bounded contexts</b>.</li>
    <li>Supply lines show <b>upstream and downstream</b>.</li>
    <li>Customs posts are <b>anti-corruption layers</b>.</li>
  </ul>""",
    analogy_figs=[cm_analogy],
    map=[("A country", "A bounded context"),
         ("Supplies water to its neighbour", "Upstream context: its changes affect downstream"),
         ("Trade agreement", "Customer–supplier or partnership"),
         ("Customs post", "Anti-corruption layer"),
         ("Standard shipping containers", "Open host service with a published language")],
    how_side="contexts, arrows and patterns",
    how="""  <p>The map describes <b>what is</b>, not what you wish. If Ordering in fact copies whatever Payments sends, write “conformist”, even if you'd like an anti-corruption layer. The gaps between the map you have and the one you want become your to-do list.</p>""",
    how_figs=[cm_how],
    steps=[("List the contexts", "Including external systems and SaaS: they are contexts you don't control."),
           ("Draw who talks to whom", "One line per pair that exchanges data or calls."),
           ("Mark upstream and downstream", "Upstream changes affect downstream, not the other way round. Write U and D on each end."),
           ("Name the pattern", "Partnership, shared kernel, customer–supplier, conformist, ACL, open host service, published language, separate ways."),
           ("Add the teams", "Who owns each context. Many problems are team problems, not code problems."),
           ("Keep it alive", "Update it when integrations change; review it when planning big changes.")],
    vocab=[("Context map", "A diagram of contexts and the relationships between them."),
           ("Upstream", "The side whose model and changes affect the other side."),
           ("Downstream", "The side that depends on the upstream's model."),
           ("Relationship pattern", "A named way two contexts and teams relate, such as conformist."),
           ("Separate ways", "Two contexts that deliberately don't integrate at all."),
           ("Big ball of mud", "A part of the map with no clear borders; mark it honestly.")],
    code=dict(file="shop.cml", note="Context Mapper DSL, renders the diagram", src="""
ContextMap ShopMap {
  contains Catalogue, Pricing, Ordering, Shipping, Payments

  Catalogue [U, OHS, PL] -> [D] Ordering        // open host service, published language
  Pricing   [U]          -> [D] Ordering : CustomerSupplier
  Ordering  [P]         <-> [P] Shipping         // partnership
  Payments  [U]          -> [D, ACL, CF] Ordering // external: we conform, behind an ACL
}
"""),
    tools="tools: Context Mapper (an Eclipse/VS Code plug-in with a small DSL that draws the map), the DDD Crew's context mapping cheat sheet, or a whiteboard photo kept next to the code.",
    gains=["<b>Dependencies are visible</b> before a change.",
           "<b>Team relationships</b> are named and can be improved.",
           "<b>A shared picture</b> for planning and onboarding.",
           "<b>Shows where to invest</b>: missing ACLs, risky conformists."],
    losses=["<b>Takes effort</b> to draw honestly.",
            "<b>Goes stale</b> if nobody owns it.",
            "<b>Uncomfortable truths</b> (“we are conformist to that mess”).",
            "<b>Pattern names</b> are jargon outside DDD circles."],
    baseline="Each line compares <b>integrations that grew without a map</b> to <b>a maintained context map with named relationships</b>.",
    ratings=[(2, 4, "One picture of how everything connects."),
             (3, 4, "Contexts named in business terms."),
             (3, 3, "Neutral on its own."),
             (2, 4, "You know who's affected before you change something."),
             (3, 3, "Neutral."),
             (2, 4, "Hidden dependencies become visible and can be cut."),
             (3, 3, "Neutral."),
             (4, 3, "A diagram to draw and keep current."),
             (2, 4, "Teams know who to talk to, and how.")],
    pitfalls=[("Drawing the wished-for map", "Every line says “ACL” but the code copies upstream fields everywhere.", "draw what is true today; draw the target separately."),
              ("Only technical arrows", "Lines show HTTP calls but not which team must agree to a change.", "add team names and the relationship pattern."),
              ("A one-off poster", "Drawn in a workshop, never updated.", "keep it in the repository and review it in architecture meetings."),
              ("Leaving out external systems", "The payment provider isn't on the map, but it shapes Ordering's model.", "every external system is a context too.")],
    use=["More than three contexts or teams that integrate.",
         "Before a big change that crosses borders.",
         "When integration problems keep surprising people."],
    skip=["One team, one context, nothing to map.",
          "As a substitute for talking to the other team."],
    related=["<b>Bounded Context</b>", "<b>Customer–Supplier &amp; Conformist</b>", "<b>Anti-Corruption Layer</b>", "<b>Open Host Service &amp; Published Language</b>", "<b>System Context Diagram</b> (Ana, vol. 1)"],
    quiz=[("What does “upstream” mean on a context map?", "The context whose model and changes affect the other; the downstream side depends on it."),
          ("Should a context map show how things are, or how you want them?", "How they are. Draw the target separately; the difference is your plan."),
          ("Name four relationship patterns.", "Partnership, shared kernel, customer–supplier, conformist, anti-corruption layer, open host service, published language, separate ways."),
          ("Why add team names to the map?", "Many integration problems are about who must agree and who can change what, not about technology.")],
    quiz_sit=[("A team wants to change the format of its <code>OrderPlaced</code> event. They ask “who uses it?” and nobody can answer in less than a day of grepping. What do you set up?",
               "A context map that shows every consumer of each context, kept in the repository, plus consumer-driven contract tests or a schema registry that lists subscribers, so the answer is a lookup, not an investigation.")],
    try_it="Draw the context map of a system you know, including external services. For every line, write U and D, and the pattern you think it is. Then circle the one relationship that worries you most and write why.",
    then_now=dict(src="Evans, 2003", verdict="core",
                  then="Evans described the context map as a document of the contexts and their relationships, with a set of named patterns, many of them about teams and politics rather than code.",
                  now="The same patterns are used daily, now for microservices, SaaS integrations and team design. Team Topologies' interaction modes (collaboration, X-as-a-service, facilitating) map closely to them. Context Mapper turns the map into a small DSL.",
                  take="Still core. The patterns were always as much about people as code, which is why they aged well."),
    remember="Before you change a context, <span class=\"hl\">read the map</span>: the arrows tell you who you're about to <span class=\"hl\">break</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14.",
             "DDD Crew, “Context Mapping” cheat sheet (github.com/ddd-crew/context-mapping).",
             "Context Mapper documentation (contextmapper.org).",
             "Matthew Skelton &amp; Manuel Pais, <i>Team Topologies</i> (2019), ch. 7."],
)

# ------------------------------------------------------------------ 06 Customer–Supplier & Conformist
cs_problem = Doodle(760, 260, "Doodle of a downstream team stuck waiting. Ordering needs Pricing to add a discount field. Pricing's roadmap is full; the request sits in their backlog for three months. Ordering hacks around it by parsing discount text out of a description field. Nobody ever decided what kind of relationship the two teams have.",
                    "Ordering waits three months for Pricing, then hacks around it. Nobody agreed how the teams relate.")
cs_problem.box(20, 50, 220, 80, "Ordering", "green", sub="needs a field")
cs_problem.arrow(244, 90, 496, 90, label="please add “discount”", lx=370, ly=74)
cs_problem.box(500, 50, 240, 80, "Pricing", "blue", sub="backlog: full")
cs_problem.note(370, 170, "3 months later…", "pen")
cs_problem.box(160, 194, 440, 50, "parse it from the description", "pink", stroke="red", size=18)

cs_analogy = Doodle(760, 250, "Doodle of two kinds of supplier relationship. A restaurant chain asks its bakery for a new bread size, and the bakery adds it to its plan because the chain is an important customer. A corner café uses the standard loaves from the supermarket, as they are, because it can't ask the supermarket for anything.",
                    "A big customer asks its bakery for changes. A small café just takes the supermarket's standard loaf.")
cs_analogy.box(20, 40, 340, 90, "chain ↔ bakery", "y", sub="asks, plans together")
cs_analogy.box(400, 40, 340, 90, "café → supermarket", "paper", sub="takes what's on the shelf")
cs_analogy.note(190, 170, "customer–supplier", "green")
cs_analogy.note(570, 170, "conformist", "pen")
cs_analogy.note(380, 220, "both are fine, if you know which one you're in", "pen")

cs_how = Doodle(760, 310, "Two relationships between an upstream and a downstream context. In customer–supplier, the downstream team's needs go into the upstream team's planning, they agree interfaces, and contract tests protect the downstream. In conformist, the downstream adopts the upstream model as it is, with no say, which is simple but means the upstream's model shapes the downstream's code. When the upstream model is poor, a downstream adds an anti-corruption layer instead.",
                 "Customer–supplier: downstream has a say. Conformist: downstream takes the model as it is.")
cs_how.box(20, 20, 340, 70, "customer–supplier", "green", sub="needs in upstream's plan")
cs_how.box(400, 20, 340, 70, "conformist", "paper", sub="adopt the model as it is")
cs_how.text(190, 130, "agreed interfaces")
cs_how.text(190, 160, "contract tests downstream")
cs_how.text(190, 190, "joint planning")
cs_how.text(570, 130, "no translation code")
cs_how.text(570, 160, "no say in changes")
cs_how.text(570, 190, "their model leaks in")
cs_how.box(400, 230, 340, 60, "poor upstream? add an ACL", "pink", stroke="red", size=16)

CUSTOMER_SUPPLIER = dict(
    slug="customer-supplier",
    kicker="a.k.a. “do we get a say, or do we take what's on the shelf?”",
    tldr="When one context depends on another, decide <b>which kind of dependency</b> it is. <b>Customer–supplier</b>: the downstream team's needs go into the upstream team's <b>planning</b>, interfaces are agreed and protected by <b>contract tests</b>. <b>Conformist</b>: the downstream simply <b>adopts</b> the upstream's model, because it can't influence it (a big vendor, a legacy system) or doesn't need to. Both work; <b>not knowing which you're in</b> doesn't.",
    chips=[("Family", "context relationship"), ("From", "Evans (2003), ch. 14"), ("Decides", "who has a say in the interface"), ("Pairs with", "contract testing, anti-corruption layer")],
    problem="""  <p class="lead">Two teams depend on each other, but nobody has agreed <span class="hl-pink">who can ask whom for what</span>.</p>
  <ul>
    <li>Requests sit in another team's backlog for months.</li>
    <li>The downstream team hacks around missing data.</li>
    <li>The upstream team changes things without knowing who uses them.</li>
  </ul>""",
    problem_figs=[cs_problem],
    analogy_side="the bakery and the supermarket",
    analogy="""  <p>A <b>restaurant chain</b> asks its bakery for a new bread size, and the bakery puts it in its plan: the chain is a valued <b>customer</b>. A <b>corner café</b> buys standard loaves at the supermarket: it can't ask for anything, so it <b>conforms</b> and plans its sandwiches around what's on the shelf.</p>
  <ul>
    <li>The chain and bakery are <b>customer–supplier</b>.</li>
    <li>The café is <b>conformist</b>.</li>
    <li>Both work, because each knows where it stands.</li>
  </ul>""",
    analogy_figs=[cs_analogy],
    map=[("The chain asks for a new size", "Ordering's need goes into Pricing's backlog and planning"),
         ("Agreed delivery specs", "An agreed API or event schema, with contract tests"),
         ("The café takes standard loaves", "Ordering uses the payment provider's model as it is"),
         ("Can't ask the supermarket", "No influence over a vendor or a legacy system"),
         ("Re-wrapping the loaf", "An anti-corruption layer, when the upstream model is a poor fit")],
    how_side="name the relationship, then act like it",
    how="""  <p>Customer–supplier needs <b>upstream goodwill</b>: management must make serving downstream teams part of the upstream team's job. Conformist needs a <b>decent upstream model</b>: if it's poor, conforming spreads the mess, so put an anti-corruption layer in between.</p>""",
    how_figs=[cs_how],
    steps=[("Find the direction", "Which context's changes affect the other? That one is upstream."),
           ("Ask about influence", "Can the downstream team realistically change the upstream's plans? If yes, customer–supplier is possible."),
           ("For customer–supplier", "Downstream needs go into upstream planning; agree interfaces; downstream writes contract tests that run in upstream's pipeline."),
           ("For conformist", "Use the upstream model directly; keep a thin wrapper so a later ACL is possible."),
           ("Check the model quality", "If conforming would spread a confusing model through your code, translate instead (ACL)."),
           ("Write it on the context map", "So everyone knows the deal, and revisit it when teams or vendors change.")],
    vocab=[("Customer–supplier", "Upstream plans with downstream's needs in mind; interfaces are negotiated."),
           ("Conformist", "Downstream adopts the upstream model without translation or influence."),
           ("Upstream / downstream", "Who affects whom when they change."),
           ("Consumer-driven contract", "A test written by the consumer that the provider must keep passing."),
           ("Veto", "A downstream's power to block breaking changes; customer–supplier gives some."),
           ("Separate ways", "Choosing not to integrate at all when it costs more than it gives.")],
    code=dict(file="pricing.contract.test.ts", note="Ordering's expectations, run in Pricing's pipeline", src="""
// Written by Ordering (customer), run by Pricing (supplier) on every build.
import { pactWith } from "jest-pact";

pactWith({ consumer: "ordering", provider: "pricing" }, (provider) => {
  test("a quote includes the discount per line", async () => {
    await provider.addInteraction({
      uponReceiving: "a quote for a basket",
      withRequest: { method: "POST", path: "/quotes" },
      willRespondWith: { status: 200, body: {
        lines: [{ sku: "BIKE-42", price: { amount: 49900, currency: "EUR" },
                  discount: { amount: 5000, currency: "EUR" } }] } },
    });
    // ... call the client and assert
  });
});
"""),
    tools="tools: consumer-driven contract tests (Pact, Spring Cloud Contract), a shared roadmap or planning ritual between the two teams, and the context map to record which relationship applies.",
    gains=["<b>Clear expectations</b> between teams.",
           "<b>Customer–supplier</b>: downstream needs get planned, not ignored.",
           "<b>Conformist</b>: no translation code at all.",
           "<b>Contract tests</b> catch breaking changes before release."],
    losses=["<b>Customer–supplier</b> needs upstream time and goodwill.",
            "<b>Conformist</b> lets another model shape your code.",
            "<b>Politics</b>: priorities between teams must be settled by someone.",
            "<b>Relationships change</b> when teams or vendors do."],
    baseline="Each line compares <b>an unnamed dependency between two teams</b> to <b>an explicit customer–supplier or conformist relationship</b>.",
    ratings=[(3, 4, "Everyone knows who decides what."),
             (3, 3, "Conformist can blur the language; customer–supplier keeps it."),
             (3, 4, "Contract tests protect what downstream relies on."),
             (2, 4, "Breaking changes are planned, not discovered."),
             (3, 4, "Contracts are tested on both sides."),
             (2, 3, "Coupling remains, but it's agreed and visible."),
             (3, 3, "Neutral."),
             (3, 3, "Contract tests and planning vs no translation code: roughly even."),
             (2, 4, "Teams stop blocking each other by surprise.")],
    pitfalls=[("Customer–supplier in name only", "The upstream team never actually plans for downstream needs.", "make serving downstream part of the upstream team's goals, with a manager who arbitrates."),
              ("Conforming to a mess", "A legacy model's odd names and codes spread through the new system.", "conform only to good models; otherwise add an anti-corruption layer."),
              ("No contract tests", "The upstream team “promised” not to break things, and did.", "consumer-driven contracts in the upstream's pipeline."),
              ("Assuming influence over vendors", "Waiting for a SaaS vendor to add a field.", "with vendors you are conformist (or ACL); plan accordingly.")],
    use=["Any dependency between two teams' contexts.",
         "A downstream team that keeps waiting on, or being broken by, an upstream one.",
         "Integrating a vendor or legacy system (usually conformist or ACL)."],
    skip=["Two contexts owned by one team (just change both).",
          "When integration costs more than it gives: choose separate ways."],
    related=["<b>Context Map</b>", "<b>Anti-Corruption Layer</b>", "<b>Shared Kernel &amp; Partnership</b>", "<b>Contract Testing</b> (Vol. 4)", "<b>SaaS &amp; Vendor Integration</b> (Ana, vol. 4)"],
    quiz=[("What's the difference between customer–supplier and conformist?", "In customer–supplier, the downstream's needs shape the upstream's plans. In conformist, the downstream adopts the upstream model with no say."),
          ("When is conformist a good choice?", "When the upstream model is decent and you can't or don't need to influence it, such as a well-designed vendor API."),
          ("What protects a customer–supplier relationship technically?", "Consumer-driven contract tests run in the upstream's pipeline."),
          ("What do you do if the upstream model is poor and you can't change it?", "Put an anti-corruption layer between it and your model.")],
    quiz_sit=[("Your Ordering team has waited four months for the Pricing team to add a field. Pricing says their roadmap is set by another director. What do you do?",
               "Escalate it as a relationship question, not a ticket: either make it customer–supplier (a shared planning slot and someone who arbitrates priorities), or accept conformist and work around it properly (compute it in an ACL from data you do get), and record the decision on the context map.")],
    try_it="For one dependency your team has on another team, write down: who is upstream, whether you can influence their plans, and what happens when they change something. Then name the relationship and add one contract test for the field you rely on most.",
    then_now=dict(src="Evans, 2003", verdict="core",
                  then="Evans named these as patterns of team relationships: customer–supplier when the upstream team can be persuaded to care, conformist when it can't, both with notes on politics and acceptance tests.",
                  now="Unchanged in substance. Consumer-driven contract testing (Pact, 2013) made the “acceptance tests” part practical, and the rise of SaaS made conformist the everyday relationship with vendors.",
                  take="Still core. Every team that depends on another is in one of these, whether it says so or not."),
    remember="Know whether you're the <span class=\"hl\">restaurant chain</span> or the <span class=\"hl\">corner café</span>, and plan like it.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14.",
             "DDD Crew, “Context Mapping” (github.com/ddd-crew/context-mapping).",
             "Pact documentation, “Consumer-driven contracts” (docs.pact.io).",
             "Vaughn Vernon, <i>Domain-Driven Design Distilled</i> (2016), ch. 4."],
)

# ------------------------------------------------------------------ 07 Shared Kernel & Partnership
sk_problem = Doodle(760, 260, "Doodle of a shared library that grew out of control. Five services depend on a common-model package. It started with Money and Address, and now has Order, Customer and Product classes with fields for every service. Any change needs all five teams to upgrade at once; versions drift; one team is three major versions behind.",
                    "A “common” package with everyone's classes: five teams must upgrade together, and one is three versions behind.")
sk_problem.box(250, 30, 260, 110, "common-model", "pink", stroke="red", sub="Money · Order · Customer…")
for i in range(5):
    x = 20 + i * 148
    sk_problem.box(x, 190, 130, 50, f"svc {i + 1}", "paper", size=16)
    sk_problem.arrow(x + 65, 186, 380, 144, dash=True)
sk_problem.note(640, 70, "v1 · v2 · v4 in prod", "red")

sk_analogy = Doodle(760, 250, "Doodle of two neighbours who share a garden wall and a hedge. They agreed that neither changes the wall without asking the other, and they trim the hedge together each spring. They don't share their houses: only the wall.",
                    "Neighbours share one garden wall, and agree never to change it without asking each other.")
sk_analogy.box(30, 60, 260, 120, "house A", "y")
sk_analogy.box(470, 60, 260, 120, "house B", "blue")
sk_analogy.box(330, 40, 100, 160, "wall", "paper", sub="shared")
sk_analogy.note(380, 230, "change the wall only together", "green")

sk_how = Doodle(760, 300, "A shared kernel between Ordering and Shipping: a small package with Money, Address and OrderId, owned jointly. Changes need both teams to agree, run both test suites and release together. Everything else in each context stays private. In a partnership, the two teams also plan together: they coordinate releases and succeed or fail together.",
                 "Share a small kernel of model, changed only together. Everything else stays private.")
sk_how.box(20, 40, 260, 160, None, "green", dash=True)
sk_how.head(150, 76, "Ordering")
sk_how.text(150, 116, "private model")
sk_how.box(480, 40, 260, 160, None, "paper", dash=True)
sk_how.head(610, 76, "Shipping")
sk_how.text(610, 116, "private model")
sk_how.box(220, 120, 320, 100, "shared kernel", "y", sub="Money · Address · OrderId")
sk_how.note(380, 260, "both test suites run on every change · release together", "pen")

SHARED_KERNEL = dict(
    slug="shared-kernel",
    kicker="a.k.a. “the garden wall two neighbours share”",
    tldr="Two teams that work closely can share a <b>small piece of model</b> (like Money, Address, a few IDs) as a <b>shared kernel</b>: jointly owned, changed <b>only by agreement</b>, tested by <b>both</b>. In a <b>partnership</b>, the two teams go further and plan and release together. Keep the kernel <b>tiny</b>: the bigger it gets, the more it becomes a shared monolith in disguise.",
    chips=[("Family", "context relationship"), ("From", "Evans (2003), ch. 14"), ("Size", "small: a few types, not entities"), ("Watch out", "the “common” library that ate everything")],
    problem="""  <p class="lead">“Let's put the shared classes in a common library” is how many systems end up with <span class="hl-pink">every team coupled to every other</span>.</p>
  <ul>
    <li>The common package grows from Money to Order, Customer and Product.</li>
    <li>Every change needs every team to upgrade together.</li>
    <li>Versions drift; nobody dares to change anything.</li>
  </ul>""",
    problem_figs=[sk_problem],
    analogy_side="the garden wall",
    analogy="""  <p>Two <b>neighbours</b> share a garden wall. They agreed neither changes it without asking, and they trim the hedge on top together each spring. They <b>don't</b> share their houses: only the wall.</p>
  <ul>
    <li>The wall is the <b>shared kernel</b>.</li>
    <li>“Only together” is the <b>joint ownership</b>.</li>
    <li>Trimming together each spring is a <b>partnership</b>.</li>
  </ul>""",
    analogy_figs=[sk_analogy],
    map=[("The shared wall", "A small package of shared types"),
         ("Ask before changing it", "Changes reviewed and approved by both teams"),
         ("Each house is private", "Each context's own model stays private"),
         ("Trimming the hedge together", "Partnership: joint planning and releases"),
         ("A wall that becomes a shared house", "A “common” library that grew into a shared model")],
    how_side="share little, change together",
    how="""  <p><b>Partnership</b> is about the teams: they coordinate plans and succeed or fail together. <b>Shared kernel</b> is about the code: a small model they both use. They often go together, but either can exist alone.</p>""",
    how_figs=[sk_how],
    steps=[("Ask if you need it", "Can each side keep its own copy of these few types instead? Often yes, and that's simpler."),
           ("Keep it to value types", "Money, Address, IDs, maybe a shared enum. Not entities or aggregates."),
           ("Own it jointly", "Both teams review every change; neither can merge alone."),
           ("Test with both", "Both teams' test suites run on every change to the kernel."),
           ("Release together", "Or version it carefully, and upgrade both sides in the same sprint."),
           ("Watch its size", "If it keeps growing, the contexts may really be one, or need separating.")],
    vocab=[("Shared kernel", "A small part of the model shared by two contexts, changed only together."),
           ("Partnership", "Two teams that coordinate plans and releases and succeed or fail together."),
           ("Common library", "The usual (often over-large) implementation of a shared kernel."),
           ("Lockstep release", "Deploying two components together because they depend on the same change."),
           ("Duplication", "Keeping separate copies instead of sharing: often the cheaper choice."),
           ("Schema registry", "A modern way to share event shapes without sharing code.")],
    code=dict(file="packages/shared-kernel/index.ts", note="small, value types only", src="""
// Owned by: ordering-team AND shipping-team (CODEOWNERS requires both)
export type OrderId = string & { readonly __brand: "OrderId" };

export class Money {
  private constructor(readonly cents: bigint, readonly currency: "EUR" | "GBP") {}
  static of(cents: bigint, currency: "EUR" | "GBP") { return new Money(cents, currency); }
  add(o: Money) { /* same currency only */ return Money.of(this.cents + o.cents, this.currency); }
}

export type Address = Readonly<{ street: string; postcode: string; city: string; country: string }>;

// NOT here: Order, Customer, Product. Those belong to one context each.
"""),
    tools="tools: a small package in a monorepo with CODEOWNERS listing both teams, both pipelines triggered on change, or a schema registry (Confluent, Apicurio) for shared event shapes instead of shared code.",
    gains=["<b>No duplicate code</b> for truly shared concepts.",
           "<b>Consistent</b> money, address and ID handling.",
           "<b>Close collaboration</b> where it really helps.",
           "<b>Partnership</b>: two teams move as one on joint goals."],
    losses=["<b>Coupling</b>: neither team can change it alone.",
            "<b>Coordination cost</b> on every change.",
            "<b>Tends to grow</b> into a shared model.",
            "<b>Lockstep releases</b> if not versioned carefully."],
    baseline="Each line compares <b>each context keeping its own copy of shared types</b> to <b>a small jointly-owned shared kernel</b>.",
    ratings=[(3, 3, "One copy instead of two, but one more thing to understand."),
             (3, 4, "Shared concepts mean the same on both sides."),
             (3, 4, "Money and IDs handled the same way everywhere."),
             (4, 2, "Every change needs both teams."),
             (3, 3, "Neutral."),
             (4, 2, "The kernel couples the two contexts by design."),
             (3, 3, "Neutral."),
             (3, 3, "Less duplication, more coordination."),
             (4, 2, "Two teams must move together on it.")],
    pitfalls=[("The common library that ate everything", "Started with Money, now holds Order with fields for six services.", "value types only; entities stay in their context."),
              ("Shared kernel across many teams", "Ten teams share it, so nothing ever changes.", "two teams, maybe three; beyond that, publish a language instead."),
              ("One side changes it alone", "A “small fix” breaks the other team's build.", "CODEOWNERS with both teams, both test suites in CI."),
              ("Sharing to avoid five lines of code", "Coupling two teams to save a tiny copy.", "duplication of small value types is usually cheaper.")],
    use=["Two teams that already work closely, sharing a few important value types.",
         "Concepts that must be identical on both sides (money rounding, ID formats).",
         "Partnership: two contexts that must deliver a feature together."],
    skip=["Many teams, or teams that rarely talk.",
          "When a copy of a few small types would do.",
          "To share entities or aggregates (use events or an API)."],
    related=["<b>Context Map</b>", "<b>Customer–Supplier &amp; Conformist</b>", "<b>Open Host Service &amp; Published Language</b>", "<b>Value Object</b>"],
    quiz=[("What belongs in a shared kernel?", "A small set of shared types, usually value types and IDs, owned jointly by two teams."),
          ("What's the difference between shared kernel and partnership?", "Shared kernel is shared code or model; partnership is two teams coordinating plans and releases. They often come together."),
          ("What's the main risk?", "It grows into a shared model that couples the contexts and forces lockstep changes."),
          ("What's often a better alternative?", "Each context keeps its own small copy, or shares only an event schema through a published language.")],
    quiz_sit=[("Your company's <code>@acme/common</code> package is used by twelve services and contains <code>Order</code>, <code>Customer</code> and <code>Product</code>. Upgrading it takes a month of coordination. What do you do?",
               "Shrink it: move each entity into the context that owns it, let others keep their own small read models filled by events, and leave only value types (Money, IDs) in a much smaller kernel, or replace sharing code with a published event schema.")],
    try_it="Look at a shared or “common” package in a codebase you know. Sort its types into “value type” and “belongs to one context”. For the second group, name the owning context and sketch how others could get that data instead.",
    then_now=dict(src="Evans, 2003", verdict="rethought",
                  then="Evans offered the shared kernel as a way for two closely working teams to share part of a model, with a continuous integration process covering both.",
                  now="With microservices, a shared code library became a known trap: it couples deployments. Teams today prefer duplication, or sharing <b>schemas</b> (Protobuf, JSON Schema, a schema registry) instead of code. Partnership survived as a team pattern; the shared kernel survived only in small doses.",
                  take="The idea holds, but keep it tiny. Share schemas, not classes, wherever you can."),
    remember="Share the <span class=\"hl\">garden wall</span>, never the <span class=\"hl\">house</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14.",
             "Sam Newman, <i>Building Microservices</i>, 2nd ed. (2021), ch. 5 (shared libraries).",
             "DDD Crew, “Context Mapping” (github.com/ddd-crew/context-mapping).",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 4."],
)

# ------------------------------------------------------------------ 08 Anti-Corruption Layer
acl_problem = Doodle(760, 270, "Doodle of a legacy model leaking into a new system. The old ERP has a customer table called KNA1 with fields like KUNNR and LIFSD. The new Ordering code starts using those names directly: if customer.LIFSD equals 01, block delivery. Soon the ERP's odd codes and names are everywhere in the new code.",
                    "The old ERP's names and codes (KUNNR, LIFSD = '01') spread through the new code.")
acl_problem.box(20, 40, 230, 130, "old ERP", "paper", sub="KNA1 · KUNNR · LIFSD")
acl_problem.arrow(254, 105, 330, 105, color="red")
acl_problem.box(340, 30, 400, 160, None, "green")
acl_problem.head(540, 64, "new Ordering")
acl_problem.text(540, 104, "if (c.LIFSD === '01') …")
acl_problem.text(540, 140, "order.kunnr = …")
acl_problem.note(380, 240, "the old model is taking over the new one", "red")

acl_analogy = Doodle(760, 250, "Doodle of an interpreter at a business meeting. The visiting delegation speaks its own language; the interpreter translates both ways at the edge of the table, so the host team never has to learn the visitors' grammar, and misunderstandings are caught by one person whose job is exactly that.",
                     "An interpreter at the edge of the table: each side keeps its own language.")
acl_analogy.box(20, 60, 220, 90, "visitors", "paper", sub="their language")
acl_analogy.box(290, 50, 180, 110, "interpreter", "y", sub="both ways")
acl_analogy.box(520, 60, 220, 90, "hosts", "green", sub="our language")
acl_analogy.arrow(244, 105, 286, 105, both=True)
acl_analogy.arrow(474, 105, 516, 105, both=True)
acl_analogy.note(380, 220, "nobody has to learn the other's grammar", "pen")

acl_how = Doodle(760, 330, "An anti-corruption layer between Ordering and the legacy ERP. Inside the layer: a facade that calls the ERP, adapters, and translators that turn ERP records like KNA1 into Ordering's Customer with a deliveryBlocked boolean, and back. Ordering's model only sees its own types. A test checks that nothing outside the layer imports the ERP client.",
                  "The layer translates both ways. Ordering only ever sees its own types.")
acl_how.box(20, 40, 200, 220, "ERP", "paper", sub="KNA1 · LIFSD")
acl_how.box(260, 30, 240, 240, None, "y", dash=True)
acl_how.head(380, 62, "ACL")
acl_how.box(280, 84, 200, 50, "facade", "paper", size=16)
acl_how.box(280, 146, 200, 50, "translator", "paper", size=16)
acl_how.box(280, 208, 200, 50, "adapter", "paper", size=16)
acl_how.box(540, 40, 200, 220, "Ordering", "green", sub="deliveryBlocked")
acl_how.arrow(224, 150, 256, 150, both=True)
acl_how.arrow(504, 150, 536, 150, both=True)
acl_how.note(380, 310, "a test fails if anything else imports the ERP client", "pen")

ACL = dict(
    slug="anti-corruption-layer",
    kicker="a.k.a. “the interpreter at the edge of the table”",
    tldr="When you must integrate with a model you don't like and can't change (legacy, a vendor, another team's mess), put a <b>translation layer</b> at your border. It talks to the other system in <b>its</b> terms and gives your code only <b>your</b> types, in <b>your</b> language. The other model's names, codes and quirks <b>stop at the layer</b>, so your model stays clean and the other system stays <b>replaceable</b>.",
    chips=[("Family", "context relationship"), ("From", "Evans (2003), ch. 14"), ("Made of", "facades, adapters, translators"), ("Pairs with", "strangler fig, conformist (the alternative)")],
    problem="""  <p class="lead">Integrating directly with a poor or foreign model lets <span class="hl-pink">its names and quirks leak</span> into your code, until your model is theirs.</p>
  <ul>
    <li>Legacy field names and magic codes appear in new code.</li>
    <li>Rules are written in the other system's terms: <code>LIFSD === '01'</code>.</li>
    <li>Replacing the old system later means touching everything.</li>
  </ul>""",
    problem_figs=[acl_problem],
    analogy_side="the interpreter",
    analogy="""  <p>At an international meeting, an <b>interpreter</b> sits at the edge of the table and translates <b>both ways</b>. The hosts never learn the visitors' grammar; the visitors never learn the hosts'. If something is ambiguous, one person, whose job it is, sorts it out.</p>
  <ul>
    <li>The interpreter is the <b>anti-corruption layer</b>.</li>
    <li>Each side keeps its <b>own language</b>.</li>
    <li>A new delegation means a new interpreter, not new hosts.</li>
  </ul>""",
    analogy_figs=[acl_analogy],
    map=[("Visitors' language", "The legacy or vendor model: KNA1, LIFSD"),
         ("Hosts' language", "Your model: <code>Customer.deliveryBlocked</code>"),
         ("The interpreter", "Facade + translator + adapter at your border"),
         ("Translating both ways", "Mapping requests out and responses back"),
         ("A new delegation", "Swapping the vendor changes only the layer")],
    how_side="translate at the border, both ways",
    how="""  <p>An ACL is the opposite of <b>conformist</b>: it costs code, but keeps your model yours. It's also the main tool of the <b>strangler fig</b>: new code sits behind an ACL while the old system is replaced piece by piece.</p>""",
    how_figs=[acl_how],
    steps=[("Define your model first", "Write the types your code wants, in your language, ignoring the other system."),
           ("Wrap the other system", "A facade that hides its protocol, sessions and error codes."),
           ("Translate", "Pure functions that map their records to your types and back. Test them with real examples."),
           ("Expose a port", "Your code depends on an interface (<code>CustomerDirectory</code>), not on the facade."),
           ("Guard the border", "An architecture test fails if anything outside the layer imports the other system's client or types."),
           ("Translate events too", "Their webhooks become your domain events, in your words.")],
    vocab=[("Anti-corruption layer", "A translation layer that protects your model from another model."),
           ("Facade", "A simple interface over a complicated system."),
           ("Adapter", "Converts one interface to another."),
           ("Translator", "Maps data between two models."),
           ("Port", "The interface your domain code depends on; the ACL implements it."),
           ("Corruption", "The other model's concepts leaking into yours.")],
    code=dict(file="ordering/acl/erp-customers.ts", note="their words stop here", src="""
// Ordering's own port, in Ordering's language
export interface CustomerDirectory {
  find(id: CustomerId): Promise<Customer | undefined>;
}

// The ACL: the only place that knows about the ERP
export class ErpCustomerDirectory implements CustomerDirectory {
  constructor(private erp: ErpClient) {}
  async find(id: CustomerId) {
    const r = await this.erp.read("KNA1", { KUNNR: toErpNumber(id) });
    return r && toCustomer(r);
  }
}

const toCustomer = (r: Kna1Row): Customer => ({
  id: fromErpNumber(r.KUNNR),
  name: r.NAME1.trim(),
  deliveryBlocked: r.LIFSD === "01" || r.LIFSD === "02",   // ERP code -> our rule
});
"""),
    tools="tools: plain code (ports and adapters), an integration platform or API gateway for protocol translation, ArchUnit or dependency-cruiser to forbid imports of the other system's client outside the layer.",
    gains=["<b>Your model stays yours</b>, in your language.",
           "<b>The other system is replaceable</b>: only the layer changes.",
           "<b>One place</b> to understand the integration.",
           "<b>Testable</b>: translators are pure functions."],
    losses=["<b>More code</b> to write and maintain.",
            "<b>Translation can lose</b> or distort meaning.",
            "<b>Extra latency</b> if it's a separate service.",
            "<b>Needs discipline</b>: one shortcut import breaks it."],
    baseline="Each line compares <b>using the other system's model directly (conformist)</b> to <b>translating it in an anti-corruption layer</b>.",
    ratings=[(3, 3, "Clean model inside, one more layer to read."),
             (2, 5, "Your code speaks only your language."),
             (2, 4, "Odd codes are interpreted once, correctly, in one place."),
             (2, 4, "The other side changes; only the layer follows."),
             (2, 4, "Your domain tests use your types; translators have their own tests."),
             (1, 5, "The main gain: the other model can't reach your code."),
             (4, 3, "A little mapping cost, more if it's a separate service."),
             (4, 2, "Translators, facades and their tests."),
             (3, 4, "Teams on each side change their model alone.")],
    pitfalls=[("A layer that only renames", "Fields are copied 1:1 with new names; the old concepts survive.", "translate meaning, not just names (LIFSD codes → <code>deliveryBlocked</code>)."),
              ("Leaky shortcuts", "One team imports the ERP client “just this once”.", "an architecture test that fails the build."),
              ("One giant ACL for everything", "A central integration team becomes a bottleneck.", "each context owns the ACL at its own border."),
              ("Over-using it", "An ACL in front of a well-designed internal API that fits your model.", "if the upstream model is good, conforming is cheaper.")],
    use=["Integrating with legacy systems, ERPs or vendors with a different or poor model.",
         "Replacing a system gradually (with the strangler fig).",
         "Another team's model doesn't fit yours and they can't change it."],
    skip=["The upstream model is good and fits yours (conform).",
          "A short-lived integration you'll remove soon (weigh the cost)."],
    related=["<b>Customer–Supplier &amp; Conformist</b>", "<b>Context Map</b>", "<b>Strangler Fig</b> (Vol. 1)", "<b>Anti-Corruption Layer</b> (Ana, vol. 4)", "<b>SaaS &amp; Vendor Integration</b> (Ana, vol. 4)"],
    quiz=[("What does an anti-corruption layer protect?", "Your model and language, from another system's model leaking in."),
          ("What's the alternative relationship, and when is it better?", "Conformist: use the upstream model directly. Better when that model is good and fits yours."),
          ("Name three building blocks of an ACL.", "A facade over the other system, translators that map data, and adapters that implement your ports."),
          ("How does an ACL help when replacing a legacy system?", "Your code only depends on your own port, so the old system can be swapped behind the layer without changing your model.")],
    quiz_sit=[("A new team integrates with a CRM and their code is full of <code>crm_status_cd</code> and <code>acct__c</code>. The company plans to switch CRM next year. What do you ask them to change?",
               "Define their own Customer types and a port, and move every CRM name and code into an anti-corruption layer that translates both ways. Add an architecture test so only the layer imports the CRM client. Next year, only the layer is rewritten.")],
    try_it="Find one place where your code uses another system's field names or status codes directly. Define your own type for it, write a pure translator function with three example tests, and route all access through one adapter.",
    then_now=dict(src="Evans, 2003", verdict="core",
                  then="Evans described the ACL for integrating with legacy systems: a layer of facades, adapters and translators that let a new model talk to an old one without being corrupted by it.",
                  now="It's everywhere: in front of SaaS and ERP systems, in strangler-fig migrations, and in hexagonal architecture as an adapter behind a port. Architecture tests now enforce the border automatically.",
                  take="Still core, and even more common now that most systems integrate with several vendors."),
    remember="Let their words stop <span class=\"hl\">at the door</span>; inside, speak <span class=\"hl\">your own language</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14.",
             "Microsoft Azure Architecture Center, “Anti-corruption Layer pattern”.",
             "Martin Fowler, “StranglerFigApplication” (bliki, 2004, updated 2019).",
             "Vlad Khononov, <i>Learning Domain-Driven Design</i> (2021), ch. 4."],
)

# ------------------------------------------------------------------ 09 Open Host Service & Published Language
oh_problem = Doodle(760, 260, "Doodle of an upstream team building a custom integration for every consumer. Catalogue exposes one endpoint for the website, a CSV export for marketing, a different JSON for the app, and a nightly database dump for search. Every consumer change means a new variant. The team spends more time on integrations than on the catalogue.",
                    "One custom integration per consumer: the upstream team drowns in variants.")
oh_problem.box(20, 90, 200, 80, "Catalogue", "y", sub="4 integrations")
for i, t in enumerate(["web API", "CSV export", "app JSON", "DB dump"]):
    y = 20 + i * 56
    oh_problem.box(330, y, 180, 44, t, "pink", stroke="red", size=16)
    oh_problem.arrow(224, 130, 326, y + 22, color="red")
    oh_problem.text(620, y + 28, ["website", "marketing", "mobile", "search"][i])
oh_problem.note(380, 252, "every consumer change = a new variant", "red")

oh_analogy = Doodle(760, 250, "Doodle of a standard shipping container. A port doesn't build a special crane for every ship. It publishes one container standard, and every ship, truck and train that follows the standard can load and unload. The standard is documented, versioned and shared.",
                    "Ports don't build a crane per ship: they publish one container standard everybody follows.")
oh_analogy.icon("container", 40, 80, 1.8)
oh_analogy.note(470, 60, "one documented standard size", "pen")
oh_analogy.note(470, 110, "every ship, truck and train fits", "pen")
oh_analogy.note(470, 160, "the port isn't rebuilt per customer", "green")

oh_how = Doodle(760, 320, "Catalogue as an open host service. It offers one documented, versioned API and one set of events, described in OpenAPI and AsyncAPI with JSON Schemas: the published language. The website, mobile app, search and marketing all use the same interface. Breaking changes go into a new version with a deprecation period; consumers translate into their own models if they need to.",
                 "One documented, versioned API and event set for everyone; consumers translate if they need to.")
oh_how.box(20, 100, 200, 100, "Catalogue", "y", sub="open host")
oh_how.box(270, 70, 220, 160, None, "blue", dash=True)
oh_how.head(380, 104, "published language")
oh_how.text(380, 144, "OpenAPI v2")
oh_how.text(380, 176, "events · JSON Schema")
oh_how.text(380, 208, "versioned, documented")
oh_how.arrow(224, 150, 266, 150)
for i, t in enumerate(["website", "app", "search", "marketing"]):
    y = 40 + i * 62
    oh_how.box(560, y, 180, 46, t, "paper", size=16)
    oh_how.arrow(494, 150, 556, y + 23)
oh_how.note(380, 300, "breaking change → new version + deprecation period", "pen")

OPEN_HOST = dict(
    slug="open-host-service",
    kicker="a.k.a. “one container standard, not a crane per ship”",
    tldr="When many contexts need your data, don't build a custom integration for each. Offer an <b>open host service</b>: <b>one</b> well-documented API (and event stream) for everyone. Describe its data in a <b>published language</b>: a documented, versioned format like an OpenAPI spec, JSON Schemas or Protobuf. Consumers translate into their own model if they need to; you <b>version</b> carefully instead of breaking them.",
    chips=[("Family", "context relationship"), ("From", "Evans (2003), ch. 14"), ("Today", "OpenAPI, AsyncAPI, Protobuf, CloudEvents"), ("Pairs with", "API versioning, contract testing")],
    problem="""  <p class="lead">An upstream team that builds <span class="hl-pink">one integration per consumer</span> ends up maintaining integrations instead of its domain.</p>
  <ul>
    <li>An API for the website, a CSV for marketing, a dump for search.</li>
    <li>Each consumer's change means a new variant.</li>
    <li>Nobody knows which format is the “real” one.</li>
  </ul>""",
    problem_figs=[oh_problem],
    analogy_side="the shipping container",
    analogy="""  <p>A port doesn't build a special crane for every ship. It works with <b>one container standard</b>, documented and shared, and every ship, truck and train that follows it can load and unload. The port grows by handling more containers, not by rebuilding itself for each customer.</p>
  <ul>
    <li>The port's loading service is the <b>open host service</b>.</li>
    <li>The container standard is the <b>published language</b>.</li>
    <li>A new container size comes with a <b>transition period</b>.</li>
  </ul>""",
    analogy_figs=[oh_analogy],
    map=[("The port", "The upstream context (Catalogue)"),
         ("One loading service for all", "One API and event stream for every consumer"),
         ("The container standard", "OpenAPI / AsyncAPI / JSON Schema: the published language"),
         ("New container size, phased in", "A new API version with a deprecation period"),
         ("Repacking at the warehouse", "Consumers translating into their own model")],
    how_side="one interface, one documented language",
    how="""  <p>The published language should be <b>designed for integration</b>, not a dump of your internal model. Internals can change freely; the published language changes slowly and in versions.</p>""",
    how_figs=[oh_how],
    steps=[("Collect consumer needs", "What do all consumers actually need? Design for the common shape, not each one's wish."),
           ("Design the published language", "Resources and events in clear terms, separate from your internal classes."),
           ("Document it as a spec", "OpenAPI for requests, AsyncAPI and JSON Schema or Protobuf for events."),
           ("Version it", "Additive changes are free; breaking changes get a new version and a deprecation date."),
           ("Test it", "Consumer contract tests and schema compatibility checks in CI."),
           ("Retire variants", "Move old custom feeds onto the open host, one consumer at a time.")],
    vocab=[("Open host service", "A protocol or API offered to all consumers, instead of one integration each."),
           ("Published language", "A documented, shared format for exchanging data between contexts."),
           ("Schema", "A machine-readable description of a message or resource."),
           ("Backward compatible", "A change existing consumers can ignore safely."),
           ("Deprecation period", "Time during which old and new versions both work."),
           ("Schema registry", "A service storing event schemas and checking compatibility.")],
    code=dict(file="catalogue-events.asyncapi.yaml", note="the published language for events", plain=True, src="""
asyncapi: 3.0.0
info: { title: Catalogue events, version: 2.1.0 }
channels:
  productPublished:
    address: catalogue.product-published.v2
    messages:
      ProductPublished:
        payload:
          type: object
          required: [productId, title, price, publishedAt]
          properties:
            productId:   { type: string, format: uuid }
            title:       { type: string }
            price:       { $ref: "#/components/schemas/Money" }
            weightGrams: { type: integer, minimum: 0 }   # added in 2.1, optional
            publishedAt: { type: string, format: date-time }
"""),
    tools="tools: OpenAPI and AsyncAPI specs, JSON Schema, Protobuf or Avro, a schema registry with compatibility checks (Confluent, Apicurio, Buf), CloudEvents for event envelopes, and contract tests.",
    gains=["<b>One integration</b> to maintain, not one per consumer.",
           "<b>Self-service</b> for new consumers.",
           "<b>Internals can change</b> behind a stable language.",
           "<b>Clear documentation</b> and tooling from the spec."],
    losses=["<b>Designing for everyone</b> fits no one perfectly.",
            "<b>Versioning discipline</b> is needed.",
            "<b>Slower to change</b> than a private interface.",
            "<b>Consumers translate</b> into their own models."],
    baseline="Each line compares <b>a custom integration per consumer</b> to <b>one open host service with a published language</b>.",
    ratings=[(2, 4, "One interface to learn instead of four."),
             (3, 4, "The published language is designed and named with care."),
             (3, 4, "Schemas validate every message."),
             (2, 4, "Internals change freely behind the stable interface."),
             (3, 4, "Contract and schema checks run in CI."),
             (2, 4, "Consumers depend on the spec, not your internals."),
             (3, 3, "Neutral; some consumers get more data than they need."),
             (2, 3, "Specs and versioning, but no more variants."),
             (2, 5, "New consumers onboard without the upstream team.")],
    pitfalls=[("Publishing your internals", "The API is a JSON dump of the ORM classes.", "design the published language separately and map to it."),
              ("Breaking without versions", "A renamed field breaks every consumer the same day.", "additive changes only, or a new version with a deprecation period."),
              ("Bending for one consumer", "Special fields and endpoints for the loudest team.", "serve the common need; let a backend-for-frontend adapt it."),
              ("No spec, only code", "Consumers reverse-engineer payloads from logs.", "a spec in the repository, published as docs, checked in CI.")],
    use=["Many contexts or external partners need the same data.",
         "An upstream team spends much of its time on integrations.",
         "Events that several teams subscribe to."],
    skip=["A single consumer that you work closely with (customer–supplier is enough).",
          "Internal module calls inside one context."],
    related=["<b>Context Map</b>", "<b>Customer–Supplier &amp; Conformist</b>", "<b>Contract Testing</b> (Vol. 4)", "<b>API-First Design</b> (Ana, vol. 4)", "<b>API Versioning Strategy</b> (Ana, vol. 4)"],
    quiz=[("What's the difference between an open host service and a published language?", "The open host service is the one interface offered to all; the published language is the documented format of the data it exchanges."),
          ("Why shouldn't the published language be your internal model?", "Then every internal change breaks consumers. A separate, designed language lets internals change freely."),
          ("Give three modern forms of a published language.", "OpenAPI specs, AsyncAPI with JSON Schema, Protobuf or Avro, CloudEvents."),
          ("How do you make a breaking change?", "Publish a new version alongside the old one, with a deprecation period and a migration guide.")],
    quiz_sit=[("Search, marketing and the app each ask the Catalogue team for a slightly different product feed. The team has five feeds and no time for catalogue work. What do you propose?",
               "One open host service: a documented, versioned product API and a <code>ProductPublished</code> event with a schema in a registry. Migrate consumers onto it one by one and retire the custom feeds; consumers that need a special shape adapt it on their side.")],
    try_it="Write an OpenAPI or AsyncAPI spec for one API or event your team owns. Compare it with the internal classes: mark every field that leaks an internal detail, and decide which ones to rename, hide or keep.",
    then_now=dict(src="Evans, 2003", verdict="built-in",
                  then="Evans suggested an open protocol for all consumers and a well-documented shared language for exchange; his examples were industry formats like chemical markup or XML standards.",
                  now="This is how APIs are built today: OpenAPI and AsyncAPI specs, JSON Schema and Protobuf, schema registries that refuse incompatible changes, CloudEvents envelopes. The pattern became the default toolset.",
                  take="Built in now: you rarely name it, but every well-run public API and event stream is one."),
    remember="Publish one <span class=\"hl\">container standard</span>; don't build a <span class=\"hl\">crane per ship</span>.",
    sources=["Eric Evans, <i>Domain-Driven Design</i> (2003), ch. 14.",
             "AsyncAPI specification 3.0 (asyncapi.com).",
             "OpenAPI Specification 3.1 (spec.openapis.org).",
             "CloudEvents specification 1.0 (cloudevents.io)."],
)

NOTES = [CONTEXT_MAP, CUSTOMER_SUPPLIER, SHARED_KERNEL, ACL, OPEN_HOST]
