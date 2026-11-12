# Series 2 · Book 2 · The Product Owner's Notebook · Vol. 1 · Understanding customers.
# Narrator: Grace. Running case study: Larder (facts in docs/larder-casebook.md).

# ------------------------------------------------------------------ 01 Customer Interviews
ci_problem = Doodle(760, 280, "Doodle of the customer research Grace inherits in her first week: a survey where 31 people asked for better substitutes, and an in-app wish list asking for recipes and more brands. Both say what customers think they want. Neither says what happened the last time a substitution went wrong, or why it hurt.",
                    "The research she inherits: opinions and wishes, but not one story about what actually happened.")
ci_problem.box(20, 30, 220, 120, None, "paper")
ci_problem.head(130, 60, "survey, Sept", size=17)
ci_problem.text(130, 94, "31 × “better", size=16)
ci_problem.text(130, 118, "substitutes”", size=16)
ci_problem.box(270, 30, 220, 120, None, "paper")
ci_problem.head(380, 60, "app wish list", size=17)
for i, t in enumerate(["“add recipes”", "“more brands”", "“dark mode”"]):
    ci_problem.text(380, 90 + i * 22, t, size=15)
ci_problem.box(520, 30, 220, 120, "what happened?", "pink", sub="why did it hurt?", stroke="red", size=17, subsize=15)
ci_problem.note(380, 196, "what people say they want ≠ what they do", "red")
ci_problem.note(380, 228, "so: talk to 12 customers in two weeks", "pen")

ci_analogy = Doodle(760, 260, "Doodle of a detective interviewing a witness. The detective asks what the witness saw at nine o'clock, not whether they think the butler did it. Facts about one specific past moment are reliable; opinions and predictions are not.",
                    "A detective asks “what did you see at nine?”, not “do you think the butler did it?”")
ci_analogy.icon("magnifier", 40, 50, 1.6)
ci_analogy.box(170, 40, 260, 60, "“what did you see", "green", sub="at nine o'clock?”", size=16, subsize=15)
ci_analogy.note(300, 124, "✓ a fact, one moment", "green")
ci_analogy.box(470, 40, 270, 60, "“did the butler", "pink", sub="do it, you think?”", stroke="red", size=16, subsize=15)
ci_analogy.note(605, 124, "✗ an opinion, a guess", "red")
ci_analogy.note(380, 200, "past behaviour is evidence; opinions and predictions aren't", "pen")

ci_how = Doodle(760, 360, "How Grace runs and uses an interview. The guide moves from a warm-up, to 'tell me about the last time something was substituted', to digging with 'what happened next', 'how did that feel' and 'what did you do'. She avoids 'would you use' questions. After each interview she fills one snapshot card. Twelve snapshots later, three patterns stand out: people don't mind substitutes, they mind not being asked; allergies make some swaps dangerous; and they find out at the door, too late.",
                 "One story per interview, one snapshot card each, then look for patterns across the cards.")
steps = [("warm up", "who, how often"), ("“last time…”", "one real story"), ("dig", "then? felt? did?")]
for i, (t, sub) in enumerate(steps):
    x = 14 + i * 160
    ci_how.box(x, 20, 146, 64, t, "blue" if i != 1 else "y", sub=sub, size=15, subsize=13)
    if i < 2:
        ci_how.arrow(x + 148, 52, x + 158, 52)
ci_how.box(500, 20, 246, 64, "✗ “would you use…?”", "pink", sub="predictions mislead", stroke="red", size=14, subsize=13)
for i in range(4):
    ci_how.box(14 + i * 46, 120 + i * 6, 160, 100, None, "paper")
ci_how.head(150, 262, "12 snapshot cards", size=15)
ci_how.arrow(318, 170, 340, 170)
pats = [("“ask me first”", "12 of 12"), ("allergies: unsafe swaps", "4 of 12"), ("“I find out at the door”", "10 of 12")]
for i, (t, n) in enumerate(pats):
    ci_how.box(346, 110 + i * 56, 290, 46, None, "green")
    ci_how.text(360, 140 + i * 56, t, anchor="start", size=15)
    ci_how.text(624, 140 + i * 56, n, "t-head", anchor="end", size=14)
ci_how.note(380, 300, "they don't mind substitutes; they mind not being asked", "pen", size=19)
ci_how.note(380, 334, "12 interviews · 6 express · 4 slots · 2 who left", "pen", size=17)

