# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 3 · Writing it down.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 05 User Stories that Work
us_problem = Doodle(760, 280, "Doodle of three approvals tickets in February 2026. One says: as a user, I want approvals, so that I can approve. One says: implement the swap endpoint. One says: countdown timer. None says who it's for, what they're trying to do, or how anyone will know it works.",
                    "Three tickets: a user who wants approvals to approve, an endpoint, a timer. Who for? Why? How will we know?")
for i, t in enumerate(["“As a user I want approvals so I can approve”", "“Implement swap endpoint”", "“Countdown timer”"]):
    us_problem.box(20, 24 + i * 64, 470, 50, t, "paper", size=15, rx=6)
for i, t in enumerate(["who?", "why?", "done when?"]):
    us_problem.note(620, 60 + i * 50, t, "red", size=22)
us_problem.note(380, 262, "tickets that start no conversation", "red")

us_analogy = Doodle(760, 250, "Doodle of a restaurant order ticket: table four, steak medium-rare, no garlic, nut allergy. The ticket is short because the waiter talked to the guest; it's a reminder of the conversation, and the plate is checked against it before it leaves the kitchen.",
                     "An order ticket is a reminder of a conversation with the guest, and the plate is checked against it.")
us_analogy.icon("receipt", 40, 50, 1.6)
us_analogy.box(160, 40, 200, 110, "the ticket", "y", sub="table 4 · no garlic")
us_analogy.box(380, 40, 180, 110, "the chat", "blue", sub="“nut allergy”")
us_analogy.box(580, 40, 160, 110, "the check", "green", sub="at the pass")
us_analogy.note(450, 210, "card · conversation · confirmation", "pen")

us_how = Doodle(760, 360, "Grace's rewritten story for approvals, 18 February 2026. The card: as a tonight-dinner parent whose item ran out, I want to say yes or no to the substitute within two minutes, so that I don't find out on the doormat. The conversation: Grace, Noor and Ben with the story map and the prototype findings. The confirmation: the example map's rules and examples, such as no answer in two minutes means the default for that customer. Underneath, the INVEST checks: independent, negotiable, valuable, estimable, small, testable.",
                 "Card, conversation, confirmation. A real person, a real need, a reason, and examples that say when it's done.")
us_how.box(14, 14, 732, 110, None, "y")
us_how.text(30, 46, "As a tonight-dinner parent whose item ran out,", "t-head", anchor="start", size=16)
us_how.text(30, 76, "I want to say yes or no to the substitute within 2 minutes,", "t-head", anchor="start", size=16)
us_how.text(30, 106, "so that I don't find out on the doormat.", "t-head", anchor="start", size=16)
us_how.box(14, 140, 360, 100, "conversation", "blue", sub="Grace, Noor, Ben + the map")
us_how.box(386, 140, 360, 100, "confirmation", "green", sub="the example map (rules + examples)")
for i, (l, w) in enumerate([("I", "independent"), ("N", "negotiable"), ("V", "valuable"), ("E", "estimable"), ("S", "small"), ("T", "testable")]):
    x = 20 + i * 122
    us_how.head(x + 50, 280, l, size=24)
    us_how.text(x + 50, 306, w, size=14)
us_how.note(380, 346, "INVEST: a quick check, not a law", "pen", size=16)

