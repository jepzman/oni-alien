# Series 2 · The Solution Architect's Notebook · Vol. 3 · Diagrams.
# Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 C4 Model
c4_problem = Doodle(760, 290, "Doodle of Larder's wiki in October 2026: eleven architecture diagrams, each drawn differently. Some use clouds, some cylinders, some coloured boxes with no legend. One still shows Dispatch inside Larder Core, a year out of date. A new engineer asks which one is true.",
                    "Eleven diagrams, eleven notations, one of them a year out of date. “Which one is true?”")
shapes = [(20, 30, 150, 60, "blue"), (200, 20, 120, 80, "y"), (350, 40, 170, 50, "pink"), (550, 26, 190, 70, "paper"),
          (40, 130, 130, 70, "green"), (210, 140, 160, 50, "paper"), (400, 120, 140, 90, "blue"), (580, 130, 150, 60, "y")]
for i, (x, y, w, h, f) in enumerate(shapes):
    c4_problem.box(x, y, w, h, None, f, dash=i % 3 == 0, rx=4 + (i % 4) * 8)
c4_problem.text(470, 170, "Dispatch ⊂ Core?", "t t-red", size=13)
c4_problem.note(160, 250, "11 diagrams · no legends", "red")
c4_problem.box(450, 228, 290, 50, "new hire: “which is true?”", "y", size=15)

c4_analogy = Doodle(760, 260, "Doodle of a map app zooming in four steps: the country, then the city, then the street, then the house. Each level has its own detail, and you only zoom as far as your question needs.",
                    "A map app: country, city, street, house. Zoom only as far as the question needs.")
for i, (t, s, w, f) in enumerate([("country", "where's the city?", 180, "paper"), ("city", "which district?", 160, "blue"), ("street", "which building?", 150, "y"), ("house", "which door?", 140, "green")]):
    x = 20 + i * 186
    c4_analogy.box(x, 50, w - 10, 110, t, f, sub=s, size=18, subsize=14)
    if i < 3:
        c4_analogy.arrow(x + w - 6, 105, x + 182, 105)
c4_analogy.note(380, 220, "zoom in: four levels, one map", "pen")

c4_how = Doodle(760, 380, "Larder's C4 diagrams. Level 1, context: the Larder platform, with customers, pickers, couriers, offices, and the outside systems: StockPilot, two payment providers, the billing service and the helpdesk. Level 2, containers: customer apps, picker app, Larder Core (modular monolith), Dispatch with Engine A, Postgres and Kafka. Level 3, components: the modules inside Larder Core, such as Ordering, Payments, Stock and Fulfilment. Level 4, code: rarely drawn; the code is the diagram.",
                "Four levels: context for everyone, containers for engineers, components for one team, code almost never.")
levels = [("1 · context", "Larder + people + 5 outside systems", "everyone", "paper"),
          ("2 · containers", "apps · Core · Dispatch · Postgres · Kafka", "engineers, ops", "blue"),
          ("3 · components", "Core's modules: Ordering, Stock…", "one team", "y"),
          ("4 · code", "rarely drawn: the code is the diagram", "nobody, mostly", "green")]
for i, (lvl, what, who, f) in enumerate(levels):
    y = 14 + i * 86
    inset = i * 28
    c4_how.box(14 + inset, y, 560 - inset * 2, 72, None, f, rx=8)
    c4_how.text(30 + inset, y + 30, lvl, "t-head", anchor="start", size=17)
    c4_how.text(30 + inset, y + 56, what, anchor="start", size=15)
    c4_how.note(660, y + 44, who, "pen", size=17)
c4_how.note(660, 14 + 4 * 86 + 6, "for whom", "green", size=17)