CUSTOMER_INTERVIEWS = dict(
    slug="customer-interviews",
    kicker="a.k.a. “what did you see at nine o'clock?”",
    tldr="Talk to customers <b>every week</b>, and ask about <b>what they actually did</b>, not what they'd like or would do. “Tell me about the last time…” gets you a real story; “would you use…?” gets you a polite guess. Dig into each story (what happened next, how it felt, what they did about it), write <b>one snapshot card</b> per interview, and look for <b>patterns across the cards</b>. Twelve good conversations beat a survey of thousands when you don't yet know the right questions.",
    chips=[("Family", "understanding customers"), ("Origin", "Rob Fitzpatrick, <i>The Mom Test</i> (2013); Teresa Torres, story-based interviewing"), ("Lives in", "a weekly interview slot and a folder of snapshot cards"), ("Pairs with", "jobs to be done, opportunity solution tree, journey map")],
    problem_side="Larder, Grace's first week",
    problem="""  <p class="lead">On day one Priya hands Grace “the customer research”: a September survey where <b>31 people</b> asked for “better substitutes”, and the in-app wish list (recipes, more brands, dark mode). Both are what customers <i>think</i> they want. Neither tells Grace what actually happened the last time a substitution went wrong, or <span class="hl-pink">why it hurt</span>. So she books <b>twelve interviews</b> in her first two weeks.</p>
  <ul>
    <li>Surveys and wish lists collect opinions and solutions, not problems.</li>
    <li>People are bad at predicting what they'd do, and kind enough to say yes to your idea.</li>
    <li>Without stories, the team builds what was asked for, not what was needed.</li>
  </ul>""",
    problem_figs=[ci_problem],
    meanwhile=[("architect-1", "stakeholder-map", "the same week, Ana maps who inside Larder can say no; Grace starts with the people who pay.", "the same week, Grace starts interviewing customers: the people who pay the bills.")],
    analogy_side="the detective",
    analogy="""  <p>A good detective asks a witness <b>“what did you see at nine o'clock?”</b>, not “do you think the butler did it?”. Facts about one specific moment in the past are reliable. Opinions, theories and predictions are not, however sincerely they're given. And the detective keeps asking “and then?” until the story is complete.</p>""",
    analogy_figs=[ci_analogy],
    map=[("A witness", "A customer who recently ordered (or left)"),
         ("“What did you see at nine?”", "“Tell me about the last time something was substituted.”"),
         ("“And then what?”", "Digging: what happened next, how it felt, what they did"),
         ("“Do you think the butler did it?”", "“Would you use an approve button?” (avoid)"),
         ("The case board", "Snapshot cards, compared to find patterns")],
    how_side="one story, one card, then patterns",
    how="""  <p>Each interview is <b>30 minutes about one real story</b>. Grace interviews in pairs (with Sam or an engineer) so one person can listen and note. After each call they fill a <b>snapshot card</b> within the hour. Patterns only count once they show up across several cards.</p>""",
    how_figs=[ci_how],
    steps=[("Recruit a mix", "Recent, frequent and lapsed customers; both express and slots. Offer a €15 voucher. Aim for 3–5 a week."),
           ("Open with context", "Who they are, how often they order, for whom. Two minutes, no more."),
           ("Ask for one specific story", "“Tell me about the last time something in your order was substituted.” Not “in general”."),
           ("Dig, don't pitch", "“What happened next?”, “How did you feel?”, “What did you do?”. Never show your solution."),
           ("Write a snapshot card", "Within the hour: quote, story, needs and pains, insights, one photo-worthy line."),
           ("Synthesise weekly", "Lay out the cards; a pattern needs several independent stories behind it.")],
    vocab=[("Story-based interview", "An interview built around one specific past experience."),
           ("Leading question", "One that suggests the answer (“wouldn't it be great if…?”)."),
           ("Snapshot card", "A one-page summary of one interview."),
           ("Synthesis", "Finding patterns across interviews."),
           ("Continuous interviewing", "A small number of interviews every week, forever."),
           ("Recruiting screener", "Questions used to pick the right people to interview.")],
    code=dict(file="research/interviews/2025-10-16-rik.md", note="interview snapshot card", plain=True, src="""
# Interview snapshot · 16 Oct 2025 · “Rik”            interviewers: Grace, Sam

Who       38, two kids (one with a dairy allergy), Amsterdam-Oost
Orders    express 2–3 × a week, around 17:30; slots for the Sunday shop
Quote     “I don't mind a swap. I mind finding out on the doormat.”

The story (last time something was substituted)
  - Tue 7 Oct, ordered at 17:20: pasta, vegetables, lactose-free milk
  - 17:48 courier at the door. Milk swapped for regular milk. No message.
  - Couldn't use it (allergy). Went to the corner shop anyway: 20 minutes.
  - Wrote to support; refund two days later. “The refund wasn't the point.”

Needs / pains
  - Be asked before a swap, quickly (“I'm on my phone anyway at that time”)
  - Some items must never be swapped (allergy)
  - Know before the courier arrives

Insight   The pain is the surprise, not the substitute.
Follow up Ask the next 4 express customers about allergies.
"""),
    tools="tools: a calendar link, a video call and a €15 voucher. Recruit in the app or the order confirmation email; record with permission and keep recordings per your privacy policy (Lena signed off Larder's). Dovetail, Notion or a shared folder for snapshot cards.",
    gains=["<b>Real problems</b>, in customers' own words.",
           "<b>Surprises</b>: the pain was the surprise, not the substitute.",
           "<b>Quotes that persuade</b> stakeholders better than charts.",
           "<b>Cheap and fast</b>: twelve calls in two weeks.",
           "<b>A habit</b>: weekly interviews keep the team close to customers."],
    losses=["<b>Small samples</b>: twelve people can mislead; check with data.",
            "<b>Skill needed</b>: leading questions are easy to slip into.",
            "<b>Recruiting effort</b> every week.",
            "<b>Privacy care</b>: recordings and notes hold personal data."],
    baseline="Each line compares <b>relying on surveys, wish lists and stakeholder opinions</b> to <b>weekly story-based interviews with snapshot cards and regular synthesis</b>.",
    ratings=[(2, 5, "The team hears real stories about real pain."),
             (3, 3, "Interviews find problems; business impact comes later."),
             (2, 4, "Decisions rest on what people did, not what they said they'd do."),
             (2, 4, "Twelve calls in two weeks change the direction."),
             (2, 4, "Patterns show which problem matters most."),
             (2, 5, "Engineers who join calls understand customers directly."),
             (3, 4, "Quotes and stories make the case to stakeholders."),
             (3, 3, "Neutral: discovery, not delivery."),
             (3, 2, "Recruiting and calls take a few hours every week.")],
    pitfalls=[("Asking about the future", "“Would you use an approve button?” “Sure!”", "ask about the last time it happened; past behaviour is evidence."),
              ("Pitching your idea", "Half the call is a demo of the solution.", "never show the solution in a problem interview; test it later."),
              ("Only happy customers", "Everyone recruited orders twice a week and loves Larder.", "include lapsed and unhappy customers on purpose."),
              ("Notes in heads", "Great conversations, nothing written down.", "fill a snapshot card within the hour, every time.")],
    use=["Starting on a new product area or a new problem.",
         "When the team argues about what customers want.",
         "Every week, as a habit, while building.",
         "Before a big bet, to check the problem is real."],
    skip=["Questions data can answer better (how many, how often).",
          "Testing usability of a screen: do a prototype test instead.",
          "When you'd only be confirming a decision already made."],
    related=["<b>Jobs to be done</b> (this volume)", "<b>Customer journey map</b> (this volume)", "<b>Opportunity solution tree</b> (this volume)", "<b>Prototype testing with users</b> (this volume)"],
    quiz=[("Why ask about the last time instead of what they'd like?", "Past behaviour is evidence; opinions and predictions are unreliable and often polite."),
          ("What three questions keep a story going?", "What happened next? How did you feel? What did you do?"),
          ("What is a snapshot card?", "A one-page summary of a single interview: quote, story, needs, pains, insights."),
          ("What did Grace's interviews reveal about substitutions?", "Customers don't mind substitutes; they mind not being asked, and finding out at the door.")],
    try_it="Book two 30-minute calls with customers this week. Write one opening question that starts with “Tell me about the last time…”. After each call, fill a snapshot card within the hour. Did either story surprise you?",
    remember="Ask what they <span class=\"hl\">did</span>, not what they'd <span class=\"hl\">like</span>. Then ask “and then?”",
    sources=["Rob Fitzpatrick, <i>The Mom Test</i> (2013).",
             "Teresa Torres, <i>Continuous Discovery Habits</i> (2021), chapters on interviewing.",
             "Steve Portigal, <i>Interviewing Users</i>, 2nd ed. (2023).",
             "Erika Hall, <i>Just Enough Research</i>, 2nd ed. (2019)."],
)

