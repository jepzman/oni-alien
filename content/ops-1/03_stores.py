# Series 2 · Book 5 · The IT Operations Notebook · Vol. 1 · Answering the stores.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 1".

# ------------------------------------------------------------------ 10 Where Do People Report Problems?
sd_problem = Doodle(760, 260, "Doodle of Eli's phone in April 2026: 146 messages from the stores in four weeks, by WhatsApp, text and calls. Noord sent 61, Zuid 52, Rotterdam 33 in its first week. They arrive at dinner, on Sundays and during meetings, and some are lost: two Zuid messages about a broken label printer were never answered.",
                    "146 messages to one phone in four weeks. Two were never answered.")
sd_problem.icon("phone", 50, 30, 1.8)
sd_problem.row([("Noord", "61", "y"), ("Zuid", "52", "y"), ("Rotterdam", "33 · week 1", "y")], x=160, y=30, h=90, w=180, gap=14, size=19, subsize=16)
sd_problem.box(160, 150, 568, 60, "2 Zuid messages about a label printer: never answered", "pink", stroke="red", size=16)
sd_problem.note(380, 242, "WhatsApp · texts · calls · at dinner", "pen", size=17)

sd_analogy = Doodle(760, 220, "Doodle of a block of flats with one caretaker's office and a logbook on the counter. Tenants write the problem in the book or phone the office; urgent leaks go to an emergency number. The caretaker works through the book in order and ticks each line. Before the book, tenants knocked on the caretaker's own front door at all hours.",
                    "One logbook at the caretaker's office, and an emergency number for leaks. Not his front door at 22:00.")
sd_analogy.icon("door", 70, 40, 1.5)
sd_analogy.box(160, 40, 260, 100, "caretaker's logbook", "green", sub="written · ticked", size=17, subsize=14)
sd_analogy.box(450, 40, 296, 100, "emergency number", "pink", sub="leaks, fires only", size=17, subsize=14)
sd_analogy.note(380, 190, "one front door for problems, not the caretaker's own", "pen", size=17)

sd_how = Doodle(760, 350, "Larder's service desk from Monday 11 May 2026. Stores and office staff report problems in one place: an 'IT and stores' queue in the helpdesk tool Sam's team already uses, reached by a QR code on the wall in each store or by email. Urgent problems that stop picking (no handhelds, no network) go to the on-call phone number, which forwards to the primary. Eli and the on-call primary work the queue in working hours. In June: 128 tickets, median first response 12 minutes in store hours, and 9 messages to Eli's personal phone.",
                "One queue, one urgent number. In June: 128 tickets, 12-minute first response, 9 stray messages.")
sd_how.box(14, 14, 220, 110, "stores + office", "green", sub="QR code · email", size=17, subsize=14)
sd_how.arrow(240, 69, 290, 69)
sd_how.box(296, 14, 230, 110, "IT & stores queue", "blue", sub="in Sam's helpdesk", size=17, subsize=14)
sd_how.arrow(532, 69, 580, 69)
sd_how.box(586, 14, 160, 110, "Eli + on-call", "paper", sub="working hours", size=16, subsize=14)
sd_how.box(14, 152, 512, 72, "picking stopped? call the on-call number", "pink", sub="forwards to the primary · 07:00–23:00", size=16, subsize=13)
sd_how.row([("128", "tickets in June", "y"), ("12 min", "first response", "y"), ("9", "to Eli's phone", "green")], x=14, y=250, h=80, w=232, gap=18, size=22, subsize=14)