C4 = dict(
    slug="c4-model",
    kicker="a.k.a. “zoom levels on a map”",
    tldr="Most architecture diagrams fail because nobody can tell what a box is or how far in we've zoomed. The <b>C4 model</b> gives four fixed zoom levels: <b>Context</b> (the system and the people and systems around it), <b>Containers</b> (the deployable things: apps, services, databases), <b>Components</b> (the parts inside one container) and <b>Code</b> (almost never drawn). Every box says its <b>name, type, technology and job</b>, every arrow says what flows, and every diagram has a <b>title and a legend</b>.",
    chips=[("Family", "diagrams"), ("Origin", "Simon Brown, “The C4 model for visualising software architecture” (2006–2018)"), ("Lives in", "docs/architecture/ as diagrams-as-code"), ("Pairs with", "system context diagram, docs as code, living diagrams")],
    problem_side="Larder, 6 October 2026",
    problem="""  <p class="lead">Larder now has 18 engineers, four of them new this year. The wiki holds <b>eleven architecture diagrams</b>: clouds, cylinders, coloured boxes with no legend, arrows that might mean calls or data or “talks to, somehow”. One still shows <b>Dispatch inside Larder Core</b>, a year after it moved out. A new engineer asks Ana the simplest question: <span class="hl-pink">which one is true?</span></p>
  <ul>
    <li>Every author invents a notation, so every diagram needs its author to explain it.</li>
    <li>Diagrams mix zoom levels: a database next to a whole partner company.</li>
    <li>Nobody knows which diagrams are current, so nobody trusts any.</li>
  </ul>""",
    problem_figs=[c4_problem],
    analogy_side="zoom levels on a map",
    analogy="""  <p>A map app doesn't show every house on the map of Europe. You zoom: <b>country</b>, <b>city</b>, <b>street</b>, <b>house</b>. Each level shows what that level's question needs, the symbols are the same every time, and you only zoom as far as you need. Nobody draws their own symbols for motorways.</p>""",
    analogy_figs=[c4_analogy],
    map=[("The country", "Context: Larder and everything around it"),
         ("The city", "Containers: apps, Core, Dispatch, databases"),
         ("The street", "Components: the modules inside Larder Core"),
         ("The house", "Code: rarely needed on a diagram"),
         ("The map's legend", "Every box's type and technology, every arrow's label")],
    how_side="four levels, one notation",
    how="""  <p>Ana replaced the eleven diagrams with <b>four</b>: one context diagram (updated from Vol. 1's), one container diagram, and component diagrams for Larder Core and Dispatch. Each box says what it is and what it's built with; each arrow says what it carries. The old diagrams went into an archive folder with a note pointing to the new ones.</p>""",
    how_figs=[c4_how],
    steps=[("Start at context", "One box for your system, the people who use it, the systems it talks to."),
           ("Draw the containers", "Every separately deployed or run thing: apps, services, databases, queues."),
           ("Components only where needed", "Inside a container that's big or contested, like Larder Core."),
           ("Label everything", "Box: name, type, technology, one-line job. Arrow: what flows, how."),
           ("Title and legend on every diagram", "Scope, level, date, and what shapes and colours mean."),
           ("Retire the rest", "Archive old diagrams with a link to the new ones.")],
    vocab=[("Context diagram", "Level 1: the system, its users and neighbouring systems."),
           ("Container", "Level 2: a deployable or runnable unit: app, service, database."),
           ("Component", "Level 3: a grouping inside one container."),
           ("Supplementary diagram", "Sequence, deployment or data views that add to C4."),
           ("Notation", "The agreed meaning of shapes, lines and colours."),
           ("Legend", "The key that explains the notation on each diagram.")],
    code=dict(file="docs/architecture/c4/containers.md", note="the container list behind Larder's level-2 diagram", plain=True, src="""
# Larder · containers (C4 level 2)                         updated 6 Oct 2026 · owner: Ana

| Container        | Type                  | Technology                | Job                                   |
|------------------|-----------------------|---------------------------|---------------------------------------|
| Customer apps    | mobile + web app      | React Native, web shop    | browse, order, approve swaps, track   |
| Picker app       | mobile app (handheld) | React Native, offline     | pick and pack in the store            |
| Larder Core      | modular monolith      | Python, Django            | catalogue, pricing, ordering, payments,|
|                  |                       |                           | stock, fulfilment, customer care      |
| Dispatch         | service               | Python + routing Engine A | couriers, vans, assignment, tracking  |
| Core database    | database              | managed Postgres          | Core's modules, one schema each       |
| Event bus        | message broker        | managed Kafka             | events between Core and Dispatch      |

External: StockPilot (warehouse) · payment providers ×2 · billing service · helpdesk
Arrows: label with what flows and how, e.g. "order.ready_for_dispatch (Kafka)".
"""),
    tools="tools: Structurizr (DSL and site), C4-PlantUML, Mermaid's C4 diagrams, IcePanel, draw.io with the C4 shape library. Pick one and use it everywhere.",
    gains=["<b>One notation</b>: anyone can read any diagram.",
           "<b>Right detail for the reader</b>: context for executives, components for a team.",
           "<b>Fewer, trusted diagrams</b> instead of many stale ones.",
           "<b>Faster onboarding</b> for new engineers.",
           "<b>Tool support</b>: diagrams as code, generated sites."],
    losses=["<b>Learning the rules</b> takes an hour or two.",
            "<b>Not everything fits</b>: flows and deployment need extra diagrams.",
            "<b>Still goes stale</b> unless kept as code and reviewed.",
            "<b>Tempting to draw every level</b> for every container."],
    baseline="Each line compares <b>freehand diagrams, each with its own notation and zoom level</b> to <b>C4: four fixed levels, labelled boxes and arrows, a title and legend on every diagram</b>.",
    ratings=[(2, 5, "Any engineer can read any diagram."),
             (2, 4, "Executives see context; engineers see containers."),
             (3, 4, "Less time arguing about what a box means."),
             (3, 3, "Clearer pictures expose some risks."),
             (3, 3, "Doesn't change how the system can change."),
             (2, 4, "Diagrams are dated, owned and kept in the repo."),
             (3, 3, "Containers show the paid services clearly."),
             (3, 4, "Four diagrams instead of eleven."),
             (2, 4, "Teams draw their own components in the same notation.")],
    pitfalls=[("Mixed levels", "A database next to a partner company.", "one level per diagram; zoom on a separate one."),
              ("Unlabelled arrows", "Lines that mean “related somehow”.", "every arrow says what flows and how."),
              ("No legend", "Colours that only the author understands.", "title, scope and legend on every diagram."),
              ("Drawing every level", "Component diagrams nobody reads.", "components only where a container is big or contested.")],
    use=["Onboarding and shared understanding of a system.",
         "Replacing a pile of inconsistent diagrams.",
         "Explaining a system to people at different levels.",
         "Before a design discussion or review."],
    skip=["Code-level detail: read the code.",
          "Runtime flows and infrastructure: add sequence and deployment diagrams."],
    related=["<b>Views &amp; viewpoints (4+1)</b> (this volume)", "<b>Docs as code</b> (this volume)", "<b>Living diagrams</b> (this volume)", "<b>System context diagram</b> (Vol. 1)"],
    quiz=[("What are the four C4 levels?", "Context, Containers, Components, Code."),
          ("What's a container in C4?", "Something separately deployed or run: an app, a service, a database, a queue."),
          ("What must every box say?", "Its name, type, technology and job."),
          ("Which level is rarely drawn?", "Code: the code itself is the diagram.")],
    try_it="Find every architecture diagram your team has. Redraw just two of them in C4: one context and one container diagram, with labelled boxes and arrows, a title and a legend. Ask a new joiner which version helps them more, then archive the old ones.",
    remember="Zoom like a <span class=\"hl\">map</span>: country, city, street, house. Label every <span class=\"hl\">box and arrow</span>.",
    sources=["Simon Brown, <i>Software Architecture for Developers</i>, vol. 2 (2018), and c4model.com.",
             "Simon Brown, “The C4 model for visualising software architecture” (InfoQ, 2018).",
             "Structurizr documentation (structurizr.com).",
             "Eoin Woods, “Software Architecture Visualisation” (talks, 2016–)."],
)