# ------------------------------------------------------------------ 02 Jobs to Be Done
jt_problem = Doodle(760, 270, "Doodle of Priya's customer segments by age and income, such as 'young professionals 25 to 34'. The segments don't explain behaviour: the same person, Rik, orders express on Tuesday at 17:30 and a slot on Sunday morning, and wants completely different things each time.",
                    "Age and income don't explain why the same person shops two different ways in one week.")
jt_problem.box(20, 30, 240, 100, None, "paper")
jt_problem.head(140, 60, "segment B", size=17)
jt_problem.text(140, 92, "“young professionals”", size=15)
jt_problem.text(140, 116, "25–34 · €40–60k", size=15)
jt_problem.arrow(266, 80, 330, 80, dash=True, label="explains?", lx=298, ly=66)
jt_problem.box(336, 20, 190, 70, "Tue 17:30", "y", sub="express · 6 items", size=17, subsize=14)
jt_problem.box(550, 20, 190, 70, "Sun 10:00", "blue", sub="slot · 41 items", size=17, subsize=14)
jt_problem.note(540, 120, "same person: Rik", "pen")
jt_problem.note(380, 190, "speed matters on Tuesday; completeness on Sunday", "red")
jt_problem.note(380, 224, "one segment, two jobs", "red", size=19)

jt_analogy = Doodle(760, 260, "Doodle of the morning milkshake. A fast-food chain found that many milkshakes were bought before 8 a.m. by commuters with a long, boring drive. They weren't hiring a dessert; they were hiring something thick that lasts the drive and fits in one hand. Its competitors were bananas, bagels and boredom, not other milkshakes.",
                    "The morning milkshake: commuters hire it for a long, boring drive. Its rivals are bananas and boredom.")
jt_analogy.icon("cup", 40, 60, 1.6)
jt_analogy.note(90, 180, "7:40 a.m.", "pen")
jt_analogy.box(190, 50, 280, 80, "hired for:", "green", sub="a boring 40-min drive", size=17, subsize=15)
jt_analogy.box(500, 30, 240, 120, None, "paper")
jt_analogy.head(620, 58, "real competitors", size=16)
for i, t in enumerate(["bananas", "bagels", "the radio, boredom"]):
    jt_analogy.text(620, 88 + i * 22, t, size=15)
jt_analogy.note(380, 220, "not other milkshakes", "pen")

jt_how = Doodle(760, 360, "Larder's two main jobs, written as job stories. Express: when it's 17:30 and there's nothing for dinner, I want to get what I need without going out, so I can feed the kids by 18:30. What matters: speed, a swap is fine if I'm asked. It competes with the corner shop and takeaway. Slots: when I plan the week's meals, I want the whole list delivered at a time I choose, so my Saturday stays free. What matters: completeness; a swap of a staple ruins the plan. It competes with the supermarket and its own delivery. A third job is emerging from two interviews: keep the office pantry stocked without anyone thinking about it.",
                 "Two jobs, two meanings of a substitution. The third job (offices) is a hint, not yet a bet.")
for i, (title, when, want, matters, rivals, fill) in enumerate([
        ("express", "17:30, nothing for dinner", "without going out", "speed · ask me", "corner shop · takeaway", "y"),
        ("slots", "planning the week", "the whole list, my time", "complete · no staple swaps", "supermarket · its delivery", "blue")]):
    x = 14 + i * 372
    jt_how.box(x, 20, 356, 220, None, fill)
    jt_how.head(x + 178, 50, title, size=20)
    for k, (lbl, val) in enumerate([("when", when), ("I want", want), ("matters", matters), ("vs", rivals)]):
        jt_how.text(x + 16, 92 + k * 38, lbl, "t t-soft", anchor="start", size=14)
        jt_how.text(x + 96, 92 + k * 38, val, anchor="start", size=15)
jt_how.box(160, 262, 440, 56, "emerging: “keep the office pantry stocked”", "paper", dash=True, size=14)
jt_how.note(380, 346, "2 of 12 interviews · a hint for Larder for Business", "pen", size=17)

