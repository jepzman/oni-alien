# Series 5 · On the Client's Floor · Vol. 6 · The Cost and the Ending · Handing it over (notes 5–8).
# Narrator: Ines Duarte (she/her). Facts: docs/lodestar-casebook.md, "Vol. 6".
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 05 What Do We Owe After Go-Live?
wa_problem = Doodle(760, 240, "Doodle of the warranty inbox: 37 reports in 90 days, from 22 November 2028 to 20 February 2029. Some are real defects. Some are new wishes. Rupert's office says a slow monthly report is a defect, so it should be fixed free. The warranty ends in eight days and nobody has agreed what's been closed.",
                    "37 reports in 90 days, and a disagreement about what a defect is.", exact=True)
wa_problem.box(14, 20, 732, 70, "warranty · 22 Nov 2028 → 20 Feb 2029 · 37 reports", "y", size=20)
for i, (t, fill) in enumerate([("defect?", "pink"), ("change?", "blue"), ("not ours?", "paper")]):
    wa_problem.box(14 + i * 250, 120, 232, 60, t, fill, size=20)
wa_problem.note(380, 220, "Rupert's office: “the slow report is a defect”", "red", size=18)

wa_how = Doodle(760, 330, "The warranty triage. Read the warranty first: Schedule 9 says a defect is a failure to meet the agreed specification, fixed free within the target times. Triage every report against it, with the client in the room, twice a week. 37 reports: 14 defects fixed free, 15 changes to the change pool or wave 2, 8 not reproducible or operational. The slow report met its agreed performance criterion of under 30 seconds at 22 seconds: a change, priced at £6k, or tuned free as a goodwill gesture. Close the warranty in writing.",
                "Read it, triage against it with the client, fix fast, and close it in writing.", exact=True)
for i, (h, n, fill) in enumerate([("defects", "14", "pink"), ("changes", "15", "blue"), ("not ours", "8", "paper")]):
    wa_how.box(14 + i * 250, 20, 232, 110, n, fill, sub=h, size=34, subsize=15)
wa_how.box(14, 160, 732, 70, "slow report: 22 s (criterion < 30 s) → change · tuned free as goodwill, recorded", "y", size=16)
wa_how.note(380, 280, "warranty certificate WC-01 · signed Fri 23 Feb 2029", "green", size=18)

