# Series 2 · Book 5 · The IT Operations Notebook · Vol. 5 · Risk, money and vendors.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 5".

# ------------------------------------------------------------------ 11 What Does It Cost to Run?
cc_problem = Doodle(760, 260, "Doodle of January 2028: the cloud bill is 78,000 euros a month and cost per order 3.05 euros against a target of 2.80. Marco asks which services cost what. Eli can't say: 61 percent of the spending carries no tag for a service or an owner. Staging runs all night and every weekend, old snapshots pile up, and the browse replica sized for Christmas is still at Christmas size.",
                    "€78k a month, and 61 % of it can't be traced to a service or an owner.")
cc_problem.box(14, 30, 230, 100, "€78k / month", "pink", sub="cloud bill, Jan 2028", size=21, subsize=14)
cc_problem.box(264, 30, 230, 100, "61 % untagged", "pink", sub="no service, no owner", size=20, subsize=14)
cc_problem.box(514, 30, 232, 100, "€3.05 / order", "y", sub="target €2.80", size=20, subsize=14)
cc_problem.note(380, 180, "staging all night · old snapshots · Christmas-sized replica in January", "pen", size=15)

cc_analogy = Doodle(760, 220, "Doodle of a household electricity bill split by meter: the heat pump, the car charger, the rest of the house. Once each has its own number, the family notices the car charges at the peak price, and the heat pump runs when nobody's home. The total bill never told them that.",
                    "One bill says nothing. A meter per thing shows the car charging at peak price.")
cc_analogy.icon("plug", 60, 50, 1.3)
cc_analogy.row([("heat pump", "€62", "y"), ("car charger", "€48 (peak!)", "pink"), ("the rest", "€35", "paper")], x=170, y=40, h=96, w=180, gap=18, size=17, subsize=15)
cc_analogy.note(450, 190, "a meter per thing, and someone who reads it", "pen", size=18)

cc_how = Doodle(760, 400, "Larder's cost practice from February 2028. Every resource is tagged with its service and owner; untagged spending fell from 61 to 2 percent, and the pipeline refuses untagged resources. Each service's monthly bill and cost per 1,000 orders goes on its monthly service review, so its owner sees it. A monthly 30-minute waste hunt by Eli and Bram: staging switched off nights and weekends, 4,100 euros a month; old snapshots and unattached disks, 2,600; the browse replica back to normal size after Christmas, 1,900; log retention matched to need, 800. Operations' share of the reduction: about 9,400 euros a month. With Ana's architecture changes the bill went from 78,000 to 58,000 euros a month.",
                "Tag everything, show each owner their bill, hunt waste monthly. Ops' share: ≈ €9,400 a month of the €20k saved.")
cc_how.box(14, 14, 236, 110, "tags", "blue", sub="service + owner · 61 % → 2 % untagged", size=19, subsize=12)
cc_how.box(262, 14, 236, 110, "bill per service", "y", sub="on the monthly review", size=19, subsize=13)
cc_how.box(510, 14, 236, 110, "waste hunt", "green", sub="30 min a month", size=19, subsize=13)
for i, (t, v) in enumerate([("staging off nights/weekends", "€4,100"), ("old snapshots + disks", "€2,600"), ("replica back to size", "€1,900"), ("log retention", "€800")]):
    cc_how.box(14, 146 + i * 46, 560, 40, t, "paper", size=14)
    cc_how.box(586, 146 + i * 46, 160, 40, v, "green", size=15)
cc_how.note(380, 354, "with Ana's changes: €78k → €58k a month", "green", size=17)
cc_how.note(380, 388, "the pipeline refuses untagged resources", "pen", size=15)

