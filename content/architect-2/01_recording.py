# Series 2 · The Solution Architect's Notebook · Vol. 2 · Recording decisions — sample chapter.
# Running case study: Larder, a grocery delivery start-up growing from one city to six.

# ------------------------------------------------------------------ 01 Architecture Decision Records
adr_problem = Doodle(760, 260, "Doodle of a team meeting at Larder, eight months after a decision. A new engineer asks why orders go through Postgres and an outbox instead of straight to Kafka. Nobody who decided is still on the team, the chat thread has expired, and the team spends two weeks re-arguing it, nearly undoing a choice made for a reason nobody remembers.",
                    "Eight months later: “why did we do it this way?” Nobody knows, so the team argues it all again.")
adr_problem.box(20, 30, 230, 70, "“why not just Kafka?”", "y", size=17)
adr_problem.note(135, 130, "new engineer, month 8", "pen")
for i, (t, x) in enumerate([("decided by: left in March", 300), ("chat thread: expired", 300), ("wiki page: 2 lines, outdated", 300)]):
    adr_problem.note(x, 50 + i * 40, "✗ " + t, "red", anchor="start")
adr_problem.box(300, 180, 300, 54, "2 weeks of re-arguing", "pink", stroke="red", size=17)
adr_problem.note(660, 200, "and almost", "red")
adr_problem.note(660, 226, "undoing it", "red")

adr_analogy = Doodle(760, 260, "Doodle of a ship's captain's log next to a court judgement. A judgement records the facts, the arguments considered and the reasoning, not just the verdict, so later judges can follow it or overturn it on purpose. Each judgement is numbered and never rewritten; a later case can supersede it.",
                     "A court judgement: facts, arguments, reasoning and verdict, numbered, never rewritten, only overturned by a later one.")
adr_analogy.icon("ledger", 40, 50, 1.8, fill="y")
adr_analogy.note(95, 200, "judgement no. 7", "pen")
for i, t in enumerate(["the facts", "arguments considered", "reasoning", "the verdict"]):
    adr_analogy.box(240, 30 + i * 50, 220, 40, t, "paper" if i < 3 else "green", size=16)
adr_analogy.arrow(470, 180, 536, 180, dash=True, label="later", lx=503, ly=166)
adr_analogy.box(540, 150, 210, 60, "no. 12 overrules no. 7", "pink", size=15)
adr_analogy.note(655, 240, "on purpose, with reasons", "green")

adr_how = Doodle(760, 300, "Life of an ADR at Larder. A significant decision appears, such as how orders reach the delivery service. Someone writes ADR 0007 as a pull request with context, options, decision and consequences, status proposed. The people affected review it. When merged it becomes accepted and lives in the repository next to the code. Later, ADR 0015 supersedes it; 0007 is kept but marked superseded, with a link to its successor.",
                 "One short file per decision, reviewed as a pull request, kept forever next to the code; replaced only by a newer record.")
adr_how.box(20, 40, 170, 70, "a decision", "y", sub="hard to reverse?")
adr_how.arrow(196, 75, 256, 75)
adr_how.box(262, 30, 210, 90, "ADR 0007", "blue", sub="proposed · as a PR")
adr_how.arrow(478, 75, 548, 75, color="green", label="review", lx=513, ly=61)
adr_how.box(554, 30, 190, 90, "accepted", "green", sub="docs/adr/ in the repo")
adr_how.arrow(649, 124, 649, 184, dash=True, label="2 years later", lx=662, ly=160, anchor="start")
adr_how.box(470, 188, 270, 64, "0015 supersedes 0007", "pink", size=16)
adr_how.note(220, 200, "context · options · decision · consequences", "pen")
adr_how.note(220, 230, "one page, plain words", "pen")

