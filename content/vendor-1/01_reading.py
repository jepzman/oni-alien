# Series 5 · On the Client's Floor · Vol. 1 · Winning the Work · Reading the tender (notes 1–4).
# Narrator: Ines Duarte (she/her), lead architect at Wrenfield Digital. Facts: docs/lodestar-casebook.md.
from datetime import date

# ------------------------------------------------------------------ 01 How Do I Read a Tender?
rt_problem = Doodle(760, 270, "Doodle of Wednesday 3 February 2027. A 96-page tender lands with 212 requirements. Vivian forwards it with the subject line THIS IS OURS!!! A calendar shows six weeks until the deadline on 24 March at noon.",
                    "96 pages, 212 requirements, six weeks, and a subject line in capitals.", exact=True)
rt_problem.box(24, 30, 200, 200, None, "paper", rx=4)
rt_problem.box(36, 18, 200, 200, None, "paper", rx=4)
rt_problem.box(48, 6, 200, 200, "LODESTAR ITT", "y", sub="96 pages · 212 reqs", size=22, subsize=16, rx=4)
rt_problem.icon("envelope", 300, 40, 1.3)
rt_problem.note(340, 140, "fwd: THIS IS OURS!!!", "red", size=22)
rt_problem.note(340, 168, "— Vivian, 15:12", "", size=18)
rt_problem.icon("calendar", 560, 30, 1.6)
rt_problem.head(610, 160, "6 weeks", size=24)
rt_problem.note(610, 190, "due Wed 24 March, 12:00", "pen", size=18)
rt_problem.note(380, 250, "first instinct: start writing. wrong instinct.", "red", size=20)

rt_analogy = Doodle(760, 230, "Doodle of a job advert. Three highlighter colours: yellow on how candidates will be judged, blue on the duties hidden in each sentence, pink on a line that hints why the last person left after a year.",
                    "Read a job advert three times: how you'll be judged, what the job really is, and why the last person left.", exact=True)
rt_analogy.box(30, 20, 300, 190, None, "paper", rx=4)
rt_analogy.head(180, 52, "WANTED: Head of Ops", size=20)
for i, (fill, t) in enumerate([("y", "assessed on: interview 60 %"), ("blue", "“will own all systems”"), ("pink", "“immediate start”")]):
    rt_analogy.box(48, 70 + i * 44, 264, 34, t, fill, size=16, rx=3)
rt_analogy.arrow(340, 110, 420, 110)
rt_analogy.row([("judged", "yellow", "y"), ("the job", "blue", "blue"), ("history", "pink", "pink")], x=430, y=60, h=100, w=96, gap=10, size=18, subsize=14)

rt_how = Doodle(760, 340, "Ines's three reads of the Lodestar tender. Read one, yellow: how it is scored. Quality 60 per cent, price 40, and 14 pass or fail requirements that can throw a bid out. Read two, blue: the work hidden in every will and shall, 212 requirements, of which three carry most of the risk: migrate all customer data, integrate with the existing billing system, and support for five years. Read three, pink: the history nobody wrote down. Orion's words appear in section 4, the indicative budget is four to six million, and the timetable is short.",
                "Three reads, three colours. Most of the risk sits in three sentences of 212.", exact=True)
cols = [("1 · how it's scored", "y", ["quality 60 / price 40", "14 pass / fail lines", "team = 10 %"]),
        ("2 · the work", "blue", ["212 × “will” / “shall”", "“migrate all data”", "“integrate with billing”", "“support for 5 years”"]),
        ("3 · the history", "pink", ["Orion's words in §4", "budget £4–6m", "six weeks: who knew?"])]
for i, (h, fill, lines) in enumerate(cols):
    x = 14 + i * 250
    rt_how.box(x, 14, 232, 52, h, fill, size=19)
    rt_how.box(x, 74, 232, 190, None, "paper", rx=4)
    for r, t in enumerate(lines):
        rt_how.text(x + 116, 110 + r * 40, t, size=17)
rt_how.note(380, 300, "write the answers on one sheet before anyone writes a word of the bid", "red", size=19)

