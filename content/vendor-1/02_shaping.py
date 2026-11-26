# Series 5 · On the Client's Floor · Vol. 1 · Winning the Work · Shaping the answer (notes 5–8).
from datetime import date

# ------------------------------------------------------------------ 05 How Do I Design on Two Pages of Facts?
sd_problem = Doodle(760, 250, "Doodle of what Ines knows about MAVIS on 8 March 2027: two pages of the tender, section 3, describing a 1997 COBOL system on a mainframe with 2.31 million live accounts, a nightly batch, and a file to Halvorsen billing at 02:10. Everything else is a question mark: data quality, change detection, who knows the code, the size of the batch.",
                    "Two pages of facts, and a wall of question marks.", exact=True)
sd_problem.box(24, 20, 220, 200, None, "paper", rx=4)
sd_problem.head(134, 50, "ITT §3 · MAVIS", size=19)
for i, t in enumerate(["1997 · COBOL", "mainframe", "2.31m live accounts", "nightly batch", "02:10 → Halvorsen"]):
    sd_problem.text(134, 84 + i * 28, t, size=16)
for i, t in enumerate(["data quality?", "what changed today?", "who knows the code?", "how big is the batch?", "the Orion hub?", "Halvorsen's interface?"]):
    c, r = divmod(i, 3)
    sd_problem.box(290 + c * 230, 24 + r * 66, 210, 54, t, "pink", size=17)
sd_problem.note(500, 236, "design anyway, and say what you don't know", "red", size=19)

sd_how = Doodle(760, 360, "Three options for Lodestar on one page. Option A: big bang, a new customer platform for all 2.3 million accounts in one cutover; fast if it works, catastrophic if it doesn't. Option B: wrap and extend, put APIs in front of MAVIS and keep the mainframe; cheap and safe, but MAVIS never leaves and Bert retires in 2029. Option C: strangle in waves, a new customer platform takes districts one at a time while MAVIS shrinks; first value in nine months, each wave a rehearsal for the next. C is chosen, with three things to learn in discovery.",
                "Three honest options, scored the same way. C wins on how it fails, not on how it looks.", exact=True)
opts = [("A · big bang", "pink", ["all 2.3m in one night", "fast, if it works", "fails all at once", "Orion's shape"]),
        ("B · wrap MAVIS", "y", ["APIs in front", "cheap and safe", "MAVIS never leaves", "Bert retires 2029"]),
        ("C · waves", "green", ["districts one by one", "first value: month 9", "fails one wave", "each wave rehearses"])]
for i, (h, fill, lines) in enumerate(opts):
    x = 14 + i * 250
    sd_how.box(x, 14, 232, 50, h, fill, size=20)
    sd_how.box(x, 72, 232, 170, None, "paper", rx=4)
    for r, t in enumerate(lines):
        sd_how.text(x + 116, 104 + r * 36, t, size=17)
sd_how.box(514, 252, 232, 92, "learn in discovery", "blue", sub="data · changes · billing", size=18, subsize=16)
sd_how.note(250, 290, "judge each by how it fails", "red", size=20)