ADR = dict(
    slug="adr",
    kicker="a.k.a. “the court judgement”",
    tldr="For every decision that is <b>significant and hard to reverse</b>, write a <b>one-page record</b>: the <b>context</b>, the <b>options</b> you considered, the <b>decision</b>, and its <b>consequences</b>, good and bad. Number it, review it like code, keep it <b>in the repository</b> next to what it explains, and <b>never rewrite it</b>: when you change your mind, write a new record that <b>supersedes</b> the old one. Months later, “why did we do this?” has an answer.",
    chips=[("Family", "recording decisions"), ("Origin", "Michael Nygard, “Documenting Architecture Decisions” (2011)"), ("Lives in", "docs/adr/ in the repo, as Markdown"), ("Pairs with", "options analysis, RFCs, decision log")],
    problem_side="Larder, month eight",
    problem="""  <p class="lead">Larder chose Postgres with a transactional outbox to send orders to delivery, not direct Kafka writes. Eight months later a new engineer asks <i>why</i>. The people who decided have moved on, the chat thread is gone, and the wiki says only “we use the outbox”. So the team <span class="hl-pink">argues it all again</span> for two weeks, and nearly undoes it.</p>
  <ul>
    <li>Decisions live in meetings, chats and people's heads, all of which disappear.</li>
    <li>Without the reasons, every decision looks arbitrary, so it gets re-litigated.</li>
    <li>Or the opposite: nobody dares change anything, because maybe there was a reason.</li>
  </ul>""",
    problem_figs=[adr_problem],
    analogy_side="the court judgement",
    analogy="""  <p>A court doesn't just announce a verdict. A <b>judgement</b> records the <b>facts</b>, the <b>arguments considered</b> and the <b>reasoning</b>, then the verdict. It's <b>numbered</b> and never rewritten. A later court can overrule it, but it does so <b>on purpose</b>, in a new judgement that says why.</p>
  <ul>
    <li>The judgement is the <b>ADR</b>; its number is the ADR number.</li>
    <li>Arguments considered are the <b>options</b>; the reasoning is the <b>decision drivers</b>.</li>
    <li>Overruling with a new judgement is <b>superseding</b>.</li>
  </ul>""",
    analogy_figs=[adr_analogy],
    map=[("The facts of the case", "Context: the forces and constraints at the time"),
         ("Arguments considered", "Options, with pros and cons"),
         ("The verdict", "Decision: what we will do"),
         ("What the verdict means for everyone", "Consequences, including the costs we accept"),
         ("A later judgement overrules it", "A new ADR supersedes the old one, which stays on file")],
    how_side="one decision, one page, kept forever",
    how="""  <p>An ADR is <b>short on purpose</b>: one page someone can read in five minutes. The value isn't the document; it's that the reasoning <b>survives</b> the people and the meeting.</p>""",
    how_figs=[adr_how],
    steps=[("Spot a significant decision", "Hard or costly to reverse, affects several teams, or will surprise a newcomer: datastores, integration style, build vs buy, a major library."),
           ("Write it as a pull request", "Copy the template into <code>docs/adr/NNNN-short-title.md</code>, status <i>proposed</i>."),
           ("Name the options honestly", "At least two real options, including “do nothing”, each with what it costs."),
           ("Write the consequences, both kinds", "What gets easier, what gets harder, what we now have to do (and who)."),
           ("Review with the people affected", "Comments on the PR are the discussion; merge = <i>accepted</i>."),
           ("Never edit, supersede", "Changing your mind? A new ADR that links to the old one; mark the old one <i>superseded by NNNN</i>.")],
    vocab=[("ADR", "Architecture Decision Record: one decision, one short file."),
           ("Architecturally significant", "Costly to reverse or wide in its effect."),
           ("Decision drivers", "The forces that decided it (cost, deadline, skills, risk)."),
           ("Status", "Proposed, accepted, deprecated or superseded."),
           ("Supersede", "Replace an ADR with a newer one, keeping the old on file."),
           ("Decision log", "The numbered list of all ADRs, the index.")],
    code=dict(file="docs/adr/0007-orders-to-delivery-via-outbox.md", note="Nygard-style template, filled in", plain=True, src="""
# 7. Send orders to delivery via a transactional outbox

Status:   Accepted · 2026-03-14 · deciders: Ana (architect), Ben (orders), Cho (payments)

## Context
Orders must reach the delivery service exactly once. Payment and the order row
are written in one Postgres transaction. We run one Kafka cluster, with no
transactional producer experience in the team. Launch in Rotterdam is in 6 weeks.

## Options
1. Write to Kafka directly from the order service
   + simple
   – a crash between the DB commit and the publish loses the order
2. Transactional outbox in Postgres + a relay to Kafka
   + no lost orders
   – one more table and a relay to run
3. Change data capture (Debezium) on the orders table
   + no app changes
   – new infrastructure, and our table becomes a public contract

## Decision
Option 2. The order, the payment and the outbox row commit together.

## Consequences
+ No order is lost or sent twice (consumers dedupe on order_id).
+ Works with the skills we have; no new infrastructure before launch.
– Delivery sees orders up to ~2 s later (relay polling).
– We own the relay. Revisit if order volume passes 200/s (then consider option 3).
"""),
    tools="tools: plain Markdown in the repo is enough. adr-tools and Log4brains (CLI + a browsable site), MADR (a richer template), Backstage ADR plugin, Structurizr (ADRs next to C4 diagrams), joelparkerhenderson/architecture-decision-record (template collection).",
    gains=["<b>The reasoning survives</b> people leaving and chats expiring.",
           "<b>Faster onboarding</b>: newcomers read the why, not just the what.",
           "<b>Fewer re-arguments</b>: revisit on purpose, with the original reasons.",
           "<b>Better decisions</b>: writing options down exposes weak reasoning.",
           "<b>Reviewed like code</b>: the people affected get a say."],
    losses=["<b>Writing time</b>: 30–60 minutes per decision.",
            "<b>Easy to over-do</b>: an ADR for every library bump.",
            "<b>Easy to forget</b>: records only help if they're written at the time.",
            "<b>Not a design doc</b>: too short for detailed designs (link an RFC)."],
    baseline="Each line compares <b>decisions made in meetings and chats, with no record</b> to <b>one-page ADRs, reviewed as pull requests and kept in the repo</b>.",
    ratings=[(2, 4, "Newcomers can read why the system looks like this."),
             (2, 4, "The people affected review the record before it's accepted."),
             (3, 3, "Writing takes an hour; re-arguing takes weeks. Even."),
             (2, 4, "Writing the options down exposes risks early."),
             (3, 4, "Consequences say when to revisit; changing course is deliberate."),
             (1, 5, "Every significant decision has a dated, numbered reason."),
             (2, 3, "Options usually list cost; it's not the focus."),
             (4, 3, "An hour per decision; a few decisions a month."),
             (2, 4, "Teams can read past reasoning instead of asking the architect.")],
    pitfalls=[("Recording only the winner", "The ADR says “we chose X” with no alternatives.", "list at least two real options and why each lost."),
              ("Editing old records", "The 2026 decision is quietly rewritten in 2027.", "never edit; supersede with a new ADR and link both ways."),
              ("Writing them afterwards", "Six months later someone reconstructs the reasons from memory.", "write it as part of the decision, as a PR."),
              ("An ADR for everything", "Records for library bumps and naming choices bury the important ones.", "only decisions that are costly to reverse or wide in effect.")],
    use=["Choosing datastores, integration styles, platforms or vendors.",
         "Decisions that affect several teams.",
         "Anything a newcomer would ask “why?” about.",
         "Regulated environments that need an audit trail of design choices."],
    skip=["Easily reversible, local choices (a helper library, a naming convention).",
          "Detailed designs: write an RFC or design doc, and an ADR for its key decision.",
          "Throwaway prototypes."],
    related=["<b>Options analysis</b> (Vol. 2)", "<b>RFCs &amp; design docs</b> (Vol. 2)", "<b>One-way vs two-way doors</b> (Vol. 2)", "<b>Transactional outbox</b> (patterns, Vol. 1)"],
    quiz=[("What makes a decision worth an ADR?", "It's significant: costly or hard to reverse, affects several teams, or would puzzle a newcomer."),
          ("What are the four core parts of an ADR?", "Context, options considered, the decision, and its consequences."),
          ("You've changed your mind about ADR 0007. What do you do?", "Write a new ADR that supersedes it, and mark 0007 as superseded with a link; never edit the original."),
          ("Why keep ADRs in the repository?", "They sit next to the code they explain, are reviewed like code, and are versioned with it.")],
    try_it="Pick one decision your team made in the last three months that a new joiner would question. Write its ADR in under 45 minutes using the template above, and open it as a pull request. Ask one person who was <i>not</i> in the original discussion whether the reasoning makes sense to them.",
    remember="Write the <span class=\"hl\">judgement</span>, not just the verdict. Never rewrite it; <span class=\"hl\">overrule</span> it with a new one.",
    sources=["Michael Nygard, “Documenting Architecture Decisions” (Cognitect blog, 2011).",
             "MADR, “Markdown Any Decision Records” (adr.github.io/madr).",
             "ThoughtWorks Technology Radar, “Lightweight Architecture Decision Records” (Adopt).",
             "Olaf Zimmermann et al., “Sustainable Architectural Design Decisions” (IEEE Software, 2013)."],
)

