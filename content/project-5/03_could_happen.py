# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 5 · What could happen? (the Risk domain, part 1)
# Narrator: Sanne. Facts: docs/larder-casebook.md, "Book 3, Vol. 5"; numbers in the comment block of 01_involved.py.
# Scales (16 Nov 2026): probability 1 <10 % · 2 10–30 % · 3 30–50 % · 4 50–70 % · 5 >70 %;
#   impact 1 <1 week or <€2k · 2 1–2 weeks or €2–5k · 3 2–4 weeks or €5–15k · 4 4–8 weeks or €15–50k · 5 >8 weeks or >€50k.
#   score = P × I: red ≥ 12, amber 6–11, green ≤ 5.

RISK = ["risk"]

# ------------------------------------------------------------------ 08 How Will We Handle Risk?
ra_problem = Doodle(760, 260, "Doodle of 16 November 2026. Sanne asks Femke a question before listing any risks: would she pay nine thousand euros for an extra month's rent, keys on 1 May instead of 1 June, to give the fit-out a month of margin? Femke says no: a few weeks' slip is survivable, nine thousand on an empty store isn't. Neither of them puts a price on a week of delay.",
                    "“A month's rent for a month of margin?” Femke: no. Nobody asks what a week of delay costs.", exact=True)
ra_problem.box(20, 24, 330, 140, None, "y")
ra_problem.head(185, 60, "the question", size=19)
ra_problem.text(185, 94, "keys 1 May, not 1 June", size=16)
ra_problem.text(185, 122, "+ €9k rent", size=16)
ra_problem.box(410, 24, 330, 140, None, "blue")
ra_problem.head(575, 60, "Femke", size=19)
ra_problem.text(575, 94, "“a few weeks is survivable”", size=16)
ra_problem.text(575, 122, "“€9k on an empty store isn't”", size=16)
ra_problem.note(380, 210, "an appetite with a price on one side only", "red", size=19)
ra_problem.note(380, 242, "a week late ≈ €15k of lost contribution (Marco, May 2026)", "pen", size=16)

ra_analogy = Doodle(760, 250, "Doodle of a family planning a long hike. Before choosing the route they agree how much risk they'll take: no ridges in high wind, turn back if the weather turns by noon, who carries the first-aid kit, how they'll judge a stream crossing. Then they pick the route.",
                    "Before the route: how much risk we'll take, when we turn back, who carries the kit.", exact=True)
ra_analogy.row([("appetite", "no ridges in wind", "y"), ("thresholds", "turn back at noon", "pink"), ("roles", "who has the kit", "blue"), ("scales", "how we judge a stream", "green")], y=40, h=96, size=17, subsize=13)
ra_analogy.note(380, 196, "agreed before the hike, not on the ridge", "pen", size=19)

ra_how = Doodle(760, 460, "Antwerp's risk approach, signed by Femke on 16 November 2026, on one page in five parts. Appetite: schedule, a slip of up to two weeks is tolerable; money, keep within the budget and its contingency. Thresholds: a forecast slip over two weeks or a draw beyond the contingency goes to Femke. Scales: probability one to five, from under ten percent to over seventy; impact one to five, from under a week or two thousand euros to over eight weeks or fifty thousand. Score is probability times impact: twelve and above red, six to eleven amber, five and below green. Roles: every risk has a Larder owner; Sanne keeps the register. Rhythm: the leads review it every other Thursday; the top five go in Femke's Friday note; the steering group sees it monthly.",
                "One page: appetite, thresholds, scales, roles, rhythm. The rule “a Larder owner for every risk” is in it.", exact=True)
ra_how.box(14, 14, 360, 130, None, "y")
ra_how.head(194, 42, "appetite", size=18)
ra_how.text(194, 74, "schedule: ≤ 2 weeks tolerable", size=15)
ra_how.text(194, 100, "money: within budget + contingency", size=15)
ra_how.text(194, 126, "(price of a week: not written)", size=13)
ra_how.box(386, 14, 360, 130, None, "pink")
ra_how.head(566, 42, "thresholds → Femke", size=18)
ra_how.text(566, 74, "forecast slip > 2 weeks", size=15)
ra_how.text(566, 100, "a draw beyond contingency", size=15)
ra_how.box(14, 156, 732, 150, None, "paper")
ra_how.head(380, 184, "scales", size=18)
ra_how.text(30, 214, "P", anchor="start", size=15)
ra_how.text(30, 240, "I", anchor="start", size=15)
for k, (pp, ii) in enumerate([("<10 %", "<1 wk · €2k"), ("10–30 %", "1–2 wks · €5k"), ("30–50 %", "2–4 wks · €15k"), ("50–70 %", "4–8 wks · €50k"), (">70 %", "more")]):
    cx = 120 + k * 132
    ra_how.head(cx - 50, 214, str(k + 1), anchor="start", size=14)
    ra_how.text(cx - 34, 214, pp, anchor="start", size=13)
    ra_how.head(cx - 50, 240, str(k + 1), anchor="start", size=14)
    ra_how.text(cx - 34, 240, ii, anchor="start", size=12)
ra_how.text(380, 280, "score = P × I:  red ≥ 12 · amber 6–11 · green ≤ 5", size=15)
ra_how.box(14, 318, 360, 130, None, "blue")
ra_how.head(194, 346, "roles", size=18)
ra_how.text(194, 378, "every risk: a Larder owner", size=15)
ra_how.text(194, 404, "register kept by Sanne", size=15)
ra_how.box(386, 318, 360, 130, None, "green")
ra_how.head(566, 346, "rhythm", size=18)
ra_how.text(566, 378, "leads: every other Thursday", size=15)
ra_how.text(566, 404, "top 5 in Femke's Friday note", size=15)
ra_how.text(566, 430, "steering group: monthly", size=15)