READING_A_TENDER = dict(
    slug="reading-a-tender", date=date(2027, 2, 4), meta="bid day 2 of 50", where="LEEDS",
    kicker="a.k.a. “reading an invitation to tender (ITT / RFP)”",
    tldr="A tender tells you three things, and only one of them on purpose. Read it <b>three times</b>: once for <b>how it will be scored</b> (weights, pass / fail lines, what the evaluators must write down), once for <b>the work hidden in every “will” and “shall”</b>, and once for <b>the history nobody wrote down</b> (who drafted it, what failed before, why the timetable is so short). Put the answers on <b>one sheet</b> before anyone writes a word of the bid.",
    chips=[("Family", "reading the tender"), ("Lives in", "bid/lodestar/00-reading-sheet.md"), ("Pairs with", "bid / no-bid, clarification questions")],
    problem_side="Wrenfield and MetroVolt, February 2027",
    problem="""  <p class="lead">On <b>Wednesday 3 February 2027</b> at 15:12, MetroVolt publishes the tender for <b>Lodestar</b>: 96 pages, <b>212 requirements</b>, bids due on <b>24 March at noon</b>. Vivian, Wrenfield's account director, forwards it to eleven people with the subject line <span class="hl-pink">“THIS IS OURS!!!”</span>. By 16:00 two engineers have started sketching an architecture.</p>
  <ul>
    <li><b>Thursday 4 February, 07:40, the Leeds train.</b> Ines reads it properly for the first time, with three highlighters.</li>
    <li>Page 71 says bids are scored <b>60 % quality, 40 % price</b>, and that <b>14 requirements are pass / fail</b>: miss one and the bid is out.</li>
    <li>Section 4 calls the customer data a <b>“Golden Customer Record”</b>. That isn't MetroVolt's phrase. Ines has heard it before, on a Vexmoor slide.</li>
    <li>The project being replaced isn't mentioned once. Its name was <b>Orion</b>. It was cancelled last month.</li>
  </ul>""",
    problem_figs=[rt_problem],
    timesheet=dict(week="w/c 1 Feb 2027", label="Lodestar bid (pre-sales)", booked=[7.5, 7.5, 7.5, 7.5, 7.5, 0, 0], worked=[7.5, 8.0, 9.5, 10.0, 8.0, 2.0, 0],
                   note="billable this week: 0.0. the tender is free; reading it isn't."),
    sides=dict(client=("Desmond writes it", "<p>Procurement needs a tender that is <b>fair, defensible and scoreable</b>: the same questions for every bidder, weights fixed in advance, nothing a losing bidder could challenge. Desmond assembled it from the business case, Hollis's architecture notes and, under deadline, <b>Orion's old requirements</b>.</p>", "If it's in writing and scored the same for everyone, nobody can sue us."),
                   vendor=("Ines reads it", "<p>The tender is the only map Wrenfield has. Ines needs to know <b>how to score</b>, <b>what the work really is</b> and <b>whether the game is already decided</b>. The document answers the first question openly, the second in small print, and the third only by accident.</p>", "Who wrote section 4, and why does it sound like Vexmoor?")),
    sides_after="Neither side is hiding anything on purpose. A tender is written by tired people under rules, and read by hopeful people under deadline. The reading sheet is how you stay calm.",
    analogy_side="the job advert, read three times",
    analogy="""  <p>Reading a job advert for a role you want, you highlight three things in three colours. <b>How you'll be judged</b>: interview 60 %, test 40 %. <b>What the job really is</b>: “will own all systems” means you're on call. And <b>the history</b>: “immediate start” and a re-advertised post mean the last person left in a hurry, and you want to know why before you sign.</p>""",
    analogy_figs=[rt_analogy],
    map=[("Interview 60 %, test 40 %", "Quality 60 %, price 40 %, with sub-weights per section"),
         ("“Must have a driving licence”", "The 14 pass / fail requirements"),
         ("“Will own all systems”", "“The supplier will migrate all customer data”"),
         ("A re-advertised post", "Orion: cancelled in January, never mentioned"),
         ("Asking the receptionist why the last one left", "Asking around, openly, before the clarification deadline")],
    how_side="three reads, three colours, one sheet",
    how="""  <p><b>Read one: how it's scored (yellow).</b> Find the evaluation section first. Lodestar's says quality 60 % (solution 20, delivery approach 15, legacy and data 10, team 10, social value 5) and price 40 %. Evaluators must write down a <b>reason for every score</b>, so give them sentences they can copy. The 14 pass / fail lines go to the top of the sheet: they're the only part that can end the bid in an afternoon.</p>
  <p><b>Read two: the work (blue).</b> Count every “will” and “shall”: each one is a promise you'd be signing. Most are routine. Three carry most of the risk: <i>“migrate all customer data from MAVIS”</i> (that sentence <b>is</b> the project), <i>“integrate with the existing billing platform”</i> (Halvorsen, another company) and <i>“provide support for five years”</i> (a cost nobody priced).</p>
  <p><b>Read three: the history (pink).</b> What's missing? Orion. Who drafted section 4? Someone who used Vexmoor's words. Why six weeks for a £4–6m programme? Either it's urgent, or someone has already had a head start.</p>""",
    how_figs=[rt_how],
    steps=[("Don't start writing", "Nobody drafts a word until the reading sheet is done. Two days, not two hours."),
           ("Read for the scoring", "Weights, sub-weights, pass / fail lines, page limits, what evaluators must justify."),
           ("Count the promises", "Every “will” and “shall” into a spreadsheet; mark the three that carry the risk."),
           ("Read for the history", "What failed before, who wrote which section, why this timetable."),
           ("List what you don't know", "These become clarification questions and assumptions."),
           ("One sheet, shared", "The whole bid team reads the same sheet on day three.")],
    vocab=[("ITT / RFP", "Invitation to tender / request for proposal: the client's formal request for bids."),
           ("Evaluation criteria", "How bids are scored, with weights fixed before bids arrive."),
           ("Pass / fail requirement", "A must-have that excludes the bid if not met, whatever the score."),
           ("Compliance matrix", "A table answering every requirement: comply, partly, no, with a reference."),
           ("Clarification period", "The window for written questions; answers go to every bidder."),
           ("Incumbent", "The supplier already doing related work for the client.")],
    code=dict(file="bid/lodestar/00-reading-sheet.md", note="Ines · Thu 4 Feb 2027, the 07:40 train", src="""
LODESTAR · reading sheet                                  bid due Wed 24 Mar, 12:00

1 · HOW IT'S SCORED
quality 60  (solution 20 · delivery 15 · legacy+data 10 · team 10 · social 5)
price   40  (lowest price gets full marks; others pro rata)
pass / fail: 14 lines, incl. ISO 27001, UK data residency, named key people
page limit: 40 pages + appendices · evaluators must justify every score

2 · THE WORK (212 promises, 148 must / 64 should)
the three that carry the risk:
  R4.2  "migrate all customer data from MAVIS"      → the project itself
  R6.1  "integrate with the existing billing system" → Halvorsen, not us
  R9.4  "support for five years"                     → unpriced cost

3 · THE HISTORY
Orion: cancelled Jan 2027, never mentioned          §4 uses Vexmoor's words
budget £4–6m · six weeks to bid                      who had a head start?

QUESTIONS (→ clarification, due 24 Feb): 14 so far
"""),
    tools="tools: three highlighters, a spreadsheet for the “will”s, and the discipline not to start writing.",
    contract=dict(side="the tender's own rules (instructions to bidders)",
                  doc="Lodestar ITT · instructions to bidders", date="published 3 Feb 2027", stamp="pass / fail",
                  clauses=[("6.3", "Bids will be evaluated on quality (60 %) and price (40 %) using the criteria in Annex B. A score of 0 against any requirement marked <b>pass / fail</b> will exclude the bid from further evaluation.", "fourteen of them. read those first. then read them again."),
                           ("6.7", "Bidders may not contact MetroVolt staff about this procurement except through the clarification process in section 5.", "so: no calls to Priya. Vivian, please."),
                           ("9.1", "MetroVolt is not obliged to accept the lowest or any bid.", "")],
                  plain="the instructions to bidders are a contract about the contest itself. Break 6.7 and you can be excluded however good your bid is. The pass / fail lines matter more than any brilliant paragraph."),
    health=dict(now="a",
                g=("you've worked with them before", ["You already know who wrote which section.", "Read for changes since last time.", "Ask your contacts about history, through the proper channel."]),
                a=("new client, open contest", ["Read three times before writing.", "Treat the history as unknown and say so.", "Turn every gap into a question or an assumption."]),
                r=("it reads like it was written for someone else", ["Read for whether you can win at all.", "Count requirements only one supplier can meet.", "Go to bid / no-bid early; don't fall in love."])),
    pressure=dict(level=2, title="tender day", cost="one excited sales email · two engineers already designing",
                  items=["The pressure is to start, not to think. Two days of reading save two weeks of rewriting.", "Ask the engineers to put their sketches in a drawer until Monday. They'll be better on Monday."]),
    baseline="Each line compares <b>starting to write on day one</b> with <b>three reads and a one-page reading sheet first</b>.",
    ratings=[(3, 3, "The client doesn't see it yet; it shows later."),
             (2, 4, "The team stops designing the wrong thing at night."),
             (2, 4, "The three expensive sentences are found before they're priced."),
             (2, 4, "Everyone knows what's being asked."),
             (3, 4, "The design starts from the scoring and the risk, not a favourite pattern."),
             (2, 4, "The pass / fail lines can't surprise you."),
             (2, 3, "Questions are listed early, in writing."),
             (4, 3, "Two days before the first draft."),
             (4, 4, "One sheet.")],
    pitfalls=[("Writing on day one", "The architecture is sketched before anyone knows how it's scored.", "two days of reading, then a kick-off with the sheet."),
              ("Answering what you'd like to build", "A brilliant section that scores 5 % and a thin one that scores 20 %.", "write to the weights."),
              ("Skipping the pass / fail lines", "A missing certificate excludes a great bid.", "put them at the top of the sheet and assign an owner each."),
              ("Ignoring the history", "You find out about Orion at the orals, from the panel.", "ask what came before, in public, through the clarification process."),
              ("Breaking the contact rules", "A friendly call to the sponsor gets the bid excluded.", "every question goes through the procurement channel.")],
    grimoire=[(6, "rigged-rfp", "The Rigged RFP", "Not every tender with someone else's words in it is rigged; the Grimoire's entry shows how to tell, and when to walk away.")],
    use=["Any formal tender, RFP or framework call-off.", "Before the bid kick-off.", "Before deciding whether to bid at all.", "When a tender lands with an exciting subject line."],
    skip=["A two-page quote request for a small piece of work: one quick read and a phone call will do."],
    related=["<b>Should We Even Bid?</b> (next note)", "<b>Who Wrote This Tender?</b> (this volume)", "<b>What Do We Ask Before We Answer?</b> (this volume)", "<b>What Do They Actually Need?</b> (Sanne, vol. 3)"],
    quiz=[("What are the three reads of a tender?", "How it's scored, the work hidden in each “will” and “shall”, and the history nobody wrote down."),
          ("Why read the evaluation section first?", "It tells you what earns points and what excludes you, so you write to the weights."),
          ("What is a pass / fail requirement?", "A must-have that excludes the bid if it isn't met, however well you score elsewhere."),
          ("Which three Lodestar sentences carried most of the risk?", "Migrate all customer data, integrate with the existing billing system, and support for five years."),
          ("Why does the history matter if it isn't in the document?", "It explains the timetable, the wording and the client's fears; the panel will be thinking about it.")],
    quiz_sit=[("A colleague calls the sponsor to “just ask what they really want” during the tender. What do you do?", "Stop it, and put the question through the clarification process instead. Under the rules, contact outside the process can get the bid excluded, and the answer has to be shared with every bidder anyway.")],
    try_it="Take a tender, an RFP or even a detailed job advert. Read it three times with three colours: how it's scored, the promises in every “will”, and the history behind it. Fill one sheet. Which three sentences carry the most risk?",
    remember="A tender says <span class=\"hl\">how you'll be judged</span> on purpose, <span class=\"hl\">what the work is</span> in small print, and <span class=\"hl\">what went wrong before</span> only by accident.",
    late=dict(when="Thu 4 February 2027 · 23:10 · Leeds",
              lines=["Read it three times. The first time I loved it. The third time I found Orion in section 4.",
                     "Vivian thinks it's ours. Nothing is ours until someone signs.",
                     "Asked Hana and Lottie to put the whiteboard drawings in a drawer until Monday. Lottie looked hurt. Hana looked relieved."]),
    sources=["Crown Commercial Service, <i>Guidance for suppliers on bidding for public contracts</i>.",
             "Tom Sant, <i>Persuasive Business Proposals</i> (3rd ed., 2012).",
             "Association of Bid and Proposal Management Professionals (APMP), <i>Body of Knowledge</i>."],
)