SERVICE_DESK = dict(
    slug="service-desk",
    kicker="a.k.a. “the single point of contact”",
    tldr="A <b>service desk</b> is the one front door for “something's wrong” and “I need something”. It's a queue where every report is written down, gets an owner and an answer, plus <b>one urgent number</b> for things that stop the work. It replaces messages to one engineer's phone. Even a two-person team needs it: it's what makes the work <b>visible, countable and shareable</b>.",
    chips=[("Family", "answering the stores"), ("Lives in", "the helpdesk tool (an “IT &amp; stores” queue), posters in every store"), ("Pairs with", "service requests, known errors (vol. 2), tiers and swarming (vol. 2)")],
    itil=dict(groups=["service"], chain=["engage", "deliver"], practices=["service desk"],
              sre="(interrupts: SRE routes them to one person per shift)", principles=["Collaborate and promote visibility", "Focus on value"],
              older="ITIL v3: the service desk function, single point of contact"),
    problem_side="Larder, April 2026",
    problem="""  <p class="lead">In April 2026 Eli counts the messages from the stores to his own phone: <b>146 in four weeks</b>, by WhatsApp, text and calls. Noord sent 61, Zuid 52 and Rotterdam 33 in its first week. They arrive at dinner, on Sundays and in meetings. <span class="hl-pink">Two messages from Zuid about a broken label printer were never answered</span>; Tomás thought Eli was ignoring him.</p>
  <ul>
    <li>Nothing is written down, so nothing can be counted or handed over.</li>
    <li>The on-call rota doesn't help: the stores still message Eli.</li>
    <li>Urgent and trivial arrive the same way.</li>
  </ul>""",
    problem_figs=[sd_problem],
    analogy_side="the caretaker's logbook",
    analogy="""  <p>Before the logbook, the tenants of a block of flats knocked on the <b>caretaker's own front door</b>, at all hours. Now there's <b>a logbook at his office</b>: write the problem down, and he works through it in order and ticks each line. For leaks and fires there's <b>one emergency number</b>. Same caretaker, same work, but nothing is forgotten, and he gets his evenings back.</p>""",
    analogy_figs=[sd_analogy],
    map=[("The caretaker's front door", "Eli's personal phone"),
         ("The logbook at the office", "The “IT &amp; stores” queue in Sam's helpdesk"),
         ("Ticked lines", "Tickets with an owner and a status"),
         ("The emergency number", "The on-call number, for when picking stops"),
         ("Tenants", "Store managers, pickers, office staff")],
    how_side="one queue, one urgent number, and a poster",
    how="""  <p>Sam's team already uses a helpdesk tool for customers. On <b>11 May</b> Sam adds an <b>“IT &amp; stores” queue</b> to it. Stores reach it by scanning a <b>QR code on a poster</b> by each store's packing bench, or by email. The form asks four things: store, what's wrong, since when, and how many people are stuck.</p>
  <p>For anything that <b>stops picking or dispatch</b> (no handhelds, no network, no labels at the Friday peak) there's one <b>on-call number</b>. It forwards to whoever is primary that week. Eli and the primary work the queue in working hours, and the queue is part of the Monday handover. Eli's rule for himself is just as important: a store message to his own phone gets a polite reply with the QR code, <b>even when he could fix it in a minute</b>.</p>
  <p>In June there are <b>128 tickets</b>, a <b>12-minute median first response</b> in store hours, and <b>9 messages</b> to Eli's phone.</p>""",
    how_figs=[sd_how],
    steps=[("Pick one place for reports", "Reuse a tool people already have if you can."),
           ("Make it easy to reach", "A QR code where the problem happens."),
           ("Ask only what you need", "Where, what, since when, how many people stuck."),
           ("Add one urgent route", "A number that forwards to on-call, for “work has stopped”."),
           ("Redirect kindly, every time", "Personal messages get the link, even for easy fixes."),
           ("Count and review", "Tickets per store, first response, top causes.")],
    vocab=[("Service desk", "The single point of contact between IT and the people it serves."),
           ("Ticket", "One written report or request, with an owner and a status."),
           ("Queue", "Where tickets wait to be picked up."),
           ("First response time", "How long until a person answers the ticket."),
           ("Interrupt", "Unplanned work that arrives while you're doing something else."),
           ("Shadow support", "Help given off the record, through personal channels.")],
    code=dict(file="stores/poster-it-help.md", note="on the wall by every packing bench · from 11 May 2026", plain=True, src="""
  ┌─────────────────────────────────────────────┐
  │  SOMETHING NOT WORKING?                     │
  │                                             │
  │  [ QR ]  scan → "IT & stores" form          │
  │          or email it@larder…                │
  │          answer within 30 min, 07:00–23:00  │
  │                                             │
  │  PICKING OR DISPATCH STOPPED?               │
  │  call on-call:  +31 20 …  (24/7)            │
  │                                             │
  │  tell us: store · what · since when ·       │
  │           how many people are stuck         │
  └─────────────────────────────────────────────┘
"""),
    tools="tools: the helpdesk tool your support team already has, a QR code and a laminator.",
    ladder=[("personal phones", ["Messages lost.", "Nothing counted."]),
            ("one queue and an urgent number", ["Every report written down.", "First response measured."]),
            ("routed and enriched", ["Store, device and service filled in automatically.", "Known errors suggested to the desk."]),
            ("self-service first", ["Common fixes done by the stores themselves (vol. 4).", "The desk handles the new."])],
    ladder_now=1,
    baseline="Each line compares <b>messages to one engineer's phone</b> to <b>one queue with an urgent number and a poster</b>.",
    ratings=[(2, 4, "Nothing is lost; stores get an answer."),
             (3, 3, "Neutral on its own."),
             (2, 3, "Urgent problems reach on-call directly."),
             (3, 3, "Neutral."),
             (1, 4, "Every problem is counted, by store and cause."),
             (2, 3, "Repeat causes become visible (next notes)."),
             (3, 3, "No new tool."),
             (1, 4, "Eli gets his evenings back."),
             (3, 3, "A day to set up; discipline to keep.")],
    pitfalls=[("“Just this once” on WhatsApp", "Every exception teaches the store to message you again.", "reply with the link, kindly, every time."),
              ("A long form", "People don't fill it in, and message you instead.", "four questions, from a phone."),
              ("No urgent route", "Stopped picking waits in a queue.", "one number that forwards to on-call."),
              ("A queue nobody owns", "Tickets wait for days.", "it's part of on-call and of the Monday handover.")],
    use=["Problems arrive in personal chats.", "You can't say how many problems the stores had last month.", "Before sharing on-call.", "A new site is opening."],
    skip=["One small team in one room: a shared channel may be enough, as long as it's written."],
    related=["<b>Can I Have a New Handheld?</b> (next note)", "<b>Who Fixes What?</b> (vol. 2)", "<b>Feedback Loops with Operations</b> (Grace, vol. 4)"],
    quiz=[("What is a service desk for?", "One front door where every problem and request is written down, owned and answered."),
          ("Why does Eli reply to personal messages with the QR code, even for easy fixes?", "Each exception teaches the store to message him again; written tickets can be counted and shared."),
          ("What are the four questions on Larder's form?", "Which store, what's wrong, since when, how many people are stuck."),
          ("What goes to the on-call number instead of the queue?", "Anything that stops picking or dispatch."),
          ("What changed between April and June?", "146 personal messages in four weeks → 128 tickets with a 12-minute first response, and 9 personal messages.")],
    quiz_sit=[("Yara phones Eli directly on a Sunday because a label printer is down. Picking still works. What does Eli do?", "Thanks her, asks her to log it with the QR code so it's tracked, and if it doesn't stop picking it waits for Monday's queue. If it does, the on-call number is the route, not Eli's phone.")],
    try_it="For one week, write down every request for help you get, by whatever channel. Where did they come from? Which ones stopped someone's work? Use that to design one queue and one urgent route.",
    remember="Help that arrives through <span class=\"hl\">a personal phone</span> can't be counted, shared or handed over. Give people <span class=\"hl\">one front door</span>.",
    sources=["AXELOS, <i>ITIL 4: Service desk</i> practice guide (2020).",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): the helpdesk.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 29, dealing with interrupts."],
)

# ------------------------------------------------------------------ 11 Can I Have a New Handheld?
sr_problem = Doodle(760, 250, "Doodle of the first four weeks of the IT and stores queue, May to early June 2026: 74 tickets. Sorted, 46 of them are the same six requests every time: PIN resets, a broken handheld, a label printer that won't print, a new laptop, access to a tool, a new starter. Each one is handled differently, depending on who picks it up, and the store doesn't know how long it'll take.",
                    "46 of 74 tickets are the same six requests, each handled a different way.")
