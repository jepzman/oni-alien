# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 1 · What a project is.
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 1").
# Spine: PMBOK Guide, Eighth Edition. Names are PMI's; every explanation is in our own words.

# ------------------------------------------------------------------ 01 Is This a Project?
pp_problem = Doodle(760, 270, "Doodle of Sanne's third day at Larder, 14 January 2026. Eleven things have landed on her desk, all called projects: the Rotterdam launch, substitution approvals, the Noord picker rota, the cold-room repair at Zuid, courier shift planning and more. One pile, eleven sticky notes, one person.",
                    "Day three: eleven things on the desk, and everyone calls each one “a project”.")
for i, (t, f) in enumerate([("Rotterdam launch", "y"), ("swap approvals", "blue"), ("Noord rota", "green"), ("Zuid cold room", "y"),
                            ("courier shifts", "green"), ("new helpdesk", "y"), ("picker app", "blue"), ("stock counts", "green")]):
    r, c = divmod(i, 4)
    pp_problem.box(14 + c * 186, 20 + r * 76, 172, 60, t, f, size=14)
pp_problem.note(380, 206, "“can you project-manage this?” × 11", "red", size=20)
pp_problem.note(380, 240, "three different kinds of work in one pile", "pen", size=17)

pp_analogy = Doodle(760, 240, "Doodle of a restaurant. Opening a second restaurant is a project: it starts, it ends, it is new. The menu is a product: it lives for years and keeps changing. Dinner service tonight is operations: the same work, every day.",
                    "Opening a second restaurant, looking after the menu, and serving dinner tonight are three different jobs.")
pp_analogy.row([("open restaurant no. 2", "starts, ends, new", "y"), ("the menu", "lives on, keeps changing", "blue"), ("tonight's service", "same every day", "green")], y=40, h=90, size=17, subsize=14)
pp_analogy.note(132, 180, "project", "red", size=22)
pp_analogy.note(380, 180, "product", "red", size=22)
pp_analogy.note(628, 180, "operations", "red", size=22)

pp_how = Doodle(760, 330, "Sanne's sorting, 14 January 2026. Three questions: does it end, is the result new, and who owns it afterwards. Projects, four: the Rotterdam launch, the Zuid cold-room replacement, moving to a new helpdesk tool, the summer courier hiring drive. Products, three: substitution approvals and the customer app with Grace, the picker app with Dee. Operations, four: the Noord rota, courier shifts, weekly stock counts, supplier orders, all with Joost and Tomás.",
                "Three questions sort the pile: does it end? is the result new? who owns it afterwards?")
pp_how.row([("does it end?", None, "paper"), ("is the result new?", None, "paper"), ("who owns it after?", None, "paper")], y=14, h=50, size=17)
pp_how.box(14, 84, 236, 220, None, "y")
pp_how.head(132, 112, "projects · 4", size=19)
for i, t in enumerate(["Rotterdam launch", "Zuid cold room", "new helpdesk tool", "courier hiring drive"]):
    pp_how.text(132, 146 + i * 30, t, size=16)
pp_how.note(132, 286, "→ Sanne", "green", size=18)
pp_how.box(262, 84, 236, 220, None, "blue")
pp_how.head(380, 112, "products · 3", size=19)
for i, t in enumerate(["swap approvals", "customer app", "picker app"]):
    pp_how.text(380, 146 + i * 30, t, size=16)
pp_how.note(380, 286, "→ Grace, Dee", "green", size=18)
pp_how.box(510, 84, 236, 220, None, "green")
pp_how.head(628, 112, "operations · 4", size=19)
for i, t in enumerate(["Noord rota", "courier shifts", "stock counts", "supplier orders"]):
    pp_how.text(628, 146 + i * 30, t, size=16)
pp_how.note(628, 286, "→ Joost, Tomás", "green", size=18)