CLOUD_COSTS = dict(
    slug="cloud-costs",
    kicker="a.k.a. “service financial management”",
    tldr="A cloud bill is just a number until it's split by <b>service and owner</b>. <b>Tag everything</b>, show each owner <b>their service's bill and its cost per order</b> on the monthly review, and hold a short <b>monthly waste hunt</b> for the usual suspects: environments running when nobody uses them, forgotten snapshots, things sized for a peak that's over. Most waste is ordinary, and it comes back unless someone looks every month.",
    chips=[("Family", "risk, money and vendors"), ("Lives in", "tags on every resource; the monthly service review; a 30-minute waste hunt"), ("Pairs with", "the service review (vol. 4), capacity, Ana's cost-aware architecture")],
    itil=dict(groups=["general"], chain=["plan", "improve"], practices=["service financial management", "measurement and reporting"],
              sre="(efficiency as part of reliability work)", principles=["Focus on value", "Optimise and automate"],
              older="ITIL v3: financial management for IT services (budgeting, accounting, charging)"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">In January the cloud bill is <b>€78,000 a month</b>, and cost per order is <b>€3.05</b> against Femke's target of €2.80. Marco asks which services cost what. <span class="hl-pink">Eli can't say: 61 % of the spending carries no tag for a service or an owner.</span> Staging runs all night and every weekend, old snapshots pile up, and the browse replica sized for Christmas is still at Christmas size in January.</p>
  <ul>
    <li>Nobody sees the bill for the thing they own.</li>
    <li>Peak sizing never gets undone.</li>
    <li>Savings depend on someone remembering to look.</li>
  </ul>""",
    problem_figs=[cc_problem],
    meanwhile=[("architect-5", "cost-aware-architecture", "Ana's cost work of 21 February 2028: cost per order €3.05 at the end of 2027; cloud bill €78k → €58k a month; cloud cost per order ≈ 9.6 → 7.1 cents.",
                "Eli's share of the same €20k: tags, a bill per owner, and a monthly waste hunt that found about €9,400 a month.")],
    analogy_side="the electricity bill by meter",
    analogy="""  <p>One household electricity bill says nothing useful. With <b>a meter per thing</b> (the heat pump, the car charger, the rest of the house), the family notices that the car charges at <b>the peak price</b>, and the heat pump runs when nobody's home. The total never told them that. Someone still has to <b>read the meters every month</b>.</p>""",
    analogy_figs=[cc_analogy],
    map=[("A meter per thing", "A tag per resource: service and owner"),
         ("Each person sees their meter", "Each owner sees their service's bill on the monthly review"),
         ("Charging at peak price", "Staging running all night and weekend"),
         ("The heat pump when nobody's home", "A Christmas-sized replica in January"),
         ("Reading the meters monthly", "A 30-minute waste hunt")],
    how_side="tags, a bill per owner, a monthly waste hunt",
    how="""  <p>From <b>February</b>:</p>
  <ul>
    <li><b>Tags</b>: every resource carries its service and owner. Untagged spending falls from <b>61 % to 2 %</b>, and the pipeline now refuses to create untagged resources.</li>
    <li><b>A bill per owner</b>: each service's monthly cost, and its <b>cost per 1,000 orders</b>, goes on its monthly service review, so Ben sees ordering's bill next to its SLOs.</li>
    <li><b>A monthly waste hunt</b>: 30 minutes, Eli and Bram, looking at the usual suspects:
      <ul>
        <li><b>Staging off</b> at night and at weekends: <b>€4,100</b> a month.</li>
        <li>Old snapshots and unattached disks: <b>€2,600</b>.</li>
        <li>The browse replica back to normal size after Christmas: <b>€1,900</b>.</li>
        <li>Log retention matched to what's actually needed: <b>€800</b>.</li>
      </ul>
    </li>
  </ul>
  <p>Operations' share is about <b>€9,400 a month</b>. With Ana's architecture changes, the bill goes from <b>€78k to €58k a month</b>, and cost per order moves towards €2.80 for the first time.</p>""",
    how_figs=[cc_how],
    steps=[("Tag every resource with service and owner", "Refuse untagged resources in the pipeline."),
           ("Show each owner their bill", "Next to their SLOs, monthly."),
           ("Use a unit cost", "Cost per 1,000 orders, not just euros."),
           ("Hunt waste monthly", "Idle environments, snapshots, peak sizes, retention."),
           ("Undo peak sizing after the peak", "Put it on the calendar."),
           ("Count savings honestly", "And say who made them.")],
    vocab=[("Service financial management", "Knowing and managing what services cost, and their value."),
           ("Tagging", "Labelling resources so costs can be traced to services and owners."),
           ("Unit cost", "Cost per unit of business (per order), not just in total."),
           ("Showback", "Showing teams their costs without charging them."),
           ("Waste", "Spending that buys nothing: idle, forgotten or oversized resources."),
           ("Right-sizing", "Matching a resource's size to what it actually needs.")],
    code=dict(file="ops/costs/2028-02.md", note="first monthly waste hunt · Feb 2028", plain=True, src="""
untagged spend        Jan 61 % → Feb 2 % (pipeline refuses untagged from 12 Feb)
per service (Feb)     ordering €19.4k · Dispatch €7.1k · data €6.8k · staging €5.2k
                      · business €4.0k · … (on each monthly service review)
cost per 1,000 orders ordering €14.6 · Dispatch €5.3

waste hunt (30 min, Eli + Bram)                         per month
  staging off 20:00–07:00 and weekends                  €4,100
  snapshots > 35 days + unattached disks                €2,600
  browse replica: Christmas size → normal               €1,900
  log retention: 1 year only where needed (Lena)        €800
  operations total                                      ≈ €9,400
bill   Jan €78k → Apr €58k (with Ana's architecture changes)
"""),
    tools="tools: the cloud's cost reports and tags, a tag policy in the pipeline, the monthly review page, and a recurring 30-minute slot.",
    ladder=[("one big bill", ["Nobody owns any of it.", "Peak sizes stay."]),
            ("tagged, shown, hunted monthly", ["Each owner sees their bill.", "Unit cost per order."]),
            ("cost in every design", ["Cost estimates in pull requests.", "Budgets per service with alerts."]),
            ("cost as a quality", ["Cost per order tracked like an SLO.", "Waste rarely reappears."])],
    ladder_now=1,
    baseline="Each line compares <b>one untraceable cloud bill</b> to <b>tags, a bill per owner and a monthly waste hunt</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "Every euro traceable to a service and owner."),
             (3, 3, "Neutral."),
             (1, 4, "≈ €9,400 a month from operations alone."),
             (3, 3, "Neutral."),
             (3, 3, "30 minutes a month.")],
    pitfalls=[("Untagged resources", "Costs nobody owns.", "the pipeline refuses them."),
              ("Bills only to finance", "Owners never see them.", "on each service's review."),
              ("Peak sizing forgotten", "Christmas paid for until Easter.", "undo it on a calendar date."),
              ("Savings once", "Waste creeps back.", "hunt monthly.")],
    use=["Nobody can say what a service costs.", "Cost per order matters to the business.", "After a peak.", "Before a budget round."],
    skip=["Tiny bills where the time costs more than the savings."],
    related=["<b>Cost-Aware Architecture</b> (Ana, vol. 5)", "<b>Cost Visibility (FinOps)</b> (cloud, vol. 6)", "<b>Will Christmas Fit?</b> (vol. 4)", "<b>The Monthly Service Review</b> (vol. 4)"],
    quiz=[("Why couldn't Eli answer Marco in January?", "61 % of cloud spending had no service or owner tag."),
          ("What's a unit cost, and Larder's?", "Cost per unit of business; here, cost per 1,000 orders per service."),
          ("What did the first waste hunt find?", "Staging running nights and weekends, old snapshots and disks, a Christmas-sized replica, over-long log retention."),
          ("How much did operations save?", "About €9,400 a month; with Ana's changes the bill fell from €78k to €58k."),
          ("How are untagged resources prevented?", "The pipeline refuses to create them.")],
    quiz_sit=[("Ben asks why ordering's cost per 1,000 orders went up 15 % in March. What do you look at?", "The service's tagged costs by resource for February vs March: a new resource, a bigger size, more logs, or fewer orders. Then decide together whether it's waste or value.")],
    try_it="Find out what share of your cloud bill has no owner tag. Pick one service and work out its monthly cost and cost per business unit. Find one thing that runs when nobody uses it.",
    remember="A bill nobody owns never shrinks. <span class=\"hl\">Tag it, show it to its owner</span>, and hunt the ordinary waste <span class=\"hl\">every month</span>.",
    sources=["AXELOS, <i>ITIL 4: Service financial management</i> practice guide (2020).",
             "J.R. Storment and Mike Fuller, <i>Cloud FinOps</i> (2nd ed., O'Reilly, 2023).",
             "FinOps Foundation, <i>FinOps Framework</i>."],
)

# ------------------------------------------------------------------ 12 Which Risks Keep Us Up at Night?
rr_problem = Doodle(760, 260, "Doodle of the risks in Eli's head in March 2028, written down for the first time: a region outage; another phishing attack; the old handheld batteries failing at peak; the billing vendor; DNS. And one he finds hardest to write: operations depends on two people, Eli and Bram. Each risk had been discussed in a corridor at least once; none had an owner, a score or a next step.",
                    "Five risks discussed in corridors, and the hardest one: operations depends on two people.")
for i, t in enumerate(["region outage", "phishing", "old batteries", "billing vendor", "DNS"]):
    rr_problem.box(14 + i * 148, 30, 136, 80, t, "y", size=15)
rr_problem.box(110, 140, 540, 64, "operations depends on Eli and Bram", "pink", stroke="red", size=17)
rr_problem.note(380, 236, "no owner · no score · no next step", "red", size=17)

rr_analogy = Doodle(760, 220, "Doodle of a farmer's list on the kitchen wall: the barn roof before winter, the old tractor, a dry summer, the farmhand leaving. Each with how likely and how bad, what she's doing about it, and the sign that would make her act sooner. She looks at it on the first of the month.",
                    "The farmer's wall list: likely, bad, what I'm doing, and the sign to act sooner. First of the month.")
rr_analogy.icon("ledger", 60, 40, 1.4)
rr_analogy.box(170, 30, 576, 120, None, "paper")
for i, t in enumerate(["barn roof · likely · bad · fix in Oct · sign: first leak", "old tractor · likely · medium · save for new one", "farmhand leaving · possible · very bad · train a second"]):
    rr_analogy.text(190, 64 + i * 32, t, anchor="start", size=15)
rr_analogy.note(450, 190, "looked at on the first of the month", "pen", size=18)

rr_how = Doodle(760, 400, "Larder's operational risk register from March 2028: 14 risks, each with a cause, a likelihood and impact from 1 to 5, an owner, actions with dates, and a trigger that would make it urgent. Top five: R1 operations depends on two people, 4 by 4, owner Eli, action: hire two SREs, write runbooks for the last undocumented systems; R2 phishing, 4 by 3, owner Eli, action: passkeys for support and admin; R3 old handhelds' batteries at peak, 4 by 2, owner Dee, action: replace HH-2024 by September; R4 billing vendor, 3 by 3, owner Cho, action: exit plan and export test; R5 region outage, 2 by 5, owner Eli, action: pilot light and invocation rules. Reviewed monthly in 15 minutes; the top five go to Femke. By June R1 is 3 by 4 and R2 2 by 3.",
                "14 risks with owners, scores, actions and triggers. Top five to Femke monthly. R1 is people.")
rows = [("R1 two people", "4 × 4", "Eli: hire 2 SREs · runbooks", "pink"), ("R2 phishing", "4 × 3", "Eli: passkeys by May", "pink"),
        ("R3 old batteries", "4 × 2", "Dee: replace HH-2024 by Sep", "y"), ("R4 billing vendor", "3 × 3", "Cho: exit plan + export test", "y"),
        ("R5 region outage", "2 × 5", "Eli: pilot light + invocation", "y")]