sr_problem.row([("PIN reset", "23", "y"), ("broken handheld", "9", "y"), ("label printer", "6", "y")], x=14, y=24, h=78, w=232, gap=18, size=17, subsize=16)
sr_problem.row([("new laptop", "3", "y"), ("tool access", "3", "y"), ("new starter", "2", "y")], x=14, y=118, h=78, w=232, gap=18, size=17, subsize=16)
sr_problem.note(380, 232, "same six, every week · “how long will it take?” “depends”", "red", size=17)

sr_analogy = Doodle(760, 220, "Doodle of a coffee bar's menu board: six standard drinks, each with a price and a waiting time, made the same way every time. Anything special, like a custom order, you ask the barista and it may take longer. The menu makes the common things fast and predictable.",
                    "Six drinks on the board, each the same every time, with a price and a wait. Special orders: ask.")
sr_analogy.icon("cup", 60, 40, 1.6)
sr_analogy.box(160, 30, 586, 130, None, "paper")
for i, t in enumerate(["flat white · 3 min", "espresso · 1 min", "tea · 2 min"]):
    sr_analogy.text(330, 66 + i * 34, t, size=17)
for i, t in enumerate(["latte · 3 min", "cocoa · 3 min", "something else? ask"]):
    sr_analogy.text(590, 66 + i * 34, t, size=17)
sr_analogy.note(450, 196, "common = fast and the same; unusual = a conversation", "pen", size=17)

sr_how = Doodle(760, 350, "Larder's six standard requests from 1 June 2026, each with a short form, an owner, steps and a promised time. PIN reset: the store lead resets it in the device tool, 5 minutes. Broken handheld: swap from the store's spare pool of 3, then Eli repairs or replaces, same shift. Label printer: a known-error check then a swap, 1 hour. New laptop: Eli, 3 working days. Tool access: the tool's owner approves, 1 working day. New starter: the joiners checklist, ready on day one if requested 3 days before.",
                "Six standard requests, each with a form, an owner and a promised time.")
items = [("PIN reset", "store lead · 5 min"), ("broken handheld", "spare pool · same shift"), ("label printer", "check + swap · 1 h"),
         ("new laptop", "Eli · 3 days"), ("tool access", "tool owner · 1 day"), ("new starter", "JML · day one")]
for i, (t, s) in enumerate(items):
    r, c = divmod(i, 3)
    sr_how.box(14 + c * 248, 14 + r * 106, 236, 90, t, "green", sub=s, size=17, subsize=14)
sr_how.box(110, 246, 540, 70, "spare pool: 3 handhelds per store, kept by the store lead", "y", size=16)