# ------------------------------------------------------------------ 02 Decision Log
dl_problem = Doodle(760, 290, "Doodle of Larder's decisions in March 2026, six weeks before Rotterdam opens. Seven are ADRs in the repository. Eleven more were made in chat, five in ticket comments and three in meeting notes. Sanne, the delivery manager, asks which decisions for Rotterdam are still open and who is making them. Nobody can say: nineteen decisions live outside the ADRs, and six open ones have no owner.",
                    "Seven decisions in the repo, nineteen everywhere else, and nobody can say which are still open.")
for i, (t, s, f) in enumerate([("docs/adr", "7 ADRs", "green"), ("chat", "11 decisions", "pink"), ("tickets", "5 decisions", "pink"), ("meeting notes", "3 decisions", "pink")]):
    x = 20 + i * 185
    dl_problem.box(x, 30, 165, 70, t, f, sub=s, size=17, subsize=15)
    dl_problem.arrow(x + 82, 104, 250 + i * 86, 168, dash=f == "pink")
dl_problem.box(170, 172, 420, 60, "“what's still open for Rotterdam?”", "y", size=16)
dl_problem.note(675, 200, "Sanne, 16 Mar", "pen")
dl_problem.note(380, 270, "19 decisions outside the ADRs · 6 open, no owner", "red")

dl_analogy = Doodle(760, 230, "Doodle of a court's docket: a single list of every case, one line each, with its number, status, judge and date. Pending cases have a hearing date; decided ones point to the judgement; overruled ones point to the case that replaced them.",
                    "A court's docket: every case on one list, one line each, with a status, a judge and a date.")
dl_analogy.icon("ledger", 40, 60, 1.6, fill="y")
dl_analogy.note(88, 196, "the docket", "pen")
dl_analogy.table(190, 24, "today's docket", ["no. 44 · pending · hearing 2 Apr", "no. 41 · pending · judge K.", "no. 38 · decided 12 Mar", "no. 29 · overruled by no. 38"], w=370, row=36, hl=(2,), soft=(3,))
dl_analogy.note(665, 80, "every case,", "pen", size=19)
dl_analogy.note(665, 106, "one line", "pen", size=19)
dl_analogy.note(665, 160, "status · judge", "green", size=19)
dl_analogy.note(665, 186, "· date", "green", size=19)

dl_how = Doodle(760, 290, "How Larder's decision log works. Every decision gets one line. It starts open, with an owner and a due date. When it's decided, the line links to an ADR if the decision is significant, or just records the answer in one line if it's small and easy to reverse. If a later decision replaces it, it's marked superseded with the new number. Sanne and Ana review the open lines every Monday.",
                "One line per decision, open or decided; big ones link an ADR, small ones are one line. Reviewed every Monday.")
dl_how.note(380, 24, "open lines reviewed every Monday with Sanne", "pen")
dl_how.box(20, 44, 200, 80, "open", "y", sub="owner + due date")
dl_how.arrow(226, 84, 286, 84)
dl_how.box(292, 44, 210, 80, "decided", "green", sub="ADR, or one line")
dl_how.arrow(508, 84, 568, 84, dash=True)
dl_how.box(574, 44, 170, 80, "superseded", "paper", sub="by D-31")
dl_how.box(50, 180, 310, 70, "significant?", "blue", sub="→ write an ADR, link it")
dl_how.box(400, 180, 310, 70, "small, two-way?", "paper", sub="→ one line in the log is enough")
dl_how.arrow(370, 128, 210, 176)
dl_how.arrow(420, 128, 552, 176)