# ------------------------------------------------------------------ 02 Views & Viewpoints (4+1)
vv_problem = Doodle(760, 280, "Doodle of four people asking Ana different questions about the same system in October 2026. Lena, the data protection officer: where does customer data go? Joost: what happens in the store when the Wi-Fi drops? Ben: which module owns what? Eli: what runs where? The container diagram answers none of them well.",
                    "Four people, four questions, one diagram that answers none of them well.")
for i, (who, q, f) in enumerate([("Lena", "“where does personal data go?”", "pink"), ("Joost", "“the Wi-Fi drops: then what?”", "y"), ("Ben", "“which module owns what?”", "blue"), ("Eli", "“what runs where?”", "paper")]):
    x, y = (20 if i % 2 == 0 else 400), (24 if i < 2 else 130)
    vv_problem.box(x, y, 340, 80, who, f, sub=q)
vv_problem.note(380, 262, "the container diagram answers none of them", "red")

vv_analogy = Doodle(760, 260, "Doodle of four drawings of the same house: a floor plan for the family, an electrical plan for the electrician, a plumbing plan for the plumber and an elevation for the planning office. Same house, different drawings for different trades.",
                     "One house, four drawings: floor plan, wiring, plumbing, the front. Each trade gets the drawing it needs.")
for i, (t, s, f) in enumerate([("floor plan", "the family", "y"), ("wiring", "the electrician", "blue"), ("plumbing", "the plumber", "green"), ("the front", "planning office", "paper")]):
    x = 20 + i * 186
    vv_analogy.icon("frame" if i == 3 else ("plug" if i == 1 else ("bucket" if i == 2 else "map")), x + 52, 18, 1.1)
    vv_analogy.box(x, 100, 166, 80, t, f, sub=s, size=17, subsize=15)
vv_analogy.note(380, 236, "same house, a drawing per trade", "pen")

vv_how = Doodle(760, 360, "Kruchten's 4+1 views as Larder uses them. Logical view: the modules and what they own, for Ben and the teams. Process view: what happens at runtime, the flows and events, for Joost and on-call. Development view: repositories and teams, for engineers. Physical view: what runs where, for Eli. In the middle, scenarios that tie them together, such as an express order with a substitution. Larder adds a data view for Lena: where personal data lives and flows.",
                "Four views and the scenarios that tie them together, plus the one view Larder needed most: data, for Lena.")
cx, cy = 380, 170
for (t, s, x, y, f) in [("logical", "modules · Ben", 230, 22, "blue"), ("process", "flows, events · Joost", 530, 140, "y"),
                        ("development", "repos, teams", 230, 258, "paper"), ("physical", "what runs where · Eli", 0, 140, "green")]:
    vv_how.box(x + 14, y, 280 - (60 if x in (0, 530) else 0), 70, t, f, sub=s, size=17, subsize=14)
vv_how.circle(cx, cy, 52, fill="pink", label="+1", sub="scenarios")
vv_how.box(560, 270, 186, 70, "+ data view", "pink", sub="for Lena", stroke="red", size=16)
vv_how.note(380, 244, "e.g. an express order with a swap", "pen", size=15)

