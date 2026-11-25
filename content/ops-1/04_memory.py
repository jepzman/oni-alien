# Series 2 · Book 5 · The IT Operations Notebook · Vol. 1 · Out of one head.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 1".

# ------------------------------------------------------------------ 14 Where Is That Written Down?
kn_problem = Doodle(760, 260, "Doodle of Larder's wiki on 1 June 2026: 312 pages, 40 percent not edited for more than a year, three different pages about restarting Larder Core that disagree, and none of them saying why Core has a second database user called legacy_rw. Jasper made it; Jasper left in August 2025. Dee tries to answer ten common operations questions from the wiki alone and manages three.",
                    "312 pages, three that disagree, and the one answer you need was in Jasper's head.")
kn_problem.icon("book", 40, 40, 1.6)
kn_problem.box(130, 30, 200, 90, "312 pages", "paper", sub="40 % older than a year", size=19, subsize=14)
kn_problem.box(350, 30, 190, 90, "3 restart pages", "pink", sub="that disagree", size=17, subsize=14)
kn_problem.box(560, 30, 186, 90, "legacy_rw", "pink", sub="why? (ask Jasper)", size=17, subsize=14)
kn_problem.box(130, 160, 500, 64, "Dee: 10 questions from the wiki → 3 answered", "y", size=17)

kn_analogy = Doodle(760, 220, "Doodle of a family recipe box. Each card is kept next to the dish it's for, says why a step matters ('rest the dough, or it shrinks'), and has a date. Grandma's cards nobody uses any more go in a separate 'old' box, not thrown away and not mixed in.",
                    "Recipe cards next to the dish, with the why written in, and the old ones in a separate box.")
kn_analogy.icon("recipe", 60, 40, 1.6)
kn_analogy.box(160, 40, 300, 100, "“rest the dough 30 min”", "y", sub="or it shrinks in the oven", size=17, subsize=14)
kn_analogy.box(490, 40, 256, 100, "the old box", "paper", sub="kept, not mixed in", size=17, subsize=14)
kn_analogy.note(450, 190, "the why makes it safe to change", "pen", size=18)

kn_how = Doodle(760, 360, "Eli's knowledge rules from 1 June 2026. Operations docs move from the wiki into the repo, next to the service, in a folder ops/services. Every service page has the same five headings: what it is, owner and tier, depends on (the map), how to run it (links to runbooks), and why it's like this (with links to Ana's decision records). The wiki's 312 pages: 120 archived, 61 moved and rewritten, the rest left for other teams. Dee repeats the test with ten questions on 30 June and answers eight.",
                "Docs next to the code, five headings per service, the why written in. Dee's test: 3 → 8 of 10.")
for i, (t, f) in enumerate([("what it is", "paper"), ("owner + tier", "paper"), ("depends on", "blue"), ("how to run it", "green"), ("why it's like this", "y")]):
    kn_how.box(14 + i * 148, 14, 136, 80, t, f, size=15)
kn_how.row([("120", "archived", "paper"), ("61", "moved + rewritten", "green"), ("131", "left for other teams", "paper")], x=14, y=130, h=84, w=232, gap=18, size=24, subsize=14)
kn_how.box(110, 246, 540, 70, "Dee's test, 30 June: 8 of 10 answered from the docs", "green", size=16)
kn_how.note(380, 344, "legacy_rw: found in an old chat, written down, then removed in July", "pen", size=16)