APPROACH = dict(
    slug="risk-approach",
    kicker="a.k.a. planning risk management: appetite, thresholds, scales, roles",
    tldr="Before listing a single risk, agree <b>how the project will handle risk</b>: the sponsor's <b>appetite</b> (how much slip, overspend or exposure they'll accept), the <b>thresholds</b> that send a decision upstairs, the <b>scales</b> for probability and impact so everyone scores the same way, <b>roles</b> (every risk gets an owner), and the <b>rhythm</b> of reviews. One page, signed by the sponsor. Put a price on both sides of the appetite: what it costs to be safer, and what a week of delay costs.",
    chips=[("Family", "what could happen"), ("Lives in", "one page, signed by the sponsor"), ("Pairs with", "the risk register, the budget and its reserves, who decides what")],
    pmbok=dict(covers="deciding how risk will be handled: appetite, thresholds, scales, categories, roles, reserves and the review rhythm",
               domains=RISK + ["governance"], processes=["Plan Risk Management"], principles=["Be an accountable leader"], focus=["planning"],
               older="6th: “Plan Risk Management” (11.1), the risk management plan, probability and impact definitions. 7th: the Uncertainty domain."),
    problem_side="Larder, 16 November 2026",
    problem="""  <p class="lead">Before listing any risks, Sanne asks Femke one question: would she pay <b>€9,000</b> for an extra month's rent, keys on <b>1 May instead of 1 June</b>, to give the fit-out a month of margin? Femke says no. “A few weeks' slip is survivable. Nine thousand euros on an empty store isn't.” It's a fair answer, and an appetite statement. <span class="hl-pink">But it has a price on one side only.</span> In May Marco had worked out that a city opening a week earlier is worth about <b>€15k</b>; nobody puts that number beside the €9k.</p>
  <ul>
    <li>Appetite is said aloud, not written.</li>
    <li>The cost of being late isn't on the table.</li>
    <li>Nobody has agreed how risks will be scored.</li>
  </ul>""",
    problem_figs=[ra_problem],
    analogy_side="the hike",
    analogy="""  <p>A family planning a long hike agrees a few things before choosing the route: <b>no ridges in high wind</b>; if the weather turns, <b>turn back by noon</b>; who carries the <b>first-aid kit</b>; how they'll judge whether a stream is safe to cross. Then they choose a route that fits. Families who agree this on the ridge, in the wind, argue instead of deciding.</p>""",
    analogy_figs=[ra_analogy],
    map=[("No ridges in wind", "Appetite: a slip of up to two weeks tolerable; money within the contingency"),
         ("Turn back by noon", "Thresholds: over two weeks or beyond contingency goes to Femke"),
         ("Judging a stream", "Scales: probability and impact, 1 to 5"),
         ("Who carries the kit", "Roles: a Larder owner for every risk"),
         ("Checking the sky every hour", "Rhythm: leads every other Thursday, steering monthly")],
    how_side="one page, five parts, signed",
    how="""  <p>Sanne writes the approach on one page and Femke signs it on <b>16 November</b>. <b>Appetite</b>: on schedule, a slip of up to two weeks is tolerable; on money, stay within the budget and its contingency. <b>Thresholds</b>: a forecast slip over two weeks, or a draw beyond the contingency, goes to Femke. <b>Scales</b>: probability 1–5 (under 10 % to over 70 %), impact 1–5 (under a week or €2k, up to over eight weeks or €50k); the score is probability × impact; 12 and above is red. <b>Roles</b>: <b>every risk has a Larder owner</b>; Sanne keeps the register. <b>Rhythm</b>: the leads review it every other Thursday, the top five go into Femke's Friday note, the steering group sees it monthly. The categories come from Rotterdam's lessons plus one new one: <b>Belgium</b>. What the page doesn't have is the price of a week of delay. That line is added to the playbook eleven months later.</p>""",
    how_figs=[ra_how],
    steps=[("Ask the sponsor for appetite, with numbers", "Time, money, reputation."),
           ("Price both sides", "What safety costs; what a week late costs."),
           ("Set thresholds that go upstairs", "Matching the decision rights."),
           ("Agree scales before scoring", "Words and numbers for 1 to 5."),
           ("Name roles and the rule for owners", "One owner per risk, inside the organisation."),
           ("Fix the rhythm", "Who reviews, how often, where it's reported.")],
    vocab=[("Risk", "An uncertain event that, if it happens, affects the project, for worse (a threat) or better (an opportunity)."),
           ("Risk appetite", "How much uncertainty the sponsor is willing to accept for the reward."),
           ("Risk threshold", "The level at which a risk needs a decision from someone higher."),
           ("Probability and impact scales", "Agreed definitions of each score, so everyone rates alike."),
           ("Risk categories", "Groups that prompt a search for risks: site, people, systems, partners, rules."),
           ("Risk owner", "The person who watches a risk and makes sure its response happens.")],
    code=dict(file="antwerp/08-risk-approach.md", note="Sanne, signed by Femke, 16 November 2026", plain=True, src="""
# ANTWERP · HOW WE HANDLE RISK                                  signed: Femke (sponsor)

APPETITE     schedule: a slip of up to 2 weeks is tolerable
             money: within the budget and its contingency; no rent before 1 Jun
THRESHOLDS   to Femke: forecast slip > 2 weeks · a draw beyond the contingency ·
             any risk scoring 20 or more
SCALES       P 1 <10 % · 2 10–30 % · 3 30–50 % · 4 50–70 % · 5 >70 %
             I 1 <1 week or <€2k · 2 1–2 weeks or €2–5k · 3 2–4 weeks or €5–15k ·
               4 4–8 weeks or €15–50k · 5 >8 weeks or >€50k
             score = P × I · red >= 12 · amber 6–11 · green <= 5
CATEGORIES   site + building · people · systems · partners · Belgium (rules, language)
             · market · and opportunities in each
ROLES        every risk has a LARDER owner · Sanne keeps the register
RHYTHM       leads: every other Thursday · top 5 in Femke's Friday note · steering monthly
RESERVES     contingency (Sanne, by change) · management reserve (Femke): sized in Feb

added Oct 2027 (playbook v3): PRICE OF A WEEK LATE ≈ €15k contribution + €2k rent
"""),
    tools="tools: the sponsor's time, one page, two scales, the decision rights, and Marco's price of a week.",
    dial=[("Light", "a short internal piece of work", ["Ask the sponsor what would be too late or too dear.", "High / medium / low.", "Review at each check-in."]),
          ("Standard", "Antwerp", ["One page: appetite, thresholds, scales, roles, rhythm.", "Both sides priced.", "Signed by the sponsor."]),
          ("Heavy", "large regulated programmes", ["A full risk management plan.", "Quantified thresholds per objective.", "Independent risk function and audits."])],
    baseline="Each line compares <b>appetite said aloud, nothing written</b> to <b>a one-page risk approach with thresholds, scales, owners and rhythm, signed by the sponsor</b>.",
    ratings=[(3, 4, "Risk effort fits what the sponsor cares about."),
             (2, 3, "Thresholds bring decisions earlier."),
             (2, 4, "Everyone scores on the same scales."),
             (2, 4, "Appetite and thresholds are written."),
             (3, 4, "Femke signed what she'll accept."),
             (3, 4, "Owners are part of the rule."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "An hour with the sponsor.")],
    pitfalls=[("No appetite asked", "You guess what the sponsor accepts.", "ask, with numbers."),
              ("Price on one side", "Safety looks expensive, delay looks free.", "price a week of delay too."),
              ("Scales agreed later", "Scores mean different things.", "agree them before scoring."),
              ("A rule nobody checks", "“Every risk has an owner”, on paper.", "check it at every review.")],
    use=["At the start, before the register.", "When the sponsor changes.", "When the project enters a riskier phase or place.", "When scores start to disagree."],
    skip=["Never; on small work it's three sentences."],
    related=["<b>How Much Do We Set Aside?</b> (vol. 4)", "<b>Who Decides What?</b> (vol. 2)", "<b>What Could Happen?</b> (next note)", "<b>Was It Worth It?</b> (vol. 4)"],
    quiz=[("Name the five parts of the risk approach.", "Appetite, thresholds, scales, roles, rhythm."),
          ("What is risk appetite?", "How much uncertainty the sponsor will accept for the reward."),
          ("What did the page leave out?", "The price of a week late (≈ €15k contribution + rent)."),
          ("A lead scores a risk “high” and another “3”. What's missing?", "Agreed scales with definitions; use the page's 1–5 scales."),
          ("Your sponsor says “no risk is acceptable.” What do you ask?", "What a slip or overspend would cost them, and what they'd pay to avoid it; zero risk has a price too.")],
    try_it="Ask your sponsor two questions: how late or how far over would be too much, and what would you pay to be safer? Then work out what a week of delay costs, and put both on one page.",
    remember="Agree when you'll <span class=\"hl\">turn back</span> before you're on the <span class=\"hl\">ridge</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, planning risk management.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.1 Plan Risk Management.",
             "Project Management Institute, <i>The Standard for Risk Management in Portfolios, Programs, and Projects</i> (2019)."],
)

# ------------------------------------------------------------------ 09 What Could Happen?
rr_problem = Doodle(760, 260, "Doodle of Monday 30 November 2026 and Sanne's mistake for this collection. Row R-07 of the new Antwerp risk register: permit delayed. Probability one, impact three, score three, green. Owner: the builder. Response: the builder handles permits. In Rotterdam that was true. Two rules of her own page are broken in one row: the owner isn't at Larder, and the score comes from another country.",
                    "R-07: “permit delayed”, score 3, owner “builder”. Two of her own rules broken in one row.", exact=True)
rr_problem.box(20, 24, 720, 110, None, "paper")
rr_problem.text(40, 62, "R-07  permit delayed", anchor="start", size=18)
rr_problem.text(40, 98, "P 1 · I 3 · score 3 (green) · owner: builder · “builder handles permits”", anchor="start", size=15)
rr_problem.box(20, 150, 340, 70, "owner outside Larder", "pink", size=17)
rr_problem.box(400, 150, 340, 70, "scored by Rotterdam", "pink", size=17)
rr_problem.note(380, 248, "the risk that would set the date, at the bottom of the list", "red", size=17)

rr_analogy = Doodle(760, 250, "Doodle of a ship's pilot taking a ship into an unfamiliar harbour. The chart marks every known hazard: the sandbank, the wreck, the strong tide at the entrance, each with a note of what to do. A hazard written as 'water' helps nobody. A hazard on someone else's chart, from another harbour, is worse than none.",
                    "A harbour chart: each hazard named, placed, and with what to do. Another harbour's chart is worse than none.", exact=True)
rr_analogy.row([("sandbank", "keep to the buoys", "y"), ("wreck", "200 m clear", "pink"), ("tide at the gate", "enter at slack", "blue")], y=40, h=96, size=17, subsize=13)
rr_analogy.note(380, 196, "this harbour's chart, kept up to date", "pen", size=19)

rr_how = Doodle(760, 470, "Antwerp's risk register, 30 November 2026, the top ten of twenty-three rows by score. Each row: ID, the risk, probability, impact, score, owner. R-02 hiring forty in Antwerp on time, three by three, nine, Joost. R-03 builder late, three by three, nine, Sanne. R-08 courier contracts, three by three, nine, Joost. R-04 Bancontact not ready by July, two by four, eight, Cho. R-05 Belgian VAT wrong, two by four, eight, Marco. R-01 cold room late, two by three, six, Sanne. R-06 texts sound wrong, three by two, six, Grace. R-10 a rival opens first, two by three, six, Femke. R-09 neighbours object to noise, two by two, four, no owner. R-07 permit delayed, one by three, three, builder. Two opportunities: O-01 reuse Rotterdam's shelving design, O-02 landlord pays insulation.",
                "Ten of twenty-three rows. R-07, the one that set the date, is last, with an owner outside Larder.", exact=True)
hdr = [("ID", 14), ("risk", 80), ("P", 470), ("I", 510), ("score", 550), ("owner", 630)]
for h, x in hdr:
    rr_how.head(x, 30, h, anchor="start", size=15)
rows_rr = [("R-02", "hiring 40 in Antwerp on time", 3, 3, "Joost"), ("R-03", "builder late", 3, 3, "Sanne"),
           ("R-08", "courier contracts", 3, 3, "Joost"), ("R-04", "Bancontact not ready by July", 2, 4, "Cho"),
           ("R-05", "Belgian VAT wrong", 2, 4, "Marco"), ("R-01", "cold room late", 2, 3, "Sanne"),
           ("R-06", "texts sound wrong", 3, 2, "Grace"), ("R-10", "a rival opens first", 2, 3, "Femke"),
           ("R-09", "neighbours object to noise", 2, 2, "–"), ("R-07", "permit delayed", 1, 3, "builder")]
for i, (rid, txt, p, im, own) in enumerate(rows_rr):
    y = 44 + i * 36
    sc = p * im
    fill = "pink" if sc >= 12 else ("y" if sc >= 6 else "green")
    bad = rid in ("R-07", "R-09")
    rr_how.box(8, y, 744, 30, None, "paper", rx=4, stroke="red" if bad else "")
    rr_how.text(14, y + 21, rid, anchor="start", size=14)
    rr_how.text(80, y + 21, txt, anchor="start", size=14)
    rr_how.text(476, y + 21, str(p), anchor="start", size=14)
    rr_how.text(516, y + 21, str(im), anchor="start", size=14)
    rr_how.box(548, y + 3, 56, 24, str(sc), fill, size=13, rx=4)
    rr_how.text(630, y + 21, own, anchor="start", size=14)
rr_how.box(8, 412, 744, 48, "O-01 reuse Rotterdam's shelving design · O-02 landlord pays insulation", "green", size=15)

rr_deep1 = Doodle(760, 300, "Anatomy of a risk statement, using R-07 as Sanne rewrote it on 10 February 2027. Cause: because Antwerp requires an environmental permit, with a public inquiry, for a cooling plant this size and deliveries before seven. Event: the permit may not be granted by early July. Effect: which would delay installing the cold room and the opening by four to eight weeks, and cost about forty thousand euros. Below, the November version for comparison: permit delayed.",
                  "Cause, event, effect. “Permit delayed” names a worry; the full sentence names what to watch and what to do.", exact=True)