USER_STORIES = dict(
    slug="user-stories",
    kicker="a.k.a. “the order ticket”",
    tldr="A user story isn't a specification; it's a <b>reminder of a conversation</b>. Write the <b>card</b> with a real person, a real need and a reason (“as a <i>tonight-dinner parent whose item ran out</i>, I want <i>to say yes or no within two minutes</i>, so that <i>I don't find out on the doormat</i>”). Have the <b>conversation</b> with design and engineering. Write the <b>confirmation</b> as examples that say when it's done. Check it with <b>INVEST</b>: independent, negotiable, valuable, estimable, small, testable.",
    chips=[("Family", "writing it down"), ("Origin", "Kent Beck, Extreme Programming (1999); Ron Jeffries' 3 Cs (2001); Bill Wake's INVEST (2003)"), ("Lives in", "the backlog, linked to the story map and example map"), ("Pairs with", "story mapping, example mapping, proto-personas")],
    problem_side="Larder, 18 February 2026",
    problem="""  <p class="lead">With the story map on the wall, Grace reads the approvals tickets. One says <i>“As a user, I want approvals, so that I can approve.”</i> One says <i>“Implement swap endpoint.”</i> One says <i>“Countdown timer.”</i> None says <b>who</b> it's for, what they're trying to do, or how anyone will know it works. <span class="hl-pink">The tickets start no conversation</span>; engineers fill the gaps with guesses.</p>
  <ul>
    <li>“As a user” describes nobody, so nobody's needs shape the work.</li>
    <li>Technical tasks pose as stories, with no value of their own.</li>
    <li>Without a confirmation, “done” is whatever the engineer decides.</li>
  </ul>""",
    problem_figs=[us_problem],
    analogy_side="the order ticket",
    analogy="""  <p>A restaurant <b>order ticket</b> is short: “table 4, steak medium-rare, no garlic”. It works because the waiter <b>talked to the guest</b> (and heard about the nut allergy), and because the chef <b>checks the plate against it</b> at the pass. The ticket isn't the order; it's the reminder of a conversation, and a test for the result.</p>""",
    analogy_figs=[us_analogy],
    map=[("The ticket", "The card: who, what, why"),
         ("Talking to the guest", "The conversation: Grace, Noor, Ben, the story map"),
         ("“Nut allergy”", "The detail that only comes up by talking: allergens in swaps"),
         ("Checking at the pass", "The confirmation: examples from the example map"),
         ("Table 4", "A real persona, not “a user”")],
    how_side="card, conversation, confirmation",
    how="""  <p>Grace rewrote the stories with Noor and Ben, using the proto-personas from Vol. 1. <b>“As a user”</b> became <b>“as a tonight-dinner parent whose item ran out”</b>; technical tasks moved under the stories they serve; every story got a link to its <b>example map</b> as the confirmation. The approvals backlog went from 41 tickets to 17 stories, each something a picker or customer could notice.</p>""",
    how_figs=[us_how],
    steps=[("Name a real person", "A persona or role with a situation: “a tonight-dinner parent whose item ran out”."),
           ("Say what they need", "In their terms, not the system's: “say yes or no”, not “POST /answer”."),
           ("Say why", "The outcome for them: “don't find out on the doormat”."),
           ("Have the conversation", "Design and engineering, with the map and the evidence."),
           ("Write the confirmation", "Examples that say when it's done (from example mapping)."),
           ("Check INVEST", "Too big? Split it. Not valuable alone? Merge it into a story.")],
    vocab=[("User story", "A short description of a need, from a user's point of view."),
           ("3 Cs", "Card, conversation, confirmation."),
           ("INVEST", "Independent, Negotiable, Valuable, Estimable, Small, Testable."),
           ("Acceptance criteria", "Conditions that confirm a story is done."),
           ("Persona", "A described type of user, based on research."),
           ("Task", "Technical work that serves a story; not a story itself.")],
    code=dict(file="product/approvals/stories/S-03.md", note="one approvals story, as rewritten on 18 February 2026", plain=True, src="""
S-03  Decide on a substitute                                   slice 1 · story map: "customer decides"

As a   tonight-dinner parent whose item ran out
I want to say yes or no to the substitute within 2 minutes
So     I don't find out on the doormat (and don't need a refund ticket)

Conversation  Grace, Noor, Ben · 18 Feb · see prototype findings (Jan): big countdown,
              price difference visible, one tap
Confirmation  example map EM-03 (rules R1–R4, 9 examples), e.g.
              - answers "yes" at 1:40 → the picker packs the substitute
              - no answer at 2:00, default setting → keep the substitute
              - substitute contains a flagged allergen → no default, refund
Tasks         answer endpoint · push + in-app card · picker sees the answer at packing
Measure       event: swap_answered {answer, seconds}
"""),
    tools="tools: any backlog tool (Jira, Linear, Azure DevOps); keep stories short and link the story map, example map and designs instead of pasting them.",
    gains=["<b>Real people</b> shape the work, not “a user”.",
           "<b>Conversations happen</b>: the card invites them.",
           "<b>“Done” is clear</b>: the confirmation says when.",
           "<b>Fewer, more valuable items</b> in the backlog.",
           "<b>Tasks stay under stories</b>, serving value."],
    losses=["<b>Writing well takes practice</b>.",
            "<b>Template worship</b>: perfect sentences, no conversation.",
            "<b>Not every item fits</b> (pure technical work).",
            "<b>Conversations take time</b>, which is the point."],
    baseline="Each line compares <b>tickets like “as a user I want approvals” and bare technical tasks</b> to <b>stories with a real person, need and reason, a conversation, and examples as confirmation</b>.",
    ratings=[(2, 5, "Each story names who benefits and how."),
             (3, 4, "Stories trace to the outcome in the “so that”."),
             (2, 4, "Personas and prototype findings shape the stories."),
             (3, 3, "Neutral."),
             (2, 4, "41 tickets became 17 stories."),
             (2, 5, "The team shares one picture of each story."),
             (3, 3, "Neutral."),
             (3, 4, "Small, testable stories flow."),
             (3, 3, "More thought per story, fewer stories.")],
    pitfalls=[("“As a user”", "Nobody in particular.", "a real persona and situation."),
              ("Stories as specs", "Three pages of requirements in the ticket.", "the card is a reminder; have the conversation."),
              ("Tasks as stories", "“Implement swap endpoint.”", "put tasks under the story they serve."),
              ("No confirmation", "Done when the engineer says so.", "examples that say when it's done.")],
    use=["Customer-facing features.",
         "When tickets don't start conversations.",
         "Teams new to working from a backlog.",
         "Alongside story maps and example maps."],
    skip=["Pure technical work: write it as a task or enabler, honestly.",
          "Bugs: describe what happens and what should."],
    related=["<b>Example mapping</b> (this volume)", "<b>Story mapping</b> (this volume)", "<b>Proto-personas</b> (Vol. 1)", "<b>Definition of ready &amp; done</b> (this volume)"],
    quiz=[("What are the 3 Cs?", "Card, conversation, confirmation."),
          ("What's wrong with “as a user”?", "It describes nobody, so no real needs shape the work."),
          ("What does INVEST stand for?", "Independent, Negotiable, Valuable, Estimable, Small, Testable."),
          ("Where do technical tasks go?", "Under the story they serve, not as stories of their own.")],
    try_it="Take five stories from your backlog. Rewrite each with a real persona and situation, a need in their words and a reason. Link each to three examples that say when it's done. Ask an engineer which version they'd rather start from.",
    remember="The card is a <span class=\"hl\">reminder</span> of a conversation. Name a real <span class=\"hl\">person</span>.",
    sources=["Mike Cohn, <i>User Stories Applied</i> (2004).",
             "Ron Jeffries, “Essential XP: Card, Conversation, Confirmation” (2001).",
             "Bill Wake, “INVEST in Good Stories, and SMART Tasks” (2003).",
             "Jeff Patton, <i>User Story Mapping</i> (2014)."],
)

