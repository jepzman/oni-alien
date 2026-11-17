# Series 2 · Book 3 · The Project Manager's Notebook · Vol. 5 · Who's involved (the Stakeholders domain, part 1)
# Narrator: Sanne. Running case study: Larder (facts in docs/larder-casebook.md, "Book 3, Vol. 5").
#
# THE ANTWERP LAUNCH, the worked example of this volume (checked by script: weekdays, sums, the simulation).
#   Project starts Mon 5 Oct 2026; sponsor Femke; steering group Femke, Marco, Joost, Priya, Lena, first Friday monthly.
#   Store: a former tyre depot in Berchem, 640 m²; lease signed Tue 15 Dec 2026, keys Tue 1 Jun 2027.
#   Planned opening Mon 13 Sep 2027 (a planning date, never announced as a promise); actual Mon 18 Oct 2027.
#   New people: Maarten (Belgian lawyer, Antwerp, works with Lena from Oct 2026) · Pieter (site manager, the Belgian builder)
#     · Hilde (permit agent, from Mon 8 Mar 2027) · Koen (sales manager, a produce wholesaler at the early market)
#     · Inès (Antwerp store manager, starts Mon 7 Jun 2027).
#   Budget (k€, excl. VAT, 1 Mar 2027): builder 160 · cold room + fridges 84 · equipment + store IT 52 · people 68 (40 × 1.7)
#     · marketing (fr + nl) 46 · Belgian set-up 20 (lawyer 8, permit agent 6, translation 4, registrations 2) = 430
#     + contingency 20 (from net EMV 19.1) = 450 (Sanne) + management reserve 15 (Femke) = 465 authorised.
#   EMV 1 Mar 2027 (after responses): permit late 30 % × 40 = 12.0 · builder late 40 % × 10 = 4.0 · hiring above rate
#     50 % × 6 = 3.0 · cold room late 20 % × 8 = 1.6 · Bancontact late 20 % × 5 = 1.0 · translation rework 30 % × 3 = 0.9
#     · equipment prices 30 % × 2 = 0.6 → threats 23.1; opportunities: Rotterdam shelving design 50 % × 6 = 3.0 ·
#     landlord pays insulation 25 % × 4 = 1.0 → 4.0; net 19.1 → contingency €20k.
#   Simulation (1 Mar 2027, 1,000 runs, seed 2027): P10 6 Sep · P50 13 Sep · P80 27 Sep · P90 11 Oct; P(≤ 13 Sep) 51 %;
#     18 Oct ≈ P95. In the runs later than 27 Sep the permit set the date 157 times of 162 (97 %).
#   The permit (risk R-07): register 30 Nov 2026 P1 × I3 = 3, no owner, "the builder handles permits" (Sanne's mistake)
#     → Maarten 8 Feb + Pieter 10 Feb 2027: re-scored P4 × I4 = 16 → responses 22 Feb (agent, pre-application meeting
#     Thu 11 Mar, drawings by Mon 15 Mar, lodge by Fri 26 Mar) → residual P3 × I4 = 12 → drawings action had no Larder owner:
#     drawings 9 Apr, lodged Mon 19 Apr → complete 10 May → public inquiry Mon 24 May–Tue 22 Jun: 14 objections
#     (lorries before 07:00, condenser noise) → Thu 15 Jul the city's case officer: no decision before September → issue I-12
#     → extra steering group Fri 23 Jul: deliveries from 07:00 only, acoustic screen, opening Mon 18 Oct
#     → permit granted Mon 6 Sep → cold room 7–17 Sep → food-safety visit Wed 29 Sep → stocking 4–15 Oct → open 18 Oct.
#   Cost of the slip: in the project €27k (staff start held 11, marketing re-booked 9, installer re-booked 4, screen 3):
#     contingency 14 → 0 (earlier draws: hiring 4, translation rework 2), management reserve 15 → 2. Outside it: rent
#     ≈ €10k (operations) and ≈ €75k of contribution (5 weeks × €15k, Marco). Forecast at opening €457k of €465k.

STK = ["stakeholders"]

# ------------------------------------------------------------------ 01 Who Cares About This?
sr_problem = Doodle(760, 260, "Doodle of 2 November 2026. Sanne's first stakeholder list for Antwerp is a copy of Rotterdam's: fourteen names, all inside Larder except the landlord and the builder. Lena reads it and asks two questions: where is the city, and where is the food-safety agency?",
                    "Rotterdam's list, copied: fourteen names. Lena: “Where's the city? Where's the food agency?”", exact=True)
sr_problem.box(20, 24, 330, 150, None, "paper")
sr_problem.head(185, 58, "Antwerp list, v0", size=20)
for i, t in enumerate(["Femke, Marco, Joost, Priya …", "12 people inside Larder", "+ the landlord, the builder"]):
    sr_problem.text(185, 94 + i * 28, t, size=16)
sr_problem.box(410, 24, 330, 150, None, "pink")
sr_problem.head(575, 58, "Lena asks", size=20)
for i, t in enumerate(["“Where's the city?”", "“Where's the food agency?”", "“Where are the neighbours?”"]):
    sr_problem.text(575, 94 + i * 28, t, size=16)
sr_problem.note(380, 214, "a list copied from a city in another country", "red", size=19)
sr_problem.note(380, 244, "it names who we know, not who the project touches", "pen", size=16)

sr_analogy = Doodle(760, 250, "Doodle of a family moving house to another town. The obvious list: the family, the removal firm, the estate agent. The real list adds the new school, the doctor, the town hall for registration, the neighbours who share the drive, and the old landlord who holds the deposit.",
                    "Moving house: the obvious list, and the people who can make moving day go wrong.", exact=True)
moving = [("family", "y"), ("movers", "y"), ("agent", "y"), ("new school", "blue"), ("town hall", "pink"), ("neighbours", "green")]
for i, (t, f) in enumerate(moving):
    sr_analogy.box(14 + i * 124, 50, 112, 70, t, f, size=16)
sr_analogy.note(190, 156, "the obvious three", "pen", size=17)
sr_analogy.note(570, 156, "the three who can spoil moving day", "red", size=17)
sr_analogy.note(380, 210, "the second list is longer, and found by asking", "pen", size=18)

sr_how = Doodle(760, 468, "Sanne's stakeholder register for Antwerp, 2 November 2026, drawn as four rings around the project. Inside Larder: twelve, from Femke to the store manager still to be hired. Partners and suppliers: eight, among them the landlord, the Belgian builder, the cooling supplier, a produce wholesaler, the courier agency and the payment provider for Bancontact. Authorities: five: the city's permit office, the food-safety agency FAVV-AFSCA, the fire service, the VAT office and the city's mobility department. Community: six: the forty-six households in the street, the school on the corner, local shops, 3,100 waitlist customers, a rival delivery service and the local press. Thirty-one in all, found from four sources: the charter, Rotterdam's lessons, a walk round the street and an hour with Lena and Maarten.",
                "Thirty-one stakeholders in four rings, found from four sources. v0 had fourteen.", exact=True)
sr_how.raw('<ellipse class="d f-paper" cx="200" cy="200" rx="190" ry="186"/>')
sr_how.raw('<ellipse class="d f-y" cx="200" cy="214" rx="150" ry="146"/>')
sr_how.raw('<ellipse class="d f-blue" cx="200" cy="228" rx="110" ry="106"/>')
sr_how.raw('<ellipse class="d f-green" cx="200" cy="244" rx="64" ry="54"/>')
sr_how.head(200, 50, "community · 6", size=15)
sr_how.head(200, 94, "authorities · 5", size=15)
sr_how.head(200, 152, "partners · 8", size=15)
sr_how.head(200, 240, "Larder", size=16)
sr_how.head(200, 262, "12", size=16)
groups = [("Larder · 12", "Femke, Marco, Joost … the store manager", "green"),
          ("partners · 8", "landlord · builder · cooling · wholesaler · couriers · payments · staffing · insurer", "blue"),
          ("authorities · 5", "permit office · FAVV-AFSCA · fire · VAT · mobility", "y"),
          ("community · 6", "46 households · school · shops · 3,100 waitlist · rival · press", "paper")]