KNOWLEDGE = dict(
    slug="knowledge",
    kicker="a.k.a. “knowledge management”",
    tldr="Operations knowledge is useful only if the person on call can <b>find it, trust it and act on it</b>. Keep it <b>next to what it describes</b> (service pages and runbooks in the repo), use <b>the same few headings</b> everywhere, write down <b>why</b> things are the way they are as well as how, and <b>prune</b>: an archive is fine, but three pages that disagree are worse than none. Test it by asking someone to answer real questions from the docs alone.",
    chips=[("Family", "out of one head"), ("Lives in", "ops/services/ in the repo; the wiki only for history"), ("Pairs with", "runbooks, the dependency map, decision records (Ana)")],
    itil=dict(groups=["general"], chain=["improve", "deliver", "engage"], practices=["knowledge management"],
              sre="“documentation as code”; reducing the bus factor", principles=["Collaborate and promote visibility", "Keep it simple and practical"],
              older="ITIL v3: knowledge management, the service knowledge management system (SKMS)"),
    problem_side="Larder, 1 June 2026",
    problem="""  <p class="lead">Larder's wiki has <b>312 pages</b>. 40 % haven't been edited for more than a year, and <b>three different pages</b> about restarting Larder Core disagree with each other. None of them says why Core has a second database user called <code>legacy_rw</code>: Jasper created it, and Jasper left in August 2025. On 1 June Dee tries to answer ten everyday operations questions from the wiki alone. <span class="hl-pink">She manages three.</span></p>
  <ul>
    <li>Old pages look as true as new ones.</li>
    <li>The how is sometimes there; the why almost never.</li>
    <li>So people ask Eli, and the rota stays one person deep.</li>
  </ul>""",
    problem_figs=[kn_problem],
    analogy_side="the family recipe box",
    analogy="""  <p>A good family recipe box keeps each card <b>by the dish it's for</b>. The cards say <b>why</b> a step matters: “rest the dough 30 minutes, or it shrinks in the oven”. Then a cousin can change the recipe without ruining it. Grandma's cards nobody uses any more go into <b>a separate old box</b>. They're kept, but not mixed in with the ones you cook from.</p>""",
    analogy_figs=[kn_analogy],
    map=[("A card by its dish", "A service page next to the service's code"),
         ("“Rest the dough, or it shrinks”", "“Why it's like this”, with links to decision records"),
         ("Same layout on every card", "Five headings on every service page"),
         ("The old box", "The archived wiki pages"),
         ("A cousin cooks it alone", "Dee answers questions from the docs alone")],
    how_side="next to the code, five headings, the why, and a test",
    how="""  <p>Eli's rules, from <b>1 June</b>:</p>
  <ul>
    <li><b>Docs live next to what they describe.</b> Each service gets a page in <code>ops/services/</code> in the repo, reviewed like code, and updated in the same pull request as the change.</li>
    <li><b>Five headings, always:</b> what it is · owner and tier · depends on (the map) · how to run it (links to runbooks) · <b>why it's like this</b>, with links to Ana's decision records.</li>
    <li><b>Prune on purpose.</b> Of the 312 wiki pages, 120 are archived (kept and marked, but not searchable by default), 61 are moved and rewritten, and the rest belong to other teams.</li>
    <li><b>Ask the people who remember.</b> <code>legacy_rw</code>'s reason turns up in an old chat from 2024: a one-off data import. It goes into the “why” section, and in July the user is removed.</li>
  </ul>
  <p>On <b>30 June</b> Dee repeats her test with ten new questions. This time she answers <b>eight</b> from the docs alone.</p>""",
    how_figs=[kn_how],
    steps=[("Test first: ten questions, docs only", "Ask someone other than the author."),
           ("Put service docs next to the code", "Changed in the same pull request."),
           ("Use the same headings everywhere", "People find things by position."),
           ("Write the why, with links", "Decision records, tickets, incidents."),
           ("Archive instead of leaving stale pages", "Kept, marked, out of the way."),
           ("Repeat the test every quarter", "With new questions and a new person.")],
    vocab=[("Knowledge management", "Making sure the right information can be found and trusted when it's needed."),
           ("Docs as code", "Documentation kept in the repo and reviewed like code."),
           ("Tacit knowledge", "What someone knows but has never written down."),
           ("Bus factor", "How many people would have to leave before nobody knows how something works."),
           ("Archive", "Old pages kept for history, marked and kept out of everyday search."),
           ("Decision record", "A short note of a decision and its reasons (Ana's ADRs).")],
    code=dict(file="ops/services/stock-sync.md", note="a service page in the five headings · 3 June 2026", plain=True, src="""
# stock sync (Larder Core ↔ StockPilot)

What it is        Every 5 min, Core asks StockPilot for stock changes per store
                  and writes them to the product table. Customers see it as
                  "in stock" / "out of stock".
Owner · tier      Eli · important
Depends on        StockPilot API (vendor, business-hours support) · Core VM 1
                  · Postgres · see ops/services/maps/stock-sync.svg
How to run it     restart: RB-09 · stuck queue: RB-10 · vendor down: vendors.md
Why it's like this  Polling, not webhooks: StockPilot had no webhooks in 2024
                  (Jasper, chat 12 Mar 2024). 5 min = their rate limit at the
                  time. Contract ends June 2027: see ADR 0016 (warehouse).
Known weak spot   Restarted ~3×/week (toil, see 2026-06 toil log) → problem
"""),
    tools="tools: markdown in the repo, a search that covers it, and an archive flag on the old wiki. No new tool needed.",
    ladder=[("ask the person who knows", ["Wiki pages that disagree.", "The why is missing."]),
            ("service pages next to the code", ["Five headings, the why included.", "Tested quarterly."]),
            ("checked in CI", ["A new service can't merge without its page.", "Links to runbooks are checked."]),
            ("generated where possible", ["Owner, tier and map filled in from config.", "People write only the why."])],
    ladder_now=1,
    baseline="Each line compares <b>312 wiki pages of mixed age</b> to <b>service pages next to the code with five headings and a quarterly test</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 3, "Answers are found faster during incidents."),
             (2, 3, "The why makes it safer to change old things."),
             (1, 4, "Dee's test: 3 → 8 of 10."),
             (3, 3, "Fewer “quick questions” to Eli."),
             (3, 3, "Neutral."),
             (1, 3, "The bus factor goes from one."),
             (3, 3, "About three days, then minutes per change.")],
    pitfalls=[("Writing only the how", "People follow the steps, but can't tell when they no longer apply.", "a “why it's like this” section on every page."),
              ("Keeping everything live", "Stale pages are trusted by mistake.", "archive on purpose."),
              ("Docs far from the code", "They drift on the first change.", "change them in the same pull request."),
              ("Never testing", "The author thinks it's clear.", "someone else answers real questions from the docs alone.")],
    use=["People ask one person instead of reading.", "Pages disagree, or nobody knows how old they are.", "Someone important has left.", "Before sharing on-call more widely."],
    skip=["Truly throwaway work: a scratch script for one afternoon."],
    related=["<b>What Do I Do at 3 a.m.?</b> (this volume)", "<b>What Is Connected to What?</b> (this volume)", "<b>Architecture Decision Records</b> (Ana, vol. 2)", "<b>Docs as Code</b> (Ana, vol. 3)"],
    quiz=[("What are Larder's five headings for a service page?", "What it is; owner and tier; depends on; how to run it; why it's like this."),
          ("Why write the why, not just the how?", "So people can tell when the steps no longer apply, and change old things safely."),
          ("What's the difference between archiving and deleting?", "Archived pages are kept for history but marked and kept out of everyday search."),
          ("How does Eli test the docs?", "Someone else answers ten real questions from the docs alone (Dee: 3 → 8)."),
          ("What is the bus factor?", "How many people would have to leave before nobody knows how something works.")],
    quiz_sit=[("You find a strange cron job nobody can explain. What do you do before deleting it?", "Search old chats, tickets and commit history for its reason, ask whoever might remember, write down what you find in the service's “why” section, and then remove it on purpose, with a way back.")],
    try_it="Write ten questions a new on-call person would ask about your systems. Give them to a colleague who didn't write the docs, and count how many they can answer from the docs alone. Rewrite the page behind the first one they couldn't.",
    remember="If the answer is only <span class=\"hl\">in someone's head</span>, it leaves when they do. Write the <span class=\"hl\">why</span> next to the how.",
    sources=["AXELOS, <i>ITIL 4: Knowledge management</i> practice guide (2020).",
             "Andrew Etter, <i>Modern Technical Writing</i> (2016): docs as code.",
             "Michael T. Nygard, “Documenting Architecture Decisions” (2011)."],
)