DECISION_LOG = dict(
    slug="decision-log",
    kicker="a.k.a. “the court's docket”",
    tldr="ADRs explain single decisions; a <b>decision log</b> is the <b>index of all of them</b>, including the <b>open</b> ones. One line per decision: a number, the question, the <b>status</b> (open, decided, superseded), an <b>owner</b>, a <b>due date</b> and a link to the ADR, or the answer in one line if it's small. Keep it in the repo, review the open lines <b>every week</b>, and “what's still undecided, and who's deciding it?” takes ten seconds to answer.",
    chips=[("Family", "recording decisions"), ("Origin", "decision registers in project management; the ADR index (adr-tools, Log4brains)"), ("Lives in", "docs/decisions/README.md, next to the ADRs"), ("Pairs with", "ADRs, decision rights, one-way vs two-way doors")],
    problem_side="Larder, 16 March 2026",
    problem="""  <p class="lead">Six weeks before Rotterdam opens, Sanne, the delivery manager, asks Ana a simple question: <i>which decisions for Rotterdam are still open, and who's making them?</i> Ana can point to seven ADRs. But she finds <b>nineteen more decisions</b> made in chat threads, ticket comments and meeting notes, and <span class="hl-pink">six open questions with no owner at all</span>, including how Rotterdam's opening hours get into the app.</p>
  <ul>
    <li>ADRs record the decisions someone thought were big enough; the rest are scattered.</li>
    <li>Open questions have no home, so they're discovered late, usually by the person blocked by them.</li>
    <li>“Was that decided?” is answered by whoever remembers, differently each time.</li>
  </ul>""",
    problem_figs=[dl_problem],
    analogy_side="the court's docket",
    analogy="""  <p>A court doesn't keep its cases in judges' heads. The <b>docket</b> lists <b>every case</b>, one line each: number, status, judge, the next hearing date, and a pointer to the judgement once there is one. Anyone can see what's pending and who has it. The judgements are the long documents; the docket is how you find them, and how you see what's <b>not decided yet</b>.</p>""",
    analogy_figs=[dl_analogy],
    map=[("One line per case", "One line per decision: D-number and the question"),
         ("Pending, with a hearing date", "Open, with an owner and a due date"),
         ("Decided, see the judgement", "Decided, with a link to the ADR (or the answer in one line)"),
         ("Overruled by a later case", "Superseded by a later decision"),
         ("The judge", "The owner who will make the call")],
    how_side="one line per decision, open ones first",
    how="""  <p>The log is <b>cheap on purpose</b>: adding a line takes a minute, so small decisions get recorded too. Only the significant ones get an ADR; the log links them. The open lines are the useful part: they're a <b>to-do list of decisions</b> with owners and dates.</p>""",
    how_figs=[dl_how],
    steps=[("Start the file", "<code>docs/decisions/README.md</code>: a table with number, decision, status, owner, due date and link."),
           ("Backfill once", "Sweep chats, tickets and meeting notes from the last three months; one line each. Don't chase perfection."),
           ("Log open questions too", "A question someone is waiting on gets a line, an owner and a due date, today."),
           ("Close with a link or a line", "Significant → write the ADR and link it. Small and reversible → write the answer in the log."),
           ("Review weekly", "Ten minutes on Monday: overdue lines, lines without owners, decisions that block a date."),
           ("Supersede, don't delete", "A replaced decision stays in the log, marked with the number that replaced it.")],
    vocab=[("Decision log", "The index of every decision, open or closed, one line each."),
           ("Open decision", "A question someone is waiting on, with an owner and a due date."),
           ("Owner", "The one person who will make the call or get it made."),
           ("Due date", "When the decision must be made so nothing downstream slips."),
           ("ADR index", "The list of ADRs; here it's the log's “significant” rows."),
           ("Superseded", "Replaced by a later decision; kept on file.")],
    code=dict(file="docs/decisions/README.md", note="Larder's decision log, 23 March 2026 (excerpt)", plain=True, src="""
# Decision log                       open lines reviewed Mondays · Ana + Sanne

| No.  | Decision                                  | Status     | Owner  | Due    | Record   |
|------|-------------------------------------------|------------|--------|--------|----------|
| D-07 | Send orders to delivery via an outbox     | decided    | Ana    |        | ADR 0007 |
| D-19 | Rotterdam opening hours: config or code?  | decided    | Ben    |        | config (ADR 0003) |
| D-21 | Dispatch: own service, how orders get in  | open · RFC | Eli    | 27 Mar | RFC-003  |
| D-22 | Second payment provider for peak?         | open       | Cho    | 3 Apr  | ADR 0009 if yes |
| D-24 | Substitution window: 2 or 3 minutes?      | decided    | Grace  |        | 2 min, flag; easy to change |
| D-26 | Where Dispatch runs                       | open       | Eli    | 8 Apr  |          |
| D-27 | Korenwolf pilot: how orders are entered   | open       | Mo/Ana | 15 Apr |          |
| D-29 | Picker app: log library                   | decided    | Dee    |        | one line: team's choice |

Rules: one line per decision · open lines need an owner and a due date ·
significant → ADR · never delete; mark "superseded by D-NN".
"""),
    tools="tools: a Markdown table in the repo is enough. ADR tools generate the index (adr-tools <code>generate toc</code>, Log4brains); some teams keep open decisions on a board column or a spreadsheet, but link it from the repo.",
    gains=["<b>Open questions get owners</b> and dates before they block anyone.",
           "<b>Small decisions are recorded</b> without the weight of an ADR.",
           "<b>One place to look</b>: “was that decided?” takes ten seconds.",
           "<b>Delivery sees the risk</b>: overdue decisions show up next to the plan.",
           "<b>Finds the ADRs</b>: the log is their index."],
    losses=["<b>Needs a weekly habit</b>, or it goes stale in a month.",
            "<b>Duplicates</b> if open decisions also live on a board.",
            "<b>One line hides nuance</b>: small decisions lose their reasons.",
            "<b>Backfilling</b> the first time takes an afternoon."],
    baseline="Each line compares <b>decisions scattered across chats, tickets and memory, with ADRs only for some</b> to <b>one decision log with every decision, open or closed, reviewed weekly</b>.",
    ratings=[(2, 4, "Anyone can see what was decided and what's still open."),
             (2, 4, "Delivery, product and engineering look at the same list."),
             (2, 4, "Open questions get an owner and a date, so they get decided."),
             (2, 4, "Undecided questions surface weeks before they block a date."),
             (3, 3, "Doesn't change how reversible decisions are."),
             (2, 5, "Every decision has a line, a status and a link."),
             (3, 3, "Not about cost; due dates show the cost of waiting."),
             (3, 4, "A minute per line, ten minutes a week."),
             (2, 4, "Teams log their own small decisions without asking.")],
    pitfalls=[("Only closed decisions", "The log is a museum of past choices.", "log open questions the moment someone is waiting on them."),
              ("No owner", "“The team” owns D-26, so nobody does.", "one named person per open line."),
              ("A second home", "Open decisions live on a board and in the log, and disagree.", "pick one source of truth and link the other to it."),
              ("Never reviewed", "Due dates pass silently.", "ten minutes every week, overdue lines first.")],
    use=["Any project with a fixed date and many teams.",
         "When ADRs exist but nobody can find the small decisions.",
         "Before a launch, to see what's still open.",
         "Onboarding: a newcomer reads the log, then the ADRs that matter."],
    skip=["A two-person team where every decision is made at one desk.",
          "If a tracker already holds every decision and everyone uses it: link it, don't copy it."],
    related=["<b>Architecture decision records</b> (this volume)", "<b>Decision rights (RACI/DACI)</b> (this volume)", "<b>One-way vs two-way doors</b> (this volume)", "<b>Risk register</b> (Vol. 6)"],
    quiz=[("What does a decision log contain that a folder of ADRs doesn't?", "Open decisions, with owners and due dates, and small decisions that don't deserve an ADR."),
          ("Which decisions get an ADR, and which only a line?", "Significant, hard-to-reverse decisions get an ADR; small, reversible ones get one line."),
          ("What must every open line have?", "One named owner and a due date."),
          ("What happens to a decision that's replaced?", "It stays in the log, marked superseded by the new decision's number.")],
    try_it="Spend 45 minutes searching your team's chat and tickets from the last month for the words “decided”, “let's go with” and “agreed”. Put each one on a line of a new decision log, then add every open question you know of with an owner and a due date. Show the open lines at your next planning meeting.",
    remember="The judgements explain; the <span class=\"hl\">docket</span> shows what's still <span class=\"hl\">pending</span>, and who has it.",
    sources=["Michael Nygard, “Documenting Architecture Decisions” (2011), and the ADR index in adr-tools.",
             "Log4brains documentation: a browsable decision log generated from ADRs.",
             "Olaf Zimmermann, “Architectural Decisions: the Making Of” (2020), on decision backlogs.",
             "PMI, <i>PMBOK Guide</i>, on decision and issue logs."],
)

# ------------------------------------------------------------------ 03 RFCs & Design Docs
rfc_problem = Doodle(760, 290, "Doodle of two engineers building the new Dispatch service in March 2026 with two different designs in their heads. Ben, on the orders team, has Ordering call Dispatch directly over HTTP and wait for an answer. Eli, on the platform team, has Ordering publish events to Kafka that Dispatch reads. After two weeks the two halves of code don't fit together.",
                     "Two engineers, two designs in their heads, two weeks of code that doesn't fit together.")