# ------------------------------------------------------------------ 06 Example Mapping
em_problem = Doodle(760, 280, "Doodle of a question discovered in the middle of slice 1, in March 2026: what happens when the customer doesn't answer within two minutes? Ben's code keeps the substitute. Sam assumed a refund. Grace assumed it depends on a customer setting. Three people, three rules, found in testing.",
                    "“No answer in two minutes: then what?” Three people, three rules, found halfway through building.")
em_problem.box(20, 30, 220, 80, "Ben's code", "blue", sub="keep the swap")
em_problem.box(270, 30, 220, 80, "Sam", "paper", sub="refund it")
em_problem.box(520, 30, 220, 80, "Grace", "y", sub="depends on a setting")
em_problem.box(170, 150, 420, 70, "no answer at 2:00?", "pink", stroke="red", size=18)
em_problem.note(380, 260, "found in testing, not before", "red")

em_analogy = Doodle(760, 250, "Doodle of a referees' training session with video clips. The rule is on the screen; then clips that show it applied, offside and not offside; and the clips nobody agrees on go to the rules committee as questions.",
                     "Referee training: the rule, clips that show it, and the disputed clips sent to the rules committee.")
em_analogy.icon("tv", 30, 60, 1.4)
em_analogy.box(150, 30, 200, 60, "the rule", "blue", size=17)
for i in range(2):
    em_analogy.box(150 + i * 104, 110, 96, 50, "clip", "green", size=15)