SOLUTION_TWO_PAGES = dict(
    slug="solution-on-two-pages", date=date(2027, 3, 9), meta="bid day 35 of 50", where="LEEDS",
    kicker="a.k.a. “the solution outline” or “bid architecture”",
    tldr="In a bid you design with almost no facts. Do it honestly: put <b>three real options</b> side by side (not one favourite and two straw men), judge them on the same few criteria (<b>especially how each one fails</b>), choose one you can <b>draw on a single page</b>, and write down <b>what you must learn before you commit</b>. Pitch the design at the level you'd be happy to be held to, because the bid design often becomes part of the contract.",
    chips=[("Family", "shaping the answer"), ("Lives in", "bid section 3 + appendix A (options)"), ("Pairs with", "assumptions, estimating, the strangler fig")],
    problem_side="Wrenfield, 9 March 2027",
    problem="""  <p class="lead">Everything Wrenfield knows about MAVIS fits on <b>two pages</b> of the tender: written in <b>1997</b>, COBOL on a mainframe, <b>2.31 million live accounts</b>, a nightly batch, and a file sent to Halvorsen billing at <b>02:10</b>. The clarification answers added one fact: MAVIS can't say what changed during the day, only produce a nightly extract.</p>
  <ul>
    <li>The bid needs a solution section worth <b>20 % of the quality score</b>, in six pages.</li>
    <li>Hana has a favourite design (an event stream off the mainframe's logs). It's elegant. <span class="hl-pink">Nobody knows yet if MAVIS can feed it.</span></li>
    <li>The tender says the bid's design <b>“will form Schedule 2 of the contract”</b>. Whatever Wrenfield draws, it may have to build.</li>
  </ul>""",
    problem_figs=[sd_problem],
    sides=dict(client=("Hollis will score it", "<p>Hollis has seen Orion's beautiful architecture diagrams, and a project that never went live. He'll score <b>how believable</b> the design is, not how modern. He wants to see that the bidder understood MAVIS and has a plan for the parts nobody understands yet.</p>", "Show me you know what you don't know."),
                vendor=("Ines and Hana draw it", "<p>Ines needs a design that scores well, can be priced, and won't trap Wrenfield if MAVIS turns out worse than two pages suggest. Hana needs her idea taken seriously. Both need the design <b>at the right level</b>: firm about the approach, open about the mechanisms.</p>", "Commit to the shape, not to the plumbing.")),
    sides_after="The level of detail is the real decision. Too vague and it scores badly; too detailed and Schedule 2 locks you into a guess.",
    analogy_side="the architect's sketch before the survey",
    analogy="""  <p>An architect asked to extend an old house sketches <b>three options</b> before the structural survey: a full rebuild, a rear extension, or converting room by room while the family lives there. She can say which one she recommends and why, but she writes <b>“subject to survey”</b> on the drawing, and she doesn't specify the steel beams yet.</p>""",
    map=[("Full rebuild", "A · big bang: everything in one cutover"),
         ("Rear extension", "B · wrap and extend MAVIS with APIs"),
         ("Room by room, family still living there", "C · strangle MAVIS in waves"),
         ("“Subject to survey”", "“To be confirmed in discovery”"),
         ("The steel beam spec", "The change-detection mechanism (not in the bid)")],
    how_side="three real options, one page, and what you must learn",
    how="""  <p>Ines and Hana write three options that a reasonable person could choose. <b>A · big bang</b>: a new platform for all 2.3 million accounts in one cutover. <b>B · wrap and extend</b>: put APIs in front of MAVIS and keep the mainframe. <b>C · strangle in waves</b>: a new customer platform takes one district at a time while MAVIS shrinks.</p>
  <p>They score all three on the same five criteria: <b>time to first value</b>, <b>cost</b>, <b>risk</b>, <b>fit with phase 2</b>, and <b>how it fails</b>. That last one decides it. A fails all at once, which is how Orion was shaped. B never fails, and never finishes: MAVIS stays, and its last COBOL expert retires in 2029. C fails <b>one wave at a time</b>, and every wave is a rehearsal for the next.</p>
  <p>The bid commits to the <b>shape</b> (waves, a new customer platform, MAVIS read-only for migrated districts, Halvorsen kept) and lists the mechanisms as <b>“to be confirmed in discovery”</b>: how to detect changes in MAVIS (Hana's event stream is option 1 of 3), how to reconcile records, and the Halvorsen interface. One context diagram, one wave diagram, two pages.</p>""",
    how_figs=[sd_how],
    steps=[("List what you know and what you don't", "Two columns, before any drawing."),
           ("Write three real options", "Ones a reasonable person could choose. No straw men."),
           ("Score them on the same criteria", "Include “how does it fail?”"),
           ("Choose, and say why in one sentence", "The sentence goes in the bid."),
           ("Commit to the shape, not the plumbing", "Mechanisms you can't know yet: “confirmed in discovery”."),
           ("Draw it on one page", "If it needs three, the panel won't believe it either.")],
    vocab=[("Solution outline", "A bid-level design: the approach, the main parts and the main risks."),
           ("Options analysis", "Comparing several real designs against the same criteria."),
           ("Strangler fig", "Replacing an old system piece by piece while it keeps running."),
           ("Big bang", "Switching everything over at once."),
           ("Schedule", "An attachment to a contract; a design in a schedule becomes a commitment."),
           ("Context diagram", "One picture: the system, its users and its neighbours.")],
    code=dict(file="bid/lodestar/appendix-a-options.md", note="Ines and Hana · Tue 9 Mar 2027", src="""
OPTIONS · LODESTAR phase 1                 score 1 (bad) – 5 (good)

criterion             A big bang    B wrap MAVIS    C waves
time to first value       2              5             4   (month 9)
cost (phase 1)            2              5             3
delivery risk             1              4             3
fit with phase 2          3              1             5
how it fails              1 (all)        4 (never      4 (one wave)
                                           finishes)
total                     9             19            19
tie-break: B leaves MAVIS and its last expert (retires 2029) in place → C

committed in the bid (Schedule 2):  waves by district · new customer platform ·
  MAVIS read-only for migrated districts · Halvorsen billing kept
confirmed in discovery:  change detection (3 options) · reconciliation · billing interface
"""),
    contract=dict(side="what the tender does with your design", doc="Lodestar ITT · draft contract terms", date="3 Feb 2027", stamp="becomes schedule 2",
                  clauses=[("3.1", "The Supplier's solution as described in its tender response shall form Schedule 2 (Solution) of the Contract.", "so “event stream” in the bid = “event stream” in the contract."),
                           ("3.3", "Elements of Schedule 2 identified as subject to discovery may be refined by agreement following the discovery phase without a Change Request, provided the Charges are unaffected.", "the escape hatch. use it on purpose.")],
                  plain="your bid design can become a contract schedule. Be precise about the approach you'll stand behind, and label the mechanisms you can't know yet as subject to discovery, so refining them later isn't a change request."),
    health=dict(now="a",
                g=("you've seen the system before", ["Options can be more detailed.", "Fewer “to be confirmed”s.", "Still show how it fails."]),
                a=("two pages of facts", ["Three real options, one choice.", "Commit to the shape only.", "List what discovery must answer."]),
                r=("the client wants a fixed design now", ["Price the uncertainty explicitly.", "Offer a paid discovery instead.", "Don't sign a design you've never seen running."])),
    pressure=dict(level=3, title="design week", cost="one favourite idea demoted to “option 1 of 3”",
                  items=["Hana's event stream isn't rejected; it's postponed until there's evidence. Say that out loud.", "Designing without facts is stressful because you're scared of being wrong. Writing down what you don't know is the cure."]),
    baseline="Each line compares <b>bidding one favourite, fully detailed design</b> with <b>three options, one shape committed, mechanisms left to discovery</b>.",
    ratings=[(3, 4, "Hollis sees that Wrenfield knows what it doesn't know."),
             (3, 4, "Nobody has to defend a guess for a year."),
             (2, 4, "The contract doesn't lock in an unproven mechanism."),
             (2, 4, "The shape is clear; the open points are listed."),
             (3, 5, "Chosen on how it fails, not on how it looks."),
             (2, 4, "Three discovery questions, named."),
             (3, 4, "The options table shows why C was chosen."),
             (4, 3, "Two days of options work."),
             (4, 4, "Two pages.")],
    pitfalls=[("Straw-man options", "Two silly options and the favourite.", "three a reasonable person could choose."),
              ("Over-specifying in the bid", "Unproven plumbing ends up in Schedule 2.", "commit to the shape; label mechanisms “subject to discovery”."),
              ("Never asking how it fails", "Options are compared on cost and speed only.", "add “how does it fail?” as a criterion."),
              ("A twelve-box diagram", "Nobody believes what they can't follow.", "one page, one picture."),
              ("Hiding what you don't know", "The panel knows MAVIS is a mystery.", "list the unknowns; it reads as competence.")],
    use=["Any bid with a solution section.", "Legacy replacements where you can't see inside.", "When the team has a favourite design.", "When the bid becomes a contract schedule."],
    skip=["You already run the system and know its insides: go straight to a detailed design."],
    related=["<b>What Are We Assuming?</b> (next note)", "<b>Strangler Fig</b> (patterns, Vol. 1)", "<b>Options Analysis</b> (Ana, vol. 2)", "<b>How Do I Read a Tender?</b> (this volume)"],
    quiz=[("Why three options?", "So the choice is visible and defensible; one option looks like a favourite, two look like a straw man."),
          ("Which criterion decided Lodestar's design?", "How each option fails: big bang fails all at once; waves fail one at a time."),
          ("Why not choose “wrap and extend”?", "MAVIS would never leave, and its last COBOL expert retires in 2029."),
          ("What does “commit to the shape, not the plumbing” mean?", "Promise the approach (waves, new platform), but leave unproven mechanisms to discovery."),
          ("Why does the level of detail matter in this tender?", "The bid design becomes Schedule 2 of the contract.")],
    quiz_sit=[("Hana insists the event stream must be in the bid because it's “the best design”. What do you say?", "It may well be, and it's option 1 of 3 for change detection. Until discovery shows MAVIS can feed it, putting it in Schedule 2 would make a guess contractual.")],
    try_it="Take a design decision you face. Write three options a reasonable person could choose, score them on five criteria including “how does it fail?”, and list what you'd need to learn before committing. Can you draw the winner on one page?",
    remember="Commit to <span class=\"hl\">the shape</span>. Leave <span class=\"hl\">the plumbing</span> to discovery. Choose by <span class=\"hl\">how it fails</span>.",
    late=dict(when="Tue 9 March 2027 · 23:20 · Leeds",
              lines=["Three options on one page. Big bang, wrap, waves. Waves.",
                     "Hana's event stream is “option 1 of 3, subject to discovery”. She said “fine” in the voice that means it isn't. I'll make sure discovery tests it first.",
                     "What I really know about MAVIS fits on two pages. What I'm promising fits on two pages too. That feels right."]),
    sources=["Martin Fowler, “StranglerFigApplication” (martinfowler.com, 2004).",
             "Simon Brown, <i>Software Architecture for Developers</i> (2018): the C4 model.",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020)."],
)

# ------------------------------------------------------------------ 06 What Are We Assuming? (the sample note, approved 25 Nov 2026)
as_problem = Doodle(720, 300, "Vivian's draft with three vague assumptions, next to Ines's stack of index cards: A1-07, no more than 5 per cent of records fail the address check, owner MetroVolt, tested on a sample by 1 April, and if false a priced change request. And 40 more cards.",
                    "Three vague lines protect nobody. One line with a number, an owner and a test date can be priced.", exact=True)
as_problem.box(28, 34, 270, 214, None, "paper", rx=4)
as_problem.head(46, 70, "Draft v3 · Vivian", anchor="start", size=20)
as_problem.line("M46 82 h232", thin=True)
for i, t in enumerate(["1. Client cooperates", "2. Access provided", "3. Reasonable data"]):
    as_problem.text(46, 116 + i * 34, t, anchor="start", size=19)