# ------------------------------------------------------------------ 02 Should We Even Bid?
bn_problem = Doodle(760, 250, "Doodle of the bid / no-bid meeting on Wednesday 17 February 2027. Eight people at a table, a vote of six to two. On the wall, the cost of the bid: about 110 person-days, roughly 85,000 pounds, and Wrenfield's whole annual revenue of about nine million pounds next to Lodestar's five million.",
                    "Six for, two against. The bid alone costs £85k, and the prize is half a year's revenue.", exact=True)
bn_problem.box(40, 30, 300, 170, None, "paper", rx=60)
for i in range(8):
    x = 70 + (i % 4) * 66
    y = 22 if i < 4 else 188
    bn_problem.circle(x + 20, y + 10, 16, "green" if i not in (1, 6) else "pink")
bn_problem.head(190, 122, "6 – 2", size=34)
bn_problem.box(400, 30, 340, 70, "the bid itself", "y", sub="≈ 110 person-days · ≈ £85k", size=20, subsize=16)
bn_problem.box(400, 120, 160, 80, "Wrenfield", "paper", sub="≈ £9m / year", size=18, subsize=15)
bn_problem.box(580, 120, 160, 80, "Lodestar", "blue", sub="≈ £5m / 18 mo.", size=18, subsize=15)
bn_problem.note(380, 236, "a lot to win, and a lot to lose by winning badly", "red", size=19)

bn_how = Doodle(760, 330, "Wrenfield's bid / no-bid scorecard: ten questions scored 0 to 3. Do we know the client? Can we win on quality? Can we deliver it with named people? Is the price range realistic? Is the risk bounded? Do we have a reason to win? Is the incumbent beatable? Does it fit our strategy? Can we afford to lose it? Can we afford to win it? Total 19 out of 30 against a threshold of 18, with three conditions written underneath: paid discovery, Hana named as tech lead, and no twelve-month promise.",
                "Ten questions, scored honestly. 19 / 30 clears the bar by one, so the conditions matter more than the score.", exact=True)
qs = [("know the client?", 1), ("win on quality?", 2), ("named people?", 2), ("price realistic?", 2), ("risk bounded?", 1),
      ("reason to win?", 3), ("beat incumbent?", 2), ("fits strategy?", 3), ("afford to lose?", 2), ("afford to win?", 1)]
for i, (q, sc) in enumerate(qs):
    c, r = divmod(i, 5)
    x, y = 14 + c * 372, 14 + r * 46
    bn_how.box(x, y, 300, 38, q, "paper", size=17, rx=4)
    bn_how.box(x + 308, y, 50, 38, str(sc), ["pink", "y", "y", "green"][sc], size=19, rx=4)
bn_how.box(14, 252, 230, 64, "19 / 30", "y", sub="threshold 18", size=24, subsize=15)
bn_how.box(260, 252, 486, 64, "conditions", "blue", sub="paid discovery · Hana named · no “12 months”", size=19, subsize=16)

