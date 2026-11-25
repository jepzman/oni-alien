# Series 2 · Book 5 · The IT Operations Notebook · Vol. 1 · What we run.
# Narrator: Eli (he/him). Running case study: Larder (facts in docs/larder-casebook.md, "Book 5, Vol. 1").
# Spine: ITIL 4 practices, with SRE habits. Names are PeopleCert's; every explanation is in our own words.

# ------------------------------------------------------------------ 01 What Is IT Operations For?
wo_problem = Doodle(760, 270, "Doodle of Eli's week of 23 March 2026, as Sanne's levelling showed it: platform work two and a half days, the Dispatch RFC one and a half, on call one, the Rotterdam internet line one, extras one and a half, an alert fix half a day. Eight days of work in a five-day week. Underneath, Eli's own list of 23 things he did that week, and only 9 of them can be traced to anything a customer would notice.",
                    "160 % of a week, and most of it couldn't say which customer it was for.")
for i, (t, w, f) in enumerate([("platform", "2½ d", "blue"), ("RFC-003", "1½ d", "blue"), ("on call", "1 d", "pink"),
                               ("internet line", "1 d", "y"), ("extras", "1½ d", "y"), ("alert fix", "½ d", "pink")]):
    eli = 14 + i * 124
    wo_problem.box(eli, 24, 112, 78, t, f, sub=w, size=15, subsize=14)
wo_problem.line("M14 128 h732", thin=True, dash=True)
wo_problem.note(380, 156, "8 days of work · 5-day week · 160 %", "red", size=20)
wo_problem.box(110, 182, 540, 56, "23 jobs last week · 9 traceable to a customer", "paper", size=17)

wo_analogy = Doodle(760, 240, "Doodle of a hospital's facilities team. Nobody comes to a hospital for the boilers, the lifts or the backup generator. They come for an operation. The facilities team exists so the operating theatre is warm, lit and powered at 3 a.m. Their success is measured in operations that went ahead, not in boilers serviced.",
                    "Nobody visits a hospital for the boiler. The boiler exists so the operation can go ahead.")
wo_analogy.row([("boiler · lifts · generator", "what facilities run", "paper"), ("warm, lit, powered theatre", "what it makes possible", "blue"), ("the operation goes ahead", "why anyone cares", "green")], y=40, h=96, gap=40, size=16, subsize=14, arrows=True)
wo_analogy.note(380, 196, "measured by operations that happened, not boilers serviced", "pen", size=18)

wo_how = Doodle(760, 360, "Eli's first page, Monday 30 March 2026. At the top, what customers buy: an express order in 30 minutes, a slot order in a chosen hour, and from May a weekly office restock for Korenwolf. In the middle, the work that delivers it: ordering, paying, picking, dispatching, delivering. At the bottom, what IT operations keeps running for each: the apps and Larder Core, the payment provider link, the picker handhelds and store Wi-Fi, Dispatch. On the right, the two numbers Eli will judge his work by: a four-hour outage costs about 60,000 euros of orders, and King's Day 2025 lost 40 minutes of checkout.",
                "Start from what customers buy, work down to what has to keep running. That's the job.")
wo_how.row([("express · 30 min", None, "green"), ("slots · 1 hour", None, "green"), ("office restock", "from May", "green")], x=14, y=14, h=60, w=166, gap=12, size=16, subsize=13)
wo_how.row([("order", None, "blue"), ("pay", None, "blue"), ("pick", None, "blue"), ("dispatch", None, "blue"), ("deliver", None, "blue")], x=14, y=110, h=52, w=100, gap=6, size=15)
wo_how.row([("apps + Core", None, "paper"), ("PSP link", None, "paper"), ("handhelds", None, "paper"), ("Dispatch", None, "paper"), ("courier app", None, "paper")], x=14, y=200, h=52, w=100, gap=6, size=14)
wo_how.note(270, 96, "what customers buy", "pen", size=15)
wo_how.note(270, 188, "the work that delivers it", "pen", size=15)
wo_how.note(270, 280, "what IT operations keeps running", "pen", size=15)
wo_how.box(560, 14, 186, 238, None, "y")
wo_how.head(653, 46, "judged by", size=17)
wo_how.text(653, 92, "4 h down", size=17)
wo_how.text(653, 116, "≈ €60k lost", size=16)
wo_how.text(653, 168, "King's Day '25", size=16)
wo_how.text(653, 192, "40 min, no checkout", size=15)
wo_how.note(380, 334, "if a job can't be traced up this page, ask why it exists", "red", size=18)