for i, (h, t, f) in enumerate(groups):
    y = 14 + i * 76
    sr_how.box(408, y, 340, 66, None, f, rx=6)
    sr_how.head(420, y + 24, h, anchor="start", size=15)
    words, line, out = t.split(" · "), "", []
    for w in words:
        if len(line) + len(w) + 3 > 44 and line:
            out.append(line); line = w
        else:
            line = (line + " · " + w) if line else w
    out.append(line)
    for k, l in enumerate(out):
        sr_how.text(420, y + 44 + k * 16, l, anchor="start", size=12)
sr_how.note(578, 336, "found from four sources:", "pen", size=14)
sr_how.row([("the charter", "who it names", "paper"), ("Rotterdam lessons", "neighbours told late", "paper"), ("a walk round", "Sat 31 Oct", "paper"), ("Lena + Maarten", "Belgian rules", "paper")], y=394, h=60, size=14, subsize=11)

REGISTER = dict(
    slug="stakeholder-register",
    kicker="a.k.a. identifying stakeholders: the stakeholder register",
    tldr="A <b>stakeholder</b> is anyone the project affects, or who can affect it: inside the organisation and outside, friendly or not, with a contract or without one. <b>Identify</b> them early, from several sources (the charter, lessons from the last project, a walk round the site, the experts on local rules), and write them in a <b>register</b>: who they are, what they need from the project, how much they can help or stop it, what they think of it now, who talks to them, in which language. The people you forget are the ones who surprise you.",
    chips=[("Family", "who's involved"), ("Lives in", "one table, reviewed monthly"), ("Pairs with", "the stakeholder map, power and interest, the communications plan")],
    pmbok=dict(covers="finding everyone the project affects or who can affect it, and recording what they need, their influence and their attitude",
               domains=STK, processes=["Identify Stakeholders"], principles=["Adopt a holistic view"], focus=["initiating", "planning"],
               older="6th: “Identify Stakeholders” (13.1), the stakeholder register. 7th: the Stakeholders domain."),
    problem_side="Larder, 2 November 2026",
    problem="""  <p class="lead">Antwerp is Larder's first city abroad, planned for September 2027. Femke is the sponsor; Sanne started the project on 5 October. Her first stakeholder list is a <b>copy of Rotterdam's</b>: fourteen names, twelve of them inside Larder, plus the landlord and the builder. Lena reads it and asks: <span class="hl-pink">“Where's the city? Where's the food-safety agency? Where are the neighbours?”</span> Rotterdam didn't contact its neighbours until 2 March, eight weeks before opening. In another country, with other rules, the list Sanne knew would be shorter than the list that mattered.</p>
  <ul>
    <li>The list names the people Sanne knows, not the people the project touches.</li>
    <li>Authorities and the street are missing.</li>
    <li>Nothing says what each one needs or can do.</li>
  </ul>""",
    problem_figs=[sr_problem],
    meanwhile=[("architect-1", "stakeholder-map", "Ana's stakeholder map (October 2025) lists who shapes the architecture and what each one cares about, so no concern arrives late.",
                "Sanne's Antwerp register does the same for a launch abroad, and adds the people outside Larder: the city, the food-safety agency, the street.")],
    analogy_side="moving house",
    analogy="""  <p>A family moving to another town makes a list: the family, the <b>removal firm</b>, the <b>estate agent</b>. The list that decides whether moving day goes well is longer: the <b>new school</b> (a place for the children), the <b>town hall</b> (registration, parking permit for the van), the <b>neighbours</b> who share the drive, the old landlord holding the deposit. Nobody on the second list is hostile. They just weren't asked.</p>""",
    analogy_figs=[sr_analogy],
    map=[("The family", "Larder's own people: twelve"),
         ("The removal firm, the agent", "Partners and suppliers: eight"),
         ("The town hall", "Authorities: the permit office, the food-safety agency, the fire service"),
         ("The neighbours on the drive", "Forty-six households, the school on the corner"),
         ("Asking around before you move", "Four sources, not one copied list")],
    how_side="four sources, four rings, one register",
    how="""  <p>Sanne builds the register from <b>four sources</b> in a week. The <b>charter</b> (who it names, who signs). <b>Rotterdam's lessons</b> (neighbours told late, store IT forgotten). A <b>walk round the street</b> on Saturday 31 October with Joost: a school on the corner with a 07:30 drop-off, a bakery, a terrace of forty-six houses backing onto the loading yard. And an hour with <b>Lena and Maarten</b>, the Antwerp lawyer Lena has engaged, on who in Belgium has a say. The result is <b>thirty-one stakeholders</b> in four rings: Larder (12), partners and suppliers (8), authorities (5: the city's permit office, the food-safety agency FAVV-AFSCA, the fire service, the VAT office, the city's mobility department) and the community (6). Each row says what they <b>need</b> from the project, what they can <b>do</b> to it, their <b>attitude</b> now, who at Larder <b>talks to them</b>, and in which <b>language</b>.</p>""",
    how_figs=[sr_how],
    steps=[("Start from more than one source", "The charter, past lessons, the site, local experts."),
           ("Walk the place", "Who lives, works, parks and drives there?"),
           ("Include the ones without a contract", "Authorities, neighbours, rivals."),
           ("For each: what they need and what they can do", "Help it, slow it, stop it."),
           ("Note attitude and a named contact", "And the language they work in."),
           ("Review it monthly", "Stakeholders arrive and leave.")],
    vocab=[("Stakeholder", "Anyone the project affects or who can affect it."),
           ("Stakeholder register", "The list of stakeholders with their needs, influence, attitude and contact."),
           ("Internal stakeholder", "Inside the organisation: sponsor, teams, other departments."),
           ("External stakeholder", "Outside it: suppliers, authorities, customers, neighbours."),
           ("Regulator", "An authority whose permission the project needs."),
           ("Contact owner", "The one person who speaks to a stakeholder for the project.")],
    code=dict(file="antwerp/01-stakeholder-register.md", note="Sanne, 2 November 2026 (rows 1–31; 12 of them shown)", plain=True, src="""
# ANTWERP · STAKEHOLDER REGISTER                                  v1 · 2 Nov 2026

ID   WHO                         NEEDS FROM US              CAN DO TO US           NOW   CONTACT  LANG
S-01 Femke (sponsor)             a first city abroad, Sep   decide, fund, stop      L    Sanne    en
S-04 Lena (legal, DPO)           Belgian rules met          veto contracts, data    S    Sanne    en
S-13 Landlord (Schelde Vastgoed) rent, a tidy tenant        keys 1 Jun, works OK    S    Femke    nl
S-14 Builder (Pieter)            clear drawings, payment    the fit-out date        N    Sanne    nl
S-16 Produce wholesaler (Koen)   orders, delivery times     fresh stock, prices     N    ops lead nl
S-19 Payment provider            certification steps        Bancontact by July      N    Cho      en
S-21 City permit office          a complete application     permit: cooling, hours  N    builder  nl
S-22 Food-safety agency          registration, a visit      open / not open         U    Lena     nl
S-23 Fire service                plans, exits               sign-off                U    builder  nl
S-26 Neighbours (46 households)  quiet, safe pavement       object, complain        U    Sanne    nl
S-27 School on the corner        safe drop-off 07:30–08:30  object, complain        U    Sanne    nl
S-29 Waitlist (3,100)            a date, French or Dutch    order, or not           S    Priya    fr nl

ATTITUDE  U unaware · R resistant · N neutral · S supportive · L leading
SOURCES   charter · Rotterdam lessons · walk round 31 Oct · Lena + Maarten 30 Oct
REVIEW    first Friday of each month, with the engagement matrix
"""),
    tools="tools: the charter, last project's lessons, a walk round the site, a local expert, and a table.",
    dial=[("Light", "a small internal change", ["A list of names and what each needs.", "Ten minutes.", "Kept in the plan."]),
          ("Standard", "Antwerp", ["A register from four sources.", "Needs, power, attitude, contact, language.", "Reviewed monthly."]),
          ("Heavy", "public or regulated projects", ["Formal stakeholder analysis and mapping.", "Consultation records for authorities.", "A register owned by a stakeholder manager."])],
    baseline="Each line compares <b>Rotterdam's copied list of fourteen</b> to <b>a register of thirty-one from four sources, with needs, power, attitude and a contact for each</b>.",
    ratings=[(3, 4, "The people who can stop the launch are on the page."),
             (2, 3, "Fewer late surprises from outside."),
             (2, 4, "Authorities and neighbours found in November."),
             (2, 4, "Anyone can see who talks to whom."),
             (3, 4, "Lena sees her rules covered."),
             (3, 3, "Neutral."),
             (3, 4, "New stakeholders have a place to go."),
             (3, 3, "Neutral."),
             (4, 3, "A week to build, an hour a month after.")],
    pitfalls=[("Copying the last list", "It names the last project's people.", "start from four sources."),
              ("Only people with contracts", "Regulators and neighbours surprise you.", "include everyone affected."),
              ("Names without needs", "A phone book, not a register.", "write what each needs and can do."),
              ("Written once", "Stakeholders change.", "review it monthly.")],
    use=["At the start, before the plan.", "When the project enters a new place, country or organisation.", "When a new partner or authority appears.", "At each phase."],
    skip=["Never skip it; on small work it's a five-line list."],
    related=["<b>Stakeholder Map</b> (Ana, vol. 1)", "<b>Who Matters Most, and How Much?</b> (next note)", "<b>Who Decides What?</b> (vol. 2)", "<b>Launching a New City</b> (Grace, vol. 6)"],
    quiz=[("What makes someone a stakeholder?", "The project affects them, or they can affect it."),
          ("Name Sanne's four sources.", "The charter, Rotterdam's lessons, a walk round the street, Lena and Maarten."),
          ("Why was the copied list dangerous?", "It named the people Sanne knew in a country she knew; Antwerp's authorities and street weren't on it."),
          ("In January the courier agency says Belgian couriers must be employed through a specific scheme. What does Sanne do with the register?", "Add the scheme's body if it has a say, update the agency's row (needs, power), and name who at Larder talks to them."),
          ("A colleague says “neighbours aren't stakeholders, they have no contract.” Answer them.", "They're affected by the store and can affect it (objections, complaints); that makes them stakeholders.")],
    try_it="Write your project's stakeholders from memory. Then walk round the place it affects, or ask someone who knows the local rules, and add who you missed. How many were on the second list?",
    remember="The movers you <span class=\"hl\">booked</span>. The neighbours you <span class=\"hl\">forgot</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, identifying stakeholders.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 13.1 Identify Stakeholders.",
             "R. Edward Freeman, <i>Strategic Management: A Stakeholder Approach</i> (1984)."],
)