em_analogy.box(420, 30, 320, 130, "disputed clips", "pink", sub="→ the rules committee")
em_analogy.note(380, 220, "rules · examples · questions", "pen")

em_how = Doodle(760, 370, "Grace's example map for the decide story, 25 February 2026, 25 minutes with Ben, Noor and Dee. The yellow story card at the top. Four blue rule cards: two-minute window; no answer means keep the swap, unless the customer's setting says refund; price difference over 2 euros needs an answer; allergens never default. Green example cards under each rule. Two red question cards: what if the app is closed? what if there are two swaps in one order? Few reds, so the story is ready.",
                 "Yellow story, blue rules, green examples under each rule, red questions. Twenty-five minutes; few reds means ready.")
em_how.box(220, 10, 320, 50, "S-03 decide on a substitute", "y", size=15)
rules = [("2 minutes", ["yes at 1:40", "no at 0:30"]), ("no answer →", ["keep swap", "setting: refund"]),
         ("> €2 more", ["must answer", "€1.50: default"]), ("allergen", ["never default", "warn on card"])]
for i, (r, exs) in enumerate(rules):
    x = 14 + i * 150
    em_how.box(x, 80, 138, 50, None, "blue", rx=4)
    em_how.text(x + 69, 111, r, "t-head", size=13)
    for k, e in enumerate(exs):
        em_how.box(x + 8, 146 + k * 56, 122, 44, None, "green", rx=4)
        em_how.text(x + 69, 174 + k * 56, e, size=14)
for k, q in enumerate(["app closed?", "2 swaps, 1 order?"]):
    em_how.box(620, 80 + k * 70, 126, 56, None, "pink", rx=4)
    em_how.text(683, 114 + k * 70, q, size=14)
em_how.note(683, 236, "→ pre-mortem", "red", size=15)
em_how.note(380, 300, "25 minutes · Ben, Noor, Dee, Grace", "pen", size=17)
em_how.note(380, 334, "few red cards = ready to build", "green", size=17)