VIEWS = dict(
    slug="views-viewpoints",
    kicker="a.k.a. “a drawing for each trade”",
    tldr="No single diagram can answer every stakeholder's question. A <b>viewpoint</b> is a kind of question (where does data flow? what runs where?); a <b>view</b> is the drawing that answers it for your system. Kruchten's <b>4+1</b> gives a starting set: <b>logical</b> (what the parts are), <b>process</b> (what happens at runtime), <b>development</b> (how code and teams are organised), <b>physical</b> (what runs where), tied together by <b>scenarios</b>. Add the views your stakeholders actually ask for, such as a <b>data view</b> for the DPO.",
    chips=[("Family", "diagrams"), ("Origin", "Philippe Kruchten, “The 4+1 View Model of Architecture” (IEEE Software, 1995); ISO/IEC/IEEE 42010"), ("Lives in", "docs/architecture/views/, one page per view"), ("Pairs with", "C4 model, stakeholder map, sequence and deployment diagrams")],
    problem_side="Larder, 13 October 2026",
    problem="""  <p class="lead">The new container diagram is popular, so everyone brings Ana their question. <b>Lena</b>, the DPO, needs to know <b>where customer data goes</b> before Larder for Business signs more clients. <b>Joost</b> wants to know what happens in a store <b>when the Wi-Fi drops</b>. <b>Ben</b> asks which module owns business accounts. <b>Eli</b> asks what runs where. <span class="hl-pink">The one diagram answers none of them well</span>, and adding everything to it would make it unreadable.</p>
  <ul>
    <li>One “master diagram” tries to answer every question and answers none.</li>
    <li>Some stakeholders (legal, operations) never get a picture made for them.</li>
    <li>Questions about data, runtime and infrastructure need different drawings.</li>
  </ul>""",
    problem_figs=[vv_problem],
    analogy_side="a drawing for each trade",
    analogy="""  <p>A house has a <b>floor plan</b> for the family, a <b>wiring plan</b> for the electrician, a <b>plumbing plan</b> for the plumber and an <b>elevation</b> for the planning office. It's one house; each trade gets the drawing that answers its questions. Nobody puts the pipes on the family's floor plan.</p>""",
    analogy_figs=[vv_analogy],
    map=[("The floor plan", "Logical view: modules and what they own"),
         ("The wiring plan", "Process view: flows and events at runtime"),
         ("The plumbing plan", "Data view: where personal data lives and flows"),
         ("The elevation for planners", "Physical view: what runs where, for ops"),
         ("Walking through the house", "Scenarios: an express order with a substitution")],
    how_side="a view per question",
    how="""  <p>Ana listed the questions first, then picked views to answer them: the <b>logical</b> view (modules and ownership) for the teams, the <b>process</b> view (an order's journey, with the store offline) for Joost, the <b>physical</b> view for Eli, and a <b>data view</b> for Lena that traced every place a customer's address and phone number go, including the helpdesk and the billing service. Two <b>scenarios</b> tie them together.</p>""",
    how_figs=[vv_how],
    steps=[("List the stakeholders' questions", "From the stakeholder map: what does each person need to know?"),
           ("Group them into viewpoints", "Structure, runtime, code and teams, infrastructure, data, security."),
           ("Draw one view per viewpoint", "Only the views someone asked for. Reuse C4 notation where it fits."),
           ("Tie them with scenarios", "Two or three key journeys walked through every view."),
           ("Name each view's audience", "On the page: “for Lena”, “for on-call”."),
           ("Check views agree", "A module in the logical view must appear in the physical view too.")],
    vocab=[("Viewpoint", "A kind of question and the conventions for answering it."),
           ("View", "The drawing that answers a viewpoint for this system."),
           ("4+1", "Logical, process, development, physical, plus scenarios."),
           ("Scenario", "A key journey walked through every view."),
           ("Data view", "Where data, especially personal data, lives and flows."),
           ("ISO 42010", "The standard for describing architectures with views.")],
    code=dict(file="docs/architecture/views/README.md", note="Larder's views and who they're for", plain=True, src="""
# Architecture views                                       owner: Ana · Oct 2026

| View          | Answers                                   | For            | Drawn as                 |
|---------------|-------------------------------------------|----------------|--------------------------|
| Logical       | which modules exist, what each owns       | teams, Ben     | C4 components (Core)     |
| Process       | what happens at runtime, in what order    | Joost, on-call | sequence diagrams        |
| Development   | repos, pipelines, which team owns what    | engineers      | table + C4 containers    |
| Physical      | what runs where, networks, regions        | Eli, on-call   | deployment diagram       |
| Data          | where personal data lives and flows       | Lena (DPO)     | data-flow diagram        |

Scenarios walked through every view:
  S1 Express order with a substitution, Amsterdam, Friday 18:00
  S2 Korenwolf's weekly standing order, delivered 07:00–09:00
  S3 Noord's Wi-Fi drops for 20 minutes during picking
"""),
    tools="tools: the same diagram tool as for C4 (Structurizr can hold several views of one model); data-flow diagrams in draw.io or Mermaid. arc42 has sections for each view.",
    gains=["<b>Each stakeholder gets an answer</b> in their terms.",
           "<b>Legal and operations</b> finally have pictures.",
           "<b>Simpler diagrams</b>: each does one job.",
           "<b>Scenarios check consistency</b> across views.",
           "<b>Gaps show up</b>: the helpdesk held addresses nobody listed."],
    losses=["<b>More diagrams</b> to keep current.",
            "<b>Views can disagree</b> if maintained separately.",
            "<b>Over-documenting</b> if you draw views nobody asked for.",
            "<b>Vocabulary</b> (viewpoint vs view) confuses at first."],
    baseline="Each line compares <b>one master diagram for everyone</b> to <b>views chosen for the stakeholders' questions, tied together by a few scenarios</b>.",
    ratings=[(2, 4, "Each view is simple enough to read."),
             (2, 5, "Lena, Joost, Ben and Eli each get their answer."),
             (3, 4, "Questions answered without a meeting."),
             (2, 4, "The data view found an unlisted copy of addresses."),
             (3, 3, "Doesn't change adaptability."),
             (2, 4, "Views are dated and linked from the docs."),
             (3, 3, "The physical view shows what's paid for."),
             (3, 3, "Several diagrams to maintain."),
             (3, 4, "Teams answer stakeholder questions with the views.")],
    pitfalls=[("The master diagram", "Everything on one page.", "one view per question, linked together."),
              ("Views nobody asked for", "A development view nobody reads.", "start from stakeholders' questions."),
              ("No scenarios", "Views that quietly disagree.", "walk two or three journeys through every view."),
              ("Forgetting data", "Nobody can say where addresses go.", "draw a data view whenever personal data is involved.")],
    use=["Systems with many kinds of stakeholders.",
         "Before a privacy review or audit.",
         "When one diagram keeps growing.",
         "Onboarding operations and on-call staff."],
    skip=["Small systems where one context diagram answers everything.",
          "Views nobody has a question for."],
    related=["<b>C4 model</b> (this volume)", "<b>Sequence &amp; flow diagrams</b> (this volume)", "<b>Deployment diagrams</b> (this volume)", "<b>Data classification &amp; residency</b> (Vol. 5)"],
    quiz=[("What's the difference between a viewpoint and a view?", "A viewpoint is a kind of question; a view is the drawing that answers it for your system."),
          ("Name the 4+1 views.", "Logical, process, development, physical, plus scenarios."),
          ("Which view did Larder add, and for whom?", "A data view, for Lena, the DPO."),
          ("What are scenarios for?", "Walking key journeys through every view, which ties them together and checks they agree.")],
    try_it="Write down the questions three different stakeholders ask about your system. For each, sketch the simplest view that answers it, in 20 minutes each. Walk one scenario through all three and note anything that disagrees.",
    remember="One house, a <span class=\"hl\">drawing per trade</span>. Start from the <span class=\"hl\">question</span>.",
    sources=["Philippe Kruchten, “The 4+1 View Model of Architecture” (IEEE Software, 1995).",
             "Nick Rozanski and Eoin Woods, <i>Software Systems Architecture</i>, 2nd ed. (2011).",
             "ISO/IEC/IEEE 42010, “Architecture description” (2011, 2022).",
             "Paul Clements et al., <i>Documenting Software Architectures: Views and Beyond</i>, 2nd ed. (2010)."],
)