JOBS = dict(
    slug="jobs-to-be-done",
    kicker="a.k.a. “the morning milkshake”",
    tldr="Customers don't buy products; they <b>hire</b> them to make progress in a particular situation. Describe that <b>job</b> as a short story: <b>when</b> [situation], <b>I want to</b> [motivation], <b>so I can</b> [outcome]. Jobs explain behaviour that age and income can't, show who you <b>really</b> compete with, and tell you what “good” means in each situation. The same person can have several jobs, and a feature can help one job while hurting another.",
    chips=[("Family", "understanding customers"), ("Origin", "Clayton Christensen, <i>Competing Against Luck</i> (2016); Bob Moesta; Alan Klement's job stories"), ("Lives in", "two or three job stories at the top of the product brief"), ("Pairs with", "customer interviews, proto-personas, north star metric")],
    problem_side="Larder, Priya's segments",
    problem="""  <p class="lead">Larder's marketing segments customers by age and income: “young professionals, 25–34”. But in her interviews Grace meets Rik, who orders <b>express on Tuesday at 17:30</b> (six items, dinner for the kids) and a <b>slot on Sunday morning</b> (41 items, the week's shop). Same person, same segment, and he wants <span class="hl-pink">opposite things</span>: speed on Tuesday, completeness on Sunday. A substitution means something different each time.</p>
  <ul>
    <li>Demographics describe people, not why they act.</li>
    <li>Features get designed for an average customer who doesn't exist.</li>
    <li>The team doesn't see its real competitors: the corner shop, a takeaway.</li>
  </ul>""",
    problem_figs=[jt_problem],
    meanwhile=[("architect-1", "business-drivers", "Ana turns Femke's brief into drivers; Grace finds the customer side of driver 2 (on time): the express job.", "Grace's interviews find the customer side of driver 2: the express job, “dinner sorted tonight”.")],
    analogy_side="the morning milkshake",
    analogy="""  <p>A fast-food chain wanted to sell more milkshakes and asked customers how to improve them: thicker, cheaper, more flavours. Sales didn't move. Then they watched <b>who</b> bought them: commuters, before 8 a.m., facing a <b>long, boring drive</b>. They weren't hiring a dessert; they were hiring something that lasts the drive and fits in one hand. Its real competitors were <b>bananas, bagels and boredom</b>.</p>""",
    analogy_figs=[jt_analogy],
    map=[("The morning commute", "The situation: 17:30, nothing for dinner"),
         ("Something that lasts the drive", "The progress: dinner on the table by 18:30, no trip out"),
         ("Bananas and bagels", "Real competitors: the corner shop, a takeaway"),
         ("Thicker shake for mornings", "Design for the job: fast, and ask me before swapping"),
         ("A different job at lunch (a treat for the kids)", "The Sunday slot: a different job, same customer")],
    how_side="situation, motivation, outcome",
    how="""  <p>Write each job as a <b>job story</b> from interview evidence, then add what <b>matters</b> in that job and what it <b>competes</b> with. A job is stable over years; the solutions change. Grace's two jobs explain why the substitution flow must be fast for express and careful for slots.</p>""",
    how_figs=[jt_how],
    steps=[("Start from stories", "Use interview snapshots, not brainstorms: when did they order, and what were they doing?"),
           ("Find the struggling moment", "What made them reach for Larder right then? (17:30, empty fridge, kids hungry.)"),
           ("Write job stories", "When [situation], I want to [motivation], so I can [outcome]. No product words."),
           ("Note what matters", "The two or three things that make it a success or a failure in this job."),
           ("List the real competition", "What else could they hire? Corner shop, takeaway, a supermarket's own delivery."),
           ("Design per job", "Check each feature against each job: does it help one and hurt another?")],
    vocab=[("Job to be done", "The progress a customer is trying to make in a situation."),
           ("Job story", "When [situation], I want to [motivation], so I can [outcome]."),
           ("Hire / fire", "Choosing a product for a job, or dropping it for another."),
           ("Struggling moment", "The moment the job becomes urgent enough to act."),
           ("Functional / emotional job", "What gets done / how they want to feel."),
           ("Non-consumption", "Doing nothing or a workaround: often the biggest competitor.")],
    code=dict(file="product/jobs.md", note="Larder's job stories, v1 (Nov 2025)", plain=True, src="""
# Jobs customers hire Larder for                 from 12 interviews, Oct 2025

J1 EXPRESS · “dinner tonight”                          ~70 % of orders
   When it's late afternoon and there's nothing for dinner,
   I want to get what I need without going out,
   so I can have food on the table by 18:30.
   Matters:   arrives in 30 min · a swap is fine if I'm asked · nothing unsafe
   Competes:  corner shop, takeaway, “just eat pasta again”

J2 SLOTS · “the week's shop”                           ~30 % of orders
   When I plan the week's meals,
   I want the whole list delivered at a time I choose,
   so I can keep my Saturday free.
   Matters:   complete · the right brands · no swaps on staples
   Competes:  the supermarket trip, the supermarket's own delivery

J3 EMERGING · “the office pantry”                      2 of 12 interviews
   When I'm responsible for the office kitchen,
   I want it restocked without anyone thinking about it,
   so I can stop being the person who buys milk.
   → share with Femke (Larder for Business idea)
"""),
    tools="tools: interview snapshots and a whiteboard. Bob Moesta's “switch interview” (Re-Wired Group) and Jim Kalbach's job map are useful deeper methods; jtbd.info has many examples.",
    gains=["<b>Explains behaviour</b> that segments can't.",
           "<b>Real competitors</b> come into view.",
           "<b>Clear success criteria</b> per situation.",
           "<b>Stable</b>: jobs change slowly, solutions fast.",
           "<b>New markets spotted</b>: the office pantry job."],
    losses=["<b>Abstract at first</b>: teams need examples to get it.",
            "<b>Easy to make vague</b> (“I want to feel good”).",
            "<b>Needs good interviews</b> to be more than guesses.",
            "<b>Doesn't size the market</b>: pair with data."],
    baseline="Each line compares <b>designing for demographic segments</b> to <b>designing for two or three evidence-based job stories, with what matters and the real competition</b>.",
    ratings=[(2, 5, "Features fit the situation customers are really in."),
             (3, 4, "Real competitors and new jobs (offices) become visible."),
             (2, 4, "Jobs come from interview stories, not guesses."),
             (3, 3, "Neutral; jobs guide what to test, not how fast."),
             (2, 4, "Express and slots get different, focused designs."),
             (2, 5, "One sentence per job everyone can repeat."),
             (3, 4, "Leaders recognise the jobs in their own lives."),
             (3, 3, "Neutral."),
             (3, 4, "A page of job stories; revisit twice a year.")],
    pitfalls=[("Product words in the job", "“I want to use the approve button.”", "describe the progress, never the product or a feature."),
              ("Too vague", "“I want to feel happy.”", "anchor the job in a situation and a concrete outcome."),
              ("Jobs from a brainstorm", "Written in a room with no customers.", "derive them from interview stories."),
              ("One job for everyone", "Express and slots merged into “get groceries”.", "split jobs where what matters is different.")],
    use=["When segments don't explain what customers do.",
         "Before designing a flow that serves different situations.",
         "Looking for new markets or the real competition.",
         "Writing the product strategy."],
    skip=["Small usability fixes inside a flow.",
          "When you have no interview evidence yet: interview first.",
          "As a replacement for data on how many people have each job."],
    related=["<b>Customer interviews</b> (this volume)", "<b>Proto-personas</b> (this volume)", "<b>North star metric</b> (this volume)", "<b>Business drivers &amp; goals</b> (Ana, vol. 1)"],
    quiz=[("What is the job story format?", "When [situation], I want to [motivation], so I can [outcome]."),
          ("Why did segments fail to explain Rik's behaviour?", "The same person had two jobs (express dinner, the weekly shop) with opposite needs."),
          ("Who are the real competitors of the express job?", "The corner shop, a takeaway, or making do: not other grocery apps only."),
          ("What does a substitution mean in each Larder job?", "Express: fine if asked. Slots: swapping a staple ruins the plan.")],
    try_it="Pick your product's most common use. Write it as one job story (when…, I want to…, so I can…) without naming your product. List three things customers could hire instead, including “do nothing”. Which of them is your real competitor?",
    remember="Customers <span class=\"hl\">hire</span> products for a <span class=\"hl\">job</span>. Know the job, and you know the competition.",
    sources=["Clayton Christensen et al., <i>Competing Against Luck</i> (2016).",
             "Alan Klement, <i>When Coffee and Kale Compete</i> (2016), job stories.",
             "Bob Moesta, <i>Demand-Side Sales 101</i> (2020).",
             "Anthony Ulwick, <i>Jobs to Be Done: Theory to Practice</i> (2016)."],
)

