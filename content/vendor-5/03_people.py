# Series 5 · On the Client's Floor · Vol. 5 · Other People's Politics · People, theirs and ours (notes 9–12).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 09 What If Client Staff Fear We'll Take Their Jobs?
sf_problem = Doodle(760, 240, "Doodle of MetroVolt's MAVIS support team, seven people, in October 2028. Wave 1 retired 16 per cent of MAVIS's batch. Ascend rumours say 20 per cent fewer people. Asif asks Ines quietly at the coffee machine: when MAVIS goes, do we go too?",
                    "“When MAVIS goes, do we go too?” Asif, at the coffee machine.", exact=True)
for i in range(7):
    sf_problem.circle(60 + i * 56, 90, 22, "y")
sf_problem.note(228, 150, "MAVIS support team · 7 people", "pen", size=17)
sf_problem.box(460, 40, 286, 110, "“do we go too?”", "pink", sub="Asif, 18 Oct", size=21, subsize=15)
sf_problem.note(380, 210, "Ines doesn't know. And it isn't hers to answer.", "red", size=18)

sf_how = Doodle(760, 320, "How Ines answered. Don't promise: she can't say their jobs are safe. Say what you know: MAVIS shrinks over about thirty months; Lodestar needs people who understand customer data to run it. Involve them: the MAVIS team pairs with Wrenfield on wave 1 support, and three join the Lodestar run team. Send job questions to MetroVolt: Elaine and HR hold a session for the team. And never speculate about Ascend.",
                "Don't promise, say what you know, involve them, and send job questions to the client.", exact=True)
for i, (h, sub, fill) in enumerate([("don't promise", "you can't", "pink"), ("say what you know", "≈ 30 months; skills needed", "y"), ("involve them", "pair on support", "green"), ("send to client", "Elaine + HR session", "blue")]):
    sf_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
sf_how.box(14, 160, 732, 70, "3 of the 7 join the Lodestar run team (Asif, Marta + 1)", "green", size=18)
sf_how.note(380, 280, "and never speculate about Ascend", "red", size=18)