rr_deep1.row([("because…", "a permit + public inquiry is required", "y"), ("…may happen…", "not granted by early July", "pink"), ("…which would…", "delay opening 4–8 wks, ~€40k", "blue")], y=24, h=110, size=18, subsize=13, gap=34, arrows=True)
rr_deep1.box(14, 170, 732, 60, "November: “permit delayed”", "paper", size=17)
rr_deep1.note(380, 270, "the cause tells you what to watch; the effect tells you what it's worth", "pen", size=16)

REGISTER_R = dict(
    slug="risk-register",
    kicker="a.k.a. identifying risks: the risk register",
    tldr="<b>Identify risks</b> with the people who know the work and the place: walk the plan, the categories, past lessons, assumptions and the experts. Write each one as <b>cause, event, effect</b> (“because X, Y may happen, which would Z”), so you know what to watch and what it's worth. Give each a <b>score</b>, an <b>owner inside the organisation</b>, a <b>response</b> and a <b>review date</b>, in a <b>register</b>. Include <b>opportunities</b>: good things that might happen if you help them. A register is only as good as its least-checked row.",
    chips=[("Family", "what could happen"), ("Lives in", "one table, reviewed every other Thursday"), ("Pairs with", "the risk approach, probability and impact, risk responses")],
    pmbok=dict(covers="finding threats and opportunities, writing them so they can be acted on, and recording them with owners and responses in the risk register",
               domains=RISK, processes=["Identify Risks"], principles=["Adopt a holistic view"], focus=["planning", "monitoring and controlling"],
               older="6th: “Identify Risks” (11.2), the risk register and risk report. 7th: the Uncertainty domain."),
    problem_side="Larder, 30 November 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. The leads' workshop produces <b>23 risks</b> and Sanne writes them up on Monday 30 November. Row <b>R-07</b> reads: <b>permit delayed</b>. Probability 1, impact 3, score 3, green. Owner: <b>the builder</b>. Response: “builder handles permits.” In Rotterdam that was true. <span class="hl-pink">The row breaks two rules of the page Femke signed two weeks earlier: the owner isn't at Larder, and the score comes from another country.</span> Nobody notices, because a green row near the bottom is the last thing anyone reads.</p>
  <ul>
    <li>The risk was written as a worry (“permit delayed”), not as cause, event and effect.</li>
    <li>Its owner had no reason, or contract, to watch it for Larder.</li>
    <li>The neighbours' risk, R-09, had no owner at all.</li>
  </ul>""",
    problem_figs=[rr_problem],
    meanwhile=[("architect-6", "risk-register", "Ana's architecture risk register (from April 2028) writes each risk as cause, event and effect, with an owner and a response, and reviews it with the teams.",
                "Sanne's Antwerp register is the same tool for a launch, and its R-07 shows what happens when one row has an owner outside the organisation."),
               ("product-3", "pre-mortem", "Grace's pre-mortem imagines the launch has already failed and asks the team why: a quick way to surface risks nobody wants to say.",
                "Sanne uses one at the Antwerp risk workshop; it finds the courier contracts and the texts, but nobody in the room knows Belgian permits.")],
    analogy_side="the harbour chart",
    analogy="""  <p>A pilot bringing a ship into a harbour uses a chart that marks every <b>known hazard</b>: the sandbank, the wreck, the strong tide at the entrance, each with <b>what to do</b>: keep to the buoys, stay 200 metres clear, enter at slack water. A hazard written as “water” helps nobody. A chart of <b>another harbour</b> is worse than none: it gives confidence and the wrong depths.</p>""",
    analogy_figs=[rr_analogy],
    map=[("Each hazard on the chart", "Each risk as cause, event, effect"),
         ("What to do at each", "An owner and a response"),
         ("The tide tables", "A score and a review date"),
         ("A chart of another harbour", "R-07 scored by Rotterdam's rules"),
         ("Sheltered water to use", "Opportunities: Rotterdam's shelving design, the landlord's insulation")],
    how_side="cause, event, effect; an owner inside Larder; opportunities too",
    how="""  <p>The workshop on <b>Thursday 26 November</b> uses four sources: the <b>categories</b> from the risk approach (site, people, systems, partners, Belgium, market), <b>Rotterdam's lessons</b>, the plan's <b>assumptions</b> (“the builder handles permits” was one), and a <b>pre-mortem</b>, like Grace's: “It's October 2027 and Antwerp opened late. Why?” It finds 19 threats and 4 opportunities. Sanne writes each as <b>cause, event, effect</b>, scores it on the agreed scales, and gives it an <b>owner</b>, a <b>response</b> and a review date. The top three are hiring forty people on time, the builder, and the courier contracts. Two opportunities get owners at once: <b>reuse Rotterdam's shelving design</b> (Tomás) and ask the <b>landlord to pay for roof insulation</b> (Femke). What the room lacks is anyone who knows Belgian permits. R-07 is fixed on <b>10 February</b>, after Maarten and Pieter, and rewritten as a sentence (see “going deeper”).</p>""",
    how_figs=[rr_how],
    steps=[("Gather people who know the work and the place", "Including a local expert."),
           ("Use several sources", "Categories, lessons, assumptions, a pre-mortem."),
           ("Write each as cause, event, effect", "So it can be watched and valued."),
           ("Score it on the agreed scales", "And note who scored it."),
           ("Give it an owner inside the organisation", "And a response and a date."),
           ("Add opportunities", "With owners too.")],
    vocab=[("Risk register", "The list of risks with their scores, owners, responses and status."),
           ("Threat", "A risk that would hurt the project if it happened."),
           ("Opportunity", "A risk that would help the project if it happened."),
           ("Risk statement", "“Because [cause], [event] may happen, which would [effect].”"),
           ("Assumption", "Something taken as true without proof; each one hides a risk."),
           ("Pre-mortem", "Imagine the project has failed and ask why.")],
    code=dict(file="antwerp/09-risk-register.md", note="Sanne, 30 November 2026 (top 10 of 23; R-07 as first written)", plain=True, src="""
# ANTWERP · RISK REGISTER                                       v1 · 30 Nov 2026 · 23 rows

ID    RISK                                P  I  SCORE  OWNER   RESPONSE (v1)
R-02  hiring 40 in Antwerp on time        3  3   9     Joost   Belgian agency from May
R-03  builder late on handover            3  3   9     Sanne   late penalty; weekend priced
R-08  courier contracts (Belgian rules)   3  3   9     Joost   Lena + Maarten review, Feb
R-04  Bancontact not ready by July        2  4   8     Cho     certification plan, Jan
R-05  Belgian VAT / invoices wrong        2  4   8     Marco   tested on 100 orders, Mar
R-01  cold room delivered late            2  3   6     Sanne   order in week 1 of the lease
R-06  French / Flemish texts sound wrong  3  2   6     Grace   native writers
R-10  a rival opens first                 2  3   6     Femke   accept; watch
R-09  neighbours object to noise          2  2   4     -       -
R-07  permit delayed                      1  3   3     builder "builder handles permits"
O-01  reuse Rotterdam's shelving design   3  saves ~€6k   Tomás   exploit: send the drawings
O-02  landlord pays roof insulation       2  saves ~€4k   Femke   enhance: ask at works approval

R-07 REWRITTEN 10 Feb 2027  Because Antwerp requires an environmental permit, with a
  public inquiry, for a cooling plant this size and deliveries before 07:00, the permit
  may not be granted by early July, which would delay the cold room and the opening by
  4-8 weeks and cost ~€40k.  P 4 · I 4 · 16 (red) · owner Sanne · R-09 merged in as a cause
"""),
    tools="tools: a workshop, the categories, the plan's assumptions, a pre-mortem, a local expert, and one table.",
    deep_dive=dict(
        side="writing a risk, where risks come from, opportunities, and keeping a register alive",
        intro="Most risk registers start as a good workshop and end as a forgotten spreadsheet. This chapter shows how to write a risk so it can be acted on, where to look for the ones a workshop misses, why opportunities belong in the same table, and the five columns that keep a register alive.",
        parts=[
            ("Writing a risk: cause, event, effect", """  <p>“Permit delayed” is a worry. A risk statement has three parts: <b>because</b> of a cause (a fact, true today), an <b>event</b> may happen (uncertain), which <b>would</b> have an effect on an objective (dates, money, quality). The <b>cause</b> tells you what to watch and where a response can act. The <b>effect</b> tells you what it's worth, so you can score it. The event in the middle is what you're actually uncertain about.</p>
  <p>Rewritten on 10 February, R-07 told Sanne three things the November row hadn't: the cause was a Belgian rule (so a Belgian expert should own the paperwork), the event had a date (granted by early July), and the effect had a size (4–8 weeks, about €40k).</p>""", [rr_deep1]),
            ("Where risks come from, and where workshops miss them", """  <p>A workshop finds the risks the people in the room know about. To find the rest, use sources that don't depend on memory:</p>
  <ul>
    <li><b>Categories</b> (a risk breakdown structure): site, people, systems, partners, rules, market. Walk each one.</li>
    <li><b>Assumptions</b>: every “we assume” in the plan is a risk with its probability hidden. “The builder handles permits” was one.</li>
    <li><b>Lessons</b> from earlier projects, and their issue logs: Rotterdam's internet line.</li>
    <li><b>Experts outside the room</b>, especially on a new place: Maarten found in an hour what the workshop missed.</li>
    <li><b>A pre-mortem</b>: imagining failure makes it safe to say the awkward thing.</li>
  </ul>""", []),
            ("Opportunities belong in the same table", """  <p>A risk can be good: something that might happen and would help. Antwerp had four. Writing them down gives them an <b>owner</b>, and owned opportunities happen more often. <b>O-01</b>, reusing Rotterdam's shelving design, saved about €6k because Tomás sent the drawings to Pieter in January instead of waiting to be asked. <b>O-02</b>, the landlord paying for roof insulation, didn't happen; Femke asked, and the landlord said no. Both cost nothing to try.</p>
  <p>Opportunities also balance the numbers: the reserve is sized from threats <b>minus</b> opportunities (two notes on).</p>""", []),
            ("Keeping it alive: five columns and one habit", """  <p>A register stays useful when every row has five things: a <b>score</b> on agreed scales, an <b>owner inside the organisation</b>, a <b>response</b> (not “monitor”), a <b>trigger</b> (the sign that it's starting to happen) and a <b>next review date</b>. Rows missing any of them are where surprises come from: R-07 and R-09 were both missing an owner.</p>
  <p>The habit: review the <b>bottom</b> of the list too. A green row scored by the wrong person is more dangerous than a red one everyone watches. From February Sanne reads three low-scoring rows aloud at every review and asks: who scored this, and would they still?</p>""", []),
        ]),
    dial=[("Light", "small work", ["Five risks in a list.", "An owner each.", "Reviewed at check-ins."]),
          ("Standard", "Antwerp", ["A register of cause, event, effect.", "Score, owner, response, trigger, date.", "Opportunities too; reviewed fortnightly."]),
          ("Heavy", "large programmes", ["A risk breakdown structure.", "Risk workshops per phase.", "Registers rolled up to programme and portfolio."])],
    baseline="Each line compares <b>a register of worries with one owner outside Larder</b> to <b>cause-event-effect rows, each with a Larder owner, a response, a trigger and a date</b>.",
    ratings=[(3, 4, "Effort goes to what could hurt the launch."),
             (2, 3, "Known risks priced into the dates."),
             (2, 4, "Twenty-three risks found in November."),
             (2, 4, "Every risk and its owner on one page."),
             (2, 4, "The steering group sees the top five each month."),
             (3, 4, "Leads own their risks."),
             (3, 4, "Responses ready before they're needed."),
             (3, 3, "Neutral."),
             (3, 3, "A workshop, then an hour a fortnight.")],
    pitfalls=[("Worries, not statements", "Nothing to watch or value.", "cause, event, effect."),
              ("Owner outside the organisation", "Nobody watches it for you.", "a Larder owner, always."),
              ("Only threats", "Good luck goes unclaimed.", "add opportunities with owners."),
              ("Unread bottom rows", "Wrong scores hide there.", "read a few low rows aloud each review.")],
    use=["At the start, with the plan.", "At each phase and each new place.", "When an assumption turns out false.", "When an expert joins."],
    skip=["Never; on small work it's a list of five."],
    related=["<b>How Will We Handle Risk?</b> (previous note)", "<b>Risk Register</b> (Ana, vol. 6)", "<b>Risk-Storming</b> (Ana, vol. 1)", "<b>Pre-mortem</b> (Grace, vol. 3)"],
    quiz=[("What three parts make a risk statement?", "Cause, event, effect: “because X, Y may happen, which would Z.”"),
          ("Which two rules did R-07 break?", "Its owner wasn't at Larder; it was scored by Rotterdam's rules, by nobody who knew Belgium."),
          ("Why put opportunities in the register?", "Owned opportunities happen more often, and they balance the reserve."),
          ("A lead says “we assume the landlord hands over the keys on 1 June.” What do you do?", "Write it as a risk: because the lease date depends on the landlord's works, keys may come late, which would delay the fit-out; score it, owner Femke."),
          ("At a review, a green row's score was set by a supplier. What do you ask?", "Who at Larder owns it, and would someone who knows the subject still score it that low?")],
    try_it="Take your risk list. Rewrite the three lowest-scoring rows as “because…, … may happen, which would…”. Check each has an owner inside your organisation. Add one opportunity.",
    remember="Chart <span class=\"hl\">this</span> harbour. Every hazard with <span class=\"hl\">what to do</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, identifying risks.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.2 Identify Risks.",
             "David Hillson, <i>Effective Opportunity Management for Projects</i> (2004): risk meta-language.",
             "Gary Klein, “Performing a Project Premortem”, <i>Harvard Business Review</i> (2007)."],
)