WHAT_IS_IT_OPS = dict(
    slug="what-is-it-operations",
    kicker="a.k.a. “the service value system”",
    tldr="IT operations exists so that the <b>services customers pay for keep working</b>: an order placed, paid, picked and delivered. Servers, networks and laptops are the means, not the point. ITIL 4 calls the whole picture a <b>service value system</b>: value is created <b>with</b> the customer, when the service is used. Start every operations question from the outcome: <b>who would notice, and how much would it cost them?</b>",
    chips=[("Family", "foundations"), ("Lives in", "the first page of the runbook binder"), ("Pairs with", "the service catalogue, the guiding principles")],
    itil=dict(groups=["general"], chain=["plan", "engage", "deliver"], practices=["the service value system", "the four dimensions"],
              sre="“reliability is a feature, and the most important one”", principles=["Focus on value", "Start where you are"],
              older="ITIL v3: service strategy, the service lifecycle"),
    problem_side="Larder, 30 March 2026",
    problem="""  <p class="lead">Sanne's levelling sheet for the week of <b>23 March 2026</b> showed Eli at <b>160 %</b>: platform work, the Dispatch RFC, a week on call, Rotterdam's internet line and an alert fix. Ana took his on-call week and Ben took the Dispatch code. On Monday 30 March Eli writes down the 23 jobs he did the week before. <span class="hl-pink">He can link only 9 of them to anything a customer would notice.</span></p>
  <ul>
    <li>Urgent and important look the same when everything arrives by chat.</li>
    <li>Nobody can say which systems matter most, so all of them get the same attention.</li>
    <li>Rotterdam opens in four weeks, and it will add work, not remove it.</li>
  </ul>""",
    problem_figs=[wo_problem],
    meanwhile=[("project-4", "resource-levelling", "Sanne's levelling sheet: Eli at 160 % in the week of 23 March; on call swapped to Ana, the Dispatch code to Ben, key people planned at 80 % from then on.",
                "Eli's first page in his own notebook, the Monday after: 23 jobs, 9 traceable to a customer, and the question “what is all this for?”")],
    analogy_side="the hospital's boiler room",
    analogy="""  <p>Nobody goes to a hospital for the <b>boilers, the lifts or the backup generator</b>. They go for an operation. The facilities team exists so the operating theatre is <b>warm, lit and powered at 3 a.m.</b> A good facilities manager knows which machines the theatre needs, and measures the team by operations that went ahead, not by boilers serviced.</p>""",
    analogy_figs=[wo_analogy],
    map=[("The operation", "An order delivered on time, as promised"),
         ("Warm, lit, powered theatre", "Ordering, payment, picking and Dispatch working"),
         ("Boilers, lifts, generator", "Larder Core's VMs, Postgres, store Wi-Fi, handhelds"),
         ("Facilities manager", "Eli"),
         ("“Operations that went ahead”", "Orders placed, picked and delivered; minutes of outage avoided")],
    how_side="from what customers buy, down to what must keep running",
    how="""  <p>Eli draws one page. At the top is <b>what customers buy</b>: express in 30 minutes, a one-hour slot, and from May a weekly office restock for Korenwolf. Below that is the work that delivers it: <b>order, pay, pick, dispatch, deliver</b>. At the bottom is what IT operations keeps running for each step. On the side are the two numbers he'll judge his work by: a <b>four-hour outage ≈ €60k</b> of lost orders, and <b>King's Day 2025</b>, when checkout timed out for 40 minutes.</p>
  <p>Then he checks the page against ITIL's <b>four dimensions</b>. Every service needs <b>people</b> (who runs it), <b>information and technology</b> (what it runs on), <b>partners and suppliers</b> (the PSP, StockPilot, the cloud) and a <b>value stream</b> (the steps from order to doorstep). His page had the technology, but it was missing the people and the partners.</p>""",
    how_figs=[wo_how],
    steps=[("Write down what customers buy", "In their words: “groceries in 30 minutes”, not “the order API”."),
           ("Draw the steps that deliver it", "Order, pay, pick, dispatch, deliver: the value stream."),
           ("List what each step runs on", "Apps, services, devices, networks, vendors."),
           ("Put a price on downtime", "Euros, orders or angry customers per hour, even roughly."),
           ("Check the four dimensions", "People, technology, partners, value streams: which is missing?"),
           ("Trace last week's work up the page", "Anything that doesn't trace up needs a reason.")],
    vocab=[("Service", "A way of delivering value to customers: they get an outcome without owning the costs and risks."),
           ("Value", "What the customer gets out of it: groceries on time, not uptime."),
           ("Outcome", "The result the customer wants. An output is what we produce on the way."),
           ("Service value system", "ITIL 4's picture of how demand becomes value: principles, governance, the value chain, practices, improvement."),
           ("Four dimensions", "People and organisation, information and technology, partners and suppliers, value streams and processes."),
           ("IT operations", "The day-to-day work of keeping services running, and restoring them when they stop.")],
    code=dict(file="ops/00-what-we-are-for.md", note="Eli · Mon 30 March 2026", plain=True, src="""
# What IT operations at Larder is for

Customers buy      express (30 min) · slots (1 hour) · office restock (from 4 May)
Delivered by       order → pay → pick → dispatch → deliver
We keep running    apps + Larder Core · PSP link · handhelds + store Wi-Fi
                   · Dispatch · courier app · the people who answer
A bad hour costs   ≈ €15k of orders (a 4-hour outage ≈ €60k)
Worst so far       King's Day 2025: checkout down 40 min at 5× peak

Last week          23 jobs · 9 traced to a customer · 14 to ask about
Missing            people (one person knows everything)
                   partners (vendor contacts live in my inbox)
"""),
    tools="tools: one page, a pen and last week's calendar. The hard part is admitting how much of the week doesn't trace up.",
    ladder=[("nobody has written down what it's for", ["Work arrives by chat.", "Everything is urgent.", "The engineer decides alone."]),
            ("one page: customers, steps, systems", ["Outcomes named.", "A rough price for downtime.", "Shared at the tech leads' meeting."]),
            ("the page drives the work", ["Each job tagged to a service.", "Monthly look at where time went.", "Downtime cost in every incident note."]),
            ("measured all the time", ["Live view of orders affected.", "Cost of incidents reported monthly.", "Planning starts from it."])],
    ladder_now=1,
    baseline="Each line compares <b>running whatever arrives in the chat</b> to <b>starting from what customers buy and what it costs when it stops</b>.",
    ratings=[(2, 4, "The work is aimed at what customers feel."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral on its own."),
             (3, 3, "Neutral."),
             (1, 3, "One page shows what matters and why."),
             (2, 3, "Fourteen jobs get questioned."),
             (2, 4, "A price on downtime makes trade-offs possible."),
             (1, 2, "Still one person, but now it's written down."),
             (4, 4, "Half a day.")],
    pitfalls=[("Starting from the servers", "A list of machines says nothing about which one matters.", "start from what customers buy."),
              ("No price for downtime", "Every fix looks equally urgent.", "a rough euro figure per hour is enough."),
              ("Forgetting people and partners", "The technology is drawn; the person who knows how it works and the vendor's phone number are not.", "check all four dimensions."),
              ("A page nobody reads again", "It's written once and then ignored.", "trace last week's work up it every month.")],
    use=["You've inherited “everything technical”.", "Your week is full but you can't say what it protected.", "Before building a catalogue or an on-call rota.", "Someone asks “why do we need an ops person?”"],
    skip=["The team already plans from clear service outcomes.", "A one-off script with no users."],
    related=["<b>What Do We Run, and Who Owns It?</b> (next note)", "<b>Who Is Overloaded?</b> (Sanne, vol. 4)", "<b>Business drivers</b> (Ana, vol. 1)", "<b>Outcomes over outputs</b> (Grace, vol. 1)"],
    quiz=[("What is IT operations for, in one sentence?", "Keeping the services customers pay for working, and restoring them quickly when they stop."),
          ("Where is value created, according to ITIL 4?", "With the customer, when they use the service: not in the server room."),
          ("Name the four dimensions.", "People and organisation; information and technology; partners and suppliers; value streams and processes."),
          ("Why put a price on downtime, even a rough one?", "So trade-offs (what to fix first, what to spend) can be made in the same units as the business uses."),
          ("Which dimension was missing from Eli's first page?", "People (it all lived in his head) and partners (vendor contacts were in his inbox).")],
    quiz_sit=[("A manager asks you to “just keep the servers up”. What do you ask back?", "Which customer outcomes the servers support, and what an hour without each one costs. Then you can say which servers matter most.")],
    try_it="Write what your customers buy at the top of a page, the steps that deliver it in the middle, and what you keep running at the bottom. Now take last week's calendar: how many of your jobs trace up the page?",
    remember="Nobody buys uptime. They buy <span class=\"hl\">an order that arrives</span>. Start from that, and price the hour it doesn't.",
    sources=["AXELOS, <i>ITIL 4 Foundation</i> (2019): key concepts, the four dimensions and the service value system.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (O'Reilly, 2016): introduction.",
             "Gene Kim et al., <i>The Phoenix Project</i> (2013)."],
)

# ------------------------------------------------------------------ 02 What Do We Run, and Who Owns It?
wr_problem = Doodle(760, 260, "Doodle of 2 April 2026. Eli lists everything he looks after on sticky notes: 47 of them, from Larder Core's three virtual machines to the label printers at Zuid and the domain name. When he groups them into services, four groups have no owner at all: the store network, staff accounts and laptops, the nightly price script, and the domain and email.",
                    "47 things on the wall. Four services that belong to nobody.")
for i in range(18):
    r, c = divmod(i, 9)
    wr_problem.box(14 + c * 82, 20 + r * 52, 72, 40, None, ["y", "blue", "green"][i % 3], rx=3)
wr_problem.note(380, 150, "47 components · 11 services", "pen", size=20)
for i, t in enumerate(["store network", "accounts + laptops", "price script", "domain + email"]):
    wr_problem.box(14 + i * 186, 176, 172, 56, t, "pink", stroke="red", size=15)

wr_analogy = Doodle(760, 230, "Doodle of a restaurant menu next to the kitchen's equipment list. Guests order from the menu: dishes in plain words, with a price. The equipment list (ovens, fridges, the dishwasher) matters only because of what it lets the kitchen cook. Each dish has a chef responsible for it.",
                    "Guests read the menu, not the list of ovens. Each dish has a chef who answers for it.")
wr_analogy.icon("menu", 90, 30, 1.5)
wr_analogy.box(190, 40, 230, 100, "the menu", "green", sub="dishes · prices · chef", size=19)
wr_analogy.icon("kitchen", 470, 54, 1.2)
wr_analogy.box(570, 40, 176, 100, "equipment", "paper", sub="ovens · fridges", size=18)
wr_analogy.note(380, 196, "what people use vs what it runs on", "pen", size=18)

wr_how = Doodle(760, 380, "Larder's service catalogue, version 1, 2 April 2026. Eleven services in three tiers. Critical: ordering (owner Ben), payments (Cho), Dispatch (Eli and Ben), the picker app (Dee). Important: stock sync with StockPilot (Eli), store network (Eli), courier app (Dee), the helpdesk (Sam). Normal: staff accounts and laptops (Eli), the nightly price script (Eli), domain and email (Eli). Every row has users and a 'what if it stops' line.",
                "Eleven services, three tiers, one owner each. Eli owns too many: that's the next problem, but now it's visible.")
tiers = [("critical", "pink", [("ordering", "Ben"), ("payments", "Cho"), ("Dispatch", "Eli + Ben"), ("picker app", "Dee")]),
         ("important", "y", [("stock sync", "Eli"), ("store network", "Eli"), ("courier app", "Dee"), ("helpdesk", "Sam")]),
         ("normal", "paper", [("accounts + laptops", "Eli"), ("price script", "Eli"), ("domain + email", "Eli")])]
for r, (name, fill, items) in enumerate(tiers):
    y = 14 + r * 112
    wr_how.box(14, y, 120, 96, name, fill, size=17)
    for c, (svc, own) in enumerate(items):
        wr_how.box(146 + c * 152, y, 142, 96, svc, fill, sub=own, size=15, subsize=14)
wr_how.note(380, 366, "Eli's name on 6 of 11 rows", "red", size=18)

WHAT_WE_RUN = dict(
    slug="what-we-run",
    kicker="a.k.a. “service catalogue management”",
    tldr="A <b>service catalogue</b> lists what you run <b>as the people who use it would describe it</b>: “ordering”, not “VM 2”. Each line has an <b>owner</b> who answers for it, its <b>users</b>, how much it matters (a <b>tier</b>) and what happens if it stops. It turns a pile of servers and SaaS logins into a short list you can rank, staff and promise things about.",
    chips=[("Family", "knowing what you run"), ("Lives in", "ops/catalogue.md, reviewed every quarter"), ("Pairs with", "the dependency map, service owners, the on-call rota")],
    itil=dict(groups=["service"], chain=["plan", "engage"], practices=["service catalogue management", "relationship management (owners)"],
              sre="“service ownership”", principles=["Focus on value", "Keep it simple and practical"],
              older="ITIL v3: the service catalogue and service portfolio"),
    problem_side="Larder, 2 April 2026",
    problem="""  <p class="lead">Eli writes everything he looks after on sticky notes: <b>47</b>, from Larder Core's three VMs to Zuid's label printers and the domain name. Grouped by what people use them for, they become <b>11 services</b>. <span class="hl-pink">Four of them have no owner at all</span>: the store network, staff accounts and laptops, the nightly price script, and the domain and email. They're Eli's by default, because nobody else knows they exist.</p>
  <ul>
    <li>Nobody can say which service matters most, so the loudest one wins.</li>
    <li>An unowned service only gets attention when it breaks.</li>
    <li>On-call can't be shared when nobody knows what they're on call for.</li>
  </ul>""",
    problem_figs=[wr_problem],
    analogy_side="the menu and the oven list",
    analogy="""  <p>A restaurant has two lists. Guests read <b>the menu</b>: dishes in plain words, each with a price. The kitchen has an <b>equipment list</b>: ovens, fridges, the dishwasher. Nobody orders an oven. The menu is what you promise, and <b>each dish has a chef</b> who answers for it when it comes back.</p>""",
    analogy_figs=[wr_analogy],
    map=[("A dish on the menu", "A service: ordering, payments, Dispatch, the store network"),
         ("Its price", "Its tier: critical, important, normal"),
         ("The chef who answers for it", "The service owner"),
         ("The equipment list", "Components: VMs, databases, routers, SaaS accounts"),
         ("Dishes nobody cooks any more", "Services to retire")],
    how_side="eleven lines, an owner each, and a tier",
    how="""  <p>For each group Eli writes one line: <b>name</b> (in users' words), <b>what it does</b>, <b>users</b>, <b>owner</b>, <b>tier</b> and <b>if it stops</b>. Critical means customers can't order, pay, be picked for or be delivered to. Important means someone has a workaround for a few hours. Normal can wait until morning.</p>
  <p>At Thursday's tech leads' meeting (2 April, 09:30) owners sign their own lines. The four orphans go to Eli for now, but written down, with a note: <b>“Eli owns 6 of 11: next problem.”</b> The catalogue becomes the spine for everything after it: dependencies, the on-call rota, the alerts and the runbooks.</p>""",
    how_figs=[wr_how],
    steps=[("List everything you look after", "Sticky notes, no sorting yet."),
           ("Group by what people use it for", "A service is something a user would name."),
           ("Write one line per service", "Name, what it does, users, owner, tier, if it stops."),
           ("Get each owner to sign their line", "An owner who wasn't asked isn't an owner."),
           ("Mark the orphans honestly", "Unowned is a finding, not a failure."),
           ("Review it every quarter", "And whenever something new goes live.")],
    vocab=[("Service catalogue", "The list of live services, described for the people who use them."),
           ("Service owner", "The person accountable for a service working: they don't have to do every task themselves."),
           ("Tier", "How much a service matters; it sets on-call, alerting and recovery targets."),
           ("Component", "A part a service runs on: a VM, a database, a router, a SaaS account."),
           ("Orphan", "A service nobody owns; usually discovered during an incident."),
           ("Service portfolio", "Everything in the pipeline, live and being retired; the catalogue is the live part.")],
    code=dict(file="ops/catalogue.md", note="v1 · signed at tech leads, Thu 2 April 2026", plain=True, src="""
service           tier       owner      users              if it stops
ordering          critical   Ben        customers          no orders: ≈ €15k/hour
payments          critical   Cho        customers          orders fail at the last step
Dispatch          critical   Eli + Ben  couriers, stores   couriers assigned by hand
picker app        critical   Dee        pickers            offline mode for ≈ 2 hours
stock sync        important  Eli        stores, customers  stale stock, more swaps
store network     important  Eli        pickers            4G backup (Rotterdam only)
courier app       important  Dee        couriers           paper routes, phone calls
helpdesk          important  Sam        support agents     email inbox fallback
accounts+laptops  normal     Eli        staff              new starters wait
price script      normal     Eli        customers          yesterday's prices
domain + email    normal     Eli        everyone           …everything, eventually

Eli owns 6 of 11.  Next problem.
"""),
    tools="tools: sticky notes, then one markdown table in the repo. A CMDB tool can come later, if ever.",
    ladder=[("it's all in one head", ["Ask Eli.", "Orphans found during incidents."]),
            ("one signed table", ["Owner, tier and “if it stops” per line.", "Reviewed quarterly."]),
            ("generated from code", ["Services tagged in the infrastructure code.", "The table is checked against it in CI."]),
            ("self-service", ["New services register themselves.", "Owners and tiers shown in the alert and the ticket."])],
    ladder_now=1,
    baseline="Each line compares <b>47 things in one engineer's head</b> to <b>eleven owned, tiered services in one signed table</b>.",
    ratings=[(2, 3, "Critical services are known, so they get attention first."),
             (3, 3, "Neutral on its own."),
             (2, 3, "The owner is known before the incident."),
             (3, 3, "Neutral."),
             (1, 4, "One table anyone can read."),
             (3, 3, "Neutral."),
             (2, 4, "Effort goes to the critical tier."),
             (1, 3, "Owners are named, though Eli still has six."),
             (4, 4, "One afternoon, then a quarterly look.")],
    pitfalls=[("Listing servers, not services", "“VM 2” means nothing to the person reporting a problem.", "name it as a user would."),
              ("Owners who weren't asked", "A name in a table nobody agreed to.", "owners sign their own line."),
              ("Everything is critical", "The tier stops meaning anything.", "critical = customers can't order, pay or get delivered."),
              ("A catalogue that never changes", "New services go live and never get added.", "add it to the go-live checklist.")],
    use=["Nobody can answer “what do we run?” in one minute.", "Before you set up on-call or alerts.", "A new service is about to go live (Rotterdam).", "Incidents keep finding things nobody knew about."],
    skip=["A team with one service and one owner.", "You already have a maintained catalogue: review it instead."],
    related=["<b>What Is Connected to What?</b> (next note)", "<b>Service Catalogue</b> (cloud, vol. 6)", "<b>Who Gets Woken Up?</b> (this volume)", "<b>Application Portfolio (TIME)</b> (Ana, vol. 4)"],
    quiz=[("What is the difference between a service and a component?", "A service is what users use and would name (ordering); a component is what it runs on (a VM, a database)."),
          ("What does a service owner have to do?", "Answer for the service working: decisions, priorities, being reachable. Not every task personally."),
          ("What makes a Larder service critical?", "If it stops, customers can't order, pay, be picked for or be delivered to."),
          ("Why write down the orphans instead of quietly taking them?", "Unowned services are a risk the business should see; hidden, they stay Eli's forever."),
          ("When must the catalogue be updated?", "At every go-live, and at a quarterly review.")],
    quiz_sit=[("A new service goes live without anyone adding it to the catalogue. Two months later it breaks at night. What would have helped?", "A go-live checklist line: “added to the catalogue with owner and tier”. Then on-call would have known who to call and how much it mattered.")],
    try_it="List everything you look after on sticky notes. Group them into services a user would name. Write owner, tier and “if it stops” for each. How many have your name on them? How many have none?",
    remember="A service is what <span class=\"hl\">users would name</span>, and every service needs a name next to it: <span class=\"hl\">its owner</span>.",
    sources=["AXELOS, <i>ITIL 4: Service catalogue management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter on service ownership.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019): ownership boundaries."],
)

# ------------------------------------------------------------------ 03 What Is Connected to What?
dm_problem = Doodle(760, 250, "Doodle of 7 April 2026. Eli asks four engineers to draw what checkout depends on. He gets four different drawings: Ben's has five boxes, Cho's has the payment provider and nothing else, Dee's starts at the app, and Eli's own has nine boxes but forgets the address lookup service that every checkout calls.",
                    "Four engineers, four drawings of checkout. None of them complete.")
for i, (who, n) in enumerate([("Ben", "5 boxes"), ("Cho", "PSP only"), ("Dee", "starts at the app"), ("Eli", "9, no address lookup")]):
    dm_problem.box(14 + i * 186, 30, 172, 110, who, ["blue", "y", "green", "pink"][i], sub=n, size=20, subsize=14)
dm_problem.note(380, 190, "“what does checkout need to work?”", "red", size=20)
dm_problem.note(380, 222, "four answers", "pen", size=18)

dm_analogy = Doodle(760, 220, "Doodle of a theatre's cue sheet for opening night: the lights depend on the dimmer rack, the dimmer rack on the mains, the sound on the mixing desk, the mixing desk on one extension lead under the stage. The stage manager draws it so that when the stage goes dark, she knows to check the extension lead.",
                    "The stage manager knows the sound desk hangs on one extension lead under the stage.")
dm_analogy.row([("stage lights", None, "y"), ("dimmer rack", None, "paper"), ("mains", None, "paper")], x=14, y=30, h=56, w=200, gap=40, size=17, arrows=True)
dm_analogy.row([("sound", None, "blue"), ("mixing desk", None, "paper"), ("one extension lead", None, "pink")], x=14, y=120, h=56, w=200, gap=40, size=17, arrows=True)
dm_analogy.note(380, 208, "know the single lead before the show", "pen", size=17)

dm_how = Doodle(760, 400, "Larder's dependency map for checkout, 7 April 2026. The customer app and web shop call Larder Core on three virtual machines. Larder Core depends on Postgres, the payment provider, the address lookup service, the push notification service, the cloud DNS, and a TLS certificate. Two surprises are circled in red: the address lookup service is on a free plan limited to 10,000 calls a day, and the nightly price script runs on virtual machine 2 only.",
                "Checkout hangs on eleven things. Two of them were surprises, and one would have broken in Rotterdam's first week.")
dm_how.box(300, 14, 160, 60, "customer app", "green", size=16)
dm_how.box(300, 120, 160, 70, "Larder Core", "blue", sub="3 VMs", size=17, subsize=14)
dm_how.arrow(380, 76, 380, 118)
deps = [("Postgres", "paper", 14, 250), ("PSP", "paper", 136, 250), ("address lookup", "pink", 258, 250), ("push service", "paper", 380, 250),
        ("DNS", "paper", 502, 250), ("certificate", "paper", 624, 250)]
for t, f, x, y in deps:
    dm_how.box(x, y, 112, 58, t, f, size=14, stroke="red" if f == "pink" else "")
    dm_how.arrow(380, 192, x + 56, y - 2, dash=True)
dm_how.box(14, 120, 220, 70, "price script", "pink", sub="VM 2 only", stroke="red", size=16, subsize=14)
dm_how.note(318, 336, "free plan: 10,000 calls a day · Rotterdam ≈ 14,000", "red", size=16)
dm_how.note(380, 376, "drawn once, then checked in every incident review", "pen", size=17)

DEPENDENCY_MAP = dict(
    slug="dependency-map",
    kicker="a.k.a. “service configuration management”",
    tldr="A <b>dependency map</b> shows, for each service, the components and other services it needs to work, inside and outside the company. It's what on-call looks at first: if checkout fails, which of the eleven things below it is broken? ITIL calls the information <b>configuration items</b> and their relationships. Keep it <b>per service, small and checked against reality</b>, and the surprises show up before an incident does.",
    chips=[("Family", "knowing what you run"), ("Lives in", "ops/services/&lt;service&gt;.md, one drawing each"), ("Pairs with", "the catalogue, deployment diagrams, runbooks")],
    itil=dict(groups=["service"], chain=["design", "deliver"], practices=["service configuration management"],
              sre="“know your dependencies”: a dependency is part of your reliability", principles=["Think and work holistically"],
              older="ITIL v3: configuration management, the CMDB"),
    problem_side="Larder, 7 April 2026",
    problem="""  <p class="lead">Eli asks Ben, Cho and Dee to draw what checkout needs in order to work, and draws his own. <b>Four drawings, none alike.</b> Ben has five boxes; Cho draws the payment provider and stops; Dee starts at the app. Eli's has nine, and it misses the <b>address lookup service</b> that every checkout calls. <span class="hl-pink">If the team can't agree what checkout depends on, an incident starts with an argument.</span></p>
  <ul>
    <li>Each engineer knows their own corner.</li>
    <li>Outside services (SaaS, DNS, certificates) are the least drawn and the most surprising.</li>
    <li>Rotterdam will put more load on all of them in three weeks.</li>
  </ul>""",
    problem_figs=[dm_problem],
    analogy_side="the stage manager's cue sheet",
    analogy="""  <p>A theatre's stage manager draws what each part of the show hangs on: the lights on the dimmer rack, the dimmer rack on the mains, the sound on the mixing desk, and the mixing desk on <b>one extension lead under the stage</b>. When the sound dies mid-scene, she doesn't debate it. She sends someone to the lead.</p>""",
    analogy_figs=[dm_analogy],
    map=[("The show", "Checkout: a customer pays for a basket"),
         ("Lights, sound", "Larder Core, the apps"),
         ("Dimmer rack, mixing desk", "Postgres, the PSP, DNS, the push service"),
         ("The single extension lead", "The address lookup service on a free plan"),
         ("The cue sheet", "The dependency map in ops/services/")],
    how_side="one drawing per critical service, then go and check",
    how="""  <p>Eli takes the four drawings and merges them into one per critical service, starting with checkout. Then he <b>checks it against reality</b>. He reads the network rules and the code that calls outside services, and looks at a week of outgoing traffic. That finds <b>eleven</b> dependencies, and two surprises:</p>
  <ul>
    <li>The <b>address lookup</b> SaaS is on a <b>free plan, 10,000 calls a day</b>. Amsterdam uses about 9,000. With Rotterdam, the estimate is 14,000. He moves it to a paid plan (€49 a month) on 8 April.</li>
    <li>The <b>nightly price script</b> runs on <b>VM 2 only</b>: if VM 2 is down at 02:00, tomorrow's prices are yesterday's. He writes it down as a known single point, and it becomes a runbook.</li>
  </ul>
  <p>Each map lives next to its service page, and every incident review asks: <b>was the map right?</b></p>""",
    how_figs=[dm_how],
    steps=[("Pick one critical service", "Checkout first: it pays the bills."),
           ("Ask several people to draw it", "The differences are the interesting part."),
           ("Merge, then check against reality", "Network rules, outgoing calls, config, contracts."),
           ("Mark outside dependencies clearly", "SaaS, DNS, certificates, the cloud provider."),
           ("Circle single points and limits", "Free plans, one machine, one person."),
           ("Check the map in every incident review", "Was it right? Fix it the same day.")],
    vocab=[("Dependency", "Something a service needs in order to work."),
           ("Configuration item (CI)", "ITIL's name for a thing you track: a server, an app, a contract, a certificate."),
           ("Relationship", "How two CIs are linked: runs on, calls, needs."),
           ("CMDB", "A configuration management database. Useful when maintained, misleading when not."),
           ("Single point of failure", "One part whose failure stops the whole service."),
           ("Hidden dependency", "One nobody drew: found by reading traffic, or by an incident.")],
    code=dict(file="ops/services/checkout.md", note="dependency map · checked 7 April 2026", plain=True, src="""
# checkout · critical · owner Ben

needs                 kind        if it fails                  note
Larder Core (3 VMs)   ours        no checkout                  any 2 of 3 is enough
Postgres primary      managed     no checkout                  replica is read-only
PSP A                 vendor      cards + iDEAL fail           24/7 line in vendors.md
address lookup        vendor      checkout blocked at address  ⚠ free plan 10k/day →
                                                               paid plan from 8 Apr
push service          vendor      no "order on its way"        checkout still works
cloud DNS             vendor      nothing resolves             TTL 300 s
TLS certificate       ours        browsers refuse              expires 14 Jun, renew!
price script          ours        yesterday's prices           ⚠ VM 2 only, 02:00
StockPilot sync       vendor      stale stock, more swaps      not on the checkout path
"""),
    tools="tools: a whiteboard, then a text file per service. Read outgoing traffic logs and network rules to check it. A CMDB tool only if someone will keep it right.",
    ladder=[("in people's heads", ["Each engineer knows a corner.", "Hidden dependencies found by incidents."]),
            ("a drawing per critical service", ["Checked against traffic and config.", "Fixed in every incident review."]),
            ("generated from code and traffic", ["Infrastructure code and tracing draw most of it.", "Differences flagged weekly."]),
            ("live", ["A service map from tracing, always current.", "Shown in the alert itself."])],
    ladder_now=1,
    baseline="Each line compares <b>four partial drawings in four heads</b> to <b>one checked map per critical service</b>.",
    ratings=[(2, 3, "A rate limit was found before Rotterdam hit it."),
             (2, 3, "Two single points written down; one fixed."),
             (2, 4, "On-call starts from a picture."),
             (3, 3, "Neutral."),
             (1, 4, "Outside services are finally on paper."),
             (3, 3, "Neutral."),
             (3, 4, "€49 a month instead of a blocked checkout."),
             (2, 3, "Others can reason about checkout without Eli."),
             (3, 3, "A day for the first map; minutes to keep it right.")],
    pitfalls=[("Only drawing what you built", "SaaS, DNS and certificates are left out, and they're the ones that surprise you.", "list outside dependencies first."),
              ("A giant map of everything", "Too big to read in an incident.", "one small map per critical service."),
              ("Trusting the drawing", "It shows what people believe.", "check it against traffic, rules and contracts."),
              ("A CMDB nobody maintains", "Wrong data is worse than none.", "keep it next to the service and fix it in reviews.")],
    use=["Engineers disagree about what a service needs.", "Before a big change in load (a new city).", "Incidents keep finding surprises.", "You use several SaaS services on a critical path."],
    skip=["A tiny service with no outside calls.", "You already have accurate tracing that draws it for you: check it, don't redraw it."],
    related=["<b>What Do We Run, and Who Owns It?</b> (this volume)", "<b>Deployment Diagrams</b> (Ana, vol. 3)", "<b>SaaS & Vendor Integration</b> (Ana, vol. 4)", "<b>What Do I Do at 3 a.m.?</b> (this volume)"],
    quiz=[("What does a dependency map show?", "For one service: everything it needs to work, ours and outside, and what happens if each one fails."),
          ("How did Eli find the address lookup limit?", "By checking the drawing against reality: outgoing calls and the vendor's plan, not by asking people."),
          ("Why one small map per service instead of one big one?", "It can be read in an incident, and the owner can keep it right."),
          ("What is a configuration item?", "Anything you track because it affects a service: server, app, contract, certificate."),
          ("When should the map be checked again?", "In every incident review, and before big load changes.")],
    quiz_sit=[("Checkout fails at 19:00. The on-call engineer suspects the database, but it looks healthy. What do they do next?", "Open checkout's dependency map and go down the list: PSP, address lookup, DNS, certificate. Check each one's status instead of debating the database.")],
    try_it="Ask three colleagues to draw what your most important service needs, separately. Compare. Then check the merged drawing against network rules and outgoing calls. What did nobody draw?",
    remember="If the team draws it <span class=\"hl\">four different ways</span>, the incident will start with an argument. Draw it once, then <span class=\"hl\">check it against reality</span>.",
    sources=["AXELOS, <i>ITIL 4: Service configuration management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 22, cascading failures.",
             "Simon Brown, <i>The C4 Model</i>: deployment and dynamic diagrams."],
)

# ------------------------------------------------------------------ 04 What Do We Own, and Where Is It?
ia_problem = Doodle(760, 260, "Doodle of 9 April 2026. Eli tries to count Larder's devices and subscriptions. Handhelds: 62 at Noord and Zuid, 30 on their way to Rotterdam, but 4 at Zuid can't be found. 46 SaaS subscriptions, 9 of them still paying for people who left, about 340 euros a month. And the domain larder.nl renews on 23 April on Jasper's personal credit card, which expired.",
                    "Four handhelds missing, nine paid seats for people who left, and the domain on an expired personal card.")
ia_problem.icon("phone", 40, 30, 1.2)
ia_problem.box(110, 30, 180, 80, "92 handhelds", "blue", sub="4 not found", size=18, subsize=15)
ia_problem.icon("receipt", 330, 30, 1.2)
ia_problem.box(400, 30, 160, 80, "46 SaaS", "y", sub="9 for leavers", size=18, subsize=15)
ia_problem.box(590, 30, 156, 80, "€340", "y", sub="a month, wasted", size=18, subsize=15)
ia_problem.box(110, 150, 540, 64, "larder.nl renews 23 Apr · Jasper's card, expired", "pink", stroke="red", size=16)
ia_problem.note(380, 244, "two weeks from losing the domain", "red", size=18)

ia_analogy = Doodle(760, 220, "Doodle of a school's equipment cupboard with a sign-out sheet: each projector, laptop and microphone has a number, the name of who has it, and when it's due back. The caretaker checks the cupboard against the sheet once a term.",
                    "Every projector has a number, a borrower and a due date. The caretaker counts once a term.")
ia_analogy.icon("cabinet", 60, 30, 2.0)
ia_analogy.box(220, 30, 520, 130, None, "paper")
for i, row in enumerate(["#07 projector · Ms. Vos · back Fri", "#12 laptop · Mr. Dam · back Mon", "#15 mic · drama club · term"]):
    ia_analogy.text(480, 66 + i * 34, row, size=16)
ia_analogy.note(480, 196, "count it against the sheet once a term", "pen", size=17)

ia_how = Doodle(760, 340, "Larder's asset list, started 9 April 2026. Four sections: devices (92 handhelds, 21 laptops, 3 routers, 6 label printers), each with a number, a store or person, and a status; subscriptions (46 SaaS tools, with owner, seats, price and renewal date); names and certificates (domains, TLS certificates, with renewal dates and the company card); and leases (the 4G router in Rotterdam). Renewal dates go into a shared calendar with a reminder 30 days before.",
                "Four lists in one file, with a renewal calendar. The domain moved to the company card on 10 April.")
for i, (t, s, f) in enumerate([("devices", "92 handhelds · 21 laptops · 3 routers · 6 printers", "blue"),
                               ("subscriptions", "46 SaaS · owner · seats · price · renewal", "y"),
                               ("names + certs", "domains · TLS · company card", "green"),
                               ("leases", "4G router · e-bike chargers", "paper")]):
    ia_how.box(14, 14 + i * 70, 470, 58, t, f, sub=s, size=16, subsize=13)
ia_how.icon("calendar", 560, 40, 1.6)
ia_how.box(520, 150, 226, 100, "renewals", "pink", sub="reminder 30 days before", size=17, subsize=13)
ia_how.note(380, 320, "9 leaver seats cancelled · €340 a month back", "green", size=17)

IT_ASSETS = dict(
    slug="it-assets",
    kicker="a.k.a. “IT asset management”",
    tldr="<b>IT asset management</b> means knowing what you own or pay for, where it is, who has it, what it costs and <b>when it renews or runs out</b>. Devices, licences, SaaS seats, domains and certificates all count. A single list with a renewal calendar stops the three classic surprises: <b>lost devices, paying for people who left, and things that quietly expire</b>.",
    chips=[("Family", "knowing what you run"), ("Lives in", "ops/assets.csv + a shared renewals calendar"), ("Pairs with", "joiners and leavers, service requests, the store IT kit")],
    itil=dict(groups=["service"], chain=["plan", "build", "deliver"], practices=["IT asset management"],
              sre="(SRE rarely names it; the cost of forgetting it is an outage)", principles=["Start where you are"],
              older="ITIL v3: service asset and configuration management (SACM)"),
    problem_side="Larder, 9 April 2026",
    problem="""  <p class="lead">Eli tries to count what Larder owns. There are <b>92 handhelds</b> on paper (31 at Noord, 31 at Zuid, 30 on their way to Rotterdam), but <b>4 at Zuid can't be found</b>. There are <b>46 SaaS subscriptions</b>, and 9 seats still belong to people who left: about <b>€340 a month</b>. Then the bad one: <span class="hl-pink">the domain larder.nl renews on 23 April on Jasper's personal card, and that card has expired.</span></p>
  <ul>
    <li>Nobody has one list; it's split across invoices, inboxes and the stores.</li>
    <li>Renewals happen, or don't, by surprise.</li>
    <li>Rotterdam adds 30 handhelds, a router and a dozen new seats in three weeks.</li>
  </ul>""",
    problem_figs=[ia_problem],
    analogy_side="the school's equipment cupboard",
    analogy="""  <p>A school's equipment cupboard has a <b>sign-out sheet</b>: each projector and laptop has a <b>number</b>, the name of whoever has it, and when it's due back. Once a term the caretaker <b>counts the cupboard against the sheet</b>. Nothing fancy, and nothing walks away unnoticed for long.</p>""",
    analogy_figs=[ia_analogy],
    map=[("Numbered projector", "Handheld ZU-17, laptop LT-09"),
         ("The borrower's name", "The store or the person who has it"),
         ("Due date", "Renewal date, warranty end, contract end"),
         ("Counting once a term", "A quarterly count per store with the store manager"),
         ("The cupboard", "Devices, SaaS seats, domains, certificates")],
    how_side="one file, four sections, a renewals calendar",
    how="""  <p>Eli makes one file with four sections. <b>Devices</b> each get a number, a location or person, a status and a purchase date. <b>Subscriptions</b> get an owner, seats, price and renewal date. <b>Names and certificates</b> covers domains and TLS certificates, with renewal dates and the card they're paid with. <b>Leases</b> covers things like the Rotterdam 4G router. Every renewal goes into a shared calendar with a reminder <b>30 days</b> before.</p>
  <p>First results. The domain moves to the company card on <b>10 April</b>. The 9 leaver seats are cancelled. Tomás finds 3 of Zuid's 4 missing handhelds in a drawer of broken ones, and the fourth is written off. Each store manager now counts devices with Eli once a quarter, using the asset numbers stuck on the back.</p>""",
    how_figs=[ia_how],
    steps=[("Collect every invoice and card statement", "SaaS hides in expense claims."),
           ("Number every device", "A sticker on the back, the same number in the file."),
           ("Write who has it", "A store or a person, never “somewhere”."),
           ("Add renewal and expiry dates", "Contracts, domains, certificates, warranties."),
           ("Put renewals in a shared calendar", "Reminder 30 days before, two names on each."),
           ("Count it every quarter", "With the store manager, against the file.")],
    vocab=[("IT asset", "Anything with value you own or pay for: device, licence, subscription, domain."),
           ("Asset register", "The list of assets with owner, location, status and dates."),
           ("Lifecycle", "Request → buy → use → repair → retire → dispose."),
           ("Renewal", "A date when something continues (and charges) or stops."),
           ("Shadow IT", "Tools bought by teams on their own, outside any list."),
           ("Write-off", "Removing a lost or broken asset from the register, on purpose.")],
    code=dict(file="ops/assets.csv", note="extract · 10 April 2026", plain=True, src="""
id      kind         where/who      status    bought      renews/ends   note
ZU-17   handheld     Zuid           ok        2024-11     warranty 2026-11
ZU-23   handheld     Zuid           lost      2024-11     —             written off 10 Apr
RT-01…  handheld ×30 Rotterdam      arriving  2026-04     warranty 2028-04
LT-09   laptop       Sam            ok        2025-02     —
RTR-RT  4G router    Rotterdam      lease     2026-04     monthly       C-04, €600
SAAS-12 helpdesk     owner Sam      14 seats  —           2026-09-01    3 seats freed
SAAS-31 rota tool    owner Joost    60 seats  —           2026-07-15
DOM-01  larder.nl    owner Eli      ok        —           2026-04-23    ✓ company card, 10 Apr
TLS-03  api cert     owner Eli      ok        —           2026-06-14    reminder 15 May
"""),
    tools="tools: a spreadsheet or CSV in the repo, a shared calendar, and stickers. Device management software (MDM) can fill the device list for you later.",
    ladder=[("invoices and memory", ["Renewals by surprise.", "Devices “somewhere”."]),
            ("one register and a calendar", ["Every asset numbered.", "Quarterly count with each store."]),
            ("filled automatically", ["MDM lists the handhelds.", "SaaS seats pulled from billing and sign-in logs."]),
            ("tied to people", ["Joining and leaving update the register.", "Unused seats flagged monthly."])],
    ladder_now=1,
    baseline="Each line compares <b>assets scattered across invoices and stores</b> to <b>one numbered register with a renewals calendar</b>.",
    ratings=[(2, 3, "The domain didn't lapse."),
             (2, 3, "Expiring certificates and contracts are seen in time."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "Anyone can see what exists and who has it."),
             (2, 3, "Quarterly counts replace searches."),
             (1, 4, "€340 a month back; one handheld written off honestly."),
             (2, 3, "The renewals calendar has two names, not one."),
             (3, 4, "A day to start, an hour a quarter.")],
    pitfalls=[("Forgetting SaaS", "Tools bought on a card never reach any list.", "go through card statements, not just invoices."),
              ("Renewals with one name", "That person is on holiday on the day.", "two names on every renewal."),
              ("Personal cards for company things", "The domain lapses when the person leaves.", "move everything to company accounts."),
              ("A register nobody counts", "It drifts from reality within months.", "count with each store every quarter.")],
    use=["You can't say how many devices you have.", "Something expired by surprise.", "Before a new site adds dozens of devices.", "Someone important has left."],
    skip=["A two-person company with five laptops: a note is enough.", "You already run MDM and a SaaS management tool: check them, don't duplicate them."],
    related=["<b>Forty New People on Monday</b> (next note)", "<b>How Does a New Store Get Its IT?</b> (this volume)", "<b>Cost Visibility (FinOps)</b> (cloud, vol. 6)"],
    quiz=[("What counts as an IT asset?", "Anything you own or pay for that affects IT: devices, licences, SaaS seats, domains, certificates, leases."),
          ("What three surprises does an asset register prevent?", "Lost devices, paying for people who left, and things that quietly expire."),
          ("Why put two names on every renewal?", "So it doesn't depend on one person being there on the day."),
          ("What was the most dangerous finding?", "The domain renewing on an ex-founder's expired personal card, two weeks away."),
          ("How often should you count devices, and with whom?", "Every quarter, with each store manager, against the register.")],
    quiz_sit=[("A store manager says “we've got about thirty handhelds”. Your register says 33. What do you do?", "Count them together, by asset number, and update the register. “About” is how the four at Zuid went missing.")],
    try_it="Go through the last three months of card statements and invoices and list every subscription. Add when each one renews and whose card pays. Which one would hurt most if it lapsed next week?",
    remember="If you can't say <span class=\"hl\">where it is and when it renews</span>, you don't own it. It just hasn't failed yet.",
    sources=["AXELOS, <i>ITIL 4: IT asset management</i> practice guide (2020).",
             "ISO/IEC 19770-1: IT asset management systems (overview).",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): chapters on fleet and asset management."],
)

# ------------------------------------------------------------------ 05 Forty New People on Monday
jl_problem = Doodle(760, 260, "Doodle of Monday 13 April 2026. Forty Rotterdam pickers, couriers and leads start training. Each needs a handheld login, a courier app account or a rota tool account, a store door code and email for leads. Eli sets each one up by hand: about 25 minutes per person, about 17 hours. While doing it, he finds that Jasper's admin account, eight months after he left, still works, and three couriers who left in March can still sign in to the courier app.",
                    "Seventeen hours of accounts by hand, and three ways in for people who'd already left.")
jl_problem.box(14, 30, 230, 90, "40 starters", "green", sub="Mon 13 April", size=20, subsize=15)
jl_problem.arrow(250, 75, 296, 75)
jl_problem.box(300, 30, 200, 90, "× 25 min", "y", sub="by hand", size=20, subsize=15)
jl_problem.arrow(506, 75, 552, 75)
jl_problem.box(556, 30, 190, 90, "≈ 17 hours", "pink", size=20)
jl_problem.box(14, 160, 732, 60, "still active: Jasper's admin (left Aug 2025) · 3 couriers (left March)", "pink", stroke="red", size=16)

jl_analogy = Doodle(760, 230, "Doodle of a hotel front desk. A new guest gets one key card programmed for their room, the gym and the breakfast room, from one screen, in two minutes. At checkout the card stops working automatically. Housekeeping doesn't need to change the locks.",
                    "A hotel key card: set up in two minutes from one screen, and it stops working at checkout.")
jl_analogy.icon("keycard", 60, 40, 1.8)
jl_analogy.row([("check-in", "room + gym + breakfast", "green"), ("stay", "card works", "blue"), ("checkout", "card stops by itself", "pink")], x=200, y=40, h=96, gap=40, size=17, subsize=13, arrows=True)
jl_analogy.note(470, 196, "one screen, one card, automatic end", "pen", size=18)

jl_how = Doodle(760, 360, "The joiners, movers and leavers process from 14 April 2026. Three lanes. Joiner: HR's hiring form names a role (picker, courier, store lead, office), the role decides which accounts and devices, Eli's checklist creates them from a group in under 6 minutes. Mover: a role change swaps the group. Leaver: the last working day removes every account on the same day, devices are returned to the store manager and checked off in the asset register. A monthly check compares active accounts with the staff list.",
                "Three lanes, driven by role. The role decides what you get; the last day decides when it stops.")
for r, (lane, steps, f) in enumerate([("joiner", ["hiring form", "role → group", "accounts + device", "day one"], "green"),
                                       ("mover", ["role change", "swap group", "old access gone"], "blue"),
                                       ("leaver", ["last day", "all accounts off", "device back", "register ✓"], "pink")]):
    y = 14 + r * 100
    jl_how.box(14, y, 110, 80, lane, f, size=17)
    n = len(steps)
    w = (600 - 14 * (n - 1)) / n
    for i, s in enumerate(steps):
        jl_how.box(round(140 + i * (w + 14)), y + 10, round(w), 60, s, "paper", size=14)
jl_how.note(380, 340, "monthly: active accounts vs the staff list", "pen", size=17)

JOINERS_LEAVERS = dict(
    slug="joiners-leavers",
    kicker="a.k.a. “joiners, movers, leavers”",
    tldr="Every new person needs accounts and devices on <b>day one</b>; every leaver must lose them on <b>their last day</b>. Joiners, movers and leavers (JML) is the process that does both from <b>one checklist driven by the person's role</b>: a picker gets the picker set, a store lead the lead set. It saves hours on every hiring wave, and it closes the doors that people forget to lock when someone leaves.",
    chips=[("Family", "knowing what you run"), ("Lives in", "ops/jml.md, with HR's hiring form and Joost's ops lead"), ("Pairs with", "IT assets, service requests, access reviews (vol. 5)")],
    itil=dict(groups=["service", "general"], chain=["engage", "deliver"], practices=["service request management", "information security management (access)"],
              sre="(toil, if done by hand)", principles=["Optimise and automate", "Collaborate and promote visibility"],
              older="ITIL v3: access management, request fulfilment"),
    problem_side="Larder, 13 April 2026",
    problem="""  <p class="lead">On Monday <b>13 April</b> forty Rotterdam pickers, couriers and leads start training. Each needs a handheld login, a courier or rota account, a door code, and email for the leads. Eli creates them by hand, at about <b>25 minutes a person</b>: roughly <b>17 hours</b>. On the way he finds that <span class="hl-pink">Jasper's admin account still works, eight months after he left</span>, and that three couriers who left in March can still sign in to the courier app.</p>
  <ul>
    <li>Starters wait, so training starts late.</li>
    <li>Each account is set up a little differently.</li>
    <li>Nobody tells IT when someone leaves, so access never ends.</li>
  </ul>""",
    problem_figs=[jl_problem],
    analogy_side="the hotel key card",
    analogy="""  <p>At a hotel desk a new guest gets <b>one key card</b>, programmed in two minutes from one screen for their room, the gym and the breakfast room. At checkout the card simply <b>stops working</b>. Nobody changes the locks, and nobody has to remember which doors that guest could open.</p>""",
    analogy_figs=[jl_analogy],
    map=[("Room type", "Role: picker, courier, store lead, office"),
         ("The key card's doors", "The accounts and devices that role gets"),
         ("Check-in at the desk", "HR's hiring form → Eli's checklist, day one"),
         ("Changing rooms", "A mover: picker becomes store lead"),
         ("Checkout: the card stops", "Last working day: all access removed the same day")],
    how_side="the role decides what you get; the last day decides when it stops",
    how="""  <p>Eli agrees three things with Yara and Joost's operations lead on <b>14 April</b>:</p>
  <ul>
    <li><b>Roles drive access.</b> Four role groups (picker, courier, store lead, office), each with a fixed list of accounts and devices. A new picker is added to the picker group and gets the whole set at once: <b>under 6 minutes</b>.</li>
    <li><b>One trigger in, one trigger out.</b> HR's hiring form, with role and start date, starts a joiner; the last working day, on the same form, ends every account on that day. Devices go back to the store manager and are ticked off in the asset register.</li>
    <li><b>A monthly check.</b> Active accounts are compared with the staff list. The first check, on <b>14 April</b>, closes Jasper's admin account, the three couriers' accounts and 6 others.</li>
  </ul>
  <p>The second Rotterdam wave (5 pickers and 12 couriers, later in the year) takes about 2 hours instead of 7.</p>""",
    how_figs=[jl_how],
    steps=[("Define a few roles", "Picker, courier, store lead, office: the access each needs."),
           ("Make each role a group", "Add a person to the group, not account by account."),
           ("Agree one trigger in, one out", "HR's hiring form, and the last working day."),
           ("Remove everything on the last day", "Same day, every account, then the device."),
           ("Handle movers on purpose", "A new role swaps the group; old access goes."),
           ("Check monthly against the staff list", "Anything active and not on the list is closed.")],
    vocab=[("Joiner", "A new person who needs access and devices."),
           ("Mover", "Someone changing role; they need new access, and to lose the old."),
           ("Leaver", "Someone leaving; all access must end on their last day."),
           ("Role-based access", "Access given by role (group), not person by person."),
           ("Least privilege", "Each role gets only what it needs to do the job."),
           ("Orphaned account", "An active account whose person has left.")],
    code=dict(file="ops/jml.md", note="from 14 April 2026 · agreed with Yara and Joost's ops lead", plain=True, src="""
# Joiners · movers · leavers

roles        picker        handheld PIN · rota app · door code
             courier       courier app · rota app · e-bike lock code
             store lead    + store email · helpdesk · stock screen
             office        email · laptop · tools on request

trigger in   HR hiring form (role, store, start date)  → Eli, 3 days before
trigger out  last working day on the same form          → removed that day
devices      back to the store manager · ticked in ops/assets.csv
movers       new role = swap group; nothing is "added on top"
monthly      active accounts vs staff list (first: 14 Apr → 9 closed,
             incl. Jasper's admin and 3 couriers who left in March)
"""),
    tools="tools: groups in your identity provider (or each tool's own role settings), HR's form, a monthly export. Automated provisioning (SCIM) can come later.",
    ladder=[("each account by hand", ["25 minutes a person.", "Leavers never removed."]),
            ("one checklist per role", ["Groups by role.", "Removal on the last day.", "Monthly check."]),
            ("scripted from the form", ["The hiring form creates the accounts.", "Leaving ends them."]),
            ("automatic from HR", ["The HR system drives every account.", "Unused access expires by itself."])],
    ladder_now=1,
    baseline="Each line compares <b>accounts made by hand and never removed</b> to <b>role groups, one trigger in and out, and a monthly check</b>.",
    ratings=[(2, 4, "Starters work on day one; leavers can't get back in."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Every account is the same by role."),
             (1, 4, "Who has access, and why, is on one page."),
             (1, 3, "25 minutes → 6 minutes a person."),
             (2, 3, "Seats freed as people leave."),
             (2, 3, "Store leads can see a starter is ready without asking Eli."),
             (3, 4, "A morning to set up.")],
    pitfalls=[("No leaver trigger", "IT never hears that someone left.", "the last day goes on the same HR form."),
              ("Access added on top for movers", "Over the years people collect every door.", "a new role swaps the group."),
              ("One-off exceptions", "“Just give her admin for a week” becomes permanent.", "exceptions get an end date."),
              ("Forgetting founders and contractors", "The riskiest accounts are the oldest.", "the monthly check covers everyone.")],
    use=["A hiring wave is coming (a new store, a peak).", "You've found an active account for someone who left.", "Starters wait days for access.", "Before a security questionnaire from a business client."],
    skip=["Five people who all need the same three tools: a shared checklist is enough."],
    related=["<b>What Do We Own, and Where Is It?</b> (this volume)", "<b>Can I Have a New Handheld?</b> (this volume)", "<b>Where Do They Come From?</b> (Sanne, vol. 4)", "<b>Least Privilege</b> (security, vol. 5)"],
    quiz=[("What are the three parts of JML?", "Joiners get access on day one, movers swap to their new role's access, leavers lose all access on their last day."),
          ("Why give access by role rather than by person?", "It's faster, consistent, and easy to check: the role says what you should have."),
          ("What must happen on a leaver's last day?", "Every account is removed that day and devices go back and are ticked off in the register."),
          ("What did the first monthly check find?", "Nine active accounts for people who had left, including Jasper's admin account."),
          ("What's the trap with movers?", "Adding the new access on top of the old, so people collect access over the years.")],
    quiz_sit=[("A courier leaves on Friday. On Monday his e-bike lock code still works. Where did the process break?", "The leaver trigger: either the last day wasn't on HR's form, or removal wasn't done that day. Fix the trigger, then check the other leavers from that week.")],
    try_it="Export the active accounts from your three most-used tools and compare them with your staff list. How many belong to people who have left? Then write the role groups that would have prevented it.",
    remember="Access starts with <span class=\"hl\">a role</span> and ends on <span class=\"hl\">the last day</span>. Anything else is a door left open.",
    sources=["AXELOS, <i>ITIL 4: Service request management</i> and <i>Information security management</i> practice guides (2020).",
             "NIST SP 800-53 Rev. 5: AC-2, account management.",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): onboarding and offboarding."],
)

NOTES = [WHAT_IS_IT_OPS, WHAT_WE_RUN, DEPENDENCY_MAP, IT_ASSETS, JOINERS_LEAVERS]