SERVICE_REQUESTS = dict(
    slug="service-requests",
    kicker="a.k.a. “service request management”",
    tldr="Most of what reaches a service desk isn't broken; it's <b>a standard request</b>: a PIN reset, a new device, access to a tool. Give each common request <b>a short form, an owner, fixed steps and a promised time</b>, and push the simplest ones to the people closest to them (a store lead can reset a PIN). The common becomes fast and predictable, which leaves time for the unusual.",
    chips=[("Family", "answering the stores"), ("Lives in", "the helpdesk's request forms, ops/requests.md"), ("Pairs with", "the service desk, joiners and leavers, IT assets")],
    itil=dict(groups=["service"], chain=["engage", "deliver"], practices=["service request management"],
              sre="(toil: standard requests by hand are the classic example)", principles=["Optimise and automate", "Keep it simple and practical"],
              older="ITIL v3: request fulfilment"),
    problem_side="Larder, early June 2026",
    problem="""  <p class="lead">The new queue has <b>74 tickets</b> after four weeks. Eli sorts them. <b>46</b> are the same six requests every time: PIN resets (23), broken handhelds (9), label printers (6), new laptops, tool access and new starters. Each is handled differently depending on who picks it up, and a store asking “how long?” gets “depends”. <span class="hl-pink">The queue has made the work visible. It hasn't made it any faster.</span></p>
  <ul>
    <li>A picker with a locked handheld waits for IT to unlock it.</li>
    <li>A broken handheld is picked up when someone has time.</li>
    <li>Repeat work fills the queue, so new problems wait behind it.</li>
  </ul>""",
    problem_figs=[sr_problem],
    analogy_side="the coffee bar's menu board",
    analogy="""  <p>A coffee bar's <b>menu board</b> lists six standard drinks, each made the same way every time, with a price and roughly how long it takes. Order a flat white and you know what you'll get, and when. <b>Something special?</b> Ask the barista, and it may take longer. The board makes the common things fast, and frees the barista for the special orders.</p>""",
    analogy_figs=[sr_analogy],
    map=[("A drink on the board", "A standard request: PIN reset, new laptop"),
         ("Made the same way every time", "Fixed steps in ops/requests.md"),
         ("Price and wait", "Owner and promised time"),
         ("The barista's free hands", "Time for the problems that are new"),
         ("Something special? ask", "Anything else is a normal ticket")],
    how_side="six standard requests, and push the simplest to the store",
    how="""  <p>From <b>1 June</b> the queue offers six request types, each with its own two-line form, an owner, steps and a promised time:</p>
  <ul>
    <li><b>PIN reset</b>: done by the <b>store lead</b> in the device tool. 5 minutes, no ticket needed. Tomás and Yara learn it on 29 May.</li>
    <li><b>Broken handheld</b>: swapped from the store's <b>spare pool of 3</b>, kept by the store lead. The broken one goes into the queue for Eli to repair or replace. Picking loses one shift at most.</li>
    <li><b>Label printer</b>: check the known fixes first, then swap. 1 hour.</li>
    <li><b>New laptop</b> (3 working days), <b>tool access</b> (approved by the tool's owner, 1 working day), <b>new starter</b> (the joiners checklist, ready on day one if asked 3 days before).</li>
  </ul>
  <p>Six weeks later, PIN resets have left the queue entirely, and the median time to close a request is <b>4 hours</b>, down from 2 days.</p>""",
    how_figs=[sr_how],
    steps=[("Sort a month of tickets", "Find the requests that repeat."),
           ("Pick the top five or six", "Not every request needs a form."),
           ("Write steps, owner and promised time", "One short page each."),
           ("Push the simplest to the front line", "Store leads reset PINs."),
           ("Keep spares where the work is", "Swap first, repair later."),
           ("Measure time to close per request", "And move the next one down the ladder.")],
    vocab=[("Service request", "A request for something normal: information, access, a device, a reset."),
           ("Incident", "Something that's broken or degraded. Not the same thing."),
           ("Request catalogue", "The list of standard requests people can make."),
           ("Fulfilment", "Doing the request: the steps behind the form."),
           ("Approval", "A yes from whoever owns the thing being asked for."),
           ("Spare pool", "Ready-to-use devices kept where the work happens.")],
    code=dict(file="ops/requests.md", note="the six standard requests · from 1 June 2026", plain=True, src="""
request          who does it        approval        promised             form asks
PIN reset        store lead         —               5 min, no ticket     —
broken handheld  store lead swaps;  —               same shift           device no., what happened
                 Eli repairs
label printer    desk: KE check,    —               1 hour               store, printer no.
                 then swap
new laptop       Eli                manager         3 working days       who, start date
tool access      tool owner         tool owner      1 working day        tool, why
new starter      Eli (JML)          HR form         day one (3 days'     role, store, start date
                                                    notice)
anything else    → normal ticket
"""),
    tools="tools: request forms in the helpdesk tool, the device management tool for PIN resets, a shelf for the spare pool.",
    ladder=[("each request a favour", ["Handled differently by each person.", "“Depends.”"]),
            ("standard requests with times", ["Forms, owners, promised times.", "Simple ones done by the stores."]),
            ("scripted fulfilment", ["Access granted from the approval.", "Laptops pre-built."]),
            ("self-service", ["People ask and get it in one step.", "The desk sees only exceptions."])],
    ladder_now=1,
    baseline="Each line compares <b>every request handled as a one-off</b> to <b>six standard requests with owners, times and a spare pool</b>.",
    ratings=[(2, 4, "Pickers lose minutes, not shifts."),
             (3, 3, "Neutral."),
             (2, 4, "Swap first, repair later."),
             (3, 3, "Neutral."),
             (2, 4, "Stores know what to expect and when."),
             (2, 4, "PIN resets leave the queue."),
             (3, 3, "Nine spare handhelds, bought once."),
             (3, 4, "Fewer interruptions for on-call."),
             (3, 4, "Six short pages.")],
    pitfalls=[("A form for everything", "Forty request types nobody can choose between.", "the top five or six; the rest are normal tickets."),
              ("Approval theatre", "A manager approves PIN resets.", "approve only what costs money or grants access."),
              ("No spares", "Every broken device waits for a repair.", "keep a pool where the work happens."),
              ("Treating requests as incidents", "Urgent flags on laptops; real outages wait.", "separate the two in the queue.")],
    use=["The same requests fill the queue every week.", "People ask “how long?” and get “it depends”.", "Front-line staff wait for IT for simple things.", "Before a hiring wave."],
    skip=["Requests are rare and all different: keep them as normal tickets."],
    related=["<b>Where Do People Report Problems?</b> (this volume)", "<b>Forty New People on Monday</b> (this volume)", "<b>What Can the Stores Fix Themselves?</b> (vol. 4)"],
    quiz=[("What's the difference between a service request and an incident?", "A request asks for something normal (a reset, a device, access); an incident is something broken."),
          ("What does a standard request need?", "A short form, an owner, fixed steps and a promised time."),
          ("Why do store leads reset PINs?", "It's simple, safe and urgent for the picker; making them wait for IT wastes a shift."),
          ("What is the spare pool for?", "Swap a broken handheld at once, so picking continues, and repair the broken one later."),
          ("Which requests need approval?", "Those that cost money or grant access, and the approval comes from whoever owns the thing.")],
    quiz_sit=[("Rotterdam's spare pool is empty on a Friday afternoon and two handhelds break. What should happen now, and on Monday?", "Now: borrow from Noord or Zuid, or move pickers to shared devices for the peak. Monday: refill the pool, and check whether three spares is enough for a 30-device store.")],
    try_it="Sort the last month of your requests. Which five repeat most? For each, write who does it, whether it needs approval, and a promised time. Which one could the requester do themselves?",
    remember="Make the <span class=\"hl\">common requests boring</span>: same steps, same time, done by whoever is closest. Save the thinking for the new ones.",
    sources=["AXELOS, <i>ITIL 4: Service request management</i> practice guide (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 5, eliminating toil.",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): workstation fleet logistics."],
)

# ------------------------------------------------------------------ 12 Is It the Network?
nw_problem = Doodle(760, 260, "Doodle of Noord in April 2026: 23 tickets saying 'picker app offline'. Pickers say it happens near the freezers. The store has two Wi-Fi access points for 31 handhelds, both at the front. The usual answer has been 'restart the handheld'. Meanwhile Rotterdam has run on a 4G router since opening, and its new internet line arrives on 13 May, but nobody has ever tested what happens when the line fails.",
                    "23 “app offline” tickets at Noord, mostly by the freezers. Rotterdam's failover never tested.")
nw_problem.box(14, 20, 470, 160, None, "paper")
nw_problem.head(249, 46, "Noord", size=18)
nw_problem.box(40, 64, 70, 40, "AP", "blue", size=15)
nw_problem.box(130, 64, 70, 40, "AP", "blue", size=15)
nw_problem.box(330, 64, 136, 96, "freezers", "pink", sub="“offline”", size=16, subsize=14)
nw_problem.note(140, 150, "front of store", "pen", size=15)
nw_problem.box(510, 20, 236, 160, "Rotterdam", "y", sub="4G now · line 13 May · failover never tested", size=17, subsize=12)
nw_problem.note(380, 226, "23 tickets: “restart the handheld”", "red", size=18)

nw_analogy = Doodle(760, 220, "Doodle of a house with poor phone signal in the back bedroom. The family keeps restarting their phones. A friend walks around with a signal meter, finds the dead spot behind the thick wall, and adds a small repeater. The family also checks once that the landline works when the power is out.",
                    "Stop restarting the phone: walk the house with a meter, find the dead spot, fix the coverage.")