BID_NO_BID = dict(
    slug="bid-no-bid", date=date(2027, 2, 17), meta="bid day 15 of 50", where="LEEDS",
    kicker="a.k.a. “bid qualification” or “go / no-go”",
    tldr="A bid isn't free: Lodestar's will cost Wrenfield about <b>110 person-days</b> whether it wins or not. Decide whether to bid with a <b>scorecard</b> of honest questions (can we win, can we deliver, can we afford to lose, <b>can we afford to win?</b>), a written <b>reason to win</b>, and the <b>conditions</b> you'd need. Decide early, before anyone falls in love with the drawings, and write down why.",
    chips=[("Family", "reading the tender"), ("Lives in", "bid/lodestar/01-bid-no-bid.md"), ("Pairs with", "reading the tender, pricing models")],
    problem_side="Wrenfield, Leeds, 17 February 2027",
    problem="""  <p class="lead">Two weeks in, the bid team has already spent <b>31 person-days</b>. On <b>Wednesday 17 February</b> Graham Wren calls the bid / no-bid meeting: eight people, one hour, a vote. Vivian opens with “this is the one that changes Wrenfield”. That's exactly what worries Ines.</p>
  <ul>
    <li>Lodestar is worth about <b>£5m over 18 months</b>. Wrenfield's whole revenue last year was about <b>£9m</b>.</li>
    <li>A fixed-price failure that size wouldn't hurt Wrenfield: <span class="hl-pink">it could close it</span>.</li>
    <li>Wrenfield has never met Priya, Elaine or Hollis. Vexmoor has worked there for three years.</li>
    <li>The first vote is <b>6–2</b>. Ines votes against. So does Oskar.</li>
  </ul>""",
    problem_figs=[bn_problem],
    sides=dict(client=("Desmond hopes for bids", "<p>MetroVolt wants <b>at least three serious bids</b>, or the procurement looks uncompetitive and the board asks why. A bidder who drops out late, after asking forty questions, wastes evaluators' time. A bidder who bids badly wastes more.</p>", "Please bid properly, or tell us early you won't."),
                vendor=("Ines votes against, then for", "<p>Ines isn't against Lodestar. She's against <b>bidding it the way Vivian wants</b>: fixed price for everything, twelve months, whatever team is free. She'd vote for a bid with <b>paid discovery first</b>, Hana named as tech lead, and no twelve-month promise.</p>", "I'll say yes to the bid we can deliver, not the one we can sell.")),
    sides_after="The useful outcome of a bid / no-bid isn't the vote. It's the written conditions that the vote depends on.",
    analogy_side="the mountain guide's turn-back time",
    analogy="""  <p>A mountain guide decides <b>before the climb</b> whether conditions are good enough, and sets a <b>turn-back time</b>: if we're not at the summit by 13:00, we go down, however close it looks. The decision is made at the bottom, calmly, because at the top everyone is tired and the summit looks very close.</p>""",
    map=[("Checking the weather at the bottom", "The bid / no-bid scorecard"),
         ("“We go if the forecast is X”", "The conditions: paid discovery, named tech lead, no 12 months"),
         ("The turn-back time", "Re-check points: after clarifications, before pricing"),
         ("Summit fever", "Falling in love with the bid after six weeks' work"),
         ("Can the group survive a night out?", "Can Wrenfield survive winning badly?")],
    how_side="ten honest questions, a reason to win, and conditions",
    how="""  <p>Callum's scorecard has <b>ten questions, each scored 0–3</b>, filled in by each person alone before the meeting so the loudest voice doesn't set the scores. Lodestar averages <b>19 / 30</b>; Wrenfield's threshold is 18. The low scores are the useful part: <b>we don't know the client (1)</b>, <b>the risk isn't bounded (1)</b>, <b>could we afford to win? (1)</b>.</p>
  <p>Then the <b>reason to win</b>, in one sentence the panel would recognise: <i>“A small senior team that has moved a legacy customer system before, and will tell you the truth about your data.”</i> If you can't write it, don't bid.</p>
  <p>Ines changes her vote when the conditions go into the minutes: (1) a <b>paid discovery</b> phase before any fixed price; (2) <b>Hana</b> named as tech lead, not “a senior engineer”; (3) <b>no twelve-month promise</b> in writing. Graham agrees. A second check is set for <b>10 March</b>, after the clarification answers.</p>""",
    how_figs=[bn_how],
    steps=[("Count what the bid will cost", "People, days and the work you'll turn down meanwhile."),
           ("Score alone, then together", "Each person fills the scorecard before the meeting."),
           ("Read the low scores aloud", "They're the risks you'll be pricing."),
           ("Write the reason to win", "One sentence the panel would agree with. No sentence, no bid."),
           ("Write the conditions", "What must be true for a yes. Into the minutes."),
           ("Set a turn-back point", "A date to check the conditions again, and walk away if they fail.")],
    vocab=[("Bid / no-bid", "The decision whether to spend money competing for a contract."),
           ("Qualification", "Checking an opportunity against criteria before pursuing it."),
           ("Win theme", "The one reason a client should choose you, repeated across the bid."),
           ("Cost of sale", "What it costs to win (or lose) a contract: mostly people's time."),
           ("Win rate", "Bids won ÷ bids made; a falling one usually means poor qualification."),
           ("Turn-back point", "A planned moment to re-check the decision and withdraw if needed.")],
    code=dict(file="bid/lodestar/01-bid-no-bid.md", note="minutes · Wed 17 Feb 2027", src="""
BID / NO-BID · LODESTAR (MetroVolt)                 decision: BID, with conditions

scores (0–3, average of 8)      know the client 1 · win on quality 2 · named people 2
                                price realistic 2 · risk bounded 1 · reason to win 3
                                beat incumbent 2 · fits strategy 3 · afford to lose 2
                                afford to win 1                       total 19 / 30
cost of the bid                 ≈ 110 person-days (≈ £85k); 31 already spent
reason to win                   "a small senior team that has moved a legacy customer
                                 system before, and will tell you the truth about
                                 your data"
conditions (all three, or we withdraw)
  C1  paid discovery before any fixed price
  C2  Hana Sato named as tech lead in the bid
  C3  no 12-month promise, in writing or out loud
turn-back point                 Wed 10 Mar, after the clarification answers
vote                            6–2, then 8–0 with the conditions
"""),
    contract=dict(side="our own board's rules for bidding",
                  doc="Wrenfield Digital · bid policy v3", date="approved by the board, Jan 2026", stamp="conditions apply",
                  clauses=[("2.1", "Any bid above £1m or above 20 % of annual revenue requires a recorded bid / no-bid decision by the managing director and two directors.", "Lodestar is both."),
                           ("2.4", "Fixed-price bids above £2m require a priced risk register and a named delivery lead before submission.", "Ines, apparently."),
                           ("2.6", "Conditions recorded at bid / no-bid must be re-confirmed before submission.", "C3 is going to be fun.")],
                  plain="the most important contract in a bid is the one with your own firm. Writing the conditions into the minutes turns “Ines is worried” into “the board decided”."),
    health=dict(now="a",
                g=("you know them and they know you", ["The scorecard is quick.", "The reason to win is your track record there.", "Still write the conditions."]),
                a=("first contact, strong fit", ["Score honestly; low scores become risks to price.", "Conditions in the minutes.", "A turn-back date after the answers."]),
                r=("the client barely knows you exist", ["Ask whether you're making up the numbers.", "No reason to win, no bid.", "Spend the 110 days on a client who knows you."])),
    pressure=dict(level=3, title="the vote", cost="one hour · one awkward vote against the room",
                  items=["Voting against an exciting deal feels disloyal. Vote against the risk, not the deal, and say what would change your mind.", "If your conditions are in the minutes, you don't have to win the argument twice."]),
    baseline="Each line compares <b>bidding because it's big and exciting</b> with <b>a scorecard, a reason to win and written conditions</b>.",
    ratings=[(3, 3, "The client doesn't see it."),
             (2, 4, "The team knows the bid won't promise the impossible."),
             (1, 4, "Paid discovery and no twelve-month promise protect the price."),
             (2, 3, "The conditions shape the scope early."),
             (3, 4, "Hana named means the design has a real owner."),
             (1, 4, "Risks are named before they're priced."),
             (2, 4, "The board's decision is in the minutes."),
             (4, 3, "An hour, and the scoring beforehand."),
             (4, 4, "One page.")],
    pitfalls=[("Deciding by excitement", "The size of the prize decides, not the odds.", "score alone first, then talk."),
              ("No reason to win", "The bid says the same as everyone else's.", "one sentence the panel would recognise, or no bid."),
              ("Conditions nobody wrote down", "The worries are forgotten by week five.", "conditions in the minutes, re-checked before submission."),
              ("Never walking away", "Six weeks in, it's too late emotionally.", "set a turn-back date and keep it."),
              ("Forgetting “can we afford to win?”", "A big fixed price can hurt more than losing.", "score it explicitly.")],
    use=["Any bid that costs more than a few days.", "Any fixed price, or a deal large for your firm.", "When the room is excited.", "Before the first draft, and again after clarifications."],
    skip=["A repeat order from a client you know, on terms you've delivered before."],
    related=["<b>How Do I Read a Tender?</b> (previous note)", "<b>Fixed Price, or Time and Materials?</b> (this volume)", "<b>What If Sales Already Promised?</b> (this volume)", "<b>Build vs Buy</b> (Ana, vol. 2)"],
    quiz=[("Why fill in the scorecard alone first?", "So the most senior or loudest person doesn't set everyone's scores."),
          ("What is a reason to win?", "One sentence that says why this client should choose you; if you can't write it, don't bid."),
          ("Why ask “can we afford to win?”", "A large fixed-price contract can hurt a small firm more than losing it would."),
          ("What turned Ines's vote from no to yes?", "Three conditions in the minutes: paid discovery, Hana named, and no twelve-month promise."),
          ("What is a turn-back point?", "A planned date to re-check the conditions and withdraw if they've failed.")],
    quiz_sit=[("At the turn-back point the clarification answers say discovery can't be paid separately. What do you do?", "Condition C1 has failed, so go back to Graham and the directors: either withdraw, or price the discovery risk into the fixed price openly and re-vote. Don't quietly carry on.")],
    try_it="Take an opportunity you're chasing (a bid, a project, a job). Score it on the ten questions, alone. Write your reason to win in one sentence, and three conditions for a yes. Would you still go?",
    remember="Decide at the bottom of the mountain. <span class=\"hl\">Write the conditions</span>, and keep the <span class=\"hl\">turn-back time</span>.",
    late=dict(when="Wed 17 February 2027 · 22:48 · Leeds",
              lines=["Voted against. Felt like voting against Christmas.",
                     "Then Graham wrote my three conditions into the minutes and I voted for. Vivian said I'd “come round”. I haven't. The bid has.",
                     "Afford to win: 1. Nobody else scored that one below 2. I hope I'm wrong."]),
    sources=["APMP, <i>Body of Knowledge</i>: opportunity qualification and bid / no-bid.",
             "David Maister, <i>Managing the Professional Service Firm</i> (1993).",
             "Neil Rackham, <i>SPIN Selling</i> (1988): qualifying large sales."],
)