as_problem.line("M190 170 q40 -6 76 4", color="red")
as_problem.note(186, 230, "“reasonable”?", "red", anchor="start", size=21)
as_problem.arrow(318, 140, 376, 140, color="pen")
as_problem.box(430, 20, 262, 150, None, "y", rx=3)
as_problem.box(418, 32, 262, 150, None, "blue", rx=3)
as_problem.box(404, 48, 270, 170, None, "paper", rx=3)
as_problem.head(420, 82, "A1-07 · data", anchor="start", size=20)
as_problem.line("M420 94 h236", thin=True)
for i, t in enumerate(["≤ 5 % records fail", "owner: MetroVolt", "test: sample, 1 Apr"]):
    as_problem.text(420, 124 + i * 30, t, anchor="start", size=19)
as_problem.note(420, 210, "if false: CR, priced", "red", anchor="start", size=19)
as_problem.note(470, 274, "…and 40 more cards", "pen", anchor="start", size=21)

as_analogy = Doodle(720, 300, "A house with the wall cut open to show hatched asbestos, and a builder's quote for 18,400 pounds listing what it assumes and excludes: assumes no asbestos, excludes rewiring, we'll know on day 2, if found priced extra, signed by both.",
                    "Nobody can see inside the wall. The quote says what you both hope is there, and what happens if it isn't.", exact=True)
as_analogy.line("M40 130 L170 50 L300 130")
as_analogy.box(58, 130, 224, 140, None, "paper", rx=2)
as_analogy.box(120, 150, 96, 100, None, "pink", rx=2)
as_analogy.line("M124 166 l20 -14 M124 186 l46 -34 M124 206 l72 -52 M124 226 l88 -66 M136 246 l78 -60 M164 246 l50 -38 M192 246 l22 -16", color="red", thin=True)
as_analogy.note(104, 292, "1970s wall", "pen", anchor="start", size=20)
as_analogy.arrow(310, 170, 350, 170, color="pen")
as_analogy.box(380, 30, 300, 240, None, "paper", rx=3)
as_analogy.head(400, 66, "QUOTE £18,400", anchor="start", size=21)
as_analogy.line("M400 78 h260", thin=True)
for i, t in enumerate(["assumes: no asbestos", "excludes: rewiring", "we'll know: day 2"]):
    as_analogy.text(400, 112 + i * 34, t, anchor="start", size=19)
as_analogy.note(400, 214, "if found: priced extra", "red", anchor="start", size=19)
as_analogy.note(400, 252, "signed by both", "pen", anchor="start", size=20)

as_how = Doodle(770, 270, "The life of an assumption: write it in the bid in March, price it, sign it in SOW section 3, test it in discovery, and reach a verdict. True means nothing to do. False means a change request, priced. A1-07 is tested in December 2027.",
                "An assumption that never reaches the contract, or is never tested, protects nobody.", exact=True)
for i, (h, sub, fill) in enumerate([("Write it", "bid, March", "y"), ("Price it", "in the £", "paper"), ("Sign it", "SOW §3", "blue"), ("Test it", "discovery", "paper"), ("Verdict", "true / false", "y")]):
    as_how.box(16 + i * 150, 40, 124 if i < 4 else 140, 70, h, fill, sub=sub, size=20, subsize=17)
    if i:
        as_how.line(f"M{16 + i * 150 - 26} 75 h24", thin=True)
as_how.line("M650 112 q-40 40 -90 66", color="green")
as_how.line("M700 112 q10 40 0 66", color="red")
as_how.box(440, 180, 140, 50, "✓ nothing", "green", size=19)
as_how.box(616, 180, 140, 50, "CR, priced", "pink", size=19)
as_how.note(16, 160, "A1-07 is tested in December 2027.", "pen", anchor="start", size=21)
as_how.note(16, 190, "(Remember that date.)", "pen", anchor="start", size=21)