EXAMPLE_MAP = dict(
    slug="example-mapping",
    kicker="a.k.a. “referee training with video clips”",
    tldr="Most misunderstandings about a story are about its <b>rules</b>, and they're found too late, in testing. <b>Example mapping</b> finds them first, in <b>25 minutes</b>, with the “three amigos” (product, engineering, testing or design). Put the <b>story</b> on a yellow card, each <b>rule</b> on a blue card, concrete <b>examples</b> on green cards under their rule, and every <b>question</b> nobody can answer on a red card. Lots of reds: not ready. Too many blues: split the story.",
    chips=[("Family", "writing it down"), ("Origin", "Matt Wynne, “Introducing Example Mapping” (Cucumber, 2015)"), ("Lives in", "a photo or a table linked from the story"), ("Pairs with", "user stories, definition of ready, behaviour-driven development")],
    problem_side="Larder, 25 February 2026",
    problem="""  <p class="lead">Halfway through slice 1, Dee tests a swap with no answer. What should happen at <b>2:00</b>? <b>Ben's code</b> keeps the substitute. <b>Sam</b> assumed a refund. <b>Grace</b> assumed it depends on a customer setting. Three people, three rules, and <span class="hl-pink">nobody found out until testing</span>. Grace realises the other stories probably hide the same kind of gap.</p>
  <ul>
    <li>Rules live in people's heads, each slightly different.</li>
    <li>Edge cases surface in testing, when changing them is expensive.</li>
    <li>Long specs don't help: nobody reads them closely enough to disagree.</li>
  </ul>""",
    problem_figs=[em_problem],
    analogy_side="referee training",
    analogy="""  <p>Referees train with <b>video clips</b>. The <b>rule</b> is on the screen; then <b>clips</b> that show it applied (offside, not offside); and the clips nobody in the room agrees on are written down as <b>questions</b> for the rules committee. By the time of the match, the hard cases have been talked through.</p>""",
    analogy_figs=[em_analogy],
    map=[("The rule on screen", "A blue rule card: “2 minutes to answer”"),
         ("Clips showing it", "Green examples: “answers yes at 1:40”"),
         ("Disputed clips", "Red question cards: “what if the app is closed?”"),
         ("The rules committee", "Whoever can answer, before building"),
         ("The match", "The sprint")],
    how_side="story, rules, examples, questions",
    how="""  <p>Grace ran 25-minute sessions for every slice-2 story, with Ben, Noor and Dee. The decide story yielded <b>four rules</b> (two-minute window; no answer keeps the swap unless the customer's setting says refund; more than €2 extra must be answered; allergens never default) and <b>two questions</b>. One, “what if the app is closed?”, went to the pre-mortem and became the in-app banner. Stories with more than three reds waited.</p>""",
    how_figs=[em_how],
    steps=[("Pick one story", "Yellow card on the table."),
           ("Write the rules you know", "One blue card each: the acceptance criteria, as rules."),
           ("Add examples under each rule", "Green cards, concrete: “no answer, setting “refund me” → refund”."),
           ("Write every open question", "Red cards; don't debate them now."),
           ("Stop at 25 minutes", "Many reds → not ready. Many blues → split the story."),
           ("Keep the result", "A photo or table linked from the story; examples become tests.")],
    vocab=[("Three amigos", "Product, engineering and testing (or design) looking at a story together."),
           ("Rule", "An acceptance criterion: a constraint on behaviour."),
           ("Example", "A concrete case that illustrates a rule."),
           ("Question", "Something nobody in the room can answer yet."),
           ("BDD", "Behaviour-driven development: examples become automated tests."),
           ("Gherkin", "Given-when-then format for examples as tests.")],
    code=dict(file="product/approvals/example-maps/EM-03.md", note="example map for S-03, 25 February 2026", plain=True, src="""
EM-03  S-03 Decide on a substitute                25 min · Grace, Ben, Noor, Dee

RULE R1  The customer has 2 minutes to answer
   ex  answers yes at 1:40 → picker packs the substitute
   ex  answers no at 0:30 → item removed, refunded at packing
RULE R2  No answer → keep the substitute, unless the setting says "refund me"
   ex  no answer, default setting → keep
   ex  no answer, setting "refund me if I don't answer" → refund
RULE R3  Substitute costs more than €2 extra → must answer; no default "keep"
   ex  +€2.40, no answer → refund
   ex  +€1.50, no answer → keep (R2)
RULE R4  Substitute contains one of the customer's flagged allergens → never default
   ex  shows a warning; no answer → refund

QUESTIONS  ? What if the app is closed?          → pre-mortem (banner + default)
           ? Two swaps in one order: one timer or two?   → Noor, by 2 Mar
"""),
    tools="tools: four colours of sticky notes and a timer; Miro or FigJam templates for remote; examples can become automated tests (Cucumber, pytest-bdd).",
    gains=["<b>Rules agreed before building</b>, not in testing.",
           "<b>Edge cases found</b> in 25 minutes.",
           "<b>Examples become tests</b>.",
           "<b>Readiness is visible</b>: count the red cards.",
           "<b>Too-big stories show up</b>: count the blue cards."],
    losses=["<b>25 minutes per story</b> for three or four people.",
            "<b>Needs discipline</b> not to debate questions in the session.",
            "<b>Photos get lost</b> unless linked.",
            "<b>Not for trivial stories</b>."],
    baseline="Each line compares <b>rules assumed separately by each person and found in testing</b> to <b>a 25-minute example map with rules, examples and questions before building</b>.",
    ratings=[(2, 4, "Customers get consistent behaviour at 2:00."),
             (3, 3, "Indirect."),
             (2, 4, "Examples are concrete and testable."),
             (2, 5, "Gaps found in minutes, not in testing."),
             (2, 4, "Big stories get split early."),
             (1, 5, "Ben, Sam and Grace now share one rule."),
             (3, 4, "Support knows the rules before launch."),
             (2, 4, "Fewer stories bounce back from testing."),
             (3, 4, "25 minutes per story.")],
    pitfalls=[("Debating the reds", "The session becomes a two-hour argument.", "write the question, find who can answer, move on."),
              ("Only product in the room", "Grace writes the rules alone.", "product, engineering and testing or design together."),
              ("Abstract examples", "“Handles timeouts correctly.”", "concrete: “no answer, setting “refund me” → refund”."),
              ("Ignoring the signal", "Seven reds, built anyway.", "many reds means not ready.")],
    use=["Stories with business rules or edge cases.",
         "Before a story enters a sprint.",
         "When testing keeps finding “what should happen here?”.",
         "Teams adopting behaviour-driven development."],
    skip=["Trivial stories (a copy change).",
          "Exploratory spikes."],
    related=["<b>User stories that work</b> (this volume)", "<b>Definition of ready &amp; done</b> (this volume)", "<b>Pre-mortem</b> (this volume)", "<b>Testable hypotheses</b> (Vol. 1)"],
    quiz=[("What do the four colours mean?", "Yellow story, blue rules, green examples, red questions."),
          ("What do many red cards tell you?", "The story isn't ready to build."),
          ("What do many blue cards tell you?", "The story is too big; split it."),
          ("Who should be in the session?", "The three amigos: product, engineering, and testing or design.")],
    try_it="Pick the next story your team will start. Get an engineer and a tester or designer for 25 minutes with four colours of sticky notes. Map rules, examples and questions. Count the reds before deciding whether it's ready.",
    remember="The <span class=\"hl\">rule</span>, the clips, and the disputed ones as <span class=\"hl\">questions</span>. Twenty-five minutes.",
    sources=["Matt Wynne, “Introducing Example Mapping” (cucumber.io, 2015).",
             "Gojko Adzic, <i>Specification by Example</i> (2011).",
             "Seb Rose, Matt Wynne, Aslak Hellesøy, <i>The Cucumber Book</i>, 2nd ed. (2017).",
             "George Dinwiddie, on the “three amigos” (2009)."],
)