STAFF_FEAR = dict(
    slug="staff-fear", date=date(2028, 10, 18), meta=on_site(date(2028, 10, 18)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. when your project threatens the client's people",
    tldr="Replacing a system often threatens the jobs of the people who ran it, and they'll ask you, quietly, what it means for them. <b>Don't promise</b> what you can't control. <b>Say what you know</b>, plainly. <b>Involve them</b> in what comes next (they know things you need). And <b>send job questions to their employer</b>, who must answer them. Never speculate about restructures you've only heard about.",
    chips=[("Family", "people, theirs and ours"), ("Lives in", "delivery/lodestar/run-team-plan.md"), ("Pairs with", "one team (vol. 2), the person who knows (vol. 3)")],
    problem_side="The Grid, 18 October 2028",
    problem="""  <p class="lead">MetroVolt's <b>MAVIS support team</b> is seven people. Wave 1 retired 16 % of MAVIS's nightly batch. Rumours about Ascend talk of “20 % fewer people”.</p>
  <ul>
    <li>On <b>18 October</b>, <b>Asif</b>, who's paired with Bilal since 2027, asks Ines at the coffee machine: <i>“When MAVIS goes, do we go too?”</i></li>
    <li>Ines doesn't know. MetroVolt hasn't said. It isn't Wrenfield's decision.</li>
    <li>Two of the seven have stopped coming to the Lodestar stand-up. <span class="hl-pink">Bert retires in March; his knowledge is in their heads now.</span></li>
  </ul>""",
    problem_figs=[sf_problem],
    sides=dict(client=("Asif and the MAVIS team", "<p>They've kept MAVIS running for years, and Lodestar is visibly shrinking it. In a year of cost cuts they're scared, and Wrenfield is the most visible sign of the change. They ask the vendor because the vendor is at the next desk; their own management hasn't said anything.</p>", "Are you here to switch us off along with MAVIS?"),
                vendor=("Ines", "<p>Ines likes Asif and needs the MAVIS team's knowledge for waves 2–4. She also knows she has no right to promise anything about MetroVolt jobs, and that a wrong word at a coffee machine becomes a rumour by lunchtime.</p>", "I can't answer his question. I can answer the ones that are mine.")),
    sides_after="People don't need the vendor to promise their jobs are safe. They need honesty about what the vendor knows, and a way to be part of what comes next.",
    analogy_side="the builders and the tenants",
    analogy="""  <p>Builders renovating a block of flats are asked by tenants: “Will we be able to stay?” A good site manager doesn't guess. He says what he knows (“we're doing two floors at a time, about thirty months”), asks the tenants what they know about the building, and says: “That question is for the housing association; I'll ask them to hold a meeting.” Then he makes sure they do.</p>""",
    map=[("The tenants", "The MAVIS support team"),
         ("“Will we be able to stay?”", "“When MAVIS goes, do we go too?”"),
         ("Two floors at a time, thirty months", "Waves 2–4, about thirty months"),
         ("What they know about the building", "MAVIS knowledge Lodestar needs"),
         ("The housing association's meeting", "Elaine and HR's session")],
    how_side="don't promise, say what you know, involve them, send it to the client",
    how="""  <p><b>Don't promise.</b> Ines tells Asif honestly: “I don't know, and it isn't Wrenfield's decision. I won't guess, because a guess from me would sound like a fact.”</p>
  <p><b>Say what you know.</b> “MAVIS shrinks wave by wave, over about thirty months. Lodestar will need people who understand customer data to run it. That's not a promise about anyone; it's the plan.”</p>
  <p><b>Involve them.</b> Ines proposes to Elaine that the MAVIS team <b>pair with Wrenfield on wave 1 support</b> during hypercare, and that MetroVolt consider them for the <b>Lodestar run team</b>. By January three of the seven (Asif, Marta and one more) have joined it. Their MAVIS knowledge goes into Bert's book and the runbooks.</p>
  <p><b>Send job questions to MetroVolt.</b> Ines asks Elaine, the same afternoon, whether MetroVolt could talk to the team. Elaine and HR hold a session on 1 November: no promises either, but a timeline and a named person to ask.</p>
  <p><b>Never speculate about Ascend.</b> Not to Asif, not to Callum, not to anyone.</p>""",
    how_figs=[sf_how],
    steps=[("Don't promise anything about jobs", "It isn't yours to promise."),
           ("Say what you know, plainly", "Timelines, skills needed."),
           ("Don't guess", "Guesses become facts by lunchtime."),
           ("Involve them in what's next", "Their knowledge is valuable."),
           ("Take the question to the client", "Same day, to your counterpart."),
           ("Follow up", "Make sure someone answered them.")],
    vocab=[("Redundancy risk", "The chance a role is removed in a restructure."),
           ("Run team", "The people who operate a system after it's delivered."),
           ("Knowledge retention", "Keeping know-how when people or systems change."),
           ("Speculation", "Guessing about decisions you don't know."),
           ("Change anxiety", "Fear caused by uncertain change, often worse than the change itself."),
           ("Employer's duty", "The client, not the supplier, answers its staff's job questions.")],
    code=dict(file="delivery/lodestar/run-team-plan.md", note="proposal to Elaine · Wed 18 Oct 2028", src="""
LODESTAR RUN TEAM · proposal

need      people who know MetroVolt's customer data to run Lodestar after Wrenfield
          (waves 1–4, ≈ 30 months, then steady state)
proposal  MAVIS support team pairs with Wrenfield on wave 1 support (hypercare)
          MetroVolt considers them first for the run team (MetroVolt's decision)
pairs     Asif ↔ Bilal · Marta ↔ Hana · Kemi ↔ Oskar
asked     Elaine to hold a session for the MAVIS team on timelines and roles (HR)
outcome   session 1 Nov (Elaine + HR) · Jan 2029: 3 of 7 in the run team
we never  promise about jobs · guess about Ascend
"""),
    contract=dict(side="whose people they are", doc="Lodestar SOW · §11.2 and §17", date="signed 30 June 2027", stamp="their employer",
                  clauses=[("11.2", "The Supplier shall transfer knowledge to MetroVolt staff throughout the Services, so that MetroVolt can operate the solution.", "the run team is §11.2 in practice. their knowledge moves both ways."),
                           ("17.3", "The Supplier shall not make representations to MetroVolt staff about their employment.", "this clause exists for exactly the coffee-machine moment.")],
                  plain="contracts often forbid suppliers from making statements to client staff about their employment. That's protection for everyone; it's also a reason to send those questions straight to the client."),
    health=dict(now="a",
                g=("the client communicates well", ["Point people to its announcements.", "Involve them anyway.", "No speculation."]),
                a=("staff afraid, client silent", ["Say what you know; don't promise.", "Ask the client to talk to them.", "Involve them in the run team."]),
                r=("staff hostile to the vendor", ["Patience and respect.", "Never argue about restructures.", "Keep offering involvement."])),
    pressure=dict(level=4, title="a friend's question", cost="an honest “I don't know” · a fear you can't fix",
                  items=["“I don't know” feels inadequate. It's the only honest answer, and it's respected.", "Fear makes good people stop coming to stand-ups. Notice who's missing."]),
    baseline="Each line compares <b>reassuring, guessing or avoiding the question</b> with <b>honesty, involvement and sending job questions to MetroVolt</b>.",
    ratings=[(3, 4, "MetroVolt hears its staff's fear through the right channel."),
             (3, 3, "Hard conversations, honestly handled."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "MAVIS knowledge feeds Lodestar's runbooks."),
             (2, 4, "Knowledge loss before Bert's retirement reduced."),
             (3, 4, "No representations about jobs."),
             (3, 3, "Months to build the run team."),
             (3, 3, "Pairs to maintain.")],
    pitfalls=[("False reassurance", "“You'll be fine” becomes a broken promise.", "don't promise."),
              ("Guessing", "Rumours with your name on them.", "say only what you know."),
              ("Avoiding them", "Fear turns to resentment.", "involve them."),
              ("Answering for the client", "Breaches §17.3 and trust.", "send it to the employer."),
              ("Ignoring absences", "Quiet withdrawal, lost knowledge.", "notice who stops coming.")],
    grimoire=[(5, "survivors-haunting", "Survivor's Haunting", "is what happens inside MetroVolt after cuts: guilt, workload and morale."), (5, "reading-the-omens", "Reading the Omens", "is the same fear, from the inside, a year earlier.")],
    use=["Your project replaces or shrinks a team's work.", "Staff ask you about their future.", "A restructure is rumoured."],
    skip=["Never skip honesty; the involvement depends on the client."],
    related=["<b>Who Knows How It Really Works?</b> (vol. 3)", "<b>How Do Two Companies Work as One Team?</b> (vol. 2)", "<b>How Do We Hand It Over So It Sticks?</b> (vol. 6)", "<b>What Do We Do with What We Overhear?</b> (this volume)"],
    quiz=[("What must a vendor never do when asked about jobs?", "Promise, guess, or answer for the client."),
          ("What did Ines say she knew?", "MAVIS shrinks over about thirty months, and Lodestar needs people who understand customer data."),
          ("How were the MAVIS team involved?", "Pairing on wave 1 support, and three joined the run team."),
          ("What did Ines ask Elaine to do?", "Hold a session with the team on timelines and roles, with HR."),
          ("What does clause 17.3 forbid?", "The supplier making representations to MetroVolt staff about their employment.")],
    quiz_sit=[("Asif asks Ines whether Wrenfield is hiring. What does she say?", "That Wrenfield can't recruit MetroVolt staff involved in Lodestar during the contract (§17) and that his question about his future is best answered by MetroVolt; she'll make sure he gets an answer.")],
    try_it="Think of the people whose work your project changes. What do you honestly know about what happens to them? Who should answer what you don't know? How could they be involved in what comes next?",
    remember="Don't promise, <span class=\"hl\">don't guess</span>. Say what you know, involve them, and <span class=\"hl\">send job questions to their employer</span>.",
    late=dict(when="Wed 18 October 2028 · 20:50 · hotel near The Grid",
              lines=["Asif asked if they go when MAVIS goes. I said I don't know and wouldn't guess. He nodded as if that was the first straight answer he'd had.",
                     "Asked Elaine to talk to them. She said she should have already. She will on the 1st.",
                     "Two of them stopped coming to stand-up. I hadn't noticed. Lottie had."]),
    sources=["William Bridges, <i>Managing Transitions</i> (1991).",
             "UK ACAS, guidance on redundancy consultation.",
             "Amy Edmondson, <i>The Fearless Organization</i> (2018)."],
)

# ------------------------------------------------------------------ 10 How Do We Manage Up in Our Own Firm?
mu_problem = Doodle(760, 240, "Doodle of Graham Wren in Leeds, October 2028, with three demands: cut the Lodestar team from eight to three for the warranty to save money; push Vivian to sell phase 2 to Rupert directly; and promise MetroVolt that Wrenfield will be cheaper than Vexmoor. Ines, between Graham and the client.",
                    "Graham's October: cut to three, sell to Rupert directly, promise to be cheapest.", exact=True)
for i, t in enumerate(["team 8 → 3", "Vivian → Rupert", "“cheaper than Vexmoor”"]):
    mu_problem.box(14 + i * 250, 40, 232, 90, t, "pink", size=19)
mu_problem.note(380, 190, "Ines, between Graham and the client", "pen", size=19)

mu_how = Doodle(760, 330, "How Ines managed up. A Friday note to Graham, the same honesty as to the client: done, numbers, risks, decisions needed. For each demand, options with consequences: team down to five, not three, after hypercare; no direct selling during a planned procurement; price phase 2 from evidence, not from a promise. Graham decides what's his to decide. Ines decides what's hers. Both written down.",
                "Give your own boss what you give the client: a weekly note, numbers, options, and their decisions to make.", exact=True)
mu_how.box(14, 20, 732, 70, "Friday note to Graham", "y", sub="done · numbers · risks · decisions you need to make", size=20, subsize=15)
for i, (h, sub, fill) in enumerate([("team", "8 → 5 after hypercare", "green"), ("selling", "not during procurement", "pink"), ("price", "from evidence", "blue")]):
    mu_how.box(14 + i * 250, 110, 232, 90, h, fill, sub=sub, size=20, subsize=15)
mu_how.box(14, 220, 732, 60, "Graham's decisions: team size, bid / no-bid · Ines's: design, client conduct", "paper", size=16)
mu_how.note(380, 310, "his firm, his risk; my account, my integrity", "pen", size=17)

MANAGING_UP = dict(
    slug="managing-up-own-firm", date=date(2028, 10, 27), meta=on_site(date(2028, 10, 27)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. managing up inside the vendor",
    tldr="A vendor's architect has two clients: the customer, and their own firm's leadership, who see the account through spreadsheets and phone calls. Give your own boss the <b>same honesty</b> you give the client: a <b>weekly note</b>, the <b>numbers</b>, the <b>risks</b>, and <b>options with consequences</b> for decisions only they can make. Be clear which decisions are theirs and which are yours, and never let pressure from home change how you behave on the client's floor.",
    chips=[("Family", "people, theirs and ours"), ("Lives in", "Friday notes to Graham (since Oct 2028)"), ("Pairs with", "protecting margin (vol. 4), saying no")],
    problem_side="Wrenfield, Leeds, 27 October 2028",
    problem="""  <p class="lead">At Wrenfield's monthly review in Leeds on <b>Friday 27 October</b>, Graham has three demands about Lodestar:</p>
  <ul>
    <li><b>Cut the team from eight to three</b> for the warranty, “to get the margin back”.</li>
    <li>Have <b>Vivian sell phase 2 to Rupert directly</b>, “before Vexmoor does”.</li>
    <li><b>Tell MetroVolt Wrenfield will be cheaper than Vexmoor</b> on phase 2.</li>
  </ul>
  <p>Graham is worried: margin at 10 %, phase 2 worth more than the whole of 2027's revenue. <span class="hl-pink">Each demand, done literally, would hurt the account he's trying to protect.</span></p>""",
    problem_figs=[mu_problem],
    sides=dict(client=("MetroVolt (not in the room)", "<p>MetroVolt expects warranty support at the level promised, a fair phase 2 procurement, and bids built on facts. It has no view on Wrenfield's internal arguments, and shouldn't have to.</p>", "(not asked, and shouldn't have to be)"),
                vendor=("Ines and Graham", "<p>Graham owns the firm's risk: cash, margin, the next contract. Ines owns the account's integrity: what's promised, how Wrenfield behaves, the design. Both are legitimate. The friction comes when Graham's pressure arrives without the facts Ines sees every day.</p>", "He sees spreadsheets. I see Elaine. He needs both.")),
    sides_after="Most tension between a firm's leadership and its people on site comes from information gaps, not different values. A weekly note closes most of the gap.",
    analogy_side="the ship's captain and the owners",
    analogy="""  <p>A ship's owners, on shore, see fuel costs and delivery dates. The captain sees the weather. A good captain sends <b>regular, honest reports</b>, gives the owners the decisions that are theirs (which port, which cargo) with options and costs, and keeps the decisions that are hers (how to sail through a storm). She doesn't follow an order that would sink the ship; she explains why, with the chart.</p>""",
    map=[("The owners on shore", "Graham and Wrenfield's board"),
         ("The weather", "What Ines sees on floor 19"),
         ("Regular honest reports", "The Friday note"),
         ("Which port, which cargo", "Team size, bid / no-bid, price floor"),
         ("How to sail through the storm", "Design, client conduct, integrity")],
    how_side="a Friday note, options with consequences, clear decision rights",
    how="""  <p><b>A Friday note</b>, from 27 October: the same shape as the client's status. Done this week, the numbers (margin, hours, cash), risks, and <b>decisions Graham needs to make</b>. Half a page. Graham reads it on Saturday mornings.</p>
  <p><b>Options with consequences</b> for each demand:</p>
  <ul>
    <li><b>Team size</b>: three would breach the warranty and hypercare service levels in Schedule 9; <b>five</b> after hypercare ends (19 November) meets them and saves about £14k a month. Graham chooses five.</li>
    <li><b>Selling to Rupert</b>: phase 2 is a planned procurement; direct selling now could get Wrenfield excluded (as with the football box). Instead: deliver warranty perfectly and let the readiness pack and the results speak. Graham agrees, reluctantly.</li>
    <li><b>“Cheaper than Vexmoor”</b>: an unpriceable promise. Instead: price phase 2 from wave 1's real velocity and data, at a margin above the floor. Graham agrees, if the bid / no-bid includes his floor.</li>
  </ul>
  <p><b>Decision rights, written down.</b> Graham decides team size, bid / no-bid and price floor. Ines decides design, client conduct and what Wrenfield promises on site. Both on one page, signed by both.</p>""",
    how_figs=[mu_how],
    steps=[("Send your boss a weekly note", "Done, numbers, risks, decisions needed."),
           ("Answer demands with options", "Each with its consequence."),
           ("Use the contract as a fact", "Service levels, procurement rules."),
           ("Agree who decides what", "Written, signed."),
           ("Bring problems before they're crises", "No surprises, upwards too."),
           ("Never act on pressure you disagree with on site", "Escalate inside your firm.")],
    vocab=[("Managing up", "Helping your own leaders make good decisions with the information you have."),
           ("Decision rights", "Who is entitled to make which decisions."),
           ("Information asymmetry", "When one party knows much more than another."),
           ("Service levels", "Contractual commitments about support and response."),
           ("Escalation inside the firm", "Raising disagreement with your own leadership, not with the client."),
           ("Weekly note", "A short regular update with decisions needed.")],
    code=dict(file="wrenfield/friday-note-2028-10-27.md", note="Ines to Graham · Fri 27 Oct 2028", src="""
FRIDAY NOTE · Lodestar · w/e 27 Oct 2028

done        exception queue 140 → 61 · 3 sev 2 fixed · run-team pairs started
numbers     margin forecast 10 % · hours worked / booked this week 1.18 · cash: M4 paid
risks       sponsor may change (Ascend) · phase 2 procurement planned March
decisions you need to make
  1 team after hypercare: 8 → 5 (meets Sch. 9; saves ≈ £14k/month)   recommended
                          8 → 3 (breaches Sch. 9 warranty SLAs)       not recommended
  2 phase 2 approach: no direct selling during planned procurement (exclusion risk)
  3 phase 2 price: from wave 1 evidence, at your floor; no "cheaper than Vexmoor"
decision rights (agreed): Graham → team size, bid / no-bid, price floor
                          Ines   → design, client conduct, on-site promises
"""),
    contract=dict(side="the client contract as a fact in an internal argument", doc="Lodestar SOW · Schedule 9 (hypercare and warranty)", date="baseline v2.0", stamp="internal",
                  clauses=[("Sch. 9, 4.1", "During warranty, the Supplier shall respond to Severity 1 defects within 1 hour and resolve within 1 Working Day, with named engineers familiar with the Solution.", "three people can't do this. five can."),
                           ("Phase 2 ITT (draft), 6.7", "Bidders may not contact MetroVolt staff about this procurement except through the clarification process.", "it won't be published until March. the spirit applies now.")],
                  plain="the client's contract is the most persuasive fact in an argument with your own leadership. It turns “I disagree” into “we've promised this”."),
    health=dict(now="a",
                g=("your firm trusts you", ["A light weekly note.", "Decisions shared openly.", "Few demands."]),
                a=("your firm is under pressure", ["Weekly note with numbers.", "Options with consequences.", "Decision rights written."]),
                r=("your firm wants something wrong", ["Refuse in writing, internally.", "Escalate above your boss if needed.", "Never on the client's floor."])),
    pressure=dict(level=4, title="pressure from home", cost="a tense Friday in Leeds · three reluctant agreements",
                  items=["Arguing with the person who pays you is harder than arguing with a client. The Friday note makes it a discussion of facts.", "Graham isn't wrong to worry. He's wrong about the remedies. Give him better ones."]),
    baseline="Each line compares <b>following Graham's three demands, or ignoring them</b> with <b>a Friday note, options with consequences and written decision rights</b>.",
    ratings=[(3, 4, "MetroVolt gets the warranty it was promised."),
             (2, 4, "The team isn't cut to breaking point."),
             (2, 3, "≈ £14k a month saved, fairly."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "No exclusion risk for phase 2."),
             (2, 4, "Decision rights signed."),
             (3, 3, "An hour a week."),
             (3, 3, "A weekly note.")],
    pitfalls=[("Silence upwards", "Your boss decides on spreadsheets alone.", "a weekly note."),
              ("Arguing without options", "It sounds like refusal.", "options with consequences."),
              ("Following pressure on site", "The client sees the firm's panic.", "escalate inside, behave the same outside."),
              ("Unclear decision rights", "The same argument every month.", "write them down."),
              ("Hiding bad numbers", "A worse surprise later.", "numbers every week.")],
    grimoire=[(3, "all-seeing-eye", "The All-Seeing Eye", "is a boss who manages by checking everything; the cure is trading updates for trust, which is the Friday note.")],
    use=["Your firm's leadership is far from the client.", "Pressure from home conflicts with the client's interests.", "Before a big bid or commercial decision."],
    skip=["Never skip it with a fixed-price account."],
    related=["<b>How Do We Protect the Margin?</b> (vol. 4)", "<b>How Do We Say No to a Client?</b> (this volume)", "<b>Should We Even Bid?</b> (vol. 1)", "<b>Managing Up</b> (Grace, vol. 5)"],
    quiz=[("What's in the Friday note?", "Done, numbers, risks, and decisions Graham needs to make."),
          ("Why five people, not three, after hypercare?", "Three would breach Schedule 9's warranty service levels; five meets them."),
          ("Why no direct selling to Rupert?", "Phase 2 is a planned procurement; direct selling risks exclusion."),
          ("Why not promise to be cheaper than Vexmoor?", "It can't be priced; price from evidence instead."),
          ("Whose decisions are whose?", "Graham: team size, bid / no-bid, price floor. Ines: design, client conduct, on-site promises.")],
    quiz_sit=[("Graham phones Rupert himself “just to say hello”. Rupert mentions it to Elaine. What does Ines do?", "Tell Graham, privately and quickly, why it's risky before a procurement, and tell Elaine (no surprises) that it was a courtesy call and won't be repeated.")],
    try_it="Write a half-page Friday note to your own boss: done, numbers, risks, and the decisions only they can make, each with options and consequences.",
    remember="Give your own boss <span class=\"hl\">what you give the client</span>: a weekly note, the numbers, and <span class=\"hl\">their decisions to make</span>.",
    late=dict(when="Fri 27 October 2028 · 22:40 · the train home from Leeds",
              lines=["Three demands. Three counter-offers. Five people, not three. No selling to Rupert. No “cheaper than Vexmoor”.",
                     "Graham signed the decision-rights page. He said it was the first time anyone had told him which decisions were his.",
                     "Friday notes from now on. I should have started in 2027."]),
    sources=["Kim Scott, <i>Radical Candor</i> (2017).",
             "David Maister, <i>Managing the Professional Service Firm</i> (1993).",
             "Mary Abbajay, <i>Managing Up</i> (2018)."],
)

# ------------------------------------------------------------------ 11 How Do We Protect Our Team from the Client?
pt_problem = Doodle(760, 240, "Doodle of three incidents in one week of December 2028. Gareth's deputy shouts at Lottie in a working group over a meter field. Rupert's office emails Hana at 23:00 three nights running with urgent questions. A MetroVolt manager tells Oskar his testers are lazy. Hana hasn't had a weekend off since August.",
                    "One week: a shout at Lottie, three 23:00 emails to Hana, “lazy testers” to Oskar.", exact=True)
for i, (h, sub) in enumerate([("Lottie", "shouted at, Mon"), ("Hana", "23:00 emails ×3"), ("Oskar", "“lazy testers”")]):
    pt_problem.box(14 + i * 250, 40, 232, 100, h, "pink", sub=sub, size=22, subsize=15)
pt_problem.note(380, 200, "and Hana hasn't had a weekend since August", "red", size=19)

pt_how = Doodle(760, 330, "Three protections. In the moment: step in immediately, calmly, and stop it: let's take this offline. The same day: speak to the person's manager or to Elaine, about the behaviour, not the person. As a rule: one front door for urgent requests, Ines or Callum, never individual engineers out of hours; written into the team agreement with MetroVolt. And look after the person: check in privately with Lottie, Hana and Oskar.",
                "Step in at once, raise it the same day, make a rule, and look after the person.", exact=True)
for i, (h, sub, fill) in enumerate([("in the moment", "step in, calmly", "pink"), ("same day", "Elaine / their manager", "y"), ("as a rule", "one front door, no 23:00", "blue"), ("the person", "check in privately", "green")]):
    pt_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
pt_how.box(14, 160, 732, 70, "team agreement v2 (13 Dec): urgent requests via Ines or Callum · 08:00–19:00 unless sev 1", "paper", size=16)
pt_how.note(380, 280, "your team is lent to the client, not given", "pen", size=18)

PROTECT_TEAM = dict(
    slug="protecting-the-team", date=date(2028, 12, 6), meta=on_site(date(2028, 12, 6)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. boundaries between client and vendor team",
    tldr="Your team is <b>lent</b> to the client, not given. When someone on the client side mistreats them (shouting, contempt, late-night demands), <b>step in at once</b>, calmly; <b>raise it the same day</b> with the right person, about the behaviour; set <b>rules</b> that stop it recurring (one front door, working hours); and <b>look after the person</b> privately. The client relationship matters. Your people matter more, and they're watching what you do.",
    chips=[("Family", "people, theirs and ours"), ("Lives in", "team agreement v2 (13 Dec 2028)"), ("Pairs with", "one team (vol. 2), stress on a vendor team (vol. 6)")],
    problem_side="The Grid, December 2028",
    problem="""  <p class="lead">One week in December, after hypercare ends:</p>
  <ul>
    <li><b>Monday</b>: in a meter-data working group, Gareth's deputy <b>shouts at Lottie</b> about a field name, in front of eight people. Lottie says nothing and leaves early.</li>
    <li><b>Monday to Wednesday</b>: Rupert's office emails <b>Hana at 23:00</b> three nights running with “urgent” questions about phase 2 estimates. She answers each by midnight.</li>
    <li><b>Wednesday</b>: a MetroVolt manager tells Oskar his testers are “lazy” in the corridor.</li>
    <li><span class="hl-pink">Hana hasn't had a weekend off since August.</span></li>
  </ul>""",
    problem_figs=[pt_problem],
    sides=dict(client=("MetroVolt people", "<p>Under Ascend pressure, MetroVolt's managers are stretched and short-tempered. Most don't think of supplier staff as people they need to look after: they're “the vendor”, paid to be available. Nobody means harm; the harm happens anyway.</p>", "They're the supplier. That's what they're paid for."),
                vendor=("Ines", "<p>Ines's team has watched her be diplomatic with MetroVolt for eighteen months. Now they're watching whether she'll be equally firm for them. If she isn't, they'll conclude that the client always comes first, and the best of them will leave.</p>", "My team is watching what I do this week.")),
    sides_after="A vendor lead's first duty to the client is good work. Their first duty to their team is not to let them be harmed doing it.",
    analogy_side="the agency nurse and the ward",
    analogy="""  <p>An agency sends nurses to a hospital. If a consultant shouts at one of them, the agency manager doesn't say “they're the client”. She <b>speaks to the ward manager the same day</b>, agrees how requests will come in future, and checks the nurse is all right. The hospital usually thanks her: it doesn't want its consultants behaving like that either.</p>""",
    map=[("The agency nurse", "Lottie, Hana, Oskar"),
         ("The consultant who shouts", "Gareth's deputy"),
         ("The ward manager, same day", "Elaine, and the person's manager"),
         ("How requests will come", "One front door, working hours"),
         ("Checking the nurse is all right", "Private check-ins")],
    how_side="step in, raise it, make a rule, look after the person",
    how="""  <p><b>In the moment.</b> Ines wasn't in Monday's working group; Bilal was, and froze. Ines tells the team: next time, whoever is senior steps in at once, calmly: <i>“Let's take this one offline.”</i> In Wednesday's corridor, Ines is there; she says it.</p>
  <p><b>The same day.</b> Ines speaks to <b>Elaine</b> about all three incidents on Wednesday evening, and to Gareth (whom she now knows well) about his deputy. She describes the <b>behaviour</b>, not the person: “shouting at a junior engineer in a meeting”. Gareth apologises to Lottie himself on Thursday.</p>
  <p><b>A rule.</b> The <b>team agreement v2</b>, signed by Elaine on 13 December: urgent requests to Wrenfield go through <b>Ines or Callum</b>, not to individual engineers; no requests outside <b>08:00–19:00</b> except severity 1; disagreements about work go to the working group lead, not to the person.</p>
  <p><b>The person.</b> Ines checks in privately with each. Lottie is fine, mostly; she wanted to know Ines would have stepped in. Oskar laughs it off. <b>Hana</b> says she's fine, and then cries in the stairwell. That conversation starts the next volume.</p>""",
    how_figs=[pt_how],
    steps=[("Step in at once", "Calmly: “let's take this offline”."),
           ("Raise it the same day", "With the client lead and the person's manager."),
           ("Describe behaviour, not character", "What happened, where, to whom."),
           ("Make a rule", "One front door, working hours, in writing."),
           ("Check in privately", "With each person affected."),
           ("Tell the team what you did", "They need to know you'll do it again.")],
    vocab=[("Boundaries", "Agreed limits on how people are treated and when they're contacted."),
           ("Psychological safety", "Feeling safe to speak up without being humiliated."),
           ("Front door", "The single route for requests to a team."),
           ("Duty of care", "An employer's responsibility for its people's wellbeing."),
           ("Bystander", "Someone who witnesses mistreatment; their action or silence matters."),
           ("Out-of-hours contact", "Requests outside agreed working times.")],
    code=dict(file="delivery/lodestar/team-agreement-v2.md", note="signed by Elaine and Ines · Wed 13 Dec 2028", src="""
LODESTAR TEAM AGREEMENT v2 (adds §5, how we treat each other)

5.1  Urgent requests to Wrenfield go through Ines Duarte or Callum Reid,
     not to individual engineers.
5.2  No requests to Wrenfield staff outside 08:00–19:00 except severity 1
     incidents (via the on-call number).
5.3  Disagreements about work go to the working-group lead, in the meeting
     or after it; not to the individual, and never by raising voices.
5.4  Anyone, of any firm, may say "let's take this offline", and the meeting moves on.
5.5  Concerns about behaviour go to Elaine Corbett and the person's manager.
"""),
    contract=dict(side="what protects the team", doc="Lodestar SOW · §18 (conduct) · team agreement v2", date="13 Dec 2028", stamp="signed",
                  clauses=[("18.1", "Each Party shall ensure its personnel treat the other's personnel with courtesy and respect, and comply with the other Party's dignity at work policy while on its premises.", "MetroVolt's own policy applies to its managers too."),
                           ("TA v2, 5.2", "No requests to Wrenfield staff outside 08:00–19:00 except severity 1 incidents.", "Hana's 23:00 emails, ended by a sentence.")],
                  plain="many contracts include a mutual conduct clause and the client's dignity-at-work policy. Pointing to them makes protecting your team a matter of agreed rules, not a personal complaint."),
    health=dict(now="a",
                g=("respectful client", ["Rules anyway, lightly.", "Thank the client when they back you.", "Check in regularly."]),
                a=("a client under pressure", ["Step in, raise it, rule, check in.", "Behaviour, not character.", "Team agreement updated."]),
                r=("repeated mistreatment", ["Formal complaint under the contract.", "Remove your people from the situation.", "Consider whether to continue."])),
    pressure=dict(level=4, title="your people", cost="three conversations with the client · one in a stairwell",
                  items=["Raising a client's behaviour feels like risking the account. Not raising it risks your team, and they'll remember either way.", "“I'm fine” from someone who hasn't had a weekend since August isn't an answer. It's a symptom."]),
    baseline="Each line compares <b>staying diplomatic and saying nothing</b> with <b>stepping in, raising it the same day, a written rule and private check-ins</b>.",
    ratings=[(3, 4, "Elaine and Gareth backed Wrenfield's people."),
             (1, 4, "The team sees its lead step in."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Hana's overload surfaces before it's a crisis."),
             (3, 4, "Team agreement v2 signed."),
             (4, 4, "A day."),
             (4, 4, "One page.")],
    pitfalls=[("Saying nothing", "Your team learns the client always wins.", "step in, raise it."),
              ("Raising it weeks later", "Nobody remembers; nothing changes.", "the same day."),
              ("Attacking the person", "They defend themselves.", "describe the behaviour."),
              ("No rule", "It happens again next week.", "front door, working hours."),
              ("Forgetting the person", "They feel unsupported.", "check in privately.")],
    grimoire=[(2, "bulldozer-ogre", "The Bulldozer Ogre", "explains the shouter."), (2, "boundary-goblin", "The Boundary Goblin", "explains the 23:00 “quick question, no rush”.")],
    use=["Anyone on the client side mistreats your team.", "Out-of-hours demands become normal.", "Your team is quieter than usual."],
    skip=["Never skip it."],
    related=["<b>How Do Two Companies Work as One Team?</b> (vol. 2)", "<b>How Do We Notice Stress on a Vendor Team?</b> (vol. 6)", "<b>What Do We Do When the Client Shouts?</b> (next note)", "<b>Why Is the Team Arguing?</b> (Sanne, vol. 4)"],
    quiz=[("What do you say in the moment?", "Something calm like “let's take this one offline”."),
          ("Who do you raise it with, and when?", "The client lead and the person's manager, the same day."),
          ("What do you describe?", "The behaviour, not the person's character."),
          ("What rules went into the team agreement?", "One front door for urgent requests; no requests outside 08:00–19:00 except severity 1; disagreements to the working-group lead."),
          ("Why check in privately?", "People say they're fine in public; private check-ins find out.")],
    quiz_sit=[("Rupert himself emails Hana at 22:30 after the new agreement. What does Ines do?", "Reply herself the next morning with the answer, and remind Rupert's office politely of the agreed front door, copying Elaine. Tell Hana not to answer out-of-hours emails.")],
    try_it="Think of the last time someone outside your team treated one of your people badly. What did you do in the moment, the same day, and afterwards? Write the one rule that would stop it recurring.",
    remember="Your team is <span class=\"hl\">lent, not given</span>. Step in at once, raise it the same day, <span class=\"hl\">and check on the person</span>.",
    late=dict(when="Wed 6 December 2028 · 22:00 · hotel near The Grid",
              lines=["Lottie shouted at on Monday. Hana's 23:00 emails. “Lazy testers”. One week.",
                     "Gareth apologised to Lottie himself. Elaine signed the new agreement without a word changed.",
                     "Hana said she's fine and then cried in the stairwell. Since August, no weekend. I knew. I didn't do anything. That changes now."]),
    sources=["Amy Edmondson, <i>The Fearless Organization</i> (2018).",
             "UK ACAS, guidance on bullying and harassment at work.",
             "Christine Porath, <i>Mastering Civility</i> (2016)."],
)

# ------------------------------------------------------------------ 12 What Do We Do When the Client Shouts?
cs_problem = Doodle(760, 240, "Doodle of the hypercare closing review on 21 November 2028. Rupert, reading a Vexmoor summary, believes 1,206 exceptions means 1,206 customers with wrong bills. He raises his voice at Ines in front of twelve people: this is exactly what I was warned about. In fact all 1,206 were resolved within a day, and none produced a wrong bill.",
                    "“This is exactly what I was warned about!” In front of twelve people.", exact=True)
cs_problem.box(150, 30, 460, 110, "“1,206 customers with wrong bills!”", "pink", sub="Rupert · reading a summary", size=20, subsize=15)
cs_problem.box(150, 170, 460, 50, "fact: 1,206 handled by hand in a day · 0 wrong bills", "green", size=16)

cs_how = Doodle(760, 330, "How Ines answered in the room. Stay calm and lower your voice. Acknowledge the worry, not the accusation: wrong bills would be serious. Answer with one fact: all 1,206 were handled by hand within a day, and no customer received a wrong bill; the reconciliation report is in the pack, page 4. Offer to go through it after the meeting. Then, later that week, a private conversation about the shouting, and a written follow-up of the facts.",
                "Lower your voice, acknowledge the worry, one fact, an offer; talk about the shouting later, privately.", exact=True)
for i, (h, sub, fill) in enumerate([("calm", "lower your voice", "y"), ("acknowledge", "the worry, not the blame", "blue"), ("one fact", "0 wrong bills · p. 4", "green"), ("offer", "walk through it after", "paper")]):
    cs_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=13)
cs_how.box(14, 150, 360, 80, "later, privately", "pink", sub="“the way it was said”", size=19, subsize=15)
cs_how.box(386, 150, 360, 80, "in writing", "paper", sub="the facts, same day", size=19, subsize=15)
cs_how.note(380, 290, "never shout back; never apologise for facts", "red", size=18)

CLIENT_SHOUTS = dict(
    slug="client-who-shouts", date=date(2028, 11, 21), meta=on_site(date(2028, 11, 21)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. handling an angry client in a meeting",
    tldr="When a client shouts at you in a meeting, the room is watching how you respond, not who's right. <b>Stay calm</b> and lower your voice. <b>Acknowledge the worry</b> (not the accusation). Answer with <b>one clear fact</b> and where to find the proof, and <b>offer</b> to go through it afterwards. Follow up <b>in writing</b> the same day. Talk about <b>the shouting itself</b> later, privately. Never shout back, and never apologise for facts.",
    chips=[("Family", "people, theirs and ours"), ("Lives in", "hypercare closing pack, page 4"), ("Pairs with", "the steering ambush (vol. 4), protecting the team")],
    problem_side="The Grid, room 27A, 21 November 2028",
    problem="""  <p class="lead">At the <b>hypercare closing review</b> on <b>Tuesday 21 November</b>, Rupert, two weeks into sponsoring Lodestar, reads from a one-line Vexmoor summary: “1,206 exceptions at cutover.”</p>
  <ul>
    <li>He believes that means <b>1,206 customers with wrong bills</b>.</li>
    <li>He raises his voice, in front of twelve people: <i>“This is exactly what I was warned about.”</i></li>
    <li>In fact all 1,206 were handled by hand within a day by Customer Ops' exception desk, and <b>no customer received a wrong bill</b>. <span class="hl-pink">It's on page 4 of the pack he hasn't opened.</span></li>
  </ul>""",
    problem_figs=[cs_problem],
    sides=dict(client=("Rupert", "<p>Rupert is new to Lodestar, under pressure from Ascend's targets, and has been briefed mostly by Vexmoor. Wrong bills would be a board-level problem. His anger is mostly fear, expressed badly, in public.</p>", "I won't be the sponsor who let this happen."),
                vendor=("Ines", "<p>Ines knows the facts are on her side. The danger is the room: twelve people watching whether Wrenfield is defensive, rattled or calm. Winning the argument loudly would lose the relationship with the new sponsor.</p>", "The facts will win. My job is to let them, calmly.")),
    sides_after="Anger in meetings is usually fear in public. Answer the fear; deal with the manner privately.",
    analogy_side="the airline gate agent",
    analogy="""  <p>A passenger shouts at a gate agent that the flight is cancelled. The good agent doesn't shout back or argue. She <b>lowers her voice</b>, says “I understand you're worried about making your connection”, gives <b>one fact</b> (“the flight is delayed 40 minutes, not cancelled, and your connection is protected”), and shows him the screen. Most passengers calm down in a sentence.</p>""",
    map=[("The shouting passenger", "Rupert"),
         ("“Worried about the connection”", "Worried about wrong bills"),
         ("One fact", "0 wrong bills; all 1,206 handled within a day"),
         ("Showing the screen", "Page 4 of the pack"),
         ("Not shouting back", "A lower voice, not a counter-attack")],
    how_side="calm, acknowledge, one fact, an offer; the manner later",
    how="""  <p><b>In the room</b>, Ines waits a second, lowers her voice and says three things:</p>
  <ul>
    <li><b>Acknowledge the worry</b>: <i>“Wrong bills would be serious, and you're right to ask.”</i></li>
    <li><b>One fact, and the proof</b>: <i>“All 1,206 were handled by hand within a day by Customer Ops' exception desk; no customer received a wrong bill. The reconciliation is on page 4.”</i></li>
    <li><b>An offer</b>: <i>“I'd be glad to go through it with you after the meeting.”</i></li>
  </ul>
  <p>Elaine confirms the fact from the exception desk's report. Rupert says “fine” and moves on. The meeting continues.</p>
  <p><b>The same day, in writing</b>: a five-line email to Rupert, through Elaine, with the exception figures, the reconciliation and the desk's report attached.</p>
  <p><b>Later, privately</b>: on Thursday, in a short one-to-one Rupert asked for, Ines says: <i>“On Tuesday, I'd have preferred that question before the meeting. If something worries you, call me directly; I'll always give you the facts.”</i> Rupert says Vexmoor's summary had alarmed him. He doesn't apologise. He does call directly, twice, in December.</p>""",
    how_figs=[cs_how],
    steps=[("Pause and lower your voice", "Calm is contagious too."),
           ("Acknowledge the worry", "Not the accusation."),
           ("One fact, and where the proof is", "Short, checkable."),
           ("Offer to go through it", "After the meeting."),
           ("Follow up in writing the same day", "Facts, attachments."),
           ("Address the manner privately", "Later, briefly, without blame.")],
    vocab=[("De-escalation", "Reducing the intensity of a conflict."),
           ("Acknowledgement", "Recognising someone's concern without agreeing with their claim."),
           ("Face", "A person's standing in front of others."),
           ("Fight-or-flight", "The stress response that makes people shout or freeze."),
           ("Follow-up", "A written record after a difficult exchange."),
           ("Direct line", "Inviting someone to bring concerns to you first.")],
    code=dict(file="email/2028-11-21-exceptions.md", note="Ines to Rupert, via Elaine · Tue 21 Nov 2028, 16:30", src="""
Subject: Wave 1 exceptions: the facts

Rupert,
Following this morning: of 380,000 accounts, 1,206 (0.32 %) needed manual handling
at cutover. Customer Ops' exception desk resolved all 1,206 by Sunday 24 Sep, 19:10.
No moved customer received an incorrect bill (billing runs 25 Sep onward reconciled
100 %; Halvorsen confirms no reissued bills).
Attached: exception desk report · reconciliation 24 Sep · Halvorsen confirmation.
Happy to go through any of it, any time: 07700 900 412.
Ines
"""),
    contract=dict(side="what the milestone already proved", doc="Lodestar SOW · Schedule 4, M4 and M5", date="M5 accepted 22 Nov 2028", stamp="facts",
                  clauses=[("M4", "Wave 1 live: … ≤ 0.5 % of records in the exception queue …", "0.32 %. accepted on 2 Oct, by MetroVolt."),
                           ("M5", "Hypercare ended: 8 weeks · no open severity 1 or 2 incidents.", "accepted the day after the shouting.")],
                  plain="accepted milestones are facts both sides have already agreed. Pointing to them is calmer and stronger than arguing about what happened."),
    health=dict(now="a",
                g=("a client who trusts you", ["A quick private word.", "Facts in a sentence.", "Move on."]),
                a=("a new sponsor briefed by others", ["Calm, acknowledge, one fact, offer.", "Same-day follow-up.", "A direct line."]),
                r=("repeated public hostility", ["Raise it formally under §18.", "Meetings with an agenda and minutes.", "Protect juniors from attending."])),
    pressure=dict(level=4, title="shouted at in public", cost="twelve witnesses · one deep breath",
                  items=["The second before you answer is the most important. Take it.", "Never apologise for facts to make the anger stop. Apologise for mistakes, if there are any."]),
    baseline="Each line compares <b>defending yourself loudly, or apologising to calm him</b> with <b>calm, acknowledgement, one fact, an offer, and the manner discussed later</b>.",
    ratings=[(3, 4, "Rupert calls directly in December."),
             (3, 3, "Stressful, but the room stayed calm."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "A misunderstanding corrected in a sentence."),
             (2, 4, "Facts in writing the same day."),
             (4, 4, "Minutes, not days."),
             (4, 4, "One email.")],
    pitfalls=[("Shouting back", "Two angry people, one loser: you.", "lower your voice."),
              ("Apologising for facts", "You've accepted a false claim.", "acknowledge the worry, not the claim."),
              ("A lecture", "The room loses patience.", "one fact."),
              ("No follow-up", "The false number survives.", "in writing, same day."),
              ("Never addressing the manner", "It becomes normal.", "privately, later, briefly.")],
    grimoire=[(2, "bulldozer-ogre", "The Bulldozer Ogre", "is the client who talks over everyone; the Grimoire's counter-spells work on sponsors too."), (6, "client-demon", "The Client Demon", "covers the difficult client from GridSight's side.")],
    use=["A client raises their voice in a meeting.", "An accusation based on wrong information.", "A new stakeholder briefed by others."],
    skip=["Never skip the private conversation if it happens twice."],
    related=["<b>What Happens When Steering Turns on Us?</b> (vol. 4)", "<b>How Do We Protect Our Team from the Client?</b> (previous note)", "<b>What If Our Sponsor Moves On?</b> (this volume)", "<b>Why Is the Team Arguing?</b> (Sanne, vol. 4)"],
    quiz=[("What three things did Ines say in the room?", "Acknowledged the worry, gave one fact with where the proof was, and offered to go through it."),
          ("Why acknowledge the worry and not the accusation?", "The worry is legitimate; the accusation was wrong."),
          ("What was the fact?", "All 1,206 exceptions were handled within a day; no customer received a wrong bill."),
          ("When was the shouting itself discussed?", "Later, privately, briefly, in a one-to-one."),
          ("Why never apologise for facts?", "It accepts a false claim to make anger stop.")],
    quiz_sit=[("Rupert shouts at Lottie, not Ines, in a meeting. What does Ines do?", "Step in at once and take the question herself (“I'll answer that, Rupert”), then raise it with Elaine and Rupert privately the same day, as in the previous note.")],
    try_it="Think of a time someone was angry with you in public. Write the three sentences you'd say now: the worry, one fact with its proof, an offer. What would you say privately afterwards?",
    remember="Anger in public is <span class=\"hl\">fear, badly expressed</span>. Answer the fear calmly; deal with <span class=\"hl\">the manner privately</span>.",
    late=dict(when="Tue 21 November 2028 · 21:30 · hotel near The Grid",
              lines=["Rupert shouted. Twelve people watched me. I waited one second and lowered my voice. It worked better than I deserved.",
                     "Zero wrong bills. Page 4. He hadn't opened the pack. Vexmoor's summary had one line, and it was the wrong one.",
                     "M5 accepted tomorrow. Hypercare's over. Shaking hands still, at 21:30."]),
    sources=["Douglas Stone, Bruce Patton and Sheila Heen, <i>Difficult Conversations</i> (1999).",
             "William Ury, <i>Getting Past No</i> (1991).",
             "Chris Voss, <i>Never Split the Difference</i> (2016): tactical empathy."],
)

NOTES = [STAFF_FEAR, MANAGING_UP, PROTECT_TEAM, CLIENT_SHOUTS]