for i, (r, sc, a, f) in enumerate(rows):
    y = 14 + i * 56
    rr_how.box(14, y, 230, 48, r, f, size=15)
    rr_how.box(254, y, 90, 48, sc, "paper", size=16)
    rr_how.box(354, y, 392, 48, a, "paper", size=13)
rr_how.note(380, 318, "monthly, 15 minutes · top five to Femke", "pen", size=16)
rr_how.note(380, 354, "June: R1 3 × 4 · R2 2 × 3", "green", size=16)

OPS_RISK = dict(
    slug="ops-risk-register",
    kicker="a.k.a. “operational risk management”",
    tldr="An <b>operational risk register</b> writes down what could go wrong before it does: each risk with a <b>cause</b>, a <b>likelihood and impact</b>, an <b>owner</b>, <b>actions with dates</b>, and a <b>trigger</b> that would make it urgent. Review it monthly in a few minutes and send the top few to leadership. Include the uncomfortable risks, especially the ones about people, because those are usually the biggest.",
    chips=[("Family", "risk, money and vendors"), ("Lives in", "ops/risks.md, monthly 15 minutes, top five to Femke"), ("Pairs with", "Ana's and Sanne's risk registers, near misses (vol. 2), game days")],
    itil=dict(groups=["general"], chain=["plan", "improve"], practices=["risk management"],
              sre="(risk-based prioritisation of reliability work)", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: risk management within ITSCM and information security"),
    problem_side="Larder, March 2028",
    problem="""  <p class="lead">In March Eli writes down, for the first time, the risks he carries in his head: a <b>region outage</b>, <b>another phishing attack</b>, the <b>old handhelds' batteries</b> failing at the peak, the <b>billing vendor</b>, <b>DNS</b>. And the one he finds hardest to write: <b>operations depends on two people, Eli and Bram</b>. <span class="hl-pink">Each had been discussed in a corridor at least once. None had an owner, a score or a next step.</span></p>
  <ul>
    <li>Risks nobody owns turn into incidents somebody has to handle.</li>
    <li>The scariest risks (people) are the least likely to be written down.</li>
    <li>Leadership can't fund what it can't see.</li>
  </ul>""",
    problem_figs=[rr_problem],
    meanwhile=[("architect-6", "risk-register", "Ana's architecture risk register of 24 April 2028: twelve risks, number 1 “architecture depends on Ana” (4 × 4 → 2 × 4 by September).",
                "Eli's operational register, the month before: number 1 “operations depends on Eli and Bram”, 4 × 4, and the plan for a reliability team.")],
    analogy_side="the farmer's list on the kitchen wall",
    analogy="""  <p>A farmer keeps a list on the kitchen wall: the <b>barn roof before winter</b>, the <b>old tractor</b>, a dry summer, the <b>farmhand leaving</b>. Each has how likely and how bad, what she's doing about it, and the <b>sign that would make her act sooner</b> (the first leak). She looks at it on the first of every month. The farmhand line is the one she most wanted to leave off.</p>""",
    analogy_figs=[rr_analogy],
    map=[("The barn roof", "A region outage"),
         ("The old tractor", "The HH-2024 handhelds' batteries"),
         ("The farmhand leaving", "Operations depending on Eli and Bram"),
         ("The first leak", "A trigger: a second phishing attempt, a battery failing at peak"),
         ("The first of the month", "A 15-minute monthly review")],
    how_side="cause, score, owner, actions, trigger; monthly; top five up",
    how="""  <p>Eli writes <b>14 risks</b>, each with a cause, likelihood and impact (1–5 each), an owner, actions with dates, and a trigger. The top five:</p>
  <ul>
    <li><b>R1 Operations depends on two people</b> (4 × 4, Eli): hire two SREs; runbooks for the last undocumented systems. That becomes the reliability team (vol. 6).</li>
    <li><b>R2 Phishing</b> (4 × 3, Eli): passkeys for support and admin accounts by May.</li>
    <li><b>R3 Old handhelds' batteries</b> at the peak (4 × 2, Dee): replace HH-2024 by September.</li>
    <li><b>R4 Billing vendor</b> (3 × 3, Cho): exit plan and export test before June's renewal.</li>
    <li><b>R5 Region outage</b> (2 × 5, Eli): pilot light (ADR 0026) and invocation rules.</li>
  </ul>
  <p>The register is reviewed monthly in <b>15 minutes</b>, with the top five going to Femke alongside the incident page. Near misses and game-day findings feed it. By <b>June</b>, R1 is <b>3 × 4</b> (two SREs hired) and R2 <b>2 × 3</b> (passkeys live).</p>""",
    how_figs=[rr_how],
    steps=[("Write the risks you carry in your head", "Including the uncomfortable ones."),
           ("Give each a cause, a score and an owner", "Likelihood × impact, 1–5."),
           ("Add actions with dates", "And who does them."),
           ("Add a trigger", "The sign that makes it urgent."),
           ("Review monthly, briefly", "Top five to leadership."),
           ("Feed it from near misses and game days", "Evidence, not guesses.")],
    vocab=[("Risk", "Something that might happen and would affect what matters."),
           ("Likelihood × impact", "A simple score for ranking risks."),
           ("Risk owner", "The person accountable for managing a risk."),
           ("Treatment", "What you do: reduce, transfer, avoid or accept."),
           ("Trigger", "A sign that a risk is about to become an issue."),
           ("Key-person risk", "Too much depending on one or two people.")],
    code=dict(file="ops/risks.md", note="from March 2028 · reviewed monthly", plain=True, src="""
id  risk                            cause                          L×I   owner  actions (dates)                         trigger
R1  ops depends on Eli + Bram       no team, tacit knowledge       4×4   Eli    hire 2 SREs (Jul, Aug) · runbooks for   either on leave
                                                                                 last 6 systems (Jun)                    at a peak
R2  phishing → account takeover     approvable prompts             4×3   Eli    number matching (Mar ✓) · passkeys      2nd attempt
                                                                                 support + admin (May ✓)
R3  old handheld batteries at peak  HH-2024 ageing                 4×2   Dee    replace HH-2024 by Sep                  > 5 swaps/day
R4  billing vendor                  silent failures, weak export   3×3   Cho    exit plan + export test (May)           2nd silence
R5  region outage                   one region                     2×5   Eli    pilot light (ADR 0026) · invocation     outage > 1 h
… 14 risks                                                                       June: R1 3×4 · R2 2×3
"""),
    tools="tools: one table, a 15-minute monthly slot, and the top five on Femke's monthly page.",
    ladder=[("risks in corridors", ["No owners.", "Found again as incidents."]),
            ("a register reviewed monthly", ["Owners, actions, triggers.", "Top five to leadership."]),
            ("risks linked to evidence", ["Near misses, game days and incidents update scores.", "Trends shown."]),
            ("risk-led planning", ["Roadmaps built from the top risks.", "Few surprises."])],
    ladder_now=1,
    baseline="Each line compares <b>risks discussed in corridors</b> to <b>a register with owners, actions and triggers, reviewed monthly</b>.",
    ratings=[(2, 3, "Big risks acted on before they hit."),
             (2, 3, "Actions with dates reduce the top risks."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Leadership sees the top five monthly."),
             (3, 3, "Neutral."),
             (2, 3, "Spending decided by risk."),
             (2, 4, "The key-person risk is named, and acted on."),
             (3, 3, "15 minutes a month.")],
    pitfalls=[("Leaving out people risks", "The biggest risk isn't on the list.", "write it, however uncomfortable."),
              ("No owner", "Everyone agrees; nothing happens.", "one owner per risk."),
              ("Scores without actions", "A ranked worry list.", "actions with dates."),
              ("Never reviewed", "Stale by summer.", "monthly, 15 minutes.")],
    use=["You carry risks in your head.", "Leadership asks what could go wrong.", "Planning a budget or a team.", "After near misses or game days."],
    skip=["Very small, stable setups: a short list in the service review may do."],
    related=["<b>Risk Register</b> (Ana, vol. 6)", "<b>What Could Happen?</b> (Sanne, vol. 5)", "<b>What About the Near Misses?</b> (vol. 2)", "<b>Who Runs What?</b> (vol. 6)"],
    quiz=[("What does each risk need?", "A cause, likelihood and impact, an owner, actions with dates, and a trigger."),
          ("What was Larder's top operational risk?", "Operations depending on two people, Eli and Bram (4 × 4)."),
          ("What's a trigger?", "A sign that makes a risk urgent, like a second phishing attempt."),
          ("Where do the top five go?", "To Femke, monthly, alongside the incident page."),
          ("How had R1 and R2 changed by June?", "R1 3 × 4 (two SREs hired), R2 2 × 3 (passkeys live).")],
    quiz_sit=[("Bram tells Eli he's thinking of leaving next year. How does that change the register?", "R1's likelihood goes up; the actions (hiring, runbooks, pairing on the hardest systems) get earlier dates, and Femke sees it in the top five. Thank Bram for saying it early.")],
    try_it="Write down the five risks you'd least like to happen in your area. Score each, give it an owner and one action with a date. Is the biggest one about people?",
    remember="Write down <span class=\"hl\">the risks you carry in your head</span>, especially the one about people, and give each an owner, an action and a trigger.",
    sources=["AXELOS, <i>ITIL 4: Risk management</i> practice guide (2020).",
             "ISO 31000:2018, Risk management guidelines (overview).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): on prioritising reliability work."],
)

# ------------------------------------------------------------------ 13 Prove It to the Auditor
ae_problem = Doodle(760, 260, "Doodle of Korenwolf's supplier questionnaire, sent on Monday 14 February 2028 for the renewed contract: 186 questions. How are changes authorised? How often are backups restored? Who reviews access? How fast are critical vulnerabilities fixed? How are incidents reviewed? A year earlier this would have meant weeks of digging through chats and memory, and answers nobody could prove.",
                    "186 questions, each asking “how do you know?” A year earlier: weeks of digging and answers nobody could prove.")
ae_problem.box(14, 30, 230, 100, "186 questions", "y", sub="Korenwolf, 14 Feb", size=20, subsize=14)
for i, t in enumerate(["changes?", "restores?", "access?", "patches?", "incidents?"]):
    ae_problem.box(264 + i * 98, 30, 90, 100, t, "paper", size=13)
ae_problem.note(380, 180, "“describe” is easy · “show evidence” is the hard part", "red", size=18)

ae_analogy = Doodle(760, 220, "Doodle of a restaurant's food-safety inspection. A good kitchen doesn't prepare for the inspector: the fridge temperatures are written on a sheet twice a day, the cleaning rota is signed, the delivery notes are filed. When the inspector comes, the evidence is already on the wall.",
                    "The good kitchen doesn't prepare for the inspector: the temperature sheet is already on the wall.")
ae_analogy.icon("fridge", 60, 40, 1.3)
ae_analogy.row([("fridge temps", "twice a day", "green"), ("cleaning rota", "signed", "green"), ("delivery notes", "filed", "green")], x=150, y=40, h=96, w=184, gap=14, size=16, subsize=14)
ae_analogy.note(450, 190, "evidence as a by-product of the work", "pen", size=18)

ae_how = Doodle(760, 400, "Larder's evidence folder, assembled from 2027 onwards as a by-product of the work. Changes: the change feed and pull requests with risk scores and reviewers. Restores: the monthly restore test log with times. Access: the quarterly access review files. Patching: nightly and monthly patch reports. Incidents: the reviews and action list. Vendors: scorecards. Security: the monitoring rules and the 9 March incident record. Continuity: plans with last-tested dates. Korenwolf's 186 questions were answered in 6 working days, each with a link to evidence, reviewed by Lena, and sent on Monday 13 March 2028. Ruben's follow-up questions: 4.",
                "Evidence collected as the work happens: changes, restores, access, patches, incidents, vendors. 186 answers in 6 days.")
for i, t in enumerate(["change feed + PRs", "restore log", "access reviews", "patch reports", "incident reviews", "vendor scorecards", "security record", "plans + test dates"]):
    r, c = divmod(i, 4)
    ae_how.box(14 + c * 186, 14 + r * 76, 172, 64, t, "green", size=14)
ae_how.row([("14 Feb", "186 questions", "y"), ("6 working days", "answered with links", "green"), ("13 Mar", "sent · 4 follow-ups", "green")], x=14, y=180, h=86, gap=40, size=17, subsize=13, arrows=True)
ae_how.note(380, 310, "reviewed by Lena · carbon answered by Ana (6 Mar)", "pen", size=16)
ae_how.note(380, 346, "the questionnaire found two gaps: vendor exits, office sign-in", "red", size=15)

AUDIT_EVIDENCE = dict(
    slug="audit-evidence",
    kicker="a.k.a. “evidence as a by-product”",
    tldr="Audits and client questionnaires don't ask what you do; they ask <b>how you know you did it</b>. If evidence is collected <b>as a by-product of the work</b> (the change feed, restore logs, access review files, patch reports, incident reviews), answering takes days and every answer has a link. If not, it takes weeks of reconstruction and some answers can't be proved. Design practices so the proof <b>falls out of doing them</b>.",
    chips=[("Family", "risk, money and vendors"), ("Lives in", "ops/evidence/ (links to logs and records); Lena's review"), ("Pairs with", "access reviews, restore tests, the change feed (vol. 2)")],
    itil=dict(groups=["general"], chain=["engage", "improve"], practices=["information security management", "measurement and reporting", "relationship management"],
              sre="(automation leaves an audit trail)", principles=["Collaborate and promote visibility", "Optimise and automate"],
              older="ITIL v3: compliance, audit and the service knowledge management system"),
    problem_side="Larder, February 2028",
    problem="""  <p class="lead">On <b>Monday 14 February</b> Korenwolf sends its supplier questionnaire for the renewed contract: <b>186 questions</b>. How are changes authorised? How often are backups restored? Who reviews access, and how often? How fast are critical vulnerabilities fixed? How are incidents reviewed? <span class="hl-pink">“Describe” is easy. The hard part is “show evidence”.</span> A year earlier this would have meant weeks of digging through chats and memory, with answers nobody could prove.</p>
  <ul>
    <li>Evidence collected for an audit is slow, partial and doubtful.</li>
    <li>Clients increasingly ask for proof, not policies.</li>
    <li>The same questions come back every year, from every client.</li>
  </ul>""",
    problem_figs=[ae_problem],
    meanwhile=[("project-6", "sustainability-in-practice", "Sanne's sustainability work answered the questionnaire's environmental part on 13 March 2028, with Ana's platform carbon figures.",
                "Eli's part of the same questionnaire: 186 questions on changes, restores, access, patching and incidents, answered from evidence in six working days.")],
    analogy_side="the kitchen inspection",
    analogy="""  <p>A good restaurant kitchen doesn't prepare for the food-safety inspector. The <b>fridge temperatures</b> are written on a sheet twice a day, the <b>cleaning rota</b> is signed, and the <b>delivery notes</b> are filed. When the inspector comes, the evidence is <b>already on the wall</b>, because it's part of how the kitchen works.</p>""",
    analogy_figs=[ae_analogy],
    map=[("The fridge temperature sheet", "The monthly restore log with times"),
         ("The signed cleaning rota", "The quarterly access review files"),
         ("Filed delivery notes", "The change feed and pull requests with risk scores"),
         ("The inspector", "Korenwolf's 186 questions"),
         ("Already on the wall", "Links in ops/evidence/, answered in six days")],
    how_side="evidence that falls out of the work, linked from one folder",
    how="""  <p>Most of Larder's practices since 2026 already leave a trail, so Eli builds <code>ops/evidence/</code> as a set of <b>links</b>, not copies:</p>
  <ul>
    <li><b>Changes</b>: the change feed, and pull requests with risk scores and reviewers.</li>
    <li><b>Restores</b>: the monthly restore test log with times.</li>
    <li><b>Access</b>: the quarterly access review files.</li>
    <li><b>Patching</b>: nightly and monthly patch reports, and the 72-hour critical record.</li>
    <li><b>Incidents</b>: reviews and the action list. <b>Vendors</b>: scorecards. <b>Security</b>: the monitoring rules and the 9 March record. <b>Continuity</b>: plans with last-tested dates.</li>
  </ul>
  <p>The <b>186 answers</b> take <b>6 working days</b>, each with a link to its evidence. Lena reviews them, Ana answers the carbon questions, and they're sent on <b>Monday 13 March</b>. Ruben comes back with only <b>4 follow-up questions</b>. The questionnaire also does Larder a favour by finding two gaps: <b>exit plans for vendors</b> and a plan for <b>losing office sign-in</b>. Both are the next notes.</p>""",
    how_figs=[ae_how],
    steps=[("List what auditors and clients ask every year", "Changes, backups, access, patching, incidents, vendors."),
           ("For each, find where the evidence already falls out", "Logs, feeds, reviews."),
           ("Fill the gaps by changing the practice", "So doing it leaves proof."),
           ("Link it from one folder", "Links, not copies."),
           ("Answer with links, reviewed by legal", "Not essays."),
           ("Turn every unprovable answer into an action", "Gaps found are gifts.")],
    vocab=[("Evidence", "A record showing a control or practice actually happened."),
           ("Control", "A practice that reduces a risk (access review, change approval)."),
           ("Supplier questionnaire", "A client's list of questions about how you run services."),
           ("Audit trail", "A chronological record of actions."),
           ("By-product evidence", "Proof created by doing the work, not prepared for an audit."),
           ("Gap", "A question you can't answer with evidence.")],
    code=dict(file="ops/evidence/README.md", note="for Korenwolf's questionnaire · sent Mon 13 March 2028", plain=True, src="""
area         question (example)                              evidence (links)
changes      How are production changes authorised?           change feed · PRs with risk score + reviewer
                                                              · emergency write-ups
backups      How often are restores tested?                   ops/continuity/restore-tests.md (monthly, timed)
access       How often is access reviewed?                    ops/security/access-reviews/2028-Q1.md
patching     How fast are critical vulnerabilities fixed?     patch reports · 72 h rule record
incidents    How are incidents reviewed?                      ops/reviews/* · ops/actions.md
vendors      How are critical suppliers managed?              ops/vendors/scorecards.md
continuity   Are continuity plans tested?                     plans with last-tested dates
gaps found   vendor exit plans (→ May) · office sign-in outage plan (→ May)

186 questions · 6 working days · reviewed by Lena · 4 follow-ups from Ruben
"""),
    tools="tools: the logs and records you already keep, one folder of links, and an hour with legal.",
    ladder=[("evidence reconstructed for each audit", ["Weeks of digging.", "Unprovable answers."]),
            ("evidence as a by-product, linked", ["Answers in days, with links.", "Gaps become actions."]),
            ("a standing trust page", ["Common answers published for clients.", "Updated automatically."]),
            ("continuous assurance", ["Controls checked by machines continuously.", "Audits confirm, not discover."])],
    ladder_now=1,
    baseline="Each line compares <b>reconstructing evidence for each questionnaire</b> to <b>evidence that falls out of the work, linked from one folder</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (1, 4, "Every answer links to proof."),
             (2, 4, "6 days instead of weeks."),
             (2, 3, "Client trust kept at renewal."),
             (3, 3, "Neutral."),
             (3, 4, "Almost no extra work once practices leave trails.")],
    pitfalls=[("Preparing evidence for the audit", "Slow, and looks like it.", "change practices so proof falls out."),
              ("Copies instead of links", "Out of date the day after.", "link to the live records."),
              ("Answering with policy prose", "“We take security seriously.”", "a link to evidence."),
              ("Hiding gaps", "Found later, by the client.", "say so, and make them actions.")],
    use=["Clients or auditors send questionnaires.", "Renewals depend on trust.", "You answer the same questions every year.", "After building new practices: check they leave a trail."],
    skip=["Nobody ever asks: but someone will."],
    related=["<b>Who Still Has Access?</b> (this volume)", "<b>Can We Actually Restore?</b> (this volume)", "<b>Was It a Change?</b> (vol. 2)", "<b>Compliance by Design</b> (Ana, vol. 5)"],
    quiz=[("What do audits really ask?", "How you know you did it: evidence, not descriptions."),
          ("What is by-product evidence?", "Proof created by doing the work (logs, feeds, review files), not prepared for an audit."),
          ("How long did the 186 answers take?", "6 working days, each with a link, reviewed by Lena."),
          ("Why links, not copies?", "Links stay current; copies are out of date the next day."),
          ("What gaps did the questionnaire find?", "Vendor exit plans and a plan for losing office sign-in.")],
    quiz_sit=[("A question asks “How do you ensure leavers lose access on their last day?” and you know agency workers were missed until February. How do you answer?", "Honestly, with evidence: the process, the Q1 review finding (9 agency accounts), the fix (agency workers on HR's form from 1 February) and the Q2 result. Clients trust an honest gap with a fix more than a perfect claim.")],
    try_it="Take the last questionnaire or audit you answered. For each answer, could you link to evidence created by the work itself? Pick the weakest one and change the practice so it leaves proof.",
    remember="Don't prepare for the auditor. Make <span class=\"hl\">the proof fall out of the work</span>, link it from one place, and turn every gap into an action.",
    sources=["AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020).",
             "ISO/IEC 27001:2022, Annex A controls (overview).",
             "AICPA, SOC 2 Trust Services Criteria (overview)."],
)

# ------------------------------------------------------------------ 14 Leaving a Vendor
ve_problem = Doodle(760, 260, "Doodle of the billing vendor's renewal in May 2028, the contract running to June. Its scorecard was amber after the 2027 silence. Cho and Marco ask: if we didn't renew, how would we leave? Nobody knows how to get all invoices and payment data out, how long it would take, or what it would cost. The vendor knows that too.",
                    "Renewal in June. “If we didn't renew, how would we leave?” Nobody knows, and the vendor knows that.")
ve_problem.box(14, 30, 230, 100, "billing vendor", "y", sub="renews June 2028", size=20, subsize=14)
ve_problem.box(264, 30, 230, 100, "scorecard", "pink", sub="amber (2027 silence)", size=20, subsize=14)
ve_problem.box(514, 30, 232, 100, "how to leave?", "paper", sub="data? time? cost?", size=20, subsize=14)
ve_problem.note(380, 180, "a vendor you can't leave sets the price", "red", size=19)

ve_analogy = Doodle(760, 220, "Doodle of renting a flat. Before signing, a careful tenant reads the notice period, takes photos of the meter readings, and keeps copies of every letter in a folder, not just in the landlord's portal. Leaving is then a month's notice and a box of papers, not a battle.",
                    "A careful tenant reads the notice period and keeps copies, so leaving is a month and a box of papers.")
ve_analogy.icon("door", 60, 40, 1.4)
ve_analogy.row([("notice period", "read before signing", "y"), ("own copies", "not only their portal", "green"), ("leaving", "a month, a box", "blue")], x=150, y=40, h=96, w=184, gap=14, size=16, subsize=13)
ve_analogy.note(450, 190, "plan the exit while you're still friends", "pen", size=18)

ve_how = Doodle(760, 400, "Larder's vendor exit plans, written in April and May 2028 for eight critical vendors. Each one page: what data we'd need and in what format, how to get it out, the steps and time to move, the cost, the alternative, and the contract terms that help or hurt. The billing vendor's exit test on Tuesday 9 May: exporting all invoices and payments was expected to take an hour and took three days, because exports were limited to 1,000 invoices per file and a full export needed a support ticket. At the June renewal Cho and Marco got a full-export API and a 90-day exit-assistance clause, and a lower price. PSP: PSP B already live. Cloud: the pilot light. WMS B: exit plan written, low readiness, accepted.",
                "One page per critical vendor: data, steps, time, cost, alternative. The billing export test took 3 days, not an hour.")
ve_how.box(14, 14, 732, 50, "data + format · how to get it out · steps + time · cost · alternative · contract terms", "blue", size=14)
for i, (v, s, f) in enumerate([("billing", "export test 9 May: 3 days (not 1 h)", "pink"), ("PSP", "PSP B already live", "green"), ("cloud", "pilot light in Paris", "green"), ("WMS B", "plan written · low readiness, accepted", "y")]):
    ve_how.box(14, 80 + i * 56, 160, 48, v, f, size=15)
    ve_how.box(184, 80 + i * 56, 562, 48, s, "paper", size=14)
ve_how.box(14, 316, 732, 50, "June renewal: full-export API + 90-day exit help + lower price", "green", size=15)
ve_how.note(380, 388, "eight critical vendors, one page each", "pen", size=15)

VENDOR_EXIT = dict(
    slug="vendor-exit",
    kicker="a.k.a. “exit plans and supplier lock-in”",
    tldr="Every critical vendor needs an <b>exit plan</b> written while you're still on good terms: what data you'd need and in what format, how to get it out, the steps and time to move, the cost, the alternative, and which contract terms help or hurt. <b>Test the riskiest step</b> (usually the data export). A tested exit plan is insurance, and the best negotiating position at renewal.",
    chips=[("Family", "risk, money and vendors"), ("Lives in", "ops/vendors/exit/&lt;vendor&gt;.md; the vendor scorecards"), ("Pairs with", "vendor silence (vol. 4), decommissioning (vol. 4), the risk register")],
    itil=dict(groups=["general"], chain=["plan", "engage"], practices=["supplier management", "risk management"],
              sre="(avoiding single points of failure in dependencies)", principles=["Think and work holistically"],
              older="ITIL v3: supplier management (contract renewal and termination)"),
    problem_side="Larder, April 2028",
    problem="""  <p class="lead">The billing vendor's contract runs to <b>June 2028</b>, and its scorecard has been <b>amber</b> since the 2027 silence. Before the renewal, Cho and Marco ask Eli: <b>if we didn't renew, how would we leave?</b> <span class="hl-pink">Nobody knows</span> how to get every invoice and payment record out, how long it would take, or what it would cost. The vendor knows that as well as Larder does.</p>
  <ul>
    <li>A vendor you can't leave sets the price and the terms.</li>
    <li>The data you'd need is in their format, behind their portal.</li>
    <li>The time to plan an exit is before you need one.</li>
  </ul>""",
    problem_figs=[ve_problem],
    analogy_side="the careful tenant",
    analogy="""  <p>Before signing a lease, a careful tenant reads the <b>notice period</b>, photographs the meter readings, and keeps <b>copies of every letter</b> in a folder of their own, not just in the landlord's portal. Then leaving is <b>a month's notice and a box of papers</b>, not a battle. Even the landlord is easier to deal with, knowing that.</p>""",
    analogy_figs=[ve_analogy],
    map=[("The notice period", "Contract terms for ending and exit help"),
         ("Own copies of letters", "Our own export of invoices and payments"),
         ("Meter readings", "The data's format and completeness"),
         ("A month and a box", "Steps, time and cost to move"),
         ("An easier landlord", "A better renewal: export API, exit clause, lower price")],
    how_side="one page per critical vendor, and a test of the riskiest step",
    how="""  <p>In <b>April and May</b>, each critical vendor's owner writes a <b>one-page exit plan</b>: what data and in what format, how to get it out, the steps and time to move, the cost, the alternative, and the contract terms that help or hurt.</p>
  <ul>
    <li><b>Billing</b> (Cho): the export test on <b>Tuesday 9 May</b> was expected to take an hour. It took <b>three days</b>: exports were limited to 1,000 invoices per file, and a full export needed a support ticket. At the <b>June renewal</b> Cho and Marco ask for a <b>full-export API</b> and a <b>90-day exit-assistance clause</b>, and get both, plus a lower price.</li>
    <li><b>PSP</b>: the exit is already live, in the form of PSP B.</li>
    <li><b>Cloud</b>: the pilot light in Paris (ADR 0026), plus infrastructure code that could rebuild elsewhere.</li>
    <li><b>WMS B</b>: plan written; readiness is low and leaving would take months. The risk is <b>accepted on purpose</b> and goes in the register.</li>
  </ul>
  <p>Eight critical vendors, eight pages. Each plan's readiness goes on that vendor's quarterly scorecard.</p>""",
    how_figs=[ve_how],
    steps=[("List critical vendors", "From the dependency maps."),
           ("Write one page each", "Data, how out, steps, time, cost, alternative, terms."),
           ("Test the riskiest step", "Usually a full data export."),
           ("Use it at renewal", "Ask for the terms the test showed you need."),
           ("Accept some lock-in on purpose", "Written in the risk register."),
           ("Review with the scorecards", "Quarterly.")],
    vocab=[("Exit plan", "How you'd move away from a vendor, written in advance."),
           ("Lock-in", "How hard and costly it is to leave a vendor."),
           ("Data portability", "Being able to get your data out in a usable format."),
           ("Exit assistance", "A contract promise that the vendor helps you leave."),
           ("Exit test", "Actually trying the riskiest step of leaving."),
           ("Accepted risk", "A risk you choose to live with, on purpose and on record.")],
    code=dict(file="ops/vendors/exit/billing.md", note="Cho · tested Tue 9 May 2028", plain=True, src="""
# Exit plan · billing SaaS                                  owner: Cho · renews Jun 2028

data needed     all invoices (≈ 41,000), payments, credit notes, VAT lines, customers
format          their CSV + PDF invoices · Peppol files for Belgium
how out         portal export: 1,000 invoices per file · full export: support ticket
exit test       Tue 9 May: expected 1 h → took 3 days (43 files + ticket)
steps + time    new vendor set-up 4–6 weeks · parallel run 1 month · cut over at month end
cost            ≈ €25k one-off + team time ≈ 30 days
alternative     two vendors shortlisted (Mar 2028)
contract asks   full-export API · 90-day exit assistance → BOTH agreed at renewal (Jun)
readiness       medium → high after renewal
"""),
    tools="tools: the contracts, a one-page template, one export test per vendor, and the scorecards.",
    ladder=[("no idea how to leave", ["Vendors set the terms.", "Data trapped."]),
            ("an exit plan per critical vendor", ["Riskiest step tested.", "Used at renewal."]),
            ("portability built in", ["Regular exports kept by Larder.", "Standard formats."]),
            ("easy to switch", ["Critical vendors have live alternatives.", "Lock-in rare and chosen."])],
    ladder_now=1,
    baseline="Each line compares <b>not knowing how to leave a vendor</b> to <b>a tested exit plan per critical vendor, used at renewal</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "A vendor failure has a known way out."),
             (3, 3, "Neutral."),
             (2, 4, "Each vendor's exit readiness on its scorecard."),
             (3, 3, "Neutral."),
             (2, 4, "Better terms and a lower price at renewal."),
             (3, 3, "Neutral."),
             (3, 3, "A page and a test per vendor.")],
    pitfalls=[("Planning the exit when you need it", "No leverage, no time.", "while you're still friends."),
              ("Assuming export works", "1,000 per file and a ticket.", "test it."),
              ("Exit plans for every tool", "Effort on things that don't matter.", "critical vendors only."),
              ("Hiding accepted lock-in", "A surprise for leadership later.", "accept it on purpose, in the register.")],
    use=["A critical vendor's contract is coming up.", "A vendor's scorecard is amber.", "Clients ask about supplier risk.", "Choosing a new vendor (ask about exit first)."],
    skip=["Tools you could replace in a day with nothing lost."],
    related=["<b>The Vendor Went Quiet</b> (vol. 4)", "<b>Switching a System Off</b> (vol. 4)", "<b>SaaS & Vendor Integration</b> (Ana, vol. 4)", "<b>Which Risks Keep Us Up at Night?</b> (this volume)"],
    quiz=[("What's in an exit plan?", "Data and format, how to get it out, steps and time, cost, alternative, contract terms."),
          ("What did the billing export test show?", "Expected an hour, took three days: 1,000 invoices per file and a support ticket for a full export."),
          ("What did Larder get at renewal?", "A full-export API, a 90-day exit-assistance clause, and a lower price."),
          ("Why is WMS B's exit risk accepted?", "Leaving would take months; Larder chose to live with it, on purpose and on record."),
          ("When should exit plans be written?", "While you're still on good terms, before you need them.")],
    quiz_sit=[("Marketing wants to sign with a new email vendor quickly. What one question do you ask before signing?", "How do we get our data (lists, consent records, history) out if we leave, and is that in the contract? It's the cheapest moment to ask.")],
    try_it="Pick your most critical vendor. Write one page: what data you'd need, how you'd get it out, how long and how much. Then try the export, today, and time it.",
    remember="Plan the exit <span class=\"hl\">while you're still friends</span>, and <span class=\"hl\">test the export</span>. A vendor you can't leave sets the price.",
    sources=["AXELOS, <i>ITIL 4: Supplier management</i> practice guide (2020).",
             "European Banking Authority, <i>Guidelines on outsourcing arrangements</i> (2019): exit strategies (as a strong example).",
             "Gregor Hohpe, <i>Cloud Strategy</i> (2020): on lock-in."],
)

