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

NOTES = [ADR]