ASSUMPTIONS = dict(
    slug="assumptions", date=date(2027, 3, 11), meta="bid day 37 of 50", where="FL 19",
    kicker="a.k.a. “assumptions, dependencies and exclusions” · the most important page of the bid",
    tldr="A fixed price is only fixed <b>for the world you priced</b>. Write that world down as three lists: <b>assumptions</b> (what we believe is true), <b>dependencies</b> (what the client must do, by when) and <b>exclusions</b> (what we aren't doing). Each line needs <b>a number, an owner, a test date and what happens if it's false</b>. Then get the lists into the contract. A risk you don't write down is a risk you've agreed to carry, at a fixed price.",
    chips=[("Family", "shaping the answer"), ("Lives in", "bid appendix C, then SOW §3"), ("Pairs with", "estimating in fog, change control, the discovery report")],
    timesheet=dict(week="w/c 8 Mar 2027", label="Lodestar bid (pre-sales)", booked=[7.5, 7.5, 7.5, 7.5, 7.5, 0, 0], worked=[9.0, 10.5, 11.0, 12.5, 9.5, 4.0, 3.0],
                   note="billable this week: 0.0. Bids are paid for by the deals you win."),
    problem_side="Wrenfield and MetroVolt, March 2027",
    problem="""  <p class="lead">The Lodestar bid is due on <b>24 March</b>: <b>£4.8m fixed price</b> to move MetroVolt's first <b>380,000 customer accounts</b> off MAVIS, a customer system written in 1997. Vivian's draft of the bid has an assumptions page. It has <b>three lines</b>.</p>
  <ul>
    <li><b>Wed 10 March, 18:40, Leeds.</b> Vivian's draft: “1. MetroVolt will cooperate. 2. Access will be provided. 3. Data will be of reasonable quality.” Price: £4.8m.</li>
    <li><b>Thu 11 March, 10:00, The Grid, floor 19.</b> The bidders' meeting. Desmond Rook (procurement) takes questions in writing only. Ines asks how many customer records fail the address check. The written answer: “MetroVolt's data is of good quality.” No number.</li>
    <li><b>10:52.</b> Elaine Corbett, the programme director, says it out loud: “Orion's vendor had <b>four</b> assumptions. We paid for every one of them.”</li>
    <li><b>12:15, the lift.</b> A young analyst (Pip, his badge says) sees the Wrenfield lanyard and says quietly: “If you're pricing the data, ask for a sample. Nobody's looked since 2014.”</li>
    <li><b>Thursday night.</b> Ines and Hana write down everything that would ruin the price if it turned out wrong. By 23:00 the list has <b>41 lines</b>.</li>
  </ul>""",
    problem_figs=[as_problem],
    sides=dict(client=("Elaine reads it", "<p>A long list of assumptions looks like a vendor <b>building exits</b>. Orion's vendor had four, and MetroVolt still paid for each one in change requests. Elaine has a board to face, and the board wants one number.</p>", "Will they hide behind these when it slips?"),
               vendor=("Ines writes it", "<p>Each line is a risk Wrenfield can <b>price</b>, <b>share</b> or <b>hand back</b>. Anything not written down belongs to Wrenfield by default, at a fixed price, for an 80-person firm. Lodestar would be a third of next year's revenue.</p>", "If they think 5 % is unfair, I want to hear it now, not in December.")),
    sides_after="They are both right. The client fears exits; the vendor fears an open cheque. A good list answers both: <b>few enough to read, specific enough to test, and fair enough that the client could have written it.</b>",
    analogy_side="the builder's quote that says “assumes no asbestos”",
    analogy="""  <p>A builder quotes <b>£18,400</b> to knock through a wall in a 1970s house. The quote says: <i>assumes no asbestos; excludes rewiring; if asbestos is found, removal is priced separately</i>. That isn't the builder being difficult. Nobody can see inside the wall until it's open. The quote names what's in the wall, who pays if it's there, and when you'll both find out.</p>""",
    analogy_figs=[as_analogy],
    map=[("The wall nobody can see inside", "MAVIS: 4 million lines of COBOL, 30 years of data"),
         ("Assumes no asbestos", "A1-07: no more than 5 % of records fail the address check"),
         ("Excludes rewiring", "X-02: rework of the 02:10 MAVIS → Halvorsen batch job"),
         ("“We'll know on day 2”", "a 10,000-record sample by 1 April; full profiling in discovery"),
         ("Priced separately if found", "a change request under SOW clause 7")],
    how_side="three lists, four boxes per line",
    how="""  <p>Split everything you're unsure of into <b>three lists</b>:</p>
  <ul>
    <li><b>Assumptions:</b> things you believe are true and have priced on. “No more than 5 % of records fail address validation.”</li>
    <li><b>Dependencies:</b> things someone else must do, by a date. “Halvorsen provides the billing interface spec by 30 July 2027.”</li>
    <li><b>Exclusions:</b> work you're not doing, named so nobody assumes you are. “Training beyond 40 super-users.”</li>
  </ul>
  <p>Then every line must fill <b>four boxes</b>: a <b>number</b> (not “reasonable”), an <b>owner</b>, a <b>test</b> (how and when you'll find out) and a <b>consequence</b> (what happens to the price or the date if it's false). A line that can't fill all four is a worry, not an assumption. Move it to the risk log.</p>""",
    how_figs=[as_how],
    steps=[("Read the tender for every “will”", "“The supplier will migrate all customer data.” Each one hides an assumption about what that data is like."),
           ("Ask the team what would ruin the price", "Twenty minutes, everyone, sticky notes. Engineers know where the asbestos is."),
           ("Fill the four boxes", "Number, owner, test, consequence. If a line can't, it goes to the risk log."),
           ("Decide for each: carry, share or hand back", "Carry it (add contingency), share it (a rate per unit above the line) or hand it back (exclude it, openly)."),
           ("Put the top eight in the bid itself", "The rest go in an appendix, grouped. Forty-one lines on page 3 read like fear."),
           ("Get them into the contract", "A clause that says what happens when one is false (SOW §3, below)."),
           ("Test the dangerous ones first", "Ask for a data sample before you sign, if you can. Book the rest into discovery with dates.")],
    vocab=[("Assumption", "Something believed true and priced on. If it's false, the price or date changes."),
           ("Dependency", "Something another party must deliver, by a date, for you to deliver."),
           ("Exclusion", "Work you are explicitly not doing."),
           ("Contingency", "Money or time in the price for risks you carry yourself."),
           ("Relief", "The contract lets you move a date when the client's dependency is late (usually day for day)."),
           ("Change request (CR)", "The agreed way to change scope, price or date once the contract is signed.")],
    code=dict(file="bid/lodestar/appendix-c-assumptions.md", note="as submitted · Wed 24 March 2027", src="""
id     line                              owner     test         if false
── assumptions ────────────────────────────────────────────────────────
A1-07  ≤ 5 % of records fail the         MetroVolt sample,      CR: £9,500
       address check                               by 1 Apr     per 1 % over
A1-11  no MAVIS changes in a wave        MetroVolt change cal.  CR, re-plan
A2-03  wave 1 = 380,000 domestic accts   both      wave plan    CR
── dependencies ───────────────────────────────────────────────────────
D-03   Halvorsen interface spec, 30 Jul  Halvorsen design auth. relief
D-05   12 laptops + VPN in 10 days       MV IT     mobilising   relief
D-09   a MAVIS expert, 3 days a week     MetroVolt kick-off     relief + CR
── exclusions ─────────────────────────────────────────────────────────
X-02   rework of the 02:10 batch job     —         —            quoted apart
X-04   training beyond 40 super-users    —         —            rate card

relief = dates move day for day
top 8 in the bid (section 4.3) · 33 more, grouped, in this appendix
reviewed with Hana (tech), Bilal (data), Callum (plan), Vivian (price)
"""),
    tools="tools: a spreadsheet, a whiteboard, the tender's requirements list and one honest hour with the engineers.",
    contract=dict(side="SOW §3, after MetroVolt's legal team had a go at it",
                  doc="Lodestar SOW · draft v0.3 · redlined", date="9 June 2027", stamp="accepted subject to",
                  clauses=[("3.2", "The Charges are based on the Assumptions in Appendix C. If an Assumption proves materially incorrect, <del>the Supplier shall absorb any resulting cost</del> <ins>either Party may raise a Change Request under clause 7</ins>.", "their legal tried “absorb”. three calls to get it out."),
                           ("3.4", "MetroVolt shall provide the Dependencies in Appendix C by the dates shown. Where a Dependency is late, the Supplier is entitled to relief <ins>day for day</ins> on affected Milestones.", ""),
                           ("3.5", "Exclusions are outside the Services and may be added only by Change Request.", "")],
                  plain="an assumption only protects you if the contract says what happens when it's wrong. A list in the bid that never reaches the contract is a wish. Read the redlines for the word <b>absorb</b>."),
    health=dict(now="a",
                g=("trust is high", ["The list is a shared map of risks.", "Walk it together at kick-off; review it monthly.", "False assumptions are fixed with a short CR, without drama."]),
                a=("they've been burned before", ["Fewer, sharper lines in the main bid.", "Offer to test the biggest one early, before signing.", "Price what you can (a rate per 1 %), so it doesn't read as an exit."]),
                r=("it's a war", ["The list is evidence. Quote it by ID and clause number.", "Confirm every dependency date in writing.", "Raise CRs promptly; late claims look like excuses."])),
    pressure=dict(level=3, title="bid week", cost="two late nights · one weekend · one tense call with sales",
                  items=["The argument with Vivian is about money and pride, so have it with numbers: “Each line we drop, we carry. Here's what that's worth.”", "Write the list <b>with</b> the team, in daylight. Fears written alone at 23:00 turn into 41 lines."]),
    baseline="Each line compares Vivian's <b>three vague lines</b> with <b>eight priced lines in the bid, 33 in appendix C, and clause 3.2 in the contract</b>.",
    ratings=[(3, 4, "Specific and priced reads as honest; vague reads as exits."),
             (2, 4, "Engineers stop carrying risks nobody priced."),
             (1, 4, "A1-07 alone is worth hundreds of thousands if it's false."),
             (2, 5, "The exclusions name the 02:10 job before anyone argues about it."),
             (3, 4, "The design no longer has to pretend the data is clean."),
             (1, 4, "Every line has a test date."),
             (2, 4, "Signed in §3; nobody can say “you never told us”."),
             (4, 3, "Two days of writing, three legal calls."),
             (4, 3, "The list needs a monthly review.")],
    pitfalls=[("Escape hatches", "“The client will cooperate.” It can't be tested, so it reads as a trap and protects nothing.", "a number, an owner and a date, or delete it."),
              ("Two hundred lines", "Nobody reads them, and the client's lawyer strikes the lot.", "eight in the bid, the rest grouped in an appendix."),
              ("Lost on the way to the contract", "The bid had the list; the SOW doesn't.", "check §3 and Appendix C line by line before signing."),
              ("Never tested", "You find out in month nine, when it's an argument.", "a test date on every line, the dangerous ones before signing."),
              ("Excluding the obvious", "Excluding data migration from a migration bid. You lose the bid, or the client's trust.", "price it with a rate instead.")],
    grimoire=[(6, "overpromise-golem", "The Overpromise Golem", "Vivian's “twelve months, over dinner” is a young one."), (1, "sacrificial-lamb", "The Sacrificial Lamb", "And it explains why Orion's leads kept disappearing.")],
    use=["The price is fixed, or capped.", "You can't see inside the legacy system before you bid.", "Another vendor or the client's own IT must deliver something you need.", "The client has been burned before, and the next failure will need someone to blame."],
    skip=["It's time and materials: the client already carries the risk. Keep the dependencies and drop most of the rest."],
    related=["<b>How Long Will It Really Take?</b> (next note)", "<b>What Does the Contract Actually Say?</b> (vol. 2)", "<b>Architecture Decision Records</b> (Ana, vol. 2)", "<b>The Risk Register</b> (Sanne, vol. 5)"],
    quiz=[("What's the difference between an assumption and a dependency?", "An assumption is something you believe is true and priced on. A dependency is something someone else must do, by a date."),
          ("What are the four boxes every line must fill?", "A number, an owner, a test (how and when you'll find out) and a consequence if it's false."),
          ("Why is “the client will cooperate” a bad assumption?", "It can't be measured or tested, so it protects nobody and reads like an escape hatch."),
          ("Why did the word “absorb” matter in clause 3.2?", "It would have made Wrenfield pay for every false assumption, turning the list into decoration."),
          ("What are the three things you can do with a risk on a fixed-price bid?", "Carry it (contingency), share it (a rate above a threshold) or hand it back (exclude it openly).")],
    quiz_sit=[("Vivian says 41 assumptions will lose the bid and wants three. Elaine has said Orion had four. What do you propose?", "Keep all 41, but show eight in the bid, each priced or tested, and group the rest in an appendix. Offer to test A1-07 on a sample before signing. Show Vivian what each dropped line would cost Wrenfield if it's false.")],
    try_it="Take a quote or estimate you've given recently. Write down five things that would ruin it if they turned out wrong. For each, fill the four boxes: number, owner, test, consequence. How many were in the quote?",
    remember="A fixed price is fixed <span class=\"hl\">for the world you wrote down</span>. Everything you didn't write down, <span class=\"hl\">you just agreed to carry</span>.",
    late=dict(when="Thu 11 March 2027 · 23:04 · Leeds",
              lines=["Forty-one lines. Vivian will say it looks like we don't trust them. Elaine will think the same.",
                     "The only one I'd go to war for is A1-07. Nobody at MetroVolt would give me a number for their data, and that tells me something.",
                     "Best advice of the day came from a stranger in a lift. Note to self: find out who Pip is."]),
    sources=["David Maister, <i>Managing the Professional Service Firm</i> (1993): pricing and risk in professional services.",
             "Steve McConnell, <i>Software Estimation: Demystifying the Black Art</i> (2006): ranges, assumptions and the cone of uncertainty.",
             "The UK Government's Model Services Contract and its guidance notes: one public example of how assumptions, dependencies and relief are written into a contract."],
)