# ------------------------------------------------------------------ 03 Sequence & Flow Diagrams
sq_problem = Doodle(760, 280, "Doodle of Korenwolf's first scheduled business order in October 2026. The orders team assumed the billing line is created when the order is placed; the billing team assumed when it's delivered. Korenwolf was invoiced for three items that were out of stock and never delivered, and needed credit notes.",
                    "Two teams, two assumptions about “when”, and Korenwolf billed for three items it never got.")
sq_problem.box(20, 30, 330, 80, "orders team", "blue", sub="“bill when placed”")
sq_problem.box(410, 30, 330, 80, "billing team", "y", sub="“bill when delivered”")
sq_problem.arrow(185, 116, 330, 164, dash=True)
sq_problem.arrow(575, 116, 430, 164, dash=True)
sq_problem.box(160, 168, 440, 64, "Korenwolf billed for 3 missing items", "pink", stroke="red", size=16)
sq_problem.note(380, 264, "credit notes, and Ruben's first complaint", "red")

sq_analogy = Doodle(760, 260, "Doodle of a theatre stage manager's cue sheet: lights down, then music, then the curtain, then the actor enters. Each cue has an order and a trigger. Without the sheet, the curtain goes up in the dark.",
                     "A stage manager's cue sheet: who does what, in what order, on what trigger.")
for i, (t, f) in enumerate([("lights down", "paper"), ("music", "blue"), ("curtain", "y"), ("actor enters", "green")]):
    x = 20 + i * 186
    sq_analogy.box(x, 70, 166, 60, t, f, size=17)
    sq_analogy.note(x + 83, 50, f"cue {i + 1}", "pen", size=17)
    if i < 3:
        sq_analogy.arrow(x + 170, 100, x + 182, 100)
sq_analogy.icon("curtain", 330, 160, 1.2)
sq_analogy.note(600, 210, "no sheet: curtain up in the dark", "red", size=17)

sq_how = Doodle(760, 380, "The sequence diagram for a Korenwolf standing order, as agreed on 27 October 2026. Ordering creates the order at 05:00 and writes it to the outbox; the event goes through Kafka. Fulfilment at store Zuid picks from 05:30 and reports items short. Dispatch assigns a van at 06:30. The van delivers at about 08:10 and Dispatch publishes order delivered. Only then does Billing create the usage lines, for what was actually delivered.",
                 "Lifelines across, time down. The fix was one arrow: billing listens for “delivered”, not “placed”.")
lanes = [("Ordering", 80), ("Kafka", 230), ("Fulfilment", 380), ("Dispatch", 530), ("Billing", 680)]
for name, x in lanes:
    sq_how.box(x - 62, 10, 124, 40, name, "blue" if name != "Kafka" else "paper", size=15, rx=6)
    sq_how.line(f"M{x} 54 V340", dash=True, thin=True)
msgs = [(80, 230, 80, "05:00 order.placed"), (230, 380, 124, "→ pick at Zuid"), (380, 230, 168, "05:50 packed, 2 short"),
        (230, 530, 212, "→ assign a van"), (530, 230, 256, "08:10 order.delivered"), (230, 680, 300, "→ bill what was delivered")]
for x1, x2, y, label in msgs:
    green = "bill" in label
    sq_how.arrow(x1, y, x2, y, color="green" if green else "")
    sq_how.text(min(x1, x2) + 8, y - 8, label, "t-s" + (" t-green" if green else ""), anchor="start", size=15)
sq_how.note(380, 366, "time runs down the page", "pen", size=16)