nw_analogy.icon("tower", 80, 40, 1.4)
nw_analogy.row([("restart phone", "again", "pink"), ("walk with a meter", "find the spot", "y"), ("repeater", "fixed", "green")], x=180, y=40, h=96, w=170, gap=40, size=16, subsize=14, arrows=True)
nw_analogy.note(450, 190, "measure before you blame", "pen", size=18)

nw_how = Doodle(760, 380, "Eli's store network sheet, May 2026. For each store: the internet line, the 4G backup router, the access points and where they are, and the VPN to the cloud. At Noord, a Wi-Fi survey on Thursday 14 May found the freezer aisle and cold room at minus 82 dBm, too weak. Two more access points were installed on 21 May for 900 euros; 'offline' tickets at Noord fell from 23 in April to 2 in June. At Rotterdam, the line went live on 13 May; on Tuesday 19 May at 15:00 Eli unplugged it and the 4G router took over in 40 seconds. The test is repeated on the first Tuesday of each month.",
                "One sheet per store; measure the Wi-Fi; pull the plug on purpose, monthly.")
nw_how.box(14, 14, 360, 170, None, "paper")
nw_how.head(194, 40, "Noord · 14 May survey", size=17)
nw_how.text(194, 76, "freezer aisle: −82 dBm", size=16)
nw_how.text(194, 104, "+2 access points · €900 · 21 May", size=15)
nw_how.box(40, 122, 300, 50, "“offline”: 23 (Apr) → 2 (Jun)", "green", size=15)
nw_how.box(386, 14, 360, 170, None, "paper")
nw_how.head(566, 40, "Rotterdam · line + 4G", size=17)
nw_how.text(566, 76, "line live 13 May", size=16)
nw_how.text(566, 104, "Tue 19 May 15:00: pull the line", size=15)
nw_how.box(412, 122, 308, 50, "4G took over in 40 s ✓", "green", size=15)
nw_how.row([("line", None, "blue"), ("4G backup", None, "y"), ("access points", None, "blue"), ("VPN to cloud", None, "blue")], x=14, y=214, h=56, gap=12, size=16)
nw_how.note(380, 310, "first Tuesday of every month: pull the plug, write down the seconds", "pen", size=17)
nw_how.note(380, 350, "offline-first picker app = minutes of grace, not hours", "red", size=16)