# ------------------------------------------------------------------ 03 Who Wrote This Tender?
ww_problem = Doodle(760, 250, "Doodle of tender section 4 next to an old Vexmoor slide from Orion. The same phrases appear on both: Golden Customer Record, the hub, single view of the customer. Ines draws lines between them.",
                    "Section 4 of the tender and an Orion slide from 2024, side by side. Five matching phrases.", exact=True)
ww_problem.box(24, 20, 300, 200, None, "paper", rx=4)
ww_problem.head(174, 50, "Lodestar ITT · §4", size=20)
ww_problem.box(460, 20, 276, 200, None, "blue", rx=4)
ww_problem.head(598, 50, "Orion slide, 2024", size=20)
for i, t in enumerate(["Golden Customer Record", "“the hub”", "single customer view", "survivorship rules", "R4.7: reuse the hub?"]):
    y = 82 + i * 28
    ww_problem.text(40, y, t, anchor="start", size=16)
    if i < 4:
        ww_problem.text(476, y, t, anchor="start", size=16)
        ww_problem.line(f"M300 {y - 5} L470 {y - 5}", color="red", dash=True, thin=True)
ww_problem.note(380, 242, "familiarity, or a head start?", "red", size=20)

ww_how = Doodle(760, 300, "A decision tree for a tender that seems written for someone else. First question: are there requirements only one supplier can meet? If yes, ask about them in a clarification question, and if the answer keeps them, consider not bidding. If no, it's probably familiarity: the client copied the words they knew. Then ask openly whether reuse is expected, design for what the client needs, and use their words where they help.",
                "Copied words are usually familiarity, not a fix. The test is whether only one supplier could meet a requirement.", exact=True)
ww_how.box(230, 14, 300, 64, "only one supplier", "y", sub="could meet a requirement?", size=20, subsize=16)
ww_how.arrow(300, 80, 160, 130, label="yes", lx=210, ly=100)
ww_how.arrow(460, 80, 600, 130, label="no", lx=550, ly=100)
ww_how.box(14, 132, 300, 74, "ask about it", "pink", sub="in a clarification", size=19, subsize=16)
ww_how.arrow(164, 208, 164, 228)
ww_how.box(14, 230, 300, 56, "kept? consider no-bid", "pink", size=18)
ww_how.box(446, 132, 300, 74, "familiarity", "green", sub="they used words they knew", size=19, subsize=16)
ww_how.arrow(596, 208, 596, 228)
ww_how.box(446, 230, 300, 56, "ask openly · design for need", "green", size=17)