# ------------------------------------------------------------------ 03 Proto-Personas
pp_problem = Doodle(760, 270, "Doodle of a 28-page persona deck from a marketing agency: 'Urban Ursula', with a stock photo, a favourite coffee order and a star sign, none of it from research. Nobody in the team uses it. In meetings people argue about what 'the user' wants, each picturing someone different.",
                    "A 28-page persona with a star sign and no evidence. In meetings, everyone still pictures their own “user”.")
pp_problem.box(20, 20, 260, 200, None, "paper")
pp_problem.head(150, 50, "“Urban Ursula”", size=18)
pp_problem.icon("frame", 120, 64, 1.0)
for i, t in enumerate(["flat white, oat", "Libra", "loves brunch"]):
    pp_problem.text(150, 150 + i * 22, t, size=14)
pp_problem.note(150, 246, "28 pages · 0 interviews", "red")
for i, (who, pic) in enumerate([("Ben", "a student"), ("Dee", "a busy mum"), ("Joost", "his own parents")]):
    pp_problem.box(330 + i * 140, 70, 126, 64, f"{who}'s user", "blue", sub=pic, size=14, subsize=13)
pp_problem.note(540, 180, "everyone pictures someone else", "red")

pp_analogy = Doodle(760, 250, "Doodle of a police sketch, an identikit drawn from several witness statements. It's rough, but good enough for people to recognise the person, and the artist updates it as more witnesses come in. It's labelled with how many witnesses agreed.",
                    "A police sketch: rough, drawn from witnesses, good enough to recognise, updated when more come in.")
pp_analogy.box(40, 20, 170, 200, None, "paper")
pp_analogy.raw('<ellipse class="d f-paper" cx="125" cy="100" rx="48" ry="60"/><path class="d d-thin" d="M105 90 h10 M135 90 h10 M125 100 v16 M110 130 q15 10 30 0"/>')
pp_analogy.note(125, 200, "from 5 witnesses", "pen")
for i, t in enumerate(["witness 1: “tall”", "witness 2: “cap”", "witness 3: “beard”"]):
    pp_analogy.box(260, 20 + i * 54, 230, 42, t, "y", size=14)
pp_analogy.arrow(496, 100, 546, 100)
pp_analogy.box(550, 60, 190, 80, "updated", "green", sub="as evidence comes in", size=17, subsize=14)

pp_how = Doodle(760, 360, "Grace's three proto-personas, one card each, built from twelve interviews. The tonight-dinner parent: orders express two or three times a week, needs to be asked before a swap, some items must never be swapped because of allergies, six interviews. The Sunday planner: orders big slot orders, needs completeness and the right brands, four interviews. The office stocker: orders for a team of sixty, needs predictable restocking and an invoice, two interviews, low confidence. Each card shows its evidence count.",
                 "Three cards, built from twelve interviews. Each one says how much evidence is behind it.")
cards = [("tonight-dinner parent", "express · 2–3×/week", ["ask me before a swap", "never swap allergens", "know before the door"], "6 interviews · high", "y"),
         ("Sunday planner", "slots · weekly, 40+ items", ["the whole list", "the right brands", "no staple swaps"], "4 interviews · medium", "blue"),
         ("office stocker", "for a team of 60", ["restock on a schedule", "one invoice", "no one has to think"], "2 interviews · low", "paper")]
for i, (name, how, needs, ev, fill) in enumerate(cards):
    x = 14 + i * 248
    pp_how.box(x, 20, 236, 270, None, fill, dash=(i == 2))
    pp_how.raw(f'<circle class="d f-paper" cx="{x + 118}" cy="62" r="24"/>')
    pp_how.head(x + 118, 118, name, size=15)
    pp_how.text(x + 118, 142, how, "t t-soft", size=14)
    for k, nd in enumerate(needs):
        pp_how.text(x + 18, 180 + k * 26, "• " + nd, anchor="start", size=14)
    pp_how.note(x + 118, 276, ev, "pen", size=15)
pp_how.note(380, 330, "no star signs, no stock photos: only what interviews showed", "pen", size=17)