# ------------------------------------------------------------------ 02 Who Matters Most, and How Much?
pi_problem = Doodle(760, 260, "Doodle of 9 November 2026 and Sanne's mistake for this collection. On the power and interest grid she puts the city's permit office low on power: in Rotterdam the cold room needed only a notice, so she assumes the permit is a form. Its box says keep informed: one letter. In Antwerp the permit office can stop the store opening.",
                    "Sanne puts the permit office in “keep informed”: one letter. In Antwerp it can stop the store opening.", exact=True)
pi_problem.box(20, 24, 330, 140, None, "paper")
pi_problem.head(185, 60, "permit office", size=20)
pi_problem.text(185, 94, "power: low (“it's a form”)", size=16)
pi_problem.text(185, 122, "→ keep informed, one letter", size=16)
pi_problem.box(410, 24, 330, 140, None, "pink")
pi_problem.head(575, 60, "in fact", size=20)
pi_problem.text(575, 94, "permit for cooling + hours", size=16)
pi_problem.text(575, 122, "no permit, no opening", size=16)
pi_problem.arrow(352, 94, 406, 94, color="red")
pi_problem.note(380, 210, "placed by Rotterdam's rules, not Antwerp's", "red", size=19)
pi_problem.note(380, 242, "Sanne's mistake: found three months later", "pen", size=16)

pi_analogy = Doodle(760, 250, "Doodle of planning a street party. The neighbour who will bake for everyone gets a lot of your time. The council officer who issues the road-closure permit gets a careful, early visit. The shopkeeper at the end of the road is kept informed. The man who walks his dog through once a week just gets a flyer.",
                    "A street party: time for the bakers, an early visit to the permit officer, a flyer for the rest.", exact=True)
pi_analogy.box(380, 20, 360, 100, "council officer", "pink", sub="power to stop it: visit early", size=17, subsize=13)
pi_analogy.box(14, 20, 356, 100, "the bakers", "green", sub="keen, and they decide the day", size=17, subsize=13)
pi_analogy.box(14, 130, 356, 100, "the shopkeeper", "y", sub="interested: keep informed", size=17, subsize=13)
pi_analogy.box(380, 130, 360, 100, "the dog walker", "paper", sub="a flyer is enough", size=17, subsize=13)

pi_how = Doodle(760, 460, "Antwerp's power and interest grid, as corrected on 8 February 2027. Manage closely, high power and high interest: Femke, Joost, the landlord, the builder, the city's permit office (moved from keep informed), the food-safety agency, the neighbours. Keep satisfied, high power and low interest: Marco, the fire service, the payment provider. Keep informed, high interest and low power: the waitlist customers, the school, the local shops. Monitor: the press and the rival. An arrow shows the permit office's move from the keep-informed box to the manage-closely box.",
                "Antwerp's grid after 8 February: the permit office moved to “manage closely”, where it belonged.", exact=True)
pi_how.box(70, 20, 330, 190, None, "y")
pi_how.box(410, 20, 330, 190, None, "pink")
pi_how.box(70, 220, 330, 190, None, "paper")
pi_how.box(410, 220, 330, 190, None, "blue")
pi_how.head(235, 48, "keep satisfied", size=18)
pi_how.head(575, 48, "manage closely", size=18)
pi_how.head(235, 248, "monitor", size=18)
pi_how.head(575, 248, "keep informed", size=18)
for i, t in enumerate(["Marco", "fire service", "payment provider"]):
    pi_how.text(235, 84 + i * 26, t, size=15)
for i, t in enumerate(["Femke · Joost", "landlord · builder", "permit office ★", "food-safety agency", "neighbours"]):
    pi_how.text(575, 82 + i * 25, t, size=15)
for i, t in enumerate(["the press", "the rival"]):
    pi_how.text(235, 284 + i * 26, t, size=15)
for i, t in enumerate(["waitlist customers", "school · local shops", "permit office (Nov) ✗"]):
    pi_how.text(575, 284 + i * 26, t, size=15)
pi_how.arrow(660, 330, 660, 150, color="red", curve=(735, 240))
pi_how.text(30, 120, "power", size=15)
pi_how.text(400, 438, "interest →", size=15)
pi_how.note(380, 454, "★ moved on 8 Feb: Maarten, “here it's a permit, with a public inquiry”", "red", size=13)

pi_deep1 = Doodle(760, 400, "The engagement matrix for six Antwerp stakeholders on 8 February 2027. Five columns: unaware, resistant, neutral, supportive, leading. C marks where each stakeholder is now and D where Sanne needs them. Femke: C and D both at leading. Landlord: C and D at supportive. Permit office: C at unaware, D at supportive, a gap of two. Food-safety agency: C unaware, D neutral. Neighbours: C neutral, D supportive. Koen the wholesaler: C resistant, D supportive. The rows with a gap get actions.",
                  "C now, D needed. The gaps are the work: the permit office is two columns short.", exact=True)