WARRANTY = dict(
    slug="warranty", date=date(2029, 2, 12), meta=on_site(date(2029, 2, 12)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. the warranty and the long tail",
    tldr="After go-live, the client will report everything: real defects, new wishes and problems that aren't yours. <b>Read what the warranty actually covers</b>, <b>triage every report against it with the client in the room</b>, <b>fix real defects fast and free</b>, price changes honestly, and <b>close the warranty in writing</b>. A generous gesture is fine when it's recorded as one.",
    chips=[("Family", "handing it over"), ("Lives in", "warranty log · Schedule 9 · certificate WC-01"), ("Pairs with", "acceptance (vol. 2), UAT triage (vol. 4)")],
    problem_side="Floor 19, 12 February 2029",
    problem="""  <p class="lead">Wave 1's <b>warranty</b> runs for 90 days after hypercare: from M5's acceptance on <b>22 November 2028</b> to <b>20 February 2029</b>. In that time, <b>37 reports</b> have arrived.</p>
  <ul>
    <li>Some are real defects: a rounding error on a refund letter.</li>
    <li>Some are new wishes: “can the screen show the last three meter reads?”</li>
    <li>Rupert's office says the slow monthly arrears report <span class="hl-pink">is a defect and should be fixed free</span>.</li>
    <li>The warranty ends in eight days and nobody has agreed which reports are closed.</li>
  </ul>""",
    problem_figs=[wa_problem],
    sides=dict(client=("MetroVolt", "<p>To MetroVolt, anything that annoys a user after go-live feels like the supplier's problem. After Lodestar's history (and Orion's) nobody wants to pay for something that might have been the supplier's mistake.</p>", "If it's wrong after go-live, it's yours."),
                vendor=("Ines and Callum", "<p>Wrenfield owes real defects, fixed fast. It doesn't owe new features for free, and a warranty that never closes is an open-ended cost. But arguing every report as a lawyer would damage the relationship weeks before the phase 2 bid.</p>", "Fix what's ours, fast. Be clear about what isn't.")),
    sides_after="A warranty is a promise about the agreed specification, not about everything users wish for. The specification is the referee.",
    analogy_side="the builder's snagging list",
    analogy="""  <p>When a builder finishes a house, the owner walks round with a <b>snagging list</b>: a door that sticks, a crack in the plaster. The builder fixes snags free. A new window the owner has decided she'd like is not a snag; it's an extra, and it's priced. Good builders fix the snags quickly and say “happy to quote” for the extras, and everyone signs the list off at the end.</p>""",
    map=[("The snagging list", "The warranty log (37 reports)"),
         ("A door that sticks", "A defect: fixed free"),
         ("A new window", "A change: priced"),
         ("The neighbour's fence", "Not ours: operational or Halvorsen"),
         ("Signing the list off", "Warranty certificate WC-01")],
    how_side="read it, triage against it, fix fast, close in writing",
    how="""  <p><b>Read what's covered.</b> Schedule 9: a <b>defect</b> is a failure to meet the agreed specification; severity 1 responded to within an hour, fixed within a day; severity 3 within ten working days. Changes in function, and problems caused by MetroVolt's operation or other suppliers, are excluded.</p>
  <p><b>Triage with the client in the room.</b> Twice a week, Rosa (MetroVolt) and Oskar go through new reports against the spec, as they did in UAT. Each one gets a label and a reason, agreed by both: <b>14 defects</b>, <b>15 changes</b>, <b>8 not ours</b> (5 not reproducible, 2 operational, 1 Halvorsen's).</p>
  <p><b>Fix defects fast and free.</b> All 14 are fixed inside the target times; the refund rounding error in two days.</p>
  <p><b>The slow report.</b> The spec says the arrears report runs in under <b>30 seconds</b>; it runs in <b>22</b>. It's not a defect: users want it in five. Ines offers to tune it <b>free, as a recorded goodwill gesture</b> (about £6k of effort), rather than argue. Rupert's office accepts; the log says “change, done as goodwill”, not “defect”.</p>
  <p><b>Close it in writing.</b> Warranty certificate <b>WC-01</b>, signed by Elaine on <b>Friday 23 February</b>: 37 reports, each closed or moved, with the remaining changes in the wave 2 backlog.</p>""",
    how_figs=[wa_how],
    steps=[("Read what the warranty covers", "Definition, severities, exclusions."),
           ("Triage every report against it", "With the client, twice a week."),
           ("Fix real defects fast", "Inside the target times."),
           ("Price changes honestly", "Or give them as recorded goodwill."),
           ("Move the rest", "To the change pool, wave 2 or the right owner."),
           ("Close the warranty in writing", "A certificate, signed.")],
    vocab=[("Warranty", "A period after acceptance when the supplier fixes defects free."),
           ("Defect", "A failure to meet the agreed specification."),
           ("Change", "Something new or different from the specification."),
           ("Goodwill gesture", "Free work given as a favour, recorded as such."),
           ("Warranty certificate", "A signed record that the warranty is closed."),
           ("Long tail", "Small issues that keep arriving long after go-live.")],
    code=dict(file="warranty/lodestar-wave1-log.md", note="closed Fri 23 Feb 2029 · certificate WC-01", src="""
WARRANTY · wave 1 · 22 Nov 2028 → 20 Feb 2029 · triage Mon/Thu (Rosa + Oskar)

reports    37
defects    14  fixed free, all inside target times (refund rounding: 2 days)
changes    15  9 → change pool (£22k) · 6 → wave 2 backlog
not ours    8  5 not reproducible · 2 operational · 1 Halvorsen (passed on, IA-01)
note       W-29 arrears report: 22 s vs criterion < 30 s → CHANGE ·
           tuned to 4 s as recorded goodwill (≈ £6k), not as a defect
closed     WC-01 signed by Elaine Corbett, Fri 23 Feb 2029
"""),
    contract=dict(side="what the warranty promises", doc="Lodestar SOW · Schedule 9 (warranty)", date="signed 30 June 2027", stamp="closed",
                  clauses=[("Sch. 9, 2.1", "For 90 days after acceptance of Milestone 5, the Supplier shall correct Defects at no charge. A Defect is a failure of the Deliverables to meet the Specification.", "the specification is the referee. not the mood of the meeting."),
                           ("Sch. 9, 2.4", "The warranty excludes changes to function, and faults caused by MetroVolt's operation or by Other Suppliers.", "8 of 37 were outside it. we helped anyway, and said so.")],
                  plain="a warranty covers failures against what was agreed. Use the specification to decide each report, with the client, and close the period in writing."),
    health=dict(now="g",
                g=("a tidy warranty", ["Triage with the client.", "Fix fast.", "Close in writing."]),
                a=("arguments about defects", ["Use the specification.", "Offer recorded goodwill.", "Escalate only the big ones."]),
                r=("a warranty that never closes", ["Agree a closure list.", "Move changes to a contract.", "Get the certificate signed."])),
    pressure=dict(level=2, title="the long tail", cost="£6k of goodwill · two meetings a week",
                  items=["Arguing a £6k report while bidding for £9m is the wrong fight. Give it, and record it as a gift.", "A warranty with no end date is unlimited liability by another name."]),
    baseline="Each line compares <b>fixing whatever arrives and letting the warranty drift</b> with <b>triage against the specification, fast fixes, recorded goodwill and a signed certificate</b>.",
    ratings=[(3, 4, "Defects fixed fast, gestures visible."),
             (3, 4, "Clear rules instead of arguments."),
             (2, 4, "Changes priced; the warranty closes."),
             (2, 5, "Every report labelled and closed."),
             (3, 4, "Defects fixed inside target times."),
             (2, 4, "No open-ended liability."),
             (3, 5, "WC-01 signed."),
             (3, 3, "Twice-weekly triage."),
             (3, 3, "A small log.")],
    pitfalls=[("Fixing everything free", "The warranty never ends.", "triage against the spec."),
              ("Arguing every report", "The relationship pays.", "recorded goodwill for small ones."),
              ("Triage without the client", "Every label is disputed.", "Rosa in the room."),
              ("Unrecorded favours", "They become obligations.", "write “goodwill”."),
              ("No closing document", "It drifts on.", "a signed certificate.")],
    grimoire=[(6, "scope-creep-swarm", "The Scope Creep Swarm", "is what an unclosed warranty turns into.")],
    use=["Every go-live with a warranty.", "When “defect” is being stretched.", "Before a follow-on bid."],
    skip=["Time-and-materials work with no warranty (still triage)."],
    related=["<b>How Will We Know It's Done?</b> (vol. 2)", "<b>Is It a Defect or a Change?</b> (vol. 4)", "<b>How Do We Hand It Over So It Sticks?</b> (next note)", "<b>Can We Change That?</b> (Sanne, vol. 2)"],
    quiz=[("How long was the warranty, and from when?", "90 days from M5's acceptance on 22 November 2028."),
          ("What defines a defect?", "A failure to meet the agreed specification (Schedule 9)."),
          ("How were the 37 reports split?", "14 defects, 15 changes, 8 not ours."),
          ("Why wasn't the slow report a defect?", "It ran in 22 seconds against a criterion of under 30."),
          ("How was the warranty closed?", "Warranty certificate WC-01, signed by Elaine on 23 February 2029.")],
    quiz_sit=[("A week after WC-01, Rosa reports a new rounding error in a rare letter. Is it in warranty?", "No, the warranty is closed. But if it's a genuine failure against the spec, fix it quickly and say so: it costs little and the relationship matters. Record it as goodwill, or under the support terms if there are any.")],
    try_it="Take your last go-live's issue list. Label each item: defect (against which line of the spec?), change, or not yours. How many would you have argued about? Which would you give as goodwill?",
    remember="The specification is <span class=\"hl\">the referee</span>. Fix defects fast, give gifts on purpose, and <span class=\"hl\">close it in writing</span>.",
    late=dict(when="Fri 23 February 2029 · 20:15 · train to Leeds",
              lines=["WC-01 signed. 37 reports, all labelled, all closed or moved.",
                     "The arrears report runs in four seconds now. We gave it away and wrote down that we gave it away. Rupert's office sent a thank-you, which I'm keeping.",
                     "Hana sent a photo from the Dales. First weekend walk in six months."]),
    sources=["UK Cabinet Office, <i>Model Services Contract</i> (warranty and defects schedules).",
             "ITIL 4, <i>Service Transition</i> (early life support).",
             "Steve McConnell, <i>Software Estimation</i> (2006): on the cost of the long tail."],
)

# ------------------------------------------------------------------ 06 How Do We Hand It Over So It Sticks?
kt_problem = Doodle(760, 240, "Doodle of a knowledge transfer plan made of slides: 23 presentations scheduled for March, an attendance list, and a sign-off box ticked by a manager. MetroVolt's run team, Asif, Marta and Kemi, will be called at three in the morning when the back-feed stops. They've watched demos. They haven't run anything.",
                    "23 slide decks and a ticked box. The run team has never run it.", exact=True)
kt_problem.box(14, 20, 360, 110, "23 presentations", "paper", sub="“knowledge transfer”", size=22, subsize=14)
kt_problem.box(386, 20, 360, 110, "03:00", "pink", sub="Asif · Marta · Kemi, alone", size=30, subsize=14)
kt_problem.note(380, 190, "watching isn't the same as doing", "red", size=20)

kt_how = Doodle(760, 340, "How the handover was done. Shadow: the run team watches Wrenfield run it for two weeks. Reverse shadow: Wrenfield watches the run team run it for two weeks, hands off the keyboard. Runbooks written by the run team, not for them. Four drills: back-feed stopped, MetroBus queue full, bad file from Halvorsen, a failed release. Sign-off by the people who'll be called at night: Kemi, Marta and Asif, not a manager.",
                "Shadow, reverse-shadow, their runbooks, real drills, and their sign-off.", exact=True)
for i, (h, sub, fill) in enumerate([("shadow", "they watch us", "paper"), ("reverse", "we watch them", "blue"), ("runbooks", "written by them", "y"), ("drills", "4, with failures", "pink"), ("sign-off", "the 03:00 people", "green")]):
    kt_how.box(14 + i * 148, 20, 138, 100, h, fill, sub=sub, size=18, subsize=12)
kt_how.box(14, 150, 732, 70, "drill 3: Halvorsen's bad file · Kemi fixed it in 41 min, nobody from Wrenfield touched a key", "green", size=15)
kt_how.note(380, 290, "Kemi: “I'd take the call at three.”", "pen", size=19)

KNOWLEDGE_TRANSFER = dict(
    slug="knowledge-transfer", date=date(2029, 3, 9), meta=on_site(date(2029, 3, 9)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. knowledge transfer that sticks",
    tldr="Knowledge transfer done with slides transfers slides. Transfer it <b>by doing</b>: the client's people <b>shadow</b> you, then you <b>reverse-shadow</b> them, hands off the keyboard; <b>they</b> write the runbooks; <b>drills</b> with real failures; and the <b>sign-off comes from the people who'll be called at night</b>, not from a manager who attended the presentations.",
    chips=[("Family", "handing it over"), ("Lives in", "run/lodestar/kt-plan.md · runbooks/"), ("Pairs with", "Bert's book (vol. 3), rotating off")],
    problem_side="Floor 19, March 2029",
    problem="""  <p class="lead">From April, MetroVolt's run team (<b>Asif, Marta and Kemi</b>) will run Lodestar's wave 1 platform on their own. §11.2 of the contract requires Wrenfield to transfer knowledge “so that MetroVolt can operate the solution”.</p>
  <ul>
    <li>The first draft plan, written in a hurry in January, was <b>23 presentations</b> and a sign-off box for a manager.</li>
    <li>The run team has watched demos. <span class="hl-pink">None of them has run a release or fixed a stopped back-feed alone.</span></li>
    <li>Hana, who knew the back-feed best, has rotated off.</li>
  </ul>""",
    problem_figs=[kt_problem],
    sides=dict(client=("Kemi, Marta and Asif", "<p>The run team will be the ones paged at 03:00. They've worked beside Wrenfield in mixed squads, but always with a Wrenfield engineer nearby. Kemi says it plainly: “I don't want a certificate. I want to know I can fix it.”</p>", "Let us break it while you're still here."),
                vendor=("Ines and Tariq", "<p>Wrenfield wants a clean handover: the contract requires it, and a client who can't run the system calls the supplier forever, for free. Tariq is new and has his own learning to do. Presentations would be quicker. They wouldn't work.</p>", "If they can't run it, we haven't handed it over.")),
    sides_after="Knowledge transfer is finished when the client's people can do it without you, under pressure, not when you've finished talking.",
    analogy_side="learning to drive",
    analogy="""  <p>Nobody learns to drive from a lecture. You sit beside the instructor, then <b>you drive while she watches</b>, with her hands in her lap and a foot near the dual brake. Then you practise the hard things: a hill start, a roundabout in the rain. The test is taken by the driver, not by the instructor's manager.</p>""",
    map=[("Sitting beside the instructor", "Shadowing (weeks 1–2)"),
         ("Driving while she watches", "Reverse shadowing (weeks 3–4)"),
         ("A hill start in the rain", "Drills with real failures"),
         ("The dual brake", "Wrenfield on standby, hands off"),
         ("The driving test", "Sign-off by the run team")],
    how_side="shadow, reverse-shadow, their runbooks, drills, their sign-off",
    how="""  <p>Tariq and Ines rewrite the plan in January with Kemi, Marta and Asif. <b>23 presentations become 4</b>, for the background. The rest is doing:</p>
  <p><b>Shadow (12–23 February).</b> The run team sits with Wrenfield during every operational task: the nightly checks, a release, the MetroBus queue, the back-feed.</p>
  <p><b>Reverse shadow (26 February – 9 March).</b> The run team does everything; Wrenfield watches with <b>hands off the keyboard</b>. Lottie keeps a tally of every time a Wrenfield engineer was tempted to grab the mouse (19, falling to 2).</p>
  <p><b>Their runbooks.</b> The run team writes the <b>11 runbooks</b> themselves, starting from Hana's 14 pages, in their own words. Wrenfield reviews them. Bert reads the back-feed one and adds a page about the 02:10 file.</p>
  <p><b>Drills with real failures.</b> Four, in the pre-production copy: the back-feed stopped; the MetroBus queue full (wave 1 night's problem); a bad file from Halvorsen; a failed release to roll back. In drill 3, Kemi finds and fixes the bad file in <b>41 minutes</b> without anyone from Wrenfield touching a key.</p>
  <p><b>Their sign-off.</b> On <b>Friday 9 March</b>, the knowledge transfer certificate is signed by Kemi, Marta and Asif, then countersigned by Hollis. Kemi's comment in the box: <i>“I'd take the call at three.”</i></p>""",
    how_figs=[kt_how],
    steps=[("Plan it with the people who'll run it", "Not for them."),
           ("Shadow", "They watch you do the real work."),
           ("Reverse shadow", "You watch them, hands off."),
           ("Let them write the runbooks", "In their own words."),
           ("Drill real failures", "The ones you've actually had."),
           ("Sign-off by the night-call people", "Then their manager countersigns.")],
    vocab=[("Knowledge transfer", "Moving the ability to run something to another team."),
           ("Shadowing", "Learners watching experts do real work."),
           ("Reverse shadowing", "Experts watching learners do it, without helping."),
           ("Runbook", "Step-by-step instructions for an operational task."),
           ("Drill", "A rehearsed failure to practise the response."),
           ("Operational acceptance", "The run team agreeing they can run it.")],
    code=dict(file="run/lodestar/kt-certificate.md", note="signed Fri 9 Mar 2029", src="""
KNOWLEDGE TRANSFER · Lodestar wave 1 platform → MetroVolt run team (SOW §11.2)

presentations   4 (background only; 19 cut)
shadow          12–23 Feb · all nightly checks, 1 release, queue, back-feed
reverse shadow  26 Feb–9 Mar · hands off (tally of mouse-grabs: 19 → 2)
runbooks        11, written by the run team (from Hana's 14 pages) · back-feed: +1 page by Bert
drills          1 back-feed stopped ✓ · 2 MetroBus queue full ✓ ·
                3 bad Halvorsen file ✓ (Kemi, 41 min, no Wrenfield keys) · 4 failed release, rolled back ✓
signed          Kemi · Marta · Asif (run team) · countersigned: Hollis Wade
Kemi's note     "I'd take the call at three."
"""),
    contract=dict(side="what the knowledge transfer clause asks", doc="Lodestar SOW · §11.2 and Schedule 10", date="signed 30 June 2027", stamp="transferred",
                  clauses=[("11.2", "The Supplier shall transfer knowledge to MetroVolt staff throughout the Services, so that MetroVolt can operate the solution at the end of Wave 1.", "“can operate”. not “has attended”."),
                           ("Sch. 10, 3.1", "Knowledge transfer is complete when MetroVolt's nominated operational staff confirm in writing that they can operate the solution.", "we nominated the people who'd be paged. Hollis agreed.")],
                  plain="read what “complete” means in your knowledge-transfer clause. If it says “can operate”, the evidence is the client's people operating it, not attendance lists."),
    health=dict(now="g",
                g=("a team that can run it", ["Drills passed.", "Their runbooks.", "Their signatures."]),
                a=("slides but no doing", ["Add reverse shadowing.", "Drill the real failures.", "Move sign-off to the run team."]),
                r=("handover at the last minute", ["Extend the overlap.", "Do the riskiest tasks first.", "Stay on call, paid, for a period."])),
    pressure=dict(level=2, title="taking your hands off", cost="four weeks of overlap · 19 mouse-grabs resisted",
                  items=["Watching someone slower do your job is uncomfortable. That's the job now.", "Every presentation you skip is an hour for a drill."]),
    baseline="Each line compares <b>23 presentations and a manager's sign-off</b> with <b>shadow, reverse shadow, their runbooks, four drills and the run team's own sign-off</b>.",
    ratings=[(3, 5, "MetroVolt can run it."),
             (3, 4, "Fewer night calls to Wrenfield later."),
             (3, 3, "Four weeks of overlap."),
             (3, 4, "Clear end to the support."),
             (2, 5, "Runbooks tested by drills."),
             (2, 5, "Operational risk handed over properly."),
             (3, 4, "§11.2 evidenced, not asserted."),
             (3, 2, "Slower than slides."),
             (3, 4, "No calls for help in April.")],
    pitfalls=[("Slides as transfer", "Nobody can run it.", "do it, with them."),
              ("Hands on the keyboard", "They never practise.", "reverse shadow, hands off."),
              ("Writing runbooks for them", "They don't trust them.", "they write, you review."),
              ("Drilling the easy things", "The real failure is new.", "drill what actually broke."),
              ("Manager's sign-off", "It measures attendance.", "the 03:00 people sign.")],
    grimoire=[(8, "phylactery-of-paper", "The Phylactery of Paper", "is about the paper you keep; this note is about the skill you hand over.")],
    use=["Every handover to a client run team.", "Before a supplier leaves.", "When key people rotate off."],
    skip=["Never; shorten it, but keep the drills."],
    related=["<b>Who Knows How It Really Works?</b> (vol. 3)", "<b>How Do We Rotate Someone Off an Account?</b> (this volume)", "<b>What Should the Handover Architecture Say?</b> (this volume)", "<b>Can Someone Else Run This?</b> (Sanne, vol. 6)"],
    quiz=[("What did the first plan consist of?", "23 presentations and a sign-off box for a manager."),
          ("What happens in reverse shadowing?", "The run team does the work; Wrenfield watches with hands off the keyboard."),
          ("Who wrote the runbooks?", "The run team, from Hana's pages; Wrenfield reviewed."),
          ("Which drill did Kemi fix alone, and how fast?", "Drill 3, the bad Halvorsen file, in 41 minutes."),
          ("Who signed the certificate?", "Kemi, Marta and Asif, countersigned by Hollis.")],
    quiz_sit=[("Rupert's office wants the handover finished a fortnight early to save money. What does Ines suggest?", "Keep the drills and the reverse shadowing; cut the remaining presentations instead. If time must be cut, do the riskiest tasks first and offer a short paid on-call period after.")],
    try_it="For something you run, list the three failures you've actually had. Could a colleague fix each one alone, at 03:00, from a runbook they wrote? Plan one drill.",
    remember="Handed over means <span class=\"hl\">they can do it without you</span>. Shadow, reverse-shadow, drill, and let <span class=\"hl\">the 03:00 people sign</span>.",
    late=dict(when="Fri 9 March 2029 · 20:40 · hotel near The Grid",
              lines=["Kemi fixed the bad Halvorsen file in 41 minutes. Tariq sat on his hands. Literally: Lottie took a photo.",
                     "“I'd take the call at three.” Best line on any certificate I've signed.",
                     "Bert added a page to their back-feed runbook. In pencil. They've scanned it."]),
    sources=["ITIL 4, <i>Service Transition</i> (knowledge management).",
             "Gene Kim et al., <i>The DevOps Handbook</i> (2016): game days.",
             "UK Government Digital Service, <i>Service Manual</i>: moving to live."],
)

# ------------------------------------------------------------------ 07 How Do We Run a Lessons Session Both Sides Attend?
jl_problem = Doodle(760, 240, "Doodle of the problems with a joint lessons session in March 2029. Phase 2 tender is open, so Vexmoor is a rival bidder. Rupert's office wants a list of supplier failures. Bert says the last lessons document he saw, from 2019, was never opened again. And everyone in the room has something to protect.",
                    "A tender open, a rival in the room, and a request for a list of failures.", exact=True)
for i, (t, fill) in enumerate([("tender open", "pink"), ("Vexmoor in the room", "blue"), ("“list of failures”", "pink"), ("2019 lessons: unopened", "paper")]):
    jl_problem.box(14 + (i % 2) * 374, 20 + (i // 2) * 90, 358, 70, t, fill, size=19)

jl_how = Doodle(760, 340, "The joint lessons session on Thursday 15 March 2029. Desmond's rules: no phase 2 discussion, the same notes published to every bidder. Blameless: describe what happened and what made sense at the time, never who. Everyone who did the work is invited: MetroVolt, Wrenfield, Halvorsen, Vexmoor. 63 sticky notes become 5 lessons, each with an owner and a date. Facilitator: Lottie.",
                "Rules from procurement, blameless, the doers in the room, and five lessons with owners.", exact=True)
jl_how.box(14, 20, 230, 110, "63", "y", sub="sticky notes", size=34, subsize=14)
jl_how.arrow(254, 75, 300, 75)
jl_how.box(310, 20, 230, 110, "5", "green", sub="lessons, owners, dates", size=34, subsize=14)
jl_how.box(560, 20, 186, 110, "Lottie", "blue", sub="facilitator", size=22, subsize=14)
jl_how.box(14, 160, 732, 70, "Desmond's rules: no phase 2 talk · same notes to every bidder · blameless", "paper", size=16)
jl_how.note(380, 290, "what happened, what made sense at the time; never who", "red", size=18)

JOINT_LESSONS = dict(
    slug="joint-lessons", date=date(2029, 3, 15), meta=on_site(date(2029, 3, 15)), where="RM 27B", pass_kind="contractor",
    kicker="a.k.a. a lessons session both sides attend",
    tldr="A lessons session run by one side becomes a list of the other side's failures. Run it <b>jointly</b>: client, vendors (even rivals) and <b>the people who did the work</b>. Make it <b>blameless</b>: what happened and why it made sense at the time, never who. Agree the <b>rules</b> with procurement if a tender is open. End with <b>a few lessons, each with an owner and a date</b>, not a document nobody reopens.",
    chips=[("Family", "handing it over"), ("Lives in", "lessons/lodestar-wave1.md · five owners"), ("Pairs with", "wave 1 night (vol. 4), handover architecture")],
    problem_side="Room 27B, 15 March 2029",
    problem="""  <p class="lead">Elaine wants a <b>lessons session</b> on wave 1 before phase 2 begins. The difficulties:</p>
  <ul>
    <li>The <b>phase 2 tender opened on 5 March</b>. Vexmoor and Wrenfield are rival bidders.</li>
    <li>Rupert's office asks for <span class="hl-pink">“a list of supplier failures”</span>.</li>
    <li>Bert says the last lessons document he saw, from 2019, was <b>never opened again</b>.</li>
    <li>Everyone in the room has something to protect: a bid, a budget, a reputation.</li>
  </ul>""",
    problem_figs=[jl_problem],
    sides=dict(client=("Elaine and Desmond", "<p>Elaine wants real lessons for phase 2, whoever wins it. Desmond wants the tender kept fair: anything said in the session mustn't give one bidder an advantage. Rupert's office wants something it can show the board.</p>", "Learn from it, without breaking the procurement."),
                vendor=("Ines", "<p>Wrenfield could use the session to look good before the bid, or keep quiet to avoid giving Vexmoor anything. Either would waste it. Ines suggests Lottie facilitates: junior, neutral, and the one who's asked the obvious questions for two years.</p>", "If it's honest, everyone learns, including us.")),
    sides_after="Lessons sessions fail when they're about blame or when nothing happens afterwards. Make them blameless, and make them small.",
    analogy_side="the air accident investigation",
    analogy="""  <p>Air accident investigators don't ask “whose fault was it?”. They ask <b>what happened, and why it made sense to the crew at the time</b>. Pilots, engineers and controllers talk freely because they won't be punished for honesty. The report ends in a short list of <b>recommendations, each sent to someone who must reply</b>. That's why flying keeps getting safer.</p>""",
    map=[("What happened, and why it made sense", "Blameless questions"),
         ("Pilots talking freely", "Every side, including Vexmoor and Halvorsen"),
         ("Not punished for honesty", "No names in the notes"),
         ("Recommendations with replies", "Five lessons, each with an owner"),
         ("Flying getting safer", "Phase 2 better, whoever wins")],
    how_side="agreed rules, blameless, the doers, a few lessons with owners",
    how="""  <p><b>Rules from procurement.</b> Desmond agrees the session if: <b>no phase 2 discussion</b>, both bidders invited, and the <b>same notes published to every bidder</b> through the tender portal. Rupert's office gets the same notes, not a list of failures.</p>
  <p><b>The doers in the room.</b> Twenty-four people: Elaine, Hollis, Rosa, Kofi, Bert, the run team, Wrenfield's team (Hana comes back for the day), Sven from Halvorsen, and from Vexmoor <b>Bea</b>, who worked on the acceleration review. Oliver declines; Bea comes anyway, with his blessing.</p>
  <p><b>Blameless.</b> Lottie opens with one rule: <i>“We talk about what happened and why it made sense at the time. Never who.”</i> When someone starts “Wrenfield should have…”, Lottie rewrites it on the board as “the plan assumed…”.</p>
  <p><b>From many to a few.</b> 63 sticky notes, grouped on the wall, voted on. <b>Five lessons</b> survive, each with an owner and a date:</p>
  <ol>
    <li>Profile real data before pricing (owner: Desmond, in the phase 2 tender rules).</li>
    <li>Test interfaces against the partner's real test system, early (Sven).</li>
    <li>Book a performance environment at the start (Hollis).</li>
    <li>Plan queue capacity for the cutover night, not the average day (Kemi).</li>
    <li>Measure team hours on fixed-price work (Elaine, as a phase 2 reporting line).</li>
  </ol>
  <p>Bea's sticky note, on the MetroBus queue, is the one that becomes lesson 4. Nobody says “Vexmoor” or “Wrenfield” in the notes.</p>""",
    how_figs=[jl_how],
    steps=[("Agree the rules with procurement", "If a tender is open."),
           ("Invite the doers, all sides", "Including rivals and partners."),
           ("Pick a neutral facilitator", "Junior is fine."),
           ("Make it blameless", "What happened and why; never who."),
           ("Converge to a few lessons", "Vote; keep five."),
           ("Give each an owner and a date", "And check them later.")],
    vocab=[("Lessons learned", "What a project changes in future work because of its experience."),
           ("Blameless review", "A review focused on systems and decisions, not people."),
           ("Retrospective", "A team's regular look back at how it worked."),
           ("Facilitator", "Someone who runs the session without taking a side."),
           ("Level playing field", "Procurement rule that no bidder gets an unfair advantage."),
           ("Action owner", "The person who must make a lesson happen.")],
    code=dict(file="lessons/lodestar-wave1.md", note="published to all phase 2 bidders · Fri 16 Mar 2029", src="""
LESSONS · Lodestar wave 1 · Thu 15 Mar 2029 · room 27B · facilitator: Lottie Marsh
rules      blameless · no phase 2 discussion · same notes to every bidder (Desmond)
attended   24 · MetroVolt, Wrenfield, Halvorsen, Vexmoor
input      63 sticky notes → 11 groups → 5 lessons

L1  profile real data before pricing          owner Desmond   phase 2 tender rules   ✓ 16 Mar
L2  test interfaces on the partner's real     owner Sven      by wave 2 design
    test system, early
L3  book a performance environment at start   owner Hollis    by wave 2 design
L4  plan queue capacity for cutover night     owner Kemi      by wave 2 rehearsal 1
L5  measure team hours on fixed-price work    owner Elaine    phase 2 reporting
review     each owner reports at the first phase 2 steering
"""),
    contract=dict(side="what the tender rules allow", doc="Phase 2 invitation to tender · §4 (conduct)", date="issued 5 Mar 2029", stamp="fair to all",
                  clauses=[("4.2", "Bidders shall not seek to discuss this procurement with MetroVolt staff other than through the tender portal.", "so: no phase 2 talk in the session. Lottie had a bell."),
                           ("4.5", "Any information MetroVolt gives to one bidder about this procurement will be given to all bidders.", "hence the notes on the portal, to everyone.")],
                  plain="during a live tender, every joint meeting is a procurement risk. Ask procurement for rules first; publishing the same notes to all bidders keeps it fair."),
    health=dict(now="g",
                g=("a blameless habit", ["Joint sessions after each wave.", "Few lessons, owned.", "Check them later."]),
                a=("a tender in the way", ["Procurement's rules.", "Publish to all.", "No talk of the next phase."]),
                r=("a blame hunt", ["Postpone it.", "Change the facilitator.", "Start with what made sense."])),
    pressure=dict(level=3, title="honesty in front of the rival", cost="your mistakes on the wall · the rival in the room",
                  items=["Wrenfield's mistakes are on the wall where Vexmoor can read them. So are everyone else's. That's the point.", "If the lessons help Vexmoor in phase 2, MetroVolt still benefits. That's the job too."]),
    baseline="Each line compares <b>a supplier-failure list for Rupert's office</b> with <b>a blameless joint session, fair rules, and five owned lessons</b>.",
    ratings=[(3, 5, "MetroVolt sees a supplier that shares its mistakes."),
             (3, 4, "The team's work is honoured, not blamed."),
             (3, 3, "A day of everyone's time."),
             (3, 4, "Lessons shape the phase 2 tender."),
             (3, 4, "Real causes, not stories."),
             (3, 4, "Phase 2 risks reduced for whoever wins."),
             (2, 4, "Procurement's rules followed."),
             (3, 3, "A day."),
             (3, 4, "Five lessons, not fifty.")],
    pitfalls=[("One side runs it", "It becomes a list of the other's failures.", "jointly."),
              ("Names in the notes", "People stop talking.", "what, not who."),
              ("Fifty lessons", "Nobody acts on any.", "five, with owners."),
              ("No owners or dates", "The 2019 document.", "owner, date, review."),
              ("Ignoring the tender", "Procurement challenge.", "agree rules, publish to all.")],
    grimoire=[(6, "frenemy-pact", "The Frenemy Pact", "is working with a rival when it helps the client.")],
    use=["After a major milestone or go-live.", "Before the next phase.", "When several suppliers did the work."],
    skip=["During an incident (do it after)."],
    related=["<b>What Did the Night Teach Us?</b> (vol. 4)", "<b>How Do We Share a Floor with the Rival?</b> (vol. 5)", "<b>What Should the Handover Architecture Say?</b> (next note)", "<b>What Did We Learn?</b> (Sanne, vol. 2)"],
    quiz=[("What rules did Desmond set?", "No phase 2 discussion, both bidders invited, the same notes published to every bidder."),
          ("What's the blameless rule?", "What happened and why it made sense at the time; never who."),
          ("How many sticky notes, and how many lessons?", "63 sticky notes, 5 lessons."),
          ("Who facilitated, and why?", "Lottie: junior, neutral, and good at the obvious questions."),
          ("Whose note became lesson 4?", "Bea's, from Vexmoor, on the MetroBus queue.")],
    quiz_sit=[("Halfway through, Graham (visiting) asks Elaine whether phase 2 will use wave 1's architecture. What does Lottie do?", "Ring the bell: no phase 2 discussion in this session; questions about the tender go through the portal. Then carry on.")],
    try_it="Take your last project's lessons document. How many lessons had an owner and a date? Pick the top three, give each an owner, and check them in a month.",
    remember="Blameless, joint, and small: <span class=\"hl\">five lessons with owners</span> beat fifty with none.",
    late=dict(when="Thu 15 March 2029 · 21:10 · hotel near The Grid",
              lines=["Lottie ran a room of 24, including Vexmoor and Halvorsen, and rang her bell twice. Once at Graham.",
                     "Bea's sticky note became lesson 4. I told her so at the lift. She looked surprised to be thanked.",
                     "Hana came for the day. She looked rested. She didn't say anything about phase 2, and I didn't ask."]),
    sources=["Sidney Dekker, <i>The Field Guide to Understanding 'Human Error'</i> (3rd ed., 2014).",
             "Norman Kerth, <i>Project Retrospectives</i> (2001).",
             "Google, <i>Site Reliability Engineering</i> (2016): blameless postmortems."],
)

# ------------------------------------------------------------------ 08 What Should the Handover Architecture Say?
ha_problem = Doodle(760, 240, "Doodle of what Lodestar's architecture currently is: 74 decision log entries, 11 interface agreements, a wiki of 410 pages, three versions of the context diagram, and the answers in Hana's head and Ines's notebook. In three months there will be nobody from Wrenfield to ask, if Wrenfield loses phase 2.",
                    "74 decisions, 410 wiki pages, three diagrams, and the reasons in two heads.", exact=True)
for i, (t, fill) in enumerate([("74 decisions", "y"), ("410 wiki pages", "paper"), ("3 context diagrams", "blue"), ("the why: in 2 heads", "pink")]):
    ha_problem.box(14 + (i % 2) * 374, 20 + (i // 2) * 90, 358, 70, t, fill, size=20)

ha_how = Doodle(760, 340, "The handover handbook, 22 pages. One page: the picture, the current context diagram, one version only. The decisions that matter: 12 of 74, each with the reason and what would change it. The known debts: 9, each with its cost and a suggested fix. How to change it safely: the contract tests, the rehearsal pattern, who to ask. And what we'd do differently.",
                "One picture, twelve decisions and why, nine debts, how to change it safely.", exact=True)
for i, (h, sub, fill) in enumerate([("1 picture", "one version", "y"), ("12 decisions", "and why", "blue"), ("9 debts", "cost, fix", "pink"), ("change safely", "tests, rehearsals", "green"), ("differently", "our regrets", "paper")]):
    ha_how.box(14 + i * 148, 20, 138, 110, h, fill, sub=sub, size=17, subsize=12)
ha_how.box(14, 160, 732, 70, "Lodestar architecture handbook v1.0 · 22 pages · adopted by Hollis as the design authority template", "green", size=15)
ha_how.note(380, 290, "hand over the why, not just the what", "red", size=19)

HANDOVER_ARCH = dict(
    slug="handover-architecture", date=date(2029, 3, 23), meta=on_site(date(2029, 3, 23)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. the architecture you leave behind",
    tldr="When the supplier leaves, the reasons leave with it. Hand over a short <b>architecture handbook</b>: <b>one picture</b> (one version), <b>the decisions that matter and why</b>, with what would change them, <b>the known debts</b> with costs and fixes, <b>how to change it safely</b>, and <b>what you'd do differently</b>. Twenty pages someone reads beat four hundred nobody does.",
    chips=[("Family", "handing it over"), ("Lives in", "architecture/lodestar-handbook-v1.md · 22 pages"), ("Pairs with", "the decision log (vol. 2), knowledge transfer")],
    problem_side="Floor 19, 23 March 2029",
    problem="""  <p class="lead">Lodestar's architecture is spread across:</p>
  <ul>
    <li><b>74 decision log entries</b> (DL-001 to DL-074), some superseded.</li>
    <li><b>11 interface agreements</b>, IA-01 to IA-11.</li>
    <li>A wiki of <b>410 pages</b>, many out of date.</li>
    <li><b>Three versions</b> of the context diagram, each slightly different.</li>
    <li>And <span class="hl-pink">the reasons, mostly in Hana's head and Ines's notebook</span>. If Wrenfield loses phase 2, nobody from Wrenfield will be there to ask.</li>
  </ul>""",
    problem_figs=[ha_problem],
    sides=dict(client=("Hollis", "<p>Hollis's design authority will own Lodestar's architecture after wave 1, possibly with Vexmoor building phase 2 on it. He needs to know what can change, what mustn't, and why each odd-looking decision was made, so that nobody “fixes” something that was deliberate.</p>", "Tell me why, so we don't undo it by accident."),
                vendor=("Ines", "<p>Ines could hand over everything: all 410 pages, all 74 decisions. That would satisfy the contract and help nobody. Writing it short means choosing what matters, and admitting the debts and regrets in writing, possibly for a rival to read.</p>", "The short version is harder. And it's the only one they'll read.")),
    sides_after="The most valuable part of an architecture handover is the reasons: without them, the next team will undo good decisions and keep bad ones.",
    analogy_side="the house handbook",
    analogy="""  <p>When you sell a house you've renovated, the best thing to leave is a short <b>house handbook</b>: where the stopcock is, why the kitchen wall can't come down (it's holding up the bathroom), which bit of the roof needs doing in five years, and the builder's number. Not every receipt. The new owners need the few things that would hurt if they didn't know them.</p>""",
    map=[("Where the stopcock is", "The one-page picture"),
         ("The wall that can't come down", "Decisions that matter, and why"),
         ("The roof in five years", "Known debts, with costs"),
         ("The builder's number", "How to change it safely, who to ask"),
         ("Every receipt", "The 410-page wiki (archived, not handed over)")],
    how_side="one picture, the decisions and why, the debts, changing safely, regrets",
    how="""  <p>Ines, Tariq and Bilal write <b>Lodestar architecture handbook v1.0</b>: <b>22 pages</b>, reviewed by Hollis and the run team.</p>
  <ul>
    <li><b>One picture.</b> A single context diagram, version-controlled; the other two are archived with a note saying so.</li>
    <li><b>Twelve decisions that matter</b> out of 74, each with its <b>reason</b> and <b>what would change it</b>: e.g. DL-012, the anti-corruption layer around MAVIS (“remove only when MAVIS is switched off”); DL-047, velocity planned at 38; the back-feed's queue limit after wave 1 night.</li>
    <li><b>Nine known debts</b>, each with an estimated cost and a suggested fix: the manual workaround for the 3 excluded accounts; ten years of meter history only readable in MAVIS (CR-019); the arrears report index.</li>
    <li><b>How to change it safely</b>: run the contract tests, rehearse any migration twice, ask the design authority, and check the runbooks.</li>
    <li><b>What we'd do differently</b>: book the performance environment on day 1; profile all the data, not a sample; plan for the queue, not the average.</li>
  </ul>
  <p>The handbook is written so that <b>whoever builds phase 2</b> can use it, Vexmoor included. Hollis adopts its structure as the template for every supplier handover from April.</p>""",
    how_figs=[ha_how],
    steps=[("Draw one picture", "Archive the rest, with a note."),
           ("Pick the decisions that matter", "With the reason and what would change it."),
           ("List the known debts", "Cost and suggested fix."),
           ("Explain how to change it safely", "Tests, rehearsals, who to ask."),
           ("Write what you'd do differently", "Honestly."),
           ("Review it with the new owners", "Then let them own it.")],
    vocab=[("Architecture handbook", "A short document explaining a system's design and its reasons."),
           ("Architecture decision record", "A note of one decision, its context and consequences."),
           ("Technical debt", "Shortcuts that cost more to change later."),
           ("Context diagram", "A picture of a system and what it connects to."),
           ("Design authority", "The client group that approves architectural changes."),
           ("Fitness function", "An automated check that an architectural property still holds.")],
    code=dict(file="architecture/lodestar-handbook-v1.md", note="v1.0 · Fri 23 Mar 2029 · reviewed by Hollis Wade", src="""
LODESTAR ARCHITECTURE HANDBOOK v1.0 · 22 pages

1  the picture            one context diagram (v4); v1–v3 archived with a note
2  12 decisions that matter (of DL-001…DL-074)
   DL-012 anti-corruption layer around MAVIS · change: only when MAVIS is off
   DL-047 plan velocity 38, not 45          · change: after 3 waves of data
   DL-062 MetroBus queue limit (wave 1 night) · change: never without a load test
   …
3  9 known debts          D-1 manual handling, 3 excluded accounts (≈ 2 days/yr) ·
                          D-4 meter history readable only in MAVIS (CR-019, ≈ £140k) · …
4  changing it safely     contract tests · rehearse migrations twice · DA approval ·
                          update the runbooks
5  what we'd do differently  perf environment on day 1 · profile all data ·
                             plan for the queue, not the average
"""),
    contract=dict(side="what the exit clause asks for", doc="Lodestar SOW · Schedule 10 (exit) · §4", date="signed 30 June 2027", stamp="delivered",
                  clauses=[("Sch. 10, 4.1", "On exit, the Supplier shall deliver documentation sufficient for MetroVolt or a Replacement Supplier to operate, maintain and develop the solution.", "“or a Replacement Supplier”. we wrote it for Vexmoor too."),
                           ("Sch. 10, 4.2", "Documentation includes the design, the key decisions and their rationale, and known defects and limitations.", "rationale and limitations: the parts suppliers usually leave out.")],
                  plain="exit schedules often require rationale and known limitations, not just design. Those are the parts most worth writing, and the hardest to write honestly."),
    health=dict(now="g",
                g=("a readable handbook", ["Short, owned, reviewed.", "Reasons included.", "Debts admitted."]),
                a=("documents but no reasons", ["Pick the key decisions.", "Add the why.", "List the debts."]),
                r=("supplier leaves tomorrow", ["One picture and the top five decisions today.", "Record a walkthrough.", "Names to ask."])),
    pressure=dict(level=2, title="your regrets in writing", cost="22 pages a rival may read · the debts admitted",
                  items=["Writing “what we'd do differently” while bidding against Vexmoor feels like a gift to them. It's a gift to MetroVolt.", "A handbook that hides the debts gets found out by the first person who changes the system."]),
    baseline="Each line compares <b>handing over the 410-page wiki and 74 decisions</b> with <b>a 22-page handbook: one picture, twelve decisions and why, nine debts, how to change safely, regrets</b>.",
    ratings=[(3, 5, "Hollis can own it."),
             (3, 4, "The reasons outlive the people."),
             (3, 3, "Two weeks of writing."),
             (3, 3, "Neutral."),
             (2, 5, "Deliberate decisions protected from being undone."),
             (2, 4, "Debts visible to the next team."),
             (3, 4, "Schedule 10 met in substance."),
             (3, 3, "Two weeks."),
             (3, 4, "22 pages to keep current, not 410.")],
    pitfalls=[("Handing over everything", "Nobody reads it.", "the 22 pages that matter."),
              ("Design without reasons", "Good decisions get undone.", "why, and what would change it."),
              ("Hiding the debts", "The next team finds them painfully.", "list them, with costs."),
              ("Several pictures", "Nobody knows which is true.", "one, versioned."),
              ("Writing it alone", "The owners don't trust it.", "review it with them.")],
    grimoire=[(8, "phylactery-of-paper", "The Phylactery of Paper", "is the inside version: keeping the record that protects you, and them.")],
    use=["At the end of any supplier engagement.", "When the build team changes.", "Before a phase handed to another supplier."],
    skip=["Never; shorten it, but keep the reasons."],
    related=["<b>Who Decides What, and Where?</b> (vol. 2)", "<b>How Do We Hand It Over So It Sticks?</b> (this volume)", "<b>How Do We Strangle a Customer System?</b> (vol. 3)", "<b>Architecture Decision Records</b> (Ana, vol. 1)"],
    quiz=[("What were the architecture's pieces before the handbook?", "74 decisions, 11 interface agreements, a 410-page wiki, three context diagrams, and reasons in two heads."),
          ("What five sections does the handbook have?", "One picture, the decisions that matter, known debts, how to change safely, what we'd do differently."),
          ("How many decisions were included?", "Twelve of 74, each with the reason and what would change it."),
          ("What does Schedule 10 require?", "Documentation sufficient for MetroVolt or a replacement supplier, including rationale and limitations."),
          ("What did Hollis do with it?", "Adopted its structure as the template for supplier handovers.")],
    quiz_sit=[("Callum asks whether to leave the “what we'd do differently” section out until the phase 2 decision. What does Ines say?", "No: it's part of what MetroVolt needs, whoever wins, and Schedule 10 asks for limitations. Leaving it out would look worse when found. Write it plainly and without blame.")],
    try_it="For a system you know, write the twelve decisions that matter in one line each, with the reason and what would change it. Which one is most likely to be undone by accident?",
    remember="Hand over <span class=\"hl\">the why</span>, not just the what: one picture, the key decisions, <span class=\"hl\">the debts admitted</span>.",
    late=dict(when="Fri 23 March 2029 · 19:50 · train to Leeds",
              lines=["Handbook v1.0 is with Hollis. 22 pages. Section 5 was the hardest to write and the first he read.",
                     "He's using it as the template for every supplier from April. Vexmoor's handover too, one day.",
                     "The phase 2 bid is due in twelve days. Callum's been in Leeds all week. Tomorrow, so am I."]),
    sources=["Michael Nygard, “Documenting Architecture Decisions” (2011).",
             "Simon Brown, <i>The C4 model for visualising software architecture</i>.",
             "Neal Ford, Rebecca Parsons and Patrick Kua, <i>Building Evolutionary Architectures</i> (2017)."],
)

NOTES = [WARRANTY, KNOWLEDGE_TRANSFER, JOINT_LESSONS, HANDOVER_ARCH]