# ------------------------------------------------------------------ 07 How Long Will It Really Take?
ef_problem = Doodle(760, 250, "Doodle of three numbers on a whiteboard on 15 March 2027. Vivian's: twelve months, for all customers, said over dinner. Orion's: planned twelve months, cancelled at thirty-six. The industry's: five comparable customer-system replacements took fourteen to thirty months. Ines's team has not estimated yet.",
                    "Three numbers on the board before anyone has estimated anything.", exact=True)
for i, (h, sub, fill) in enumerate([("12 months", "Vivian · for everything", "y"), ("12 → 36", "Orion · then cancelled", "pink"), ("14–30 months", "5 similar projects", "blue")]):
    ef_problem.box(14 + i * 250, 40, 232, 110, h, fill, sub=sub, size=28, subsize=17)
ef_problem.note(380, 200, "which one does the bid believe?", "red", size=22)

ef_how = Doodle(760, 340, "Wave 1 estimated three ways. Bottom up: nine work streams, each with an optimistic, likely and pessimistic estimate, run ten thousand times in a spreadsheet, giving a P50 of eleven months and a P80 of fourteen months from contract start. Reference class: five comparable first waves took nine to sixteen months. The two agree. The plan commits to the pilot in month nine and wave 1 complete in month twelve, and prices effort at P80.",
                "The bottom-up range and the reference class agree: 11 months likely, 14 with bad luck. Commit to 12, price for 14.", exact=True)
ef_how.line("M40 260 C 160 260 200 60 300 60 C 400 60 460 250 720 258", thin=True)
ef_how.line("M40 262 H740", thin=True)
for x, t, c in [(250, "P50 · 11 mo", "pen"), (355, "commit · 12", "green"), (480, "P80 · 14 mo", "red")]:
    ef_how.line(f"M{x} 268 V100", color=c, dash=True)
    ef_how.note(x, 292, t, c, size=19)
ef_how.box(520, 20, 226, 74, "reference class", "blue", sub="5 first waves: 9–16 mo", size=18, subsize=16)
ef_how.box(14, 20, 200, 74, "bottom up", "y", sub="9 streams × 3 points", size=18, subsize=16)
ef_how.note(380, 326, "pilot (20,000) in month 9 · wave 1 (380,000) in month 12", "pen", size=19)