levels = ["unaware", "resistant", "neutral", "supportive", "leading"]
for k, t in enumerate(levels):
    pi_deep1.head(250 + k * 100, 30, t, size=14)
mx = [("Femke", 4, 4), ("landlord", 3, 3), ("permit office", 0, 3), ("food-safety agency", 0, 2), ("neighbours", 2, 3), ("Koen (wholesaler)", 1, 3)]
for i, (name, c, d) in enumerate(mx):
    y = 50 + i * 52
    pi_deep1.text(16, y + 30, name, anchor="start", size=15)
    for k in range(5):
        pi_deep1.box(204 + k * 100, y + 6, 92, 40, None, "paper", rx=4)
    if c == d:
        pi_deep1.box(204 + c * 100, y + 6, 92, 40, "C D", "green", size=15, rx=4)
    else:
        pi_deep1.box(204 + c * 100, y + 6, 92, 40, "C", "y", size=15, rx=4)
        pi_deep1.box(204 + d * 100, y + 6, 92, 40, "D", "pink", size=15, rx=4)
        pi_deep1.arrow(204 + c * 100 + 92, y + 26, 204 + d * 100, y + 26, color="red")
pi_deep1.note(380, 384, "a gap is an action with an owner and a date", "pen", size=16)

POWER = dict(
    slug="power-and-interest",
    kicker="a.k.a. “the engagement matrix”: planning stakeholder engagement with power and interest",
    tldr="Not every stakeholder needs the same amount of you. Place each on a <b>power and interest grid</b>: high power and high interest, <b>manage closely</b>; high power, low interest, <b>keep satisfied</b>; low power, high interest, <b>keep informed</b>; the rest, <b>monitor</b>. Then mark on an <b>engagement matrix</b> where each one is now (unaware, resistant, neutral, supportive, leading) and where the project <b>needs</b> them. The gaps are the plan. Place them by <b>this</b> project's rules, not the last one's: power is what they can do to you here.",
    chips=[("Family", "who's involved"), ("Lives in", "a grid and a matrix beside the register"), ("Pairs with", "the stakeholder register, the communications plan, monitoring engagement")],
    pmbok=dict(covers="analysing stakeholders by power, interest and attitude, and planning how to engage each one: the engagement matrix (current vs desired)",
               domains=STK, processes=["Plan Stakeholder Engagement"], principles=["Adopt a holistic view", "Be an accountable leader"], focus=["planning"],
               older="6th: “Plan Stakeholder Engagement” (13.2), the power / interest grid and the engagement assessment matrix. 7th: the Stakeholders domain."),
    problem_side="Larder, 9 November 2026",
    problem="""  <p class="lead">This is <b>Sanne's mistake</b> for this collection. She places the thirty-one stakeholders on a power and interest grid. The city's <b>permit office</b> goes low on power: in Rotterdam the cold room needed only a notice, so she assumes the Antwerp permit is a form the builder fills in. Its box says <b>keep informed</b>: one letter, sent by the builder. <span class="hl-pink">In Antwerp, a cooling plant that size and lorries before 07:00 need an environmental permit, with a public inquiry the neighbours can object to.</span> Without it there is no opening. Nobody finds out until 8 February.</p>
  <ul>
    <li>Power was judged by habit, from another country's rules.</li>
    <li>“Keep informed” meant nobody owned the relationship.</li>
    <li>Current and desired attitudes looked the same, so there was nothing to do.</li>
  </ul>""",
    problem_figs=[pi_problem],
    analogy_side="the street party",
    analogy="""  <p>Planning a street party, you give most of your time to the <b>neighbours who'll bake and set up</b>: they care, and the day depends on them. The <b>council officer</b> who issues the road-closure permit doesn't care about your party, but can cancel it, so you visit early and hand in a tidy form. The <b>shopkeeper</b> at the end of the road is interested, so you keep them informed. The <b>dog walker</b> gets a flyer. Get the council officer wrong and the bakers have nowhere to put the cakes.</p>""",
    analogy_figs=[pi_analogy],
    map=[("The bakers", "Femke, Joost, the landlord, the builder: manage closely"),
         ("The council officer", "The permit office and the food-safety agency: power to stop it"),
         ("The shopkeeper", "Waitlist customers, the school: keep informed"),
         ("The dog walker", "The press, the rival: monitor"),
         ("Thinking the permit is just a form", "Placing the permit office by Rotterdam's rules")],
    how_side="the grid, the matrix, and the move of 8 February",
    how="""  <p>Sanne's November grid had the permit office in the wrong box. The correction comes on <b>8 February 2027</b>, when Maarten walks through the Belgian rules with Lena and her: <b>“In Rotterdam your cold room needed nothing. Here it's a permit, with a public inquiry.”</b> The permit office moves to <b>manage closely</b>, beside Femke, Joost, the landlord, the builder, the food-safety agency and the neighbours. On the engagement matrix it is <b>unaware</b> of Larder now and needs to be <b>supportive</b>, meaning confident in a complete application: a gap of two columns, and a named owner (Sanne, until Hilde, the permit agent, starts in March). Two other gaps get actions the same day: the food-safety agency (unaware → neutral: Lena books the registration) and Koen, the wholesaler (resistant → supportive: see “Are we being understood?”). Three months had gone by. That cost is told in the risk notes.</p>""",
    how_figs=[pi_how],
    steps=[("Place each stakeholder by power and interest", "Power: what they can do to the project here."),
           ("Check the high-power ones against local rules", "Ask someone who knows."),
           ("Choose an approach per box", "Manage closely, keep satisfied, keep informed, monitor."),
           ("Mark current and desired attitude", "Unaware, resistant, neutral, supportive, leading."),
           ("Turn every gap into an action", "With an owner and a date."),
           ("Re-place them when things change", "Monthly, and after any surprise.")],
    vocab=[("Power / interest grid", "Stakeholders placed by how much they can affect the project and how much they care."),
           ("Manage closely", "High power, high interest: regular, two-way, personal."),
           ("Keep satisfied", "High power, low interest: enough to keep them content."),
           ("Engagement matrix", "Where each stakeholder is now (C) and where they need to be (D)."),
           ("Engagement levels", "Unaware, resistant, neutral, supportive, leading."),
           ("Salience", "A stakeholder's pull: power, legitimacy and urgency together.")],
    code=dict(file="antwerp/02-engagement-plan.md", note="Sanne, 9 November 2026; corrected 8 February 2027", plain=True, src="""
# ANTWERP · STAKEHOLDER ENGAGEMENT PLAN                   v2 · 8 Feb 2027 (v1 9 Nov 2026)

STAKEHOLDER          BOX              NOW → NEEDED     ACTION                         OWNER   BY
Femke (sponsor)      manage closely   L → L            monthly steering, weekly note  Sanne   ongoing
Landlord             manage closely   S → S            keys 1 Jun; works approval     Femke   15 Mar
Builder (Pieter)     manage closely   N → S            drawings, payment terms agreed Sanne   1 Mar
Permit office        manage closely*  U → S            pre-application meeting,       Sanne → 11 Mar
                                                       complete application           Hilde
Food-safety agency   manage closely   U → N            registration, first visit      Lena    Sep
Neighbours           manage closely   N → S            quarterly meeting, contact     Sanne   ongoing
Koen (wholesaler)    keep satisfied   R → S            re-run the meeting, in Dutch   ops     17 Feb
Waitlist (3,100)     keep informed    S → S            monthly email, fr + nl         Priya   monthly
Press, rival         monitor          –                watch                          Priya   –

* v1 (9 Nov) had the permit office in "keep informed", power low, NOW = NEEDED = N, owner
  "builder". Wrong: power judged by Rotterdam's rules. Moved 8 Feb after Maarten's review.
"""),
    tools="tools: the register, a two-by-two grid, an engagement matrix, and someone who knows the local rules.",
    deep_dive=dict(
        side="the grid's four boxes, the engagement matrix, other lenses, and how placing goes wrong",
        intro="The grid is the most-drawn picture in stakeholder work and the easiest to get wrong. This chapter explains what each box asks of you, how the engagement matrix turns the grid into actions, two other lenses that catch what the grid misses, and four ways a stakeholder lands in the wrong box.",
        parts=[
            ("The four boxes, and what each asks of you", """  <ul>
    <li><b>Manage closely</b> (high power, high interest): regular, personal, two-way. You ask them before you decide. Femke, Joost, the landlord, and, as it turned out, the permit office.</li>
    <li><b>Keep satisfied</b> (high power, low interest): enough attention that they never have a reason to start caring. Marco on Antwerp's spending; the fire service.</li>
    <li><b>Keep informed</b> (low power, high interest): regular, clear updates; listen to them, they often see problems first. The waitlist; the school.</li>
    <li><b>Monitor</b> (low, low): watch for change. The press, the rival.</li>
  </ul>
  <p>The boxes are about <b>your time</b>, not about who matters as a person. A box is a decision about how much of you each stakeholder gets.</p>""", []),
            ("The engagement matrix: from picture to plan", """  <p>The grid says how much attention; the <b>engagement matrix</b> says what for. For each stakeholder mark where they are now (<b>C</b>) and where the project needs them (<b>D</b>) on five levels: <b>unaware</b>, <b>resistant</b>, <b>neutral</b>, <b>supportive</b>, <b>leading</b>.</p>
  <p>Not everyone needs to be supportive. A regulator should stay neutral and fair; what you need is that it understands your application. Where C and D are the same, keep doing what you do. Where they differ, write an action with an owner and a date. In November the permit office had C = D = neutral, so there was nothing to do; that was the mistake hiding inside the first one.</p>""", [pi_deep1]),
            ("Two other lenses", """  <p>The grid has two axes, and some stakeholders don't fit them. Two other lenses help:</p>
  <ul>
    <li><b>Salience</b>: how much a stakeholder pulls on the project, from three things: <b>power</b> (can they make it happen or stop it?), <b>legitimacy</b> (is their claim recognised, by law or custom?) and <b>urgency</b> (do they need an answer now?). A regulator scores high on all three the day a deadline comes. Neighbours gain legitimacy in a public inquiry.</li>
    <li><b>Direction of influence</b>: upward (sponsor, board), downward (team), sideways (peers, other departments), outward (suppliers, authorities, the community). Antwerp's surprises all came from outward.</li>
  </ul>""", []),
            ("Four ways a stakeholder lands in the wrong box", """  <ul>
    <li><b>By habit</b>: placed as they were on the last project. The permit office, placed by Rotterdam's rules.</li>
    <li><b>By org chart</b>: senior people placed high, outsiders low. A clerk with a stamp can stop a launch.</li>
    <li><b>Power to help mistaken for power to stop</b>: the landlord can help; the permit office can stop. Look for both.</li>
    <li><b>Placed once</b>: the neighbours' power rose the day the public inquiry opened. Re-place after every change of phase.</li>
  </ul>
  <p>The cure for all four is the same: for each high-power stakeholder, ask someone who knows <b>this</b> place what that stakeholder can actually do to the project, and by when.</p>""", []),
        ]),
    dial=[("Light", "a small internal project", ["A quick sort: who decides, who's affected.", "No grid.", "Talk to the first group weekly."]),
          ("Standard", "Antwerp", ["Grid and engagement matrix.", "Gaps turned into owned actions.", "Re-placed monthly."]),
          ("Heavy", "public infrastructure, mergers", ["Formal stakeholder analysis with salience.", "Engagement strategies per group.", "Independent consultation records."])],
    baseline="Each line compares <b>placing stakeholders by habit, with no gaps to act on</b> to <b>a grid checked against local rules and an engagement matrix with owned actions</b>.",
    ratings=[(3, 4, "Time goes where the launch depends on it."),
             (2, 3, "A regulator in the right box gives earlier dates."),
             (1, 4, "The stakeholder who can stop the launch is managed closely."),
             (2, 4, "Who gets how much attention is visible."),
             (2, 4, "Key stakeholders are asked, not told."),
             (3, 3, "Neutral."),
             (3, 4, "Re-placing is part of the monthly review."),
             (3, 3, "Neutral."),
             (3, 3, "An hour to place, an hour a month.")],
    pitfalls=[("Placed by habit", "Last project's rules.", "check power against this place's rules."),
              ("Senior = powerful", "A permit clerk can stop you.", "ask what each can do to the project."),
              ("No current vs desired", "A grid with nothing to do.", "mark C and D, act on the gaps."),
              ("Drawn once", "Power shifts with phases.", "re-place monthly and after surprises.")],
    use=["After the register, before the communications plan.", "When entering a new country or organisation.", "When a stakeholder surprises you.", "At each phase."],
    skip=["A two-person job with one customer you see every day."],
    related=["<b>Who Cares About This?</b> (previous note)", "<b>Stakeholder Map</b> (Ana, vol. 1)", "<b>Different Country, Different Rules</b> (this volume)", "<b>Are They Still With Us?</b> (this volume)"],
    quiz=[("Name the four boxes of the grid.", "Manage closely, keep satisfied, keep informed, monitor."),
          ("What do C and D mean on the engagement matrix?", "Where the stakeholder is now, and where the project needs them."),
          ("Why was the permit office in the wrong box?", "Its power was judged by Rotterdam's rules, where the cold room needed only a notice."),
          ("A new project in a city you know well: do you still check the high-power boxes with someone local?", "Yes, briefly: rules and people change; the check costs an hour."),
          ("The food-safety agency only needs to be neutral, not supportive. Why?", "A regulator should judge fairly; you need it to know you and find your application complete, not to champion you.")],
    try_it="Place your project's stakeholders on the grid. For each in the two high-power boxes, ask someone who knows the place: what can they actually do to us, and when? Move any that surprise you, and mark C and D.",
    remember="Bake with the <span class=\"hl\">neighbours</span>. Visit the <span class=\"hl\">permit officer</span> early.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, planning stakeholder engagement.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 13.2 Plan Stakeholder Engagement.",
             "Ronald K. Mitchell, Bradley R. Agle and Donna J. Wood, “Toward a Theory of Stakeholder Identification and Salience” (1997).",
             "Colin Eden and Fran Ackermann, <i>Making Strategy</i> (1998): the power / interest grid."],
)