PROTO_PERSONAS = dict(
    slug="proto-personas",
    kicker="a.k.a. “the police sketch”",
    tldr="A <b>proto-persona</b> is a quick, one-page sketch of a main kind of customer: their <b>situation, needs and pains</b>, drawn from real interviews, with a note of <b>how much evidence</b> is behind it. Keep two to four, give them plain names that describe the situation (“the tonight-dinner parent”), leave out invented details, and update them as you learn. They replace “the user” in meetings with someone specific everyone can picture.",
    chips=[("Family", "understanding customers"), ("Origin", "Alan Cooper, <i>The Inmates Are Running the Asylum</i> (1999); Jeff Gothelf, proto-personas in <i>Lean UX</i> (2013)"), ("Lives in", "one page per persona on the team wall"), ("Pairs with", "jobs to be done, customer interviews, journey map")],
    problem_side="Larder, the persona deck",
    problem="""  <p class="lead">Larder has personas: a 28-page deck from a marketing agency starring <b>“Urban Ursula”</b>, with a stock photo, a favourite coffee order and a star sign. None of it came from research, and nobody uses it. In meetings, Ben pictures a student, Dee a busy mum, Joost his own parents. Everyone argues for <span class="hl-pink">“the user”</span>, and everyone means someone different.</p>
  <ul>
    <li>Invented details make personas fun and useless.</li>
    <li>Without a shared picture, “the user” becomes whoever wins the argument.</li>
    <li>Heavy research personas take months and go stale.</li>
  </ul>""",
    problem_figs=[pp_problem],
    meanwhile=[("architect-1", "system-context", "Ana's context diagram has one box called “customer”; Grace's proto-personas show it's at least three.", "Grace's proto-personas split this one “customer” box into three kinds of customer with different needs.")],
    analogy_side="the police sketch",
    analogy="""  <p>A <b>police sketch</b> is drawn from several witness statements. It's rough (no birthday, no favourite colour), but good enough for people to <b>recognise</b> someone, and the artist <b>updates it</b> as more witnesses come in. A good sketch also says how many witnesses agreed.</p>""",
    analogy_figs=[pp_analogy],
    map=[("Witness statements", "Interview snapshot cards"),
         ("The sketch", "A one-page proto-persona"),
         ("“Five witnesses agreed”", "The evidence count on each persona"),
         ("Updated as witnesses come in", "Revised after each round of interviews"),
         ("No birthday, no favourite colour", "No invented details: only what affects the product")],
    how_side="a few cards, all evidence",
    how="""  <p>Group the snapshot cards by <b>situation and needs</b>, not by age. Each group with enough stories becomes a card: a descriptive name, the situation, three needs or pains, and the <b>evidence count</b>. A card with two interviews is marked low confidence; it's a hypothesis, not a fact.</p>""",
    how_figs=[pp_how],
    steps=[("Group the interviews", "Sort snapshot cards by situation and needs. Two to four groups usually appear."),
           ("Name by situation", "“The tonight-dinner parent”, not “Urban Ursula”. The name should remind you of the need."),
           ("Write only what matters", "Situation, how they use Larder, top three needs and pains, a quote. Nothing invented."),
           ("Show the evidence", "Number of interviews and data behind it; mark confidence high, medium or low."),
           ("Put them on the wall", "Use the names in stories, reviews and designs: “would the parent see this in time?”"),
           ("Revise each quarter", "Merge, split or retire personas as new interviews come in.")],
    vocab=[("Persona", "A representative description of a kind of customer."),
           ("Proto-persona", "A quick, evidence-light persona, treated as a hypothesis."),
           ("Evidence count", "How many interviews or data points support it."),
           ("Anti-persona", "Someone you're deliberately not designing for."),
           ("Archetype", "A pattern of behaviour, rather than a fictional person."),
           ("Segment", "A group defined for marketing (age, income), often not behaviour.")],
    code=dict(file="product/personas/tonight-dinner-parent.md", note="one proto-persona card", plain=True, src="""
# The tonight-dinner parent                       confidence: HIGH (6 of 12 interviews)

Situation   Works until 17:00, picks up kids, nothing planned for dinner.
Uses Larder express, 2–3 × a week, ordering between 17:00 and 18:00, on the phone.
Job         J1 “dinner tonight” (product/jobs.md)

Needs       1. Be asked before a swap, and answer in one tap
            2. Some items are never swapped (allergies: 4 of 6 had one)
            3. Know what's coming before the courier rings
Pains       Finding a swap at the door; a second trip to the corner shop
Quote       “I don't mind a swap. I mind finding out on the doormat.” (Rik)

Not this persona: the Sunday planner (big baskets, brands matter more than speed)
Evidence    interviews 16, 17, 20, 21, 23, 24 Oct · order data: 70 % of orders are express
Next check  4 more express customers in November, focus on allergies
"""),
    tools="tools: one page per persona in a shared doc or on the wall. Lean UX's proto-persona template is a good start; tools like Miro and FigJam have persona templates (delete the star-sign fields).",
    gains=["<b>One shared picture</b> instead of “the user”.",
           "<b>Fast</b>: a few hours from existing interviews.",
           "<b>Honest</b>: evidence counts show what's solid and what's a guess.",
           "<b>Better reviews</b>: “would the parent see this in time?”",
           "<b>Spots new customers</b>: the office stocker."],
    losses=["<b>Can harden into stereotypes</b> if never revised.",
            "<b>Small samples</b>: low-confidence cards can mislead.",
            "<b>Easy to decorate</b> with invented detail.",
            "<b>Not a market size</b>: pair with data."],
    baseline="Each line compares <b>an invented agency persona deck and “the user” in meetings</b> to <b>two to four evidence-based proto-personas with confidence levels, used daily and revised quarterly</b>.",
    ratings=[(2, 4, "Designs are checked against real kinds of customer."),
             (3, 3, "Neutral; helps to focus, doesn't move numbers alone."),
             (1, 4, "Every line traces back to interviews; confidence is explicit."),
             (3, 3, "Neutral."),
             (2, 4, "Fewer, sharper target customers."),
             (2, 5, "Everyone pictures the same three people."),
             (3, 4, "Stakeholders recognise their customers in them."),
             (3, 3, "Neutral."),
             (3, 4, "A few hours to make; an hour a quarter to revise.")],
    pitfalls=[("Invented detail", "Star signs, coffee orders, stock photos.", "only include what changes product decisions."),
              ("Personas by demographics", "“Female, 25–34, urban.”", "group by situation, needs and behaviour."),
              ("Too many", "Nine personas, so nobody remembers any.", "two to four; merge the rest."),
              ("Never revised", "The 2025 cards still rule in 2027.", "revise each quarter; show the evidence count.")],
    use=["When “the user” causes arguments.",
         "After a first round of interviews.",
         "Onboarding designers and engineers to the customers.",
         "Choosing which customer a feature is for."],
    skip=["When you have no interviews yet: interview first.",
          "To size a market: use data.",
          "When jobs to be done already give the team enough focus."],
    related=["<b>Jobs to be done</b> (this volume)", "<b>Customer interviews</b> (this volume)", "<b>Customer journey map</b> (this volume)", "<b>System context diagram</b> (Ana, vol. 1)"],
    quiz=[("How is a proto-persona different from a classic persona?", "It's quick, based on the evidence you have, marked with its confidence, and treated as a hypothesis."),
          ("Why name personas by situation?", "The name reminds everyone of the need (“the tonight-dinner parent”)."),
          ("What should never be on a proto-persona?", "Invented details that don't change product decisions: star signs, coffee orders, stock photos."),
          ("Why is the office stocker marked low confidence?", "Only two interviews support it; it's a hint to test, not a fact.")],
    try_it="From your last five customer conversations, sort the people into groups by situation and need. Write one proto-persona card for the biggest group, with an evidence count. Read it to a colleague who joined the calls: would they recognise the people?",
    remember="A <span class=\"hl\">sketch from witnesses</span>, not a novel. Say how many witnesses agree.",
    sources=["Jeff Gothelf &amp; Josh Seiden, <i>Lean UX</i>, 3rd ed. (2021), proto-personas.",
             "Alan Cooper, <i>The Inmates Are Running the Asylum</i> (1999).",
             "Indi Young, <i>Practical Empathy</i> (2015).",
             "Nielsen Norman Group, “Personas Make Users Memorable” (nngroup.com)."],
)