# ------------------------------------------------------------------ 10 How Likely, and How Bad?
pb_problem = Doodle(760, 260, "Doodle of Wednesday 10 February 2027. Sanne phones Pieter, site manager of the Belgian builder, after Maarten's review. Pieter: the permit is yours, not ours; with deliveries before seven it's the regular procedure, with a public inquiry; four to six months is normal, longer if neighbours object. R-07 had been scored one for probability by people who had never applied for one in Belgium.",
                    "Pieter: “The permit is yours, not ours. Four to six months is normal.” R-07 had been scored 1.", exact=True)
pb_problem.box(20, 24, 330, 140, None, "paper")
pb_problem.head(185, 60, "R-07 in November", size=19)
pb_problem.text(185, 94, "P 1 · I 3 = 3", size=16)
pb_problem.text(185, 122, "scored by Rotterdam people", size=16)
pb_problem.box(410, 24, 330, 140, None, "pink")
pb_problem.head(575, 60, "Pieter, 10 Feb", size=19)
pb_problem.text(575, 94, "“yours, not ours”", size=16)
pb_problem.text(575, 122, "“4–6 months is normal”", size=16)
pb_problem.note(380, 210, "a score is only as good as the person who gave it", "red", size=19)
pb_problem.note(380, 242, "nobody who'd applied in Belgium had been asked", "pen", size=16)

pb_analogy = Doodle(760, 250, "Doodle of a weather forecast for a wedding in another country. The couple's guess from home: it never rains in June. The local forecaster, who knows the coast: thirty percent chance of a storm in the afternoon, and when it comes it's heavy. They move the ceremony to the morning. Same scale, a better-informed score.",
                    "“It never rains in June” vs the local forecaster: 30 %, and heavy when it comes.", exact=True)
pb_analogy.box(14, 40, 350, 100, "the couple's guess", "y", sub="“never rains in June”", size=17, subsize=14)
pb_analogy.box(396, 40, 350, 100, "the local forecaster", "blue", sub="30 %, and heavy", size=17, subsize=14)
pb_analogy.arrow(366, 90, 392, 90)
pb_analogy.note(380, 190, "ask the person who knows this coast", "pen", size=19)

pb_how = Doodle(760, 470, "The probability and impact grid, five by five, with Antwerp's risks before and after the re-score of 10 February 2027. Cells with a score of twelve or more are red, six to eleven amber, five or less green. R-07 permit moves from probability one, impact three to probability four, impact four: score sixteen, red. R-09 neighbours object is merged into R-07 as a cause. R-03 builder late moves from three by three to two by three after Pieter's crew plan. R-02 hiring stays at three by three. Arrows show the moves.",
                "Re-scored after two calls: R-07 from 3 to 16. R-03 down, after Pieter's crew plan.", exact=True)
cell, gx, gy = 108, 150, 20
for pi_ in range(5):
    for ii in range(5):
        p, im = 5 - pi_, ii + 1
        sc = p * im
        fill = "pink" if sc >= 12 else ("y" if sc >= 6 else "green")
        pb_how.box(gx + ii * cell, gy + pi_ * 76, cell - 6, 70, None, fill, rx=4)
        pb_how.text(gx + ii * cell + 14, gy + pi_ * 76 + 20, str(sc), anchor="start", size=12)
for k in range(5):
    pb_how.text(gx + k * cell + cell / 2 - 3, gy + 5 * 76 + 22, str(k + 1), size=15)
    pb_how.text(gx - 18, gy + k * 76 + 42, str(5 - k), size=15)
pb_how.text(gx + 2.5 * cell, gy + 5 * 76 + 50, "impact →", size=15)
pb_how.text(60, gy + 2.5 * 76, "probability", size=15)

def pos(p, im):
    return gx + (im - 1) * cell + (cell - 6) / 2, gy + (5 - p) * 76 + 42
x1, y1 = pos(1, 3); x2, y2 = pos(4, 4)
pb_how.text(x1, y1 + 8, "R-07", size=14)
pb_how.box(x2 - 36, y2 - 16, 72, 32, "R-07", "paper", size=14, rx=4, stroke="red")
pb_how.arrow(x1 + 20, y1 - 8, x2 - 30, y2 + 14, color="red")
x3, y3 = pos(3, 3); x4, y4 = pos(2, 3)
pb_how.text(x3 - 22, y3 + 4, "R-03", size=13)
pb_how.text(x4 - 22, y4 + 10, "R-03", size=13)
pb_how.arrow(x3 - 22, y3 + 12, x4 - 22, y4 - 6, dash=True)
pb_how.text(x3 + 26, y3 + 4, "R-02", size=13)