STORE_NETWORK = dict(
    slug="store-network",
    kicker="a.k.a. “infrastructure management, at the edge”",
    tldr="A store's work depends on its <b>network</b>: Wi-Fi for the handhelds, an internet line, a backup and a secure link to the cloud. Treat it as a service. Keep <b>one sheet per store</b> (line, backup, access points, VPN), <b>measure</b> the Wi-Fi where people actually work before blaming it or the devices, and <b>test the failover on purpose</b> every month. A backup you've never tried is a hope, not a backup.",
    chips=[("Family", "answering the stores"), ("Lives in", "ops/stores/&lt;store&gt;-network.md, plus a monthly test in the calendar"), ("Pairs with", "monitoring (store heartbeat), the store IT kit, continuity (vol. 5)")],
    itil=dict(groups=["technical", "service"], chain=["build", "deliver"], practices=["infrastructure and platform management", "availability management"],
              sre="“hope is not a strategy”: test the failover", principles=["Start where you are"],
              older="ITIL v3: technical management, network management"),
    problem_side="Larder, May 2026",
    problem="""  <p class="lead">Noord has logged <b>23 tickets</b> since April saying “picker app offline”. The pickers say it happens near the freezers. The answer every time has been “restart the handheld”. Noord has <b>two access points for 31 handhelds</b>, both at the front of the store. Meanwhile Rotterdam has run on a 4G router since opening, its internet line goes live on <b>13 May</b>, and <span class="hl-pink">nobody has ever tested what happens when that line fails</span>.</p>
  <ul>
    <li>Devices get blamed for network gaps, and the gaps stay.</li>
    <li>The offline-first picker app hides short drops, and so does a long ticket history.</li>
    <li>A backup that has never been tried may not work at the Friday peak.</li>
  </ul>""",
    problem_figs=[nw_problem],
    meanwhile=[("project-2", "issue-log", "Sanne's issue log: I-07, Rotterdam's internet line, raised by Eli on 20 March, ordered 30 March, live 13 May; the store opened on a 4G router with a backup SIM (€600).",
                "Eli's store network sheet takes over where the issue closes: the line live, the 4G kept as backup, and the failover tested on purpose on 19 May and every month after.")],
    analogy_side="the dead spot in the back bedroom",
    analogy="""  <p>A family has no phone signal in the back bedroom and keeps <b>restarting their phones</b>. A friend walks the house with <b>a signal meter</b>, finds the dead spot behind a thick wall, and adds a small repeater. While she's there, she makes them check once that <b>the landline still works when the power is out</b>. Measure before you blame, and test the backup before you need it.</p>""",
    analogy_figs=[nw_analogy],
    map=[("Restarting the phone", "“Restart the handheld”"),
         ("Walking the house with a meter", "A Wi-Fi survey of the store floor"),
         ("The thick wall", "Freezers and the cold room"),
         ("The repeater", "Two more access points at the back"),
         ("Checking the landline in a power cut", "Pulling Rotterdam's line to test the 4G failover")],
    how_side="a sheet per store, a survey, and a monthly pulled plug",
    how="""  <p>Eli writes <b>one network sheet per store</b>: the internet line (provider, contract, support number), the <b>4G backup</b>, each <b>access point</b> and where it is, and the <b>VPN</b> to the cloud.</p>
  <p>At <b>Noord</b> on Thursday <b>14 May</b> he walks the floor with a Wi-Fi survey app. The freezer aisle and the cold-room door read <b>−82 dBm</b>, too weak for a handheld to hold on. Two more access points go in on <b>21 May</b> (€900), and “offline” tickets at Noord drop from <b>23 in April to 2 in June</b>. Zuid's survey finds no gaps.</p>
  <p>At <b>Rotterdam</b> the line goes live on 13 May, and the 4G router stays as backup. On Tuesday <b>19 May at 15:00</b>, with Yara watching, Eli pulls the line: the router switches to 4G in <b>40 seconds</b>, the picker app doesn't notice, and the store heartbeat stays green. The test goes in the calendar for the <b>first Tuesday of every month</b>, at a quiet hour, with the seconds written down. Noord and Zuid get 4G backup routers in June.</p>""",
    how_figs=[nw_how],
    steps=[("Write one network sheet per store", "Line, backup, access points, VPN, support numbers."),
           ("Count the “offline” tickets by place", "Where in the store, not just which store."),
           ("Measure before blaming", "Walk the floor with a survey app."),
           ("Fix the coverage, not the device", "Access points where the work is."),
           ("Give every store a backup link", "And alert when it's in use."),
           ("Pull the plug on purpose, monthly", "Quiet hour, someone watching, seconds written down.")],
    vocab=[("Access point (AP)", "The box that provides Wi-Fi to devices nearby."),
           ("dBm", "Signal strength. Around −65 is good; below −80 is too weak to work reliably."),
           ("Wi-Fi survey", "Measuring signal across a site, where people actually work."),
           ("Failover", "Switching to the backup when the main link fails."),
           ("4G backup", "A mobile-data router that takes over if the line fails."),
           ("VPN", "An encrypted tunnel from the store to Larder's cloud network.")],
    code=dict(file="ops/stores/rotterdam-network.md", note="store network sheet · failover tested Tue 19 May 2026", plain=True, src="""
# Rotterdam · store network

line        fibre, 500/500 · live 13 May · support 24/7 +31 …  · contract to 2029
backup      4G router (RTR-RT, leased, C-04) · 2 SIMs, two networks
            alert "store on 4G" → ticket (not a page)
Wi-Fi       4 access points: front · aisles A–D · chilled · packing bench
            survey 12 May: worst −67 dBm (chilled)
VPN         store → EU region · if down: picker app offline mode (≈ 2 h of work)

failover tests (first Tuesday, 15:00, with the store lead)
  19 May   line pulled → 4G in 40 s · app OK · heartbeat green   (Eli, Yara)
  02 Jun   38 s · OK
"""),
    tools="tools: a Wi-Fi survey app on a phone, the router's admin page, a calendar reminder and a store lead willing to watch.",
    ladder=[("restart and hope", ["Tickets closed with “restarted”.", "Backup never tested."]),
            ("a sheet per store, measured and tested", ["Surveys, a 4G backup, monthly failover.", "“Store on 4G” is visible."]),
            ("managed network", ["Access points and routers managed centrally.", "Coverage problems flagged by the devices."]),
            ("tested automatically", ["Failover tested by script at a quiet hour.", "Results tracked over time."])],
    ladder_now=1,
    baseline="Each line compares <b>restarting handhelds and hoping the backup works</b> to <b>a measured network sheet per store and a monthly failover test</b>.",
    ratings=[(2, 4, "Pickers by the freezers stay online."),
             (2, 4, "Coverage gaps fixed; backup proven."),
             (2, 3, "A line failure costs 40 seconds."),
             (3, 3, "Neutral."),
             (1, 4, "Each store's network is on one page."),
             (2, 4, "23 tickets → 2."),
             (3, 4, "€900 against weeks of lost minutes."),
             (2, 3, "Fewer “is it the network?” calls."),
             (3, 3, "An hour a month per store.")],
    pitfalls=[("Blaming the device", "Restarting handhelds hides a coverage gap for months.", "count tickets by place and measure."),
              ("Untested backup", "The 4G SIM expired months ago.", "pull the plug monthly and write down the seconds."),
              ("Testing at the peak", "A failover test becomes an incident.", "quiet hour, store lead watching."),
              ("Surveying the empty store", "Freezers full of stock block more signal.", "survey during a normal working day.")],
    use=["“Offline” tickets cluster in one store or one place.", "A store depends on one line.", "Before a new store opens.", "Nobody remembers the last failover test."],
    skip=["The store's work doesn't depend on the network (it does at Larder)."],
    related=["<b>How Does a New Store Get Its IT?</b> (next note)", "<b>How Do We Know It's Broken?</b> (this volume)", "<b>What's in the Way Right Now?</b> (Sanne, vol. 2)", "<b>Offline-First</b> (frontend, vol. 2)"],
    quiz=[("Why did Noord's “restart the handheld” fix keep failing?", "The problem was Wi-Fi coverage near the freezers, not the devices."),
          ("Roughly what signal is too weak for a handheld?", "Below about −80 dBm."),
          ("How did Eli test Rotterdam's backup?", "He pulled the line at a quiet hour with Yara watching: the 4G took over in 40 seconds."),
          ("Why test the failover monthly?", "Backups fail silently: expired SIMs, changed settings. A monthly test finds that before a peak does."),
          ("What should “store on 4G” trigger?", "A ticket, so someone checks the line, not a page: the store is still working.")],
    quiz_sit=[("Zuid reports “app offline” three times in one evening, all at the packing bench. Zuid's survey found no gaps in May. What do you do?", "Check the store heartbeat and the router first (is the line down, are they on 4G?), then survey again at the bench: a new freezer or racking can block signal. Don't close it as “restarted”.")],
    try_it="Pick one site that depends on a network. Write its sheet: line, backup, access points, link to your systems. When was the backup last tested? Schedule a pulled-plug test at a quiet hour.",
    remember="<span class=\"hl\">Measure before you blame</span> the devices, and <span class=\"hl\">pull the plug on purpose</span> before the line pulls it for you.",
    sources=["AXELOS, <i>ITIL 4: Infrastructure and platform management</i> and <i>Availability management</i> practice guides (2020).",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 1, “hope is not a strategy”.",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): network infrastructure."],
)

# ------------------------------------------------------------------ 13 How Does a New Store Get Its IT?
sk_problem = Doodle(760, 260, "Doodle of the Rotterdam launch as seen from IT: the internet line was raised as an issue on 20 March, ordered on 30 March with a six-week lead time, and arrived on 13 May, three weeks after opening. Thirty handhelds were set up by hand, about 20 minutes each, over two evenings. Accounts for 40 starters by hand. Sanne's lessons-learned session on 18 May puts it at the top: store IT is an eighth workstream.",
                    "Rotterdam's IT, from the IT side: the line three weeks late, 30 handhelds by hand, 40 accounts by hand.")