IS_PROJECT = dict(
    slug="project-product-operations",
    kicker="a.k.a. “project, product or operations”",
    tldr="A <b>project</b> is temporary work that creates something new: it has a start, an end, and a result that didn't exist before. A <b>product</b> lives on and keeps changing for as long as customers use it. <b>Operations</b> is the same work, repeated, that keeps the business running. They need different management. Before you plan anything, <b>sort the pile</b>.",
    chips=[("Family", "foundations"), ("Lives in", "the first week of any new job"), ("Pairs with", "the value delivery system, the project manager's role")],
    pmbok=dict(covers="what a project is; projects, products and operations", older="6th: chapter 1 (“temporary endeavor”). 7th: the system for value delivery."),
    problem_side="Larder, 14 January 2026",
    problem="""  <p class="lead">Sanne joined Larder on Monday <b>12 January 2026</b> as delivery manager. By Wednesday eleven people have asked her to “project-manage” something: the Rotterdam launch, substitution approvals, the picker rota at Noord, the broken cold room at Zuid. <span class="hl-pink">If everything is a project, she can't run any of them well.</span></p>
  <ul>
    <li>Everything gets a deadline, even work that never ends.</li>
    <li>Nobody knows who owns the result once it is “done”.</li>
    <li>The one real deadline, Rotterdam on 27 April, hides in the pile.</li>
  </ul>""",
    problem_figs=[pp_problem],
    analogy_side="a restaurant",
    analogy="""  <p>A restaurant owner does three kinds of work. <b>Opening a second restaurant</b> starts, ends, and produces something new. <b>The menu</b> is never finished: it changes with the seasons and the guests. <b>Tonight's dinner service</b> is the same work every evening, done well. Nobody would plan tonight's service with a building schedule, or the new building with a rota.</p>""",
    analogy_figs=[pp_analogy],
    map=[("Opening restaurant no. 2", "The Rotterdam launch"),
         ("The menu", "Substitution approvals, the customer app"),
         ("Tonight's dinner service", "Picking and delivering 4,000 orders a day"),
         ("The owner asks “what kind of work is this?”", "Sanne sorts the pile on day three"),
         ("The new restaurant joins the nightly service", "Rotterdam becomes operations on 27 April")],
    how_side="three questions, then three piles",
    how="""  <p>Sanne asks three questions of each item. <b>Does it end?</b> <b>Is the result new?</b> <b>Who owns it afterwards?</b> Four items are projects: Rotterdam, the Zuid cold-room replacement, the new helpdesk tool and the summer courier hiring drive. Three are products, and they already have owners: Grace and Dee. Four are operations, which Joost and Tomás run every day. She keeps the four projects, and Rotterdam goes to the top: it is the only one with a signed lease.</p>""",
    how_figs=[pp_how],
    steps=[("List everything you've been asked to manage", "One line each, no judging yet."),
           ("Ask: does it end?", "A real end, not a wish."),
           ("Ask: is the result new?", "Or is it the same result, again?"),
           ("Ask: who owns it afterwards?", "Every project hands over to someone."),
           ("Sort into three piles", "Projects, products, operations."),
           ("Give each pile back to its owner", "Keep the projects. Rank them.")],
    vocab=[("Project", "Temporary work that creates a new product, service or result."),
           ("Temporary", "It has a start and an end. It doesn't mean short."),
           ("Product", "Something that gives value for as long as it lives, and keeps changing."),
           ("Operations", "Ongoing, repeated work that keeps the business running."),
           ("Deliverable", "A thing the project hands over: a store, an app release, a trained team."),
           ("Handover", "The moment a project's result becomes someone's daily work.")],
    code=dict(file="sanne/desk-sort.md", note="14 January 2026", plain=True, src="""
# What's on my desk · sorted

                         ends?   new?   owner after        → kind
Rotterdam launch         27 Apr  yes    Joost (store)      PROJECT  ← lease signed
Zuid cold-room replace   March   yes    Tomás              PROJECT
New helpdesk tool        May     yes    Sam                PROJECT
Courier hiring drive     June    yes    Joost              PROJECT
Substitution approvals   no      keeps  Grace              product
Customer app             no      keeps  Grace              product
Picker app               no      keeps  Dee                product
Noord picker rota        no      no     Tomás              operations
Courier shifts           no      no     Joost              operations
Weekly stock counts      no      no     Tomás              operations
Supplier orders          no      no     Joost              operations
"""),
    tools="tools: a list, three questions and half an hour. The hard part is giving things back.",
    dial=[("Light", "a small team, a few requests", ["Ask the three questions out loud.", "Say whose it is.", "No document."]),
          ("Standard", "Rotterdam: one person, eleven requests", ["A one-page sorted list.", "Agreed with your manager.", "Reviewed when new work arrives."]),
          ("Heavy", "a company with many projects", ["Written rules for what counts as a project.", "An intake form.", "A portfolio board decides."])],
    baseline="Each line compares <b>calling all eleven items projects</b> to <b>sorting them into projects, products and operations with named owners</b>.",
    ratings=[(2, 4, "Rotterdam's benefit is visible, not buried."),
             (2, 4, "Four dated projects, not eleven."),
             (2, 3, "The one hard deadline stands out."),
             (2, 4, "One list everyone can read."),
             (3, 4, "People know who to ask."),
             (2, 4, "Grace, Dee and Tomás keep their own work."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (4, 4, "Half an hour.")],
    pitfalls=[("Everything is a project", "Work that never ends gets a fake deadline.", "ask “does it end?” first."),
              ("Nothing is a project", "A launch run as daily work, with nobody watching the date.", "one date, one owner, one plan."),
              ("Temporary means short", "A project can take years.", "temporary means it ends."),
              ("No owner afterwards", "The project “finishes” and the result drifts.", "name the receiver on day one.")],
    use=["You're new and handed a pile.", "A team says “we have too many projects”.", "Nobody can say who owns a result.", "A deadline is put on never-ending work."],
    skip=["The work is clearly one project already.", "A product team with a clear owner and backlog."],
    related=["<b>What Is It All For?</b> (next note)", "<b>Outcomes over outputs</b> (Grace, vol. 1)", "<b>Business drivers</b> (Ana, vol. 1)"],
    quiz=[("What makes work a project?", "It is temporary (it ends) and it creates something new."),
          ("Does temporary mean short?", "No. It means there is an end."),
          ("Joost asks Sanne to “project-manage” the weekly stock counts. What does she do first?", "Ask whether it ends. It doesn't: it's operations, and Tomás owns it. She can help improve it once, as a small project, but not run it."),
          ("What happens to Rotterdam on 27 April?", "The project hands over; running the store becomes operations."),
          ("Who looks after substitution approvals?", "Grace: it is a product, it lives on.")],
    try_it="List everything you are managing this month. For each line answer: does it end, is the result new, who owns it afterwards? Mark each P, Pr or O. How many real projects are left?",
    remember="A project <span class=\"hl\">ends</span> and leaves something <span class=\"hl\">new</span> behind. Sort the pile before you plan it.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): introduction and key terms.",
             "Project Management Institute, <i>The Standard for Project Management</i> (2021): the system for value delivery.",
             "Marty Cagan, <i>Inspired</i> (2nd ed., 2017): products versus projects."],
)

# ------------------------------------------------------------------ 02 What Is It All For?
vd_problem = Doodle(760, 260, "Doodle of 16 January 2026. Joost hands Sanne his launch spreadsheet, Rotterdam version 7: 140 rows, 31 with no owner. No row says why Larder is opening in Rotterdam at all, or what will be better afterwards.",
                    "140 rows of things to do. Not one says what will be better when they're done.")
vd_problem.icon("ledger", 40, 40, 1.6)
vd_problem.head(260, 70, "Rotterdam v7.xlsx", size=21)
vd_problem.text(260, 104, "140 rows · 31 without an owner", size=17)
vd_problem.box(470, 36, 270, 100, "why?", "pink", sub="no row answers it", size=26, subsize=16)
vd_problem.note(380, 210, "“when all 140 are ticked, what is better?”", "red", size=20)

vd_analogy = Doodle(760, 250, "Doodle of a family: the goal is a healthier family. That leads to a plan with several parts: a kitchen rebuild, a vegetable garden, a weekly cooking evening. The kitchen rebuild is one project. The new kitchen is the output. Cooking at home four nights a week is the outcome. Better health and lower food bills are the benefit.",
                    "A new kitchen is not the point. Cooking at home, and what that brings, is.")