WHO_WROTE = dict(
    slug="who-wrote-the-tender", date=date(2027, 2, 19), meta="bid day 17 of 50", where="LEEDS",
    kicker="a.k.a. “wired tenders, and the much commoner copied ones”",
    tldr="When a tender uses another supplier's words, it tells you <b>who the client has been talking to</b>, not necessarily that the game is fixed. The test: are there requirements <b>only one supplier could meet</b>? If yes, ask about them openly in a clarification question and be ready to walk away. If not, it's familiarity: <b>ask whether reuse is expected</b>, design for what the client actually needs, and borrow their words where it helps them read your bid.",
    chips=[("Family", "reading the tender"), ("Lives in", "the reading sheet's pink column"), ("Pairs with", "clarification questions, the incumbent")],
    problem_side="Wrenfield, 19 February 2027",
    problem="""  <p class="lead">Hana finds it first. Section 4 of the tender describes customer data in five phrases: “Golden Customer Record”, “the hub”, “single customer view”, “survivorship rules” and, in <b>requirement 4.7</b>, “reuse of existing hub components where appropriate”. Four of them are on a <b>2024 Vexmoor slide</b> about Orion, still on a conference website.</p>
  <ul>
    <li>Vexmoor built Orion's data hub. Orion was cancelled in January.</li>
    <li>If “the hub” must be reused, Vexmoor knows it and nobody else does.</li>
    <li>Vivian: “It's rigged. We should complain.” Graham: “We should withdraw.” <span class="hl-pink">Neither has asked a single question yet.</span></li>
  </ul>""",
    problem_figs=[ww_problem],
    sides=dict(client=("Desmond, under deadline", "<p>Desmond had three weeks to turn a business case into a tender. Section 4 came from the Orion requirements, because they were the only written description of MetroVolt's customer data. He removed Orion's name. <b>He didn't notice the vocabulary.</b></p>", "We reused what we had. That's not favouritism, that's January."),
                vendor=("Hana and Ines", "<p>To Wrenfield it looks like a head start for Vexmoor. Maybe it is. But <b>requirement 4.7 says “where appropriate”</b>, not “must”. The only way to find out is to ask, in writing, where every bidder will see the answer.</p>", "Are we being told to build on Orion, or allowed to?")),
    sides_after="Most “wired” tenders are written by busy people who copied what they had. A few really are written for one supplier. The clarification answer tells you which.",
    analogy_side="the house listing written by the old owner",
    analogy="""  <p>A house for sale is described with the previous owner's words: “the snug”, “Dad's workshop”. That tells you who wrote the listing, not that the house is promised to a relative. But if the listing says <b>“buyers must keep the workshop exactly as it is”</b>, you'd want to ask why, before you make an offer.</p>""",
    map=[("The old owner's words", "Orion's vocabulary in section 4"),
         ("“The snug”", "“Golden Customer Record”"),
         ("“Must keep the workshop”", "A requirement only one supplier could meet"),
         ("Asking the estate agent in writing", "A clarification question, answered to all bidders"),
         ("Walking away from the viewing", "A no-bid, if the answer keeps the lock-in")],
    how_side="test for lock-in, ask openly, then decide",
    how="""  <p>Ines and Hana go through section 4 requirement by requirement with one question: <b>could only one supplier meet this?</b> Three phrases are just vocabulary. One (4.7, “reuse of existing hub components where appropriate”) could become a lock-in if MetroVolt meant “must”.</p>
  <p>They write it as a neutral clarification question, with no accusation and no hint of Wrenfield's design: <i>“Requirement 4.7: is reuse of Orion components expected, or may bidders propose an alternative approach to customer data?”</i> The answer, published to all bidders on <b>3 March</b>: <b>“Bidders may propose reuse; no Orion component is mandated.”</b> The same answer list shows that Vexmoor asked whether it <i>may</i> reuse the hub. They plan to. That's useful too.</p>
  <p>Wrenfield keeps bidding, uses MetroVolt's words (“customer record”, not “golden”) where it helps the evaluators, and designs for what MetroVolt needs rather than for or against Orion.</p>""",
    how_figs=[ww_how],
    steps=[("Notice the borrowed words", "Phrases, structure, odd specifics: write them down."),
           ("Apply the one-supplier test", "Could only one firm meet this requirement as written?"),
           ("Ask, neutrally, in writing", "Through the clarification process; no accusations."),
           ("Read the answer, and the others' questions", "Both tell you how the field is thinking."),
           ("Decide with the facts", "Lock-in confirmed: re-run bid / no-bid. Familiarity: carry on."),
           ("Never badmouth the last supplier", "The panel worked with them; some of them liked them.")],
    vocab=[("Wired tender", "A tender written so only one supplier can win; rarer than people think."),
           ("Lock-in requirement", "A requirement only one supplier can meet: a named product, years on a platform."),
           ("Neutral question", "A clarification question that reveals nothing about your design or suspicions."),
           ("Challenge", "A formal complaint about a procurement; a last resort with real costs."),
           ("Head start", "Knowledge one bidder has from past work; legal, but you need to price around it."),
           ("Client vocabulary", "The client's own words for things; use them so evaluators can score you.")],
    code=dict(file="bid/lodestar/02-borrowed-words.md", note="Hana and Ines · Fri 19 Feb 2027", src="""
SECTION 4 · borrowed words                       source: Vexmoor/Orion slide, 2024

phrase / requirement                   only one supplier?   action
"Golden Customer Record"               no (vocabulary)      say "customer record"
"the hub"                              no (vocabulary)      avoid; say "customer data service"
"single customer view"                 no                   use it: it's MetroVolt's goal too
"survivorship rules"                   no                   explain in plain words
R4.7 "reuse of existing hub            MAYBE (if "must")    clarification Q-07, neutral
      components where appropriate"

Q-07 (sent 22 Feb): "Requirement 4.7: is reuse of Orion components expected, or may
bidders propose an alternative approach to customer data?"
A (3 Mar, to all): "Bidders may propose reuse; no Orion component is mandated."
also seen in the Q&A: Vexmoor asked if it MAY reuse the hub   → they will
decision: keep bidding; design for need; don't mention Orion unless asked
"""),
    contract=dict(side="the rules on equal treatment", doc="Lodestar ITT · instructions to bidders", date="3 Feb 2027", stamp="answered to all",
                  clauses=[("5.2", "Clarification questions must be submitted in writing by 24 February 2027. MetroVolt will publish all questions and answers, without the name of the bidder, to every bidder.", "so the question must be useful to us even when Vexmoor reads it."),
                           ("5.5", "Where a clarification changes the requirements, MetroVolt will issue an addendum and may extend the deadline.", "4.7 wasn't changed. just explained.")],
                  plain="equal treatment cuts both ways: your questions are shown to rivals, and their questions are shown to you. Ask neutrally, and read everyone else's questions as intelligence."),
    health=dict(now="a",
                g=("you know the client well", ["Ask your contact which parts came from history, through the proper channel.", "Familiarity is easy to spot.", "Still ask in writing."]),
                a=("new client, one suspicious requirement", ["One-supplier test.", "One neutral question.", "Decide on the answer, not the feeling."]),
                r=("the answer confirms lock-in", ["Re-run bid / no-bid.", "A formal challenge only with advice and a reason.", "Walking away politely keeps the next door open."])),
    pressure=dict(level=2, title="suspicion", cost="one heated conversation · two people ready to quit the bid",
                  items=["Suspicion spreads faster than facts. Ask the question before you have the argument.", "Write the question as if the client will read it aloud, because they will."]),
    baseline="Each line compares <b>complaining or withdrawing on a hunch</b> with <b>the one-supplier test and a neutral question</b>.",
    ratings=[(2, 4, "A calm question reads better than an accusation."),
             (3, 4, "The team stops arguing about a hunch."),
             (3, 3, "Neutral."),
             (2, 4, "Reuse is optional: in writing."),
             (2, 4, "Wrenfield designs for need, not against Orion."),
             (2, 4, "The lock-in risk is tested, not guessed."),
             (2, 4, "The answer is published to all."),
             (4, 4, "One question."),
             (4, 4, "Nothing to keep up.")],
    pitfalls=[("Seeing a conspiracy in every copied phrase", "Most tenders borrow from what came before.", "apply the one-supplier test."),
              ("Asking a loaded question", "“Why is this tender written for Vexmoor?” helps nobody.", "ask what's expected, neutrally."),
              ("Revealing your design in a question", "Rivals read every question.", "ask about the requirement, not your solution."),
              ("Attacking the last supplier", "The panel worked with them for three years.", "talk about what you'll do, not what they did."),
              ("Challenging without advice", "A formal challenge costs money and goodwill.", "only with a clear breach, and proper advice.")],
    grimoire=[(6, "rigged-rfp", "The Rigged RFP", "shows the real thing: a requirement nobody but one firm can meet, and how Pip decided not to bother.")],
    use=["A tender uses a past supplier's vocabulary.", "A requirement names a product, platform or years of experience on it.", "Someone on the team says “it's rigged”."],
    skip=["The words are generic industry terms everyone uses."],
    related=["<b>How Do I Read a Tender?</b> (this volume)", "<b>What Do We Ask Before We Answer?</b> (next note)", "<b>How Do We Compete with a Big Consultancy?</b> (this volume)", "<b>Technology Evaluation</b> (Ana, vol. 2)"],
    quiz=[("What is the one-supplier test?", "Asking whether only one supplier could meet a requirement as written."),
          ("Why are most “wired” tenders not really wired?", "Busy people copy the only written description they have, usually from the last project."),
          ("Why must a clarification question be neutral?", "Every bidder sees it, and the client reads it; it should reveal nothing and accuse no one."),
          ("What did the Q&A reveal about Vexmoor?", "They asked whether they may reuse the Orion hub, so they plan to."),
          ("Why not criticise Orion in the bid?", "The panel worked on it; attacking it attacks them.")],
    quiz_sit=[("The answer had said “bidders must reuse the hub”. What then?", "That's a lock-in. Go back to bid / no-bid: can you price learning the hub, or partner, or is it a no? A formal challenge only with advice and a clear reason.")],
    try_it="Take a tender or a requirements document you've received. Highlight any phrase you've seen in someone else's material. Apply the one-supplier test to each. Which one would you ask about, and how would you word it neutrally?",
    remember="Borrowed words usually mean <span class=\"hl\">a tired author</span>, not a fixed game. <span class=\"hl\">Ask neutrally</span>, then decide.",
    late=dict(when="Fri 19 February 2027 · 22:30 · Leeds",
              lines=["Vivian wanted to complain to procurement. Graham wanted to withdraw. Hana wanted to ask a question. Hana won.",
                     "If it's rigged, we lose a week. If it isn't, we nearly threw away the best bid we've ever written.",
                     "Note: never write “golden” in our bid. Never write “Orion” either."]),
    sources=["Crown Commercial Service, <i>Procurement Policy Notes</i> on equal treatment and transparency.",
             "OECD, <i>Guidelines for Fighting Bid Rigging in Public Procurement</i> (2009): what real rigging looks like.",
             "APMP, <i>Body of Knowledge</i>: competitive analysis."],
)

