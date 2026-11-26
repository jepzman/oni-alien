# Series 5 · On the Client's Floor · Vol. 4 · Delivery Under Fire · The night (notes 13–15).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 13 What Happens on the Night?
cp_problem = Doodle(760, 240, "Doodle of the cutover window for wave 1: Saturday 23 September 2028 from 18:00 to Sunday 08:00, fourteen hours. Inside it, 380,000 accounts, the MAVIS freeze, the migration, reconciliation, the router switch and the 02:10 job, which runs whether Lodestar is ready or not. Callum's first runbook is a two-page checklist.",
                    "Fourteen hours, 380,000 accounts, and a batch job that runs at 02:10 whether we're ready or not.", exact=True)
cp_problem.line("M60 120 H700", thin=True)
for x, t in [(60, "Sat 18:00"), (330, "02:10"), (700, "Sun 08:00")]:
    cp_problem.line(f"M{x} 108 V132", color="red" if t == "02:10" else "")
    cp_problem.note(x, 160, t, "red" if t == "02:10" else "pen", size=17)
cp_problem.box(450, 20, 280, 70, "runbook v0.1", "pink", sub="2 pages", size=20, subsize=16)
cp_problem.note(380, 216, "the night must be boring; that takes planning", "red", size=19)

cp_how = Doodle(760, 360, "The cutover runbook, version 3. 312 steps, each with an owner, a start time, a duration, a check, and what to do if the check fails. Named roles: a cutover lead, Ines; a decision maker for MetroVolt, Elaine; a communications lead; a scribe. Checkpoints at 23:00, 02:10, 04:30 and 07:00, each a go or roll back decision. The point of no return at 04:30. Rehearsal 3 on 26 August ran the whole runbook in 10 hours 40 minutes against an 11-hour target.",
                "312 steps, named roles, four checkpoints, one point of no return, rehearsed three times.", exact=True)
for i, (t, h, fill) in enumerate([("23:00", "migration 50 %", "y"), ("02:10", "the batch, both feeds", "y"), ("04:30", "point of no return", "pink"), ("07:00", "go live?", "green")]):
    cp_how.box(14 + i * 186, 20, 174, 90, t, fill, sub=h, size=22, subsize=14)
cp_how.box(14, 136, 360, 120, "each step", "paper", sub="owner · start · duration · check · if it fails", size=19, subsize=14)
cp_how.box(386, 136, 360, 120, "roles", "blue", sub="lead Ines · decider Elaine · comms · scribe", size=19, subsize=14)
cp_how.note(380, 300, "rehearsal 3 (26 Aug): 10 h 40 against 11 h", "pen", size=19)
cp_how.note(380, 334, "after 04:30, we fix forward", "red", size=18)