# ------------------------------------------------------------------ 04 Customer Journey Map
jm_problem = Doodle(760, 260, "Doodle of Larder's teams each owning one screen: the shop team the basket, payments the checkout, the store team the picker app, support the refund tool. Each screen works on its own. Nobody sees the whole journey, so nobody sees that the customer's worst moment is at the front door.",
                    "Every team owns a screen, and every screen works. Nobody owns the moment at the front door.")
for i, (scr, team) in enumerate([("basket", "shop"), ("checkout", "payments"), ("picker app", "store"), ("refund tool", "support")]):
    x = 14 + i * 186
    jm_problem.box(x, 30, 172, 80, scr, "blue", sub=f"✓ {team} team", size=16, subsize=14)
jm_problem.box(260, 160, 240, 60, "the front door", "pink", sub="owner: nobody", stroke="red", size=17, subsize=14)
jm_problem.note(380, 250, "where the customer finds the swap", "red")

jm_analogy = Doodle(760, 250, "Doodle of a theme park manager walking the park as a visitor. Every ride works, but the forty-minute queue in the sun with no sign saying how long is what visitors remember. You only see it by walking the whole day as a guest.",
                    "Every ride works. Visitors remember the 40-minute queue in the sun. You only see it as a guest.")
for i, t in enumerate(["gate ✓", "ride ✓", "queue", "ride ✓", "exit ✓"]):
    x = 20 + i * 148
    bad = t == "queue"
    jm_analogy.box(x, 40, 128, 60, t, "pink" if bad else "green", sub="40 min" if bad else None, stroke="red" if bad else "", size=15, subsize=12)
jm_analogy.line("M20 170 C 150 150, 250 150, 330 220 S 520 150, 740 150", color="pen")
jm_analogy.note(380, 132, "the mood curve dips where no ride is broken", "pen")

jm_how = Doodle(760, 400, "The express parent's journey map, drawn by Grace with Sam and Tomás. Stages: order at 17:20, wait, the picker finds an item out of stock at 17:31, the picker swaps it without asking, the courier arrives at 17:48, the customer discovers the swap at the door, contacts support, gets a refund two days later. The mood line is high at ordering, drops sharply at the door and stays low until the refund. Below the line, the backstage: at 17:31 the picker has no way to reach the customer, which is the real moment of truth, seventeen minutes before the doorbell.",
                 "The mood drops at the door, but the moment that matters is 17 minutes earlier, backstage, when the picker finds the gap.")
stages = [("17:20", "order"), ("17:31", "item OOS"), ("17:33", "swap, no ask"), ("17:48", "at the door"), ("19:00", "support"), ("+2 days", "refund")]
for i, (t, s) in enumerate(stages):
    x = 14 + i * 124
    jm_how.box(x, 20, 112, 56, t, "pink" if i == 3 else "paper", sub=s, stroke="red" if i == 3 else "", size=15, subsize=13)
jm_how.note(14, 104, "mood", "pen", anchor="start", size=16)
jm_how.line("M70 120 L194 126 L318 132 C 360 140, 400 240, 442 250 L566 240 L690 220", color="pen")
jm_how.raw('<circle class="d f-red" cx="442" cy="250" r="7"/>')
jm_how.note(472, 280, "“on the doormat”", "red", anchor="start", size=17)
jm_how.line("M14 300 H746", dash=True, thin=True)
jm_how.note(14, 324, "backstage", "pen", anchor="start", size=16)
jm_how.box(130, 330, 300, 56, "17:31 · picker finds the gap", "y", sub="no way to reach the customer", size=15, subsize=13)
jm_how.arrow(436, 358, 486, 358, color="green")
jm_how.box(492, 330, 254, 56, "moment of truth", "green", sub="17 min before the door", size=15, subsize=13)