# ------------------------------------------------------------------ 15 Why Am I Always Busy?
tl_problem = Doodle(760, 260, "Doodle of Eli's time log for the week of 8 to 12 June 2026. Of about 40 hours, 16.5 are toil: patching three virtual machines by hand, 5 hours; restarting the stock sync three times, 2 hours; renewing certificates by hand, 1 hour; copying weekly store figures into a spreadsheet for Joost, 2 hours; resetting things nobody else could reset, 3.5 hours; small manual fixes, 3 hours. That's 41 percent of his week, and it grows with every store.",
                    "41 % of the week was handwork that grows with every store.")
items = [("patching VMs", 5), ("stock sync restarts", 2), ("certificates", 1), ("store figures", 2), ("resets", 3.5), ("small fixes", 3)]
x = 14
for t, h in items:
    w = round(h * 44)
    tl_problem.box(x, 30, w - 4, 90, None, "pink")
    tl_problem.text(x + w / 2 - 2, 82, f"{h:g} h", size=15)
    x += w
tl_problem.box(x, 30, 746 - x, 90, "everything else", "paper", size=15)
tl_problem.note(380, 150, "patching · sync restarts · certs · store figures · resets · fixes", "pen", size=15)
tl_problem.box(110, 176, 540, 60, "16.5 h of 40 = 41 % toil", "pink", stroke="red", size=19)