# ------------------------------------------------------------------ 03 Who Hears What, and When?
cp_problem = Doodle(760, 250, "Doodle of 23 November 2026. In Rotterdam Sanne tailored out the communications plan: everyone spoke Dutch or English and sat in the same building. Antwerp has three languages: Dutch, in its Flemish form, for the city, the landlord and the neighbours; French for part of the customers; English inside Larder. The first letter to the landlord, drafted in Amsterdam, came back marked too blunt.",
                    "Three languages, thirty-one stakeholders, and a first letter that came back “too blunt”.", exact=True)
cp_problem.row([("Dutch (Flemish)", "city, landlord, street", "y"), ("French", "part of the customers", "blue"), ("English", "inside Larder", "green")], y=30, h=84, size=17, subsize=13)
cp_problem.note(380, 166, "Rotterdam had no communications plan, on purpose", "pen", size=18)
cp_problem.note(380, 204, "the first letter to the landlord: “too blunt”", "red", size=19)

cp_analogy = Doodle(760, 250, "Doodle of an airport. Passengers hear announcements in two languages and read the gate screen. The crew get a briefing in English before the flight. Air traffic control gets one exact message format. The same flight, four audiences, each told what they need, in their language, through their channel, at the right moment.",
                    "One flight, four audiences: each told what it needs, in its language, through its channel.", exact=True)
cp_analogy.row([("passengers", "two languages, the screen", "y"), ("crew", "briefing, English", "green"), ("control tower", "one exact format", "pink"), ("families", "arrival board", "paper")], y=40, h=96, size=17, subsize=12)
cp_analogy.note(380, 188, "who · what · how · when · in which language", "pen", size=19)