vd_analogy.row([("new kitchen", "the output", "y"), ("cook at home 4×", "the outcome", "blue"), ("healthier, cheaper", "the benefit", "green")], y=50, h=90, gap=40, size=17, subsize=15, arrows=True)
vd_analogy.note(380, 196, "the builder finishes at box one. The family is after box three.", "pen", size=18)

vd_how = Doodle(760, 400, "The value chain for Rotterdam, drawn by Sanne on 16 January 2026. Strategy: six cities by the end of 2027. Portfolio: Femke's board list of everything Larder invests in. Programme: the six-city expansion. Project: the Rotterdam launch. Operations: the Rotterdam store running every day. Underneath: outputs are a store, a configured app and a trained team; the outcome is Rotterdam customers ordering; the benefit is orders, revenue and proof that a city can open quickly.",
                "Strategy → portfolio → programme → project → operations. Value appears at the end of the chain, not in the middle.")
vd_how.row([("strategy", "six cities by end 2027", "paper"), ("portfolio", "Femke's board list", "y"), ("programme", "the six-city expansion", "y")], y=14, h=78, gap=40, size=18, subsize=14, arrows=True)
vd_how.row([("project", "the Rotterdam launch", "blue"), ("operations", "the store, every day", "green")], x=120, y=126, h=78, gap=60, size=18, subsize=14, arrows=True)
vd_how.arrow(560, 92, 330, 124)
vd_how.line("M14 232 h732", thin=True, dash=True)
vd_how.row([("outputs", "store · app · team", "y"), ("outcome", "Rotterdam orders", "blue"), ("benefit", "orders · proof of speed", "green")], y=258, h=84, gap=40, size=18, subsize=14, arrows=True)
vd_how.note(132, 372, "27 April", "pen", size=17)
vd_how.note(380, 372, "May", "pen", size=17)
vd_how.note(628, 372, "summer, and Utrecht", "pen", size=17)

vd_deep1 = Doodle(760, 300, "Sanne's benefits map for Rotterdam. Left: three outputs: the store open on 27 April, the city set up in the platform, forty pickers and couriers trained. Middle: two outcomes: Rotterdam customers order and come back; the next city can be set up faster. Right: three benefits with owners: 500 orders a day by the end of May, owned by Joost; 90 percent express on time by the end of the summer, owned by Joost; a new city in 8 weeks or less, owned by Femke.",
                  "A benefits map reads right to left when you plan, and left to right when you deliver.")
for i, t in enumerate(["store open 27 Apr", "city set up", "40 staff trained"]):
    vd_deep1.box(14, 30 + i * 84, 216, 66, t, "y", size=16)
for i, t in enumerate(["customers order", "next city is faster"]):
    vd_deep1.box(272, 60 + i * 110, 216, 70, t, "blue", size=16)
for i, (t, s) in enumerate([("500 orders/day", "end May · Joost"), ("90 % on time", "end summer · Joost"), ("a city in ≤ 8 weeks", "Utrecht · Femke")]):
    vd_deep1.box(530, 30 + i * 84, 216, 66, t, "green", sub=s, size=16, subsize=13)
for y1, y2 in [(63, 95), (147, 95), (231, 205)]:
    vd_deep1.arrow(230, y1, 270, y2)
vd_deep1.arrow(230, 147, 270, 205)
for y1, y2 in [(95, 63), (95, 147), (205, 231)]:
    vd_deep1.arrow(488, y1, 528, y2)
vd_deep1.note(122, 290, "outputs", size=17)
vd_deep1.note(380, 290, "outcomes", size=17)
vd_deep1.note(638, 290, "benefits + owner", size=17)

vd_deep2 = Doodle(760, 210, "A timeline of when value shows up. The project runs from 12 January to 27 April and then closes after hypercare in May. Benefits are measured after that: four weeks after opening, twelve weeks after, and when Utrecht starts. The project team has gone by then, so each benefit needs an owner who stays.",
                  "Most of the benefit arrives after the project team has gone home. Someone who stays must own it.")
vd_deep2.box(14, 40, 380, 56, "the project", "blue", sub="12 Jan → 27 Apr + hypercare", size=17, subsize=13)
vd_deep2.box(394, 40, 352, 56, "benefits arrive", "green", sub="measured by the owner", size=17, subsize=13)
for x, t in [(394, "open"), (490, "+4 weeks"), (600, "+12 weeks"), (716, "Utrecht")]:
    vd_deep2.line(f"M{x} 96 v26", thin=True)
    vd_deep2.note(x, 146, t, "pen", size=16)
vd_deep2.note(204, 186, "Sanne's team", size=17)
vd_deep2.note(570, 186, "Joost, Femke", "green", size=17)