# ------------------------------------------------------------------ 07 Definition of Ready & Done
dr_problem = Doodle(760, 280, "Doodle of slice 1 in March 2026. Two stories entered the sprint without the picker flow checked with Tomás, and had to be redone. Three stories were called done when merged, but they weren't in production, sent no tracking events, and support didn't know about them.",
                    "Started without Tomás, finished without production, tracking or support. “Done” meant merged.")
dr_problem.box(20, 30, 330, 90, "started too early", "pink", sub="picker flow not checked")
dr_problem.box(410, 30, 330, 90, "“done” = merged", "pink", sub="not live · no tracking · Sam unaware")
dr_problem.note(185, 170, "2 stories redone", "red", size=20)
dr_problem.note(575, 170, "3 stories not really done", "red", size=20)
dr_problem.note(380, 250, "nobody had agreed what ready and done mean", "pen")

dr_analogy = Doodle(760, 250, "Doodle of a restaurant kitchen. Before service: mise en place, everything chopped, measured and ready. After cooking: the plate goes to the pass, where the head chef checks it before it leaves. Ready to start, and done means checked and served, not just cooked.",
                     "A kitchen: mise en place before cooking, and the pass, where the chef checks the plate before it's served.")
dr_analogy.icon("kitchen", 40, 60, 1.3)
dr_analogy.box(170, 40, 260, 100, "mise en place", "blue", sub="ready to start")
dr_analogy.box(470, 40, 270, 100, "the pass", "green", sub="checked, then served")
dr_analogy.note(450, 210, "cooked is not served", "pen")

dr_how = Doodle(760, 340, "Larder's definitions, agreed on 4 March 2026. Ready, before a story enters a sprint: example map done with no red cards, the design for customer-facing screens ready, store or support people consulted if their work changes, the tracking event named. Done: live in production behind a flag, tracking events firing, a help article or support macro written, tested on a store handheld, accepted by Grace. Short lists, agreed by the team.",
                 "Two short checklists, agreed by the team: ready to start, and done means live, measured and supported.")
dr_how.box(14, 14, 360, 280, None, "blue")
dr_how.head(194, 46, "ready", size=19)
for i, t in enumerate(["example map, no reds", "design ready (customer screens)", "Tomás / Sam asked if affected", "tracking event named"]):
    dr_how.text(30, 90 + i * 44, "□ " + t, anchor="start", size=15)