# ------------------------------------------------------------------ 04 What Do We Ask Before We Answer?
cq_problem = Doodle(760, 240, "Doodle of the clarification log. 63 questions from all bidders, nine of them Wrenfield's. Lottie's first draft of a question reads like a design document: it mentions an event stream, the strangler pattern and Wrenfield's data tool by name. Ines circles it in red: every rival will read this.",
                    "Lottie's first question gave away half the design. Every bidder reads every question.", exact=True)
cq_problem.box(24, 20, 380, 180, None, "paper", rx=4)
cq_problem.head(214, 50, "draft Q (Lottie)", size=20)
for i, t in enumerate(["“For our event-stream", "strangler approach using", "Wrenfield DataLens, can", "MAVIS emit change events?”"]):
    cq_problem.text(44, 84 + i * 28, t, anchor="start", size=17)
cq_problem.line("M12 10 h404 v200 h-404 z", color="red", dash=True)
cq_problem.box(450, 30, 286, 70, "63 questions", "y", sub="from all bidders", size=22, subsize=16)
cq_problem.box(450, 120, 286, 70, "9 of them ours", "blue", sub="all published to all", size=20, subsize=16)
cq_problem.note(380, 228, "a clarification is a public document", "red", size=20)

cq_how = Doodle(760, 300, "A filter for clarification questions. Each candidate question passes three gates. Gate one: does the answer change our price, our risk or our design? If not, drop it. Gate two: does the wording reveal our solution or our weakness? If so, reword it. Gate three: can the answer be given in one or two sentences? If not, split it. Out of 31 candidate questions, nine are sent.",
                "Three gates: does it change the price, does it give anything away, can it be answered briefly? 31 in, 9 out.", exact=True)
cq_how.box(14, 110, 110, 80, "31 ideas", "y", size=19)
gates = [("changes price, risk", "or design?"), ("gives nothing", "away?"), ("answerable", "in 2 lines?")]
for i, (a, b) in enumerate(gates):
    x = 160 + i * 168
    cq_how.box(x, 100, 140, 100, a, "blue", sub=b, size=16, subsize=15)
    cq_how.arrow(x - 32, 150, x - 4, 150)
cq_how.arrow(642, 150, 670, 150)
cq_how.box(674, 110, 72, 80, "9", "green", size=26)
cq_how.note(230, 236, "drop: 14", "red", size=18)
cq_how.note(398, 236, "reword: 6", "pen", size=18)
cq_how.note(566, 236, "split: 2", "pen", size=18)
cq_how.note(380, 40, "and read all 63 answers, not just yours", "red", size=19)