tl_analogy = Doodle(760, 220, "Doodle of a farmer carrying water from the well to the animals in buckets every morning: two hours a day, and more with every new animal. One day she spends a week laying a pipe and a trough. The buckets weren't hard work, but they never ended, and they grew with the herd.",
                    "Carrying buckets every morning isn't hard. It just never ends, and it grows with the herd.")
tl_analogy.icon("bucket", 60, 40, 1.4)
tl_analogy.box(150, 40, 270, 100, "buckets", "pink", sub="2 h a day · grows with the herd", size=19, subsize=13)
tl_analogy.arrow(426, 90, 480, 90)
tl_analogy.box(486, 40, 260, 100, "a pipe", "green", sub="a week once, then nothing", size=19, subsize=14)
tl_analogy.note(450, 190, "toil: manual, repetitive, grows with scale, no lasting value", "pen", size=17)

tl_how = Doodle(760, 380, "Eli's toil budget from 15 June 2026. Toil is capped at 50 percent of the platform engineer's week, with a target of 30 percent by December. Every Friday, 10 minutes: log the week's toil by kind. Every month: pick the biggest item and remove it for good. June: copying store figures, replaced by a dashboard Joost can open himself. Next in line: stock sync restarts (a problem to fix, volume 2), VM patching (volume 3), certificates (automatic renewal). By the end of July the share is 33 percent.",
                "Log it weekly, cap it at 50 %, remove the biggest piece every month. 41 % → 33 % by the end of July.")
tl_how.box(14, 14, 230, 100, "log weekly", "y", sub="Fri, 10 min, by kind", size=19, subsize=14)
tl_how.box(264, 14, 230, 100, "cap 50 %", "pink", sub="target 30 % by Dec", size=19, subsize=14)
tl_how.box(514, 14, 232, 100, "remove one a month", "green", sub="the biggest, for good", size=17, subsize=14)
for i, (m, t, f) in enumerate([("Jun", "store figures → dashboard", "green"), ("Jul", "certificates → auto-renew", "green"),
                               ("Sep", "stock sync restarts → problem (vol. 2)", "y"), ("2027", "VM patching (vol. 3)", "paper")]):
    tl_how.box(14, 140 + i * 50, 80, 42, m, "paper", size=15)
    tl_how.box(104, 140 + i * 50, 642, 42, t, f, size=15)
tl_how.note(380, 356, "41 % (June) → 33 % (end of July)", "green", size=18)