sk_problem.row([("line ordered 30 Mar", "lead time 6 weeks", "y"), ("opening 27 Apr", "on 4G", "pink"), ("line live 13 May", "+16 days", "y")], x=14, y=30, h=84, gap=40, size=16, subsize=14, arrows=True)
sk_problem.row([("30 handhelds", "20 min each, by hand", "paper"), ("40 accounts", "25 min each, by hand", "paper")], x=110, y=144, h=70, w=250, gap=40, size=16, subsize=14)
sk_problem.note(380, 244, "Sanne's lesson no. 1: store IT is an eighth workstream", "red", size=17)

sk_analogy = Doodle(760, 220, "Doodle of a chain of cafés with a 'new café kit': a list of the coffee machine, the till, the Wi-Fi, the card reader and who orders each, with lead times. The card reader takes six weeks, so it's ordered first. The till arrives already set up from head office; the new manager just plugs it in.",
                    "A café chain's opening kit: the slow things ordered first, the till arrives ready to plug in.")
sk_analogy.icon("store", 60, 40, 1.5)
sk_analogy.row([("card reader", "6 weeks · order first", "pink"), ("till", "pre-set at head office", "green"), ("Wi-Fi", "standard kit", "blue")], x=160, y=40, h=96, gap=20, size=17, subsize=13)
sk_analogy.note(450, 190, "same kit every time; the slowest thing first", "pen", size=18)

sk_how = Doodle(760, 380, "Larder's store IT kit v1, written by Eli on Monday 25 May 2026, used first for Utrecht. Three phases. Week 1 of a launch: order the internet line (6 weeks) and the 4G backup router, and book the Wi-Fi survey. Weeks 4 to 6: handhelds, label printers and the router enrolled in device management centrally and shipped ready; network sheet written. Last two weeks: accounts through the joiners checklist, a failover test, store heartbeat alert on, catalogue and on-call updated. 34 items in all. Device management from 26 May: setting up a handheld goes from 20 minutes to 2.",
                "Three phases, 34 items, the slowest thing in week one. Handhelds arrive ready: 20 minutes → 2.")
for i, (t, s, f) in enumerate([("week 1", "order the line · 4G router · book survey", "pink"),
                               ("weeks 4–6", "devices enrolled centrally · network sheet", "y"),
                               ("last 2 weeks", "accounts · failover test · heartbeat · on-call", "green")]):
    sk_how.box(14, 14 + i * 96, 520, 82, t, f, sub=s, size=18, subsize=14)
sk_how.box(556, 14, 190, 274, "34 items", "paper", sub="used first for Utrecht", size=20, subsize=13)
sk_how.box(110, 306, 540, 60, "device management: handheld set-up 20 min → 2 min", "blue", size=16)