CLARIFICATIONS = dict(
    slug="clarification-questions", date=date(2027, 2, 23), meta="bid day 21 of 50", where="LEEDS",
    kicker="a.k.a. “the clarification period”",
    tldr="Clarification questions are <b>public</b>: every bidder sees every question and every answer. Ask only what <b>changes your price, risk or design</b>; word it so it <b>reveals nothing</b> about your solution or your doubts; and keep it <b>answerable in two sentences</b>. Then read <b>all</b> the answers, especially the questions other bidders asked. They're the only honest look you'll get at how your rivals think.",
    chips=[("Family", "reading the tender"), ("Lives in", "bid/lodestar/03-clarifications.md"), ("Pairs with", "reading the tender, assumptions")],
    problem_side="Wrenfield, 23 February 2027",
    problem="""  <p class="lead">The clarification window closes on <b>Wednesday 24 February</b> at 17:00. The team has <b>31 candidate questions</b>. Lottie's first draft asks whether MAVIS can emit change events <i>“for our event-stream strangler approach using Wrenfield DataLens”</i>.</p>
  <ul>
    <li>It names Wrenfield's design, its tool and its pattern, <span class="hl-pink">in a document every rival will read</span>.</li>
    <li>Fourteen of the 31 wouldn't change anything about the price or the plan.</li>
    <li>Two are really five questions in one, which MetroVolt would answer with “please refer to the tender”.</li>
  </ul>""",
    problem_figs=[cq_problem],
    sides=dict(client=("Desmond answers 63 questions", "<p>Every answer has to be checked by Hollis, Elaine or legal, then published to all. Desmond has <b>one week</b>. Long, vague or leading questions get a short, safe answer: <b>“please refer to the tender”</b>.</p>", "Ask me something I can answer in two lines."),
                vendor=("Ines filters 31 into 9", "<p>Each question is a chance to <b>shrink a risk</b> before pricing it, but also a window rivals can look through. Ines wants answers that change Wrenfield's price or plan, without telling Vexmoor what Wrenfield is planning.</p>", "If the answer won't change a number, why ask?")),
    sides_after="Good questions help both sides: the client finds the holes in its own tender, and every bidder prices the same thing.",
    analogy_side="questions at a press conference",
    analogy="""  <p>At a press conference every journalist hears every question. A good reporter asks the one question that gets <b>a fact they can use</b>, in words that don't reveal their story. A bad one gives a speech, asks three things at once, and gets “no comment”. And the smartest reporters listen hardest to <b>everyone else's</b> questions.</p>""",
    map=[("Every journalist hears every question", "Every bidder sees every clarification"),
         ("A question that reveals your story", "A question that reveals your design"),
         ("“No comment”", "“Please refer to the tender”"),
         ("Listening to rivals' questions", "Reading all 63, not just your 9"),
         ("One fact you can print", "One answer that changes your price")],
    how_side="three gates, then read everything",
    how="""  <p>Each of the 31 candidates goes through <b>three gates</b>. <b>Does the answer change our price, risk or design?</b> Fourteen don't, so they become assumptions instead. <b>Does the wording give anything away?</b> Six are reworded: Lottie's becomes <i>“Does MAVIS provide any mechanism to identify records changed since a given time? If so, please describe it.”</i> <b>Can it be answered in two sentences?</b> Two are split. Nine are sent.</p>
  <p>The answers come back on <b>3 March</b>: all 63, from five bidders. Three of Wrenfield's change the price (data volumes, the Halvorsen interface and that discovery can be paid separately). And the other bidders' questions are a map: Vexmoor asked about reusing Orion's hub and about offshore delivery; someone asked about the five-year support term four different ways.</p>""",
    how_figs=[cq_how],
    steps=[("List every question", "Everything anyone on the team wonders. Don't filter yet."),
           ("Gate 1: does it change a number?", "No? Make it an assumption instead."),
           ("Gate 2: does it give anything away?", "Reword it to ask about the requirement, not your answer."),
           ("Gate 3: two-sentence answer?", "Split anything compound."),
           ("Send before the deadline, not at it", "Late questions get rushed answers."),
           ("Read all the answers as a team", "Mark what changes the bid; note what rivals asked.")],
    vocab=[("Clarification question", "A written question to the client during a tender; answers go to all bidders."),
           ("Q&A log", "The published list of all questions and answers; part of the tender."),
           ("Addendum", "A formal change to the tender issued after questions."),
           ("Leading question", "A question that assumes or pushes an answer; it usually gets a non-answer."),
           ("Assumption", "What you'll write down and price when you choose not to ask."),
           ("Competitive intelligence", "What you can learn about rivals legitimately, e.g. from their published questions.")],
    code=dict(file="bid/lodestar/03-clarifications.md", note="sent Tue 23 Feb 2027; answers Wed 3 Mar", src="""
CLARIFICATIONS · LODESTAR                             31 candidates → 9 sent

#     question (as sent)                                       changes   answer (3 Mar)
Q-01  How many customer records are in MAVIS, by status?      price     2.31m live, 4.9m closed
Q-03  Does MAVIS provide a way to identify records changed    design    nightly extract only
      since a given time? If so, please describe it.
Q-05  Will MetroVolt provide a sample of customer records     risk      yes: 10,000 records
      to the preferred bidder before contract?                          by 1 April, to all shortlisted
Q-06  Will the billing supplier provide interface             risk      "the billing supplier will
      specifications and support to the new supplier?                   support integration"
Q-07  Requirement 4.7: is reuse of Orion components expected? design    no component mandated
Q-09  May discovery be priced and contracted separately?      price     yes

dropped → assumptions: 14 · reworded: 6 · split: 2
seen from rivals: reuse of the Orion hub (Vexmoor) · offshore delivery · 5-yr support ×4
"""),
    contract=dict(side="how answers become part of the deal", doc="Lodestar ITT · instructions to bidders", date="3 Feb 2027", stamp="part of the ITT",
                  clauses=[("5.4", "Answers published under paragraph 5.2 form part of the tender documents and will be incorporated into the contract with the successful bidder.", "so Q-05's “sample by 1 April” is now a promise. good."),
                           ("5.6", "MetroVolt may decline to answer questions it considers commercially sensitive or already addressed in the tender.", "the “please refer to the tender” clause.")],
                  plain="a clarification answer is part of the contract you'll sign. That's what makes a good question valuable: it turns a client's vague intention into a written commitment, for every bidder."),
    health=dict(now="a",
                g=("you have history with the client", ["Fewer questions; you know the answers.", "Still ask in writing for the things you'll price.", "Read rivals' questions."]),
                a=("open contest, foggy tender", ["Three gates, nine good questions.", "Turn the rest into assumptions.", "Read all 63 answers together."]),
                r=("the client answers nothing", ["Price the fog: assumptions and contingency.", "Ask yourself if you still want to bid.", "Don't resend the same question angrily."])),
    pressure=dict(level=2, title="question week", cost="a deadline at 17:00 · one junior's pride",
                  items=["Rewording someone's question can sting. Explain the rule (every rival reads it), not the mistake.", "Lottie's reworded question got the most useful answer of the nine. Tell her."]),
    baseline="Each line compares <b>sending every question as written</b> with <b>three gates and reading all the answers</b>.",
    ratings=[(3, 4, "Short, answerable questions look professional."),
             (3, 4, "Fewer, better answers to wait for."),
             (2, 4, "Three answers changed the price."),
             (2, 4, "The sample and paid discovery are now in writing."),
             (3, 4, "The design wasn't given away."),
             (2, 4, "Rivals' questions show where they're heading."),
             (2, 4, "Answers form part of the contract."),
             (3, 3, "An afternoon of filtering."),
             (4, 4, "A log.")],
    pitfalls=[("Giving away your design", "A question names your pattern, tool or plan.", "ask about the requirement, not your answer."),
              ("Asking everything", "Thirty questions, most of which change nothing.", "the ones that don't change a number become assumptions."),
              ("Compound questions", "Five questions in one get one vague answer.", "one question, two-sentence answer."),
              ("Only reading your own answers", "You miss what rivals are planning.", "read all of them as a team."),
              ("Asking at the deadline", "Rushed answers, or none.", "send early.")],
    use=["Every formal tender with a clarification window.", "When an answer would change your price, risk or design.", "When a requirement could be read two ways."],
    skip=["The answer wouldn't change anything you'd do: write an assumption instead."],
    related=["<b>Who Wrote This Tender?</b> (previous note)", "<b>What Are We Assuming?</b> (this volume)", "<b>How Do I Read a Tender?</b> (this volume)", "<b>What Do They Actually Need?</b> (Sanne, vol. 3)"],
    quiz=[("Who sees a clarification question?", "Every bidder, along with its answer."),
          ("What are the three gates?", "Does it change price, risk or design; does it give anything away; can it be answered in two sentences."),
          ("What happens to a question that fails gate one?", "It becomes an assumption instead."),
          ("Why do clarification answers matter after the contract?", "They become part of the tender documents and the contract."),
          ("What did Wrenfield learn from Vexmoor's questions?", "That Vexmoor plans to reuse Orion's hub and may deliver offshore.")],
    quiz_sit=[("A colleague wants to ask “Why is the timetable so short?” What do you suggest?", "It's leading and won't change a number. If the timetable is a risk, ask something answerable, e.g. whether the contract start date is fixed, or write an assumption about the start date.")],
    try_it="Take the open questions on a proposal you're working on. Put each through the three gates. How many would you actually send, and how would you reword one so a rival learns nothing from it?",
    remember="Every rival reads your questions. Ask what <span class=\"hl\">changes a number</span>, in words that <span class=\"hl\">give nothing away</span>.",
    late=dict(when="Tue 23 February 2027 · 21:55 · Leeds",
              lines=["Thirty-one questions became nine. Lottie's became the best one, once it stopped describing our design.",
                     "Fourteen went into the assumptions list instead. That list is going to be long.",
                     "Reminder: read all 63 answers on the 3rd. Especially the ones that aren't ours."]),
    sources=["Crown Commercial Service, <i>Guidance for suppliers</i>: the clarification process.",
             "APMP, <i>Body of Knowledge</i>: questions and clarifications.",
             "Tom Sant, <i>Persuasive Business Proposals</i> (2012)."],
)

NOTES = [READING_A_TENDER, BID_NO_BID, WHO_WROTE, CLARIFICATIONS]