ESTIMATING = dict(
    slug="estimating-in-fog", date=date(2027, 3, 15), meta="bid day 41 of 50", where="LEEDS",
    kicker="a.k.a. “three-point estimates and the reference class”",
    tldr="An estimate is a <b>range with odds</b>, not a date. Estimate bottom up in ranges (best, likely, worst), run them together to get a <b>P50</b> and a <b>P80</b>, then check the result against a <b>reference class</b>: what similar projects really took, including the client's own failures. <b>Commit</b> to a date between P50 and P80, <b>price the effort at P80</b>, and say both numbers out loud so nobody remembers only the nice one.",
    chips=[("Family", "shaping the answer"), ("Lives in", "bid/lodestar/estimate-v3.xlsx"), ("Pairs with", "assumptions, pricing models")],
    problem_side="Wrenfield, 15 March 2027",
    problem="""  <p class="lead">Nine days before the deadline, three numbers are on the whiteboard and none of them is Wrenfield's estimate. <b>Vivian's</b>: twelve months, for <i>everything</i>, said to Priya over dinner on 19 January. <b>Orion's</b>: planned at twelve months, cancelled at thirty-six. <b>The industry's</b>: five comparable customer-system replacements took <b>14 to 30 months</b> in full.</p>
  <ul>
    <li>Phase 1 is only <b>wave 1</b>: 380,000 of 2.3 million accounts. Vivian's “everything” was never in scope.</li>
    <li>Callum's first plan is a single bar chart ending exactly at month 12. <span class="hl-pink">Nobody can say how likely it is.</span></li>
    <li>MetroVolt's board will remember one number. It had better be one Wrenfield can hit.</li>
  </ul>""",
    problem_figs=[ef_problem],
    sides=dict(client=("Nkem, finance", "<p>MetroVolt's finance team needs <b>one date and one price</b> for the business case. Orion gave them both, and both were wrong. Nkem will believe a range more than a precise date, but the board paper still needs a line that says “live by”.</p>", "Give me a date you'd bet your own money on."),
                vendor=("Ines and Callum", "<p>Wrenfield needs a date it can <b>commit to</b>, an effort it can <b>price</b>, and a story that explains the gap between them. A precise single number would look confident and be a lie. A wide range would look honest and lose the bid.</p>", "Commit to a date. Price the bad luck.")),
    sides_after="The trick is to stop treating the date you commit to and the effort you price as the same number.",
    analogy_side="the satnav's arrival time",
    analogy="""  <p>A satnav says “arrive 14:20”. An experienced driver knows that's the <b>likely</b> time on a good day, and that on a Friday it's more like 14:50. For a wedding you leave <b>for 14:50</b>, and you tell the bride 14:30. You also remember that the last three times you drove there, it took longer than the satnav said.</p>""",
    map=[("The satnav's 14:20", "P50: the likely date"),
         ("Friday traffic, 14:50", "P80: the date with normal bad luck"),
         ("Telling the bride 14:30", "The committed date: month 12"),
         ("Leaving for 14:50", "Pricing the effort at P80"),
         ("“It always takes longer than the satnav”", "The reference class, Orion included")],
    how_side="bottom up in ranges, then check against history",
    how="""  <p><b>Bottom up.</b> Hana, Bilal, Oskar and Callum split wave 1 into <b>nine work streams</b> (platform, customer data, change detection, Halvorsen interface, migration tooling, reconciliation, testing, cutover, training). Each gets three numbers: best, likely, worst. A spreadsheet runs them together <b>10,000 times</b>. Result, from contract start: <b>P50 11 months, P80 14 months</b>.</p>
  <p><b>Reference class.</b> Ines asks five former colleagues and two references for real durations of <b>first waves</b> in similar replacements: 9 to 16 months. The two methods agree, which is the point of doing both. Orion is in the reference class too, and the answer to “why will this be different?” goes into the bid: waves, a pilot gate, and paid discovery.</p>
  <p><b>The decision.</b> Commit to <b>first 20,000 customers live in month 9</b> and <b>all 380,000 in month 12</b>. Price the effort at <b>P80</b>, so the contingency pays for bad luck instead of Wrenfield's margin. Both numbers go in the bid, with a sentence explaining them.</p>""",
    how_figs=[ef_how],
    steps=[("Split the work into streams", "Seven to twelve, each with an owner who'll do the work."),
           ("Three numbers per stream", "Best, likely, worst. Worst means “bad but normal”, not disaster."),
           ("Combine them", "A simple simulation gives P50 and P80; adding the likelies doesn't."),
           ("Find the reference class", "What similar projects really took, including failures."),
           ("Compare and explain", "If they disagree, find out why before you commit."),
           ("Commit between P50 and P80; price at P80", "And write both numbers down.")],
    vocab=[("Three-point estimate", "Best, likely and worst case for one piece of work."),
           ("P50 / P80", "Dates you'd hit with 50 % / 80 % likelihood."),
           ("Reference class forecasting", "Estimating from the real outcomes of similar past projects."),
           ("Monte Carlo simulation", "Running the ranges together thousands of times to get a spread of outcomes."),
           ("Cone of uncertainty", "Estimates are widest at the start and narrow as you learn."),
           ("Planning fallacy", "People's habit of underestimating their own projects, even knowing others overran.")],
    code=dict(file="bid/lodestar/estimate-v3.md", note="summary · Mon 15 Mar 2027", src="""
WAVE 1 ESTIMATE · months from contract start (discovery included)

stream                    best  likely  worst   owner
platform                   3      4       6     Hana
customer data              4      6      10     Bilal
change detection           2      3       6     Hana
Halvorsen interface        2      3       7     Ines
migration tooling          3      4       6     Lottie + Hana
reconciliation             2      3       5     Bilal
testing                    3      4       7     Oskar
cutover + hypercare        1      2       3     Callum
training (40 super-users)  1      1       2     Callum
(streams overlap; 10,000 runs with the dependencies)

result      P50 11 months · P80 14 months
reference   5 comparable first waves: 9–16 months (median 12)
            Orion: planned 12, cancelled at 36 (big bang, no pilot)
commit      pilot 20,000 live in month 9 · wave 1 (380,000) in month 12
price       effort at P80 (contingency ≈ £500k)
"""),
    contract=dict(side="how dates become promises", doc="Lodestar bid · section 4.2 (delivery plan)", date="as submitted 24 Mar 2027", stamp="milestone dates",
                  clauses=[("4.2.1", "The Supplier will deliver the Pilot Milestone (20,000 accounts live) within 9 months and the Wave 1 Milestone (380,000 accounts live) within 12 months of the Contract start date, subject to the Assumptions in Appendix C.", "“of the contract start date”, not “of 1 June”. the start will slip. it always does."),
                           ("4.2.4", "Milestone dates will be re-baselined at the end of discovery by agreement.", "the cone narrows; the dates may move. in writing.")],
                  plain="tie every date to the start of the contract, not to a calendar day, and to the assumptions. Then a late signature or a false assumption moves the date without a fight."),
    health=dict(now="a",
                g=("you've delivered for them before", ["Your own history is the reference class.", "A narrower range is believable.", "Still say P50 and P80."]),
                a=("new client, failed predecessor", ["Both methods, and show they agree.", "Explain why you're different from Orion.", "Commit between P50 and P80."]),
                r=("they want an impossible date", ["Show the range and the history.", "Offer a smaller first delivery by their date.", "Don't sign a P10 date at a fixed price."])),
    pressure=dict(level=4, title="the number", cost="one disagreement with sales · one with the managing director",
                  items=["Graham wants a lower price; Vivian wants an earlier date. Show them the curve, not your opinion.", "A range feels weak in the room and strong a year later. You're writing for a year later."]),
    baseline="Each line compares <b>a single bar chart ending at month 12</b> with <b>ranges, a reference class, a committed date and effort priced at P80</b>.",
    ratings=[(2, 4, "Nkem gets a date with odds and a reason."),
             (2, 4, "The team isn't held to a P10 date."),
             (2, 4, "Contingency pays for bad luck, not margin."),
             (3, 4, "Pilot and wave 1 dates are clear."),
             (3, 4, "The plan isn't bent to fit a dinner promise."),
             (2, 4, "Worst cases per stream show where the risk sits."),
             (2, 4, "The range and the method are in the bid."),
             (4, 3, "Three days of estimating."),
             (4, 3, "The model needs updating after discovery.")],
    pitfalls=[("One number", "A single date with no odds.", "P50 and P80, always together."),
              ("Adding up the likelies", "The total is far more optimistic than any stream.", "combine ranges with a simulation."),
              ("Ignoring the client's own history", "Orion is the best reference class you have.", "include it, and say why you're different."),
              ("Pricing at the committed date", "Bad luck comes out of your margin.", "price effort at P80."),
              ("Dates on the calendar", "A late signature eats your schedule.", "dates in months from contract start.")],
    grimoire=[(6, "overpromise-golem", "The Overpromise Golem", "is what a twelve-month dinner promise becomes if nobody re-anchors it.")],
    use=["Any estimate someone will be held to.", "Fixed-price bids.", "When a date has already been said out loud.", "When the client has a failed project behind it."],
    skip=["A two-week task you've done many times: a single honest number is fine."],
    related=["<b>What Are We Assuming?</b> (previous note)", "<b>Fixed Price, or Time and Materials?</b> (next note)", "<b>What If Sales Already Promised?</b> (this volume)", "<b>What If We Ran It a Thousand Times?</b> (Sanne, vol. 5)"],
    quiz=[("What do P50 and P80 mean?", "Dates you'd hit with a 50 % and an 80 % likelihood."),
          ("Why combine ranges with a simulation instead of adding the likely values?", "Adding likelies ignores that some streams will go badly; the total comes out far too optimistic."),
          ("What is reference class forecasting?", "Estimating from what similar projects really took, not from your own plan."),
          ("Why commit to month 12 but price at P80 (month 14)?", "The date is the promise; the price has to survive normal bad luck without eating the margin."),
          ("Why tie dates to the contract start date?", "So a late signature moves the dates automatically.")],
    quiz_sit=[("Graham asks you to commit to the P50 date to win. What do you say?", "A P50 date is a coin toss. If he wants it, the price must carry the risk, or the bid must offer something smaller by that date. Show him the curve and what the bad half costs Wrenfield.")],
    try_it="Pick a piece of work you're estimating. Split it into five to nine streams with best, likely and worst numbers. Then find three similar projects and what they really took. Do the two agree? Which date would you commit to, and which would you plan for?",
    remember="An estimate is <span class=\"hl\">a range with odds</span>. Commit between P50 and P80, and <span class=\"hl\">price the bad luck</span>.",
    late=dict(when="Mon 15 March 2027 · 22:40 · Leeds",
              lines=["P50 11, P80 14. The reference class says 12. For once, two methods agree.",
                     "Vivian heard “11” and smiled. Graham heard “14” and frowned. Both were right to.",
                     "Orion planned 12 too. The difference has to be in how we fail, not in how we promise."]),
    sources=["Steve McConnell, <i>Software Estimation: Demystifying the Black Art</i> (2006).",
             "Bent Flyvbjerg and Dan Gardner, <i>How Big Things Get Done</i> (2023): reference class forecasting.",
             "Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011): the planning fallacy."],
)