VALUE_CHAIN = dict(
    slug="value-delivery-system",
    kicker="a.k.a. “the system for value delivery”",
    tldr="A project is one link in a chain. <b>Strategy</b> picks goals; a <b>portfolio</b> is everything the company invests in to reach them; a <b>programme</b> is a group of related projects; a <b>project</b> builds something new; <b>operations</b> uses it. Value appears only at the end: an <b>output</b> (a store) leads to an <b>outcome</b> (people order) and then a <b>benefit</b> (revenue, proof). Know your link, and what comes after it.",
    chips=[("Family", "foundations"), ("Lives in", "one drawing, shown at kick-off"), ("Pairs with", "focus on value, benefits realisation (vol. 6)")],
    pmbok=dict(covers="the system for value delivery; portfolios, programmes, projects, operations; outputs, outcomes, benefits", principles=["Focus on value"],
               older="6th: “organizational project management”, section 1.2. 7th: the system for value delivery."),
    problem_side="Larder, 16 January 2026",
    problem="""  <p class="lead">Joost hands Sanne his launch spreadsheet, <b>Rotterdam v7</b>: 140 rows, 31 without an owner. She reads all of it and asks one question: <span class="hl-pink">“when all 140 are ticked, what is better?”</span> Joost says “we're open in Rotterdam.” Femke, later that day, says “we've shown we can do a city in weeks, not months.” Those are two different projects.</p>
  <ul>
    <li>A task list can be 100 % done and the goal missed.</li>
    <li>People on the same project aim at different results.</li>
    <li>Nobody is asked to check the benefit after the launch party.</li>
  </ul>""",
    problem_figs=[vd_problem],
    analogy_side="the kitchen rebuild",
    analogy="""  <p>A family wants to eat better and spend less on takeaways. They rebuild the kitchen. The builder's job ends with a <b>new kitchen</b>: the output. What the family wanted is <b>cooking at home four nights a week</b>: the outcome. And behind that, <b>better health and lower bills</b>: the benefit. A beautiful kitchen nobody cooks in is a finished project and a failed investment.</p>""",
    analogy_figs=[vd_analogy],
    map=[("The family's goal", "Six cities by the end of 2027"),
         ("Kitchen, garden, cooking evenings", "The six-city programme: Rotterdam, Utrecht, The Hague…"),
         ("The kitchen rebuild", "The Rotterdam launch"),
         ("The new kitchen", "A store, a configured city, a trained team"),
         ("Cooking at home four nights", "Rotterdam customers ordering, and coming back"),
         ("Health and lower bills", "Orders, revenue, proof that a city opens fast")],
    how_side="find your link in the chain",
    how="""  <p>Sanne draws the chain on one page. Larder's <b>strategy</b>: six cities by the end of 2027. The <b>portfolio</b>: Femke's board list (the cities, Larder for Business, the platform). The <b>programme</b>: the six-city expansion. Her <b>project</b>: Rotterdam. Then <b>operations</b>: the store, every day, from 27 April. Under it she writes three words: the <b>outputs</b> she will hand over, the <b>outcome</b> they should cause, and the <b>benefit</b> Larder is paying for. Joost and Femke both sign the page: one project again.</p>""",
    how_figs=[vd_how],
    steps=[("Write the strategy goal in one line", "The one your project serves."),
           ("Name the programme or portfolio above you", "Who decides between projects?"),
           ("List your outputs", "Things you can hand over."),
           ("Write the outcome", "What people do differently because of them."),
           ("Write the benefit, with a number and a date", "What the business gets."),
           ("Name who owns the benefit after you close", "It is rarely the project manager.")],
    vocab=[("Portfolio", "Everything an organisation invests in to reach its goals, managed together."),
           ("Programme", "Related projects managed together because they share a goal."),
           ("Output", "What the project produces and hands over."),
           ("Outcome", "The change in what people do once they have the output."),
           ("Benefit", "The measurable gain for the business from that change."),
           ("Value", "The worth of the benefits, compared with what they cost.")],
    code=dict(file="rotterdam/value-chain.md", note="Sanne, 16 January 2026 · agreed with Joost and Femke", plain=True, src="""
# Rotterdam launch · why we're doing it

Strategy    six cities by the end of 2027 (Series B condition)
Programme   six-city expansion: Rotterdam → Utrecht → The Hague → Eindhoven → Antwerp
Project     the Rotterdam launch · 12 Jan → 27 Apr 2026 · sponsor: Joost

Outputs     store open and stocked · city set up in the platform · ~40 pickers and couriers trained
Outcome     Rotterdam customers order, and order again
Benefits    500 orders a day by the end of May            owner: Joost
            90 % express on time by the end of the summer  owner: Joost
            a launch playbook: the next city in ≤ 8 weeks  owner: Femke
Checked     +4 weeks · +12 weeks · at the start of Utrecht
"""),
    tools="tools: one page and two signatures. A benefits map (in the deep dive) when there is more than one benefit.",
    deep_dive=dict(
        side="benefits: who owns them, and when they are checked",
        intro="The note stops at one page. This deep dive goes one step further: how to trace each output to a benefit, why the benefit needs an owner who is not the project manager, and how to tell when a project should stop.",
        parts=[
            ("Draw the benefits map", """  <p>A <b>benefits map</b> has three columns. Plan it from <b>right to left</b>: start with the benefits the business wants, ask what would have to change for them to happen (outcomes), then ask what must exist for that change (outputs). Deliver it from <b>left to right</b>.</p>
  <p>The map earns its place when you find an output with <b>no arrow</b> going right. Sanne found 22 such rows in Joost's spreadsheet, among them branded tote bags and a launch-day animation in the app. They may be nice. They are not what Rotterdam is for, so they go to the bottom.</p>
  <p>It also shows a benefit with <b>no arrow coming in</b>. “A new city in 8 weeks or less” had no output behind it until Sanne added one: a written launch playbook.</p>""", [vd_deep1]),
            ("Give every benefit an owner who stays", """  <p>The project team hands over in May. The benefits arrive in May, in the summer, and when Utrecht starts. If the project manager is the only person who cares about them, nobody will be looking when they arrive, or when they don't.</p>
  <p>So each benefit gets an <b>owner in the business</b> and <b>dates to check it</b>. For Rotterdam: Joost owns orders and on-time delivery, Femke owns the eight-week promise. Sanne's job is to hand over outputs that make those benefits possible, and to say early if they won't.</p>""", [vd_deep2]),
            ("Know when to stop", """  <p>Value works in both directions. If the benefit can no longer be reached, or costs more than it is worth, the right decision may be to <b>change or stop the project</b>, even when the plan is on schedule. A project manager who thinks in outputs reports “on track”. One who thinks in value asks, at every review, <i>is this still worth finishing?</i></p>
  <p>For Rotterdam the answer is tied to the lease: stopping costs more than opening. That is a fact about value, and Sanne writes it down, so nobody has to argue about it in March.</p>""", []),
        ]),
    dial=[("Light", "a two-week internal change", ["One sentence: output → outcome → benefit.", "Said at the start.", "Checked once."]),
          ("Standard", "Rotterdam", ["A one-page value chain.", "A benefits map.", "Owners and check dates."]),
          ("Heavy", "a multi-year programme", ["A full business case.", "A benefits realisation plan.", "Reviews at every phase gate."])],
    baseline="Each line compares <b>working from a 140-row task list</b> to <b>one page that links the project to strategy, with outputs, outcome, benefits and owners</b>.",
    ratings=[(1, 5, "Everyone aims at the same result."),
             (3, 3, "Neutral: this is about why, not when."),
             (2, 4, "A missing benefit shows up in January."),
             (2, 4, "One page instead of 140 rows."),
             (2, 4, "Femke and Joost signed the same page."),
             (2, 3, "The team can judge its own tasks."),
             (2, 4, "Tasks can change; the benefit stays."),
             (3, 3, "Neutral."),
             (4, 4, "One page.")],
    pitfalls=[("Output = success", "“We opened” is celebrated; nobody checks the orders.", "write the benefit and the date to check it."),
              ("Benefits with no owner", "The project closes and they belong to nobody.", "name an owner who stays."),
              ("A vague benefit", "“Grow in Rotterdam.”", "a number and a date."),
              ("Never asking “still worth it?”", "The plan is followed off a cliff.", "ask at every review.")],
    use=["At the start of every project.", "When people describe the goal differently.", "When a task list has no “why”.", "Before cutting scope."],
    skip=["Never skip it. Shrink it to one sentence for tiny work."],
    related=["<b>Is This a Project?</b> (previous note)", "<b>Focus on Value</b> (this volume)", "<b>Outcomes over outputs</b> (Grace, vol. 1)", "<b>Business drivers</b> (Ana, vol. 1)"],
    quiz=[("Put in order: benefit, output, outcome.", "Output → outcome → benefit."),
          ("What is a programme?", "Related projects managed together because they share a goal: here, the six cities."),
          ("All 140 rows are ticked and the store is open, but only 150 orders a day arrive. Did the project succeed?", "It delivered its outputs. The benefit is missing, so the investment hasn't paid off yet. The benefit owner and Sanne look at why."),
          ("Who owns “500 orders a day by the end of May”?", "Joost. He's still there after the project closes."),
          ("An output on the map has no arrow to any benefit. What do you do?", "Question it. Drop it or move it to the bottom, unless someone can draw the arrow.")],
    try_it="For your current project, write three lines: the outputs you hand over, the outcome they should cause, the benefit with a number and a date. Then write one name: who owns that benefit after you close?",
    remember="The builder finishes at the <span class=\"hl\">kitchen</span>. The family wanted <span class=\"hl\">dinner</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the system for value delivery.",
             "Project Management Institute, <i>Benefits Realization Management: A Practice Guide</i> (2019).",
             "Gerald Bradley, <i>Benefit Realisation Management</i> (2nd ed., 2010): benefits maps.",
             "Joshua Seiden, <i>Outcomes Over Output</i> (2019)."],
)