SEQUENCE = dict(
    slug="sequence-flow",
    kicker="a.k.a. “the stage manager's cue sheet”",
    tldr="Box-and-arrow diagrams show <b>what</b> talks to what; they hide <b>when</b> and <b>in what order</b>. A <b>sequence diagram</b> puts the participants across the top as <b>lifelines</b>, runs <b>time down the page</b>, and shows each message in order, with its trigger. Draw one for every flow where order matters: anything with money, retries, events or several teams. The bugs it prevents live in the gaps between “then” and “meanwhile”.",
    chips=[("Family", "diagrams"), ("Origin", "message sequence charts (ITU, 1990s); UML sequence diagrams (1997)"), ("Lives in", "docs/architecture/flows/ as Mermaid or PlantUML"), ("Pairs with", "views &amp; viewpoints, event storming, transactional outbox")],
    problem_side="Larder, 27 October 2026",
    problem="""  <p class="lead">Korenwolf signed for three offices in September, and ADR 0014 moved business orders into Ordering as <b>scheduled orders</b>. The first week, the <b>orders team</b> assumed billing lines are created when an order is <b>placed</b>; the <b>billing team</b> assumed when it's <b>delivered</b>. Both were reasonable, neither was drawn. Korenwolf was <span class="hl-pink">invoiced for three items that were out of stock</span>, and Ruben, their procurement lead, sent his first complaint.</p>
  <ul>
    <li>Container diagrams don't show order, timing or triggers.</li>
    <li>Each team pictures the flow from its own side.</li>
    <li>Money flows break silently when “when” is assumed.</li>
  </ul>""",
    problem_figs=[sq_problem],
    analogy_side="the stage manager's cue sheet",
    analogy="""  <p>A theatre runs on a <b>cue sheet</b>: lights down, <i>then</i> music, <i>then</i> curtain, <i>then</i> the actor enters, each on a trigger. Everyone knows their cue and what comes before it. Without the sheet, each crew member works from memory, and one night the curtain goes up in the dark.</p>""",
    analogy_figs=[sq_analogy],
    map=[("The crew members", "Lifelines: Ordering, Kafka, Fulfilment, Dispatch, Billing"),
         ("Cue numbers, in order", "Messages, top to bottom"),
         ("“Go on the music”", "The trigger: an event like order.delivered"),
         ("Curtain up in the dark", "Billing before delivery"),
         ("The rehearsal", "Walking the diagram with both teams")],
    how_side="lifelines across, time down",
    how="""  <p>Ana drew the standing-order flow with both teams in one hour. The fix turned out to be <b>one arrow</b>: Billing creates usage lines when it hears <b>order.delivered</b>, with what was actually delivered, not when the order is placed. The diagram now lives next to ADR 0014, and the three credit notes went out the same week.</p>""",
    how_figs=[sq_how],
    steps=[("Pick a flow where order matters", "Money, retries, events, several teams, or something that broke."),
           ("List the participants", "Systems, modules or people, as lifelines left to right in rough order of involvement."),
           ("Write the messages in order", "Each with a label: name, trigger, and what it carries."),
           ("Mark async vs sync", "Events and queues look different from calls that wait."),
           ("Add the unhappy paths", "Items short, timeouts, retries: a second diagram if it gets busy."),
           ("Walk it with every team", "One hour, everyone in the room; fix disagreements on the drawing.")],
    vocab=[("Lifeline", "A participant's vertical line; time runs down it."),
           ("Message", "A call or event from one lifeline to another."),
           ("Synchronous", "The sender waits for an answer."),
           ("Asynchronous", "The sender doesn't wait; usually an event."),
           ("Activation", "The bar showing a participant is busy."),
           ("Flowchart", "Steps and decisions, without separate participants.")],
    code=dict(file="docs/architecture/flows/standing-order.md", note="Mermaid source for the standing-order flow", plain=True, src="""
```mermaid
sequenceDiagram
    autonumber
    participant O as Ordering (Core)
    participant K as Kafka
    participant F as Fulfilment (Zuid)
    participant D as Dispatch
    participant B as Billing
    Note over O: 05:00 scheduler creates Korenwolf's standing order
    O-)K: order.placed (via outbox, ADR 0007)
    K-)F: pick list for Zuid
    F-)K: order.packed {items_short: 2}
    K-)D: order.ready_for_dispatch
    D->>D: assign a van (Engine A)
    D-)K: order.delivered {lines delivered}  ~08:10
    K-)B: usage lines = what was DELIVERED, not what was placed
```
"""),
    tools="tools: Mermaid (renders in GitHub and most wikis), PlantUML, sequencediagram.org, WebSequenceDiagrams. Keep the source in the repo next to the ADR it explains.",
    gains=["<b>Order and timing are visible</b>: when, and in response to what.",
           "<b>Teams agree</b> on the flow before building.",
           "<b>Money and retry bugs</b> show up on paper.",
           "<b>Easy to keep as code</b> in Mermaid.",
           "<b>Great for onboarding</b> and incident reviews."],
    losses=["<b>Busy fast</b>: more than ten messages gets hard to read.",
            "<b>Happy path bias</b>: errors need their own diagrams.",
            "<b>Goes stale</b> when flows change.",
            "<b>Only one scenario</b> per diagram."],
    baseline="Each line compares <b>flows described in words or box-and-arrow diagrams</b> to <b>sequence diagrams with lifelines, ordered messages and triggers, walked through with every team</b>.",
    ratings=[(2, 5, "Anyone can follow the order of events."),
             (2, 4, "Both teams agreed on one picture."),
             (3, 4, "One hour settled a cross-team argument."),
             (2, 5, "The billing bug is visible on the drawing."),
             (3, 3, "Doesn't change adaptability."),
             (2, 4, "The flow sits next to ADR 0014."),
             (2, 4, "Money flows get drawn and checked."),
             (3, 4, "Text-based diagrams are quick to edit."),
             (3, 4, "Teams draw their own flows.")],
    pitfalls=[("Happy path only", "No items short, no timeouts.", "add the unhappy paths, in a second diagram if needed."),
              ("Too many lifelines", "Fifteen participants across the page.", "group or split; keep to five or six."),
              ("Unlabelled messages", "Arrows without names or triggers.", "name every message and say what triggers it."),
              ("Drawn alone", "The author's view of the flow.", "walk it with every team involved.")],
    use=["Flows that involve money, retries or events.",
         "Anything spanning several teams or services.",
         "Before building an integration.",
         "Incident reviews: what happened, in what order."],
    skip=["Simple request/response inside one module.",
          "Structure questions: use C4 instead."],
    related=["<b>Views &amp; viewpoints (4+1)</b> (this volume)", "<b>C4 model</b> (this volume)", "<b>Transactional outbox</b> (patterns, Vol. 1)", "<b>Domain discovery (event storming)</b> (Vol. 1)"],
    quiz=[("What runs down a sequence diagram?", "Time: messages are shown in order, top to bottom."),
          ("What caused Korenwolf's wrong invoice?", "Two teams assumed different triggers for creating billing lines: placed vs delivered."),
          ("How do you show an event vs a call?", "Asynchronous messages (events) use a different arrow from synchronous calls."),
          ("When should you draw one?", "For flows where order matters: money, retries, events, several teams.")],
    try_it="Pick the flow in your system that involves money or events across two teams. Draw it as a Mermaid sequence diagram in 30 minutes, then walk it with someone from each team. Note every point where they say “wait, that's not when we do it”.",
    remember="Lifelines across, <span class=\"hl\">time down</span>. Every message has a <span class=\"hl\">cue</span>.",
    sources=["Martin Fowler, <i>UML Distilled</i>, 3rd ed. (2003), sequence diagrams.",
             "ITU-T Recommendation Z.120, “Message Sequence Chart” (1992–).",
             "Mermaid documentation, “Sequence diagrams” (mermaid.js.org).",
             "Gregor Hohpe and Bobby Woolf, <i>Enterprise Integration Patterns</i> (2003)."],
)