# ------------------------------------------------------------------ 15 When the Office Is the Outage
oo_problem = Doodle(760, 260, "Doodle of Tuesday 16 May 2028, 08:30 to 10:40. The sign-in provider has an outage. The stores keep working: the handhelds use device certificates. But nobody in the office can sign in to anything: email, the helpdesk, the cloud console, the portal's admin. Sam's support team can't open the helpdesk for 2 hours 10 minutes while customer chats queue up. Nobody had thought of the office as something that can fail.",
                    "Stores fine. The office can't sign in to anything for 2 h 10, and support can't open the helpdesk.")
oo_problem.box(14, 30, 230, 100, "sign-in provider", "pink", sub="down 08:30–10:40", size=19, subsize=14)
oo_problem.box(264, 30, 230, 100, "stores", "green", sub="fine (device certs)", size=20, subsize=14)
oo_problem.box(514, 30, 232, 100, "office", "pink", sub="email · helpdesk · console", size=20, subsize=14)
oo_problem.note(380, 180, "Sam's team: 2 h 10 without the helpdesk", "red", size=19)

oo_analogy = Doodle(760, 220, "Doodle of a hospital where the operating theatres have backup generators and the admin office has nothing: when the power fails, surgery continues, but nobody can admit patients, phone families or find the rota. The quiet back office turns out to be on the critical path.",
                    "Theatres on generators, the admin office in the dark: surgery continues, but nobody can admit a patient.")