# ------------------------------------------------------------------ 03 What Is My Job Here?
pm_problem = Doodle(760, 260, "Doodle of 19 January 2026. Four people expect four different things from Sanne. Joost wants someone to chase tasks. Ben wants someone to keep meetings away. Femke wants a date she can promise investors. Grace wonders whether Sanne will decide what the app does.",
                    "Four people, four ideas of what a project manager is for.")
pm_problem.circle(380, 120, 46, "y", label="Sanne")
for x, y, t, s in [(20, 20, "Joost", "“chase the tasks”"), (540, 20, "Femke", "“give me a date”"), (20, 170, "Ben", "“keep meetings away”"), (540, 170, "Grace", "“who decides scope?”")]:
    pm_problem.box(x, y, 200, 70, t, "paper", sub=s, size=17, subsize=14)
pm_problem.arrow(220, 60, 334, 104)
pm_problem.arrow(540, 60, 426, 104)
pm_problem.arrow(220, 200, 334, 140)
pm_problem.arrow(540, 200, 426, 140)

pm_analogy = Doodle(760, 240, "Doodle of a film set. The producer has the money and wants the film. The director decides what the film is. The first assistant director runs the schedule, the call sheet and the set, and tells everyone the truth about how the day is going. The first assistant director doesn't choose the story and doesn't act.",
                    "On a film set the first assistant director runs the day. They don't write the story and they don't pay for it.")
pm_analogy.row([("producer", "pays, wants the film", "y"), ("director", "decides what it is", "blue"), ("1st assistant director", "runs the schedule", "green")], y=40, h=90, size=16, subsize=14)
pm_analogy.note(132, 180, "sponsor", "red", size=20)
pm_analogy.note(380, 180, "product owner", "red", size=20)
pm_analogy.note(628, 180, "project manager", "red", size=20)

pm_how = Doodle(760, 360, "Sanne's role card, agreed with Joost on 19 January 2026. Sanne is accountable for the plan, the true status, risks and dependencies, and the handover. The sponsor, Joost, is accountable for the business case, the money, big decisions and removing blockers. Not Sanne's: what the app does, which is Grace's; how it's built, which is Ana's and Ben's; how stores run, which is Joost's and Tomás's. Three triggers go to the sponsor: the date at risk by more than three days, more than five thousand euros, or a change to what customers get at launch.",
                "A role card: what the project manager owns, what the sponsor owns, and what belongs to others.")
pm_how.box(14, 14, 236, 200, None, "green")
pm_how.head(132, 42, "Sanne owns", size=19)
for i, t in enumerate(["one plan", "the true status", "risks + dependencies", "the handover"]):
    pm_how.text(132, 76 + i * 32, t, size=16)
pm_how.box(262, 14, 236, 200, None, "y")
pm_how.head(380, 42, "Joost (sponsor) owns", size=18)
for i, t in enumerate(["the business case", "the money", "big decisions", "removing blockers"]):
    pm_how.text(380, 76 + i * 32, t, size=16)
pm_how.box(510, 14, 236, 200, None, "paper", dash=True)
pm_how.head(628, 42, "not Sanne's", size=19)
for i, t in enumerate(["what the app does: Grace", "how it's built: Ana, Ben", "how stores run: Tomás"]):
    pm_how.text(628, 76 + i * 32, t, size=15)