QUAL = dict(
    slug="probability-and-impact",
    kicker="a.k.a. qualitative risk analysis: probability and impact",
    tldr="<b>Qualitative analysis</b> ranks risks quickly: score each one's <b>probability</b> and <b>impact</b> on the agreed scales, multiply, and plot them on a <b>grid</b> so the worst are visible. Add what the grid misses: how <b>soon</b> it could happen, how easy it is to <b>spot</b>, which risks share a <b>cause</b>. A score is only as good as the person who gave it, so score with people who know the work and the place, write down who scored, and <b>re-score</b> whenever someone better informed speaks up.",
    chips=[("Family", "what could happen"), ("Lives in", "the register's P, I and score columns, and a 5 × 5 grid"), ("Pairs with", "the risk register, expected monetary value, risk responses")],
    pmbok=dict(covers="ranking risks by probability and impact, and by urgency, detectability and shared causes, to decide which need attention first",
               domains=RISK, processes=["Analyze Risks"], principles=["Adopt a holistic view"], focus=["planning", "monitoring and controlling"],
               older="6th: “Perform Qualitative Risk Analysis” (11.3), the probability and impact matrix. 7th: the Uncertainty domain."),
    problem_side="Antwerp, 10 February 2027",
    problem="""  <p class="lead">Two days after Maarten's review, Sanne phones <b>Pieter</b>, site manager of the Belgian builder. She asks him about R-07. <span class="hl-pink">“The permit is yours, not ours. With deliveries before seven it's the regular procedure, with a public inquiry. Four to six months is normal; longer if the neighbours object.”</span> R-07 had been scored probability 1 in November, by a room of people who had opened Rotterdam and Zuid and had never applied for a permit in Belgium. The scale was fine. The scorers weren't the right ones.</p>
  <ul>
    <li>Scores came from the wrong experience.</li>
    <li>Nobody had written down who scored what.</li>
    <li>The neighbours' risk and the permit risk shared a cause and were scored apart.</li>
  </ul>""",
    problem_figs=[pb_problem],
    analogy_side="the local forecast",
    analogy="""  <p>A couple planning a wedding on another country's coast guess from home: “It never rains there in June.” The <b>local forecaster</b>, who knows that coast, says <b>30 % chance of a storm</b> in the afternoon, and when it comes it's heavy. Same scale, a better-informed score. They move the ceremony to the morning. The forecast didn't change the weather; it changed what they did.</p>""",
    analogy_figs=[pb_analogy],
    map=[("“It never rains in June”", "R-07 scored 1 by people who knew Rotterdam"),
         ("The local forecaster", "Pieter and Maarten, who know Belgian permits"),
         ("30 %, and heavy", "Probability 4, impact 4: score 16"),
         ("Same scale", "The scales of 16 November, unchanged"),
         ("Moving the ceremony", "Responses chosen on 22 February")],
    how_side="the grid, the right scorers, and the re-score",
    how="""  <p>Sanne re-scores with what Maarten and Pieter know. <b>R-07, the permit</b>: probability from 1 to <b>4</b> (50–70 % that it's not granted by early July, given four to six months and an application not yet started), impact from 3 to <b>4</b> (a 4–8 week slip, about €40k): <b>16, red</b>, the top of the register. <b>R-09, the neighbours</b>, is merged into R-07 as one of its causes: their objections would happen in the permit's public inquiry. <b>R-03, the builder</b>, goes down from 9 to 6: Pieter has a second crew for the two weeks that matter. Three other columns are added to every row: <b>who scored it</b>, <b>how soon</b> it could strike (R-07: the application must go in by the end of March), and <b>how we'd notice</b> (the city's completeness letter; the inquiry's objections). Femke's Friday note that week opens with R-07. It goes over her threshold, so it's her decision how much to spend on it.</p>""",
    how_figs=[pb_how],
    steps=[("Score with people who know the work and the place", "And write who scored."),
           ("Use the agreed scales", "Words and numbers."),
           ("Plot on the grid", "Red, amber, green."),
           ("Add urgency and detectability", "How soon; how would we notice?"),
           ("Merge risks with a shared cause", "Score the cause once."),
           ("Re-score when better information arrives", "The same day.")],
    vocab=[("Qualitative analysis", "Ranking risks by scores on agreed scales, not by money or days."),
           ("Probability and impact matrix", "A grid of probability against impact, coloured by score."),
           ("Risk score", "Probability × impact on the agreed scales."),
           ("Urgency (proximity)", "How soon a risk could happen, or a response must start."),
           ("Detectability", "How easily you'd notice the risk starting to happen."),
           ("Data quality", "How well the people scoring a risk know about it.")],
    code=dict(file="antwerp/10-re-score.md", note="Sanne, after Maarten (8 Feb) and Pieter (10 Feb), Wednesday 10 February 2027", plain=True, src="""
# ANTWERP · RE-SCORE OF 10 FEBRUARY 2027

ID    RISK                     WAS (30 Nov)    NOW          SCORED BY          SOON?      HOW WE'D NOTICE
R-07  permit not granted by    1 x 3 = 3       4 x 4 = 16   Maarten, Pieter,   lodge by   completeness letter;
      early July (rewritten)   green           RED          Sanne              end Mar    inquiry objections
R-09  neighbours object        2 x 2 = 4       merged into R-07 as a cause (the public inquiry)
R-03  builder late             3 x 3 = 9       2 x 3 = 6    Pieter, Sanne      Jun-Aug    weekly site report
R-02  hiring 40 on time        3 x 3 = 9       3 x 3 = 9    Joost, agency      Jul-Aug    applicants per week
R-08  courier contracts        3 x 3 = 9       2 x 3 = 6    Lena, Maarten      May        draft contract

NEW COLUMNS  scored by · how soon · how we'd notice
TO FEMKE     R-07 is over a threshold (a possible slip of 4-8 weeks > 2 weeks): responses 22 Feb
"""),
    tools="tools: the scales, a 5 × 5 grid, the people who know the place, and three extra columns.",
    dial=[("Light", "small work", ["High, medium, low.", "Sort the list.", "Talk about the top three."]),
          ("Standard", "Antwerp", ["P × I on 1–5 scales, on a grid.", "Who scored, how soon, how we'd notice.", "Re-scored on new information."]),
          ("Heavy", "large programmes", ["Calibrated scales per objective.", "Expert elicitation sessions.", "Risk data quality assessments."])],
    baseline="Each line compares <b>scores from the workshop room</b> to <b>scores from people who know the place, with who scored, urgency and detectability, re-scored on new facts</b>.",
    ratings=[(3, 4, "Attention goes to what could set the date."),
             (2, 3, "Known risks priced closer to reality."),
             (2, 5, "The worst risk is at the top of the list."),
             (2, 4, "Who scored each risk is visible."),
             (3, 4, "Femke hears the real top risk."),
             (3, 3, "Neutral."),
             (3, 4, "Re-scoring is normal, not an admission."),
             (3, 3, "Neutral."),
             (3, 3, "Minutes per risk.")],
    pitfalls=[("The wrong scorers", "Confident and uninformed.", "score with people who know."),
              ("Anonymous scores", "Nobody can challenge them.", "write who scored."),
              ("Scored once", "New facts ignored.", "re-score the day they arrive."),
              ("Twins scored apart", "Shared causes hidden.", "merge risks with one cause.")],
    use=["After identifying risks.", "Whenever someone better informed speaks.", "At each review for the top rows.", "Before sizing the reserve."],
    skip=["Never; on small work it's high, medium, low."],
    related=["<b>What Could Happen?</b> (previous note)", "<b>What Is It Worth?</b> (next note)", "<b>How Sure Are We?</b> (vol. 3)", "<b>Different Country, Different Rules</b> (this volume)"],
    quiz=[("What is a risk score?", "Probability × impact on the agreed scales."),
          ("Why was R-07 scored 1 in November?", "It was scored by people who knew Rotterdam, where a cold room needed no permit."),
          ("Why merge R-09 into R-07?", "The neighbours' objections were a cause of the permit delay, through the public inquiry."),
          ("A supplier tells you a risk you scored 2 happens on “about half” of their jobs. What do you do?", "Re-score it that day (probability 3–4), note who scored it, and check whether it crosses a threshold."),
          ("Two risks both score 12. One could strike next month, one in a year. Which first?", "The near one: urgency decides between equal scores.")],
    try_it="For your top five risks, write who scored each one. For any scored without someone who has done this work in this place, ask such a person this week and re-score.",
    remember="Ask the forecaster who knows <span class=\"hl\">this coast</span>. Then <span class=\"hl\">re-score</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, analysing risks.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.3 Perform Qualitative Risk Analysis.",
             "Daniel Kahneman, <i>Thinking, Fast and Slow</i> (2011): anchoring and the outside view."],
)

# ------------------------------------------------------------------ 11 What Is It Worth?
ev_problem = Doodle(760, 250, "Doodle of February 2027. Rotterdam's reserve was sized by listing five risks at about ten thousand euros and doubling it: twenty thousand. For Antwerp, Marco asks Sanne for a number he can defend to the board: how much contingency, and how much should Femke hold back for what nobody can name?",
                    "Rotterdam: a list, doubled. Marco wants a number he can defend, and a second one for the unknown.", exact=True)
ev_problem.box(20, 30, 330, 110, "Rotterdam: ≈ €10k × 2", "y", sub="a list, then a judgment", size=18, subsize=14)
ev_problem.box(410, 30, 330, 110, "Antwerp: how much?", "pink", sub="contingency + management reserve", size=18, subsize=14)
ev_problem.note(380, 186, "“a number I can defend to the board” (Marco)", "pen", size=18)
ev_problem.note(380, 222, "and nothing yet for what nobody can name", "red", size=17)

ev_analogy = Doodle(760, 250, "Doodle of an insurer pricing house insurance. Each risk is a chance times a cost: a burst pipe, five percent a year, eight thousand euros, so four hundred a year. Fire: one in a thousand, three hundred thousand, so three hundred. The premium is the sum, plus a margin for what the tables don't know.",
                    "An insurer's sum: chance × cost for each risk, added up, plus a margin for the unknown.", exact=True)
ev_analogy.row([("burst pipe", "5 % × €8,000 = €400", "blue"), ("fire", "0.1 % × €300k = €300", "pink"), ("premium", "the sum + a margin", "green")], y=40, h=96, size=17, subsize=13)
ev_analogy.note(380, 196, "expected cost = probability × impact, added up", "pen", size=19)

ev_how = Doodle(760, 470, "Antwerp's expected monetary value, Monday 1 March 2027, after the responses of 22 February. Threats: permit late, thirty percent of forty thousand, twelve thousand. Builder late, forty percent of ten thousand, four thousand. Hiring above rate, fifty percent of six thousand, three thousand. Cold room late, twenty percent of eight thousand, one thousand six hundred. Bancontact late, twenty percent of five thousand, one thousand. Translation rework, thirty percent of three thousand, nine hundred. Equipment prices, thirty percent of two thousand, six hundred. Threats total twenty-three point one thousand. Opportunities: shelving design, fifty percent of six thousand, minus three thousand; landlord insulation, twenty-five percent of four thousand, minus one thousand. Net nineteen point one thousand: contingency twenty thousand, held by Sanne. Management reserve fifteen thousand, held by Femke, for unknown risks.",
                "Threats €23.1k − opportunities €4k = €19.1k → contingency €20k. Femke holds €15k more for the unknown.", exact=True)
emv = [("permit late (R-07)", "30 %", "40", "12.0"), ("builder late", "40 %", "10", "4.0"), ("hiring above rate", "50 %", "6", "3.0"),
       ("cold room late", "20 %", "8", "1.6"), ("Bancontact late", "20 %", "5", "1.0"), ("translation rework", "30 %", "3", "0.9"),
       ("equipment prices", "30 %", "2", "0.6")]