CUTOVER_PLAN = dict(
    slug="cutover-plan", date=date(2028, 8, 26), meta=on_site(date(2028, 8, 26)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. the cutover runbook",
    tldr="A cutover night is a performance, not an improvisation. Write a <b>runbook</b> where every step has an <b>owner</b>, a <b>start time</b>, a <b>duration</b>, a <b>check</b> and <b>what to do if the check fails</b>. Name the <b>roles</b> (lead, decision maker, communications, scribe), set <b>checkpoints</b> where you decide to go on or go back, and agree the <b>point of no return</b> in advance. Then rehearse the runbook itself until the timing is boring.",
    chips=[("Family", "the night"), ("Lives in", "migration/cutover-runbook-v3.md (312 steps)"), ("Pairs with", "migration in waves (vol. 3), go / no-go")],
    problem_side="The Grid, rehearsal 3, 26 August 2028",
    problem="""  <p class="lead">Wave 1's window: <b>Saturday 23 September, 18:00</b> to <b>Sunday 08:00</b>. Fourteen hours to freeze MAVIS for 380,000 accounts, migrate them, reconcile, switch the router, and run the <b>02:10 job</b> with both MAVIS's and Lodestar's feeds to Halvorsen.</p>
  <ul>
    <li>Callum's first runbook, in June, was a two-page checklist: “migrate accounts”, “check”, “switch router”.</li>
    <li>Rehearsal 2 in July ran over by 1 h 40, mostly waiting for people who didn't know it was their turn.</li>
    <li><span class="hl-pink">Nobody had decided who could say “roll back”, or until when.</span></li>
  </ul>""",
    problem_figs=[cp_problem],
    sides=dict(client=("Elaine and Customer Ops", "<p>For MetroVolt, the night decides whether 380,000 customers notice anything on Monday. Elaine wants to know <b>when she'll be asked to decide</b>, on what facts, and what happens if she says no. Customer Ops wants to know when their exception-queue staff start.</p>", "When do I decide, and what am I deciding?"),
                vendor=("Ines and Callum", "<p>Wrenfield needs fourteen hours of work by about forty people from four organisations to run in order, on time, without anyone improvising. Every minute lost waiting for someone eats into the time left for problems.</p>", "Every step owned, every check written, every decision pre-agreed.")),
    sides_after="The runbook isn't for when things go well. It's so that, when something goes wrong at 03:00, nobody has to think about anything except that one thing.",
    analogy_side="the theatre's prompt book",
    analogy="""  <p>A stage manager's <b>prompt book</b> lists every cue: who moves, when, what light changes, what happens if an actor misses an entrance. During the show, she calls each cue in order. Nobody wonders whose turn it is. If the set jams, the book says what happens next, and who decides whether the show goes on.</p>""",
    map=[("The prompt book", "The runbook, 312 steps"),
         ("Each cue: who, when, what", "Owner, start time, duration"),
         ("If an actor misses an entrance", "If the check fails"),
         ("The stage manager calling cues", "Ines, the cutover lead"),
         ("Whether the show goes on", "Elaine's decisions at the checkpoints")],
    how_side="every step owned, checkpoints, a point of no return, rehearsed",
    how="""  <p><b>Every step.</b> Runbook v3 has <b>312 steps</b>. Each has an <b>owner</b> (a person, with a deputy), a <b>planned start</b>, a <b>duration</b>, a <b>check</b> (how we know it worked) and an <b>if it fails</b> line (retry, skip with approval, or escalate to the checkpoint).</p>
  <p><b>Roles.</b> <b>Cutover lead</b>: Ines, who calls each phase. <b>Decision maker</b>: Elaine, for MetroVolt. <b>Communications lead</b>: Callum, who updates the bridge channel every 30 minutes and Priya at each checkpoint. <b>Scribe</b>: Lottie, who logs every step's real time.</p>
  <p><b>Checkpoints</b>, each a go / roll-back decision by Elaine on agreed facts: <b>23:00</b> (migration half done, exceptions under 0.5 %), <b>02:10</b> (the batch runs with both feeds), <b>04:30</b> (reconciliation complete), <b>07:00</b> (go live).</p>
  <p><b>Point of no return: 04:30.</b> Before it, rolling back means flipping 380,000 flags back and unfreezing MAVIS (tested: 1 h 20). After it, MAVIS has run its Sunday processes without these accounts, and the plan is to <b>fix forward</b>.</p>
  <p><b>Rehearse the runbook itself.</b> Rehearsal 3 on <b>26 August</b> runs every step with the real people, timed: <b>10 h 40</b> against an 11-hour target. Twenty-one steps are re-ordered afterwards.</p>""",
    how_figs=[cp_how],
    steps=[("Write every step", "Owner, deputy, start, duration, check, if it fails."),
           ("Name the roles", "Lead, decision maker, communications, scribe."),
           ("Set checkpoints with facts", "What must be true to go on."),
           ("Agree the point of no return", "Before it, roll back; after it, fix forward."),
           ("Rehearse with the real people", "Timed, the whole runbook."),
           ("Re-order after each rehearsal", "Remove waiting.")],
    vocab=[("Cutover", "Switching from the old system to the new one."),
           ("Runbook", "A step-by-step script for an operation, with owners and checks."),
           ("Checkpoint", "A planned moment to decide whether to continue."),
           ("Point of no return", "The moment after which rolling back is no longer the plan."),
           ("Fix forward", "Solving problems in the new state rather than going back."),
           ("Bridge", "A shared call or channel where everyone involved follows the night.")],
    code=dict(file="migration/cutover-runbook-v3.md", note="after rehearsal 3 · Sat 26 Aug 2028", src="""
CUTOVER RUNBOOK v3 · WAVE 1 · Sat 23 Sep 18:00 → Sun 24 Sep 08:00 · 312 steps

roles     lead Ines (dep. Hana) · decider Elaine (dep. Priya) · comms Callum ·
          scribe Lottie · exception desk Customer Ops (12) · Halvorsen on call (Sven)
step 147  owner Bilal (dep. Asif) · start 23:40 · 25 min · migrate batch 7 of 12
          check: rows in = rows out, balances equal · if fails: retry once → CP1
checkpoints  CP1 23:00 migration ≥ 50 %, exceptions < 0.5 %
             CP2 02:10 batch runs, MAVIS + Lodestar feeds accepted by Halvorsen
             CP3 04:30 reconciliation complete (counts, balances, debt)  ← POINT OF
                                                                         NO RETURN
             CP4 07:00 smoke tests, router live, exception queue < 1,900
rollback  before CP3: flip SOR flags, unfreeze MAVIS (rehearsed: 1 h 20)
rehearsal 3  10 h 40 (target 11 h) · 21 steps re-ordered
"""),
    contract=dict(side="what the cutover has to prove", doc="Lodestar SOW · Schedule 4 (M4) and Schedule 9 (cutover)", date="baseline v2.0", stamp="rehearsed",
                  clauses=[("M4", "Wave 1 live: 380,000 accounts migrated; balances reconcile 100 %; ≤ 0.5 % of records in the exception queue; cutover report.", "the cutover report is Lottie's log, tidied."),
                           ("Sch. 9, 3", "MetroVolt's Programme Director decides at each checkpoint whether to continue or roll back, on the facts set out in the runbook.", "Elaine decides. we inform. agreed in June, not at 04:00.")],
                  plain="write into the contract who decides at each checkpoint, on what facts. At 04:00 nobody should be negotiating authority."),
    health=dict(now="g",
                g=("trust is high", ["Rehearse together.", "Decision rights clear.", "Celebrate a boring rehearsal."]),
                a=("a first cutover for the client", ["Every step owned.", "Checkpoints with facts.", "Point of no return agreed in writing."]),
                r=("blame waiting to happen", ["Scribe logs everything.", "Decisions by the agreed person only.", "Runbook signed by both sides."])),
    pressure=dict(level=4, title="the script", cost="312 steps · 40 people · three Saturdays",
                  items=["Writing 312 steps is tedious. Every one of them is a decision someone won't have to make at 03:00.", "Ask the scribe to note who was waiting for whom in rehearsals. That's where the hours hide."]),
    baseline="Each line compares <b>a two-page checklist</b> with <b>a 312-step runbook with owners, checks, checkpoints, a point of no return and three rehearsals</b>.",
    ratings=[(3, 5, "Elaine knows when and what she decides."),
             (2, 4, "Nobody improvises at 03:00."),
             (3, 3, "Neutral."),
             (3, 4, "What “done” means at each checkpoint is written."),
             (3, 4, "The runbook matches the design."),
             (2, 5, "Rollback tested; the point of no return agreed."),
             (3, 5, "Every step logged by the scribe."),
             (2, 3, "Weeks of writing and rehearsing."),
             (3, 3, "A runbook per wave.")],
    pitfalls=[("A short checklist", "People wait and improvise.", "every step owned and timed."),
              ("Unclear decision rights", "Arguments at 04:00.", "name the decision maker, in the contract."),
              ("No point of no return", "Rolling back too late.", "agree it in advance."),
              ("Untested rollback", "It doesn't work when needed.", "rehearse it."),
              ("Rehearsing the data, not the people", "Hand-offs fail.", "rehearse with the real people.")],
    grimoire=[(2, "meeting-lich", "The Meeting Lich", "would turn the bridge call into meeting #113. The runbook keeps it a list of cues.")],
    use=["Any cutover or go-live with several teams.", "When rolling back is expensive.", "Night or weekend operations."],
    skip=["A small, easily reversed change: a short checklist will do."],
    related=["<b>How Do We Move 380,000 Customers?</b> (vol. 3)", "<b>Do We Go?</b> (next note)", "<b>Blue–Green Deployment</b> (patterns, Vol. 6)", "<b>The Urgent Fix at 17:00 on a Friday</b> (Eli, vol. 3)"],
    quiz=[("What does each runbook step have?", "An owner and deputy, a start time, a duration, a check and what to do if it fails."),
          ("What are the four roles?", "Cutover lead, decision maker, communications lead and scribe."),
          ("When is the point of no return, and why then?", "04:30: after it, MAVIS has run Sunday processes without the migrated accounts, so the plan is to fix forward."),
          ("Who decides at checkpoints?", "Elaine, on the facts in the runbook, as the contract says."),
          ("How long did rehearsal 3 take?", "10 hours 40 minutes against an 11-hour target.")],
    quiz_sit=[("At rehearsal 3, step 212 is owned by a MetroVolt engineer who isn't working on 23 September. What do you do?", "Name a deputy now and rehearse them on the step before the night; a step without a present owner is a step that won't happen.")],
    try_it="Pick an operation you'll run soon (a release, a migration, a move). Write the first ten steps with owner, start, duration, check and if-it-fails. Where's your point of no return?",
    remember="Make the night <span class=\"hl\">boring</span>: every step owned, every check written, <span class=\"hl\">every decision agreed in advance</span>.",
    late=dict(when="Sat 26 August 2028 · 05:20 · The Grid, floor 19",
              lines=["Rehearsal 3: 10 h 40. Twenty minutes inside the target. Lottie's log shows who waited for whom.",
                     "Rollback tested: 1 h 20. I hope we never need it. I'm glad we know it works.",
                     "Four weeks to the night. Going home to sleep until Monday."]),
    sources=["Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): managing launches.",
             "Johny Morris, <i>Practical Data Migration</i> (3rd ed., 2020): cutover."],
)

# ------------------------------------------------------------------ 14 Do We Go?
gn_problem = Doodle(760, 240, "Doodle of the go / no-go meeting on Wednesday 6 September 2028. Fourteen criteria on a board, thirteen green. One amber: rehearsal 3 reconciled 99.97 per cent of balances, three accounts off by pennies, cause known, fix ready but not yet proven in a full run. Oliver Thane advises no-go. Priya has to decide.",
                    "Thirteen green, one amber at 99.97 %. Vexmoor says no-go. Priya decides.", exact=True)
for i in range(14):
    gn_problem.box(14 + (i % 7) * 104, 20 + (i // 7) * 60, 94, 48, f"C{i + 1}", "y" if i == 8 else "green", size=16, rx=4)
gn_problem.note(380, 160, "C9: reconciliation 99.97 % (3 accounts, pennies)", "red", size=18)
gn_problem.note(380, 200, "Oliver: “no-go” · Priya: decides", "pen", size=18)

gn_how = Doodle(760, 330, "How the decision was made. The criteria were agreed in June, not today. Each owner reports their criterion with evidence. For the amber, the facts: three accounts, a known rounding cause in the back-feed, a fix tested on those three, and a mitigation: the three accounts excluded from wave 1 and migrated by hand the following week. Priya decides go, with that condition. Oliver's no-go advice is recorded in the minutes with its reasons. Lord Varnish isn't there.",
                "Criteria agreed in advance, evidence per criterion, a condition for the amber, dissent recorded.", exact=True)
for i, (h, sub, fill) in enumerate([("criteria", "agreed in June", "paper"), ("evidence", "each owner reports", "y"), ("amber", "3 accounts, cause known", "pink"), ("condition", "exclude 3, migrate by hand", "green")]):
    gn_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=13)
gn_how.box(14, 150, 360, 80, "decision: GO", "green", sub="Priya · with condition", size=22, subsize=15)
gn_how.box(386, 150, 360, 80, "dissent recorded", "paper", sub="Horizon assurance: no-go, reasons minuted", size=19, subsize=14)
gn_how.note(380, 290, "the decision was made by the person whose customers they are", "pen", size=18)

GO_NO_GO = dict(
    slug="go-no-go", date=date(2028, 9, 6), meta=on_site(date(2028, 9, 6)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. the go / no-go decision",
    tldr="A go / no-go decision is only as good as the <b>criteria agreed before it</b>. Fix them weeks ahead, with owners and evidence. On the day, each owner reports their criterion; anything not green comes with its <b>cause</b>, <b>impact</b> and a <b>mitigation</b>. The <b>sponsor</b> decides, not the vendor and not the loudest adviser, and any <b>dissent is recorded</b> with its reasons. “Go with conditions” is a legitimate answer; “go because we're tired” isn't.",
    chips=[("Family", "the night"), ("Lives in", "governance/go-no-go-2028-09-06.md · DL-058"), ("Pairs with", "the cutover plan, the steering ambush")],
    problem_side="The Grid, room 27A, 6 September 2028",
    problem="""  <p class="lead">The go / no-go for wave 1 is on <b>Wednesday 6 September</b>, seventeen days before the night. <b>Fourteen criteria</b> were agreed in June. Thirteen are green.</p>
  <ul>
    <li><b>C9</b>, rehearsal reconciliation: <b>99.97 %</b>. Three accounts of 380,000 have balances off by a few pence. The cause is known (rounding in a rare back-feed path); the fix is tested on those three, but not in a full run.</li>
    <li>Oliver Thane, for Horizon assurance, advises <b>no-go</b>: “100 % means 100 %.”</li>
    <li>Graham, from Leeds, wants Ines to “push for go”. <span class="hl-pink">It isn't Ines's decision, and she knows it.</span></li>
  </ul>""",
    problem_figs=[gn_problem],
    sides=dict(client=("Priya", "<p>Priya owns the customers and the decision. A no-go means a new date, another Horizon board and a long winter. A go with a known defect means three customers might get a wrong bill. She needs the facts, an honest recommendation and room to decide.</p>", "Tell me what's true, then let me decide."),
                vendor=("Ines", "<p>Wrenfield wants to go, badly: margin, morale, months of work. That's exactly why Ines mustn't push. Her job is to present the evidence straight, propose a mitigation that makes the amber safe, and accept whatever Priya decides.</p>", "Present, propose, then step back.")),
    sides_after="The worst go / no-go decisions are made by people who've stopped being able to say no. The criteria are there so somebody can.",
    analogy_side="the launch director's poll",
    analogy="""  <p>Before a rocket launch, the director polls each station: “Fuel?” “Go.” “Weather?” “Go.” The criteria were written months before. If a station says “no-go”, nobody argues them out of it; the director asks what it would take, and decides. The poll is recorded, every voice. And “hold for ten minutes” is a perfectly good answer.</p>""",
    map=[("Each station's answer", "Each criterion's owner reporting with evidence"),
         ("Criteria written months before", "Fourteen criteria agreed in June"),
         ("A station says no-go", "C9 amber; Oliver's no-go advice"),
         ("The director decides", "Priya decides"),
         ("“Hold for ten minutes”", "Go with a condition: exclude three accounts")],
    how_side="agreed criteria, evidence, a mitigation, the sponsor decides",
    how="""  <p><b>Criteria agreed in advance.</b> The fourteen were signed in June (DL-049): reconciliation, exception rate, performance, severity 1–2 defects at zero, Halvorsen contract tests, the exception desk staffed, rollback rehearsed, communications ready, and so on. Nobody can add or soften one on the day.</p>
  <p><b>Evidence per criterion.</b> Each owner reports in two minutes: Oskar on defects (zero severity 1–2), Rosa on UAT, Sven on the billing tests, Customer Ops on the exception desk. Thirteen green.</p>
  <p><b>The amber, with facts.</b> Hana presents C9: three accounts, the cause, the fix, its test, and a <b>mitigation</b>: <b>exclude those three accounts from wave 1</b> (they stay on MAVIS) and migrate them by hand the following week, after a full test of the fix. With them excluded, C9 is 100 % for the accounts that move.</p>
  <p><b>The sponsor decides.</b> Ines gives Wrenfield's recommendation (go, with the condition) and stops talking. Oliver gives his (no-go) and his reasons. Priya asks two questions, then decides: <b>GO, with the condition</b>. The minutes (DL-058) record the decision, the condition and <b>Horizon assurance's dissent</b>, with its reasons. Lord Varnish isn't there; Priya tells him afterwards.</p>""",
    how_figs=[gn_how],
    steps=[("Agree criteria weeks before", "Owners, evidence, signed."),
           ("No new or softened criteria on the day", "That's what “agreed” means."),
           ("Each owner reports with evidence", "Two minutes each."),
           ("Anything not green: cause, impact, mitigation", "A way to make it safe."),
           ("The sponsor decides", "Vendor and advisers recommend."),
           ("Record the decision and any dissent", "With reasons.")],
    vocab=[("Go / no-go", "A formal decision whether to proceed with a launch or cutover."),
           ("Go-live criteria", "Conditions that must be met to proceed, agreed in advance."),
           ("Conditional go", "Proceeding with a specific mitigation or limit."),
           ("Mitigation", "An action that reduces a risk's likelihood or impact."),
           ("Dissent", "A recorded disagreement with the decision."),
           ("Go fever", "Pressure to proceed because of effort already spent.")],
    code=dict(file="governance/go-no-go-2028-09-06.md", note="DL-058 · Wed 6 Sep 2028", src="""
GO / NO-GO · WAVE 1 · 6 Sep 2028 · decider: Priya Nair

criteria (DL-049, signed 14 Jun)                    owner          status
C1  sev 1–2 defects = 0                             Oskar          GREEN (0)
C3  Halvorsen contract tests 58/58                  Sven           GREEN
C6  UAT sign-off                                    Rosa           GREEN
C7  exception desk staffed + trained (12)           Customer Ops   GREEN
C9  rehearsal reconciliation 100 %                  Hana           AMBER 99.97 %
    3 accounts, pence; cause: rounding in back-feed path BF-17; fix tested on 3
    mitigation: exclude the 3 from wave 1; migrate by hand w/c 2 Oct after full test
C10 performance (1.5× peak, 15 % headroom)          Oskar          GREEN (18 %)
… C2, C4, C5, C8, C11–C14                                          GREEN
recommendations   Wrenfield: GO with mitigation · Horizon assurance: NO-GO ("100 %")
decision          GO, with condition (3 accounts excluded) · Priya Nair
dissent           Horizon assurance: no-go; reasons minuted
"""),
    contract=dict(side="who decides, and on what", doc="Lodestar SOW · Schedule 9, §2 (go / no-go)", date="as amended 14 Jun 2028", stamp="GO",
                  clauses=[("2.1", "The go / no-go decision for each wave is made by MetroVolt's Sponsor against the criteria in Annex A, agreed no later than 12 weeks before the wave.", "Priya decides. criteria from June. not negotiable on the day."),
                           ("2.3", "The Sponsor may decide to proceed subject to conditions. Recommendations of the Supplier and of Horizon Assurance, and any dissent, are recorded.", "conditional go: allowed. dissent: minuted.")],
                  plain="put the decision maker, the criteria deadline and the right to proceed with conditions into the contract. Then the go / no-go is a decision against agreed facts, not a negotiation under pressure."),
    health=dict(now="a",
                g=("all green", ["A short meeting.", "Record it anyway.", "Thank the owners."]),
                a=("one amber, a strong adviser against", ["Cause, impact, mitigation.", "Recommend, then step back.", "Record dissent."]),
                r=("several reds", ["No-go is the honest answer.", "Re-plan with the facts.", "Don't let go fever decide."])),
    pressure=dict(level=5, title="the decision", cost="17 days to the night · a managing director who wants a yes · a rival who wants a no",
                  items=["The hardest part is saying your recommendation and then stopping. Silence lets the sponsor decide.", "If Priya had said no-go, the right response would have been “understood” and a re-plan by Friday."]),
    baseline="Each line compares <b>a go decided by enthusiasm or by the loudest voice</b> with <b>agreed criteria, evidence, a mitigation and the sponsor deciding</b>.",
    ratings=[(3, 5, "Priya decides on facts, with options."),
             (2, 3, "A tense meeting, but clear."),
             (3, 3, "Neutral."),
             (3, 4, "Three accounts excluded, in writing."),
             (3, 4, "The amber is made safe, not waved through."),
             (3, 5, "Every criterion evidenced; the condition reduces the risk."),
             (2, 5, "Decision, condition and dissent minuted."),
             (3, 4, "One meeting."),
             (4, 4, "Light.")],
    pitfalls=[("Criteria invented on the day", "The decision follows the mood.", "agree them weeks before."),
              ("Softening an amber", "“99.97 % is basically 100 %.”", "cause, impact, mitigation."),
              ("The vendor deciding", "Go fever.", "the sponsor decides."),
              ("Ignoring dissent", "It returns as blame.", "record it with reasons."),
              ("No-go seen as failure", "People push to go.", "no-go is a legitimate result.")],
    grimoire=[(7, "pivot-storm", "The Pivot Storm", "is what happens when decisions aren't anchored to criteria: a new direction every quarter.")],
    use=["Any major go-live or cutover.", "When several parties have a stake in the decision.", "When someone influential will disagree."],
    skip=["Small, easily reversible releases: a checklist and the owner's call."],
    related=["<b>What Happens on the Night?</b> (previous note)", "<b>What Happens When Steering Turns on Us?</b> (this volume)", "<b>How Will We Know It's Done?</b> (vol. 2)", "<b>Should This Project Exist?</b> (Sanne, vol. 2)"],
    quiz=[("Why agree criteria weeks before?", "So the decision is made against facts, not negotiated under pressure."),
          ("What must accompany an amber?", "Its cause, impact and a mitigation."),
          ("What was C9's mitigation?", "Exclude the three affected accounts from wave 1 and migrate them by hand after a full test of the fix."),
          ("Who decided, and what?", "Priya: go, with the condition."),
          ("What happened to Oliver's no-go advice?", "It was recorded in the minutes with its reasons.")],
    quiz_sit=[("Priya decides no-go. Graham calls Ines furious. What does Ines do?", "Accept the decision, tell Graham it was the sponsor's call on agreed criteria, and bring a re-plan with options to Elaine by Friday. Arguing a no-go teaches the client that your go-live advice can't be trusted.")],
    try_it="For your next launch, write the go / no-go criteria now, each with an owner and the evidence they'll bring. Who decides? What would you accept as a mitigation for an amber?",
    remember="Criteria <span class=\"hl\">before</span>, evidence on the day, the sponsor decides, <span class=\"hl\">dissent recorded</span>.",
    late=dict(when="Wed 6 September 2028 · 22:00 · hotel near The Grid",
              lines=["GO. With three accounts left behind for a week. Priya decided in eleven minutes.",
                     "Oliver said no-go and gave his reasons. They're in the minutes. He shook my hand afterwards.",
                     "Hardest thing today: saying our recommendation and then not saying anything else."]),
    sources=["NASA, launch commit criteria and the go / no-go poll (public mission documentation).",
             "Diane Vaughan, <i>The Challenger Launch Decision</i> (1996).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): launch reviews."],
)

# ------------------------------------------------------------------ 15 What Did the Night Teach Us?
wn_problem = Doodle(760, 260, "Doodle of the timeline of wave 1 night, Saturday 23 to Sunday 24 September 2028. 18:00 MAVIS frozen for the Northern district. 23:00 checkpoint one, on time. 02:10 the batch job runs with both feeds. 04:10 MetroBus queue full, migration paused 22 minutes. 04:52 checkpoint three, 22 minutes late, reconciliation complete. 07:40 live. 1,206 accounts in the exception queue.",
                    "18:00 freeze · 04:10 the queue fills · 04:52 past the point of no return · 07:40 live.", exact=True)
wn_problem.line("M60 130 H730", thin=True)
for x, t, c in [(60, "18:00 freeze", ""), (190, "23:00 CP1 ✓", "green"), (330, "02:10 batch ✓", "green"), (450, "04:10 queue full", "red"), (560, "04:52 CP3", "pen"), (690, "07:40 live", "green")]:
    wn_problem.line(f"M{x} 118 V142", color=c if c in ("red", "green") else "")
    wn_problem.note(x, 100 if x in (190, 450, 700) else 172, t, c if c else "pen", size=15)
wn_problem.box(240, 196, 280, 50, "1,206 exceptions (0.32 %)", "y", size=17)

wn_how = Doodle(760, 340, "What the runbook didn't foresee, and how it was handled. At 04:10 the MetroBus queue filled: the back-feed and the migration were both writing to it. The runbook's rule for an unforeseen problem: stop the step, call the checkpoint early, decide with facts. Hana and MetroVolt IT paused the migration, drained the queue, raised its limit. 22 minutes. Elaine decided to continue past the point of no return at 04:52. At 08:15, before anyone slept, Lottie and Ines wrote the night log: 14 lessons.",
                "Run the book; when the book runs out, stop, gather facts, decide together; then write it down before sleeping.", exact=True)
for i, (h, sub, fill) in enumerate([("stop the step", "04:10", "pink"), ("facts", "queue full: 2 writers", "y"), ("fix", "drain, raise limit · 22 min", "blue"), ("decide", "Elaine: continue · 04:52", "green")]):
    wn_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=19, subsize=13)
wn_how.box(14, 150, 732, 70, "08:15 · night log before sleep", "paper", sub="what happened, when, who decided, 14 lessons for wave 2", size=19, subsize=14)
wn_how.box(14, 240, 360, 60, "Mon 02:10: billing ✓", "green", size=18)
wn_how.box(386, 240, 360, 60, "Mon: first bills, no complaints", "green", size=17)

WAVE_ONE_NIGHT = dict(
    slug="wave-one-night", date=date(2028, 9, 23), meta=on_site(date(2028, 9, 23)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. cutover night, and the morning after",
    tldr="On the night, <b>run the book</b>: call each step, log real times, decide at the checkpoints. When something happens that the book didn't foresee, follow the book's rule for that: <b>stop the step</b>, gather the <b>facts</b>, fix the smallest thing that works, and let the <b>agreed decision maker</b> decide. Then, before anyone goes home, <b>write down what happened</b>: times, decisions, lessons. Tomorrow you'll remember it differently.",
    chips=[("Family", "the night"), ("Lives in", "migration/wave1-night-log.md · cutover report (M4)"), ("Pairs with", "the cutover plan, go / no-go")],
    problem_side="The Grid, floor 19, Saturday 23 – Sunday 24 September 2028",
    problem="""  <p class="lead">At <b>18:00 on Saturday 23 September</b>, MAVIS is frozen for the Northern district. Forty people on a bridge call and on floor 19: Wrenfield, MetroVolt IT, Customer Ops' exception desk, Sven on call for Halvorsen, Elaine with a flask of tea.</p>
  <ul>
    <li><b>23:00</b>, checkpoint one: migration at 52 %, exceptions 0.29 %. Go.</li>
    <li><b>02:10</b>: the batch job runs, with MAVIS's feed for 1.9 million accounts and Lodestar's for 380,000. Halvorsen accepts both. Go.</li>
    <li><b>04:10</b>: the migration stops. <span class="hl-pink">The MetroBus queue is full.</span> Twenty minutes to the point of no return. Nothing in the runbook says “queue full”.</li>
  </ul>""",
    problem_figs=[wn_problem],
    sides=dict(client=("Elaine", "<p>Elaine has waited three years, since Orion, for a night like this to go right. At 04:10 she has to decide whether to keep going past the point of no return with a problem nobody planned for, or roll back and lose the weekend. She needs facts in minutes, not opinions.</p>", "Tell me what's wrong, what you've done, and what you recommend."),
                vendor=("Ines and Hana", "<p>The runbook covers 312 steps and has one rule for everything else: stop, gather facts, call the checkpoint early. At 04:10 Ines has to make that rule work: keep forty tired people calm, get Hana and MetroVolt IT on the problem, and give Elaine a decision she can make.</p>", "The book's last rule: when the book runs out, stop and think together.")),
    sides_after="Every cutover has a moment the plan didn't foresee. The plan's job is to make that moment the only thing anyone has to think about.",
    analogy_side="the pilot's unexpected warning",
    analogy="""  <p>When an unexpected warning light comes on, pilots have a rule older than any checklist: <b>aviate, navigate, communicate</b>. Keep the plane flying, work out where you are, then talk. They don't all shout ideas at once. And after landing, before anyone leaves, they write down exactly what happened, while it's fresh.</p>""",
    map=[("Aviate", "Stop the step; keep everything else stable"),
         ("Navigate", "Gather the facts: two writers, one queue"),
         ("Communicate", "Callum on the bridge; Elaine briefed"),
         ("The captain decides", "Elaine continues past 04:30, at 04:52"),
         ("Writing it down after landing", "The night log at 08:15")],
    how_side="run the book; when it runs out, stop, facts, fix, decide; then write",
    how="""  <p><b>Run the book.</b> Ines calls each phase; Lottie logs real times against planned. Checkpoints one and two pass on time. Callum updates the bridge every 30 minutes and texts Priya at each checkpoint.</p>
  <p><b>When the book runs out (04:10).</b> The runbook's last rule: <i>stop the step, call the checkpoint early, decide on facts</i>. Ines stops the migration. Hana and MetroVolt IT's on-call find the cause in nine minutes: the <b>back-feed</b> to MAVIS and the <b>migration</b> are both writing to one MetroBus queue, which hit its limit. Neither rehearsal ran them at the same moment. They <b>drain the queue</b>, <b>raise its limit</b>, and restart the migration: <b>22 minutes</b>.</p>
  <p><b>Decide.</b> At <b>04:52</b>, 22 minutes late, checkpoint three: reconciliation complete, counts and balances equal. Ines recommends continuing; Elaine decides to go past the point of no return. At <b>07:40</b>, the router goes live. <b>380,000</b> accounts migrated (less the three excluded); <b>1,206</b> in the exception queue (<b>0.32 %</b>), worked by Customer Ops' desk through Sunday.</p>
  <p><b>Write it down before sleeping.</b> At 08:15 Lottie and Ines write the <b>night log</b>: every checkpoint, the 04:10 problem, who decided what, and <b>14 lessons</b> for wave 2. Monday's 02:10 file to Halvorsen goes through. The first Lodestar bills go out on Monday. Customer Ops' phone lines are quiet.</p>""",
    how_figs=[wn_how],
    steps=[("Call every phase; log real times", "A scribe, against the plan."),
           ("Communicate on a rhythm", "Every 30 minutes, and at checkpoints."),
           ("When something's unforeseen, stop the step", "Keep everything else stable."),
           ("Facts first, then the smallest fix", "One team on it, everyone else waits."),
           ("The agreed person decides", "Recommend, then let them."),
           ("Write the log before sleeping", "Times, decisions, lessons.")],
    vocab=[("Hypercare", "A period of extra support straight after go-live."),
           ("Night log", "A timed record of what happened during an operation."),
           ("Bridge call", "A shared call where everyone follows the operation."),
           ("Unforeseen event", "Something the plan didn't cover."),
           ("Lessons learned", "What to do differently next time, written while fresh."),
           ("Cutover report", "The formal record of the cutover, evidence for acceptance.")],
    code=dict(file="migration/wave1-night-log.md", note="written Sun 24 Sep 2028, 08:15–09:40", src="""
WAVE 1 NIGHT LOG · Sat 23 → Sun 24 Sep 2028 · scribe: Lottie Marsh

18:00  MAVIS frozen, Northern district (380,000 − 3 excluded)
23:00  CP1  migration 52 %, exceptions 0.29 %            GO (Elaine)   on time
02:10  CP2  batch ran; Halvorsen accepted both feeds      GO (Elaine)   on time
04:10  migration stopped: MetroBus queue full (back-feed + migration, same queue)
04:19  cause confirmed (Hana + MetroVolt IT on-call) · drain + raise limit
04:32  migration restarted (22 min lost)
04:52  CP3  reconciliation complete: counts, balances, debt equal
            past point of no return                       GO (Elaine)   +22 min
07:00  CP4  smoke tests 41/41, router ready                GO (Elaine)
07:40  LIVE · exceptions 1,206 (0.32 %) → Customer Ops desk (cleared Sun 19:10)
lessons (14): L1 rehearse back-feed + migration together · L2 queue limits in
the runbook's pre-checks · L3 a 5-min "unforeseen" drill in each rehearsal · …
Mon 02:10  first Lodestar-fed billing run: accepted · Mon: bills out, no complaints
"""),
    contract=dict(side="what the night proves", doc="Lodestar SOW · Schedule 4 (M4)", date="M4 evidence submitted 2 Oct 2028", stamp="live",
                  clauses=[("M4", "Wave 1 live: 380,000 accounts migrated; balances reconcile 100 %; ≤ 0.5 % of records in the exception queue; cutover report.", "379,997 migrated (3 excluded by condition) · 100 % · 0.32 % · the night log."),
                           ("Sch. 9, 5", "The Supplier provides hypercare for 8 weeks after each wave.", "hypercare starts Sunday 07:40. so does the next volume.")],
                  plain="the night's log is also the milestone's evidence. Writing it while it's fresh makes acceptance easy and the next wave safer."),
    health=dict(now="g",
                g=("it went well", ["Write the log anyway.", "Thank everyone by name.", "Rest before celebrating."]),
                a=("something unforeseen happened", ["Stop, facts, fix, decide.", "The agreed person decides.", "Lessons before sleep."]),
                r=("it went badly", ["Roll back if before the point of no return.", "Blameless log.", "Re-plan with the lessons."])),
    pressure=dict(level=5, title="the night", cost="14 hours · 40 people · 22 minutes nobody planned for",
                  items=["At 04:10, the most useful thing Ines did was say slowly: “Stop the step. Hana, MetroVolt IT, the queue. Everyone else, wait.”", "Hana worked nineteen hours. Notice that. It's where the next volume begins."]),
    baseline="Each line compares <b>improvising through an unforeseen problem</b> with <b>stopping the step, finding facts, the smallest fix and the agreed decision maker deciding</b>.",
    ratings=[(3, 5, "Elaine decided at 04:52 on facts, with tea."),
             (2, 2, "A long night; Hana worked nineteen hours."),
             (3, 4, "M4 evidence complete the next week."),
             (3, 4, "Three excluded accounts handled by plan."),
             (3, 4, "The fix was small and right."),
             (3, 5, "The unforeseen was contained in 22 minutes."),
             (3, 5, "Every decision logged with its time."),
             (3, 4, "Live 07:40, inside the window."),
             (3, 3, "Hypercare begins.")],
    pitfalls=[("Everyone fixing at once", "Noise, and new problems.", "one team on it, everyone else waits."),
              ("Deciding without facts", "Rolling back, or forward, on a hunch.", "nine minutes for the cause."),
              ("The vendor deciding", "Authority argued at 04:30.", "the agreed person decides."),
              ("No log", "Wave 2 repeats the problem.", "write it before sleeping."),
              ("Ignoring the people", "Burnout after the success.", "notice who carried the night.")],
    grimoire=[(8, "slow-hex-of-burnout", "The Slow Hex of Burnout", "starts on nights like this: a success, and someone who worked nineteen hours and says they're fine.")],
    use=["Any cutover or major go-live.", "Any long operation with several teams.", "Whenever the plan meets something it didn't foresee."],
    skip=["Never skip the log."],
    related=["<b>What Happens on the Night?</b> (this volume)", "<b>Do We Go?</b> (previous note)", "<b>Who Is in Charge?</b> (Eli, vol. 2)", "<b>How Do We Move 380,000 Customers?</b> (vol. 3)"],
    quiz=[("What is the runbook's rule for something unforeseen?", "Stop the step, call the checkpoint early, decide on facts."),
          ("What happened at 04:10?", "The MetroBus queue filled because the back-feed and the migration were writing to it at the same time."),
          ("Who decided to go past the point of no return?", "Elaine, at 04:52, after reconciliation was complete."),
          ("What were the night's numbers?", "379,997 accounts migrated (3 excluded), 1,206 exceptions (0.32 %), live at 07:40."),
          ("Why write the log before sleeping?", "Memories change by morning; the log is also the milestone's evidence and wave 2's lessons.")],
    quiz_sit=[("At 05:30, a MetroVolt manager on the bridge suggests also fixing a known UAT cosmetic defect “while we're all here”. What do you say?", "No: tonight only the runbook's steps. Log it for hypercare. Any change during a cutover adds risk to everything else.")],
    try_it="Think of the last time a plan met something it didn't cover. Write the night log: times, the problem, who decided what, and three lessons. Would “stop, facts, smallest fix, agreed decider” have helped?",
    remember="Run the book. When the book runs out: <span class=\"hl\">stop, facts, smallest fix, the agreed person decides</span>. Then <span class=\"hl\">write it down before you sleep</span>.",
    late=dict(when="Sun 24 September 2028 · 09:55 · The Grid, floor 19",
              lines=["Live at 07:40. 1,206 exceptions, cleared by Customer Ops' desk by tonight. Elaine cried a little at 07:41. So did I.",
                     "04:10, the queue. Twenty-two minutes I'll remember for a long time. Hana fixed it in nine.",
                     "Hana's been here since 15:00 yesterday. She says she's fine. She said that in June too. Tomorrow, hypercare. And tomorrow I'm going to make her go home."]),
    sources=["Atul Gawande, <i>The Checklist Manifesto</i> (2009).",
             "UK Civil Aviation Authority, <i>CAP 737: Flight-crew human factors</i>: aviate, navigate, communicate.",
             "Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): incident response."],
)

NOTES = [CUTOVER_PLAN, GO_NO_GO, WAVE_ONE_NIGHT]