pm_how.box(14, 236, 732, 96, None, "pink")
pm_how.head(380, 264, "goes to the sponsor when…", size=19)
pm_how.text(380, 296, "date at risk > 3 days  ·  cost > €5,000  ·  what customers get at launch changes", size=16)

PM_ROLE = dict(
    slug="project-manager-role",
    kicker="a.k.a. “the project manager and the sponsor”",
    tldr="The <b>project manager</b> leads the team that delivers the project: one plan, a true picture of where things stand, risks and dependencies seen early, and a clean handover. The <b>sponsor</b> owns the reason for the project: the money, the big decisions, and clearing what the project manager can't. Neither decides what the product is or how it is built. Write the split down in week one.",
    chips=[("Family", "foundations"), ("Lives in", "a one-page role card"), ("Pairs with", "decision rights, the stakeholder map, the charter (vol. 2)")],
    pmbok=dict(covers="the project manager's role; the sponsor; project leadership", principles=["Be an accountable leader"],
               older="6th: chapter 3, “the role of the project manager”, and the talent triangle. 7th: the Team domain."),
    problem_side="Larder, 19 January 2026",
    problem="""  <p class="lead">Larder has never had a project manager. In her second week Sanne hears four versions of her job: Joost wants a task-chaser, Femke wants a date for the investors, Ben wants someone to keep meetings away from his team, and Grace asks, carefully, <span class="hl-pink">whether Sanne will now decide what the app does in Rotterdam.</span></p>
  <ul>
    <li>If she chases tasks only, nobody owns the plan.</li>
    <li>If she decides scope, she steps on Grace and Ana.</li>
    <li>Nobody has said who the sponsor is.</li>
  </ul>""",
    problem_figs=[pm_problem],
    analogy_side="the film set",
    analogy="""  <p>On a film set, the <b>producer</b> finds the money and wants a film that earns it back. The <b>director</b> decides what the film is. The <b>first assistant director</b> runs the schedule and the set: who is needed when, what today costs, what is slipping. They tell the producer the truth every evening. They don't rewrite the script, and nobody thinks less of them for it.</p>""",
    analogy_figs=[pm_analogy],
    map=[("The producer", "Joost, the sponsor (with Marco for the money)"),
         ("The director", "Grace for the app; Ana and Ben for how it's built"),
         ("The first assistant director", "Sanne"),
         ("The call sheet", "The plan and the weekly status"),
         ("“We're losing the light”", "“The date is at risk by more than three days”")],
    how_side="a role card, agreed with the sponsor",
    how="""  <p>Sanne writes a <b>role card</b> and takes it to Joost. She is accountable for <b>one plan</b>, the <b>true status</b>, <b>risks and dependencies</b> and the <b>handover</b>. Joost agrees to be the <b>sponsor</b>: the business case, the money (with Marco), the big decisions, the blockers. A third column lists what is <b>not hers</b>, with names. Three triggers send a decision up to Joost. Grace reads it and relaxes; Ben asks for a copy.</p>""",
    how_figs=[pm_how],
    steps=[("Ask each key person what they expect of you", "Write their words down."),
           ("Name the sponsor", "One person, with the authority to decide and pay."),
           ("List what you are accountable for", "Plan, status, risks, dependencies, handover."),
           ("List what you are not, with names", "Product, design, operations."),
           ("Agree what goes up to the sponsor", "A few clear triggers."),
           ("Share the card", "With everyone who gave you an expectation.")],
    vocab=[("Project manager", "The person who leads the project team to deliver the project's results."),
           ("Sponsor", "The person who provides money and support, and answers for the project's success in the business."),
           ("Accountable", "Answers for the result. One person."),
           ("Responsible", "Does the work. Can be several people."),
           ("Escalate", "Pass a decision up because it is above your authority."),
           ("Steering group", "The sponsor and a few leaders who decide what the project manager can't.")],
    code=dict(file="rotterdam/role-card.md", note="agreed with Joost, 19 January 2026", plain=True, src="""
# Rotterdam launch · who does what

SANNE (project manager) is accountable for
  one plan everyone works from      the true status, weekly
  risks and dependencies            the handover to the store team

JOOST (sponsor) is accountable for
  why we're doing it                the money (with Marco)
  decisions above Sanne's limits    removing blockers

NOT SANNE'S                         whose
  what the app does at launch       Grace (Priya above her)
  how it is built                   Ana, Ben, Dee, Eli
  how the stores run                Joost, Tomás

GOES TO JOOST WHEN
  the date is at risk by more than 3 days
  a change costs more than €5,000
  what customers get at launch would change
"""),
    tools="tools: a page, a conversation with the sponsor, and the nerve to write “not mine”.",
    dial=[("Light", "a team that knows each other", ["A five-minute talk with the sponsor.", "Three triggers agreed.", "A note in chat."]),
          ("Standard", "Rotterdam", ["A one-page role card.", "Signed off by the sponsor.", "Shared with the team."]),
          ("Heavy", "many teams, vendors, a contract", ["Roles in the charter.", "A responsibility matrix (RACI).", "A steering group with terms of reference."])],
    baseline="Each line compares <b>four people holding four ideas of the role</b> to <b>a role card agreed with a named sponsor</b>.",
    ratings=[(3, 4, "The sponsor owns the why."),
             (2, 4, "One person owns the plan."),
             (2, 4, "Clear triggers catch trouble early."),
             (2, 4, "Status has an owner."),
             (2, 4, "Femke knows who answers for the date."),
             (3, 4, "Grace, Ana and Ben keep their decisions."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (4, 4, "One page.")],
    pitfalls=[("The task-chaser", "The project manager only asks “is it done?”.", "own the plan and the risks, not the nagging."),
              ("The mini-CEO", "Deciding scope and design.", "write “not mine”, with names."),
              ("No sponsor", "Decisions wait for nobody.", "one named person."),
              ("A sponsor in name only", "Never available.", "agree a weekly 20 minutes.")],
    use=["Your first weeks on any project.", "A company's first project manager.", "When decisions bounce between people.", "When the sponsor is unclear."],
    skip=["The roles are already written in a charter that people follow."],
    related=["<b>Decision rights</b> (Ana, vol. 2)", "<b>Stakeholder map</b> (Ana, vol. 1)", "<b>Own the Outcome</b> (this volume)", "<b>The project charter</b> (vol. 2)"],
    quiz=[("Who owns the business case?", "The sponsor."),
          ("Who decides what the app does in Rotterdam?", "Grace. Sanne makes the effect on the date visible."),
          ("Ben says a change will cost four extra days. What does Sanne do?", "It is over the three-day trigger: she takes it to Joost with options, and doesn't decide it herself."),
          ("Accountable or responsible: which can only be one person?", "Accountable."),
          ("Why write “not Sanne's”?", "So others keep their decisions, and nothing falls between two people.")],
    try_it="Write your own role card: four things you answer for, three things you don't (with names), and three triggers that go to your sponsor. Then check: does your sponsor know they are the sponsor?",
    remember="Run the <span class=\"hl\">set</span>. Don't rewrite the <span class=\"hl\">script</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): roles and leadership.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): chapter 3, the role of the project manager.",
             "Scott Berkun, <i>Making Things Happen</i> (2008)."],
)