cp_how = Doodle(760, 450, "Antwerp's communications plan, 23 November 2026, as a table. Steering group: status and decisions, a one-page note and the meeting, monthly, English, Sanne. Femke: a weekly note, Fridays, English, Sanne. Permit office: application and meetings, formal letters through Hilde from March, Dutch. Landlord: works and keys, letters and a monthly call, Dutch, Femke. Neighbours: what's happening and whom to call, a quarterly meeting and a letter, Dutch with a French summary, Sanne then the store manager. Waitlist customers: the opening date and offers, email, monthly, French or Dutch by choice, Priya. Teams: the plan and who waits for what, Thursday meeting, English, Sanne. Every outside text in Dutch is written or checked by a Flemish writer.",
                "Who, what, how, how often, which language, who sends it. Outside texts in Dutch are checked by a Flemish writer.", exact=True)
hdr = ["audience", "what", "how", "how often", "lang", "owner"]
xs = [14, 170, 330, 490, 600, 660]
for x, h in zip(xs, hdr):
    cp_how.head(x, 30, h, anchor="start", size=15)
rows_cp = [("steering group", "status, decisions", "1 page + meeting", "monthly", "en", "Sanne"),
           ("Femke", "progress, risks", "a short note", "Fridays", "en", "Sanne"),
           ("permit office", "the application", "formal letters", "as needed", "nl", "Hilde"),
           ("landlord", "works, keys", "letter + call", "monthly", "nl", "Femke"),
           ("neighbours", "what's coming", "meeting + letter", "quarterly", "nl/fr", "Sanne"),
           ("waitlist", "date, offers", "email", "monthly", "fr/nl", "Priya"),
           ("food agency", "registration", "forms, a visit", "as needed", "nl", "Lena"),
           ("teams", "plan, waits", "Thursday 09:30", "weekly", "en", "Sanne")]
for i, r in enumerate(rows_cp):
    y = 46 + i * 44
    cp_how.box(8, y, 744, 38, None, "paper" if i % 2 else "y", rx=4)
    for x, c in zip(xs, r):
        cp_how.text(x + 4, y + 25, c, anchor="start", size=14)
cp_how.note(380, 428, "every outside text in Dutch: written or checked by a Flemish writer", "red", size=15)

COMMS = dict(
    slug="communications-plan",
    kicker="a.k.a. planning communications management: the communications plan",
    tldr="A <b>communications plan</b> says, for each audience: <b>what</b> they need to know, <b>how</b> (meeting, letter, email, a page), <b>how often</b>, in <b>which language and tone</b>, and <b>who sends it</b>. It's one table. A small team in one room can skip it; a project with authorities, neighbours, customers and teams in three languages can't. Write it from the stakeholder register, not from habit, and get outside texts checked by someone who writes the local language as it's spoken there.",
    chips=[("Family", "who's involved"), ("Lives in", "one table in the plan"), ("Pairs with", "the stakeholder register, the engagement plan, status reports")],
    pmbok=dict(covers="deciding what each stakeholder needs to hear, how, how often, in which language and from whom",
               domains=STK, processes=["Plan Communications Management"], principles=["Build an empowered culture"], focus=["planning"],
               older="6th: “Plan Communications Management” (10.1), the communications management plan. 7th: the Stakeholders domain. The 8th puts communications under stakeholders."),
    problem_side="Larder, 23 November 2026",
    problem="""  <p class="lead">For Rotterdam, Sanne <b>tailored out</b> the communications plan on 18 February: one team, one language, one building, a Thursday meeting and a Friday status were enough. Antwerp is different. The city, the landlord and the street work in <b>Dutch, in its Flemish form</b>; part of the customers want <b>French</b>; Larder works in <b>English</b>. The first letter to the landlord, drafted by Larder's marketing team in Amsterdam, comes back with a polite note from Maarten: <span class="hl-pink">correct, but blunt; in Belgium you'd open differently.</span></p>
  <ul>
    <li>Thirty-one stakeholders, three languages, two countries' habits.</li>
    <li>Nobody had said who speaks to whom.</li>
    <li>Netherlands Dutch reads differently in Antwerp.</li>
  </ul>""",
    problem_figs=[cp_problem],
    analogy_side="the airport",
    analogy="""  <p>An airport tells one flight's news to four audiences. <b>Passengers</b> hear an announcement in two languages and read the gate screen. The <b>crew</b> get a briefing in English. The <b>control tower</b> gets an exact message in a fixed format. <b>Families</b> waiting outside read the arrivals board. Nobody gets everything; everybody gets what they need, in their language, through their channel, at the right moment.</p>""",
    analogy_figs=[cp_analogy],
    map=[("Passengers, two languages", "Waitlist customers: French or Dutch, by their choice"),
         ("The crew briefing", "Teams: the Thursday meeting, in English"),
         ("The control tower's fixed format", "The permit office: formal letters through Hilde"),
         ("The arrivals board", "The neighbours: a quarterly meeting and a letter"),
         ("Who makes the announcement", "One owner per audience")],
    how_side="one table, built from the register",
    how="""  <p>Sanne writes the plan on <b>23 November</b>, one row per audience from the register. For each: <b>what</b> they need (not what Larder wants to say), <b>how</b>, <b>how often</b>, the <b>language</b>, and <b>one owner</b>. Femke gets a short note every Friday and the steering group a page a month; the permit office gets formal letters, from March through Hilde, the permit agent; the landlord, letters and a monthly call from Femke, who signed the lease; the neighbours, a quarterly meeting and a letter in Dutch with a French summary; the waitlist, a monthly email in the language each person chose. One rule covers every outside text: <b>Dutch texts are written or checked by a Flemish writer</b> (Maarten's office until Grace's localisation writers start in the spring). The landlord's letter is rewritten that week and answered within two days.</p>""",
    how_figs=[cp_how],
    steps=[("Start from the register", "One row per audience."),
           ("Write what they need to know", "Not what you want to say."),
           ("Choose the channel and rhythm", "Meeting, letter, email, page; how often."),
           ("Fix the language and the tone", "As it's spoken there."),
           ("Name one owner per audience", "One voice each."),
           ("Review it when the register changes", "With the engagement plan.")],
    vocab=[("Communications plan", "Who gets what information, how, how often, in which language, from whom."),
           ("Push communication", "Sent to people: letters, emails, notes."),
           ("Pull communication", "Put where people can fetch it: a page, a board."),
           ("Interactive communication", "Two-way: meetings, calls, workshops."),
           ("Register (language)", "The level of formality a text uses."),
           ("Localisation", "Adapting text to how a language is used in a place, not just translating it.")],
    code=dict(file="antwerp/03-communications-plan.md", note="Sanne, 23 November 2026", plain=True, src="""
# ANTWERP · COMMUNICATIONS PLAN                                          23 Nov 2026

AUDIENCE          NEEDS TO KNOW            HOW                    WHEN       LANG    OWNER
Steering group    status, decisions        1 page + meeting       1st Fri    en      Sanne
Femke (sponsor)   progress, top risks      short note             Fridays    en      Sanne
Permit office     a complete application   formal letters, visit  as needed  nl      Hilde (Mar)
Landlord          works, keys, access      letter + call          monthly    nl      Femke
Food-safety agcy  registration, a visit    forms, appointment     as needed  nl      Lena
Neighbours        what's coming, a contact meeting + letter       quarterly  nl (fr) Sanne → store mgr
School            e-bike routes, times     a visit + letter       term start nl      Sanne
Waitlist (3,100)  the date, offers         email                  monthly    fr / nl Priya
Teams             plan, who waits for what Thursday 09:30         weekly     en      Sanne

RULES   outside texts in Dutch: written or checked by a Flemish writer
        one owner per audience; others go through them
        reviewed with the register, first Friday of the month
"""),
    tools="tools: the stakeholder register, one table, and a writer who knows the local language.",
    dial=[("Light", "one team, one language", ["No written plan.", "A weekly meeting and a status.", "Say who speaks to the sponsor."]),
          ("Standard", "Antwerp", ["One table from the register.", "Language and tone per audience.", "One owner each."]),
          ("Heavy", "public or multinational programmes", ["A communications manager.", "Approval steps for outside messages.", "Translation and accessibility standards."])],
    baseline="Each line compares <b>Rotterdam's habit (a meeting and a status, no plan)</b> to <b>one table per audience with language, rhythm and an owner</b>.",
    ratings=[(3, 4, "Each audience hears what it needs."),
             (3, 3, "Neutral."),
             (2, 3, "Fewer misunderstandings abroad."),
             (2, 4, "Who says what to whom is on one page."),
             (2, 4, "Outside stakeholders get letters that sound right."),
             (3, 3, "Neutral."),
             (3, 4, "A new audience is one more row."),
             (3, 4, "Texts checked before they go out."),
             (4, 3, "An afternoon, and a writer's time.")],
    pitfalls=[("Same message for all", "Nobody gets what they need.", "write what each audience needs."),
              ("Translated, not localised", "Correct and wrong in tone.", "a local writer checks."),
              ("Many voices", "Mixed messages.", "one owner per audience."),
              ("Plan as paperwork", "Written, never used.", "keep it to one table, review it monthly.")],
    use=["Several audiences, especially outside the organisation.", "More than one language or country.", "Authorities with formal channels.", "When people say “nobody told us”."],
    skip=["One team, one language, one room: a meeting and a status are the plan."],
    related=["<b>Who Cares About This?</b> (this volume)", "<b>Where Are We, Really?</b> (vol. 2)", "<b>Localisation for a New Country</b> (Grace, vol. 6)", "<b>How Much Process Do We Need?</b> (vol. 1)"],
    quiz=[("What five things does each row of the plan say?", "What they need, how, how often, which language, who sends it."),
          ("Why did Rotterdam have no communications plan?", "Tailored out: one team, one language, one building."),
          ("What was wrong with the first landlord letter?", "Correct but blunt: Netherlands Dutch habits; rewritten with a Flemish writer."),
          ("Priya's team wants to post opening news to the neighbours themselves. What does Sanne say?", "The neighbours have one owner (Sanne, then the store manager); the news goes through them, in the agreed letter."),
          ("A French-speaking customer complains the waitlist email is Dutch only. What's the fix?", "The plan says French or Dutch by choice; check the sign-up field and resend in French.")],
    try_it="Write your project's communications as one table: audience, what they need, how, how often, language, owner. Find the audience with no owner, or two.",
    remember="One flight, <span class=\"hl\">four</span> announcements. Each in <span class=\"hl\">its own</span> language.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, planning communications.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 10.1 Plan Communications Management.",
             "Erin Meyer, <i>The Culture Map</i> (2014)."],
)