STORE_IT_KIT = dict(
    slug="store-it-kit",
    kicker="a.k.a. “a standard build for a site”",
    tldr="Each new site needs the same IT: a line, a backup, Wi-Fi, devices, accounts, monitoring and a place in the on-call rota. Write it down once as a <b>kit</b>: what's needed, who orders it, its <b>lead time</b>, and in which week of the launch it happens. <b>Order the slowest thing first</b>, set up devices centrally so they <b>arrive ready</b>, and let each launch improve the kit for the next one.",
    chips=[("Family", "answering the stores"), ("Lives in", "ops/store-it-kit.md, referenced by the launch playbook"), ("Pairs with", "the store network, joiners and leavers, the launch playbook")],
    itil=dict(groups=["service", "technical"], chain=["design", "build"], practices=["service configuration management", "infrastructure and platform management", "IT asset management"],
              sre="(a “golden image” and a standard build, for a site instead of a server)", principles=["Optimise and automate", "Progress iteratively with feedback"],
              older="ITIL v3: release and deployment management, standard builds"),
    problem_side="Larder, 18–25 May 2026",
    problem="""  <p class="lead">At Sanne's lessons-learned session on <b>18 May</b>, the top lesson from Rotterdam is <b>“store IT is an eighth workstream”</b>. From Eli's side it's easy to see why. The internet line was ordered on 30 March with a six-week lead time and arrived <b>16 days after opening</b>. Thirty handhelds were set up by hand over two evenings, and 40 accounts were made by hand. <span class="hl-pink">Utrecht is next, with a target of eight weeks from lease to opening, and none of this is written down.</span></p>
  <ul>
    <li>Long lead times are discovered, not planned.</li>
    <li>Device set-up is evening work for one person.</li>
    <li>Each store ends up slightly different.</li>
  </ul>""",
    problem_figs=[sk_problem],
    meanwhile=[("project-2", "lessons-learned", "Sanne's lessons session, 18 May: 41 lines → 12 playbook changes; top lesson “store IT is an eighth workstream”, and “order long-lead items in week 1”.",
                "Eli turns that lesson into the store IT kit a week later: 34 items in three phases, the line ordered in week one, devices enrolled centrally.")],
    analogy_side="the café chain's opening kit",
    analogy="""  <p>A café chain opening its tenth café has a <b>new-café kit</b>: a list of everything from the coffee machine to the card reader, with who orders each one and how long it takes. The card reader takes six weeks, so it's <b>ordered on day one</b>. The till arrives <b>already set up by head office</b>, and the new manager plugs it in. After each opening, the kit gets a little better.</p>""",
    analogy_figs=[sk_analogy],
    map=[("The card reader, six weeks", "The internet line, six weeks"),
         ("Ordered on day one", "Ordered in week 1 of the launch"),
         ("Till set up at head office", "Handhelds enrolled in device management, shipped ready"),
         ("The new manager plugs it in", "Utrecht's store manager switches them on"),
         ("The kit gets better", "v1 Utrecht → v2 after each launch")],
    how_side="three phases, the slowest thing first, devices ready on arrival",
    how="""  <p>On Monday <b>25 May</b> Eli writes the <b>store IT kit v1</b>: <b>34 items</b> in three phases, each with an owner and a lead time.</p>
  <ul>
    <li><b>Week 1:</b> order the internet line (6 weeks) and the 4G backup router, and book a Wi-Fi survey of the empty store.</li>
    <li><b>Weeks 4–6:</b> handhelds, label printers and the router are <b>enrolled in device management</b> centrally and shipped ready. Write the network sheet.</li>
    <li><b>Last two weeks:</b> accounts through the joiners checklist, the failover test, the store heartbeat alert, and the store added to the catalogue and the on-call handover.</li>
  </ul>
  <p>Device management goes live on <b>26 May</b>: €3 per device a month (about €280 for 92 devices), which is within the team's own spending limit. A handheld now enrols itself when it's switched on, so set-up drops from <b>20 minutes to 2</b>, and PIN resets and app updates can be pushed from one screen. Sanne adds the kit to the launch playbook as workstream eight, with Eli as its owner.</p>""",
    how_figs=[sk_how],
    steps=[("List everything the last site needed", "From the issue log and the tickets, not memory."),
           ("Add an owner and a lead time to each", "Lead times decide the order."),
           ("Put the slowest thing in week 1", "Lines, leases, permits."),
           ("Set devices up centrally", "They arrive ready; nobody sets them up in the store."),
           ("End with tests, not hopes", "Failover, heartbeat, a test order, accounts working."),
           ("Improve the kit after each launch", "Version it; date the changes.")],
    vocab=[("Lead time", "Time from ordering something to having it."),
           ("Standard build", "One agreed set-up, used every time."),
           ("Device management (MDM)", "Software that enrols, configures, updates and wipes devices centrally."),
           ("Zero-touch enrolment", "A device configures itself the first time it's switched on."),
           ("Workstream", "A group of launch work with its own owner."),
           ("Versioned checklist", "A checklist with a version number and dated changes.")],
    code=dict(file="ops/store-it-kit.md", note="v1 · Mon 25 May 2026 · first used for Utrecht", plain=True, src="""
# Store IT kit v1                                   owner: Eli · workstream 8

week 1     [ ] order internet line (lead 6 weeks)                 Eli
           [ ] order 4G backup router, 2 SIMs                     Eli
           [ ] book Wi-Fi survey of the empty store              Eli + store lead
weeks 4–6  [ ] 30 handhelds + 3 spares enrolled in MDM, shipped   Eli
           [ ] 2 label printers, 1 store laptop, router: enrolled Eli
           [ ] access points per survey; network sheet written    Eli
last 2 wks [ ] accounts via JML, roles from the hiring form       Eli + HR
           [ ] failover test: line pulled, seconds written down   Eli + store lead
           [ ] store heartbeat alert on; store in catalogue       Eli
           [ ] store in on-call handover; poster + QR on the wall Eli
           … 34 items in all · changes after each launch, dated
"""),
    tools="tools: a checklist in the repo, a device management service, and the launch playbook to hang it on.",
    ladder=[("each store from scratch", ["Lead times discovered late.", "Devices set up by hand."]),
            ("a versioned kit", ["Owners, lead times, three phases.", "Devices enrolled centrally."]),
            ("scripted set-up", ["Network, accounts and monitoring from one config file per store.", "Tests run by script."]),
            ("a store is configuration", ["A new store is a pull request.", "Devices and alerts follow automatically."])],
    ladder_now=1,
    baseline="Each line compares <b>Rotterdam's IT done from scratch</b> to <b>a versioned kit with the line ordered in week 1 and devices enrolled centrally</b>.",
    ratings=[(2, 4, "Stores open with a line and working devices."),
             (2, 4, "Every store is set up the same way."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer last-minute changes before opening."),
             (2, 4, "One checklist shows what's done."),
             (1, 4, "20 minutes → 2 per handheld."),
             (3, 3, "€280 a month for device management."),
             (2, 3, "No more evenings setting up devices."),
             (3, 4, "A day to write, then reuse.")],
    pitfalls=[("Writing it from memory", "The forgotten line is forgotten again.", "build it from the issue log and the tickets."),
              ("No lead times", "The order of work is wrong.", "every item has one; the slowest goes first."),
              ("Setting up devices in the store", "Evenings by hand, each slightly different.", "enrol centrally; ship ready."),
              ("A kit that never changes", "Each launch's lessons are lost.", "version it, date the changes.")],
    use=["You'll open (or set up) a similar site again.", "A launch found long lead times too late.", "Devices are set up by hand.", "Before Utrecht."],
    skip=["A truly one-off site you'll never repeat."],
    related=["<b>Is It the Network?</b> (this volume)", "<b>Forty New People on Monday</b> (this volume)", "<b>Can a Launch Be a Recipe?</b> (Sanne, vol. 6)", "<b>Launching a New City</b> (Grace, vol. 6)"],
    quiz=[("What was Sanne's top lesson from Rotterdam?", "Store IT is an eighth workstream."),
          ("Why is the internet line in week 1?", "It has the longest lead time (six weeks); the order of work follows lead times."),
          ("What does device management change?", "Handhelds enrol themselves when switched on: set-up goes from 20 minutes to 2, and updates and resets come from one screen."),
          ("How does the kit end?", "With tests: failover, heartbeat, accounts working, the store in on-call. Not with hope."),
          ("What happens to the kit after Utrecht?", "It's improved and versioned with the lessons, before the next store.")],
    quiz_sit=[("A new store's lease is signed eight weeks before opening. Which three kit items happen this week?", "Order the internet line, order the 4G backup router, and book the Wi-Fi survey: the slowest things first.")],
    try_it="Take the last site, office or team you set up. List every IT item it needed, with a lead time for each. Sort by lead time. Which ones would you now order in week 1?",
    remember="A launch is late by the length of its <span class=\"hl\">slowest order</span>. Write the kit once, <span class=\"hl\">order the slow thing first</span>, and ship devices ready.",
    sources=["AXELOS, <i>ITIL 4: Infrastructure and platform management</i> and <i>IT asset management</i> practice guides (2020).",
             "Thomas A. Limoncelli et al., <i>The Practice of System and Network Administration</i> (3rd ed., 2016): workstation fleet and standard builds.",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

NOTES = [SERVICE_DESK, SERVICE_REQUESTS, STORE_NETWORK, STORE_IT_KIT]