# ------------------------------------------------------------------ 04 What Was Here Before Me?
en_problem = Doodle(760, 260, "Doodle of 21 January 2026. Sanne's first draft plan is a clean chart, the way she made them at her old job fitting out warehouses. Then reality: a signed lease, a hiring limit of four, no templates, a food-safety registration nobody mentioned, and a Gantt chart from 2025 where nine of fourteen features were late.",
                    "A clean plan, and the surroundings it will have to live in.")
en_problem.box(260, 80, 240, 90, "Sanne's first plan", "y", sub="clean, like her old job", size=18, subsize=14)
for x, y, t in [(20, 20, "lease: 27 April"), (540, 20, "max 4 new hires"), (20, 190, "no templates"), (540, 190, "2025: 9 of 14 late"), (280, 200, "food-safety rules")]:
    en_problem.box(x, y, 200, 50, t, "paper", size=15, dash=True)
en_problem.arrow(220, 46, 262, 86, color="red")
en_problem.arrow(540, 46, 498, 86, color="red")
en_problem.arrow(220, 214, 262, 166, color="red")
en_problem.arrow(540, 214, 498, 166, color="red")

en_analogy = Doodle(760, 240, "Doodle of a gardener who has moved house. Before planting anything she walks the garden: the soil, where the sun falls, the old trees that stay, the neighbour's wall, the local rule against tall hedges, and the shed full of the last owner's tools.",
                    "A good gardener walks the garden before planting: soil, sun, rules, and what the last owner left.")
en_analogy.row([("soil + sun", "what grows here", "green"), ("old trees", "what won't move", "paper"), ("local rules", "what's not allowed", "pink"), ("the shed", "what's already here", "y")], y=50, h=90, size=16, subsize=13)
en_analogy.note(380, 190, "walk first, plant second", "pen", size=20)

en_how = Doodle(760, 380, "Sanne's environment scan for Rotterdam, 21 January 2026, in four boxes. Inside Larder, can't change: the hiring limit of four, one cloud region, StockPilot until June 2027. Inside Larder, can use: the Zuid opening lessons, Ana's walking skeleton in the RTM-0 test store, Grace's weekly demo, Tomás's training plan. Outside, must follow: the lease of 27 April, food-safety registration, building and fire rules, labour law for couriers. Outside, to watch: StockPilot's rate limit, the payment provider, a competitor already in Rotterdam, fridge delivery times.",
                "Four boxes: inside or outside, and a limit or a help.")
for (x, y, t, f, items) in [
        (14, 14, "inside · limits", "pink", ["max 4 new hires in 2026", "one cloud region", "StockPilot until June 2027"]),
        (386, 14, "inside · helps", "green", ["Zuid's opening lessons", "RTM-0 test store (Ana)", "Tomás's training plan"]),
        (14, 198, "outside · must follow", "y", ["lease starts 27 April", "food-safety registration", "building + fire rules"]),
        (386, 198, "outside · watch", "blue", ["StockPilot rate limit", "a rival already in Rotterdam", "fridge lead time: 8 weeks"])]:
    en_how.box(x, y, 360, 168, None, f)
    en_how.head(x + 180, y + 30, t, size=19)
    for i, it in enumerate(items):
        en_how.text(x + 180, y + 66 + i * 32, it, size=16)