oo_analogy.box(14, 40, 340, 100, "theatres", "green", sub="on generators", size=19, subsize=15)
oo_analogy.box(406, 40, 340, 100, "admin office", "pink", sub="dark: no admissions", size=19, subsize=15)
oo_analogy.note(380, 190, "the back office is on the critical path too", "pen", size=18)

oo_how = Doodle(760, 400, "Larder's office continuity plan, written in the week after 16 May 2028. Sign-in, email, the office network and laptops go into the catalogue as services; support tooling moves to tier 2. Two break-glass local accounts for the helpdesk and two for the cloud console, sealed, with the same alarm as production break-glass. Laptops keep cached sign-in for 7 days. A text-message group for all office staff, outside the sign-in provider, used for status. Two 4G hotspots in the office for a network outage. A printed contact sheet. The plan joins the five continuity plans; its first test was the real outage, and its second a game day on 8 June: support back in the helpdesk in 6 minutes.",
                "The office as a service: break-glass accounts for the helpdesk, cached sign-in, a text group, hotspots. Game day: 6 minutes.")
for i, (t, s) in enumerate([("in the catalogue", "sign-in · email · network · laptops"), ("break-glass", "helpdesk ×2 · console ×2 · alarmed"), ("cached sign-in", "laptops, 7 days"),
                            ("text group", "outside the sign-in provider"), ("4G hotspots", "two in the office"), ("printed sheet", "contacts + steps")]):
    r, c = divmod(i, 3)
    oo_how.box(14 + c * 248, 14 + r * 100, 236, 86, t, "y" if r == 0 else "green", sub=s, size=17, subsize=12)