# ------------------------------------------------------------------ 08 Fixed Price, or Time and Materials?
pm_problem = Doodle(760, 240, "Doodle of a seesaw. On one side MetroVolt, burned by Orion, wants a fixed price so the risk moves to the supplier. On the other side Wrenfield, an 80-person firm, can't carry the risk of a system nobody has seen inside. The plank is labelled who carries the fog.",
                    "Who carries the fog? MetroVolt wants to hand it over; Wrenfield can't afford to hold all of it.", exact=True)
pm_problem.line("M120 150 L640 90", color="")
pm_problem.line("M360 124 L330 200 L410 200 Z")
pm_problem.box(60, 70, 200, 70, "MetroVolt", "y", sub="“fixed price, please”", size=20, subsize=16)
pm_problem.box(520, 14, 220, 70, "Wrenfield", "blue", sub="80 people", size=20, subsize=16)
pm_problem.note(380, 230, "the plank is labelled: who carries the fog?", "red", size=20)

pm_how = Doodle(760, 330, "Lodestar's commercial model. Phase one: a fourteen-week discovery at time and materials, capped at 380,000 pounds. Then a fixed price of 4.8 million pounds for wave 1, paid on milestones: design approved 15 per cent, pilot live 25 per cent, wave 1 live 35 per cent, hypercare ended 15 per cent, and 10 per cent retained until the end of warranty. Underneath, a rate card for changes.",
                "Pay for the fog by the day, pay for the build by the result.", exact=True)
pm_how.box(14, 20, 200, 110, "discovery", "y", sub="T&M, capped £380k", size=20, subsize=16)
pm_how.arrow(218, 75, 250, 75)
pm_how.box(254, 20, 492, 110, None, "blue", rx=10)
pm_how.head(500, 50, "wave 1 · fixed £4.8m, on milestones", size=19)
for i, (t, pct) in enumerate([("design", "15 %"), ("pilot", "25 %"), ("wave 1", "35 %"), ("hypercare", "15 %"), ("warranty", "10 %")]):
    pm_how.box(266 + i * 95, 66, 87, 52, t, "paper", sub=pct, size=15, subsize=15)
pm_how.box(14, 160, 732, 64, "rate card for change", "paper", sub="architect £1,150/day · senior engineer £950 · engineer £750 · BA £800 · test lead £850", size=18, subsize=15)
pm_how.note(380, 270, "cost at P50 ≈ £3.4m (margin 29 %) · at P80 ≈ £3.9m (margin 19 %)", "pen", size=19)
pm_how.note(380, 304, "no milestone payment until the client can see something working", "red", size=18)