for h, x in [("threat", 20), ("P", 330), ("impact €k", 410), ("EMV €k", 560)]:
    ev_how.head(x, 26, h, anchor="start", size=15)
for i, (t, p, im, e) in enumerate(emv):
    y = 36 + i * 32
    ev_how.box(8, y, 744, 28, None, "pink" if i == 0 else "paper", rx=4)
    for x, c in [(20, t), (330, p), (430, im), (580, e)]:
        ev_how.text(x, y + 20, c, anchor="start", size=14)
ev_how.box(8, 266, 744, 28, None, "y", rx=4)
ev_how.text(20, 286, "threats", anchor="start", size=14)
ev_how.text(580, 286, "23.1", anchor="start", size=14)
ev_how.box(8, 298, 744, 28, None, "green", rx=4)
ev_how.text(20, 318, "opportunities: shelving 50 % × 6 · insulation 25 % × 4", anchor="start", size=14)
ev_how.text(574, 318, "−4.0", anchor="start", size=14)
ev_how.box(8, 340, 360, 120, None, "blue")
ev_how.head(188, 372, "contingency €20k", size=18)
ev_how.text(188, 402, "net EMV €19.1k, rounded up", size=14)
ev_how.text(188, 428, "Sanne, drawn by logged change", size=14)
ev_how.box(392, 340, 360, 120, None, "paper")
ev_how.head(572, 372, "management reserve €15k", size=18)
ev_how.text(572, 402, "for what nobody can name", size=14)
ev_how.text(572, 428, "Femke, outside the baseline", size=14)

EMV = dict(
    slug="expected-monetary-value",
    kicker="a.k.a. “contingency vs management reserve”: expected monetary value and sizing the reserves",
    tldr="<b>Expected monetary value</b> (EMV) is probability × impact in money, for each risk: a 30 % chance of a €40k cost is worth <b>€12k</b> today. Add the threats, subtract the opportunities, and you have a defensible size for the <b>contingency reserve</b>: money for <b>known</b> risks, managed by the project manager under a rule. Above it the sponsor holds a <b>management reserve</b> for the <b>unknown</b> ones, outside the baseline. EMV doesn't predict what will happen (each risk either happens or doesn't); it sizes the pot for the whole list.",
    chips=[("Family", "what could happen"), ("Lives in", "a column of the register and two lines of the budget"), ("Pairs with", "the budget and its reserves, probability and impact, simulation")],
    pmbok=dict(covers="putting a money value on risks (expected monetary value, simple decision trees) and sizing the contingency and management reserves from them",
               domains=RISK + ["finance"], processes=["Analyze Risks"], principles=["Be an accountable leader"], focus=["planning"],
               older="6th: “Perform Quantitative Risk Analysis” (11.4), EMV and decision trees; contingency and management reserves in “Determine Budget” (7.3). 7th: the Uncertainty and Measurement domains."),
    problem_side="Larder, February 2027",
    problem="""  <p class="lead">Rotterdam's reserve was a list of five risks at about <b>€10k</b>, doubled by Marco to <b>€20k</b>. It worked: three draws took it to €0.4k. For Antwerp, Marco asks for more. <span class="hl-pink">“Give me a number I can defend to the board, and tell me how much Femke should hold back for the things nobody can name.”</span> The base estimate is <b>€430k</b>: builder €160k, cold room and fridges €84k, equipment and store IT €52k, people €68k, marketing in two languages €46k, Belgian set-up €20k.</p>
  <ul>
    <li>A doubled list can't be explained line by line.</li>
    <li>Known and unknown risks were in one pot.</li>
    <li>R-07 had just jumped to the top; the reserve had to reflect it.</li>
  </ul>""",
    problem_figs=[ev_problem],
    analogy_side="the insurer's sum",
    analogy="""  <p>An insurer pricing house insurance doesn't guess. A <b>burst pipe</b>: 5 % a year, €8,000 to fix, so <b>€400</b>. A <b>fire</b>: one in a thousand, €300,000, so <b>€300</b>. The premium is the sum of those, plus a <b>margin</b> for what the tables don't know. No single house costs the premium; across the whole book, it balances.</p>""",
    analogy_figs=[ev_analogy],
    map=[("Chance × cost per risk", "EMV per row: R-07 30 % × €40k = €12k"),
         ("The premium", "The contingency: net EMV €19.1k → €20k"),
         ("The margin for the unknown", "The management reserve: €15k, Femke"),
         ("No single house costs the premium", "Each risk happens or doesn't; the pot covers the list"),
         ("A no-claims discount", "Opportunities, subtracted: −€4k")],
    how_side="EMV per risk, net of opportunities; two reserves, two owners",
    how="""  <p>On <b>Monday 1 March</b>, after the responses of 22 February, Sanne puts a money impact and a probability on every risk that could cost money. The biggest is <b>R-07</b>: if the permit is late, a month of held staff, re-booked marketing, a re-booked cold-room installer and some crash work cost about <b>€40k</b> inside the project; after the responses its probability is <b>30 %</b>, so <b>€12k</b>. Seven threats add up to <b>€23.1k</b>; two opportunities (the shelving design, the landlord's insulation) take off <b>€4k</b>: net <b>€19.1k</b>. The <b>contingency</b> is set at <b>€20k</b>, held by Sanne and drawn only through a logged change, as in Rotterdam. Above it, Femke holds a <b>management reserve of €15k</b> for what nobody has named: a first country is new to everyone. The budget becomes <b>€430k + €20k = €450k</b>, and <b>€465k</b> with the management reserve. Marco takes it to the board with one line per risk. He adds one note of his own: the €40k is only what lands in the project; the five weeks of a slip would cost far more outside it.</p>""",
    how_figs=[ev_how],
    steps=[("List the risks that cost money", "Threats and opportunities."),
           ("Give each an impact in money", "What it would cost if it happened."),
           ("Use the probability after responses", "The residual risk."),
           ("Multiply and add; subtract opportunities", "Net EMV."),
           ("Size the contingency from it", "Owned by the project manager, by a rule."),
           ("Add a management reserve for the unknown", "Owned by the sponsor.")],
    vocab=[("Expected monetary value (EMV)", "Probability × impact in money; negative for threats, positive for opportunities, by convention."),
           ("Contingency reserve", "Money for known risks, inside the project, under the project manager."),
           ("Management reserve", "Money for unknown risks, outside the baseline, under the sponsor."),
           ("Known unknowns", "Risks you've identified but can't be sure will happen."),
           ("Unknown unknowns", "Risks nobody has identified."),
           ("Decision tree", "A drawing of choices and chances, with EMV on each branch, to compare options.")],
    code=dict(file="antwerp/11-reserves.md", note="Sanne and Marco, Monday 1 March 2027", plain=True, src="""
# ANTWERP · BUDGET AND RESERVES                                         1 Mar 2027 (€k)

BASE ESTIMATE            builder 160 · cold room + fridges 84 · equipment + IT 52 ·
                         people 68 (40 x 1.7) · marketing fr+nl 46 · Belgian set-up 20   430

EXPECTED MONETARY VALUE (after the responses of 22 Feb)
  R-07 permit late              30 % x 40   = 12.0
  R-03 builder late             40 % x 10   =  4.0
  R-02 hiring above rate        50 % x  6   =  3.0
  R-01 cold room late           20 % x  8   =  1.6
  R-04 Bancontact late          20 % x  5   =  1.0
  R-06 translation rework       30 % x  3   =  0.9
  R-11 equipment prices         30 % x  2   =  0.6     threats        23.1
  O-01 shelving design reused   50 % x  6   = -3.0
  O-02 landlord pays insulation 25 % x  4   = -1.0     opportunities  -4.0
                                                       net EMV        19.1
CONTINGENCY (Sanne; by logged change)                                              20
PROJECT BUDGET                                                                    450
MANAGEMENT RESERVE (Femke; unknown risks; outside the baseline)                    15
AUTHORISED                                                                        465
OUTSIDE THE PROJECT (Marco)  a week late ≈ €15k contribution + ≈ €2k rent (operations)
"""),
    tools="tools: the register, a money impact per risk, a calculator, and two budget lines with two owners.",
    dial=[("Light", "small work", ["A percentage on top.", "Say what it's for.", "No EMV."]),
          ("Standard", "Antwerp", ["EMV per risk, net of opportunities.", "Contingency from it; management reserve for the unknown.", "Two owners, two rules."]),
          ("Heavy", "large capital projects", ["Contingency per risk with a confidence level.", "Monte Carlo on cost.", "Reserves released by stage."])],
    baseline="Each line compares <b>Rotterdam's list, doubled</b> to <b>EMV per risk, net of opportunities, and two reserves with two owners</b>.",
    ratings=[(3, 4, "Reserves sized to the risks of this launch."),
             (2, 4, "A defensible number, line by line."),
             (3, 4, "Money is there for the known risks."),
             (2, 5, "Each euro of reserve points to a risk."),
             (2, 5, "Marco took one line per risk to the board."),
             (3, 3, "Neutral."),
             (3, 4, "A second pot for what nobody named."),
             (3, 3, "Neutral."),
             (3, 3, "An afternoon with the register.")],
    pitfalls=[("EMV as a forecast", "Each risk happens or doesn't.", "use it to size the pot, not to predict one risk."),
              ("One pot for everything", "Unknowns eat the known risks' money.", "contingency and management reserve, two owners."),
              ("Before-response probabilities", "Pays twice for one risk.", "use residual probability."),
              ("Only the project's money", "The real cost of a slip is hidden.", "note the cost outside it too.")],
    use=["When sizing the budget's reserves.", "When comparing responses or options.", "When the sponsor asks “how much could this cost us?”", "After a big re-score."],
    skip=["Small work with no risk large enough to price."],
    related=["<b>How Much Do We Set Aside?</b> (vol. 4)", "<b>How Likely, and How Bad?</b> (previous note)", "<b>What If We Ran It a Thousand Times?</b> (next note)", "<b>Total Cost of Ownership</b> (Ana, vol. 5)"],
    quiz=[("What's the EMV of a 30 % chance of a €40k cost?", "€12k."),
          ("Contingency or management reserve: a risk nobody had thought of?", "Management reserve, the sponsor's."),
          ("Why subtract opportunities?", "They're expected savings; net EMV sizes the pot for the whole list."),
          ("A lead wants to use the contingency for an unplanned launch party. What does Sanne say?", "The contingency is for named risks, drawn by change; a party is a new wish, for the steering group or the operations budget."),
          ("Femke asks: if R-07 happens, will €20k cover it? Answer honestly.", "No, R-07 alone would cost ~€40k; the contingency covers the expected cost of the list, and the management reserve is there for the rest.")],
    try_it="Put a money impact and a probability on your top five risks. Multiply and add. Is your reserve that size? Who holds the money for what nobody has named?",
    remember="Chance × cost, <span class=\"hl\">added up</span>. One pot for the known, <span class=\"hl\">one</span> for the rest.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, analysing risks; Finance domain, reserves.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.4 Perform Quantitative Risk Analysis; 7.3 Determine Budget.",
             "David Vose, <i>Risk Analysis: A Quantitative Guide</i> (3rd ed., 2008)."],
)

