# Series 5 · On the Client's Floor · Vol. 3 · Digging Up the Legacy · A plan that survives (notes 13–15).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 13 How Do We Move 380,000 Customers?
mw_problem = Doodle(760, 240, "Doodle of 380,000 customers drawn as a crowd that has to cross a bridge in one night, the night of 23 September 2028. Nobody has done it before at MetroVolt. Nobody has practised. On the far side, an empty exception desk.",
                    "380,000 customers, one night, a bridge nobody has crossed before.", exact=True)
for i in range(30):
    mw_problem.circle(30 + (i % 10) * 22, 60 + (i // 10) * 30, 8, "y")
mw_problem.line("M260 150 Q 380 60 500 150", color="")
mw_problem.line("M260 150 H500", thin=True)
mw_problem.box(540, 60, 200, 110, "exception desk", "paper", sub="staffed by: ?", size=18, subsize=15)
mw_problem.note(380, 210, "unpractised, one night, all at once", "red", size=20)

mw_how = Doodle(760, 340, "The migration plan for wave 1. First, a pilot: Ashgrove, 20,000 accounts including 340 staff households, on 5 June 2028. Then three full dress rehearsals of wave 1 on copies of production data, in April, July and August, each timed and reconciled. An exception queue for records the migration can't move automatically, staffed by twelve Customer Ops people trained in May. A reconciliation report for every run. And a rollback point on the night.",
                "A pilot, three rehearsals, a staffed exception queue, a reconciliation each time.", exact=True)
for i, (h, sub, fill) in enumerate([("pilot", "20,000 · 5 Jun", "green"), ("rehearsal 1", "April", "y"), ("rehearsal 2", "July", "y"), ("rehearsal 3", "August", "y"), ("wave 1", "Sat 23 Sep", "pink")]):
    mw_how.box(14 + i * 148, 20, 138, 90, h, fill, sub=sub, size=18, subsize=13)
    if i:
        mw_how.arrow(14 + i * 148 - 8, 65, 14 + i * 148 - 1, 65)
mw_how.box(14, 140, 360, 90, "exception queue", "blue", sub="12 Customer Ops staff, trained in May", size=19, subsize=15)
mw_how.box(386, 140, 360, 90, "reconciliation", "paper", sub="counts, balances, debt · every run", size=19, subsize=15)
mw_how.note(380, 290, "by the night, the night should be the fourth time", "pen", size=19)

WAVES = dict(
    slug="migration-waves", date=date(2028, 1, 25), meta=on_site(date(2028, 1, 25)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “data migration rehearsals” and the pilot",
    tldr="A big migration should be the <b>fourth time</b> you've done it, not the first. Start with a <b>pilot</b> on a small, friendly group; run full <b>dress rehearsals</b> on copies of real data, timed; send what the automation can't handle to a <b>staffed exception queue</b>; and <b>reconcile</b> counts and balances after every run. Then the night is just another rehearsal, with customers.",
    chips=[("Family", "a plan that survives"), ("Lives in", "migration/wave1-plan.md"), ("Pairs with", "the strangler plan, cutover planning (vol. 4)")],
    problem_side="The Grid, January 2028",
    problem="""  <p class="lead">Baseline v2.0 is nearly agreed: wave 1, <b>380,000 accounts</b>, moves on the night of <b>Saturday 23 September 2028</b>. Callum's first migration plan has one line for it: “Wave 1 cutover, 23 Sep.”</p>
  <ul>
    <li>MetroVolt has never migrated customers between systems. Neither has anyone currently at MetroVolt.</li>
    <li>The profile says <b>117,800</b> wave 1 records fail the address check. After cleansing, thousands will still need a person.</li>
    <li><span class="hl-pink">Nobody has said who those people are.</span></li>
  </ul>""",
    problem_figs=[mw_problem],
    sides=dict(client=("Customer Ops", "<p>For Customer Operations, migration night is the night their customers' accounts move. If it goes wrong, the phones ring on Monday. They want it boring, and they want to know which of their staff will be working that weekend.</p>", "Make it boring, and tell us who's working."),
                vendor=("Oskar and Bilal", "<p>For Wrenfield, the migration is the moment the fixed price is judged. An unrehearsed night is a gamble on 380,000 accounts. Rehearsals cost time and environments; not rehearsing costs much more.</p>", "The night should be the fourth time we've done it.")),
    sides_after="Rehearsals feel expensive until the night. Then they're the cheapest thing you did.",
    analogy_side="the theatre's dress rehearsals",
    analogy="""  <p>A theatre doesn't open with the first full run-through. It does <b>technical rehearsals</b>, then <b>dress rehearsals</b> with costumes and lights, timed, then a <b>preview</b> for a friendly audience. When something goes wrong, the stage manager has a person ready in the wings. By opening night, the show has run four times.</p>""",
    map=[("The preview audience", "The pilot: Ashgrove, with 340 staff households"),
         ("Dress rehearsals", "Three full runs on copies of real data"),
         ("Timed, with costumes and lights", "Timed end to end, with the real 02:10 job"),
         ("A person in the wings", "The exception queue, staffed"),
         ("Opening night", "Saturday 23 September 2028")],
    how_side="a pilot, three rehearsals, a staffed queue, a reconciliation",
    how="""  <p><b>A pilot.</b> <b>Ashgrove</b>, 20,000 accounts in the Northern district, including <b>340 staff households</b> who'll report problems kindly and fast. Live on <b>Monday 5 June 2028</b>, with the full process.</p>
  <p><b>Three dress rehearsals</b> of the whole of wave 1 on copies of production data: <b>April, July and August</b>. Each is timed end to end, including the 02:10 job and the Halvorsen file. Each must finish inside the window, or the plan changes.</p>
  <p><b>An exception queue.</b> Records the migration can't move automatically (an address it can't resolve, a duplicate it can't merge) go to a queue with the reason. <b>Twelve Customer Ops staff</b>, chosen by Priya's team, are trained in May. Target for the night: under 0.5 % of accounts.</p>
  <p><b>A reconciliation report every run</b>: account counts, balances and open debt, MAVIS against Lodestar, per area. Any unexplained difference fails the rehearsal. The report is a go / no-go criterion.</p>""",
    how_figs=[mw_how],
    steps=[("Pick a small, friendly pilot group", "Staff households help."),
           ("Rehearse the whole thing, timed", "Copies of real data, the real batch."),
           ("Three rehearsals, at least", "The last one close to the night."),
           ("Design the exception queue", "Reasons, screens, who works it."),
           ("Train the people early", "Months, not days, before."),
           ("Reconcile every run", "Counts, balances, debt; differences fail the run.")],
    vocab=[("Data migration", "Moving data from one system to another, usually with transformation."),
           ("Dress rehearsal", "A full, timed run of the migration on a copy of real data."),
           ("Pilot", "A first live migration of a small group."),
           ("Exception queue", "Records needing a person, with the reason."),
           ("Migration window", "The time available to migrate without disrupting customers."),
           ("Reconciliation report", "Proof that counts and totals match after the run.")],
    code=dict(file="migration/wave1-plan.md", note="v1 · Tue 25 Jan 2028", src="""
WAVE 1 MIGRATION PLAN (baseline v2.0)

pilot          Ashgrove · 20,000 accounts (340 staff households) · live Mon 5 Jun 2028
rehearsals     R1 Sat 15 Apr · R2 Sat 15 Jul · R3 Sat 26 Aug (copies of production)
               each: timed end to end, incl. 02:10 job + Halvorsen file
               window: Sat 18:00 → Sun 08:00 (14 h); must finish in 11 h
exceptions     queue with reason codes (ADDR, DUP, METER, PSR, OTHER)
               12 Customer Ops staff (chosen by Customer Ops), trained May
               target on the night: < 0.5 % of accounts (< 1,900)
reconciliation every run: account count · balances · open debt · per area
               unexplained difference = run failed = go / no-go criterion
"""),
    contract=dict(side="what the milestones require", doc="Lodestar SOW · Schedule 4 (M3, M4) · baseline v2.0", date="v2.0 · Feb 2028", stamp="rehearsed",
                  clauses=[("M3", "Pilot live: 20,000 accounts migrated; balances reconcile 100 %; ≤ 0.5 % of records in the exception queue; two billing cycles on Halvorsen.", "the pilot is a milestone with criteria, not a trial run."),
                           ("Sch. 4, 2.2", "<ins>Wave 1 shall not proceed unless the final dress rehearsal meets the M4 criteria.</ins>", "added at our request. it protects both sides.")],
                  plain="tie rehearsals to the milestone criteria. A rehearsal that fails the criteria stops the wave, which turns “should we rehearse?” into “we have to pass”."),
    health=dict(now="a",
                g=("trust is high", ["Rehearse anyway.", "Share every reconciliation.", "Celebrate a dull rehearsal."]),
                a=("first migration for the client", ["Pilot with friendly users.", "Three rehearsals, timed.", "Their staff in the exception queue."]),
                r=("pressure to skip rehearsals", ["Make the last rehearsal a criterion.", "Show what a failed night costs.", "Never skip reconciliation."])),
    pressure=dict(level=3, title="one night, 380,000 accounts", cost="three Saturday rehearsals · twelve people trained",
                  items=["Rehearsals take three Saturdays from the team. Plan rest after each; you'll need them fresh in September.", "Ask Customer Ops to choose the exception-queue people. They know who stays calm."]),
    baseline="Each line compares <b>“wave 1 cutover, 23 Sep” as one line</b> with <b>a pilot, three timed rehearsals, a staffed exception queue and reconciliation every run</b>.",
    ratings=[(3, 4, "Customer Ops sees its people and its customers protected."),
             (3, 3, "Three Saturdays of rehearsal."),
             (3, 4, "Failures found in rehearsal cost less."),
             (3, 4, "What “done” means on the night is written."),
             (3, 4, "The design is tested at full size."),
             (2, 5, "Four runs before the real one."),
             (3, 4, "A reconciliation report for every run."),
             (2, 2, "Months of preparation."),
             (3, 3, "Rehearsals need environments and people.")],
    pitfalls=[("The night as the first full run", "Every surprise happens live.", "three dress rehearsals."),
              ("Rehearsing on fake data", "Real data's oddities are missed.", "copies of production."),
              ("Untimed rehearsals", "The night runs over.", "time end to end."),
              ("An unstaffed exception queue", "Records wait for nobody.", "trained people, named."),
              ("Reconciling totals only", "Errors cancel out.", "per area, per measure.")],
    use=["Any migration of customer or financial records.", "First-time migrations for a client.", "Large volumes in a short window."],
    skip=["A small migration you can verify by hand afterwards."],
    related=["<b>How Do We Strangle a Customer System?</b> (this volume)", "<b>What Happens on the Night?</b> (vol. 4)", "<b>How Will We Know It's Done?</b> (vol. 2)", "<b>Did the Handover Work?</b> (Eli, vol. 6)"],
    quiz=[("Why a pilot with staff households?", "They report problems kindly and fast, and the group is small."),
          ("How many dress rehearsals, and on what data?", "Three, on copies of production data, timed end to end."),
          ("What is the exception queue?", "Records the automation can't migrate, with reasons, worked by trained people."),
          ("What makes a rehearsal fail?", "Any unexplained reconciliation difference, or running over the window."),
          ("Who chose the exception-queue staff?", "Customer Ops.")],
    quiz_sit=[("Rehearsal 2 finishes in 12 hours 40 minutes against an 11-hour target. What happens?", "The plan changes: find the slow steps, parallelise or move work earlier, and prove it in rehearsal 3. Wave 1 doesn't proceed unless the final rehearsal meets the criteria.")],
    try_it="Pick a big change you'll make in one go. Plan a pilot group, at least two rehearsals and a check after each. Who handles what the automation can't?",
    remember="The night should be <span class=\"hl\">the fourth time</span>, not the first. Rehearse, staff the exceptions, <span class=\"hl\">reconcile every run</span>.",
    late=dict(when="Tue 25 January 2028 · 21:45 · hotel near The Grid",
              lines=["Callum's plan had one line for wave 1. Now it has a pilot, three rehearsals and twelve named people.",
                     "Priya's team chose the exception-queue staff. One of them asked if she could bring her own headset. Yes.",
                     "Ashgrove has 340 staff households. If anyone's bill goes wrong in June, I'll hear about it in the lift."]),
    sources=["Johny Morris, <i>Practical Data Migration</i> (3rd ed., 2020).",
             "Philip Russom, <i>Best Practices in Data Migration</i> (TDWI, 2006).",
             "Atul Gawande, <i>The Checklist Manifesto</i> (2009)."],
)

# ------------------------------------------------------------------ 14 What If the Client Overrules Our Design?
ov_problem = Doodle(760, 240, "Doodle of the design authority on 19 January 2028. Hana's proposal: log-based change capture for nine core tables, about 40 seconds' delay, with an 85,000-pound-a-year licence. Hollis's decision: no new licence; use MetroBus, MetroVolt's integration bus from 2014, with batch adapters every 15 minutes. Hana's face.",
                    "Hana's 40 seconds, or Hollis's 15 minutes on MetroBus. Hollis chairs.", exact=True)
ov_problem.box(24, 40, 300, 120, "Hana", "blue", sub="log capture · 40 s · £85k/yr", size=21, subsize=15)
ov_problem.box(436, 40, 300, 120, "Hollis", "y", sub="MetroBus (2014) · 15 min · £0", size=21, subsize=15)
ov_problem.note(380, 100, "vs", "red", size=26)
ov_problem.note(380, 210, "the client's architect chairs the design authority", "pen", size=19)

ov_how = Doodle(760, 320, "Disagree and commit. One: disagree in writing before the decision, with facts: what each option costs and what each risks. Two: when the decision is made, record it in an architecture decision record, ADR-0019, with Wrenfield's dissent and the risks it accepts, signed by Hollis. Three: commit fully and make MetroBus work, with monitoring and a test of the 15-minute delay in the pilot. Four: no told-you-so, ever.",
                "Disagree in writing, record the decision and the dissent, then make their choice work.", exact=True)
for i, (h, sub, fill) in enumerate([("disagree", "in writing, before", "y"), ("record", "ADR-0019 + dissent", "blue"), ("commit", "make MetroBus work", "green"), ("no told-you-so", "ever", "pink")]):
    ov_how.box(14 + i * 186, 30, 174, 110, h, fill, sub=sub, size=19, subsize=14)
ov_how.box(14, 170, 732, 90, "what it cost", "paper", sub="+3 weeks to integrate · 15-minute delay accepted for wave 1 · −£85k a year for MetroVolt", size=19, subsize=15)

OVERRULED = dict(
    slug="overruled", date=date(2028, 1, 19), meta=on_site(date(2028, 1, 19)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. “disagree and commit”, on the vendor side",
    tldr="The client owns its architecture, and sometimes it will overrule your design for reasons you don't fully share: standards, cost, people. <b>Disagree in writing</b> before the decision, with costs and risks. When it's made, <b>record it</b> (with your dissent and the risks accepted) and <b>commit</b>: make their choice work as if it were yours. Never say “I told you so”. A vendor that sulks gets replaced.",
    chips=[("Family", "a plan that survives"), ("Lives in", "design/adr/0019-change-capture-metrobus.md"), ("Pairs with", "mainframe integration, design authority day")],
    problem_side="The Grid, design authority, 19 January 2028",
    problem="""  <p class="lead">At the design authority on <b>Wednesday 19 January</b>, Hana proposes <b>log-based change capture</b> for the nine core tables: about <b>40 seconds</b> of delay, a licence of about <b>£85k a year</b>. Hollis says no.</p>
  <ul>
    <li>MetroVolt has an integration bus, <b>MetroBus</b>, bought in 2014. Hollis's rule: no new integration licences while MetroBus can do the job.</li>
    <li>MetroBus can poll MAVIS every <b>15 minutes</b> with batch adapters. Slower, but it's MetroVolt's standard, and MetroVolt's team can support it after Wrenfield leaves.</li>
    <li>Hana is furious. <span class="hl-pink">It was her idea since the bid, and it worked in the spike.</span></li>
  </ul>""",
    problem_figs=[ov_problem],
    sides=dict(client=("Hollis", "<p>Hollis has to support whatever Lodestar leaves behind, with a small team, for years. Every new tool is another licence, another skill, another thing that breaks at 3 a.m. after the vendor has gone. In a Horizon year, a new £85k licence is also a hard conversation upstairs.</p>", "I'll be running this long after you've left."),
                vendor=("Ines and Hana", "<p>Wrenfield thinks log capture is better: fresher data, less load on MAVIS. But 15 minutes is enough for wave 1, MetroBus is a real option, and Hollis chairs the design authority. The question isn't whether Wrenfield is right; it's how to disagree well, then deliver.</p>", "We can be right, or we can be useful. Ideally both, in that order.")),
    sides_after="Most overruled designs aren't wrong decisions, just different weights: the client values long-term support more than the vendor does, because the client stays.",
    analogy_side="the homeowner's choice of boiler",
    analogy="""  <p>A heating engineer recommends a modern heat pump. The homeowner chooses a boiler <b>their local plumber can service</b>. The good engineer writes down her advice and its reasons, then <b>installs the boiler properly</b>, the best boiler installation she's ever done. She doesn't fit it badly to prove a point, and she doesn't mention the heat pump every winter.</p>""",
    map=[("The heat pump", "Log-based change capture"),
         ("The boiler the plumber can service", "MetroBus, supported by MetroVolt's team"),
         ("Writing down her advice", "Wrenfield's dissent in ADR-0019"),
         ("Installing it properly", "Making MetroBus work, monitored and tested"),
         ("Not mentioning it every winter", "No told-you-so")],
    how_side="disagree in writing, record, commit",
    how="""  <p><b>Disagree in writing, before.</b> Hana's paper for the design authority already compared both options: delay, cost, load on MAVIS, who supports it. Ines adds one sentence: <i>“Wrenfield recommends log capture; MetroBus is viable for wave 1 if a 15-minute delay is acceptable to Customer Operations.”</i> Customer Ops confirms 15 minutes is fine.</p>
  <p><b>Record the decision.</b> Hollis decides MetroBus. It's written as <b>ADR-0019</b>: the decision, the options, the reasons (support, cost, standards), and <b>Wrenfield's dissent</b> with the risks MetroVolt accepts (15-minute delay; batch load on MAVIS, to be measured in the pilot). Hollis signs it. Decision log DL-028.</p>
  <p><b>Commit.</b> Hana builds the MetroBus adapters as if they were her idea, with monitoring of the delay and a load test in the pilot. It costs <b>three weeks</b>; it saves MetroVolt <b>£85k a year</b> and goes into CR-007's negotiation. Ines asks the team for one thing: nobody says “told you so”, ever, including if the pilot shows load problems.</p>
  <p>Two weeks later, Hollis asks Hana to present the MetroBus adapters to his own team as an example of how to use it well.</p>""",
    how_figs=[ov_how],
    steps=[("Compare options in writing beforehand", "Costs, risks, who supports it."),
           ("Make your recommendation clear", "And say when the other option is viable."),
           ("Let the owner decide", "Their architecture, their call."),
           ("Record the decision and the dissent", "An ADR, signed, with risks accepted."),
           ("Commit fully", "Build their choice as if it were yours."),
           ("Never say “told you so”", "Measure, report facts, move on.")],
    vocab=[("Design authority", "The forum that approves architecture decisions."),
           ("Architecture decision record (ADR)", "A short record of a decision, its context, options and consequences."),
           ("Dissent", "A recorded disagreement with a decision."),
           ("Disagree and commit", "Arguing your case, then fully supporting the decision made."),
           ("Enterprise standard", "A technology the client has chosen to use everywhere."),
           ("Supportability", "How easily the client's own team can run and fix a system.")],
    code=dict(file="design/adr/0019-change-capture-metrobus.md", note="decided 19 Jan 2028 · DL-028", src="""
ADR-0019 · Change capture for the 9 core MAVIS tables

status      decided (design authority, 19 Jan 2028) · decider: Hollis Wade
context     wave 1 needs MAVIS changes during coexistence (see Sch. 2 §4)
options     A log capture: ≈ 40 s · licence ≈ £85k/yr · new skill to support
            B MetroBus (2014) batch adapters: 15 min · £0 · MetroVolt team supports
decision    B. reasons: supportability after handover; enterprise standard;
            no new licence in 2028
dissent     Wrenfield recommended A (freshness, lower MAVIS load). Risks MetroVolt
            accepts: 15-minute delay (Customer Ops confirmed OK); batch load on MAVIS
            → measure in pilot; revisit for waves 2–4 if needed
consequence +3 weeks (CR-007 line 3: −£85k) · adapters monitored for delay
signed      Hollis Wade (MetroVolt) · Ines Duarte (Wrenfield)
"""),
    contract=dict(side="who decides architecture", doc="Lodestar SOW · Schedule 7, §3 (design authority)", date="v1.1 · Aug 2027", stamp="client's call",
                  clauses=[("3.1", "The Design Authority, chaired by MetroVolt's Head of IT Architecture, approves the architecture of the Solution.", "Hollis chairs. Hollis decides. that's the deal we signed."),
                           ("3.4", "<ins>Where the Supplier disagrees with a decision, its recommendation and the risks MetroVolt accepts shall be recorded with the decision.</ins>", "we added this in August. it's why the dissent is in ADR-0019, not in a grudge.")],
                  plain="the client usually owns architecture decisions. A clause that records the vendor's dissent and the risks accepted protects both sides: the client decides, and nobody can later claim the vendor didn't warn."),
    health=dict(now="g",
                g=("trust is high", ["Disagree in conversation, then record.", "Commit without fuss.", "Revisit later with data."]),
                a=("a strong-willed client architect", ["Options and costs in writing.", "ADR with dissent and accepted risks.", "Make their choice shine."]),
                r=("decisions you think are dangerous", ["Escalate the risk once, formally.", "Record everything.", "If it's unsafe, say so in writing and refuse to build that part."])),
    pressure=dict(level=3, title="losing the argument", cost="three weeks · one engineer's pride",
                  items=["Hana's anger is about care for the design. Acknowledge it before you ask her to commit.", "Losing a design argument gracefully earns more influence than winning one rudely."]),
    baseline="Each line compares <b>fighting the decision or building it half-heartedly</b> with <b>disagreeing in writing, an ADR with dissent, then full commitment</b>.",
    ratings=[(3, 5, "Hollis asks Hana to teach his team."),
             (3, 3, "Pride hurts, but the team moves on."),
             (3, 3, "Three weeks cost; £85k a year saved for MetroVolt."),
             (3, 4, "The decision and its trade-offs are written."),
             (4, 4, "MetroBus is a sound, supportable option."),
             (3, 4, "Accepted risks named and measured in the pilot."),
             (2, 5, "Dissent recorded, signed."),
             (3, 3, "Three weeks of rework."),
             (3, 4, "One standard tool for MetroVolt to run.")],
    pitfalls=[("Fighting after the decision", "You look like you're protecting your idea.", "disagree before; commit after."),
              ("Building it badly to prove a point", "You'll own the failure.", "make their choice work."),
              ("Dissent not recorded", "Later, nobody remembers you warned.", "an ADR, signed."),
              ("“Told you so”", "The relationship never recovers.", "report facts, never the gloat."),
              ("Silent compliance with something unsafe", "Real harm.", "refuse in writing if it's unsafe.")],
    grimoire=[(2, "know-it-all-basilisk", "The Know-It-All Basilisk", "is what a vendor becomes if it can't lose an argument: one glance and every idea but its own turns to stone.")],
    use=["The client overrules your recommended design.", "Standards or supportability outweigh technical preference.", "You disagree, but the choice is safe."],
    skip=["The decision is unsafe or unlawful: then disagree formally and don't build it."],
    related=["<b>How Do We Get Data Out of a Mainframe?</b> (this volume)", "<b>How Do We Get the Design Approved?</b> (next note)", "<b>Architecture Decision Records</b> (Ana, vol. 2)", "<b>Who Decides What, and Where?</b> (vol. 2)"],
    quiz=[("What does “disagree and commit” mean?", "Argue your case before the decision, then fully support the decision made."),
          ("What went into ADR-0019 besides the decision?", "The options, the reasons, Wrenfield's dissent, and the risks MetroVolt accepts."),
          ("Why did Hollis choose MetroBus?", "Supportability after the vendor leaves, an existing standard, and no new licence."),
          ("What did the decision cost and save?", "Three weeks of work; £85k a year of licence for MetroVolt."),
          ("When should you refuse instead of commit?", "When the decision is unsafe or unlawful.")],
    quiz_sit=[("In the pilot, MetroBus's batch load slows MAVIS's nightly run by 25 minutes. What do you report?", "The fact, the measurement and options (tune the polling, move it outside the batch window, or revisit log capture for waves 2–4), referencing the accepted risk in ADR-0019. No told-you-so.")],
    try_it="Think of a decision that went against your recommendation. Write it as an ADR: options, decision, reasons, your dissent and the risks accepted. Then list three things you'd do to make the chosen option work well.",
    remember="Disagree <span class=\"hl\">before</span>, in writing. Then make <span class=\"hl\">their choice</span> the best version of itself.",
    late=dict(when="Wed 19 January 2028 · 22:30 · hotel near The Grid",
              lines=["Hollis said no to log capture. MetroBus. 15 minutes. Hana left the room for ten minutes.",
                     "When she came back she said: “Fine. Then it'll be the best MetroBus adapter they've ever seen.”",
                     "Our dissent is in ADR-0019, signed by Hollis. That's all the being-right we need."]),
    sources=["Michael Nygard, “Documenting Architecture Decisions” (2011).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020).",
             "Kim Scott, <i>Radical Candor</i> (2017): disagree and commit."],
)

# ------------------------------------------------------------------ 15 How Do We Get the Design Approved?
da_problem = Doodle(760, 240, "Doodle of design authority day, 9 February 2028. Milestone M2, design approved, is worth 720,000 pounds. Six members around the table: Hollis in the chair, Kofi, MetroVolt security, the privacy office, MetroVolt's mainframe lead and Vexmoor's Bea as Horizon assurance. Wrenfield's first idea: a 60-slide deck.",
                    "M2 is worth £720k. Six people at the table, and a 60-slide deck in the queue.", exact=True)
da_problem.box(200, 70, 360, 100, "M2 · design approved", "y", sub="£720,000", size=22, subsize=18)
for i, n in enumerate(["Hollis", "Kofi", "security", "privacy", "mainframe", "Bea"]):
    da_problem.box(14 + i * 124, 196, 114, 36, n, "pink" if n == "Bea" else "paper", size=15, rx=18)
da_problem.box(600, 20, 146, 60, "60 slides?", "pink", size=18)

da_how = Doodle(760, 340, "Design authority day, as run. Two weeks before: a 20-minute pre-wire with each member, asking what they need to approve. One week before: a 9-page decision paper, not a deck, with the decision asked for, the design on one page, each member's concern and how it's met, and open points. On the day: 45 minutes, questions only. Outcome: approved with four conditions, each with an owner and a date: field-level encryption for priority services data, MetroBus delay monitoring, a performance test by July, and Kofi's sign-off on meter fields.",
                "Pre-wire each member, send a decision paper, leave with conditions you can meet.", exact=True)
for i, (h, sub, fill) in enumerate([("pre-wire", "20 min each · 2 wks before", "y"), ("decision paper", "9 pages · 1 wk before", "blue"), ("the meeting", "45 min · questions only", "green")]):
    da_how.box(14 + i * 250, 20, 232, 90, h, fill, sub=sub, size=19, subsize=14)
da_how.box(14, 140, 732, 40, "approved, with 4 conditions (owner · date)", "pink", size=18)
for i, t in enumerate(["PSR field encryption", "MetroBus delay alerts", "perf. test by July", "Kofi: meter fields"]):
    da_how.box(14 + i * 186, 190, 174, 60, t, "paper", size=15)
da_how.note(380, 300, "M2 accepted 9 Feb 2028 · £720,000 invoiced", "pen", size=19)

DESIGN_AUTHORITY = dict(
    slug="design-authority", date=date(2028, 2, 9), meta=on_site(date(2028, 2, 9)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. getting an architecture approved",
    tldr="A design authority approves designs it already understands and trusts. So <b>pre-wire</b>: meet each member beforehand and ask what they need to approve. Send a short <b>decision paper</b>, not a deck: the decision asked for, the design on one page, each member's concern and how it's met, and the open points. Use the meeting for <b>questions only</b>, and leave with <b>conditions</b> that each have an owner and a date.",
    chips=[("Family", "a plan that survives"), ("Lives in", "design/DA-2028-02-09-decision-paper.pdf · Schedule 2 v1.1"), ("Pairs with", "being overruled, the strangler plan, governance (vol. 2)")],
    problem_side="The Grid, 9 February 2028",
    problem="""  <p class="lead">Milestone <b>M2, design approved</b>, is worth <b>£720,000</b>: 15 % of the fixed price, and Wrenfield's cash for the spring. It needs the design authority to approve Schedule 2 v1.1 on <b>Wednesday 9 February 2028</b>.</p>
  <ul>
    <li>Six members: Hollis (chair), Kofi (metering), MetroVolt security, the privacy office, the mainframe lead, and <b>Bea from Vexmoor</b> as Horizon assurance.</li>
    <li>Callum's plan: a <b>60-slide deck</b>, presented in 90 minutes.</li>
    <li>Each member has a different worry. <span class="hl-pink">A deck answers none of them specifically.</span></li>
  </ul>""",
    problem_figs=[da_problem],
    sides=dict(client=("the six members", "<p>Each member approves on behalf of something they'll have to defend later: Hollis, the architecture; Kofi, the meters; security and privacy, the customers' data; the mainframe lead, MAVIS's nights. None of them wants to discover their concern in slide 47.</p>", "Show me my part, and how it's handled."),
                vendor=("Ines and Hana", "<p>Wrenfield needs approval, not applause, and approval comes from six separate yeses. A long presentation invites six separate “we'll need to think about it”s, and a second meeting in March.</p>", "Six private conversations, then one short public decision.")),
    sides_after="Approval meetings rarely change minds. They record decisions people have already reached, if you've helped them reach them.",
    analogy_side="the planning committee",
    analogy="""  <p>An architect applying for planning permission doesn't surprise the committee. She talks to the <b>planning officer</b>, the <b>neighbours</b> and the <b>conservation adviser</b> first, adjusts the drawings to answer their concerns, and submits a <b>short application</b> that shows each concern and how it's met. The committee meeting takes fifteen minutes and ends with conditions: “brick to match; no work on Sundays”.</p>""",
    map=[("The planning officer, neighbours, conservation adviser", "Hollis, Kofi, security, privacy, the mainframe lead, Bea"),
         ("Talking to them first", "Pre-wiring, 20 minutes each"),
         ("A short application", "The 9-page decision paper"),
         ("Each concern and how it's met", "One section per member"),
         ("Conditions: brick to match", "Four conditions, owners and dates")],
    how_side="pre-wire, a decision paper, questions only, conditions",
    how="""  <p><b>Pre-wire, two weeks before.</b> Ines and Hana meet each member for 20 minutes with one question: <i>“What do you need to see to approve this?”</i> Security: the priority-services encryption. Kofi: the meter fields in the back-feed. The mainframe lead: the MetroBus load on MAVIS's nights. Bea: the reconciliation design and the rollback.</p>
  <p><b>A decision paper, one week before</b>: nine pages, not sixty slides. Page 1: the decision asked for (“approve Schedule 2 v1.1”). Page 2: the design on one page. Pages 3–8: <b>one section per member</b>, their concern in their words and how the design meets it. Page 9: open points and proposed conditions.</p>
  <p><b>The meeting: 45 minutes, questions only.</b> No presentation. Hollis asks the members in turn. Bea asks two questions about rollback; Hana answers both from page 7.</p>
  <p><b>Approved with four conditions</b>, each with an owner and a date: field-level encryption for priority-services data (Hana, before the pilot); MetroBus delay alerts (MetroVolt IT, May); a performance test by July (Oskar); Kofi's sign-off on meter fields (Kofi, March). <b>M2 accepted on 9 February 2028; £720,000 invoiced.</b></p>""",
    how_figs=[da_how],
    steps=[("List every approver and their concern", "Ask; don't guess."),
           ("Pre-wire each one", "Twenty minutes, one question."),
           ("Write a decision paper", "Decision asked, design on a page, a section per concern."),
           ("Send it a week ahead", "Time to read, not to be surprised."),
           ("Use the meeting for questions", "No presentation."),
           ("Propose conditions you can meet", "Owners and dates, in the minutes.")],
    vocab=[("Decision paper", "A short document asking for a specific decision, with what's needed to make it."),
           ("Pre-wiring", "Talking to decision makers individually before the meeting."),
           ("Conditional approval", "Approval subject to listed conditions with owners and dates."),
           ("Milestone payment", "Money released when a defined milestone is accepted."),
           ("Schedule 2", "Lodestar's solution description in the contract."),
           ("Approval meeting", "The meeting that records a decision; ideally not where it's reached.")],
    code=dict(file="design/DA-2028-02-09-decision-paper.md", note="sent Wed 2 Feb 2028 · approved Wed 9 Feb", src="""
DESIGN AUTHORITY · 9 Feb 2028 · DECISION PAPER (9 pages)

p.1  decision asked: approve Schedule 2 v1.1 (milestone M2)
p.2  the design on one page (context, waves, router, back-feed, MetroBus, billing adapter)
p.3  Hollis      supportability → MetroBus (ADR-0019), standard tooling
p.4  security    PSR data → field-level encryption, 2 roles, access logged (S3)
p.5  privacy     DPIA passed 12 Jan; retention of MAVIS records 6 years (D2)
p.6  mainframe   MetroBus batch load → measured in pilot; outside 22:00–05:30 window
p.7  Bea         reconciliation per area nightly; rollback 14 days per wave
p.8  Kofi        meter fields in back-feed (COPYMTR) → his sign-off
p.9  open points + proposed conditions
outcome  APPROVED with 4 conditions (owners, dates) · DL-030 · M2 accepted · £720,000
"""),
    contract=dict(side="the milestone, and how it's accepted", doc="Lodestar SOW · Schedule 4 (M2)", date="baseline v2.0", stamp="M2 accepted",
                  clauses=[("M2", "Design approved: signed design authority minutes and Schedule 2 v1.0 or later.", "signed minutes, not a deck. Elaine insisted in June 2027."),
                           ("5.5", "<ins>Approval subject to conditions is acceptance of the Milestone where each condition has an owner and a date.</ins>", "without this, four conditions would have held up £720,000.")],
                  plain="make sure conditional approval counts as acceptance, as long as each condition has an owner and a date. Otherwise every condition becomes a reason to hold a payment."),
    health=dict(now="g",
                g=("trust is high", ["Short pre-wire, short paper.", "Approval in one meeting.", "Conditions agreed in advance."]),
                a=("several concerned approvers, an outside reviewer", ["Pre-wire every one.", "A section per concern.", "Questions only."]),
                r=("an approver looking for reasons to delay", ["Their concern answered on paper, in their words.", "Conditions instead of refusal.", "Minutes signed the same day."])),
    pressure=dict(level=3, title="£720,000 in one meeting", cost="six pre-wires · a paper rewritten twice",
                  items=["Pre-wiring feels political. It's simply asking people what they need before asking them to decide.", "Bea's questions were fair and answered on page 7. Write for the toughest reader in the room."]),
    baseline="Each line compares <b>a 60-slide presentation</b> with <b>pre-wiring, a 9-page decision paper and a questions-only meeting</b>.",
    ratings=[(3, 5, "Each member saw their concern answered."),
             (3, 4, "One meeting instead of two."),
             (2, 5, "M2 paid on the day."),
             (3, 4, "Conditions have owners and dates."),
             (3, 4, "The design was improved by six concerns."),
             (3, 4, "Open points listed, not hidden."),
             (3, 5, "Signed minutes, DL-030."),
             (3, 4, "Two weeks of preparation, 45 minutes of meeting."),
             (4, 4, "A paper, not a deck.")],
    pitfalls=[("A long deck", "Every concern buried somewhere.", "a decision paper with a section per concern."),
              ("No pre-wire", "Surprises in the meeting.", "twenty minutes with each member."),
              ("Presenting in the meeting", "Time for questions runs out.", "questions only."),
              ("Vague conditions", "Payment held indefinitely.", "owners and dates."),
              ("Ignoring the reviewer", "The outside voice derails it.", "answer their concern on paper too.")],
    grimoire=[(1, "meeting-before-the-meeting", "The Meeting Before the Meeting", "is the same move, inside MetroVolt, by the coffee machine on 27.")],
    use=["Any approval forum: design authority, architecture board, investment committee.", "Several approvers with different concerns.", "A payment depends on the decision."],
    skip=["A single approver you speak to daily."],
    related=["<b>What If the Client Overrules Our Design?</b> (previous note)", "<b>Who Decides What, and Where?</b> (vol. 2)", "<b>How Will We Know It's Done?</b> (vol. 2)", "<b>Lightweight Architecture Review</b> (Ana, vol. 6)"],
    quiz=[("What is pre-wiring?", "Meeting each decision maker beforehand to learn what they need to approve."),
          ("What's in the decision paper?", "The decision asked, the design on one page, a section per member's concern, and open points."),
          ("Why questions only in the meeting?", "Everyone has read the paper; the time is for resolving concerns."),
          ("What were the four conditions?", "PSR field encryption, MetroBus delay alerts, a performance test by July, and Kofi's sign-off on meter fields."),
          ("Why does clause 5.5 matter?", "It makes conditional approval count as acceptance, so the £720,000 milestone isn't held by conditions.")],
    quiz_sit=[("Bea asks in the meeting for a full independent review of the reconciliation code before approval. What do you say?", "Point to page 7 and the M3 and M4 criteria, which test reconciliation on real runs; offer the reconciliation reports from each rehearsal to Horizon assurance. Ask Hollis to decide whether it's a condition with a date.")],
    try_it="Think of a decision you need from a group. List each person and their concern. Write a one-page decision paper with a section per concern. Who would you pre-wire, and with what question?",
    remember="Approval meetings <span class=\"hl\">record decisions people already reached</span>. Pre-wire, write a paper, leave with <span class=\"hl\">conditions you can meet</span>.",
    late=dict(when="Wed 9 February 2028 · 22:00 · hotel near The Grid",
              lines=["Approved. Four conditions. £720,000 invoiced at 16:10. Callum checked the bank twice anyway.",
                     "Bea's two questions were on page 7. Hana answered without looking.",
                     "Discovery's done. Design's done. Now we have to build the thing, in environments we don't control, by 23 September."]),
    sources=["Barbara Minto, <i>The Pyramid Principle</i> (1987).",
             "Amazon's six-page narrative memo practice (as described by Colin Bryar and Bill Carr, <i>Working Backwards</i>, 2021).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020)."],
)

NOTES = [WAVES, OVERRULED, DESIGN_AUTHORITY]