TOIL = dict(
    slug="toil",
    kicker="a.k.a. “eliminating toil”",
    tldr="<b>Toil</b> is operational work that is <b>manual, repetitive, could be automated, and grows as the business grows</b>, and that leaves nothing lasting behind. A little is normal; too much crowds out every improvement and burns people out. <b>Measure it</b> for a few weeks, <b>cap it</b> (SRE teams use 50 % of the week), and <b>remove the biggest piece every month</b>, for good.",
    chips=[("Family", "out of one head"), ("Lives in", "ops/toil-log.md, ten minutes every Friday"), ("Pairs with", "runbooks, service requests, problem management (vol. 2)")],
    itil=dict(groups=["general"], chain=["improve", "deliver"], practices=["continual improvement", "workforce and talent management"],
              sre="“toil”, and the 50 % cap on operational work", principles=["Optimise and automate", "Progress iteratively with feedback"],
              older="ITIL v3: continual service improvement (CSI)"),
    problem_side="Larder, 8–12 June 2026",
    problem="""  <p class="lead">Ten weeks after the 160 % week, Eli has a rota, a desk queue, runbooks and a catalogue, and he's still always busy. So for the week of <b>8–12 June</b> he logs every hour. <b>16.5 of 40</b> are toil: patching three VMs by hand (5 h), restarting the stock sync three times (2 h), renewing certificates by hand (1 h), copying store figures into a spreadsheet for Joost (2 h), resets only he can do (3.5 h) and small manual fixes (3 h). <span class="hl-pink">41 % of his week, and every item grows with every new store.</span></p>
  <ul>
    <li>Toil feels productive, because something got done.</li>
    <li>It crowds out the work that would remove it.</li>
    <li>With six cities planned, it grows faster than any hiring plan.</li>
  </ul>""",
    problem_figs=[tl_problem],
    analogy_side="the farmer's buckets",
    analogy="""  <p>A farmer carries water from the well to her animals <b>in buckets every morning</b>: two hours a day, and more with every new animal. It isn't hard work, it just <b>never ends, and it grows with the herd</b>. One week she lays <b>a pipe and a trough</b>. That week is harder than any morning with the buckets. After it, the two hours are hers again, and the next ten animals cost nothing extra.</p>""",
    analogy_figs=[tl_analogy],
    map=[("Carrying buckets", "Patching VMs, restarting the sync, copying figures"),
         ("More animals, more buckets", "More stores, more handwork"),
         ("A week laying the pipe", "A day building the dashboard, or fixing the sync for good"),
         ("Two hours back every morning", "Toil down from 41 % to 33 %"),
         ("Counting the trips", "The Friday toil log")],
    how_side="log it, cap it, remove the biggest piece monthly",
    how="""  <p>Eli uses the SRE definition of toil (manual, repetitive, automatable, grows with scale, no lasting value) and sets up three habits from <b>15 June</b>:</p>
  <ul>
    <li><b>Log it weekly.</b> Ten minutes every Friday: hours of toil by kind.</li>
    <li><b>Cap it.</b> Toil may take at most <b>50 %</b> of the platform engineer's week, with a target of <b>30 % by December</b>. Over the cap, improvement work comes first, and Eli says so at tech leads.</li>
    <li><b>Remove the biggest piece every month</b>, for good. In June it's the store figures: a dashboard Joost opens himself saves 2 hours a week. In July, certificates move to automatic renewal. Stock sync restarts aren't toil to automate: they're a <b>problem</b> to fix (vol. 2). VM patching waits for the platform work (vol. 3).</li>
  </ul>
  <p>By the end of July Eli's toil is <b>33 %</b>. The log has a second use: it's the evidence for the second platform engineer Femke approves in August.</p>""",
    how_figs=[tl_how],
    steps=[("Log every hour for two weeks", "By kind of task, honestly."),
           ("Mark what is toil", "Manual, repetitive, automatable, grows with scale, no lasting value."),
           ("Set a cap and a target", "At most 50 %; aim lower."),
           ("Remove the biggest piece each month", "For good, not with a quicker manual trick."),
           ("Tell problems from toil", "Some toil is a symptom: fix the cause."),
           ("Use the log as evidence", "For hiring, for priorities, for saying no.")],
    vocab=[("Toil", "Manual, repetitive, automatable operational work that grows with scale and leaves nothing lasting."),
           ("Overhead", "Necessary work that isn't toil: meetings, planning, reviews."),
           ("Toil budget", "The share of time toil is allowed to take."),
           ("Engineering work", "Work that leaves the system better, so tomorrow needs less effort."),
           ("Automation", "Turning repeated steps into something that runs without a person."),
           ("Symptom", "Toil caused by a fault: fix the fault, don't automate the restart.")],
    code=dict(file="ops/toil-log.md", note="Fridays from 12 June 2026", plain=True, src="""
week        patch  sync  certs  figures  resets  fixes  toil h / 40   share
08–12 Jun    5.0   2.0   1.0    2.0      3.5     3.0    16.5          41 %
15–19 Jun    5.0   1.5   1.0    0.5 ✓    2.0     2.5    12.5          31 %
22–26 Jun    5.0   2.5   0.5    0        1.5     3.5    13.0          33 %
…
27–31 Jul    5.0   2.0   0 ✓    0        1.0     5.0    13.0          33 %

cap 50 % · target 30 % by December
removed: Jun store figures → dashboard (Joost) · Jul certificates → auto-renew
next:    stock sync restarts → problem PRB-003 (not a script!) · VM patching (2027)
"""),
    tools="tools: a plain table, ten minutes on Fridays, and the discipline to log honestly.",
    ladder=[("busy and can't say why", ["Toil invisible.", "Improvements never start."]),
            ("logged weekly, capped", ["Biggest piece removed monthly.", "Share tracked."]),
            ("toil tracked per service", ["Each service's toil visible to its owner.", "Automation planned from it."]),
            ("toil designed out", ["New services launch with their toil automated.", "The cap is rarely tested."])],
    ladder_now=1,
    baseline="Each line compares <b>a busy week nobody measures</b> to <b>a weekly toil log, a 50 % cap and one removal a month</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 3, "Fixing causes (not restarts) makes things break less."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Where time goes is visible to everyone."),
             (1, 4, "41 % → 33 % in seven weeks."),
             (2, 4, "Evidence for the second hire."),
             (2, 4, "Room to breathe, and a case for help."),
             (3, 3, "Ten minutes a week.")],
    pitfalls=[("Automating a symptom", "A script restarts the sync every hour, and the fault is never fixed.", "ask whether it's a problem first."),
              ("Logging from memory", "Toil looks smaller than it is.", "log every Friday, by kind."),
              ("No cap", "Toil quietly eats the whole week again.", "50 % at most, said out loud."),
              ("Swapping toil for faster toil", "A quicker manual trick, still every week.", "remove it for good, or it isn't removed.")],
    use=["You're busy but nothing improves.", "Work grows with every new site or customer.", "You need evidence for help or priorities.", "One person does all the handwork."],
    skip=["Work that's done once: that's a project, not toil."],
    related=["<b>Why Did It Really Happen?</b> (vol. 2)", "<b>Can I Have a New Handheld?</b> (this volume)", "<b>What Is IT Operations For?</b> (this volume)", "<b>Who Is Overloaded?</b> (Sanne, vol. 4)"],
    quiz=[("What makes work toil?", "It's manual, repetitive, could be automated, grows with scale, and leaves nothing lasting."),
          ("What cap does SRE put on operational work?", "About 50 % of the week; the rest goes to engineering work."),
          ("Why isn't the stock sync restart solved with a script?", "It's a symptom of a fault; the fault should be found and fixed (problem management)."),
          ("What did Eli remove first, and why?", "Copying store figures: the biggest piece he could remove for good in a day, with a dashboard Joost uses himself."),
          ("What else is the toil log good for?", "Evidence: for priorities, for saying no, and for hiring the second platform engineer.")],
    quiz_sit=[("A new store doubles the weekly resets. Eli suggests a script that resets every device nightly. What do you ask?", "Why do the devices need resetting at all? If there's a fault behind it, the nightly reset just hides it. Find the cause before automating.")],
    try_it="Log your work for one week in half-hour blocks. Mark what's toil by the five tests. What share is it? Pick the biggest piece and remove it for good this month.",
    remember="Toil isn't hard, it just <span class=\"hl\">never ends</span> and <span class=\"hl\">grows with the business</span>. Count it, cap it, and lay one pipe a month.",
    sources=["Betsy Beyer et al., <i>Site Reliability Engineering</i> (2016): chapter 5, eliminating toil.",
             "Betsy Beyer et al., <i>The Site Reliability Workbook</i> (2018): chapter 6, eliminating toil.",
             "AXELOS, <i>ITIL 4: Continual improvement</i> practice guide (2020)."],
)

NOTES = [KNOWLEDGE, TOIL]