ENVIRONMENT = dict(
    slug="project-environment",
    kicker="a.k.a. “the project environment”",
    tldr="No project starts on empty ground. Around it are things <b>inside</b> the organisation (its structure, habits, tools, people, what earlier projects left behind) and things <b>outside</b> (laws, contracts, the market, suppliers). Some are limits, some are help. A plan that ignores them is a plan for a different company. <b>Scan the surroundings first</b>, on one page.",
    chips=[("Family", "foundations"), ("Lives in", "a four-box page, redone each quarter"), ("Pairs with", "constraints and assumptions, the stakeholder map, tailoring")],
    pmbok=dict(covers="the project environment: internal and external influences; organisational knowledge and existing processes",
               principles=["Adopt a holistic view"],
               older="6th: “enterprise environmental factors” (EEFs) and “organizational process assets” (OPAs). 7th: the project environment."),
    problem_side="Larder, 21 January 2026",
    problem="""  <p class="lead">Sanne's last job was fitting out warehouses, where a plan was a contract. Her first Rotterdam draft looks like one. Then she shows it around. Marco: no more than <b>four new hires</b> this year. Ana: StockPilot can't be replaced before <b>June 2027</b>. Tomás: has anyone registered the new store with the food-safety authority? And Ben shows her the <span class="hl-pink">2025 Gantt chart: 14 features, 9 late</span>, which is why his team winces at the word “plan”.</p>
  <ul>
    <li>The plan assumed freedoms Larder doesn't have.</li>
    <li>It ignored things that could help: Zuid's lessons, the test store.</li>
    <li>It used a style of planning the team no longer trusts.</li>
  </ul>""",
    problem_figs=[en_problem],
    analogy_side="walking the garden",
    analogy="""  <p>A gardener who moves house doesn't plant on the first day. She <b>walks the garden</b>: the soil, where the sun falls, the old trees that will stay whatever she wants, the rule about hedge height, and the shed with the last owner's tools. Half of what she finds are limits. The other half she'd have paid for.</p>""",
    analogy_figs=[en_analogy],
    map=[("Soil and sun", "Larder's culture and skills: fast, informal, Python and React Native"),
         ("Old trees that stay", "StockPilot until June 2027; the hiring limit"),
         ("The hedge rule", "The lease, food-safety and labour rules"),
         ("The shed of tools", "Zuid's lessons, RTM-0, Tomás's training plan"),
         ("Walking before planting", "A scan before the plan")],
    how_side="four boxes on one page",
    how="""  <p>Sanne spends two days asking, then fills <b>four boxes</b>. <b>Inside, limits</b>: what Larder won't change for her. <b>Inside, helps</b>: what already exists and can be used. <b>Outside, must follow</b>: laws and contracts. <b>Outside, watch</b>: suppliers, rivals, lead times. Each line gets a name: who knows most about it. The fridge line (eight weeks to deliver) moves straight to the top of her plan.</p>""",
    how_figs=[en_how],
    steps=[("Ask five people “what should I know that isn't written down?”", "Different departments."),
           ("List limits inside the organisation", "Budget rules, hiring, tools, structure."),
           ("List what you can reuse", "Lessons, templates, people who did it before."),
           ("List rules and contracts outside", "Laws, permits, leases, suppliers' terms."),
           ("List outside things to watch", "Market, vendors, lead times."),
           ("Put a name on every line, and redo it each quarter", "Surroundings change.")],
    vocab=[("Project environment", "Everything around the project that affects it, inside and outside the organisation."),
           ("Internal environment", "The organisation's own structure, culture, rules, tools and people."),
           ("External environment", "Laws, markets, suppliers, society: outside the organisation's control."),
           ("Constraint", "A limit the project must work within."),
           ("Organisational knowledge", "Lessons, templates and records from earlier work."),
           ("Governance", "How decisions are made and checked in the organisation.")],
    code=dict(file="rotterdam/environment-scan.md", note="Sanne, 21 January 2026 · review in April", plain=True, src="""
# Rotterdam · the surroundings                                   who knows

INSIDE · LIMITS
  max 4 new hires in 2026                                        Marco
  one cloud region; StockPilot stays until June 2027             Ana
  three product teams, already busy (approvals, flag)            Priya, Grace
INSIDE · HELPS
  Zuid's opening, Nov 2024: 340 products had no price            Tomás, Sam
  RTM-0: a test store, an order end to end since 15 Jan          Ana, Ben
  fortnightly demo; a training plan for pickers                  Grace, Tomás
OUTSIDE · MUST FOLLOW
  lease starts 27 April (rent runs from that day)                Joost
  food-safety registration before the first delivery             Tomás, Lena
  building and fire rules for the fit-out; labour law            Joost, Lena
OUTSIDE · WATCH
  StockPilot: 10 requests a second per account                   Ana
  a rival already delivers in Rotterdam                          Priya
  cold-room and fridge delivery: 8 weeks from order              Joost
"""),
    tools="tools: five conversations and a four-box page. The casebook of the last launch, if there is one.",
    dial=[("Light", "a familiar team, a familiar kind of work", ["Ask “what's changed since last time?”", "A short list.", "No page."]),
          ("Standard", "Rotterdam: a new person, a new city", ["Five conversations.", "The four-box page.", "Names and a review date."]),
          ("Heavy", "a new country, a regulated industry", ["Legal and compliance review.", "A market study.", "A formal constraints and assumptions log."])],
    baseline="Each line compares <b>planning from experience in another company</b> to <b>a four-box scan of Larder's surroundings first</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 4, "The plan fits real limits and lead times."),
             (2, 4, "Fridges and registration found in January."),
             (3, 4, "Limits are written, not assumed."),
             (3, 4, "People see their warnings were heard."),
             (3, 4, "The team's own lessons are used."),
             (3, 4, "Reviewed each quarter."),
             (2, 4, "Zuid's mistakes are designed out."),
             (4, 4, "Two days.")],
    pitfalls=[("Planning like your last company", "The old habits don't fit.", "scan before you plan."),
              ("Only listing limits", "Missing the help.", "ask what can be reused."),
              ("A scan done once", "The world moves.", "redo it each quarter."),
              ("No names", "Nobody to ask when a line changes.", "one name per line.")],
    use=["You're new to the organisation.", "A new city, country or industry.", "Before the first real plan.", "When a plan keeps hitting surprises."],
    skip=["The same team repeats the same kind of project, and nothing around it changed."],
    related=["<b>Constraints vs assumptions</b> (Ana, vol. 1)", "<b>Stakeholder map</b> (Ana, vol. 1)", "<b>See the Whole</b> (this volume)", "<b>How Much Process Do We Need?</b> (this volume)"],
    quiz=[("Name one internal and one external influence on Rotterdam.", "Internal: the hiring limit of four. External: the lease date."),
          ("What did older editions call these?", "Enterprise environmental factors and organisational process assets."),
          ("Why list what helps?", "To reuse it: lessons, the test store, a training plan."),
          ("Sanne learns that fridges take eight weeks to arrive. What does she do with that?", "Puts it in the scan with an owner, and moves the order to the top of the plan: 27 April minus eight weeks is 2 March, and they still have to be fitted, so the order goes out by mid-February."),
          ("How often is the scan redone?", "Each quarter, or when something big changes.")],
    try_it="Ask three colleagues: “what should I know about how things work here that isn't written down?” Sort the answers into the four boxes. Which line changes your plan this week?",
    remember="Walk the <span class=\"hl\">garden</span> before you plant. Half of what you find is <span class=\"hl\">help</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): the project environment.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): chapter 2, the environment in which projects operate.",
             "Michael Watkins, <i>The First 90 Days</i> (2013)."],
)

NOTES = [IS_PROJECT, VALUE_CHAIN, PM_ROLE, ENVIRONMENT]
