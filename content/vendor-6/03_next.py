# Series 5 · On the Client's Floor · Vol. 6 · The Cost and the Ending · The next deal (notes 9–12).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 6".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 09 How Do We Bid Against the Rival for the Next Phase?
pb_problem = Doodle(760, 240, "Doodle of the phase 2 tender: waves 2 to 4, about 1.9 million more customers, budget about £9m, issued 5 March 2029, bids due Wednesday 4 April. Two bidders: Wrenfield, the incumbent for wave 1, and Vexmoor, the large rival already advising Rupert. Vexmoor will be cheaper. Wrenfield knows exactly how hard the work is.",
                    "Phase 2: ≈ £9m, bids due 4 April. Vexmoor will be cheaper. We know how hard it is.", exact=True)
pb_problem.box(14, 20, 732, 70, "phase 2 · waves 2–4 · ≈ 1.9 m customers · ≈ £9m · due Wed 4 Apr 2029", "y", size=17)
pb_problem.box(14, 120, 360, 80, "Wrenfield", "blue", sub="the incumbent · knows the pain", size=22, subsize=14)
pb_problem.box(386, 120, 360, 80, "Vexmoor", "pink", sub="the rival · near Rupert · cheaper", size=22, subsize=14)
pb_problem.note(380, 226, "the temptation: promise twelve months again", "red", size=17)

pb_how = Doodle(760, 340, "How Wrenfield's phase 2 bid was built. Real velocity: 38 points a sprint, from wave 1. Real data: wave 1's exception rate of 0.32 per cent and the profiling of all 1.9 million remaining accounts. Real lessons: the five from the joint session, built into the plan. A named team: Ines, Callum, Tariq, Bilal, Oskar, Lottie; Hana's role her own decision. Priced on what we now know: £9.4m, 15 per cent margin, including the 6 per cent for sustainable pace.",
                "Real velocity, real data, real lessons, a named team, an honest price.", exact=True)
for i, (h, sub, fill) in enumerate([("velocity", "38 / sprint", "y"), ("data", "all 1.9 m profiled", "blue"), ("lessons", "5 built in", "green"), ("team", "named", "paper"), ("price", "£9.4m · 15 %", "pink")]):
    pb_how.box(14 + i * 148, 20, 138, 100, h, fill, sub=sub, size=18, subsize=12)
pb_how.box(14, 150, 732, 70, "three waves, 28 months · wave 2 live Jun 2030 · plan at 85 % capacity", "paper", size=16)
pb_how.note(380, 290, "bid what you know, not what they'd like to hear", "red", size=18)

