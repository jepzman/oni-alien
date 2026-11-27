# Series 5 · On the Client's Floor · Vol. 3 · Digging Up the Legacy · Bad news, honestly (notes 9–12).
from datetime import date


def on_site(d):
    return f"day {(d - date(2027, 7, 4)).days} on site"


# ------------------------------------------------------------------ 09 What Do We Say When Discovery Changes Everything?
dr_problem = Doodle(760, 240, "Doodle of six discovery findings on sticky notes: 31 per cent of addresses fail; the 02:10 job has 14 steps and two hidden ones; 37 per cent of MAVIS never runs; change capture needs a licence; the billing interface had six undocumented behaviours; the security review started late. Callum's first draft of the report is 112 pages, with the findings on page 71.",
                    "Six findings. Callum's first draft: 112 pages, with the bad news on page 71.", exact=True)
for i, t in enumerate(["31 % addresses", "02:10: 14 steps", "37 % dead code", "CDC licence", "6 billing quirks", "security late"]):
    dr_problem.box(14 + (i % 3) * 150, 20 + (i // 3) * 80, 140, 66, t, "y" if i else "pink", size=15)
dr_problem.box(480, 20, 266, 146, "draft 1", "paper", sub="112 pages · findings p. 71", size=22, subsize=15)
dr_problem.note(380, 214, "the people who decide will read two pages", "red", size=20)

dr_how = Doodle(760, 340, "The discovery report as delivered on 14 December. Two pages up front: what we found, in six numbered findings with numbers; what it means for the plan and the price; three options, A, B and C, each with cost, date and risk; and a recommendation, option B. Behind it, 38 pages of evidence, one section per finding, and appendices. Bert is credited on page one.",
                "Two pages: findings, what they mean, priced options, a recommendation. Evidence behind.", exact=True)
dr_how.box(14, 14, 360, 280, None, "y", rx=6)
dr_how.head(194, 44, "pages 1–2", size=20)
for i, t in enumerate(["1 · six findings, with numbers", "2 · what they mean", "3 · options A / B / C, priced", "4 · recommendation: B", "credit: Bert Ogundipe"]):
    dr_how.text(34, 84 + i * 40, t, anchor="start", size=17)
dr_how.box(400, 14, 346, 280, None, "paper", rx=6)
dr_how.head(573, 44, "pages 3–40", size=20)
for i, t in enumerate(["evidence, per finding", "profile, traces, spikes", "the golden master", "appendices"]):
    dr_how.text(420, 84 + i * 40, t, anchor="start", size=17)
dr_how.note(380, 324, "if they read only page 1, they know what we know", "pen", size=19)

DISCOVERY_REPORT = dict(
    slug="discovery-report", date=date(2027, 12, 14), meta=on_site(date(2027, 12, 14)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. “the discovery report”, deliverable D4",
    tldr="A discovery report exists to change decisions, and the people who decide will read two pages. Put the <b>findings first, with numbers</b>; then <b>what they mean</b> for the plan and the price; then <b>priced options</b> and a <b>recommendation</b>. The evidence goes behind, one section per finding. Credit the people who helped. If the report doesn't change anything, either discovery didn't look or the report didn't say.",
    chips=[("Family", "bad news, honestly"), ("Lives in", "discovery/D4-discovery-report-v1.0.pdf"), ("Pairs with", "profiling the data, the honest change request")],
    problem_side="The Grid, room 27A, 14 December 2027",
    problem="""  <p class="lead">Discovery ended on <b>10 December</b>. The report, deliverable <b>D4</b>, goes to the steering committee on <b>Tuesday 14 December</b>. It has six findings, and the first one is <b>31 %</b>.</p>
  <ul>
    <li>Callum's first draft is <b>112 pages</b>: method, interviews, every table. The findings start on <b>page 71</b>.</li>
    <li>Priya will read two pages. Rupert's delegate, one. Oliver Thane will read all of it, looking for weak points.</li>
    <li><span class="hl-pink">The draft doesn't say what Wrenfield recommends.</span> Callum thought that would “look like selling”.</li>
  </ul>""",
    problem_figs=[dr_problem],
    sides=dict(client=("Priya and the steering", "<p>MetroVolt paid £380k to find out what's really in MAVIS. The steering committee needs to decide one thing: <b>what now?</b> It wants the facts, what they cost, and the vendor's honest advice, in that order, and short.</p>", "Tell me what you found and what you'd do."),
                vendor=("Ines and Callum", "<p>Wrenfield needs a report that's <b>impossible to dispute</b> and <b>easy to act on</b>, without looking like a sales document for more money. Callum's instinct is to prove the effort; Ines's is to prove the findings.</p>", "Page one should be enough to decide.")),
    sides_after="A recommendation isn't selling. Refusing to give one, after being paid to look, is a kind of hiding.",
    analogy_side="the house survey",
    analogy="""  <p>A good building survey starts with a <b>one-page summary</b>: “roof sound; damp in the cellar, about £6,000 to fix; wiring needs replacing within five years.” Then the options and the surveyor's advice. The fifty pages of photos and readings come after, for anyone who wants to check. A survey that starts with the methodology is a survey nobody reads.</p>""",
    map=[("The one-page summary", "Pages 1–2: findings, meaning, options, recommendation"),
         ("“Damp in the cellar, £6,000”", "“31 % of addresses fail; A1-07 prices it at £247k”"),
         ("The surveyor's advice", "Recommendation: option B"),
         ("Fifty pages of photos", "38 pages of evidence"),
         ("Starting with methodology", "Callum's 112-page draft")],
    how_side="findings first, meaning, priced options, a recommendation",
    how="""  <p>Ines rewrites the front: <b>two pages</b> that stand alone.</p>
  <ul>
    <li><b>Findings</b>, numbered, each with a number: 31 % of wave 1 addresses fail; the 02:10 job has 14 steps, two undocumented; 37 % of MAVIS never runs; change capture needs a licence; the billing spec missed six behaviours (now fixed in v1.2); the security review started late.</li>
    <li><b>What they mean</b>: the baseline dates and price can't hold; three assumptions (A1-07, X-02, D-03) are affected; the rest of the design stands.</li>
    <li><b>Three options</b>, each with cost, date and risk. <b>A</b>: as planned, with cleansing at A1-07's rate (+£1.1m, +4 months). <b>B</b>: MetroVolt's own team cleanses a share, portal moved to wave 2 (less cost, +3 months). <b>C</b>: a smaller wave 1 (190,000 accounts) on the original date.</li>
    <li><b>A recommendation</b>: B, with one sentence why.</li>
  </ul>
  <p>Behind it, <b>38 pages of evidence</b>, one section per finding. Bert is credited by name on page one. The 112-page draft becomes the appendix. Oliver Thane reads all of it and finds two typos.</p>""",
    how_figs=[dr_how],
    steps=[("Write the two front pages first", "Then build the evidence behind them."),
           ("Number the findings, each with a number", "No adjectives without data."),
           ("Say what they mean", "For the plan, the price, the assumptions."),
           ("Give priced options", "Cost, date and risk for each."),
           ("Recommend one", "One sentence why."),
           ("Credit the people who helped", "By name, on page one.")],
    vocab=[("Discovery report", "The findings of a discovery phase and their consequences."),
           ("Executive summary", "The pages that stand alone for decision makers."),
           ("Finding", "A fact discovered, stated with evidence."),
           ("Option", "A possible course of action, with its cost, time and risk."),
           ("Recommendation", "The option the author advises, and why."),
           ("Pyramid principle", "Lead with the answer; support it with the reasons below.")],
    code=dict(file="discovery/D4-front-pages.md", note="v1.0 · Tue 14 Dec 2027", src="""
LODESTAR DISCOVERY REPORT (D4) · pages 1–2                with thanks to Bert Ogundipe

FINDINGS
F1  31 % of wave 1 customer records fail the address check (117,800 of 380,000)
F2  the 02:10 job has 14 steps; ADDRFIX (2003) and COPYMTR are undocumented
F3  37 % of MAVIS programs never ran in 12 months; 61 touch addresses
F4  change capture: log capture for 9 tables needs a licence (≈ £85k/yr)
F5  the billing spec missed 6 behaviours → fixed in v1.2 (2 Nov)
F6  security and data-protection review started late (week 14 of 12 planned)
MEANING   baseline v1.0 dates and price cannot hold · A1-07, X-02 affected
OPTIONS          cost      wave 1 date      risk
  A as planned   +£1.1m    +4 months        lowest delivery risk, highest cost
  B shared       ≈ +£0.7m  +3 months        MetroVolt cleanses ≈ 40 %; portal → wave 2
  C smaller      +£0.3m    24 Jun 2028      190,000 accounts only; wave 2 doubles
RECOMMENDATION  B: it fixes the data where it lives, with the people who'll keep it clean
"""),
    contract=dict(side="what D4 is for", doc="Lodestar SOW · Schedule 3, D4 · §4.2.4", date="signed 30 June 2027", stamp="D4",
                  clauses=[("D4", "A discovery report setting out findings, their effect on the Assumptions, and options.", "“and options”. a report without options doesn't meet the deliverable."),
                           ("4.2.4", "Milestone dates will be re-baselined at the end of discovery by agreement.", "this report is the start of that agreement.")],
                  plain="the contract usually defines what the discovery report must contain. Findings without options don't meet it; options without a recommendation leave the client to guess what you think."),
    health=dict(now="a",
                g=("trust is high", ["Walk the sponsor through it before steering.", "Options discussed openly.", "Decide quickly."]),
                a=("bad news in a cut year", ["Two pages that stand alone.", "Numbers, not adjectives.", "A clear recommendation."]),
                r=("a reviewer looking for holes", ["Every finding traceable to evidence.", "No claim without a number.", "Let them find typos, not gaps."])),
    pressure=dict(level=4, title="the report", cost="112 pages cut to 2 · a recommendation that costs money",
                  items=["Recommending the option that costs MetroVolt more feels like selling. Recommending nothing feels safer and helps nobody.", "Callum's 112 pages were real work. They're the appendix; tell him that's where the proof lives."]),
    baseline="Each line compares <b>a 112-page report with findings on page 71</b> with <b>two front pages of findings, meaning, priced options and a recommendation</b>.",
    ratings=[(3, 5, "Priya can decide from page 1."),
             (3, 3, "Hard to write, easier to present."),
             (3, 4, "Options priced from the contract's own rates."),
             (3, 4, "Affected assumptions named."),
             (3, 4, "The design that stands is said to stand."),
             (2, 5, "Every risk is on page 1."),
             (3, 5, "Evidence behind every finding."),
             (3, 3, "A week of rewriting."),
             (4, 4, "Two pages to maintain.")],
    pitfalls=[("Methodology first", "Findings on page 71.", "findings first."),
              ("Adjectives without numbers", "“Significant data issues.”", "31 %, 117,800 records."),
              ("No recommendation", "The client has to guess.", "recommend one, say why."),
              ("Unpriced options", "Nobody can choose.", "cost, date and risk for each."),
              ("No credit to helpers", "The client's expert feels used.", "name them on page one.")],
    use=["The end of any discovery or assessment.", "Findings that change price or plan.", "Readers who won't read past page two."],
    skip=["Never skip the front pages; the evidence can be short if the findings are small."],
    related=["<b>How Bad Is the Data, Really?</b> (this volume)", "<b>How Do We Tell Them It's Worse Than They Think?</b> (next note)", "<b>How Do We Ask for More Money Honestly?</b> (this volume)", "<b>Where Are We, Really?</b> (Sanne, vol. 2)"],
    quiz=[("What goes on the first two pages?", "Findings with numbers, what they mean, priced options and a recommendation."),
          ("Why recommend an option?", "The client paid to learn what you know; refusing to advise is a kind of hiding."),
          ("What were options A, B and C?", "A: as planned with full cleansing; B: MetroVolt cleanses a share and the portal moves to wave 2; C: a smaller wave 1 on the original date."),
          ("What does the contract say D4 must contain?", "Findings, their effect on the assumptions, and options."),
          ("Where did the 112-page draft go?", "Into the appendix, as evidence.")],
    quiz_sit=[("Oliver Thane says option B is “the vendor protecting its margin”. How do you answer at steering?", "Show the numbers: B costs MetroVolt less than A and fixes the data where it lives; Wrenfield's margin is lower under B. Offer the pricing workings to anyone who wants them.")],
    try_it="Take a report you've written or must write. Write its first two pages alone: findings with numbers, what they mean, options with prices, and your recommendation. Could someone decide from those pages?",
    remember="Findings first, <span class=\"hl\">with numbers</span>. Options, <span class=\"hl\">with prices</span>. And say what you'd do.",
    late=dict(when="Tue 14 December 2027 · 22:15 · hotel near The Grid",
              lines=["Two pages. Six findings. Three options. One recommendation. Bert's name on page one.",
                     "Priya read page one twice and asked for B's details by Friday. That's a decision starting.",
                     "Oliver found two typos. Only two. Callum framed them."]),
    sources=["Barbara Minto, <i>The Pyramid Principle</i> (1987).",
             "Peter Block, <i>Flawless Consulting</i> (2011): feedback and the decision meeting.",
             "Gerald Weinberg, <i>The Secrets of Consulting</i> (1985)."],
)

# ------------------------------------------------------------------ 10 How Do We Tell Them It's Worse Than They Think?
bn_problem = Doodle(760, 240, "Doodle of the wrong way: the discovery report emailed to eleven steering members on a Friday evening, landing in Priya's inbox at the same moment as Lord Varnish's and Oliver Thane's. Priya reads 31 per cent on her phone at a school concert.",
                    "The wrong way: eleven inboxes, one Friday evening, a school concert.", exact=True)
bn_problem.icon("envelope", 40, 50, 1.6)
for i in range(11):
    bn_problem.box(160 + (i % 6) * 96, 40 + (i // 6) * 70, 84, 54, None, "pink" if i == 0 else "paper", rx=4)
bn_problem.note(202, 158, "Priya", "red", size=15)
bn_problem.note(380, 214, "the owner of the data hears it with everyone else", "red", size=19)

bn_how = Doodle(760, 320, "The order in which Ines told the bad news, between 8 and 14 December. First Bert, to check the facts and so he isn't surprised by findings about his system. Then Elaine, at the Thursday 08:00 coffee. Then Priya and Nkem, who own the data and the money, in person. Then Hollis, about the 02:10 job and the design. Then Kofi, about the meter feed. Only then the steering committee on 14 December, where nobody hears it for the first time.",
                "Experts, then the counterpart, then the owners, then everyone. Nobody hears it first at steering.", exact=True)
seq = [("Bert", "8 Dec · facts", "y"), ("Elaine", "9 Dec · 08:00", "green"), ("Priya + Nkem", "9 Dec · 14:00", "pink"), ("Hollis", "10 Dec", "blue"), ("Kofi", "10 Dec", "paper"), ("steering", "14 Dec", "y")]
for i, (h, sub, fill) in enumerate(seq):
    bn_how.box(14 + i * 124, 30, 114, 90, h, fill, sub=sub, size=16, subsize=13)
    if i:
        bn_how.arrow(14 + i * 124 - 10, 75, 14 + i * 124 - 1, 75)
bn_how.box(14, 160, 732, 110, "each conversation", "paper", sub="in person · the number · the evidence · what it means · no blame · what we propose", size=19, subsize=15)

BAD_NEWS = dict(
    slug="delivering-bad-news", date=date(2027, 12, 9), meta=on_site(date(2027, 12, 9)), where="FL 2", pass_kind="contractor",
    kicker="a.k.a. “pre-wiring” bad news",
    tldr="Bad news delivered badly becomes a fight about how it was delivered. Tell it <b>in person</b>, in the <b>right order</b>: the <b>expert</b> first (check the facts, no surprises about their system), then your <b>counterpart</b>, then the people who <b>own</b> the problem, then everyone else. Bring <b>the number</b>, the <b>evidence</b>, what it <b>means</b> and what you <b>propose</b>, and no blame. Nobody important should hear it first in a meeting.",
    chips=[("Family", "bad news, honestly"), ("Lives in", "Ines's notebook: the telling order"), ("Pairs with", "the discovery report, the client counterpart (vol. 2)")],
    problem_side="The Grid, 8–14 December 2027",
    problem="""  <p class="lead">The discovery report goes to the steering committee on <b>14 December</b>. Its first line is <b>31 %</b>. Callum's plan: email the report to all eleven steering members on Friday 10 December, “so they have time to read it”.</p>
  <ul>
    <li>Priya would read it on her phone, the same evening as Lord Varnish and Oliver Thane. <span class="hl-pink">The data is hers.</span></li>
    <li>Bert would learn from a report that “37 % of MAVIS never runs” and that a 2003 fix corrupts postcodes.</li>
    <li>Kofi would learn that his meter system depends on a hidden step, from a document his boss Gareth reads at the same time.</li>
  </ul>""",
    problem_figs=[bn_problem],
    sides=dict(client=("Priya", "<p>Priya owns Customer Operations' data. Hearing that a third of it is wrong is bad. Hearing it at the same time as Lord Varnish and the Vexmoor partner, without a chance to think, is <b>humiliating</b>, and in a Horizon year it's dangerous.</p>", "Let me hear it first, from you, in a room."),
                vendor=("Ines", "<p>Ines needs the findings accepted, not fought. That depends less on the numbers than on <b>who hears them first and how</b>. An email to eleven people is the fastest way to make Priya defend her data instead of fixing it.</p>", "The order of telling is part of the message.")),
    sides_after="People forgive bad news. They don't forgive being the last to know about their own area.",
    analogy_side="a doctor's diagnosis",
    analogy="""  <p>A doctor with bad test results doesn't email them to the whole family. She <b>checks the results with the lab</b>, tells the <b>patient first</b>, in a room, with time, the facts and a plan, and lets the patient decide who else to tell and when. The facts are the same either way. The order changes everything about what happens next.</p>""",
    map=[("Checking with the lab", "Bert checks the findings about MAVIS"),
         ("The patient first, in a room", "Priya and Nkem, in person"),
         ("Time, facts and a plan", "The number, the evidence, the options"),
         ("Letting them decide who else to tell", "Priya chooses how to present it to Rupert"),
         ("Emailing the whole family", "The report to eleven inboxes on a Friday")],
    how_side="the expert, the counterpart, the owners, then everyone",
    how="""  <p>Ines replaces the Friday email with a <b>telling order</b>, over six days:</p>
  <ul>
    <li><b>Bert</b>, Wednesday 8 December: every finding about MAVIS, to check facts. He corrects one number and asks that ADDRFIX be described as “a 2003 fix that outlived its lookup table”, which is fairer.</li>
    <li><b>Elaine</b>, Thursday 08:00 at the café: the whole picture, under the no-surprises pact.</li>
    <li><b>Priya and Nkem</b>, Thursday 14:00, in Priya's office: the data is theirs and so is the money. Bilal shows thirty failing records on screen. Priya asks for an hour alone, then calls Ines back: “Option B. And I want to tell Rupert myself.”</li>
    <li><b>Hollis</b>, Friday: the 02:10 job, change capture, the design. <b>Kofi</b>, Friday: COPYMTR, before Gareth reads it.</li>
    <li><b>The steering committee</b>, Tuesday 14 December. Nobody hears 31 % there for the first time. Priya presents finding 1 herself.</li>
  </ul>
  <p>In every conversation: the number, the evidence, what it means, no blame, and what Wrenfield proposes.</p>""",
    how_figs=[bn_how],
    steps=[("List who owns each finding", "Data, money, systems, teams."),
           ("Check facts with the expert first", "And let them shape fair wording."),
           ("Tell your counterpart early", "No surprises."),
           ("Tell owners in person", "The number, evidence, meaning, proposal."),
           ("Let owners tell their bosses", "If they want to."),
           ("Only then the big meeting", "Where nobody hears it first.")],
    vocab=[("Pre-wiring", "Talking to key people individually before a meeting."),
           ("Problem owner", "The person whose area the bad news concerns."),
           ("Telling order", "The sequence in which people hear bad news."),
           ("Blameless framing", "Describing causes as conditions, not as people's failures."),
           ("Face", "A person's standing in front of others; easy to damage in public."),
           ("Escalation by surprise", "When a boss hears bad news before the owner does.")],
    code=dict(file="notebook/telling-order-D4.md", note="Ines's notebook · Wed 8 Dec 2027", src="""
TELLING ORDER · DISCOVERY FINDINGS (D4)

who            when               owns            what / how
Bert           Wed 8 Dec, 11:00   MAVIS facts     every finding about MAVIS; fair wording
Elaine         Thu 9 Dec, 08:00   the programme   all six; café; no-surprises pact
Priya + Nkem   Thu 9 Dec, 14:00   data + money    F1 with 30 records on screen; options
Hollis         Fri 10 Dec, 10:00  architecture    F2, F4, F5; design impact
Kofi           Fri 10 Dec, 15:00  meter feed      COPYMTR (before Gareth reads D4)
steering       Tue 14 Dec, 10:00  decisions       report sent Mon 13 Dec, 17:00
each time: the number · the evidence · what it means · no blame · our proposal
Priya: "Option B. And I'll tell Rupert myself."   (she did, Mon 13 Dec)
"""),
    contract=dict(side="the contract's view of bad news", doc="Lodestar SOW · Schedule 7, §6 (early warning)", date="v1.1 · Aug 2027", stamp="early warning",
                  clauses=[("6.1", "Each Party shall notify the other promptly of any matter which could increase the Charges, delay a Milestone or impair performance.", "“promptly” and “notify” don't say “by email to everyone”."),
                           ("6.3", "The Parties shall meet within 5 Working Days of an early warning to consider how to avoid or reduce its effect.", "the Thursday meetings were 6.3, early.")],
                  plain="contracts usually require early warning of anything that could change cost or time. How you warn is up to you; a meeting with the owner meets the clause and the relationship."),
    health=dict(now="a",
                g=("trust is high", ["Short version of the order.", "Owner first, still.", "Then the meeting."]),
                a=("bad news in a political year", ["Expert, counterpart, owners, everyone.", "In person, with evidence.", "Let owners tell their bosses."]),
                r=("factions waiting to use it", ["Same order, faster.", "Written summary the same day as the talks.", "Nobody hears it first in the meeting."])),
    pressure=dict(level=4, title="the telling", cost="six conversations in six days · one person's data called wrong",
                  items=["Telling someone their data is a third wrong is hard. Bring the thirty records, not adjectives, and let them see it themselves.", "Asking for an hour alone isn't rejection. Priya came back with a decision."]),
    baseline="Each line compares <b>emailing the report to eleven people on a Friday</b> with <b>a telling order: expert, counterpart, owners, then the meeting</b>.",
    ratings=[(2, 5, "Priya presented finding 1 herself."),
             (3, 3, "Six hard conversations, but no fights."),
             (3, 4, "Option B chosen before steering."),
             (3, 3, "Neutral."),
             (3, 4, "Bert's fairer wording made the report more accurate."),
             (2, 4, "No surprise reactions at steering."),
             (3, 4, "Early warning met, in person and in writing."),
             (3, 2, "Six days instead of one email."),
             (3, 3, "A plan to write each time.")],
    pitfalls=[("Email to everyone at once", "The owner learns with their boss.", "owners first, in person."),
              ("Skipping the expert", "A wrong fact, or an insulted colleague.", "check with them first."),
              ("Blame in the wording", "“Corrupted by a bad fix.”", "conditions, not people."),
              ("Telling the boss first", "Escalation by surprise.", "let the owner tell their boss."),
              ("Surprises at the meeting", "The meeting becomes a fight.", "nobody hears it there first.")],
    grimoire=[(1, "meeting-before-the-meeting", "The Meeting Before the Meeting", "is the same skill from inside MetroVolt: Priya and Gareth by the coffee machine.")],
    use=["Any finding that hurts someone's area, budget or pride.", "Before a big meeting.", "When the audience includes rivals."],
    skip=["Emergencies, where speed matters more than order: tell everyone at once, then follow up in person."],
    related=["<b>What Do We Say When Discovery Changes Everything?</b> (previous note)", "<b>How Do We Earn the Programme Director's Trust?</b> (vol. 2)", "<b>How Do We Keep Them With Us?</b> (Sanne, vol. 5)", "<b>How Do We Ask for More Money Honestly?</b> (next note)"],
    quiz=[("Why tell the expert first?", "To check the facts and agree fair wording, so they aren't surprised about their own system."),
          ("Who owns finding 1, and how were they told?", "Priya and Nkem (data and money), in person, with thirty failing records on screen."),
          ("Why let Priya tell Rupert herself?", "It protects her standing; she presents bad news as a leader, not as its victim."),
          ("What's in each conversation?", "The number, the evidence, what it means, no blame, and a proposal."),
          ("What's the rule for the big meeting?", "Nobody important hears the bad news there for the first time.")],
    quiz_sit=[("Lord Varnish hears a rumour about “31 %” before Priya has told Rupert, and emails Ines directly. What do you do?", "Reply briefly that the findings are being reviewed with the sponsor and will be at steering on the 14th, and tell Priya at once so she can speak to Rupert and Lord Varnish first.")],
    try_it="Think of a piece of bad news you need to deliver. List everyone affected, mark who owns it, and write the telling order. Who should hear it first, and what will you bring?",
    remember="The order of telling is <span class=\"hl\">part of the message</span>. Nobody should hear bad news about <span class=\"hl\">their own area</span> last.",
    late=dict(when="Thu 9 December 2027 · 21:30 · hotel near The Grid",
              lines=["Priya asked for an hour alone. Longest hour of the project. Then: “Option B. And I'll tell Rupert myself.”",
                     "Bert changed one word about ADDRFIX. It was fairer. It's in the report.",
                     "Callum's Friday email would have been faster. It would also have been the end of us."]),
    sources=["Douglas Stone, Bruce Patton and Sheila Heen, <i>Difficult Conversations</i> (1999).",
             "Peter Block, <i>Flawless Consulting</i> (2011): the feedback meeting.",
             "Robert Buckman, <i>How to Break Bad News</i> (1992): the SPIKES approach."],
)

# ------------------------------------------------------------------ 11 How Do We Ask for More Money Honestly?
cr_problem = Doodle(760, 240, "Doodle of change request CR-007, submitted on 14 December: 1.1 million pounds and four months more. Next to it, a thought bubble over Elaine: Orion's vendor did this too. And a voice from Graham in Leeds: ask for 1.5 million, they'll negotiate down.",
                    "CR-007: £1.1m and four months. Elaine thinks “Orion”. Graham says “ask for £1.5m”.", exact=True)
cr_problem.box(250, 40, 260, 120, "CR-007", "pink", sub="+£1.1m · +4 months", size=26, subsize=17)
cr_problem.box(14, 60, 200, 80, "Elaine", "paper", sub="“Orion did this”", size=18, subsize=15)
cr_problem.box(546, 60, 200, 80, "Graham", "paper", sub="“ask for £1.5m”", size=18, subsize=15)
cr_problem.note(380, 210, "the temptation is to pad it; the cure is to show every line", "red", size=18)

cr_how = Doodle(760, 360, "CR-007 built line by line from the contract. Data cleansing above A1-07: 26 points at 9,500 pounds each, 247,000. Replacing steps 9 and 12 of the 02:10 job, outside exclusion X-02: 310,000. Change capture licence and mainframe work: 180,000. Extra reconciliation and exception tooling: 363,000. Total 1.1 million, four months. Agreed on 11 February at 700,000 and three months: MetroVolt's team cleanses about 40 per cent, minus 99,000; MetroBus instead of the licence, minus 85,000; the self-service portal moves to wave 2, minus 216,000.",
                "Every line from a clause or a rate. Negotiated by moving scope, not by haggling the rates.", exact=True)
lines = [("cleansing above A1-07", "26 × £9,500", "£247k"), ("02:10 steps 9 + 12", "X-02 didn't cover", "£310k"), ("change capture", "licence + mainframe", "£180k"), ("reconciliation tooling", "rate card", "£363k")]
for i, (a, b, c) in enumerate(lines):
    y = 14 + i * 46
    cr_how.box(14, y, 250, 40, a, "paper", size=16, rx=4)
    cr_how.box(274, y, 200, 40, b, "paper", size=15, rx=4)
    cr_how.box(484, y, 100, 40, c, "y", size=16, rx=4)
cr_how.box(594, 14, 152, 178, "£1.1m", "pink", sub="+4 months", size=26, subsize=16)
for i, (a, c) in enumerate([("MetroVolt cleanses ≈ 40 %", "−£99k"), ("MetroBus, no licence", "−£85k"), ("portal → wave 2", "−£216k")]):
    y = 214 + i * 40
    cr_how.box(14, y, 460, 34, a, "green", size=16, rx=4)
    cr_how.box(484, y, 100, 34, c, "green", size=16, rx=4)
cr_how.box(594, 214, 152, 114, "£700k", "green", sub="+3 months · 11 Feb", size=24, subsize=15)

HONEST_CR = dict(
    slug="honest-change-request", date=date(2028, 2, 11), meta=on_site(date(2028, 2, 11)), where="FL 27", pass_kind="contractor",
    kicker="a.k.a. the change request after discovery",
    tldr="A change request after bad news is where trust is won or lost. Build it <b>line by line from the contract</b>: each line tied to an <b>assumption</b>, <b>exclusion</b> or <b>rate</b> the client already signed. No padding to “leave room”. Offer <b>options</b> that move scope, not just price, and negotiate in the open by <b>changing what's delivered</b>, never by quietly changing the rates. Then re-baseline.",
    chips=[("Family", "bad news, honestly"), ("Lives in", "delivery/lodestar/CR-007.md · change register"), ("Pairs with", "assumptions (vol. 1), the discovery report, change control (vol. 2)")],
    problem_side="The Grid, December 2027 – February 2028",
    problem="""  <p class="lead">With the discovery report, Wrenfield submits <b>CR-007</b> on <b>14 December</b>: <b>+£1.1m</b> and <b>+4 months</b> to deliver wave 1 against what discovery found.</p>
  <ul>
    <li>Elaine's first words: “Orion's vendor did this after discovery too.” <span class="hl-pink">She doesn't say it angrily. That's worse.</span></li>
    <li>Graham, from Leeds: “Ask for £1.5m. They'll negotiate down to what we need.”</li>
    <li>Nkem has to take the number to Horizon's investment board in a 15 % cost-cut year.</li>
  </ul>""",
    problem_figs=[cr_problem],
    sides=dict(client=("Elaine and Nkem", "<p>For MetroVolt, a big change request after discovery is the Orion pattern: win cheap, then charge. Elaine needs to see that every pound comes from <b>something MetroVolt already agreed to</b>, and Nkem needs options she can take to a cost-cutting board.</p>", "Show me it's the contract, not a trick."),
                vendor=("Ines and Callum", "<p>Wrenfield's fixed price assumed a world that discovery showed isn't real. The contract says so, line by line. If the request is padded, the one thing that separates Wrenfield from Orion's vendor (honesty) is gone.</p>", "Every line from a clause. No line for “room”.")),
    sides_after="Padding a change request to leave room for negotiation teaches the client that your numbers aren't real. After that, every number is negotiated.",
    analogy_side="the builder who found asbestos",
    analogy="""  <p>The builder from the assumptions note opened the wall and found asbestos. An honest builder doesn't add a mystery 30 % “for complications”. He points at the line in the quote (“if found, removal priced separately”), shows the <b>specialist's invoice</b>, and offers options: full removal; seal it and box it in; or do this room now and the rest next year.</p>""",
    map=[("The line in the quote", "A1-07 and X-02, signed in the contract"),
         ("The specialist's invoice", "The rate card and the A1-07 formula"),
         ("No mystery 30 %", "No padding for negotiation"),
         ("Seal it and box it in", "MetroBus instead of a licence"),
         ("This room now, the rest next year", "The portal moves to wave 2")],
    how_side="every line from a clause; negotiate scope, not rates",
    how="""  <p><b>Line by line.</b> CR-007 has four lines, each pointing to the contract: <b>cleansing above A1-07</b>, 26 points at £9,500 (the formula MetroVolt signed): £247k. <b>Replacing steps 9 and 12</b> of the 02:10 job, which exclusion X-02 never covered: £310k at the rate card. <b>Change capture</b> (the licence and mainframe work, not in Schedule 5): £180k. <b>Reconciliation and exception tooling</b> for 117,800 failing records: £363k. Total <b>£1.1m</b>. No line for contingency or “room”.</p>
  <p><b>Options that move scope.</b> In January, Ines, Nkem and Elaine work through the lines together. <b>MetroVolt's own Customer Ops data team</b> cleanses about 40 % of failing addresses (they know the streets): −£99k. <b>Hollis's decision</b> to use MetroBus instead of the licence (note 14): −£85k, +3 weeks. The <b>self-service portal</b> moves to wave 2: −£216k.</p>
  <p><b>Agreed on 11 February 2028: +£700k, +3 months.</b> Not one rate changed. The baseline becomes <b>v2.0</b>: pilot <b>5 June 2028</b>, wave 1 night <b>Saturday 23 September 2028</b>. Elaine's comment at steering: “That's the first change request I've understood.”</p>""",
    how_figs=[cr_how],
    steps=[("Tie every line to a clause", "Assumption, exclusion, schedule or rate."),
           ("Show the arithmetic", "From the contract's own formulas."),
           ("No padding", "Not for contingency, not for room."),
           ("Offer options that move scope", "Who does what, what moves to later."),
           ("Negotiate in the open", "Change what's delivered, never the rates."),
           ("Re-baseline when agreed", "New version, dated, signed.")],
    vocab=[("Change request (CR)", "A formal request to change scope, price or dates."),
           ("Padding", "Adding unexplained money to leave room for negotiation."),
           ("Re-baseline", "Agreeing a new baseline after a significant change."),
           ("Scope trade", "Reducing or moving scope to offset cost."),
           ("Client-side work", "Work the client takes on to reduce cost."),
           ("Win cheap, charge later", "A pattern of under-bidding and recovering through changes.")],
    code=dict(file="delivery/lodestar/CR-007.md", note="submitted 14 Dec 2027 · agreed 11 Feb 2028 (DL-031)", src="""
CR-007 · WAVE 1 AFTER DISCOVERY

line  what                                 contract basis         submitted   agreed
1     address cleansing above A1-07         A1-07: £9,500 × 26     £247,000    £148,000
      (MetroVolt Customer Ops cleanses ≈ 40 %)                                 (−£99k)
2     replace 02:10 steps 9 + 12 for         X-02 scope; rate card  £310,000    £310,000
      migrated customers
3     change capture: licence + mainframe   Sch. 5 (not listed)    £180,000    £95,000
      (MetroBus instead of licence, DL-028)                                    (−£85k)
4     reconciliation + exception tooling    rate card              £363,000    £147,000
      (self-service portal → wave 2)                                           (−£216k)
total                                                               £1,100,000  £700,000
dates  +4 months submitted · +3 months agreed → baseline v2.0:
       pilot Mon 5 Jun 2028 · wave 1 night Sat 23 Sep 2028
rates  unchanged
"""),
    contract=dict(side="the clauses doing the work", doc="Lodestar SOW · §3.2, §7, Appendix C", date="CR-007 agreed 11 Feb 2028", stamp="agreed",
                  clauses=[("3.2", "If an Assumption proves materially incorrect, either Party may raise a Change Request under clause 7.", "the clause we fought for in June 2027. it paid for itself in one line."),
                           ("7.2", "The Supplier shall provide an impact assessment … priced using the Rates in Schedule 5.", "the rates did the arithmetic. nobody argued with them."),
                           ("DL-031", "CR-007 approved at £700,000 and three months. Baseline v2.0 adopted.", "")],
                  plain="a change request built from the contract's own clauses and rates is hard to dispute and easy to negotiate in the open. The negotiation moves scope and responsibilities, not the price of a day."),
    health=dict(now="a",
                g=("trust is high", ["Same method, faster agreement.", "Options discussed informally first.", "Re-baseline promptly."]),
                a=("they've seen this before (Orion)", ["Every line from a clause.", "No padding, said out loud.", "Options that move scope."]),
                r=("they won't pay anything", ["Formal assessment under §7.", "Show what happens without it (option C).", "Escalate with the arithmetic."])),
    pressure=dict(level=5, title="the money conversation", cost="eight weeks of negotiation · Elaine's Orion memory · Graham's margin",
                  items=["Graham's padding instinct is common and understandable. Explain the cost: every future number would be argued.", "Agreeing £700k instead of £1.1m isn't losing £400k: it's moving £400k of work elsewhere, in the open."]),
    baseline="Each line compares <b>a padded request to leave room for haggling</b> with <b>every line from a clause, options that move scope, rates unchanged</b>.",
    ratings=[(1, 4, "“The first change request I've understood.”"),
             (2, 3, "Eight hard weeks, but no lies to keep straight."),
             (2, 4, "Paid for what discovery found; rates intact."),
             (2, 5, "Who cleanses what, and the portal's move, are written."),
             (3, 4, "Design stays honest; MetroBus accepted openly."),
             (2, 4, "New baseline with real dates."),
             (2, 5, "Each line traceable to the contract."),
             (2, 3, "Eight weeks to agree."),
             (3, 3, "A new baseline to run.")],
    pitfalls=[("Padding", "Teaches the client your numbers aren't real.", "every line from a clause."),
              ("Haggling over rates", "Future changes all re-argued.", "negotiate scope, never rates."),
              ("One take-it-or-leave-it number", "The client can't find a way to yes.", "options that move scope."),
              ("Late submission", "It looks like failure.", "with the discovery report."),
              ("No re-baseline", "Old dates haunt every status report.", "new version, signed.")],
    grimoire=[(6, "unpaid-invoice-wraith", "The Unpaid Invoice Wraith", "shows the other end of the money conversation: getting paid without burning the relationship.")],
    use=["After discovery changes the picture.", "When an assumption or exclusion proves false.", "Any request for more money or time."],
    skip=["Small changes inside the change pool: the normal process will do."],
    related=["<b>What Are We Assuming?</b> (vol. 1)", "<b>How Do We Change the Deal Without a War?</b> (vol. 2)", "<b>What Do We Say When Discovery Changes Everything?</b> (this volume)", "<b>What Exactly Did We Promise?</b> (Sanne, vol. 2)"],
    quiz=[("What does every line of an honest CR point to?", "A clause, assumption, exclusion or rate the client already signed."),
          ("Why not pad the request?", "It teaches the client your numbers aren't real, and every future number gets argued."),
          ("How did CR-007 go from £1.1m to £700k?", "MetroVolt cleansed about 40 %, MetroBus replaced the licence, and the portal moved to wave 2."),
          ("What didn't change in the negotiation?", "The day rates."),
          ("What are the new dates in baseline v2.0?", "Pilot Monday 5 June 2028; wave 1 night Saturday 23 September 2028.")],
    quiz_sit=[("Nkem asks for a further 10 % off “as a goodwill gesture for Horizon”. What do you answer?", "Offer goodwill in scope or time (a free half-day data workshop, a later invoice date), and explain that a cut without a trade would make every line of the CR look padded. The rates stay.")],
    try_it="Take a request for more money or time you need to make. Tie every line to something already agreed. Then write two options that move scope or responsibility instead of price.",
    remember="Every line <span class=\"hl\">from a clause</span>. No padding. Negotiate <span class=\"hl\">what's delivered</span>, never the rates.",
    late=dict(when="Fri 11 February 2028 · 20:10 · the train home",
              lines=["£700k and three months. Not one rate changed. The portal goes to wave 2. Priya's team cleans 40 % of the addresses themselves.",
                     "Elaine: “That's the first change request I've understood.” Best review we've had.",
                     "Graham wanted £1.5m. He's not happy with £700k. He'll be happier in a year, when they still believe our numbers."]),
    sources=["Roger Fisher and William Ury, <i>Getting to Yes</i> (1981): interests, not positions.",
             "NEC4 Engineering and Construction Contract: compensation events and assessment.",
             "UK Government, <i>Model Services Contract</i>: change control and impact assessment."],
)

# ------------------------------------------------------------------ 12 Why Does Security Take Twelve Weeks?
sr_problem = Doodle(760, 240, "Doodle of MetroVolt's security and data-protection reviews: an architecture review, a data protection impact assessment, and a penetration test, with a combined twelve-week lead time. Wrenfield requested them in week 14 of discovery instead of week 2. A calendar shows the go-live dates and the reviews squeezed against them.",
                    "Twelve weeks of reviews, requested in week 14 instead of week 2.", exact=True)
for i, (h, sub) in enumerate([("architecture review", "6 weeks"), ("data protection (DPIA)", "8 weeks"), ("penetration test", "3 weeks + fixes")]):
    sr_problem.box(14 + i * 250, 30, 232, 100, h, "pink", sub=sub, size=18, subsize=16)
sr_problem.note(380, 190, "requested in week 14 · needed by the pilot", "red", size=20)

sr_how = Doodle(760, 320, "What worked once the reviews were started. Meet the reviewers first and ask what evidence they need. Bring evidence in their format: their architecture template, their DPIA form, data flows for every personal field. Treat their findings as design input: seven findings, including field-level encryption for the Priority Services Register flags. Track the reviews on the plan like any dependency.",
                "Ask what they need, bring it in their format, and treat findings as design.", exact=True)
for i, (h, sub, fill) in enumerate([("meet them first", "what evidence?", "y"), ("their format", "templates, DPIA form", "blue"), ("findings = design", "7 findings", "green"), ("on the plan", "a dependency", "paper")]):
    sr_how.box(14 + i * 186, 20, 174, 100, h, fill, sub=sub, size=18, subsize=15)
sr_how.box(14, 150, 732, 70, "finding 3: Priority Services Register flags", "pink", sub="vulnerability data → field-level encryption, access logged", size=18, subsize=15)
sr_how.note(380, 270, "all three reviews passed 12 January 2028, two weeks late, not twelve", "pen", size=18)

SECURITY = dict(
    slug="security-review", date=date(2028, 1, 12), meta=on_site(date(2028, 1, 12)), where="FL 19", pass_kind="contractor",
    kicker="a.k.a. security architecture review, DPIA and penetration testing",
    tldr="A regulated client's security and data-protection reviews take weeks, and they always look like a surprise to the vendor who started them late. Start them in <b>week two</b>, <b>meet the reviewers</b> before you send anything, bring <b>evidence in their format</b>, track the reviews on the plan like any <b>dependency</b>, and treat their findings as <b>design input</b>, not obstacles. They're protecting customers you'll be responsible for too.",
    chips=[("Family", "bad news, honestly"), ("Lives in", "security/ (architecture pack, DPIA, test reports)"), ("Pairs with", "the discovery report, design authority day")],
    problem_side="The Grid, October 2027 – January 2028",
    problem="""  <p class="lead">MetroVolt is an electricity network operator holding data on 2.3 million customers, including the <b>Priority Services Register</b>: people on medical equipment, the elderly, households that need warning before a power cut. Any new system needs three reviews: a <b>security architecture review</b> (about 6 weeks), a <b>data protection impact assessment</b> (about 8 weeks) and a <b>penetration test</b> (3 weeks plus fixes).</p>
  <ul>
    <li>Wrenfield's plan had them starting in week 2 of discovery. They were requested in <b>week 14</b>, after the laptops, the access delays and everything else.</li>
    <li>The pilot needs all three passed. <span class="hl-pink">Finding 6 of the discovery report was this.</span></li>
    <li>Hana's view of security reviewers: “people who say no for a living”.</li>
  </ul>""",
    problem_figs=[sr_problem],
    sides=dict(client=("MetroVolt's security and privacy teams", "<p>Three people review every system MetroVolt buys. They've seen suppliers send a marketing deck as “architecture”. A breach of the Priority Services Register would hurt real, vulnerable people and bring the regulator in. They aren't there to slow Lodestar; they're there for those customers.</p>", "Show us where the vulnerable customers' data goes."),
                vendor=("Ines and Hana", "<p>Wrenfield started late and now needs the reviews done fast without asking anyone to cut corners. The only way to speed a careful reviewer up is to give them exactly the evidence they need, in the form they use.</p>", "We can't make them faster. We can make their job easier.")),
    sides_after="Security reviewers are designers who arrive late because they weren't invited early.",
    analogy_side="the building inspector",
    analogy="""  <p>A builder who calls the <b>building inspector</b> the week before the family moves in will wait, and may have to open walls. One who invites the inspector at the drawing stage, asks what they'll check and builds it in, passes the final inspection in an afternoon. The inspector's rules aren't the builder's enemy; they're why the house doesn't burn down.</p>""",
    map=[("Calling the inspector at the end", "Requesting reviews in week 14"),
         ("Inviting them at the drawing stage", "Meeting reviewers in week 2"),
         ("What they'll check", "Their templates and DPIA form"),
         ("Building it in", "Findings treated as design"),
         ("Why the house doesn't burn down", "Why vulnerable customers' data stays safe")],
    how_side="meet them, their format, findings as design, on the plan",
    how="""  <p>Once the mistake is clear, Ines does four things.</p>
  <ul>
    <li><b>Meet the reviewers first.</b> An hour with each team, one question: “What evidence do you need, in what form?” The answers are specific: data flows for every personal field, encryption at rest and in transit, who can see vulnerability data, how access is logged.</li>
    <li><b>Their format.</b> Hana fills in MetroVolt's own architecture template rather than Wrenfield's. Bilal maps <b>every personal field</b> from MAVIS through Lodestar to Halvorsen for the DPIA.</li>
    <li><b>Findings as design.</b> Seven findings. The most important: <b>Priority Services Register flags</b> need field-level encryption and logged access, because they reveal health conditions. It goes into Schedule 2 as a requirement and into the design authority's conditions.</li>
    <li><b>On the plan.</b> Each review is tracked like any dependency, with dates and owners on both sides.</li>
  </ul>
  <p>All three pass on <b>12 January 2028</b>, two weeks late, not twelve. Hana's new view: “They found something we'd have regretted.”</p>""",
    how_figs=[sr_how],
    steps=[("Find out which reviews apply in week one", "Security, privacy, testing, regulatory."),
           ("Meet each reviewer early", "Ask what evidence they need."),
           ("Use their templates", "Not yours."),
           ("Map personal data end to end", "Every field, every system."),
           ("Treat findings as requirements", "Into the design, with owners."),
           ("Put reviews on the plan", "As dependencies, with dates.")],
    vocab=[("Security architecture review", "A check that a system's design protects data and access properly."),
           ("DPIA", "Data protection impact assessment: an assessment of risks to people's personal data."),
           ("Penetration test", "Authorised attempts to break in, to find weaknesses."),
           ("Priority Services Register", "A list of customers who need extra help, e.g. because of medical equipment."),
           ("Field-level encryption", "Encrypting particular sensitive fields, not just whole databases."),
           ("Special category data", "Sensitive personal data, such as health information, with stricter rules.")],
    code=dict(file="security/review-tracker.md", note="as at Wed 12 Jan 2028", src="""
SECURITY + DATA PROTECTION REVIEWS · LODESTAR

review                 owner (MetroVolt)   requested   passed      findings
architecture review    security arch.      6 Oct 27    12 Jan 28   4
DPIA                   privacy office      6 Oct 27    12 Jan 28   2
penetration test       security ops        22 Nov 27   12 Jan 28   1 (fixed, retested)
key findings → design
  S3  PSR flags reveal health conditions → field-level encryption, access logged,
      only 2 roles can read (Schedule 2 v1.1, §6.4)
  S5  Halvorsen file contains full DOB → send year only (spec v1.3 request)
  D2  retention: migrated MAVIS records read-only, deleted after 6 years
lesson   planned week 2, requested week 14 → next phase: book in week 1
"""),
    contract=dict(side="what the contract and the law require", doc="Lodestar SOW · §10 (security) and Schedule 8", date="signed 30 June 2027", stamp="passed",
                  clauses=[("10.2", "The Supplier shall comply with MetroVolt's Security Policy and shall not process Personal Data in a new system until MetroVolt's security architecture review and data protection impact assessment have been completed.", "no pass, no pilot. that's the whole clause."),
                           ("Sch. 8, 3", "Special category data, including data held on the Priority Services Register, shall be encrypted at field level and access to it logged.", "added after finding S3. in the contract now.")],
                  plain="security and data-protection reviews are usually conditions in the contract, and sometimes in law. Starting them late doesn't make them optional; it makes them the critical path."),
    health=dict(now="g",
                g=("reviewers engaged early", ["Evidence as you design.", "Findings are cheap.", "Pass on schedule."]),
                a=("started late", ["Meet them, ask what they need.", "Their format.", "Findings as design."]),
                r=("adversarial reviews", ["Evidence for every control.", "Escalate scheduling, never the findings.", "Fix, retest, document."])),
    pressure=dict(level=3, title="the late review", cost="a planning mistake owned · seven findings",
                  items=["Admitting “we requested this late” in the discovery report was uncomfortable. Pretending otherwise would have been worse.", "Reviewers can't be hurried. They can be helped."]),
    baseline="Each line compares <b>sending a deck in week 14 and hoping</b> with <b>meeting reviewers, evidence in their format, findings as design</b>.",
    ratings=[(3, 4, "MetroVolt's reviewers see a vendor that takes them seriously."),
             (2, 3, "Two weeks late instead of twelve."),
             (3, 3, "Neutral."),
             (3, 4, "Security requirements are written into Schedule 2."),
             (3, 5, "PSR data protected properly."),
             (2, 4, "Findings caught before the pilot."),
             (3, 4, "Reviews and fixes documented."),
             (2, 3, "Twelve weeks is twelve weeks."),
             (3, 3, "Evidence packs to keep current.")],
    pitfalls=[("Starting late", "Reviews become the critical path.", "book them in week one."),
              ("Your format, not theirs", "Reviewers translate, slowly.", "use their templates."),
              ("Arguing with findings", "Delay and distrust.", "treat them as design input."),
              ("Vague data flows", "The DPIA can't conclude.", "map every personal field."),
              ("Forgetting the vulnerable", "The most sensitive data gets least attention.", "PSR first.")],
    use=["Any client with personal or sensitive data.", "Regulated industries.", "Any system that needs approval before go-live."],
    skip=["Never skip; a small internal tool may need only a light review."],
    related=["<b>What Do We Say When Discovery Changes Everything?</b> (this volume)", "<b>How Do We Get the Design Approved?</b> (this volume)", "<b>Why Can't We Log In?</b> (vol. 2)", "<b>Threat Modelling</b> (patterns, Vol. 5)"],
    quiz=[("What three reviews did Lodestar need?", "A security architecture review, a data protection impact assessment and a penetration test."),
          ("Why do Priority Services Register flags matter so much?", "They reveal health conditions and vulnerability; a breach would hurt vulnerable people."),
          ("What was the key planning mistake?", "Requesting the reviews in week 14 instead of week 2."),
          ("What does “findings as design” mean?", "Each finding becomes a requirement in the design, with an owner."),
          ("What does clause 10.2 prevent?", "Processing personal data in a new system before the reviews are complete.")],
    quiz_sit=[("The pen test finds a medium-risk issue a week before the pilot. Hana says it's “theoretical”. What do you do?", "Fix it or agree a documented risk acceptance with MetroVolt's security owner, with a date. It's their decision, not Wrenfield's, and the pilot shouldn't go ahead with an unowned finding.")],
    try_it="List the reviews your current project needs before go-live. When were they requested? Book a one-hour meeting with one reviewer and ask what evidence they need.",
    remember="Invite the inspector <span class=\"hl\">at the drawing stage</span>. Their findings are <span class=\"hl\">design you'd have regretted missing</span>.",
    late=dict(when="Wed 12 January 2028 · 21:00 · hotel near The Grid",
              lines=["All three passed. Two weeks late, not twelve, because we finally asked what they needed.",
                     "Finding S3: the vulnerability flags. Field-level encryption. They were right, and we'd have shipped without it.",
                     "Next time, week one. I'm writing it in the front of this notebook."]),
    sources=["UK Information Commissioner's Office, guidance on data protection impact assessments.",
             "UK National Cyber Security Centre, <i>Secure design principles</i>.",
             "Adam Shostack, <i>Threat Modeling: Designing for Security</i> (2014)."],
)

NOTES = [DISCOVERY_REPORT, BAD_NEWS, HONEST_CR, SECURITY]