rfc_problem.box(20, 30, 340, 170, None, "paper")
rfc_problem.head(190, 62, "Ben: “Ordering calls it”", size=17)
rfc_problem.box(40, 100, 120, 50, "Ordering", "blue", size=16)
rfc_problem.arrow(166, 125, 226, 125, label="HTTP", lx=196, ly=113)
rfc_problem.box(232, 100, 110, 50, "Dispatch", "green", size=16)
rfc_problem.note(190, 182, "sync: waits for an answer", "pen")
rfc_problem.box(400, 30, 340, 170, None, "paper")
rfc_problem.head(570, 62, "Eli: “it reads events”", size=17)
rfc_problem.box(410, 100, 95, 50, "Ordering", "blue", size=14)
rfc_problem.arrow(509, 125, 531, 125)
rfc_problem.box(535, 105, 70, 40, "Kafka", "y", size=14)
rfc_problem.arrow(609, 125, 631, 125)
rfc_problem.box(635, 100, 95, 50, "Dispatch", "green", size=14)
rfc_problem.note(570, 182, "async: events on Kafka", "pen")
rfc_problem.box(170, 222, 420, 52, "2 weeks of code that doesn't fit", "pink", stroke="red", size=17)

rfc_analogy = Doodle(760, 270, "Doodle of a planning application for a new building. The drawings are posted on the fence and online, neighbours and the people affected comment within a fixed window, and the council decides and issues a permit with its reasons, which stays on file.",
                     "A planning application: post the drawings, let the people affected comment by a date, then decide.")
for i, (ic, t, s, f) in enumerate([("board", "plans posted", "on the fence, online", "blue"), ("megaphone", "neighbours comment", "a fixed window", "y"), ("stamp", "council decides", "permit, with reasons", "green")]):
    x = 20 + i * 260
    rfc_analogy.icon(ic, x + 70, 18, 1.1)
    rfc_analogy.box(x, 106, 214, 80, t, f, sub=s, size=15)
    if i < 2:
        rfc_analogy.arrow(x + 218, 146, x + 256, 146)
rfc_analogy.note(380, 236, "anyone affected gets a say, by a known date", "pen")

rfc_how = Doodle(760, 320, "The life of RFC-003, Dispatch as a service. Eli and Ben write the draft together. It's open for comments for five working days with named reviewers. A 30-minute meeting settles what comments didn't. The decision is recorded as ADR 0008 and the RFC is frozen and linked. The RFC's sections: summary, goals, non-goals, proposal, alternatives, rollout and open questions.",
                 "Draft together, comment for five days, decide, then record the key decision as an ADR and freeze the RFC.")
for i, (t, s, f) in enumerate([("draft", "Eli + Ben write it", "blue"), ("comments", "5 working days", "y"), ("decide", "30 min, if needed", "paper"), ("ADR 0008", "RFC frozen, linked", "green")]):
    x = 10 + i * 193
    rfc_how.box(x, 30, 165, 80, t, f, sub=s, size=18, subsize=14)
    if i < 3:
        rfc_how.arrow(x + 169, 70, x + 189, 70)
rfc_how.note(295, 136, "named reviewers: Ana, Cho, Sanne", "pen", size=18)
rfc_how.box(120, 166, 520, 124, None, "paper")
rfc_how.head(380, 200, "RFC-003 · Dispatch as a service", size=18)
rfc_how.text(380, 238, "summary · goals · non-goals · proposal", size=16)
rfc_how.text(380, 268, "alternatives · rollout · open questions", size=16)