PHASE2_BID = dict(
    slug="phase-2-bid", date=date(2029, 4, 4), meta=on_site(date(2029, 4, 4)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. bidding for the next phase",
    tldr="The incumbent's advantage in a follow-on bid isn't the relationship: it's <b>evidence</b>. Bid from <b>real velocity</b>, <b>real data</b>, <b>real lessons</b> and a <b>named team</b>, and price the next phase on what you now know, not on what would beat the rival. If the rival is cheaper because it knows less, say clearly what you know, and let the client decide.",
    chips=[("Family", "the next deal"), ("Lives in", "bids/metrovolt-phase2/ · submitted Wed 4 Apr 2029"), ("Pairs with", "the bid / no-bid (vol. 1), sustainable pace")],
    problem_side="Leeds, 4 April 2029",
    problem="""  <p class="lead">MetroVolt's <b>phase 2 tender</b> was issued on <b>5 March</b>: waves 2 to 4, the remaining <b>1.9 million</b> customers, a budget of about <b>£9m</b>. Bids are due <b>Wednesday 4 April</b>.</p>
  <ul>
    <li>Two bidders: <b>Wrenfield</b>, wave 1's supplier, and <b>Vexmoor</b>, already advising Rupert on Project Horizon.</li>
    <li>Everyone expects Vexmoor to be cheaper.</li>
    <li>Vivian's suggestion: <span class="hl-pink">“we promise all three waves in eighteen months, and sort it out later.”</span> Two years ago she promised twelve months over dinner.</li>
  </ul>""",
    problem_figs=[pb_problem],
    sides=dict(client=("Desmond and Elaine", "<p>Desmond's evaluation is 60 % quality, 40 % price. Elaine knows what wave 1 really took and will be on the panel; Rupert's office will be too, and it likes Vexmoor's ambition. Lesson 1 from the joint session is in the tender: bidders get the full data profile.</p>", "Show us the plan you'd actually deliver."),
                vendor=("Ines and Callum", "<p>Wrenfield knows the work better than anyone: velocity, data, the queue on cutover night, Halvorsen's quirks. It also knows that the bid it could win cheaply is one it would lose money and people delivering. Graham needs phase 2; the pace policy has added 6 %.</p>", "We're the only bidder who's done this. Bid like it.")),
    sides_after="A follow-on bid is the incumbent's chance to replace promises with evidence. Throwing that away to match a rival's price wastes the only real advantage.",
    analogy_side="the second ascent",
    analogy="""  <p>A climber who has been up a mountain once doesn't plan her second ascent from the brochure. She knows where the ice is, how long the ridge really takes, and which camp floods. Another guide might promise clients the summit in two days. She says <b>four, and here's why</b>: the ridge, the ice, the camp. Clients who've heard both pitches know which guide has been there.</p>""",
    map=[("Where the ice is", "Real data: all 1.9 m accounts profiled"),
         ("How long the ridge takes", "Real velocity: 38 points"),
         ("The camp that floods", "Lessons: the cutover queue"),
         ("The brochure promise", "Vivian's eighteen months"),
         ("Four days, and here's why", "£9.4m and 28 months, with the evidence")],
    how_side="evidence, a named team, an honest price",
    how="""  <p><b>Real velocity.</b> The plan uses wave 1's <b>38 points</b> a sprint, not a hoped-for 45, at <b>85 %</b> of capacity.</p>
  <p><b>Real data.</b> Bilal profiles all <b>1.9 million</b> remaining accounts from the tender's data pack (lesson 1): business accounts and prepay meters are messier than wave 1's. The bid shows the numbers.</p>
  <p><b>Real lessons.</b> The five joint lessons are in the plan: interface tests on Halvorsen's test system from week 2; the performance environment booked from day 1; queue capacity planned for each cutover night.</p>
  <p><b>A named team.</b> Ines, Callum, Tariq, Bilal, Oskar, Lottie, plus four engineers. For Hana, the bid says honestly: <i>“Hana Sato, wave 1 tech lead, may rejoin for wave 3; this is her decision.”</i></p>
  <p><b>An honest price.</b> <b>£9.4m</b> over <b>28 months</b>, wave 2 live in June 2030, margin <b>15 %</b> (the floor), including the pace policy. Vivian's eighteen months is not in it. The bid's executive summary has one sentence Ines insisted on: <i>“This is the plan we would deliver, not the plan we think you'd like to hear.”</i></p>
  <p>Submitted through the portal at <b>11:40</b>, twenty minutes before the deadline.</p>""",
    how_figs=[pb_how],
    steps=[("Use your real velocity", "And plan below full capacity."),
           ("Profile the real data", "All of it, if you can."),
           ("Build in the lessons", "Visibly, in the plan."),
           ("Name the team", "Honestly, including who's uncertain."),
           ("Price on what you know", "At or above your floor."),
           ("Say why you're not the cheapest", "If you aren't.")],
    vocab=[("Follow-on bid", "A bid for the next phase of work you've delivered."),
           ("Incumbent", "The supplier currently doing the work."),
           ("Evidence-based estimate", "An estimate from measured past performance."),
           ("Quality / price split", "How the evaluation weights each (here 60 / 40)."),
           ("Margin floor", "The lowest margin the firm will accept."),
           ("Winner's curse", "Winning a bid by underpricing it, then losing money.")],
    code=dict(file="bids/metrovolt-phase2/summary.md", note="submitted Wed 4 Apr 2029 · 11:40", src="""
PHASE 2 BID · Wrenfield Digital · executive summary (extract)

scope        waves 2–4 · ≈ 1.9 m customer accounts · 28 months · wave 2 live Jun 2030
evidence     velocity 38 points/sprint (wave 1, measured) · planned at 85 % capacity
             wave 1 exceptions 0.32 % · all 1.9 m remaining accounts profiled (data pack)
             5 joint lessons built into the plan (§3.4)
team         Ines Duarte · Callum Reid · Tariq Rahman · Bilal Khan · Oskar Lind ·
             Lottie Marsh · +4 engineers · Hana Sato may rejoin for wave 3 (her decision)
price        £9.4m fixed per wave · margin 15 % (floor) · includes sustainable pace (§5.4)
one line     "This is the plan we would deliver, not the plan we think you'd like to hear."
"""),
    contract=dict(side="what the tender scores", doc="Phase 2 invitation to tender · §6 (evaluation)", date="issued 5 Mar 2029", stamp="submitted",
                  clauses=[("6.1", "Bids are evaluated 60 % quality and 40 % price. Quality includes the credibility of the plan and the evidence for it.", "credibility is 60 %. we have the evidence; use it."),
                           ("6.4", "MetroVolt may reject a bid it considers abnormally low.", "a reminder that cheaper isn't automatically safer, for them either.")],
                  plain="read how a tender scores quality. Evidence for the plan often counts more than the price difference, especially for an incumbent with real numbers."),
    health=dict(now="a",
                g=("a strong evidence bid", ["Real numbers throughout.", "A named team.", "An honest price."]),
                a=("a cheaper rival", ["Explain your price with evidence.", "Show what the cheap plan misses.", "Don't drop below the floor."]),
                r=("pressure to promise the impossible", ["Say no in writing.", "Offer phasing instead.", "Be ready to lose."])),
    pressure=dict(level=4, title="the next deal", cost="£9m of work · Graham's pipeline · a cheaper rival",
                  items=["Vivian's eighteen months would make the bid look better and the delivery worse. Ines has seen that film.", "If MetroVolt chooses a cheaper plan, it's MetroVolt's decision. Make sure it's an informed one."]),
    baseline="Each line compares <b>matching the rival's ambition and price</b> with <b>a bid from real velocity, data, lessons, a named team and an honest price</b>.",
    ratings=[(3, 4, "Elaine sees the plan they'd really deliver."),
             (3, 4, "A plan the team can live with."),
             (2, 4, "15 % margin, not a loss."),
             (3, 4, "Scope and phasing explicit."),
             (3, 4, "Plan built on measured numbers."),
             (2, 4, "No promises the team can't keep."),
             (3, 4, "Every claim backed."),
             (3, 3, "A month of evenings (within the pace policy)."),
             (3, 3, "A large bid.")],
    pitfalls=[("Bidding the brochure", "The winner's curse.", "the plan you'd deliver."),
              ("Relying on the relationship", "Procurement scores evidence.", "show the numbers."),
              ("Dropping below the floor", "You win and lose money.", "15 %."),
              ("Overstating the team", "Key-personnel promises you can't keep.", "say who's uncertain."),
              ("Attacking the rival", "It looks weak.", "say what you know.")],
    grimoire=[(6, "incumbent-dragon", "The Incumbent Dragon", "is Wrenfield now: the supplier everyone else must dislodge."), (6, "overpromise-golem", "The Overpromise Golem", "is Vivian's eighteen months, if it had gone in.")],
    use=["Any follow-on bid.", "When a cheaper rival is expected.", "After a hard first phase."],
    skip=["Never skip the evidence."],
    related=["<b>Should We Even Bid?</b> (vol. 1)", "<b>How Long Will It Really Take?</b> (vol. 1)", "<b>Can a Fixed-Price Team Keep a Sustainable Pace?</b> (this volume)", "<b>How Do We Wait for the Decision?</b> (next note)"],
    quiz=[("What is the incumbent's real advantage?", "Evidence: real velocity, real data, real lessons."),
          ("What velocity does the plan use?", "38 points a sprint, at 85 % of capacity."),
          ("How does the bid describe Hana?", "She may rejoin for wave 3; it's her decision."),
          ("What's the price and margin?", "£9.4m over 28 months, 15 % margin."),
          ("What did Vivian suggest, and what happened to it?", "All three waves in eighteen months; it isn't in the bid.")],
    quiz_sit=[("A clarification question from Desmond asks why Wrenfield's price is above the budget. How does Ines answer?", "With the evidence: velocity, the data profile of the 1.9 million accounts, the five lessons and the pace. Offer options (phasing, scope moved between waves) rather than a lower price for the same plan.")],
    try_it="For your next follow-on estimate, list the three numbers you've actually measured on the last phase. How different is your new estimate if you use them instead of the old assumptions?",
    remember="The incumbent's advantage is <span class=\"hl\">evidence</span>. Bid the plan <span class=\"hl\">you'd actually deliver</span>.",
    late=dict(when="Wed 4 April 2029 · 19:30 · Leeds",
              lines=["Submitted at 11:40. £9.4m, 28 months, 15 %. Vivian's eighteen months is not in it.",
                     "Hana read the team page and said “may rejoin for wave 3, her decision” is the kindest sentence in the bid.",
                     "Orals on the 26th. Callum has already booked a rehearsal room. I've booked a weekend off."]),
    sources=["David Maister, Charles Green and Robert Galford, <i>The Trusted Advisor</i> (2000).",
             "Steve McConnell, <i>Software Estimation</i> (2006): historical data.",
             "UK Cabinet Office, <i>Sourcing Playbook</i> (2021): abnormally low bids."],
)

# ------------------------------------------------------------------ 10 How Do We Wait for the Decision?
wl_problem = Doodle(760, 240, "Doodle of the wait. Orals on Thursday 26 April 2029. A decision promised by 15 June. Seven weeks of silence from procurement. Rumours in the lift. The team asks what happens to them if Wrenfield loses. Halvorsen's billing re-tender is also decided this month. And wave 1 still has to run.",
                    "Seven weeks of silence, rumours in the lift, and “what happens to us?”", exact=True)
wl_problem.line("M40 120 H720", thin=True)
for x, t in [(40, "orals 26 Apr"), (380, "silence"), (720, "decision by 15 Jun")]:
    wl_problem.circle(x, 120, 7, "y")
    wl_problem.note(x, 100, t, "pen", anchor="start" if x == 40 else ("end" if x == 720 else "middle"), size=16)
wl_problem.note(380, 190, "Lottie: “what happens to us if we lose?”", "red", size=18)

wl_how = Doodle(760, 330, "Two plans, both written. If we win: mobilise wave 2 from Monday 2 July, the named team, Hana's choice, design authority booked. If we lose: three months of exit assistance under Schedule 10, a full handover to Vexmoor, cooperate warmly, and every Wrenfield person has a next role in Leeds. Tell the team both plans, on Monday 30 April. Then keep running wave 1 as if nothing were being decided.",
                "A plan for winning, a plan for losing well, and a team that knows both.", exact=True)
wl_how.box(14, 20, 360, 130, "if we win", "green", sub="mobilise 2 Jul · named team · DA booked", size=22, subsize=14)
wl_how.box(386, 20, 360, 130, "if we lose", "blue", sub="3 months exit help · handover to Vexmoor · next roles", size=22, subsize=13)
wl_how.box(14, 180, 732, 60, "told to the team, both plans: Mon 30 Apr", "y", size=18)
wl_how.note(380, 290, "and wave 1 still runs as if nothing were being decided", "pen", size=17)

WIN_OR_LOSE = dict(
    slug="win-or-lose", date=date(2029, 4, 30), meta=on_site(date(2029, 4, 30)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. waiting for the decision",
    tldr="Between the bid and the decision, nothing you do changes the result, and everything you do shows who you are. <b>Write two plans</b>: one for winning, one for <b>losing well</b> (a proper handover, warm cooperation, next roles for the team). <b>Tell the team both</b>. Don't chase procurement or read the lift. And keep <b>running today's work</b> as if nothing were being decided.",
    chips=[("Family", "the next deal"), ("Lives in", "bids/metrovolt-phase2/after-the-decision.md"), ("Pairs with", "the bid, leaving well")],
    problem_side="Floor 19, 30 April 2029",
    problem="""  <p class="lead">The orals were on <b>Thursday 26 April</b>: an hour each, Wrenfield at 10:00, Vexmoor at 14:00. The decision is promised <b>by 15 June</b>.</p>
  <ul>
    <li>Procurement is silent, as it must be.</li>
    <li>Rumours in the lift: “Rupert's office loved Vexmoor's demo.” “Elaine scored us top on quality.” Nobody knows.</li>
    <li>Lottie asks at the stand-up: <span class="hl-pink">“What happens to us if we lose?”</span></li>
    <li>Halvorsen's billing re-tender, which wave 1's interface depends on, is also being decided.</li>
  </ul>""",
    problem_figs=[wl_problem],
    sides=dict(client=("Desmond", "<p>Desmond's job is a fair, defensible decision. Any contact from a bidder about the evaluation (a call, a lunch, a hint) is a risk he'll record. MetroVolt also still needs wave 1 run well, whoever wins phase 2.</p>", "Don't call me. I'll call you."),
                vendor=("Ines", "<p>The team is anxious and so is Ines. Graham checks the portal daily. The temptation is to read signals into everything, and to let wave 1 slide while everyone waits. Losing is a real possibility, and the team deserves to know what it would mean.</p>", "We can't change the decision. We can be ready for it.")),
    sides_after="How a supplier behaves while waiting, and after losing, is remembered longer than the bid.",
    analogy_side="the expectant parents' bag",
    analogy="""  <p>Expectant parents pack a hospital bag weeks before the due date, and plan for both a quick birth and a long one. Then they <b>carry on with ordinary life</b>: go to work, cook dinner. Checking the bag every hour doesn't change when the baby comes. Having it packed means that whatever happens, at 03:00, nobody panics.</p>""",
    map=[("The packed bag", "Two plans, written"),
         ("A quick birth or a long one", "Win or lose"),
         ("Carrying on with ordinary life", "Running wave 1 well"),
         ("Checking the bag every hour", "Refreshing the portal, reading the lift"),
         ("Nobody panics at 03:00", "The team knows both plans")],
    how_side="two plans, both told, no chasing, today's work",
    how="""  <p><b>The win plan.</b> Mobilise wave 2 from <b>Monday 2 July</b>: the named team, four new engineers from Leeds, design authority dates booked, Hana asked (not told) about wave 3.</p>
  <p><b>The lose plan.</b> Schedule 10's <b>three months of exit assistance</b>: a full handover to Vexmoor using the handbook, Wrenfield's engineers available to answer questions, the run team supported. Warm cooperation: Ines drafts a note offering Oliver's team a walkthrough. And for the people: Graham confirms nobody is made redundant; each person has a <b>next role in Leeds</b>, named.</p>
  <p><b>Tell the team both.</b> At the stand-up on <b>Monday 30 April</b>, Ines answers Lottie's question with both plans on one page. The room relaxes. Oskar says it's the first time a bid hasn't felt like a cliff.</p>
  <p><b>No chasing.</b> No calls to Desmond. No questions to Elaine about the scores. If anyone at MetroVolt raises phase 2, the answer is: “we're not allowed to discuss it, and we're busy with wave 1.”</p>
  <p><b>Today's work.</b> Wave 1's April billing runs clean. The run team's first month alone has one severity 2, fixed by Kemi. And in May, news that matters: <b>Halvorsen wins the billing re-tender</b>, so IA-01 stays as it is.</p>""",
    how_figs=[wl_how],
    steps=[("Write the win plan", "Mobilisation, team, dates."),
           ("Write the lose plan", "Handover, cooperation, next roles."),
           ("Tell the team both", "Early, on one page."),
           ("Don't chase", "Procurement records every contact."),
           ("Don't read the lift", "Rumours aren't scores."),
           ("Run today's work well", "It's still being watched.")],
    vocab=[("Standstill period", "A pause after an award decision before contract signature, for challenges."),
           ("Exit assistance", "Help a departing supplier gives in the handover to a successor."),
           ("Contingency plan", "A plan prepared for an outcome you hope won't happen."),
           ("Bidder contact rules", "Limits on talking to the client during evaluation."),
           ("Pipeline", "A firm's expected future work."),
           ("Bench", "Staff between client projects.")],
    code=dict(file="bids/metrovolt-phase2/after-the-decision.md", note="shared with the team · Mon 30 Apr 2029", src="""
AFTER THE DECISION (due by 15 Jun) · two plans, both real

IF WE WIN                               IF WE LOSE
mobilise wave 2 Mon 2 Jul               exit assistance 3 months (Sch. 10)
named team + 4 engineers from Leeds     handover to Vexmoor: handbook, Q&A, run team
design authority dates booked           offer Oliver's team a walkthrough
Hana asked (not told) about wave 3      nobody made redundant (Graham, in writing)
                                        next roles: each person named, in Leeds
MEANWHILE
no calls to Desmond · no questions about scores · run wave 1 as usual
"""),
    contract=dict(side="what happens if we lose", doc="Lodestar SOW · Schedule 10 (exit) · §2", date="signed 30 June 2027", stamp="ready either way",
                  clauses=[("Sch. 10, 2.1", "On expiry or termination, the Supplier shall provide exit assistance for up to three months, including cooperation with any Replacement Supplier.", "“cooperation with any Replacement Supplier”: Vexmoor, if so."),
                           ("ITT 4.6", "Bidders shall not contact MetroVolt staff about the evaluation before the award is announced.", "so: no calls. Graham has been told twice.")],
                  plain="your current contract usually says what you owe if a rival takes over. Read it while you're waiting; it's half of your lose plan already written."),
    health=dict(now="a",
                g=("calm while waiting", ["Both plans known.", "Today's work steady.", "No chasing."]),
                a=("an anxious team", ["Tell both plans.", "Name the next roles.", "Keep the routines."]),
                r=("a team pretending it can't lose", ["Write the lose plan now.", "Tell people the truth.", "Make the handover ready."])),
    pressure=dict(level=4, title="the wait", cost="seven weeks of not knowing · Graham refreshing the portal",
                  items=["Nothing you do now changes the decision. Everything you do changes how you're remembered.", "Telling the team the lose plan felt risky. It made them calmer."]),
    baseline="Each line compares <b>waiting, chasing and hoping</b> with <b>two written plans, both told, no chasing, wave 1 run well</b>.",
    ratings=[(3, 4, "MetroVolt sees a steady supplier."),
             (2, 4, "The team knows what happens either way."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 4, "Wave 1 run well meanwhile."),
             (2, 4, "Both outcomes planned."),
             (2, 4, "No contact during evaluation."),
             (3, 3, "A day to write both plans."),
             (3, 3, "One page.")],
    pitfalls=[("Only a win plan", "Losing becomes chaos.", "write both."),
              ("Not telling the team", "Rumour and anxiety.", "both plans, early."),
              ("Chasing procurement", "A recorded risk.", "silence."),
              ("Reading the lift", "False hope or false despair.", "ignore it."),
              ("Letting today's work slip", "It's still being watched.", "run it well.")],
    grimoire=[(5, "go-bag-scroll", "The Go-Bag Scroll", "is the same idea inside MetroVolt: be ready for the outcome you don't want.")],
    use=["After any bid.", "During a client's restructure.", "Before any decision you can't control."],
    skip=["Never skip the lose plan."],
    related=["<b>How Do We Bid Against the Rival for the Next Phase?</b> (previous note)", "<b>What Does It Leave Behind?</b> (Sanne, vol. 6)", "<b>How Do We Leave Well?</b> (this volume)", "<b>Leaving a Vendor</b> (Eli, vol. 5)"],
    quiz=[("When were the orals, and when is the decision due?", "26 April 2029; by 15 June."),
          ("What's in the lose plan?", "Three months' exit assistance, a handover to Vexmoor, warm cooperation, next roles for everyone."),
          ("Why tell the team both plans?", "It answers “what happens to us?” and makes them calmer."),
          ("Why not chase Desmond?", "Contact during evaluation is against the rules and recorded as a risk."),
          ("What news arrived in May?", "Halvorsen won the billing re-tender, so IA-01 stays.")],
    quiz_sit=[("Rupert's chief of staff tells Ines at the coffee machine: “Between us, it's looking good for you.” What does she do?", "Thank her politely, say she can't discuss the procurement, and not repeat it to the team as news. Carry on with both plans.")],
    try_it="Think of a decision you're waiting on. Write a one-page plan for each outcome. Who needs to know them? What will you do today regardless?",
    remember="You can't change the decision. <span class=\"hl\">Pack both bags</span>, tell the team, and <span class=\"hl\">run today's work well</span>.",
    late=dict(when="Mon 30 April 2029 · 20:10 · hotel near The Grid",
              lines=["Told the team both plans. Lottie asked the question everyone was thinking; the answer was on one page.",
                     "Oskar said it's the first bid that hasn't felt like a cliff.",
                     "Graham refreshed the portal four times during our call. I didn't mention it."]),
    sources=["UK Public Contracts Regulations 2015 (and the Procurement Act 2023): standstill periods.",
             "Chip Heath and Dan Heath, <i>Decisive</i> (2013): preparing to be wrong.",
             "David Maister, <i>Managing the Professional Service Firm</i> (1993)."],
)

# ------------------------------------------------------------------ 11 Can We Tell Lodestar's Story?
cs_problem = Doodle(760, 240, "Doodle of Graham's request: a glossy case study for Wrenfield's website, now, with MetroVolt's logo and the headline 380,000 customers migrated flawlessly. The problems: the phase 2 procurement is live; the contract forbids publicity without consent; and it wasn't flawless.",
                    "“380,000 customers, flawlessly.” Published now, with their logo.", exact=True)
cs_problem.box(14, 20, 732, 80, "“380,000 customers migrated flawlessly”", "y", size=22)
for i, (t, fill) in enumerate([("procurement live", "pink"), ("§18: consent", "paper"), ("not flawless", "pink")]):
    cs_problem.box(14 + i * 250, 130, 232, 60, t, fill, size=18)

cs_how = Doodle(760, 330, "How the case study was done. Ask permission: Elaine agrees in principle, with Anjali for legal, but nothing published during the procurement. Tell it honestly: the hard parts included, CR-007, the red status, M3 rejected and accepted ten days later, the 22-minute queue on wave 1 night. Write it with the client: Elaine edits and adds her own quotes. Hold it: approved text, published after the phase 2 award, whichever way it goes.",
                "Permission, the hard parts, written with them, and held until after the award.", exact=True)
for i, (h, sub, fill) in enumerate([("permission", "Elaine + Anjali", "green"), ("honest", "hard parts in", "y"), ("together", "her edits, her quotes", "blue"), ("held", "after the award", "paper")]):
    cs_how.box(14 + i * 186, 20, 174, 110, h, fill, sub=sub, size=19, subsize=13)
cs_how.box(14, 160, 732, 70, "headline: “Lodestar wave 1: 379,997 customers, one long night, and what we learned”", "green", size=15)
cs_how.note(380, 280, "the hard parts are what make it believable", "red", size=18)

CASE_STUDY = dict(
    slug="case-study", date=date(2029, 5, 16), meta=on_site(date(2029, 5, 16)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. the case study and the reference",
    tldr="Your best project is your best marketing, but it's <b>the client's story too</b>. <b>Ask permission</b> (the contract almost certainly requires it), <b>tell it honestly</b>, hard parts included, <b>write it with the client</b>, and <b>publish nothing during a live procurement</b>. A case study with its problems in it is more convincing than one that says “flawless”.",
    chips=[("Family", "the next deal"), ("Lives in", "marketing/lodestar-case-study-v3.md · approved, held"), ("Pairs with", "references (vol. 1), the joint lessons")],
    problem_side="Leeds, 16 May 2029",
    problem="""  <p class="lead">Graham wants a <b>case study</b> on Wrenfield's website, with MetroVolt's logo and a headline: <span class="hl-pink">“380,000 customers migrated flawlessly.”</span> He wants it now, to help win two other utility bids.</p>
  <ul>
    <li>The <b>phase 2 procurement is live</b>: publishing anything about MetroVolt now could look like lobbying.</li>
    <li>The SOW's <b>§18</b> forbids publicity without MetroVolt's written consent.</li>
    <li>And it wasn't flawless: 379,997 customers, a 22-minute queue, 1,206 exceptions, three accounts excluded.</li>
  </ul>""",
    problem_figs=[cs_problem],
    sides=dict(client=("Elaine and Anjali", "<p>Elaine is proud of wave 1 and happy to be a reference. She doesn't want MetroVolt's logo on a marketing claim during a procurement she's evaluating, and Anjali needs every word checked. After Orion, MetroVolt is wary of any story that sounds too good.</p>", "Yes, later, and true."),
                vendor=("Graham and Ines", "<p>Graham needs the story to win other work; Wrenfield's pipeline matters to everyone on the team. Ines agrees it's Wrenfield's best project, and thinks the hard parts are what make it worth reading.</p>", "Tell it right, or don't tell it yet.")),
    sides_after="Clients read case studies too. The ones they trust admit something went wrong.",
    analogy_side="the wedding speech",
    analogy="""  <p>A good best-man speech is true, a little embarrassing, and <b>approved by nobody's mother-in-law in advance</b>, which is why best men check the dodgier stories with the couple first. The speech that says “a perfect couple who never argue” is forgotten by dessert. The one with the story about the tent in the rain is remembered for years, and the couple are glad it was told.</p>""",
    map=[("Checking with the couple first", "Elaine's and Anjali's permission"),
         ("The tent in the rain", "The 22-minute queue, CR-007, M3 rejected"),
         ("“A perfect couple”", "“Flawlessly”"),
         ("The right moment in the evening", "After the phase 2 award"),
         ("Remembered for years", "A case study people believe")],
    how_side="permission, honesty, written together, held",
    how="""  <p><b>Ask permission.</b> Ines asks Elaine, who brings in Anjali. Agreed in principle, under §18, with one condition: <b>nothing published until after the phase 2 award</b>, whichever way it goes. Graham isn't happy, then agrees.</p>
  <p><b>Tell it honestly.</b> The draft includes the hard parts: the 7.8 % data-quality surprise in discovery and CR-007; the first red status; M3 rejected, then accepted ten days later; the 22 minutes at 04:10 on wave 1 night; the three excluded accounts. And what fixed each.</p>
  <p><b>Write it with the client.</b> Elaine edits two paragraphs and adds her own quote: <i>“They told us bad news early, every time. That's why we got there.”</i> Kemi adds one about the handover. Anjali changes six words.</p>
  <p><b>The headline.</b> Not “flawlessly”. <b>“Lodestar wave 1: 379,997 customers, one long night, and what we learned.”</b></p>
  <p><b>Hold it.</b> Version 3, approved in writing on <b>Wednesday 6 June</b>, sits in a folder marked “after the award”. Elaine also agrees to take reference calls, after the award. For the two other bids, Graham uses an anonymised summary that Anjali has also approved.</p>""",
    how_figs=[cs_how],
    steps=[("Check the contract", "Publicity clauses, confidentiality."),
           ("Ask the client", "And their legal team."),
           ("Tell the hard parts", "And what fixed them."),
           ("Write it together", "Their edits, their quotes."),
           ("Wait if a procurement is live", "Approve now, publish later."),
           ("Use an anonymised version meanwhile", "Also approved.")],
    vocab=[("Case study", "A published story of a project, used in marketing and bids."),
           ("Publicity clause", "A contract term controlling public mention of the client."),
           ("Reference", "A client who'll speak to prospective clients about you."),
           ("Anonymised case study", "One that doesn't name the client."),
           ("Canvassing", "Trying to influence a procurement decision improperly."),
           ("Testimonial", "A client's quote endorsing the supplier.")],
    code=dict(file="marketing/lodestar-case-study-v3.md", note="approved Wed 6 Jun 2029 · HOLD until after the phase 2 award", src="""
CASE STUDY v3 · approved: Elaine Corbett, Anjali Rao (§18) · HOLD: after the phase 2 award

headline   Lodestar wave 1: 379,997 customers, one long night, and what we learned
hard parts 7.8 % data-quality surprise → CR-007 (£700k, +3 months)
           first red status (#38) → plan v2.3, velocity 38
           M3 rejected 23 Jun 2028 → accepted 3 Jul (0.3 %)
           04:10 MetroBus queue full → 22 minutes → live 07:40
           3 accounts excluded → handled manually
quotes     Elaine: "They told us bad news early, every time. That's why we got there."
           Kemi:   "They sat on their hands while we fixed it. Then we didn't need them."
meanwhile  anonymised summary (approved) for other bids · references after the award
"""),
    contract=dict(side="who owns the story", doc="Lodestar SOW · §18 (publicity) · ITT §4", date="signed 30 June 2027", stamp="held",
                  clauses=[("18.1", "Neither Party shall make any public announcement concerning this Agreement without the prior written consent of the other.", "written consent: Elaine and Anjali, 6 June."),
                           ("ITT 4.3", "Bidders shall not seek to influence the evaluation by publicity or by contact with MetroVolt staff.", "so: approved now, published after the award.")],
                  plain="publicity clauses are common and strict. Ask early, agree the words in writing, and never publish anything about the client during a procurement you're in."),
    health=dict(now="g",
                g=("a story both sides own", ["Approved text.", "Hard parts in.", "Published at the right time."]),
                a=("a live procurement", ["Approve now, publish later.", "Anonymise meanwhile.", "References after the award."]),
                r=("a claim the client disputes", ["Withdraw it.", "Apologise.", "Rewrite it together."])),
    pressure=dict(level=2, title="the story", cost="two other bids without the logo · Graham's patience",
                  items=["“Flawlessly” would be read by Elaine, Kemi and Bert. They were there.", "A month's wait costs little; a lobbying complaint during phase 2 could cost everything."]),
    baseline="Each line compares <b>a “flawless” case study published now</b> with <b>an honest one, written with the client, approved, and held until after the award</b>.",
    ratings=[(1, 5, "Elaine trusts the story; her quote is in it."),
             (3, 4, "The team's real work recognised."),
             (3, 3, "Two bids use an anonymised version."),
             (3, 3, "Neutral."),
             (3, 4, "The facts are right."),
             (1, 4, "No procurement or contract risk."),
             (2, 5, "§18 consent in writing."),
             (3, 2, "Published later."),
             (3, 3, "Three drafts.")],
    pitfalls=[("Publishing without consent", "A contract breach.", "ask, in writing."),
              ("“Flawlessly”", "Nobody believes it; the client minds.", "the hard parts."),
              ("Publishing during a procurement", "Looks like lobbying.", "hold it."),
              ("Writing it alone", "The client's corrections arrive in public.", "together."),
              ("No anonymised version", "Other bids go without.", "approve one meanwhile.")],
    grimoire=[(4, "book-of-deeds", "The Book of Deeds", "is the inside version: recording your work so it's recognised, truthfully.")],
    use=["After a successful project.", "When a client offers to be a reference.", "Before using a client's name anywhere."],
    skip=["During a live procurement with that client (hold it)."],
    related=["<b>Who Will Vouch for Us?</b> (vol. 1)", "<b>How Do We Run a Lessons Session Both Sides Attend?</b> (this volume)", "<b>What If the Client Asks Us to Change the Numbers?</b> (vol. 5)", "<b>Presenting to Executives</b> (Ana, vol. 3)"],
    quiz=[("What did Graham want?", "A case study now, with MetroVolt's logo, headlined “380,000 customers migrated flawlessly”."),
          ("What does §18 require?", "Prior written consent for any public announcement."),
          ("Why hold it until after the award?", "Publishing during the procurement could look like influencing the evaluation."),
          ("Name two hard parts in the case study.", "CR-007, the red status, M3 rejected, the 22-minute queue, the excluded accounts."),
          ("What's the final headline?", "“Lodestar wave 1: 379,997 customers, one long night, and what we learned.”")],
    quiz_sit=[("A trade magazine calls Ines in late May asking about Lodestar. What does she say?", "That she can't comment on a client's project without their consent, and that there may be a case study later. Then tell Elaine about the call.")],
    try_it="Take a project you're proud of. Write the case study's three hardest moments and what fixed them. Who would need to approve it? Does your contract say?",
    remember="It's <span class=\"hl\">the client's story too</span>. Ask, tell the hard parts, and <span class=\"hl\">never publish during a procurement</span>.",
    late=dict(when="Wed 16 May 2029 · 21:00 · Leeds",
              lines=["Graham wanted “flawlessly”. We've settled on “one long night”. He says it's worse marketing. I think it's better.",
                     "Elaine will edit it. Anjali will change six words. It goes out after the award.",
                     "Twenty-nine days to the decision. Not counting. Much."]),
    sources=["David Maister, <i>Managing the Professional Service Firm</i> (1993): reputation.",
             "UK Cabinet Office, <i>Model Services Contract</i>: publicity clauses.",
             "Ann Handley, <i>Everybody Writes</i> (2nd ed., 2022)."],
)

# ------------------------------------------------------------------ 12 When Should We Walk Away?
wk_problem = Doodle(760, 240, "Doodle of MetroVolt's best and final offer request, 24 May 2029, from Rupert's office through Desmond: cut the price by 12 per cent, and accept that the supplier absorbs all data quality risk, with unlimited liability for data errors. The word absorb, which Ines removed from the first contract in June 2027, is back.",
                    "−12 %, “absorb” all data risk, and unlimited liability. The word is back.", exact=True)
for i, (t, fill) in enumerate([("price −12 %", "pink"), ("“absorb” data risk", "pink"), ("unlimited liability", "pink")]):
    wk_problem.box(14 + i * 250, 30, 232, 90, t, fill, size=19)
wk_problem.note(380, 180, "“absorb”: last seen in draft v0.3, June 2027", "red", size=18)

wk_how = Doodle(760, 340, "The walk-away test. Four conditions, written on 14 February, before the bid: margin no lower than 15 per cent; liability capped at the contract value; no supplier absorbing data quality risk; a plan at 85 per cent capacity. The request fails three of four. The answer: decline the three, offer alternatives, 4 per cent off by moving the business portal into wave 4 and a shared data-quality pot, and state plainly that Wrenfield would rather withdraw than sign those terms. Graham signs it.",
                "Conditions set in February, tested calmly in May, and a polite letter ready to walk.", exact=True)
for i, (h, ok) in enumerate([("margin ≥ 15 %", False), ("liability capped", False), ("no “absorb”", False), ("plan at 85 %", True)]):
    wk_how.box(14 + i * 186, 20, 174, 90, h, "green" if ok else "pink", sub="pass" if ok else "fails", size=18, subsize=14)
wk_how.box(14, 140, 732, 80, "answer: decline 3 · offer −4 % (portal → wave 4, shared data pot) · would rather withdraw", "y", size=16)
wk_how.note(380, 280, "Graham: “Send it. I mean it.”", "pen", size=19)

WALKING_AWAY = dict(
    slug="walking-away", date=date(2029, 5, 31), meta=on_site(date(2029, 5, 31)), where="LEEDS", pass_kind="contractor",
    kicker="a.k.a. when to walk away from a client",
    tldr="The time to decide what you won't accept is <b>before you want the deal</b>. Write <b>walk-away conditions</b> early (margin floor, liability, risk you won't absorb, a pace you won't break), <b>test every new demand against them calmly</b>, offer <b>real alternatives</b>, and if the deal still fails, <b>leave politely</b>, in writing, with the door open. Walking away from the wrong deal is part of winning the right ones.",
    chips=[("Family", "the next deal"), ("Lives in", "bids/metrovolt-phase2/walk-away.md · BAFO reply"), ("Pairs with", "the bid / no-bid (vol. 1), BAFO (vol. 1), saying no (vol. 5)")],
    problem_side="Leeds, 31 May 2029",
    problem="""  <p class="lead">On <b>Thursday 24 May</b>, Desmond sends both bidders a <b>best and final offer</b> request. It carries Rupert's office's fingerprints:</p>
  <ul>
    <li>Reduce the price by <b>12 %</b>.</li>
    <li>The supplier shall <span class="hl-pink">“absorb all risk arising from the quality of customer data”</span>.</li>
    <li><b>Unlimited liability</b> for errors in migrated data.</li>
  </ul>
  <p>“Absorb” is the word Ines had removed from draft v0.3 of the first contract in June 2027. Replies are due <b>Friday 1 June</b>. Graham badly wants phase 2.</p>""",
    problem_figs=[wk_problem],
    sides=dict(client=("Rupert's office and Desmond", "<p>Rupert's office wants a cheaper, lower-risk phase 2 for MetroVolt, and perhaps a test of which bidder will bend furthest. Desmond has to put the same request to both bidders and record the answers. Elaine wasn't consulted on the wording.</p>", "Let's see who wants it most."),
                vendor=("Ines, Callum and Graham", "<p>At 12 % off, the margin is about 4 %. Unlimited liability for data errors, on 1.9 million accounts already known to be messy, could sink an 80-person firm. Wrenfield needs phase 2. It needs to still exist more.</p>", "We decided this in February, when we were calm.")),
    sides_after="Demands at the last minute are a test of nerve. Conditions written in calm weather are how you pass it.",
    analogy_side="the house you'd love to buy",
    analogy="""  <p>Sensible house-buyers decide their <b>top price before the viewing</b>, because after you've seen the garden you'll want to pay anything. When the seller's agent rings at the last minute asking for £30,000 more and the buyer to pay for the new roof, they check the number they wrote down, make a fair counter-offer, and are ready to <b>say no and keep looking</b>. Sometimes the seller comes back. Sometimes they don't, and that was the right house to lose.</p>""",
    map=[("Top price decided before the viewing", "Walk-away conditions, 14 February"),
         ("The garden", "Two years of Lodestar, and Graham's pipeline"),
         ("The last-minute call", "The BAFO request"),
         ("A fair counter-offer", "−4 %, portal to wave 4, a shared data pot"),
         ("Ready to keep looking", "“We would rather withdraw”")],
    how_side="conditions in calm weather, a calm test, alternatives, a polite letter",
    how="""  <p><b>Conditions set in calm weather.</b> On <b>14 February</b>, before the bid, Ines, Callum and Graham wrote four walk-away conditions and all three signed them: margin <b>no lower than 15 %</b>; liability <b>capped at the contract value</b>; Wrenfield <b>never absorbs data-quality risk</b> alone; a plan at <b>85 %</b> of capacity.</p>
  <p><b>A calm test.</b> On 30 May they test the request against them, one line each. It fails <b>three of four</b>.</p>
  <p><b>Real alternatives.</b> The reply offers what Wrenfield can do: <b>4 % off</b>, by moving the business self-service portal into wave 4 and reusing wave 1's reconciliation tools; a <b>shared data-quality pot</b> (£400k, drawn down jointly, with the rules from CR-007); liability capped at the contract value, as in wave 1.</p>
  <p><b>Ready to leave, politely.</b> The last paragraph: <i>“We would rather withdraw than accept unlimited liability or absorb data-quality risk alone. We would be sorry to do so; wave 1 has been the best work our firm has done, and we'd hand it over carefully whoever delivers phase 2.”</i></p>
  <p>Graham reads it twice in Leeds on Thursday 31 May, says <b>“Send it. I mean it.”</b>, and signs it. Submitted Friday at 10:15. Desmond's reply on 4 June: <i>“Received. Noted.”</i> Nothing else. They don't know what Vexmoor answered.</p>""",
    how_figs=[wk_how],
    steps=[("Write walk-away conditions early", "Before you want the deal; signed by the boss."),
           ("Test each demand calmly", "One line each: pass or fail."),
           ("Offer real alternatives", "What you can do, priced."),
           ("Say clearly what you won't do", "And why."),
           ("Be ready to withdraw", "Politely, in writing."),
           ("Leave the door open", "Offer a careful handover either way.")],
    vocab=[("Walk-away conditions", "Terms agreed in advance that would make you decline a deal."),
           ("BATNA", "Best alternative to a negotiated agreement: what you'll do if this fails."),
           ("BAFO", "Best and final offer, requested late in a procurement."),
           ("Unlimited liability", "No cap on what the supplier might owe for failures."),
           ("Risk transfer", "Moving a risk from one party to another by contract."),
           ("Winner's curse", "Winning by accepting terms that make the deal a loss.")],
    code=dict(file="bids/metrovolt-phase2/walk-away.md", note="written Wed 14 Feb · tested Wed 30 May 2029", src="""
WALK-AWAY CONDITIONS · phase 2 · signed 14 Feb 2029 (Ines, Callum, Graham)

                                      BAFO request (24 May)
1  margin ≥ 15 %                       −12 % → ≈ 4 %             FAIL
2  liability capped at contract value  unlimited (data errors)   FAIL
3  never absorb data-quality risk      "absorb all risk …"       FAIL
4  plan at 85 % capacity               unaffected                PASS

reply (Fri 1 Jun, 10:15)  −4 % (business portal → wave 4; reuse reconciliation tools)
                          shared data-quality pot £400k (CR-007 rules) · liability cap as wave 1
                          "we would rather withdraw than …" · careful handover either way
Graham     "Send it. I mean it."
Desmond    4 Jun: "Received. Noted."
"""),
    contract=dict(side="the word that came back", doc="Phase 2 BAFO request · clause 7 (as drafted) · redline", date="received 24 May 2029", stamp="declined",
                  clauses=[("7.1", "The Supplier shall <s>absorb all risk arising from the quality of customer data</s> <i>share data-quality risk through a joint pot of £400,000, drawn down under the rules of CR-007</i>.", "June 2027, draft v0.3: same word, same answer."),
                           ("7.4", "The Supplier's liability <s>for errors in migrated data shall be unlimited</s> <i>shall be capped at the Contract Value</i>.", "unlimited liability is a bet-the-firm clause. we're 80 people.")],
                  plain="late requests to absorb risk or remove liability caps are common in BAFOs. Answer with a redline, a priced alternative and a calm statement of what you won't sign."),
    health=dict(now="r",
                g=("a fair BAFO", ["Sharpen within the conditions.", "Small concessions.", "Sign."]),
                a=("one condition under pressure", ["Offer alternatives.", "Explain the line.", "Escalate inside the firm."]),
                r=("several conditions fail", ["Decline in writing.", "Offer what you can.", "Be ready to withdraw."])),
    pressure=dict(level=5, title="the walk-away", cost="£9m of work · two years of relationship · Graham's nerve",
                  items=["The conditions were written in February for exactly this afternoon. Without them, the BAFO would have been negotiated by fear.", "Rupert's office may have sent the same request to Vexmoor to see who bends. Not bending is also an answer."]),
    baseline="Each line compares <b>accepting the BAFO to win</b> with <b>testing it against walk-away conditions, offering alternatives and being ready to withdraw</b>.",
    ratings=[(3, 3, "Elaine respects it; Rupert's office may not."),
             (2, 4, "No impossible phase 2 for the team."),
             (1, 4, "Margin protected (or no deal)."),
             (3, 4, "The shared pot keeps the rules clear."),
             (3, 3, "Neutral."),
             (1, 5, "No bet-the-firm liability."),
             (3, 4, "Reply in writing, redlined."),
             (3, 3, "A week."),
             (3, 3, "One page of conditions.")],
    pitfalls=[("No conditions in advance", "Fear negotiates for you.", "write them in calm weather."),
              ("Conditions only you know", "The boss overrules you at 17:00.", "signed by the boss."),
              ("Just saying no", "Looks like sulking.", "alternatives, priced."),
              ("Threatening to withdraw", "Sounds like a bluff.", "a polite statement, and mean it."),
              ("Burning the bridge", "Wave 1 still needs you.", "offer a careful handover.")],
    grimoire=[(6, "banishing-client", "Banishing a Client", "is the same decision inside MetroVolt's own supplier world: when a relationship costs more than it gives."), (8, "word-of-power-no", "The Word of Power: No", "is the craft of the sentence that ends the letter.")],
    use=["Before any bid you badly want.", "BAFOs and late demands.", "When liability or risk moves at the last minute."],
    skip=["Never skip writing the conditions."],
    related=["<b>Should We Even Bid?</b> (vol. 1)", "<b>What Do We Give Away in the Final Offer?</b> (vol. 1)", "<b>How Do We Say No to a Client?</b> (vol. 5)", "<b>Leaving a Vendor</b> (Eli, vol. 5)"],
    quiz=[("When were the walk-away conditions written, and by whom?", "14 February 2029, by Ines, Callum and Graham, all signed."),
          ("Which conditions did the BAFO fail?", "Margin, liability cap, and absorbing data-quality risk."),
          ("What alternatives did Wrenfield offer?", "4 % off (portal to wave 4), a shared £400k data-quality pot, liability capped at contract value."),
          ("What did the last paragraph say?", "Wrenfield would rather withdraw than accept those terms, and would hand over carefully either way."),
          ("What was Desmond's reply?", "“Received. Noted.”")],
    quiz_sit=[("On Friday at 09:30, Vivian rings: “Just agree to the 12 %, we'll fix it in change requests.” What does Ines say?", "No: that's the plan the conditions exist to stop, and pricing below cost to recover it in change requests is the Orion story. The reply is signed by Graham and goes at 10:15.")],
    try_it="For a deal or decision you want badly, write three walk-away conditions now, while you're calm. Who should sign them with you?",
    remember="Decide what you won't accept <span class=\"hl\">before you want the deal</span>. Then test calmly, offer what you can, and <span class=\"hl\">be ready to leave politely</span>.",
    late=dict(when="Thu 31 May 2029 · 21:30 · Leeds",
              lines=["“Absorb” came back. Same word as June 2027. Same answer, with Graham's signature this time.",
                     "He read it twice and said “Send it. I mean it.” I think he did.",
                     "We might have just lost phase 2. We definitely just kept the firm. Fifteen days."]),
    sources=["Roger Fisher, William Ury and Bruce Patton, <i>Getting to Yes</i> (3rd ed., 2011): BATNA.",
             "Chris Voss, <i>Never Split the Difference</i> (2016).",
             "UK Cabinet Office, <i>Sourcing Playbook</i> (2021): risk allocation and liability."],
)

NOTES = [PHASE2_BID, WIN_OR_LOSE, CASE_STUDY, WALKING_AWAY]