dr_how.box(386, 14, 360, 280, None, "green")
dr_how.head(566, 46, "done", size=19)
for i, t in enumerate(["live in production (flag)", "tracking events firing", "help article / support macro", "tested on a store handheld", "accepted by Grace"]):
    dr_how.text(402, 90 + i * 40, "□ " + t, anchor="start", size=15)
dr_how.note(380, 322, "a checklist, not a contract", "pen", size=17)

DOR_DOD = dict(
    slug="definition-ready-done",
    kicker="a.k.a. “mise en place and the pass”",
    tldr="Two short, <b>team-agreed</b> checklists stop two kinds of waste. A <b>definition of ready</b> says what a story needs <b>before</b> it enters a sprint (rules clear, design ready, affected people consulted), so it isn't rebuilt later. A <b>definition of done</b> says what <b>finished</b> means: not merged, but <b>live, measured and supported</b>. Keep both short, make them visible, and treat ready as a <b>checklist, not a gate</b>.",
    chips=[("Family", "writing it down"), ("Origin", "Scrum's Definition of Done (Schwaber &amp; Sutherland); Definition of Ready from Jeff Sutherland's teams (2008)"), ("Lives in", "the team's wiki page and the board's column rules"), ("Pairs with", "example mapping, user stories, launch checklist")],
    problem_side="Larder, 4 March 2026",
    problem="""  <p class="lead">Slice 1 shipped, but not smoothly. <b>Two stories</b> entered the sprint before anyone checked the picker flow with <b>Tomás</b>; both were redone. <b>Three stories</b> were moved to “done” when the code was merged, but they weren't in production, sent no tracking events, and <b>Sam's</b> support team had never heard of them. <span class="hl-pink">Nobody had agreed what ready and done mean</span>.</p>
  <ul>
    <li>Stories start half-understood and get rebuilt.</li>
    <li>“Done” means different things to different people.</li>
    <li>Tracking and support are forgotten until customers ask.</li>
  </ul>""",
    problem_figs=[dr_problem],
    analogy_side="the restaurant kitchen",
    analogy="""  <p>Before service, a kitchen does its <b>mise en place</b>: everything chopped, measured, ready. Nobody starts a dish and then goes to find the shallots. After cooking, the plate goes to <b>the pass</b>, where the head chef checks it before it leaves. A dish that's cooked but not checked and served isn't done.</p>""",
    analogy_figs=[dr_analogy],
    map=[("Mise en place", "Definition of ready"),
         ("Shallots chopped", "Example map done, no red cards"),
         ("The pass", "Definition of done"),
         ("Checked and served", "Live, measured, supported"),
         ("Cooked but sitting", "Merged but not in production")],
    how_side="two short lists, agreed by the team",
    how="""  <p>The team wrote both lists in 30 minutes, from slice 1's mistakes. <b>Ready</b>: example map with no reds, design for customer screens, Tomás or Sam asked if their work changes, tracking event named. <b>Done</b>: live behind a flag, tracking firing, a help article or support macro, tested on a store handheld, accepted by Grace. Slice 2 had no rebuilt stories and no “done” items that weren't live.</p>""",
    how_figs=[dr_how],
    steps=[("Start from real mistakes", "What went wrong last sprint? Each item answers one."),
           ("Write ready: four or five items", "What a story needs before starting, no more."),
           ("Write done: live, measured, supported", "Production, tracking, support, the device it runs on, acceptance."),
           ("Agree as a team", "The team owns the lists, not the PO alone."),
           ("Make them visible", "On the board's columns; check them at planning and review."),
           ("Review every few sprints", "Add what keeps going wrong; drop what never does.")],
    vocab=[("Definition of ready", "What a story needs before the team starts it."),
           ("Definition of done", "What must be true before work is called finished."),
           ("Merged", "Code joined to the main branch; not yet live."),
           ("Behind a flag", "Live in production but switched on only for some."),
           ("Acceptance", "The PO's check that the story does what was agreed."),
           ("Gate", "A hard stop; ready should be a checklist, not a gate.")],
    code=dict(file="team/ordering/working-agreements.md", note="ready and done, agreed 4 March 2026", plain=True, src="""
# Ordering & apps team · working agreements            review every 3 sprints

READY (before a story enters a sprint)
  [ ] Example map done, no red cards left (or each has an owner and date)
  [ ] Customer-facing screens: design ready (Noor)
  [ ] Store or support work changes? Tomás / Sam consulted
  [ ] Tracking event named (e.g. swap_answered)

DONE (before a story moves to Done)
  [ ] Live in production, behind a flag if needed
  [ ] Tracking events firing in the dashboard
  [ ] Help article or support macro written (Sam has seen it)
  [ ] Tested on a store handheld (picker stories) or both apps (customer stories)
  [ ] Accepted by Grace against the examples

Ready is a checklist, not a gate: a story can start with a named open question.
"""),
    tools="tools: a wiki page and the board's column rules (Jira, Linear and Trello support checklists per column); the example map as the main “ready” artefact.",
    gains=["<b>Fewer rebuilt stories</b>: rules and people checked first.",
           "<b>Done means live</b>, measured and supported.",
           "<b>Support isn't surprised</b>.",
           "<b>Tracking exists</b> from day one.",
           "<b>Team-owned standards</b>, not imposed ones."],
    losses=["<b>Can become bureaucracy</b> if lists grow.",
            "<b>Ready as a gate</b> slows everything.",
            "<b>Done takes longer</b> per story (honestly).",
            "<b>Needs review</b> to stay relevant."],
    baseline="Each line compares <b>no shared definitions, with “done” meaning merged</b> to <b>short team-agreed checklists for ready and done, with done meaning live, measured and supported</b>.",
    ratings=[(2, 4, "Features reach customers working and supported."),
             (3, 4, "Tracking from day one shows the effect."),
             (2, 4, "Tracking events exist for every story."),
             (2, 4, "Measured from release, not weeks later."),
             (3, 3, "Neutral."),
             (2, 5, "Everyone means the same by ready and done."),
             (2, 4, "Sam and Tomás are never surprised."),
             (2, 4, "No stories bounce back."),
             (3, 3, "Two short lists, checked at planning and review.")],
    pitfalls=[("Ready as a gate", "Nothing starts until every box is ticked.", "a checklist; a named open question is fine."),
              ("Done = merged", "Code on main, nothing live.", "done means live, measured, supported."),
              ("Lists too long", "Twenty items nobody reads.", "four or five each, from real mistakes."),
              ("PO-imposed", "Grace writes the lists alone.", "the team agrees and owns them.")],
    use=["Teams where stories get rebuilt or bounce back.",
         "When “done” is argued about.",
         "Features that need support and tracking.",
         "New teams forming working agreements."],
    skip=["Experiments meant to be thrown away (lighter lists).",
          "Incidents: fix first."],
    related=["<b>Example mapping</b> (this volume)", "<b>User stories that work</b> (this volume)", "<b>Launch checklist</b> (this volume)", "<b>Sprint goals</b> (this volume)"],
    quiz=[("What does a definition of ready prevent?", "Stories starting half-understood and being rebuilt."),
          ("What does “done” mean in Larder's definition?", "Live in production, tracking firing, support ready, tested on the right device, accepted."),
          ("Should ready be a gate?", "No: a checklist; a named open question can be allowed."),
          ("Who owns the lists?", "The team, not the product owner alone.")],
    try_it="List the last three stories that bounced back or that customers found broken. For each, write the check that would have caught it. Turn those into a four-item ready list and a five-item done list, and agree them with your team at the next retro.",
    remember="<span class=\"hl\">Mise en place</span> before cooking. The <span class=\"hl\">pass</span> before serving.",
    sources=["Ken Schwaber and Jeff Sutherland, <i>The Scrum Guide</i> (2020), on the Definition of Done.",
             "Jeff Sutherland, on the Definition of Ready (scruminc.com).",
             "Mike Cohn, “The Dangers of a Definition of Ready” (Mountain Goat Software, 2016).",
             "Henrik Kniberg, <i>Scrum and XP from the Trenches</i>, 2nd ed. (2015)."],
)

NOTES = [USER_STORIES, EXAMPLE_MAP, DOR_DOD]