RFCS = dict(
    slug="rfcs-design-docs",
    kicker="a.k.a. “the planning application”",
    tldr="An ADR is one page about one decision. When a change is <b>big enough that people will build it differently in their heads</b>, write a <b>design doc</b> first and open it as an <b>RFC</b> (request for comments): goals, <b>non-goals</b>, the proposal, the <b>alternatives</b>, the rollout and the <b>open questions</b>. Give it named reviewers and a <b>fixed comment window</b>, settle what's left in one short meeting, then record the key decision as an <b>ADR</b> and freeze the RFC.",
    chips=[("Family", "recording decisions"), ("Origin", "IETF RFCs (1969); design docs at Google; RFC processes at Rust, Uber, Spotify"), ("Lives in", "docs/rfcs/ as a pull request"), ("Pairs with", "ADRs, options analysis, decision rights")],
    problem_side="Larder, 18 March 2026",
    problem="""  <p class="lead">ADR 0002 said: extract Dispatch first. Ben, on the orders team, and Eli, on platform, both start. Two weeks later their code doesn't fit: <b>Ben</b> has Ordering <b>call Dispatch over HTTP</b> and wait; <b>Eli</b> has Ordering <b>publish events</b> that Dispatch reads from Kafka. Both pictures were reasonable. Neither was written down, so <span class="hl-pink">nobody saw the difference</span> until the code met.</p>
  <ul>
    <li>A one-line decision (“extract Dispatch”) leaves the design to everyone's imagination.</li>
    <li>Big designs discussed in meetings reach only the people in the room.</li>
    <li>Without a comment window, review is either endless or skipped.</li>
  </ul>""",
    problem_figs=[rfc_problem],
    analogy_side="the planning application",
    analogy="""  <p>Before a building goes up, the <b>drawings are published</b>: on the fence and online. The <b>people affected</b> (neighbours, the fire service) can comment, but only within a <b>fixed window</b>. Then the council <b>decides</b>, with reasons, and the permit stays on file. Nobody pours concrete on a picture that lives in the architect's head.</p>""",
    analogy_figs=[rfc_analogy],
    map=[("The drawings", "The design doc: goals, proposal, alternatives, rollout"),
         ("Posting them publicly", "Opening it as an RFC pull request"),
         ("Neighbours and the fire service", "Named reviewers from the affected teams"),
         ("The comment window", "Five working days, then it closes"),
         ("The permit, with reasons", "The ADR for the key decision; the RFC is frozen")],
    how_side="write the picture down before the code",
    how="""  <p>An RFC is for changes that span teams or weeks: a new service, a new integration, a migration. The most useful sections are the ones people skip: <b>non-goals</b> (what this won't do) and <b>alternatives</b> (what else we considered). The RFC can be long; the ADR it produces stays one page.</p>""",
    how_figs=[rfc_how],
    steps=[("Decide if it needs one", "Spans teams, takes more than two weeks, or changes an interface others use → RFC. Otherwise an ADR or a line in the log."),
           ("Write the draft together", "The people who'll build it write it. Two to six pages; diagrams welcome."),
           ("Say what it won't do", "Non-goals stop scope creep and settle half the comments in advance."),
           ("Open it with a window", "A pull request in <code>docs/rfcs/</code>, named reviewers, a closing date: five working days."),
           ("Close it", "Resolve comments in the PR; a 30-minute meeting for the rest. The owner decides, not the loudest reviewer."),
           ("Record and freeze", "Write the ADR for the key decision, link it, mark the RFC accepted. Later changes are new RFCs or ADRs.")],
    vocab=[("RFC", "Request for comments: a proposal opened for review by a date."),
           ("Design doc", "The written design: problem, goals, proposal, alternatives, rollout."),
           ("Non-goals", "Things the design deliberately won't do."),
           ("Comment window", "The fixed time reviewers have to respond."),
           ("Named reviewer", "A person from an affected team who must read it."),
           ("Frozen", "Accepted and no longer edited; changes need a new record.")],
    code=dict(file="docs/rfcs/003-dispatch-as-a-service.md", note="RFC template, filled in (shortened)", plain=True, src="""
# RFC-003: Dispatch as a service
Authors: Eli (platform), Ben (orders)   Reviewers: Ana, Cho, Sanne
Status: accepted 2026-03-27 → ADR 0008  Comments close: 2026-03-25

## Summary
Move courier assignment out of Larder Core into a Dispatch service that
owns couriers, locations and assignments. Ordering tells it an order is
ready; Dispatch tells Ordering when it's collected and delivered.

## Goals
- Rotterdam opens on Dispatch (27 Apr); Amsterdam moves the week after.
- Courier locations every 5 s without touching the Core database.
## Non-goals
- New routing algorithm (separate evaluation, May). - Courier app changes.

## Proposal
Ordering publishes order.ready_for_dispatch via the outbox (ADR 0007).
Dispatch publishes courier.assigned, order.collected, order.delivered.
No synchronous calls from Ordering to Dispatch.

## Alternatives
A. Ordering calls Dispatch over HTTP: simpler, but checkout waits on it.
B. Dispatch reads Core tables directly: fast to build, couples the schemas.

## Rollout        RTM-0 test store → Rotterdam → Amsterdam, cron kept as fallback
## Open questions  Who owns courier shifts? (→ Joost, by 3 Apr)
"""),
    tools="tools: Markdown in the repo, reviewed as a pull request, works best. Google Docs or Notion with comments are fine for early drafts; move the final version next to the code. Templates: Google-style design docs, the Rust RFC template, “Design Docs at Google” (Malte Ubl).",
    gains=["<b>One shared picture</b> before anyone builds.",
           "<b>Everyone affected gets a say</b>, including people not in the meeting.",
           "<b>Non-goals and alternatives</b> stop the same debates resurfacing.",
           "<b>A fixed window</b>: review happens, and ends.",
           "<b>Better designs</b>: writing exposes the gaps a whiteboard hides."],
    losses=["<b>Days of writing</b> before code starts.",
            "<b>Can become bureaucracy</b> if every change needs one.",
            "<b>Bikeshedding</b>: easy topics get all the comments.",
            "<b>Goes stale</b> if people keep editing it after acceptance."],
    baseline="Each line compares <b>big designs agreed in meetings and built from memory</b> to <b>a written RFC with named reviewers and a comment window, ending in an ADR</b>.",
    ratings=[(2, 5, "The design is on paper, with goals, non-goals and alternatives."),
             (2, 5, "Every affected team reads and comments before building."),
             (3, 3, "Slower to start, much faster to finish: fewer rewrites."),
             (2, 4, "Gaps show up in review, not in integration."),
             (3, 3, "Alternatives are recorded, so switching later is informed."),
             (2, 5, "The RFC explains the design; the ADR the decision."),
             (3, 3, "Rollout and alternatives often mention cost; not the focus."),
             (4, 2, "Days of writing and reviewing per RFC."),
             (2, 4, "Teams propose designs themselves, through the same process.")],
    pitfalls=[("RFC for everything", "A two-day change waits a week for comments.", "only cross-team, multi-week or interface-changing work."),
              ("No closing date", "Comments trickle in for a month.", "a fixed window, then the owner decides."),
              ("Decided by comment count", "The longest thread wins.", "the owner weighs comments; the decision and its reasons go in the ADR."),
              ("A living document", "The RFC is edited after acceptance and no longer says what was agreed.", "freeze it; changes go in new RFCs or ADRs.")],
    use=["New services, integrations or migrations.",
         "Changes to interfaces other teams depend on.",
         "Work that spans more than one team or more than two weeks.",
         "When two people already picture the design differently."],
    skip=["Small, local changes: a pull request description is enough.",
          "A single clear-cut decision: write the ADR directly.",
          "Urgent fixes: fix first, write an ADR afterwards if it matters."],
    related=["<b>Architecture decision records</b> (this volume)", "<b>Decision rights (RACI/DACI)</b> (this volume)", "<b>Options analysis</b> (this volume)", "<b>Event-driven integration</b> (Vol. 4)"],
    quiz=[("When does a change need an RFC rather than just an ADR?", "When it spans teams or weeks, or changes an interface others use, so people need a shared design before building."),
          ("Why write non-goals?", "They stop scope creep and settle many review comments in advance."),
          ("How does an RFC end?", "Comments close on a fixed date, the owner decides, the key decision becomes an ADR and the RFC is frozen."),
          ("Who should write the RFC?", "The people who will build it, with the architect reviewing.")],
    try_it="Take the next change on your roadmap that touches more than one team. Write a two-page RFC with the template above, filling in non-goals and two alternatives. Open it as a pull request with three named reviewers and a five-day window, and note how many comments would otherwise have surfaced in integration.",
    remember="Publish the <span class=\"hl\">drawings</span> before you pour concrete. Comments close on a <span class=\"hl\">date</span>.",
    sources=["Malte Ubl, “Design Docs at Google” (industrialempathy.com, 2020).",
             "The Rust RFC process (github.com/rust-lang/rfcs).",
             "Gergely Orosz, “Engineering Planning with RFCs, Design Documents and ADRs” (The Pragmatic Engineer, 2022).",
             "Stephen D. Crocker, RFC 1, “Host Software” (IETF, 1969)."],
)