oo_how.row([("16 May", "real outage: 2 h 10", "pink"), ("8 Jun game day", "helpdesk back in 6 min", "green")], x=110, y=236, h=86, w=250, gap=40, size=17, subsize=14, arrows=True)
oo_how.note(380, 362, "support tooling moved to tier 2", "pen", size=16)

OFFICE_OUTAGE = dict(
    slug="office-outage",
    kicker="a.k.a. “workplace services continuity”",
    tldr="Sign-in, email, the office network and laptops feel like background, until they fail and the people who serve customers can't work. Treat them as <b>services</b>: put them in the catalogue with a tier, and plan for losing each one. That means <b>break-glass accounts</b> for the tools support can't be without, <b>cached sign-in</b> on laptops, a <b>way to reach staff outside your normal tools</b>, and a backup network, all tested.",
    chips=[("Family", "risk, money and vendors"), ("Lives in", "the catalogue; ops/continuity/plans/office.md"), ("Pairs with", "living plans, production access (vol. 3), the catalogue (vol. 1)")],
    itil=dict(groups=["service", "technical"], chain=["design", "deliver"], practices=["service continuity management", "infrastructure and platform management", "service catalogue management"],
              sre="(dependencies of the people who respond)", principles=["Think and work holistically"],
              older="ITIL v3: ITSCM for end-user services"),
    pager=dict(when="Tue 16 May 2028 · Bram on call", lines=[
        ("08:30", "sign-in provider: status “major outage”"),
        ("08:34", "Sam: nobody can open the helpdesk · chats queueing"),
        ("08:40", "stores: all normal (device certificates)"),
        ("08:45", "Bram: cloud console unreachable too · break-glass for production only"),
        ("09:30", "Sam's team answers chats from a phone app with a cached session"),
        ("10:40", "provider recovers · ≈ 210 chats waited · avg 38 min")]),
    problem_side="Larder, Tuesday 16 May 2028",
    problem="""  <p class="lead">At <b>08:30</b> the sign-in provider has an outage that lasts until <b>10:40</b>. The <b>stores keep working</b>: the handhelds use device certificates. But <b>nobody in the office can sign in to anything</b>: email, the helpdesk, the cloud console, the portal's admin. <span class="hl-pink">Sam's support team can't open the helpdesk for 2 hours 10 minutes</span> while about 210 customer chats queue up. Korenwolf's questionnaire had asked about this in March, and it was one of the two gaps.</p>
  <ul>
    <li>The office wasn't in the catalogue, so it had no tier and no plan.</li>
    <li>The production break-glass account didn't help support.</li>
    <li>There was no way to tell office staff what was happening, because every channel needed sign-in.</li>
  </ul>""",
    problem_figs=[oo_problem],
    analogy_side="the hospital's dark admin office",
    analogy="""  <p>A hospital puts its <b>operating theatres on backup generators</b> and leaves the <b>admin office</b> on the mains. When the power fails, surgery continues, but nobody can admit patients, phone families or find the rota. The quiet back office turns out to be <b>on the critical path</b> too.</p>""",
    analogy_figs=[oo_analogy],
    map=[("Theatres on generators", "Stores on device certificates"),
         ("The dark admin office", "The office unable to sign in"),
         ("Nobody can admit patients", "Support can't open the helpdesk"),
         ("A generator for the office", "Break-glass helpdesk accounts, cached sign-in"),
         ("Phoning staff another way", "A text group outside the sign-in provider")],
    how_side="the office as a service, with its own plan",
    how="""  <p>In the week after, Sam and Eli write the <b>office continuity plan</b>:</p>
  <ul>
    <li><b>In the catalogue</b>: sign-in, email, the office network and laptops become services with owners. <b>Support tooling moves to tier 2</b>, because an hour without it costs customers.</li>
    <li><b>Break-glass</b>: two sealed local accounts for the helpdesk and two for the cloud console, with the same alarm as production break-glass.</li>
    <li><b>Cached sign-in</b>: laptops keep a cached sign-in for <b>7 days</b>, so they can unlock without the provider.</li>
    <li><b>Reaching people</b>: a <b>text-message group</b> for all office staff, outside the sign-in provider, used for status updates.</li>
    <li><b>Network</b>: two <b>4G hotspots</b> in the office, and a <b>printed sheet</b> of contacts and steps.</li>
  </ul>
  <p>The plan becomes the fifth continuity plan. Its first test was the real outage. Its second is a <b>game day on 8 June</b>, with the sign-in provider blocked for the support team on purpose: they're back in the helpdesk in <b>6 minutes</b>.</p>""",
    how_figs=[oo_how],
    steps=[("Put workplace services in the catalogue", "Sign-in, email, network, laptops."),
           ("Tier them by what an hour costs", "Support tooling may be tier 2."),
           ("Give critical tools a break-glass path", "Sealed, alarmed, tested."),
           ("Make devices work offline for a while", "Cached sign-in."),
           ("Have a channel outside your own tools", "To tell staff what's happening."),
           ("Test it with a game day", "Block the dependency on purpose.")],
    vocab=[("Workplace services", "Sign-in, email, network, laptops: the tools staff need to work."),
           ("Identity provider", "The service that signs people in to everything else."),
           ("Single sign-on dependency", "When one sign-in service failing blocks every tool."),
           ("Cached credentials", "A device remembering a recent sign-in, to work offline."),
           ("Out-of-band channel", "A way to communicate that doesn't depend on the failing systems."),
           ("Break-glass (workplace)", "An emergency account for a critical tool, outside normal sign-in.")],
    code=dict(file="ops/continuity/plans/office.md", note="after 16 May 2028 · owner Sam · tested 8 Jun", plain=True, src="""
# Office + sign-in down                                            owner: Sam

trigger      sign-in provider, email or office network down > 15 min
who decides  Sam (support) · Eli (IT) · Femke informed
steps        1 status to office staff: SMS group "Larder office" (outside SSO)
             2 support: helpdesk break-glass accounts (vault envelope, 2 keyholders)
                → alarm to Eli · log every use
             3 laptops: cached sign-in (7 days) · 4G hotspots × 2 if network down
             4 printed sheet: contacts, vendors' lines, these steps
switch back  provider up → normal sign-in · break-glass passwords rotated same day
tests        16 May 2028 (real, 2 h 10) · 8 Jun game day: helpdesk back in 6 min
catalogue    sign-in, email, office network, laptops added · support tooling → tier 2
"""),
    tools="tools: the catalogue, break-glass accounts in the vault, the laptops' cached sign-in setting, an SMS group, two 4G hotspots, a printer.",
    ladder=[("the office as background", ["No tier, no plan.", "One sign-in failure stops everyone."]),
            ("the office as a service", ["Break-glass for support tools.", "Out-of-band channel. Tested."]),
            ("resilient sign-in", ["A second sign-in path for critical tools.", "Devices offline-capable by design."]),
            ("no single sign-in point", ["Workplace services can fail without stopping support.", "Rare drills suffice."])],
    ladder_now=1,
    baseline="Each line compares <b>the office as background</b> to <b>workplace services in the catalogue with a tested plan</b>.",
    ratings=[(2, 4, "Customers answered within minutes in the next outage."),
             (3, 3, "Neutral: the provider fails as often as before."),
             (1, 4, "2 h 10 → 6 minutes for support."),
             (3, 3, "Neutral."),
             (2, 4, "Workplace services visible in the catalogue."),
             (3, 3, "Neutral."),
             (3, 3, "Two hotspots and some setup."),
             (3, 3, "Neutral."),
             (3, 3, "A week to set up.")],
    pitfalls=[("Only planning for production", "The people who respond can't work.", "the office is a service too."),
              ("Break-glass only for production", "Support stays locked out.", "break-glass for critical support tools."),
              ("Communicating through the failed tool", "Status updates by email during an email outage.", "an out-of-band channel."),
              ("Never testing", "Cached sign-in turned off by a policy change.", "a game day.")],
    use=["Everyone signs in through one provider.", "Support or operations work from an office.", "A questionnaire asks about workplace continuity.", "After any outage of email or sign-in."],
    skip=["Fully separate tools with separate sign-in (rare today)."],
    related=["<b>The Plan Nobody Has Read</b> (this volume)", "<b>Who May Touch Production?</b> (vol. 3)", "<b>Identity Federation & SSO</b> (Ana, vol. 4)", "<b>What Do We Run, and Who Owns It?</b> (vol. 1)"],
    quiz=[("Why did the stores keep working on 16 May?", "The handhelds sign in with device certificates, not the sign-in provider."),
          ("What couldn't support do, and for how long?", "Open the helpdesk, for 2 hours 10 minutes."),
          ("What's an out-of-band channel?", "A way to reach people that doesn't depend on the failing systems (an SMS group)."),
          ("What changed in the catalogue?", "Sign-in, email, network and laptops added; support tooling moved to tier 2."),
          ("What did the 8 June game day show?", "Support back in the helpdesk in 6 minutes using break-glass.")],
    quiz_sit=[("The office's internet line fails at 09:00 on a Monday. What happens under the plan?", "Sam declares it after 15 minutes, the SMS group gets a status, the two 4G hotspots go on for support first, and the line provider is called from the printed sheet.")],
    try_it="Imagine your sign-in provider is down for two hours. Which of your teams can still work? How would you tell them what's happening? Write the three steps that would get your support team working again.",
    remember="The <span class=\"hl\">office is a service</span> too. Plan for losing sign-in and email, and keep <span class=\"hl\">one channel outside your own tools</span>.",
    sources=["AXELOS, <i>ITIL 4: Service continuity management</i> practice guide (2020).",
             "Microsoft and others' guidance on resilient identity (break-glass accounts).",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): dependencies of incident response."],
)

NOTES = [CLOUD_COSTS, OPS_RISK, AUDIT_EVIDENCE, VENDOR_EXIT, OFFICE_OUTAGE]