# ------------------------------------------------------------------ 12 What If We Ran It a Thousand Times?
mc_problem = Doodle(760, 250, "Doodle of March 2027. Femke asks the question every sponsor asks: will Antwerp open on Monday 13 September? Sanne has a plan that says yes, three-point estimates for the fit-out, a permit procedure whose steps all have ranges, and a thirty percent chance of objections. A single date hides all of that.",
                    "“Will it open on 13 September?” A single date hides every range underneath it.", exact=True)
mc_problem.box(20, 30, 330, 110, "Femke: “13 September?”", "y", sub="one date, yes or no", size=18, subsize=14)
mc_problem.box(410, 30, 330, 110, "the plan underneath", "pink", sub="ranges, a 30 % objection chance", size=18, subsize=14)
mc_problem.note(380, 186, "the honest answer is a chance, not a yes", "red", size=19)
mc_problem.note(380, 222, "ranges added by hand don't give the odds of the whole", "pen", size=16)

mc_analogy = Doodle(760, 250, "Doodle of a family deciding when to leave for the airport. They don't ask how long the drive takes. They imagine it many times: some days the motorway is clear, some days there's a jam at the bridge, one day in ten there's an accident. Out of a hundred imagined trips, ninety arrive within seventy minutes. They leave seventy-five minutes before check-in closes.",
                    "Imagine the drive a hundred times: 90 of them take under 70 minutes. Leave 75 minutes ahead.", exact=True)
for i, h in enumerate([6, 14, 22, 18, 12, 8, 5, 3, 2, 1]):
    mc_analogy.box(120 + i * 52, 160 - h * 5, 44, h * 5, None, "blue" if i < 7 else "pink", rx=3)
mc_analogy.line("M110 162 H650", thin=True)
for i_, lab in [(0, "40 min"), (6, "70 min"), (9, "90 min")]:
    mc_analogy.note(142 + i_ * 52, 186, lab, "pen", size=14)
mc_analogy.note(380, 232, "90 of 100 trips arrive in time if they leave 75 minutes ahead", "pen", size=16)

mc_how = Doodle(760, 470, "The opening date as a range: Sanne's simulation of 1 March 2027, a thousand runs with seed 2027. A histogram of the opening Monday. 30 August, 32 runs; 6 September, 211; 13 September, 271; 20 September, 216; 27 September, 108; 4 October, 60; 11 October, 44; 18 October, 15; 25 October, 21; November, 22. Marked: P50, 13 September; P80, 27 September; P90, 11 October. Fifty-one percent of runs open by 13 September. In the 162 runs later than 27 September, the permit set the date in 157.",
                "1,000 runs of the plan. 13 September is a coin toss (51 %); 80 % open by 27 September; the late tail is the permit's.", exact=True)
bins = [("30 Aug", 32), ("6 Sep", 211), ("13 Sep", 271), ("20 Sep", 216), ("27 Sep", 108), ("4 Oct", 60), ("11 Oct", 44), ("18 Oct", 15), ("25 Oct", 21), ("Nov", 22)]
base, bw = 330, 66
for i, (lab, n) in enumerate(bins):
    h = n * 1.0
    x = 40 + i * (bw + 4)
    fill = "green" if i <= 2 else ("y" if i <= 4 else "pink")
    mc_how.box(x, base - h, bw, h, None, fill, rx=3)
    mc_how.text(x + bw / 2, base - h - 8, str(n), size=13)
    mc_how.text(x + bw / 2, base + 22, lab, size=13)
mc_how.line(f"M30 {base} H740", thin=True)
for x, lab in [(40 + 2 * 70 + bw + 2, "P50"), (40 + 4 * 70 + bw + 2, "P80"), (40 + 6 * 70 + bw + 2, "P90")]:
    mc_how.line(f"M{x} 40 V{base}", color="red", dash=True)
    mc_how.note(x, 32, lab, "red", size=15)
mc_how.box(14, 384, 360, 76, "13 Sep: 51 %", "y", sub="P50 · a coin toss", size=18, subsize=13)
mc_how.box(386, 384, 360, 76, "late tail: the permit", "pink", sub="157 of 162 runs after 27 Sep", size=18, subsize=13)

mc_deep1 = Doodle(760, 340, "The model behind the simulation, as boxes and arrows, in weeks from 1 March 2027. Permit chain: drawings and application, three to eight weeks, most likely four; completeness check, two to five, likely three; public inquiry, thirty days; decision, three to twelve, likely five; with a thirty percent chance of objections adding two to eight weeks. Fit-out chain: keys on 1 June, then the builder, nine to thirteen weeks, likely ten. The cold room is installed in two weeks once both the permit is granted and the building shell is ready. Then food-safety visit, stocking and rehearsal, three to five weeks. Opening on the next Monday.",
                  "Two chains meet at the cold room. Every box is a range; one is a 30 % coin.", exact=True)
mc_deep1.row([("drawings + lodge", "3 / 4 / 8 wks", "y"), ("completeness", "2 / 3 / 5", "y"), ("inquiry", "30 days", "paper"), ("decision", "3 / 5 / 12", "y")], y=20, h=72, size=15, subsize=13, gap=34, arrows=True)
mc_deep1.box(470, 104, 276, 52, "30 %: objections +2 / 4 / 8", "pink", size=14)
mc_deep1.row([("keys 1 June", "week 13", "paper"), ("builder", "9 / 10 / 13 wks", "blue")], x=14, y=176, h=72, w=200, size=15, subsize=13, gap=34, arrows=True)
mc_deep1.box(500, 176, 246, 72, "cold room", "green", sub="2 wks after permit AND shell", size=15, subsize=12)
mc_deep1.arrow(667, 92, 667, 102)
mc_deep1.arrow(620, 156, 620, 174)
mc_deep1.arrow(450, 212, 496, 212)
mc_deep1.box(260, 268, 486, 60, "visit, stock, rehearse 3 / 3.5 / 5 → next Monday", "y", size=15)
mc_deep1.arrow(620, 250, 560, 266)
mc_deep1.note(130, 300, "min / likely / max", "pen", size=15)