# ------------------------------------------------------------------ 04 Decision Rights (RACI/DACI)
dr_problem = Doodle(760, 300, "Doodle of a stuck decision at Larder in March 2026: should Larder add a second payment provider for peak days? Cho researched it in February. Marco thinks it's his because it costs money; Ana thinks it's architecture; Lena wants the contract reviewed first; Cho thinks she only did the research. Three weeks and four meetings later, nobody has said 'decided'.",
                    "Four people, each sure someone else decides, or sure they do. Three weeks, four meetings, no decision.")
dr_problem.box(250, 112, 260, 70, "second PSP?", "y", sub="researched in Feb")
for x, y, who, says in [(20, 20, "Marco", "“my budget”"), (540, 20, "Ana", "“it's architecture”"), (20, 200, "Lena", "“contract first”"), (540, 200, "Cho", "“I only researched”")]:
    dr_problem.box(x, y, 200, 62, who, "paper", sub=says)
    dr_problem.arrow(x + 100 + (80 if x < 300 else -80), y + (66 if y < 100 else -4), 380 + (-80 if x < 300 else 80), 147 + (-38 if y < 100 else 38), dash=True)
dr_problem.note(380, 290, "3 weeks · 4 meetings · nobody says “decided”", "red")

dr_analogy = Doodle(760, 260, "Doodle of planning a wedding. The planner drives it and keeps it moving. The couple approve: they say yes or no. Parents and the caterer contribute: they're heard before it's decided. The guests are informed: they're told the result.",
                    "A wedding: the planner drives, the couple decide, parents and caterer are heard, guests are told.")
for i, (letter, word, who, does, f) in enumerate([("D", "driver", "the planner", "keeps it moving", "blue"), ("A", "approver", "the couple", "say yes or no", "green"), ("C", "contributors", "parents, caterer", "are heard", "y"), ("I", "informed", "the guests", "are told", "paper")]):
    x = 10 + i * 188
    dr_analogy.head(x + 85, 52, letter, size=36)
    dr_analogy.note(x + 85, 82, word, "pen")
    dr_analogy.box(x, 106, 172, 90, who, f, sub=does, size=15, subsize=15)
dr_analogy.note(380, 236, "one approver, always", "green")

dr_how = Doodle(760, 340, "The DACI chart for Larder's decision D-22, a second payment provider. Driver: Cho, who does the work and keeps it moving. Approver: Marco, one person who says yes or no. Contributors: Ana, Lena and Sam, who are heard before it's decided. Informed: Femke, Priya and the teams, who are told afterwards. On the right, Larder's general decision rights: inside one module, the team decides; across modules or anything needing an ADR, the architect with the tech leads; spending over 1,000 euros a month, Marco; anything with personal data, Lena can veto. It was decided in eight days, on 2 April, as ADR 0009.",
                "One decision, four roles, one approver. And a standing table, so most decisions never need a chart.")
for i, (letter, who, does, f) in enumerate([("D", "Driver: Cho", "does the work, keeps it moving", "blue"), ("A", "Approver: Marco", "one person: yes or no", "green"), ("C", "Contributors: Ana, Lena, Sam", "heard before it's decided", "y"), ("I", "Informed: Femke, Priya, teams", "told afterwards", "paper")]):
    y = 20 + i * 70
    dr_how.box(20, y, 58, 56, letter, f, size=24)
    dr_how.head(92, y + 24, who, anchor="start", size=15)
    dr_how.text(92, y + 46, does, anchor="start", size=14)
dr_how.box(400, 20, 345, 276, None, "paper", dash=True)
dr_how.head(572, 52, "Larder's decision rights", size=17)
for i, (k, v) in enumerate([("inside one module", "→ the team"), ("across modules, ADRs", "→ Ana + tech leads"), ("> €1,000 a month", "→ Marco"), ("personal data", "→ Lena can veto"), ("city launch dates", "→ Femke")]):
    y = 92 + i * 42
    dr_how.text(414, y, k, anchor="start", size=15)
    dr_how.text(730, y, v, anchor="end", size=15)
dr_how.note(200, 324, "decided in 8 days: 2 Apr, ADR 0009", "green")