JOURNEY_MAP = dict(
    slug="journey-map",
    kicker="a.k.a. “walk the park as a guest”",
    tldr="Draw every step a customer takes to get their job done, <b>across all your teams and channels</b>, with what they <b>do, think and feel</b> at each step. Add a <b>backstage</b> row for what your staff and systems do at the same moment. The low points on the mood line, and what was happening backstage just before them, show where the experience really breaks, usually <b>between</b> teams, where nobody owns it.",
    chips=[("Family", "understanding customers"), ("Origin", "service design (Lynn Shostack's service blueprint, 1984); UX practice"), ("Lives in", "a long sheet on the wall, then a one-page map"), ("Pairs with", "customer interviews, event storming, opportunity solution tree")],
    problem_side="Larder, one screen per team",
    problem="""  <p class="lead">At Larder every team owns a screen: the shop team the basket, payments the checkout, the store team the picker app, support the refund tool. Every screen works, and every team's dashboard is green. But Grace's interviews keep ending at the same place: the <span class="hl-pink">front door</span>, where customers find out about a swap. No screen covers that moment, so no team owns it.</p>
  <ul>
    <li>Teams optimise their own step; customers experience the whole journey.</li>
    <li>The worst moments happen in the gaps between teams and channels.</li>
    <li>Without the backstage view, you fix the symptom (refunds), not the cause.</li>
  </ul>""",
    problem_figs=[jm_problem],
    meanwhile=[("architect-1", "event-storming", "Ana's event storm shows the same timeline from inside: “item out of stock” → “substitute offered” had no owner.", "Grace's journey map shows the customer's side of this timeline: the mood drops at the door, 17 minutes after “item out of stock”.")],
    analogy_side="the theme park",
    analogy="""  <p>A theme-park manager can check every ride and find them all working. Then they spend a day <b>as a guest</b> and discover what visitors actually remember: the <b>40-minute queue in the sun</b> with no sign saying how long. No ride is broken. The experience is, in between.</p>""",
    analogy_figs=[jm_analogy],
    map=[("A day in the park as a guest", "The whole journey, from order to refund"),
         ("Each ride", "Each team's screen or service"),
         ("The queue in the sun", "The wait, and the surprise at the door"),
         ("The mood of the visitor", "The emotion line on the map"),
         ("Staff behind the scenes", "The backstage row: pickers, support, systems")],
    how_side="steps, mood, backstage",
    how="""  <p>Map <b>one persona doing one job</b> (the parent, an express order). Build it with people from each team that touches the journey, using real interview stories and data. The insight is usually where a low point in the mood line meets a backstage step <b>nobody can act on</b>.</p>""",
    how_figs=[jm_how],
    steps=[("Pick one persona and one job", "“The tonight-dinner parent, an express order.” One map per journey."),
           ("List the stages", "From trigger to end, in the customer's terms, with real times from data."),
           ("Add doing, thinking, feeling", "From interview quotes, not guesses. Draw the mood line."),
           ("Add the backstage", "What staff and systems do at each step: picker app, support tool, dispatch."),
           ("Find the moments of truth", "Low points, and the backstage step just before them."),
           ("Turn them into opportunities", "Each moment of truth becomes an opportunity on the tree, with an owner.")],
    vocab=[("Customer journey map", "The steps, thoughts and feelings of a customer doing a job."),
           ("Touchpoint", "A moment the customer interacts with you: app, courier, email."),
           ("Front stage / backstage", "What the customer sees / what happens behind it."),
           ("Service blueprint", "A journey map with detailed backstage and support layers."),
           ("Moment of truth", "A point that makes or breaks the experience."),
           ("Pain point", "A step where the customer struggles or feels bad.")],
    code=dict(file="product/journeys/express-parent.md", note="journey map, text version", plain=True, src="""
# Journey: the tonight-dinner parent · express order              v1 · 3 Nov 2025

Stage        Order      Wait       Item OOS     Swap        At the door   Support    Refund
Time         17:20      17:20–48   17:31        17:33       17:48         19:00      +2 days
Doing        6 items    cooks pasta (picker)    (picker)    opens bag     writes     checks bank
Thinking     “quick”    “on time?” –            –           “not this!”   “again?”   “finally”
Feeling      🙂          🙂          –            –           😠           😠          😐
Backstage    —          —          no way to    picker      courier       manual     refund tool
                                   reach cust.  guesses     can't help    lookup     (Sam's team)

Moment of truth  17:31, when the picker finds the gap: 17 minutes before the door
Opportunities    → O1 “let me say yes or no” · O2 “tell me before the courier” (opportunity tree)
Owners           Grace (app), Tomás (picking), Sam (support)
"""),
    tools="tools: a long roll of paper and stickies, or Miro / FigJam journey templates; Smaply and UXPressia for detailed blueprints. Real timestamps from order data make the map honest.",
    gains=["<b>The whole experience</b> on one page, across teams.",
           "<b>Gaps between teams</b> become visible and get owners.",
           "<b>Causes, not symptoms</b>: the backstage row shows why.",
           "<b>Shared empathy</b>: teams see customers' feelings at each step.",
           "<b>Opportunities</b> for the tree, straight from the low points."],
    losses=["<b>Workshop time</b> with several teams.",
            "<b>One persona, one job</b>: you'll need more maps.",
            "<b>Can be invented</b> if not grounded in research.",
            "<b>Goes stale</b> as the product changes."],
    baseline="Each line compares <b>each team owning and optimising its own screen</b> to <b>one evidence-based journey map with a backstage row, built across teams</b>.",
    ratings=[(2, 5, "The worst moment of the journey is found and named."),
             (3, 4, "Refund costs trace back to one moment of truth."),
             (2, 4, "Built from interview quotes and real order timestamps."),
             (3, 3, "Neutral."),
             (2, 4, "One moment of truth to fix, not ten screens to polish."),
             (2, 5, "Shop, store and support see the same journey."),
             (3, 4, "Joost and Sam recognise their teams' part in it."),
             (3, 3, "Neutral."),
             (3, 3, "A half-day workshop per journey.")],
    pitfalls=[("Mapping the happy path", "Every step goes well on paper.", "map a real story, including when it goes wrong."),
              ("Only front stage", "The map shows screens, not what staff do behind them.", "always add the backstage row."),
              ("Feelings guessed", "Smiley faces from a workshop opinion.", "take thoughts and feelings from interview quotes."),
              ("A poster, not a tool", "Framed on the wall, never used.", "turn each low point into an opportunity with an owner.")],
    use=["Problems that cross several teams or channels.",
         "When every team's dashboard is green but customers are unhappy.",
         "Onboarding new team members to the customer experience.",
         "Before redesigning a service end to end."],
    skip=["A problem inside one screen: use a usability test.",
          "When you haven't talked to customers yet.",
          "Tiny products with one simple step."],
    related=["<b>Customer interviews</b> (this volume)", "<b>Proto-personas</b> (this volume)", "<b>Opportunity solution tree</b> (this volume)", "<b>Domain discovery (event storming)</b> (Ana, vol. 1)"],
    quiz=[("What does the backstage row add?", "What staff and systems do at each step, which shows the cause behind a low point."),
          ("Where was the moment of truth in Larder's express journey?", "At 17:31, when the picker finds the gap and can't reach the customer: 17 minutes before the door."),
          ("Why map one persona and one job?", "Different personas and jobs have different journeys; mixing them blurs the low points."),
          ("What happens to the low points?", "They become opportunities on the opportunity solution tree, with owners.")],
    try_it="Map one real customer story from your last interview as a journey: stages, times, what they felt, and a backstage row. Mark the lowest point. Which team owns the step just before it, and do they know?",
    remember="Every ride works; the <span class=\"hl\">queue</span> is what they remember. Look <span class=\"hl\">backstage</span> for the cause.",
    sources=["Lynn Shostack, “Designing Services that Deliver” (Harvard Business Review, 1984).",
             "Jim Kalbach, <i>Mapping Experiences</i>, 2nd ed. (2020).",
             "Marc Stickdorn et al., <i>This Is Service Design Doing</i> (2018).",
             "Nielsen Norman Group, “Journey Mapping 101” (nngroup.com)."],
)

NOTES = [CUSTOMER_INTERVIEWS, JOBS, PROTO_PERSONAS, JOURNEY_MAP]