PRICING_MODELS = dict(
    slug="pricing-models", date=date(2027, 3, 18), meta="bid day 44 of 50", where="LEEDS",
    kicker="a.k.a. “commercial models: fixed price, T&amp;M, capped, outcome-based”",
    tldr="The commercial model decides <b>who carries the uncertainty</b>. Time and materials puts it on the client; fixed price puts it on you; capped and outcome-based split it in different ways. Match the model to <b>what you know</b>: pay for the fog <b>by the day</b> (a capped, paid discovery), then a <b>fixed price</b> once you can see, paid on <b>milestones the client can check</b>, with a <b>rate card</b> for whatever changes.",
    chips=[("Family", "shaping the answer"), ("Lives in", "bid section 6 (commercial) + the pricing model"), ("Pairs with", "estimating, assumptions, change control")],
    problem_side="Wrenfield, 18 March 2027",
    problem="""  <p class="lead">The tender asks for a <b>fixed price</b> for phase 1. After Orion, MetroVolt wants the risk on someone else's balance sheet. Wrenfield's whole revenue is about <b>£9m a year</b>, and nobody has seen inside MAVIS.</p>
  <ul>
    <li>A pure fixed price for discovery <i>and</i> wave 1 means pricing the fog. Either the price is huge (and loses) or the risk is huge (and might sink Wrenfield).</li>
    <li>Pure time and materials would be honest, and MetroVolt has already said no: <span class="hl-pink">“we did that with Orion”</span>.</li>
    <li>Clarification Q-09 came back on 3 March: <b>discovery may be priced and contracted separately</b>. That's the gap.</li>
  </ul>""",
    problem_figs=[pm_problem],
    sides=dict(client=("Nkem and Desmond", "<p>Finance wants a <b>number for the board</b> that won't move. Procurement wants prices that can be <b>compared</b> across five bidders. Both remember Orion's open-ended invoices. A fixed price feels like safety, even if it buys a bidder's contingency.</p>", "If it's fixed, it's not our problem when it slips."),
                vendor=("Callum and Ines", "<p>Wrenfield needs a model where it's <b>paid for what it learns</b> before it promises, and where the fixed part is fixed <b>for a known world</b>. It also needs cash: a firm of 80 can't wait twelve months for the first payment.</p>", "We'll fix the price when we can see what we're pricing.")),
    sides_after="A fixed price isn't free safety for the client: it's insurance, and the premium is the vendor's contingency. A paid discovery lowers the premium for both.",
    analogy_side="the kitchen fitter's two prices",
    analogy="""  <p>A kitchen fitter charges <b>a day rate to survey and design</b>, then gives a <b>fixed price to fit</b> the design you both signed, paid in stages: units in, worktops on, appliances working. If you change your mind about the island, there's a <b>price list</b> for that. Nobody fixes a price for a kitchen they haven't measured.</p>""",
    map=[("Day rate to survey", "Discovery: T&amp;M, capped at £380k"),
         ("Fixed price to fit the signed design", "Wave 1: £4.8m fixed"),
         ("Paid in stages", "Milestones: design, pilot, wave 1, hypercare, warranty"),
         ("A price list for changes", "The rate card"),
         ("“Nobody prices an unmeasured kitchen”", "No fixed price before discovery")],
    how_side="match the model to what you know",
    how="""  <p>Callum puts five models on a page and asks one question of each: <b>who carries the fog?</b> <b>Time and materials</b>: MetroVolt, all of it (refused). <b>Fixed price for everything</b>: Wrenfield, all of it (too dangerous). <b>Capped T&amp;M</b>: shared, but MetroVolt hears “Orion”. <b>Outcome-based</b> (paid per account migrated): tempting, but data quality isn't in Wrenfield's control. <b>Discovery, then fixed</b>: each carries the fog it can see.</p>
  <p>The bid offers: a <b>14-week discovery, time and materials, capped at £380k</b>; then <b>£4.8m fixed for wave 1</b>, paid on five milestones the client can check (design approved 15 %, pilot live 25 %, wave 1 live 35 %, hypercare ended 15 %, 10 % retained until the warranty ends). A <b>rate card</b> covers change. The fixed price is “subject to the Assumptions in Appendix C”.</p>
  <p>The margin is checked at both ends of the estimate: about <b>29 % at P50</b>, <b>19 % at P80</b>. Graham's floor is 15 %. If the P80 margin had been below it, the answer would have been a higher price or a smaller scope, not hope.</p>""",
    how_figs=[pm_how],
    steps=[("Ask “who carries the fog?” of each model", "Write the answer for each, honestly."),
           ("Separate learning from building", "A capped, paid discovery before the fixed price."),
           ("Fix the price for a written world", "“Subject to the assumptions in Appendix C”."),
           ("Pay on things the client can see", "Working software, not documents or months."),
           ("Add a rate card", "So every change has a price before anyone argues."),
           ("Check the margin at P50 and P80", "If P80 is below your floor, change the deal.")],
    vocab=[("Time and materials (T&amp;M)", "The client pays for the time spent; the client carries the risk."),
           ("Fixed price", "One price for a defined scope; the supplier carries the risk."),
           ("Capped T&amp;M", "Paid by time, up to a maximum."),
           ("Outcome-based pricing", "Paid per result (e.g. per account migrated)."),
           ("Milestone payment", "A payment released when a defined, checkable result is accepted."),
           ("Retention", "A part of the price held back until the warranty ends.")],
    code=dict(file="bid/lodestar/section-6-commercial.md", note="as submitted · Wed 24 Mar 2027", src="""
COMMERCIAL MODEL · LODESTAR phase 1

part          model                 amount     paid when
discovery     T&M, capped           £380,000   monthly, on timesheets (14 weeks)
wave 1        fixed price           £4.8m      on milestones, subject to Appendix C
   M2  design approved by the design authority     15 %   £720,000
   M3  pilot: 20,000 accounts live                 25 %   £1,200,000
   M4  wave 1: 380,000 accounts live               35 %   £1,680,000
   M5  hypercare ended (8 weeks)                   15 %   £720,000
   M6  warranty ended (90 days), retention         10 %   £480,000
change        rate card (per day)   architect £1,150 · senior eng. £950 · eng. £750
                                    BA £800 · test lead £850 · PM £900

internal: cost P50 ≈ £3.4m (margin 29 %) · P80 ≈ £3.9m (margin 19 %) · floor 15 %
"""),
    contract=dict(side="charges and payment, as it will be signed", doc="Lodestar SOW · §9 charges (draft)", date="from the bid", stamp="fixed, for a written world",
                  clauses=[("9.1", "Discovery Services shall be charged on a time and materials basis at the Rates in Schedule 5, up to a maximum of £380,000.", "the cap protects them. the T&M protects us."),
                           ("9.2", "Wave 1 Services shall be charged as a fixed price of £4,800,000, subject to clause 3 (Assumptions), payable on acceptance of the Milestones in Schedule 4.", "“subject to clause 3”. the most valuable four words in the bid."),
                           ("9.5", "Changes shall be priced using the Rates in Schedule 5.", "")],
                  plain="the commercial model is written in the charges clause. Check that the fixed price is tied to the assumptions, the milestones to acceptance, and changes to a rate card agreed now, while everyone is friendly."),
    health=dict(now="a",
                g=("trust is high", ["T&amp;M or capped T&amp;M can work.", "Milestones still help both sides see progress.", "Keep a rate card anyway."]),
                a=("burned before, wants certainty", ["Paid discovery, then fixed.", "Milestones on working results.", "The fixed price tied to written assumptions."]),
                r=("fixed price for everything, now", ["Price the fog openly, and expect to lose.", "Or offer a smaller fixed first step.", "Don't sign a fixed price for a world you haven't seen."])),
    pressure=dict(level=3, title="the commercial model", cost="cash-flow worries · a long evening with the spreadsheet",
                  items=["The milestone profile is also Wrenfield's cash flow. Check you can pay salaries until month 9.", "Graham's margin floor is a real line. If the P80 margin is under it, change the deal, not the estimate."]),
    baseline="Each line compares <b>a single fixed price for everything</b> with <b>a capped, paid discovery, then a fixed price on milestones and a rate card</b>.",
    ratings=[(3, 4, "MetroVolt gets a fixed price, for a world it can read."),
             (2, 4, "The team isn't pricing a system it hasn't seen."),
             (1, 4, "Margin survives P80; changes have a price."),
             (2, 4, "Discovery and build are separate scopes."),
             (3, 4, "No incentive to design around an unseen system."),
             (2, 4, "Fog is paid for by the day."),
             (2, 4, "§9 ties the price to §3."),
             (4, 3, "A more complex offer to explain."),
             (4, 3, "Two contracts' worth of admin.")],
    pitfalls=[("Fixing the price of fog", "A fixed price for a system nobody has seen.", "paid discovery first."),
              ("Milestones on documents", "Paid for a design document; the client can't see progress.", "pay on working results."),
              ("No rate card", "Every change becomes a negotiation.", "agree rates now, while friendly."),
              ("Margin checked only at P50", "Bad luck takes the whole margin.", "check at P80 against your floor."),
              ("Outcome pricing on things you don't control", "Paid per account, while the client owns the data quality.", "only pay-per-result where you control the result.")],
    use=["Any fixed-price bid.", "Legacy work with hidden complexity.", "A client who has been burned by open-ended T&amp;M."],
    skip=["A small, well-known piece of work: a simple fixed price is fine."],
    related=["<b>How Long Will It Really Take?</b> (previous note)", "<b>What Are We Assuming?</b> (this volume)", "<b>How Do We Change the Deal Without a War?</b> (vol. 2)", "<b>Make It, Buy It, or Hire It?</b> (Sanne, vol. 2)"],
    quiz=[("Who carries the risk under time and materials? Under fixed price?", "The client under T&amp;M; the supplier under fixed price."),
          ("Why a paid discovery before the fixed price?", "So nobody fixes a price for a system they haven't seen; the fog is paid for by the day."),
          ("Why pay on milestones the client can see?", "Both sides can tell progress from activity, and payment follows real results."),
          ("Why was outcome-based pricing rejected?", "Payment per account migrated depends on data quality, which Wrenfield doesn't control."),
          ("What does “subject to clause 3” do in §9.2?", "It ties the fixed price to the written assumptions, so a false one can change the price.")],
    quiz_sit=[("Desmond asks if Wrenfield would take discovery as fixed price too, for “simplicity”. What do you answer?", "Offer a fixed price for a smaller, defined discovery scope (named outputs, 14 weeks) at the cap, if that helps procurement compare bids. But keep the build price tied to what discovery finds.")],
    try_it="Take a piece of work you're quoting. Write down who carries the uncertainty under T&amp;M, fixed price and a discovery-then-fixed model. Which part do you actually know enough to fix? What would you pay milestones on?",
    remember="Pay for the fog <span class=\"hl\">by the day</span>. Fix the price <span class=\"hl\">for a written world</span>. Pay on <span class=\"hl\">results you can see</span>.",
    late=dict(when="Thu 18 March 2027 · 23:35 · Leeds",
              lines=["Discovery by the day, wave 1 fixed. Five milestones, none on a document.",
                     "Margin at P80: 19 %. Graham's floor is 15. Four points between us and a bad year.",
                     "Callum checked the cash flow: we can pay everyone until the pilot. Then we need the pilot."]),
    sources=["David Maister, <i>Managing the Professional Service Firm</i> (1993): pricing and risk.",
             "Ron Baker, <i>Implementing Value Pricing</i> (2010).",
             "UK Cabinet Office, <i>The Sourcing Playbook</i> (2020): pricing mechanisms and risk allocation."],
)

NOTES = [SOLUTION_TWO_PAGES, ASSUMPTIONS, ESTIMATING, PRICING_MODELS]