DECISION_RIGHTS = dict(
    slug="decision-rights",
    kicker="a.k.a. “who's actually getting married here?”",
    tldr="Many decisions don't stall because they're hard, but because <b>nobody knows who makes them</b>. Before a cross-team decision starts, name the roles: <b>DACI</b> (Driver, Approver, Contributors, Informed) or <b>RACI</b> (Responsible, Accountable, Consulted, Informed). The rule that matters: <b>exactly one approver</b>. Then write a small <b>standing table of decision rights</b> (“inside a module, the team decides; over €1,000 a month, the CFO”) so most decisions never need a chart at all.",
    chips=[("Family", "recording decisions"), ("Origin", "RACI from 1950s–70s project management; DACI popularised by Intuit and Atlassian"), ("Lives in", "the RFC or ADR header; a decision-rights page"), ("Pairs with", "decision log, RFCs, stakeholder map")],
    problem_side="Larder, 23 March 2026",
    problem="""  <p class="lead">December's risk-storming put a <b>payment provider outage at peak</b> on the top-five list. In February Cho researched a second provider. Then nothing happened. <b>Marco</b> thought it was his decision (it costs money); <b>Ana</b> thought it was architecture; <b>Lena</b> wanted to review the contract first; <b>Cho</b> thought she'd only been asked to research. After <span class="hl-pink">three weeks and four meetings</span>, nobody had said “decided”, and Rotterdam's opening was five weeks away.</p>
  <ul>
    <li>Everyone in the meeting has an opinion; nobody has the call.</li>
    <li>Two people who each think they decide are as bad as none.</li>
    <li>The architect becomes the default decider for everything, and a bottleneck.</li>
  </ul>""",
    problem_figs=[dr_problem],
    analogy_side="planning a wedding",
    analogy="""  <p>A wedding has lots of opinions and exactly <b>one couple</b>. The <b>planner</b> drives it: books, chases, keeps it moving. The <b>couple</b> approve: yes or no, and that's final. <b>Parents and the caterer</b> are heard before anything is decided. The <b>guests</b> are told the result. When the mother of the bride thinks she's the approver, that's when weddings go wrong.</p>""",
    analogy_figs=[dr_analogy],
    map=[("The planner", "Driver: Cho, who gathers facts and keeps it moving"),
         ("The couple", "Approver: Marco, one person, yes or no"),
         ("Parents and caterer", "Contributors: Ana, Lena, Sam, heard first"),
         ("The guests", "Informed: Femke, Priya and the teams"),
         ("Family rules (who pays for what)", "The standing decision-rights table")],
    how_side="name the roles, one approver",
    how="""  <p>For a <b>single big decision</b>, put a DACI line at the top of the RFC or ADR. For the <b>everyday flow</b>, agree a standing table once: which kinds of decision belong to teams, to the architect, to finance, to legal. The table is what gives teams autonomy: inside their area, they don't need to ask.</p>""",
    how_figs=[dr_how],
    steps=[("Spot the stuck decision", "Two meetings without a decision usually means unclear rights, not a hard problem."),
           ("Name one approver", "The person accountable for the outcome. Never a committee, never two people."),
           ("Name the driver", "Often not the approver: the one who gathers facts, writes the options and books the meeting."),
           ("List contributors and informed", "Contributors are heard before; informed are told after. Keep contributors few."),
           ("Set a date", "Put the decision in the log with its due date; the driver brings options by then."),
           ("Write the standing table", "Once a quarter: kinds of decision → who decides. Publish it next to the decision log.")],
    vocab=[("DACI", "Driver, Approver, Contributors, Informed."),
           ("RACI", "Responsible, Accountable, Consulted, Informed: the older variant."),
           ("Approver / Accountable", "The one person who makes the final call."),
           ("Driver", "The person who moves the decision forward."),
           ("Veto", "A right to block (e.g. the DPO on personal data), not to decide."),
           ("Decision rights", "A standing agreement on who decides which kinds of thing.")],
    code=dict(file="docs/decisions/D-22-second-psp.md", note="DACI header, filled in", plain=True, src="""
# D-22: Do we add a second payment provider before the Christmas peak?

Driver        Cho (payments)                    → options by 30 Mar
Approver      Marco (CFO)                       → decides 2 Apr
Contributors  Ana (architecture), Lena (contract, DPO: veto on data terms),
              Sam (support impact), Joost (ops on peak days)
Informed      Femke, Priya, all tech leads (in the Friday update)

Options       1. Stay with one provider; accept the risk (4 h outage ≈ €60k lost orders)
              2. Second provider for cards + iDEAL, manual switch-over
              3. Second provider with automatic failover per transaction

Decision      2 Apr: Option 2. Live before 1 Sep 2026. ~€900/month + fees.
              Option 3 revisited after the Christmas peak.     → ADR 0009

Larder's standing decision rights (2026 Q2)
  Inside one module, reversible        the team
  Across modules, or needs an ADR      Ana + the tech leads
  Spend over €1,000/month              Marco
  Personal data, contracts             Lena (can veto)
  City launch dates                    Femke
"""),
    tools="tools: a header in the RFC or ADR, or a one-page decision-rights table on the wiki. Atlassian's DACI template, RAPID (Bain) for big organisations, and the Team Topologies interaction modes for team-to-team decisions.",
    gains=["<b>Decisions get made</b>: someone owns the call.",
           "<b>Fewer, shorter meetings</b>: contributors give input, they don't vote.",
           "<b>Teams decide alone</b> where the standing table says they can.",
           "<b>No surprise vetoes</b>: legal and finance are named up front.",
           "<b>Less architect bottleneck</b>: Ana isn't the default for everything."],
    losses=["<b>Feels formal</b> for small teams.",
            "<b>Contributors can feel overruled</b> when the approver disagrees.",
            "<b>Charts nobody reads</b> if made for every decision.",
            "<b>Politics</b>: naming the approver can start an argument."],
    baseline="Each line compares <b>decisions made by whoever is in the room, with unclear rights</b> to <b>named DACI roles with one approver, plus a standing decision-rights table</b>.",
    ratings=[(2, 4, "Everyone knows who decides what."),
             (2, 4, "Contributors are heard on purpose; nobody is surprised."),
             (1, 5, "Stuck decisions move: D-22 took 8 days after 3 stuck weeks."),
             (2, 4, "Legal and finance vetoes surface before, not after."),
             (3, 3, "Doesn't change reversibility."),
             (2, 4, "Who decided, and who was heard, is on the record."),
             (2, 4, "Spending limits make cost a named part of the decision."),
             (3, 4, "A few lines per decision; one table per quarter."),
             (2, 5, "The standing table lets teams decide alone inside their area.")],
    pitfalls=[("Two approvers", "Marco and Femke both “approve”, so neither does.", "exactly one name in the A."),
              ("Contributors become voters", "The decision waits until all eight agree.", "contributors are heard; the approver decides."),
              ("A chart for everything", "DACI tables for library bumps.", "use the standing table; chart only stuck or cross-team decisions."),
              ("The architect approves all", "Every decision queues for Ana.", "push decisions to teams; keep the architect for the cross-cutting ones.")],
    use=["A decision that's been discussed twice without a result.",
         "Decisions that cross teams, budgets or legal lines.",
         "Big RFCs: put the roles in the header.",
         "A growing organisation where “who decides?” keeps coming up."],
    skip=["Decisions inside one team that the standing table already covers.",
          "Emergencies: the incident lead decides; tidy up later."],
    related=["<b>Decision log</b> (this volume)", "<b>RFCs &amp; design docs</b> (this volume)", "<b>Stakeholder map</b> (Vol. 1)", "<b>Influencing without authority</b> (Vol. 6)"],
    quiz=[("What do the letters in DACI stand for?", "Driver, Approver, Contributors, Informed."),
          ("What's the one rule you must not break?", "Exactly one approver."),
          ("How is a contributor different from an approver?", "Contributors are heard before the decision; the approver makes it."),
          ("Why write a standing decision-rights table?", "So most decisions don't need a chart: teams know what they can decide alone.")],
    try_it="Find the decision in your team that has been discussed most often without a result. Write a DACI header for it with one approver, a driver and a due date, and send it to the approver for a yes. Then draft five lines of standing decision rights for your team and ask your manager which ones they'd change.",
    remember="Lots of opinions, <span class=\"hl\">one couple</span>. Name the approver before the meeting, not after.",
    sources=["Atlassian Team Playbook, “DACI: a decision-making framework”.",
             "Paul Rogers and Marcia Blenko, “Who Has the D?” (Harvard Business Review, 2006), on RAPID.",
             "Matthew Skelton and Manuel Pais, <i>Team Topologies</i> (2019).",
             "Gregor Hohpe, <i>The Software Architect Elevator</i> (2020), on decision making."],
)

NOTES = [ADR, DECISION_LOG, RFCS, DECISION_RIGHTS]