# ------------------------------------------------------------------ 04 How Do We Keep Them With Us?
me_problem = Doodle(760, 260, "Doodle of January 2027. Rotterdam told its neighbours on 2 March 2026, eight weeks before opening, by letter. They complained about e-bikes on the pavement in the first week. For Antwerp, Sanne wants to meet the street before anything is fixed, and Femke is about to tell investors that Antwerp opens in September.",
                    "Rotterdam told its street late, by letter. Antwerp's street, and the investors, are next.", exact=True)
me_problem.box(20, 24, 330, 140, None, "pink")
me_problem.head(185, 60, "Rotterdam, 2 Mar 2026", size=19)
me_problem.text(185, 94, "a letter, 8 weeks before", size=16)
me_problem.text(185, 122, "complaints in week 1", size=16)
me_problem.box(410, 24, 330, 140, None, "y")
me_problem.head(575, 60, "Antwerp, Jan 2027", size=19)
me_problem.text(575, 94, "46 households, a school", size=16)
me_problem.text(575, 122, "investors hear “September”", size=16)
me_problem.note(380, 210, "people who hear late, or hear a promise, feel misled", "red", size=18)
me_problem.note(380, 242, "expectations are set by the first thing they hear", "pen", size=16)

me_analogy = Doodle(760, 250, "Doodle of a family building an extension. Before the skip arrives, they knock on the neighbours' doors: here is the drawing, the builders start in June, they work eight till five, this is my number. They don't promise it will be quiet. They promise to tell them before the noisy week.",
                    "Knock before the skip arrives: the drawing, the hours, a number to call, and only promises you can keep.", exact=True)
me_analogy.row([("knock first", "before the skip", "green"), ("show the plan", "drawing, hours", "y"), ("a number", "to call", "blue"), ("keep promises", "or don't make them", "pink")], y=40, h=96, size=17, subsize=13)
me_analogy.note(380, 196, "“I'll tell you before the noisy week”, not “it'll be quiet”", "pen", size=17)

me_how = Doodle(760, 450, "The neighbours' meeting, Thursday 21 January 2027, 19:00 at the community centre. Twenty-eight people from forty-six households, and the head of the school. What they raised: lorries before seven in the morning, twelve people; e-bikes on the pavement, nine; condenser noise at night, five; litter, two. What Sanne promised: e-bikes leave by the back lane, not past the school; a named contact; a meeting every quarter; a daily litter walk. What she did not promise: lorry times, answer by the end of March. A line shows the lorry concern going into the stakeholder log but not into the risk register.",
                "Twenty-eight came. Four promises she could keep, one she wouldn't make, and one link she missed.", exact=True)
me_how.box(14, 14, 360, 210, None, "y")
me_how.head(194, 44, "they raised", size=19)
for i, t in enumerate(["lorries before 07:00 · 12", "e-bikes on the pavement · 9", "condenser noise at night · 5", "litter · 2"]):
    me_how.text(194, 84 + i * 34, t, size=16)
me_how.box(386, 14, 360, 210, None, "green")
me_how.head(566, 44, "Sanne promised", size=19)
for i, t in enumerate(["e-bikes by the back lane", "a named contact", "a meeting every quarter", "a litter walk every day"]):
    me_how.text(566, 84 + i * 34, t, size=16)
me_how.box(14, 240, 732, 76, "not promised: lorry times", "pink", sub="“we'll answer by the end of March”", size=18, subsize=14)
me_how.box(14, 340, 350, 84, "stakeholder log", "paper", sub="lorry concern: logged", size=17, subsize=13)
me_how.box(396, 340, 350, 84, "risk register", "paper", sub="R-07 permit: not linked", size=17, subsize=13, stroke="red")
me_how.arrow(364, 382, 392, 382, color="red", dash=True)
me_how.note(380, 442, "the twelve who raised lorries were the people who could object in a permit inquiry", "red", size=13)