# ------------------------------------------------------------------ 04 Deployment Diagrams
dp_problem = Doodle(760, 280, "Doodle of an incident on 29 October 2026. After a network rule change, Dispatch can't reach the database for 25 minutes. The on-call engineer, three weeks into the job, can't find out what runs where: which network Dispatch is in, where the database is, what changed.",
                    "Twenty-five minutes of “where does Dispatch actually run?” during an incident.")
dp_problem.box(20, 30, 220, 80, "Dispatch", "blue", sub="can't reach the DB")
dp_problem.arrow(246, 70, 480, 70, color="red", dash=True, label="✗ 25 minutes", lx=363, ly=56)
dp_problem.box(486, 30, 254, 80, "database", "paper", sub="which network?")
dp_problem.box(160, 156, 440, 70, "on-call, week 3: “what runs where?”", "pink", stroke="red", size=16)
dp_problem.note(380, 264, "the answer was in Eli's head", "red")

dp_analogy = Doodle(760, 250, "Doodle of a building's plan for the fire brigade: where the gas main is, where the electricity cabinet is, which doors connect which rooms, and where the exits are. The fire brigade doesn't need the furniture; it needs to know where things physically are.",
                     "The fire brigade's plan: where the gas main, the fuse box and the exits are, not the furniture.")
for i, (ic, t, f) in enumerate([("fuse", "fuse box: cellar", "y"), ("door", "exits: east, west", "green"), ("bucket", "gas main: front", "pink")]):
    x = 20 + i * 250
    dp_analogy.icon(ic, x + 85, 20, 1.0)
    dp_analogy.box(x, 110, 220, 56, t, f, size=16)
dp_analogy.note(380, 226, "where things are, not what they do", "pen")

dp_how = Doodle(760, 380, "Larder's deployment diagram, November 2026. In the cloud region, Frankfurt: a private network with the managed container service running Dispatch and routing Engine A, three virtual machines running Larder Core, managed Postgres with a primary and a replica, and managed Kafka. Outside: the stores, with picker handhelds on Wi-Fi and a 4G backup router; customers' and couriers' phones over the internet; and the SaaS services: StockPilot, two payment providers, the billing service and the helpdesk.",
                "What runs where, on which network, and how it's reached. On-call's first page.")
dp_how.box(14, 14, 520, 300, None, "paper", dash=True)
dp_how.head(274, 42, "EU region (Frankfurt) · private network", size=15)
dp_how.box(30, 60, 230, 90, "containers", "blue", sub="Dispatch + Engine A", subsize=15)
dp_how.box(290, 60, 230, 90, "3 VMs", "blue", sub="Larder Core", subsize=15)
dp_how.box(30, 180, 230, 110, "Postgres", "y", sub="primary + replica", subsize=15)
dp_how.box(290, 180, 230, 110, "Kafka", "y", sub="managed, 3 brokers", subsize=15)
dp_how.box(560, 14, 186, 92, "stores", "green", sub="Wi-Fi + 4G backup", subsize=14)
dp_how.box(560, 124, 186, 76, "phones", "green", sub="internet", subsize=14)
dp_how.box(560, 218, 186, 96, "SaaS ×5", "pink", sub="StockPilot, PSPs…", subsize=14)
dp_how.arrow(556, 60, 520, 100, dash=True)
dp_how.arrow(556, 160, 520, 110, dash=True)
dp_how.note(274, 352, "drawn from the infrastructure code · on-call's first page", "pen", size=17)