MONTE = dict(
    slug="monte-carlo",
    kicker="a.k.a. “simulation in plain words”: quantitative risk analysis with Monte Carlo",
    tldr="A <b>Monte Carlo simulation</b> runs the plan <b>a thousand times</b>. Each run draws every uncertain duration from its range (best, likely, worst) and flips every risk's coin; the computer works out the end date each time. Sorted, the thousand dates become <b>odds</b>: the date you have a 50 % chance of hitting (<b>P50</b>), the date you'd hit four times in five (<b>P80</b>), and which uncertainty drives the late tail. It turns “will we make 13 September?” into “51 % yes, 80 % by 27 September, and the permit decides the rest”. It needs ranges you trust, and a record of the model and its random seed.",
    chips=[("Family", "what could happen"), ("Lives in", "a short script, its inputs and its seed, and one chart in the status"), ("Pairs with", "three-point estimates, the critical path, expected monetary value")],
    pmbok=dict(covers="quantitative risk analysis: simulating the combined effect of uncertainties on dates and costs, reading P50 and P80, and finding what drives the result",
               domains=RISK + ["schedule"], processes=["Analyze Risks"], principles=["Adopt a holistic view"], focus=["planning", "monitoring and controlling"],
               older="6th: “Perform Quantitative Risk Analysis” (11.4), simulation, sensitivity analysis (tornado diagrams). 7th: the Uncertainty and Measurement domains."),
    problem_side="Larder, 1 March 2027",
    problem="""  <p class="lead">Femke asks what every sponsor asks: <b>will Antwerp open on Monday 13 September?</b> The plan says yes. Underneath it are ranges: Pieter's fit-out of 9 to 13 weeks, a permit procedure where every step has a best and a worst case, and a <b>30 % chance</b> that neighbours object in the public inquiry. <span class="hl-pink">Adding best cases gives August; adding worst cases gives November; neither is an answer.</span> In Vol. 3 Sanne added three-point estimates for one chain. Antwerp has two chains that meet at the cold room, and a coin in the middle of one of them.</p>
  <ul>
    <li>A single date hides every range underneath it.</li>
    <li>Two chains meeting make the end later than either alone.</li>
    <li>A yes-or-no risk can't be added like a duration.</li>
  </ul>""",
    problem_figs=[mc_problem],
    analogy_side="leaving for the airport",
    analogy="""  <p>A family doesn't ask “how long is the drive to the airport?” They imagine it many times. Most days the motorway is clear; some days there's a jam at the bridge; one day in ten, an accident. Out of a hundred imagined trips, <b>ninety arrive within seventy minutes</b>. They leave seventy-five minutes before check-in closes, and know they're taking a one-in-ten chance of a sprint through the terminal.</p>""",
    analogy_figs=[mc_analogy],
    map=[("Imagining the drive many times", "1,000 runs of the plan"),
         ("Clear road, a jam, an accident", "Each duration drawn from its range; objections 30 % of the time"),
         ("90 of 100 within 70 minutes", "P80: open by 27 September"),
         ("Leaving 75 minutes ahead", "Choosing a date with known odds"),
         ("The bridge that causes the jams", "The permit: it drives the late tail")],
    how_side="a thousand runs, a histogram, P50, P80, and what drives the tail",
    how="""  <p>Sanne writes the model on one page (see “going deeper”) and a twenty-line script with Eli: two chains, every duration a <b>triangular range</b> (best, most likely, worst, from Pieter, Hilde and Maarten), the objection as a 30 % coin, and the date the cold room can start as the later of the two chains. She runs it <b>1,000 times</b> with a recorded <b>seed (2027)</b>, so anyone can re-run it and get the same chart. The answer for the steering group of <b>Friday 5 March</b>: <b>13 September is a coin toss</b>: 51 % of runs open by then (P50). <b>80 % open by 27 September</b> (P80), 90 % by 11 October. And the shape matters most: of the 162 runs later than 27 September, the <b>permit</b> set the date in <b>157</b>; the fit-out drives the on-time runs and almost none of the late ones. Femke's two decisions follow from that. Keep 13 September as the planning date, and tell investors “September or early October”. And don't pay for earlier keys: a month's head start on the fit-out barely moves the late tail. The money goes to the permit's responses instead.</p>""",
    how_figs=[mc_how],
    steps=[("Draw the model as chains of activities", "And where they meet."),
           ("Give each uncertain step a range", "Best, most likely, worst, from people who know."),
           ("Add yes-or-no risks as coins", "With their probability and effect."),
           ("Run it a thousand times; record the seed", "So it can be repeated."),
           ("Read P50, P80 and the shape", "Not just the average."),
           ("Find what drives the late runs", "And spend responses there.")],
    vocab=[("Monte Carlo simulation", "Running a model many times with random draws from each range to see the spread of results."),
           ("Triangular distribution", "A range given by best, most likely and worst values."),
           ("P50 / P80", "The date (or cost) reached in 50 % / 80 % of runs."),
           ("Histogram", "A bar chart of how many runs ended in each week."),
           ("Sensitivity (driver) analysis", "Which uncertainty most changes the result; drawn as a tornado diagram."),
           ("Seed", "The starting number of the random draws; the same seed gives the same runs.")],
    code=dict(file="antwerp/12-opening-range.md", note="Sanne and Eli, Monday 1 March 2027 (1,000 runs, seed 2027)", plain=True, src="""
# ANTWERP · OPENING DATE AS A RANGE                     1 Mar 2027 · 1,000 runs · seed 2027

MODEL (weeks from Mon 1 Mar; min / likely / max)
  permit   drawings + lodge 3/4/8 · completeness 2/3/5 · inquiry 30 days · decision 3/5/12
           objections: 30 % chance, +2/4/8
  fit-out  keys Tue 1 Jun (week 13) · builder 9/10/13 · shell ready after week 6
  then     cold room 2 weeks after permit AND shell · visit + stock + rehearse 3/3.5/5
           → opening on the next Monday

RESULT   P10  6 Sep    P50 13 Sep    P80 27 Sep    P90 11 Oct
         open by 13 Sep: 51 % of runs · by 18 Oct: 96 %
DRIVER   runs later than 27 Sep: 162 · the permit set the date in 157 (97 %)
DECIDED  (steering group, Fri 5 Mar) planning date stays 13 Sep · investors told
         "September or early October" · no earlier keys (doesn't move the tail) ·
         responses to R-07 funded · re-run monthly with actual dates
"""),
    tools="tools: three-point ranges from the people who know, a short script, a fixed seed, and one histogram.",
    deep_dive=dict(
        side="what a simulation does, where the ranges come from, reading the output, and its limits",
        intro="“Monte Carlo” sounds like casinos and statistics. The idea is simpler than a critical path: imagine the project many times, each time with different luck, and count. This chapter shows the model Sanne ran, where good ranges come from, how to read what comes out, and what a simulation can't tell you, including whether 18 October was in the chart.",
        parts=[
            ("What it does, in plain words", """  <p>Each <b>run</b> is one possible version of the project. For every uncertain step the computer picks a duration from its range: usually near the most likely value, sometimes near the best or worst. For every yes-or-no risk it flips a weighted coin. Then it works out the end date the way you would on a network diagram: chains add up, and where two chains meet, the later one wins.</p>
  <p>Do that a thousand times and you have a thousand end dates. Sort them. The 500th is the <b>P50</b>; the 800th is the <b>P80</b>. Nothing in it is cleverer than the network diagram from Vol. 3; it's the network diagram, rolled a thousand times.</p>""", [mc_deep1]),
            ("Where the ranges come from", """  <p>A simulation is only as good as its ranges, and good ranges come from people who've done the work in this place: Pieter for the fit-out, Hilde and Maarten for the permit. Ask for three numbers, as in Vol. 3's three-point estimates: the best case, the most likely, and a <b>worst case they've actually seen</b>. People's worst cases are usually too kind; asking “what's the longest you've seen this take?” helps.</p>
  <p>Two cautions. Where two steps go wrong for the same reason (a slow city office slows both the completeness check and the decision), a simple model treats them as independent and the tail comes out too thin. And a coin like “objections, 30 %” is a judgment; write down whose.</p>""", []),
            ("Reading the output", """  <p>Three things matter, in this order:</p>
  <ul>
    <li><b>The odds of the date you've promised.</b> 13 September came out at 51 %. A planning date with even odds is fine if everyone knows it's even.</li>
    <li><b>P80 and P90</b>: the dates you'd choose if a slip is expensive. 27 September and 11 October.</li>
    <li><b>The shape and its driver.</b> Antwerp's histogram has a long right tail, and the late runs were nearly all the permit's. That is the most useful output: it says where a euro of response buys the most.</li>
  </ul>
  <p>Re-run monthly with what has actually happened. On 9 April, with the drawings in and the application booked for 19 April, the P50 moved to <b>20 September</b> and the P80 to <b>11 October</b>. With the objections in, in July, the model gave P50 11 October and P80 25 October, before the city's case officer said the same thing in words.</p>""", []),
            ("Limits, and was 18 October in the chart?", """  <p>A simulation can only shake the uncertainties you put in. It knows nothing about risks you haven't named (that's what the management reserve is for), and it believes your ranges. It's also not a promise: an 80 % date is missed one time in five.</p>
  <p>Antwerp opened on <b>18 October</b>. In the chart of 1 March, 96 % of runs had opened by then; 18 October was in the far tail, about one run in twenty-five. Everything that happened was inside the model's ranges: the drawings took seven weeks (range 3–8), the objections came (the 30 % coin), the decision took its time. Nothing in the model was wrong. What went wrong was that the draws all came out bad, and a response that would have narrowed the drawings' range had no owner (two notes on).</p>""", []),
        ]),
    dial=[("Light", "small work", ["Best, likely, worst for the whole.", "Say a range, not a date.", "No simulation."]),
          ("Standard", "Antwerp", ["A short model, ranges from experts, 1,000 runs, a seed.", "P50, P80 and the driver.", "Re-run monthly."]),
          ("Heavy", "large programmes", ["Integrated cost and schedule risk analysis.", "Correlated ranges, risk drivers.", "Specialist tools and reviewers."])],
    baseline="Each line compares <b>one planned date</b> to <b>a thousand simulated runs with P50, P80 and the driver of the late tail</b>.",
    ratings=[(3, 4, "Money for responses goes where it moves the date."),
             (2, 4, "Dates come with odds."),
             (2, 5, "The driver of the late tail is found."),
             (2, 5, "A chart anyone can read; a seed anyone can re-run."),
             (3, 4, "Investors hear a range they can trust."),
             (3, 3, "Neutral."),
             (3, 4, "Re-runs show the effect of new facts."),
             (3, 3, "Neutral."),
             (3, 2, "A model, a script, monthly re-runs.")],
    pitfalls=[("Ranges from the wrong people", "A confident, wrong chart.", "ask those who've done it here."),
              ("Reading only the average", "Misses the tail.", "read P80, P90 and the shape."),
              ("No seed, no record", "Nobody can check it.", "record the model and the seed."),
              ("Treating P80 as certain", "One time in five it's missed.", "say the odds aloud.")],
    use=["When the date or cost matters and many things are uncertain.", "When chains meet or yes-or-no risks sit on the path.", "When choosing where to spend on responses.", "When a sponsor needs a date with odds."],
    skip=["Small work, or a single chain where a three-point estimate is enough."],
    related=["<b>How Sure Are We?</b> (vol. 3)", "<b>What Decides the Finish Date?</b> (vol. 3)", "<b>What Is It Worth?</b> (previous note)", "<b>Back-of-the-Envelope Estimation</b> (Ana, vol. 5)"],
    quiz=[("What is a P80 date?", "The date reached in 80 % of the simulated runs."),
          ("What were Antwerp's P50 and P80 on 1 March?", "13 September (51 % by then) and 27 September."),
          ("Why didn't Femke pay for earlier keys?", "The late runs were driven by the permit, not the fit-out; earlier keys hardly moved the tail."),
          ("A lead asks why the chart changed when you re-ran it. What's your answer?", "New facts went in (actual dates, a changed range); with the same inputs and seed it would be identical."),
          ("Femke asks whether 18 October was “in the model”. What do you say?", "Yes, in the far tail: about 4 % of runs opened later than that; every step's range held it.")],
    try_it="Take a chain from your plan with three-point estimates. In a spreadsheet, draw each from its range 1,000 times, add them up, and sort. Compare the P80 with the date you've promised.",
    remember="Imagine the drive a <span class=\"hl\">thousand</span> times. Find the <span class=\"hl\">bridge</span> that causes the jams.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Risk domain, analysing risks; models and methods: simulation.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 11.4 Perform Quantitative Risk Analysis.",
             "Project Management Institute, <i>Practice Standard for Project Risk Management</i> (2009).",
             "Sam L. Savage, <i>The Flaw of Averages</i> (2009)."],
)

NOTES = [APPROACH, REGISTER_R, QUAL, EMV, MONTE]