EXPECT = dict(
    slug="managing-expectations",
    kicker="a.k.a. managing stakeholder engagement: keeping people with you, and their expectations honest",
    tldr="<b>Managing engagement</b> is the work of keeping stakeholders with the project: meeting them <b>early</b>, before decisions are fixed; <b>listening</b> to what worries them; making <b>only promises you can keep</b>, and keeping them visibly; and saying plainly what you <b>can't</b> promise yet, with a date for the answer. Expectations are set by the first thing people hear, so make it true. Link every concern to the plan: a worry is often a risk in disguise.",
    chips=[("Family", "who's involved"), ("Lives in", "meetings, a log of concerns and commitments"), ("Pairs with", "the engagement plan, the communications plan, the risk register")],
    pmbok=dict(covers="working with stakeholders to meet their needs, address their concerns and set honest expectations, and keeping the commitments made to them",
               domains=STK, processes=["Manage Stakeholder Engagement"], principles=["Be an accountable leader", "Focus on value"], focus=["executing"],
               older="6th: “Manage Stakeholder Engagement” (13.3), the issue log and change requests. 7th: the Stakeholders domain."),
    problem_side="Larder, January 2027",
    problem="""  <p class="lead">Rotterdam's neighbours got a <b>letter on 2 March 2026</b>, eight weeks before opening, and complained about e-bikes on the pavement in the first week. For Antwerp, Sanne wants to meet the street <b>before anything is fixed</b>. At the same time Femke is preparing an investor update that says <b>“Antwerp opens in September.”</b> <span class="hl-pink">Two groups are about to form their expectations from the first thing they hear.</span> One is a street that hasn't been asked; the other is a board that would hear a planning date as a promise.</p>
  <ul>
    <li>People who hear late feel decided upon.</li>
    <li>A planning date said as a promise becomes a promise.</li>
    <li>Concerns heard in a meeting often go nowhere.</li>
  </ul>""",
    problem_figs=[me_problem],
    analogy_side="the extension next door",
    analogy="""  <p>A family planning an extension <b>knocks on the neighbours' doors</b> before the skip arrives. They show the drawing, say the builders start in June and work eight till five, and leave a phone number. They don't promise it will be quiet; they promise to <b>tell them before the noisy week</b>, and they do. The neighbours put up with months of dust. The family down the road who didn't knock got a complaint to the council in week one.</p>""",
    analogy_figs=[me_analogy],
    map=[("Knocking before the skip", "Meeting the street in January, nine months before opening"),
         ("Showing the drawing and the hours", "The store layout, delivery and e-bike routes"),
         ("A phone number", "A named contact: Sanne, then the store manager"),
         ("“I'll tell you before the noisy week”", "Four promises she could keep; lorry times answered by March"),
         ("The investors", "“Planning date September”, not “opens in September”")],
    how_side="meet early, promise little, keep every promise, link concerns to risks",
    how="""  <p>On <b>Thursday 21 January</b> at 19:00, at the community centre, <b>twenty-eight people</b> from the forty-six households come, with the head of the school. Sanne shows the store layout and the routes, then mostly listens. Twelve raise <b>lorries before 07:00</b> (Koen's wholesaler delivers at 05:30), nine e-bikes on the pavement, five condenser noise at night, two litter. She promises four things she controls: e-bikes leave by the <b>back lane</b>, not past the school; a <b>named contact</b>; a <b>meeting every quarter</b>; a <b>daily litter walk</b>. Lorry times she <b>doesn't</b> promise: “we'll answer by the end of March.” With Femke she agrees the investor wording: <b>“planning date September 2027, confirmed when the store's permits are in.”</b> One thing she misses. The lorry concern goes into the <b>stakeholder log</b>, but not into the <b>risk register</b>, where the permit risk sits rated low. The twelve people who raised it are the people who can object when the permit goes to a public inquiry.</p>""",
    how_figs=[me_how],
    steps=[("Meet people before decisions are fixed", "Early enough that you can still change something."),
           ("Listen more than you present", "Write every concern down."),
           ("Promise only what you control", "And keep it visibly."),
           ("Say what you can't promise, with a date", "“We'll answer by…”."),
           ("Link each concern to the plan", "Is it a risk, an issue, a change?"),
           ("Set dates as ranges or planning dates", "Until they're safe to promise.")],
    vocab=[("Engagement", "Working with stakeholders so they understand and support the project, or at least aren't surprised."),
           ("Expectation", "What a stakeholder believes the project will deliver, and when."),
           ("Commitment log", "The promises made to stakeholders, with owners and dates."),
           ("Planning date", "A date to plan towards, not yet promised."),
           ("Concern", "A worry a stakeholder raises; often a risk in disguise."),
           ("Under-promise", "Commit to less than you expect to achieve, so you can keep it.")],
    code=dict(file="antwerp/04-neighbours-meeting.md", note="Sanne, Thursday 21 January 2027, community centre, 19:00", plain=True, src="""
# ANTWERP · NEIGHBOURS' MEETING                        Thu 21 Jan 2027 · 19:00 · 28 people
                                                       (of 46 households) + the school's head
CONCERNS RAISED                                  COUNT   GOES TO
lorries before 07:00 (wholesaler 05:30)            12    stakeholder log  (and R-07? NOT LINKED)
e-bikes on the pavement, past the school            9    plan: routes
condenser noise at night                            5    builder: spec
litter, parking                                     2    store routine

COMMITMENTS (only what we control)               OWNER          BY
C1 e-bikes leave by the back lane                Joost          from opening
C2 one named contact, phone + email              Sanne → store  from today
C3 a meeting every quarter                       Sanne → store  next: Apr
C4 a litter walk every day                       store manager  from opening
NOT PROMISED  lorry times: "we'll answer by 31 March"

INVESTOR WORDING (Femke, 25 Jan)  "Antwerp: planning date September 2027, confirmed when
                                   the store's permits are in."
"""),
    tools="tools: a room in the neighbourhood, a layout drawing, a notebook, a commitment log, and the risk register beside it.",
    dial=[("Light", "internal change", ["Talk to the affected people early.", "Write down what you promised.", "Follow up."]),
          ("Standard", "Antwerp", ["A meeting before decisions are fixed.", "A commitment log with owners.", "Concerns linked to risks; planning dates, not promises."]),
          ("Heavy", "public works", ["Formal consultation phases.", "Published responses to every concern.", "Community liaison officers."])],
    baseline="Each line compares <b>Rotterdam's letter eight weeks before opening</b> to <b>a meeting nine months before, four kept promises, and planning dates instead of promises</b>.",
    ratings=[(3, 4, "The store fits its street."),
             (2, 4, "A planning date never became a broken promise."),
             (2, 3, "Concerns heard early; one link missed."),
             (2, 4, "Commitments written and owned."),
             (2, 4, "The street and the board heard the truth first."),
             (3, 3, "Neutral."),
             (3, 4, "Early meetings leave room to change routes and specs."),
             (3, 3, "Neutral."),
             (3, 3, "An evening a quarter.")],
    pitfalls=[("Telling instead of asking", "People feel decided upon.", "meet before decisions are fixed."),
              ("Promising to please", "Broken later.", "promise only what you control."),
              ("Planning dates said as promises", "The board remembers the promise.", "say “planning date” until it's safe."),
              ("Concerns left in the minutes", "A worry is often a risk.", "link each to the register.")],
    use=["Before decisions that affect people are fixed.", "Whenever a date is said outside the team.", "When stakeholders change mood.", "Through the whole project, not just the start."],
    skip=["Never skip it; on small work it's a conversation."],
    related=["<b>Who Hears What, and When?</b> (previous note)", "<b>Managing Up</b> (Grace, vol. 5)", "<b>Delivering Bad News</b> (Grace, vol. 5)", "<b>What Could Happen?</b> (this volume)"],
    quiz=[("Why did Sanne meet the street in January?", "Before anything was fixed, so concerns could still change the plan; Rotterdam's letter came too late."),
          ("What did she not promise, and why?", "Lorry times: she didn't control them yet; an answer by the end of March."),
          ("What was the investor wording?", "“Planning date September 2027, confirmed when the store's permits are in.”"),
          ("At the meeting a neighbour asks Sanne to promise no noise at all. What does she say?", "She can't promise that; she promises what Larder controls (routes, contact, meetings) and to warn them before noisy work."),
          ("Which link did Sanne miss, and why did it matter?", "The lorry concern wasn't linked to the permit risk; those neighbours could object in the permit's public inquiry.")],
    try_it="List the promises your project has made to people outside the team. Which ones do you control? For each concern you've heard, write whether it's a risk, an issue or a change, and put it there.",
    remember="Knock <span class=\"hl\">before</span> the skip. Promise only what you <span class=\"hl\">control</span>.",
    sources=["Project Management Institute, <i>PMBOK Guide</i>, Eighth Edition (2025): Stakeholders domain, managing stakeholder engagement.",
             "Project Management Institute, <i>PMBOK Guide</i>, Sixth Edition (2017): 13.3 Manage Stakeholder Engagement.",
             "Sherry R. Arnstein, “A Ladder of Citizen Participation” (1969)."],
)

NOTES = [REGISTER, POWER, COMMS, EXPECT]