DEPLOYMENT = dict(
    slug="deployment-diagrams",
    kicker="a.k.a. “the fire brigade's plan”",
    tldr="A container diagram says what the parts are; a <b>deployment diagram</b> says <b>where they run</b>: which region, which network, which machines or managed services, how many copies, and how traffic gets in and out. It's the first page <b>on-call</b> needs at 3 a.m., and it's what security, auditors and new platform engineers ask for. Keep it <b>small, current and close to the infrastructure code</b>.",
    chips=[("Family", "diagrams"), ("Origin", "UML deployment diagrams (1997); C4 supplementary deployment views"), ("Lives in", "docs/architecture/deployment.md, next to the infrastructure code"), ("Pairs with", "C4 model, choosing a cloud service model, infrastructure as code")],
    problem_side="Larder, 29 October 2026",
    problem="""  <p class="lead">A network rule change at 18:10 on a Thursday cuts <b>Dispatch off from the database</b>. The on-call engineer, three weeks into the job, needs to know where Dispatch runs, which network it's in and how it reaches Postgres. <span class="hl-pink">It's all in Eli's head</span>, and Eli is on a train. It takes 25 minutes to find the rule; couriers are assigned by hand for most of that time.</p>
  <ul>
    <li>Nobody but one engineer knows the physical layout.</li>
    <li>Incidents become archaeology when the deployment isn't drawn.</li>
    <li>Security and audit questions get a different answer each time.</li>
  </ul>""",
    problem_figs=[dp_problem],
    analogy_side="the fire brigade's plan",
    analogy="""  <p>Big buildings keep a plan for the <b>fire brigade</b>: where the <b>gas main</b> and the <b>fuse box</b> are, which doors connect which rooms, where the <b>exits</b> are. Not the furniture, not who works where. When the brigade arrives at 3 a.m., they don't have time to ask the caretaker.</p>""",
    analogy_figs=[dp_analogy],
    map=[("The building", "The cloud region, Frankfurt"),
         ("Rooms and doors", "Networks and the rules between them"),
         ("The fuse box and gas main", "Databases, Kafka, the critical managed services"),
         ("Exits", "How traffic gets in and out: stores, phones, SaaS"),
         ("The fire brigade", "On-call at 3 a.m.")],
    how_side="where it runs, and how it's reached",
    how="""  <p>Ana and Eli drew it the following week: one region, one private network, <b>managed containers</b> for Dispatch and Engine A, <b>three VMs</b> for Larder Core, managed Postgres and Kafka, and the outside world on the right: stores with their 4G backup, phones, and five SaaS services. It's generated from a short description next to the infrastructure code and linked from the on-call runbook's first line.</p>""",
    how_figs=[dp_how],
    steps=[("Draw the boundary", "Region, account, network: the outer boxes."),
           ("Place each container", "On the managed service, VM or device it runs on; say how many copies."),
           ("Show the data stores", "Databases and brokers, with replicas."),
           ("Show the ways in and out", "Users, stores, partners; which network path they take."),
           ("Keep it close to the infrastructure code", "Generated or reviewed with every infra change."),
           ("Link it from the runbook", "On-call's first page, with the dashboard links.")],
    vocab=[("Deployment node", "Where something runs: a VM, a managed service, a device."),
           ("Region", "A cloud provider's data-centre area (here, Frankfurt)."),
           ("Private network", "A network not reachable from the internet directly."),
           ("Replica", "A copy of a database for safety or reads."),
           ("Runbook", "Step-by-step instructions for operating or fixing a system."),
           ("Ingress / egress", "Traffic coming in / going out.")],
    code=dict(file="docs/architecture/deployment.md", note="deployment description, reviewed with every infra change", plain=True, src="""
# Larder · deployment (Nov 2026)                    owner: Eli · reviewed with infra PRs

Region     EU, Frankfurt · one private network "larder-prod"
Runs on    managed container service   Dispatch (2–6 copies), routing Engine A (2)
           3 virtual machines          Larder Core (Django), behind a load balancer
           managed Postgres            primary + 1 replica (other zone), daily backups
           managed Kafka               3 brokers, topics owned per ADR 0006
Ways in    customer + courier phones   internet → load balancer → Core / Dispatch
           stores (Noord, Zuid, RTM)   store Wi-Fi, 4G backup router → VPN → Core
           SaaS                        StockPilot, PSP ×2, billing, helpdesk (HTTPS out)
Network    Dispatch → Postgres: allowed on 5432 (the rule changed on 29 Oct)
On-call    runbook: docs/runbooks/README.md · dashboards: link · this page first
"""),
    tools="tools: Structurizr deployment views, C4-PlantUML, cloud diagram tools that read your infrastructure (Cloudcraft, Hava, Brainboard); infrastructure-as-code repos as the source of truth.",
    gains=["<b>Faster incidents</b>: on-call knows the layout.",
           "<b>Security and audit answers</b> from one page.",
           "<b>Onboarding</b> for platform engineers.",
           "<b>Cost visibility</b>: every paid service on the page.",
           "<b>Less key-person risk</b>: not just in Eli's head."],
    losses=["<b>Changes often</b> with infrastructure.",
            "<b>Can expose sensitive details</b> if shared widely.",
            "<b>Too much detail</b> (IPs, ports) makes it unreadable.",
            "<b>Another document</b> to keep current."],
    baseline="Each line compares <b>a physical layout known only to the platform engineer</b> to <b>a deployment diagram kept next to the infrastructure code and linked from the runbook</b>.",
    ratings=[(2, 4, "Anyone can see what runs where."),
             (3, 3, "Mostly for engineers and ops."),
             (2, 4, "Incidents start from facts, not guesses."),
             (2, 5, "Key-person risk and network gaps are visible."),
             (3, 3, "Doesn't change adaptability."),
             (2, 4, "Reviewed with every infra change."),
             (2, 4, "Every paid service is on the page."),
             (3, 4, "Generated or updated with infra PRs."),
             (2, 4, "On-call can act without Eli.")],
    pitfalls=[("Only in someone's head", "Eli knows; Eli is on a train.", "draw it, and link it from the runbook."),
              ("Every IP and port", "An unreadable network dump.", "show nodes and paths; details in the infra code."),
              ("Drawn once", "Last spring's layout.", "review it with every infrastructure change."),
              ("Shared everywhere", "The network layout on a public wiki.", "keep sensitive details internal.")],
    use=["Any system with on-call.",
         "Security reviews and audits.",
         "Before and after infrastructure changes.",
         "Onboarding platform engineers."],
    skip=["Pure SaaS products with nothing of your own deployed.",
          "Explaining what the system does: use C4."],
    related=["<b>C4 model</b> (this volume)", "<b>Living diagrams</b> (this volume)", "<b>Choosing a cloud service model</b> (Vol. 2)", "<b>Infrastructure as code</b> (patterns, Vol. 6)"],
    quiz=[("What does a deployment diagram show that a container diagram doesn't?", "Where things run: region, network, nodes, copies, and how traffic gets in and out."),
          ("Who needs it first?", "On-call engineers during an incident."),
          ("Where should it live?", "Next to the infrastructure code, reviewed with infra changes, linked from the runbook."),
          ("What should be left out?", "Every IP and port: keep those in the infrastructure code.")],
    try_it="Without looking anything up, sketch where your system runs: regions, networks, managed services, how users reach it. Then check it against the infrastructure code and mark every mistake. Fix it, and link it from your on-call runbook.",
    remember="Draw it for the <span class=\"hl\">fire brigade</span>: where things are, and how to get <span class=\"hl\">in</span>.",
    sources=["Simon Brown, c4model.com, “Deployment diagram”.",
             "Martin Fowler, <i>UML Distilled</i>, 3rd ed. (2003), deployment diagrams.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016), on runbooks.",
             "Kief Morris, <i>Infrastructure as Code</i>, 2nd ed. (2020)."],
)

NOTES = [C4, VIEWS, SEQUENCE, DEPLOYMENT]
