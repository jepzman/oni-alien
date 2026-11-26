# Series 2 · Book 5 · The IT Operations Notebook · Vol. 3 · Keeping it current.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 3".

# ------------------------------------------------------------------ 13 Who May Touch Production?
pa_problem = Doodle(760, 260, "Doodle of Eli's access count on 1 March 2027: 11 people can change the production database, 14 can log in to Larder Core's virtual machines, and there are 2 shared admin accounts whose password sits in a shared vault that 9 people can open. Several of these people never use production in their normal work. Nobody would know who did what with a shared account.",
                    "11 people can change the production database, 14 can log in to the VMs, and two shared admin accounts.")
pa_problem.row([("11", "can change prod DB", "pink"), ("14", "can log in to Core VMs", "pink"), ("2", "shared admin accounts", "pink")], x=14, y=30, h=100, w=232, gap=18, size=30, subsize=14)
pa_problem.note(380, 176, "shared password · 9 people can open the vault", "red", size=18)
pa_problem.note(380, 214, "who did what? unknowable with a shared account", "pen", size=17)

pa_analogy = Doodle(760, 220, "Doodle of a hotel's keys. Housekeeping key cards open guest rooms only during their shift and are logged. The master key is in a sealed envelope in the safe; opening it rings the manager and is written in the book. Nobody carries a master key 'just in case'.",
                    "Keys that work only on shift, and a master key in a sealed envelope that rings the manager when opened.")
pa_analogy.icon("keycard", 60, 40, 1.5)
pa_analogy.box(170, 40, 270, 100, "shift key cards", "green", sub="time-limited · logged", size=18, subsize=14)
pa_analogy.icon("vault", 480, 50, 1.2)
pa_analogy.box(560, 40, 186, 100, "master key", "pink", sub="sealed · rings the manager", size=17, subsize=13)
pa_analogy.note(450, 190, "nobody carries the master key just in case", "pen", size=18)

pa_how = Doodle(760, 380, "Larder's production access from April 2027. Standing access: only Eli and Bram, for the platform, through personal accounts with two-factor sign-in. Everyone else: access on request through a chat command, with a reason, for 4 hours, posted to the change feed and approved by a second person (for the database, Eli or Bram). Break-glass: one emergency account, its credentials sealed in the vault, usable only when the request path is down; opening it pages Eli and messages Femke, and it is reviewed the next day. The two shared admin accounts deleted on 9 April. Quarterly review of who has what. Requests in May: 31, median wait 6 minutes.",
                "Two people with standing access; everyone else on request for 4 hours; break-glass that alarms.")
pa_how.box(14, 14, 236, 120, "standing", "y", sub="Eli + Bram only · personal · 2FA", size=19, subsize=12)
pa_how.box(262, 14, 236, 120, "on request", "green", sub="reason · 4 h · second person · in the feed", size=19, subsize=12)
pa_how.box(510, 14, 236, 120, "break-glass", "pink", sub="sealed · pages Eli + Femke", size=19, subsize=12)
pa_how.box(14, 160, 732, 64, "shared admin accounts: deleted 9 April · quarterly review of who has what", "paper", size=15)
pa_how.row([("before", "11 DB · 14 VM · 2 shared", "pink"), ("after", "2 standing · 31 requests in May, 6 min wait", "green")], x=110, y=250, h=86, w=250, gap=40, size=18, subsize=12, arrows=True)

PROD_ACCESS = dict(
    slug="production-access",
    kicker="a.k.a. “privileged access”",
    tldr="Every standing permission to change production is a door that can be used by mistake, or by someone else. Keep <b>standing access to the few who need it daily</b>, give everyone else <b>access on request, for a few hours, with a reason and a second person</b>, put every grant in the change feed, and keep one <b>break-glass</b> account for emergencies that <b>raises an alarm</b> when it's used. No shared accounts: every action belongs to a person.",
    chips=[("Family", "keeping it current"), ("Lives in", "the identity provider, the access request command, ops/access.md"), ("Pairs with", "joiners and leavers (vol. 1), change feed (vol. 2), access reviews (vol. 5)")],
    itil=dict(groups=["general", "technical"], chain=["deliver", "improve"], practices=["information security management", "infrastructure and platform management"],
              sre="(least privilege; audited, time-limited access)", principles=["Keep it simple and practical", "Collaborate and promote visibility"],
              older="ITIL v3: access management"),
    problem_side="Larder, 1 March 2027",
    problem="""  <p class="lead">Eli counts production access on <b>1 March</b>. <b>11 people</b> can change the production database. <b>14</b> can log in to Larder Core's VMs. There are <b>2 shared admin accounts</b>, and their password sits in a vault that 9 people can open. Several of them never use production in their normal work. <span class="hl-pink">If something were changed by a shared account, nobody could say who did it.</span> Korenwolf's security questionnaire for the renewal will ask exactly this.</p>
  <ul>
    <li>Access granted once for a reason, and never taken back.</li>
    <li>Mistakes are possible for people who don't usually work in production.</li>
    <li>Shared accounts make the change feed and reviews meaningless.</li>
  </ul>""",
    problem_figs=[pa_problem],
    analogy_side="the hotel's keys",
    analogy="""  <p>In a hotel, housekeeping key cards open guest rooms <b>only during the shift</b>, and every use is logged. The <b>master key</b> is in a sealed envelope in the safe, and opening it rings the manager and goes in the book. Nobody carries a master key <b>“just in case”</b>, however senior they are.</p>""",
    analogy_figs=[pa_analogy],
    map=[("Housekeeping on shift", "Eli and Bram: standing access for daily platform work"),
         ("A key card for one shift", "Access on request: a reason, 4 hours, a second person"),
         ("Logged use", "Every grant in the change feed"),
         ("The master key in the safe", "Break-glass account, sealed"),
         ("Opening it rings the manager", "Using it pages Eli and messages Femke")],
    how_side="few standing, the rest on request, break-glass with an alarm",
    how="""  <p>From <b>April</b>:</p>
  <ul>
    <li><b>Standing access</b>: only <b>Eli and Bram</b>, for the platform, through personal accounts with two-factor sign-in.</li>
    <li><b>On request</b>: everyone else asks with a chat command, giving a <b>reason</b>. A <b>second person</b> approves (for the database: Eli or Bram), access lasts <b>4 hours</b>, and the grant is posted to the change feed. Ben, Cho and Dee still have production access, just not always.</li>
    <li><b>Break-glass</b>: one emergency account, credentials sealed in the vault, for when the request path itself is down. Opening it <b>pages Eli and messages Femke</b>, and its use is reviewed the next day.</li>
    <li>The two <b>shared admin accounts are deleted</b> on <b>9 April</b>, after every script using them is moved to its own service account.</li>
    <li>Who has what is <b>reviewed quarterly</b>.</li>
  </ul>
  <p>In May there are <b>31 requests</b>, with a <b>median wait of 6 minutes</b>. In May Ana's ADR 0021 moves all staff tools behind one identity provider, which makes the requests one click.</p>""",
    how_figs=[pa_how],
    steps=[("Count who can change production", "Database, servers, cloud console, shared accounts."),
           ("Keep standing access for daily work only", "Usually two or three people."),
           ("Make access on request fast", "A reason, a second person, a few hours, minutes to get."),
           ("Log every grant", "In the change feed, with the reason."),
           ("Seal a break-glass account that alarms", "For when the normal path is down."),
           ("Delete shared accounts; review quarterly", "Every action belongs to a person.")],
    vocab=[("Privileged access", "Access that can change or read sensitive parts of production."),
           ("Least privilege", "Each person has only the access their work needs."),
           ("Just-in-time access", "Access granted when needed, for a limited time."),
           ("Break-glass account", "An emergency account, sealed, whose use raises an alarm."),
           ("Service account", "A non-human account for a script or system, with its own permissions."),
           ("Standing access", "Access that is always on.")],
    code=dict(file="ops/access.md", note="from April 2027", plain=True, src="""
# Production access

standing      Eli, Bram · platform · personal accounts · 2FA
on request    /prod-access <system> <reason>   → approver (DB: Eli or Bram;
              Dispatch: Ben; payments: Cho) → 4 hours → posted to the change feed
break-glass   account "glass-01" · sealed in the vault (2 keyholders)
              use = page Eli + message Femke · reviewed next working day
shared admin  larder-admin, core-root: deleted 9 Apr 2027 (scripts → service accounts)
review        quarterly: who has what, every service account's owner

1 Mar: 11 can change prod DB · 14 VM logins · 2 shared accounts
May:   2 standing · 31 requests · median wait 6 min · break-glass used 0×
"""),
    tools="tools: the identity provider's groups, a small chat command for requests, the vault for break-glass, and the change feed.",
    ladder=[("everyone, always", ["Standing access collected over years.", "Shared accounts."]),
            ("few standing, the rest on request", ["Time-limited, approved, logged.", "Break-glass with an alarm."]),
            ("access through one identity provider", ["Requests one click.", "Expiry automatic."]),
            ("hardly needed", ["Most production work through the pipeline.", "Human access rare and short."])],
    ladder_now=1,
    baseline="Each line compares <b>11 people with standing database access and two shared accounts</b> to <b>two standing, time-limited requests and break-glass</b>.",
    ratings=[(2, 3, "Fewer accidental production changes."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral: requests take minutes."),
             (2, 4, "Every production action has a person and a reason."),
             (1, 4, "Who had access when is in the feed."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Six minutes per request.")],
    pitfalls=[("Requests that take a day", "People hoard access instead.", "make requests fast: minutes."),
              ("Break-glass nobody watches", "It becomes the easy way in.", "its use alarms and is reviewed."),
              ("Deleting shared accounts first", "Scripts using them break at night.", "move scripts to service accounts first."),
              ("Never reviewing", "Standing access creeps back.", "quarterly review.")],
    use=["Many people can change production.", "Shared admin accounts exist.", "A client or auditor asks who can change what.", "After someone made an accidental production change."],
    skip=["Never: even small teams benefit from personal accounts and a log."],
    related=["<b>Forty New People on Monday</b> (vol. 1)", "<b>Least Privilege</b> (security, vol. 5)", "<b>Identity Federation & SSO</b> (Ana, vol. 4)", "<b>Which Changes Need a Second Look?</b> (this volume)"],
    quiz=[("Who has standing production access at Larder after April?", "Only Eli and Bram, for the platform."),
          ("How does everyone else get access?", "On request: a reason, a second person's approval, 4 hours, posted to the change feed."),
          ("What is break-glass for, and what happens when it's used?", "Emergencies when the request path is down; using it pages Eli and messages Femke and is reviewed next day."),
          ("Why delete shared accounts?", "Every action must belong to a person, or logs and reviews mean nothing."),
          ("What has to happen before deleting shared accounts?", "Move every script using them to its own service account.")],
    quiz_sit=[("Cho needs to check a payment row in production at 21:00, and Eli and Bram are both offline. What happens?", "Cho requests access with a reason; if no approver answers and it's urgent, the on-call lead can approve, or break-glass is used, which alarms Eli and Femke and is reviewed next day. Waiting until morning is fine if it isn't urgent.")],
    try_it="List everyone who can change your production database and servers today. For each person, ask: do they need it every day? Draft the request path for the rest, with a reason, an approver and an expiry.",
    remember="Standing access for the <span class=\"hl\">few who need it daily</span>; everyone else <span class=\"hl\">on request, for hours, logged</span>. And no master keys carried “just in case”.",
    sources=["AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020).",
             "NIST SP 800-53 Rev. 5: AC-6, least privilege; AC-2, account management.",
             "CIS Critical Security Controls v8: control 5 and 6 (account and access management)."],
)

# ------------------------------------------------------------------ 14 Patching Without Fear
pt_problem = Doodle(760, 260, "Doodle of Eli's Monday mornings until spring 2027: patching Larder Core's three virtual machines by hand, one at a time, about five hours a week, the biggest line in his toil log. When he's on holiday, nobody patches. In March a critical security fix for the operating system's SSL library comes out on a Thursday; the VMs get it the following Tuesday, five days later, because Monday was full.",
                    "Five hours a week of patching by hand, nobody patches during holidays, and a critical fix that took five days.")
pt_problem.box(14, 30, 230, 100, "5 h a week", "pink", sub="three VMs by hand", size=20, subsize=14)
pt_problem.box(264, 30, 230, 100, "holidays", "y", sub="nobody patches", size=20, subsize=14)
pt_problem.box(514, 30, 232, 100, "critical fix", "pink", sub="Thu out → Tue in", size=20, subsize=14)
pt_problem.note(380, 186, "the biggest line in the toil log since June 2026", "red", size=18)

pt_analogy = Doodle(760, 220, "Doodle of a delivery company's van fleet. Small things like tyre pressure are checked automatically every morning. Bigger services happen on a fixed day each month, one van at a time, so deliveries never stop. And an old van isn't patched forever; it's replaced with a new one built to the same spec.",
                    "Daily small checks, a monthly service one van at a time, and old vans replaced, not patched forever.")
pt_analogy.icon("truck", 40, 50, 1.3)
pt_analogy.row([("daily", "small, automatic", "green"), ("monthly", "one van at a time", "y"), ("replace", "same spec, new van", "blue")], x=140, y=40, h=96, w=190, gap=18, size=18, subsize=13)
pt_analogy.note(450, 190, "deliveries never stop", "pen", size=18)

pt_how = Doodle(760, 400, "Larder's patch routine from April 2027. Security updates install automatically every night on the Core VMs, one VM at a time between 02:00 and 04:00, with a reboot if needed; Core keeps running on the other two. Bigger updates (kernel, database minor versions) in a monthly window, first Tuesday 10:00, never in a critical window. Critical vulnerabilities, scored 9 or more, within 72 hours, as an emergency or normal change. Container images for Dispatch are scanned weekly and rebuilt from fresh base images. From June, the VMs are rebuilt from infrastructure code on Ubuntu 24.04 instead of repaired. Toil: patching 5 hours a week to about 30 minutes.",
                "Nightly automatic, one VM at a time; a monthly window; critical fixes within 72 hours; rebuild, don't repair.")
pt_how.box(14, 14, 236, 120, "nightly", "green", sub="security updates · 1 VM at a time · 02:00–04:00", size=19, subsize=11)
pt_how.box(262, 14, 236, 120, "monthly", "y", sub="kernel, DB minor · 1st Tue 10:00", size=19, subsize=12)
pt_how.box(510, 14, 236, 120, "critical ≤ 72 h", "pink", sub="score ≥ 9 · emergency or normal change", size=18, subsize=11)
pt_how.box(14, 160, 732, 64, "containers: scanned weekly, rebuilt from fresh base images", "blue", size=15)
pt_how.box(14, 244, 732, 64, "June: VMs rebuilt from code (Ubuntu 24.04), not repaired", "paper", size=15)
pt_how.note(380, 340, "toil: 5 h a week → ≈ 30 min · during Eli's holiday: still patched", "green", size=16)
pt_how.note(380, 376, "the March SSL fix today would take one night", "pen", size=15)

PATCHING = dict(
    slug="patching",
    kicker="a.k.a. “patch and vulnerability management”",
    tldr="Patching by hand is toil that never ends and stops when the person is away. Split it by size. <b>Small security updates install automatically</b>, one machine at a time, at night. <b>Bigger updates</b> go in a <b>monthly window</b>. <b>Critical vulnerabilities</b> are fixed within a set time (72 hours). Where you can, <b>rebuild machines from code</b> instead of repairing them: a fresh, patched machine is simpler to trust than a five-year-old one.",
    chips=[("Family", "keeping it current"), ("Lives in", "ops/patching.md, the infrastructure code, the image scanner"), ("Pairs with", "toil (vol. 1), the change calendar, end-of-life")],
    itil=dict(groups=["technical", "general"], chain=["deliver", "improve"], practices=["infrastructure and platform management", "information security management"],
              sre="(eliminating toil; immutable infrastructure)", principles=["Optimise and automate"],
              older="ITIL v3: technical management, patch management"),
    problem_side="Larder, March 2027",
    problem="""  <p class="lead">Since 2025, Eli's Monday mornings have gone on patching Larder Core's three VMs <b>by hand</b>, one at a time: about <b>five hours a week</b>, still the biggest line in his toil log. When he's on holiday, nobody patches. In March a <b>critical fix</b> for the operating system's SSL library comes out on a Thursday. <span class="hl-pink">The VMs get it the following Tuesday, five days later</span>, because Monday was full.</p>
  <ul>
    <li>Security depends on one person's Mondays.</li>
    <li>Every VM is patched slightly differently over time.</li>
    <li>Critical fixes wait in the same queue as routine ones.</li>
  </ul>""",
    problem_figs=[pt_problem],
    analogy_side="the van fleet's servicing",
    analogy="""  <p>A delivery company checks <b>small things automatically every morning</b>, like tyre pressure. Bigger services happen on <b>a fixed day each month, one van at a time</b>, so deliveries never stop. And an old van isn't patched forever: it's <b>replaced with a new one built to the same spec</b>.</p>""",
    analogy_figs=[pt_analogy],
    map=[("Tyre pressure every morning", "Nightly automatic security updates"),
         ("One van at a time", "One VM at a time; Core runs on the other two"),
         ("The monthly service day", "First Tuesday, 10:00: kernel and database minor versions"),
         ("A dangerous fault recall", "Critical vulnerability: within 72 hours"),
         ("A new van to the same spec", "VMs rebuilt from infrastructure code")],
    how_side="nightly, monthly, critical in 72 h, and rebuild instead of repair",
    how="""  <p>Bram and Eli set up the routine in <b>April</b>:</p>
  <ul>
    <li><b>Nightly</b>: security updates install automatically on the Core VMs, <b>one VM at a time between 02:00 and 04:00</b>, with a reboot if needed. Core keeps serving from the other two (any two of three is enough).</li>
    <li><b>Monthly</b>: bigger updates (kernel, database minor versions) on the <b>first Tuesday at 10:00</b>, as normal changes, never in a window.</li>
    <li><b>Critical</b>: anything scored <b>9 or more</b> is fixed <b>within 72 hours</b>, as an emergency or normal change depending on exposure.</li>
    <li><b>Containers</b>: Dispatch's images are scanned weekly and rebuilt from fresh base images.</li>
    <li><b>Rebuild, don't repair</b>: in June the three VMs are rebuilt from infrastructure code on <b>Ubuntu 24.04</b>, one at a time (this volume, end-of-life).</li>
  </ul>
  <p>Patching drops from <b>5 hours a week to about 30 minutes</b> of reading the reports. During Eli's holiday in July, the VMs are patched every night without him. The March SSL fix would now take one night.</p>""",
    how_figs=[pt_how],
    steps=[("Split patches by size", "Small automatic, bigger in a window, critical with a deadline."),
           ("Automate the small, one machine at a time", "At night; keep the service up on the others."),
           ("Set a monthly window for the rest", "Outside critical windows, as normal changes."),
           ("Set a deadline for critical fixes", "72 hours is common; write it down."),
           ("Scan images and rebuild them", "Fresh base images, weekly."),
           ("Rebuild machines from code", "Replace, don't repair, when you can.")],
    vocab=[("Patch", "An update that fixes a bug or a security hole."),
           ("Vulnerability", "A weakness that could be exploited; often scored 0–10 (CVSS)."),
           ("Unattended upgrades", "Updates that install automatically without a person."),
           ("Rolling update", "Updating one machine at a time so the service stays up."),
           ("Immutable infrastructure", "Replacing machines with fresh ones instead of changing them."),
           ("Image scanning", "Checking container images for known vulnerabilities.")],
    code=dict(file="ops/patching.md", note="from April 2027", plain=True, src="""
# Patching

nightly    OS security updates · Core VMs one at a time · 02:00–04:00 (core-1, -2, -3)
           reboot if needed · Core serves from the other two · result in #ops at 04:05
monthly    kernel · Postgres minor · first Tuesday 10:00 · normal change · not in a window
critical   CVSS ≥ 9: within 72 h · exposed to the internet → emergency change
containers Dispatch + Engine A images: scan weekly (Mon) · rebuild on fresh base image
rebuild    June 2027: Core VMs rebuilt from code on Ubuntu 24.04, one per night

toil       patching 5 h/week (2026) → ≈ 30 min/week (reports only)
holiday    July 2027: Eli away 2 weeks · VMs patched every night
"""),
    tools="tools: the operating system's automatic updates, a rolling reboot script, an image scanner in the pipeline, and infrastructure code to rebuild machines.",
    ladder=[("by hand, when there's time", ["One person, Mondays.", "Critical fixes wait."]),
            ("routine by size", ["Nightly, monthly, 72 hours for critical.", "Rolling, one at a time."]),
            ("rebuild instead of repair", ["Machines replaced from code.", "Images rebuilt weekly."]),
            ("nothing to patch by hand", ["Managed services patch themselves.", "People read reports."])],
    ladder_now=2,
    baseline="Each line compares <b>patching three VMs by hand on Mondays</b> to <b>a routine by size, rolling at night, and rebuilds from code</b>.",
    ratings=[(3, 3, "Neutral: rolling keeps Core up."),
             (2, 4, "Fewer known holes, fewer old bugs."),
             (3, 3, "Neutral."),
             (2, 3, "Patches are small, regular, and one machine at a time."),
             (2, 3, "Nightly results posted."),
             (1, 4, "5 h a week → 30 min."),
             (3, 3, "Neutral."),
             (2, 4, "Patching doesn't stop when Eli is away."),
             (3, 4, "Automatic once set up.")],
    pitfalls=[("Patching all machines at once", "A bad patch takes everything down.", "one at a time, with the service up on the others."),
              ("No deadline for critical fixes", "They wait in the routine queue.", "72 hours, written down."),
              ("Repairing old machines forever", "Each one drifts and nobody knows how it was built.", "rebuild from code."),
              ("Patching without watching", "Failures go unnoticed.", "post results; alert on failures.")],
    use=["Patching is manual and depends on one person.", "Critical fixes take days.", "Machines drift apart.", "Auditors or clients ask how fast you patch."],
    skip=["Fully managed services that patch themselves: check their reports instead."],
    related=["<b>Why Am I Always Busy?</b> (vol. 1)", "<b>Immutable Infrastructure</b> (cloud, vol. 6)", "<b>The Database Runs Out of Support</b> (next note)", "<b>Supply-Chain Hygiene</b> (security, vol. 5)"],
    quiz=[("How are small security updates handled now?", "Automatically, every night, one VM at a time between 02:00 and 04:00."),
          ("What's the deadline for a critical vulnerability?", "72 hours."),
          ("Why one VM at a time?", "Core keeps serving from the other two; a bad patch only affects one."),
          ("What does “rebuild, don't repair” mean?", "Replace machines with fresh ones built from code, instead of changing old ones over years."),
          ("What happened to patching toil?", "5 hours a week → about 30 minutes reading reports.")],
    quiz_sit=[("A critical vulnerability (score 9.8) in the web server is announced on Friday at 16:00 and Core is exposed to the internet. What happens?", "It's within the 72-hour rule, and exposed: an emergency change. Apply the fix or a mitigation before 17:00 if possible (the window starts then), otherwise with the incident lead's approval, one VM at a time, and watch.")],
    try_it="List every machine and image you run with how it's patched and how long the last critical fix took. Pick one thing to automate this month: nightly updates, a rolling reboot, or an image scan.",
    remember="Small patches <span class=\"hl\">every night, automatically</span>, big ones monthly, critical ones in 72 hours. And when you can, <span class=\"hl\">rebuild, don't repair</span>.",
    sources=["AXELOS, <i>ITIL 4: Infrastructure and platform management</i> practice guide (2020).",
             "NIST SP 800-40 Rev. 4, <i>Guide to Enterprise Patch Management Planning</i> (2022).",
             "Kief Morris, <i>Infrastructure as Code</i> (2nd ed., 2020)."],
)

# ------------------------------------------------------------------ 15 The Database Runs Out of Support
eol_problem = Doodle(760, 260, "Doodle of a letter from the cloud provider in February 2027: PostgreSQL 13, community support ended November 2025; extended support will cost extra from 1 April 2027, about 650 euros a month. Eli checks the rest: Larder Core runs Django 3.2 (support ended April 2024) on Python 3.8 (ended October 2024) on Ubuntu 20.04 (standard support ended May 2025). Nobody had a list of versions or end dates.",
                    "One letter about the database, and then the rest: every layer of Larder Core already out of support.")
for i, (t, s) in enumerate([("Postgres 13", "EOL Nov 2025"), ("Django 3.2", "EOL Apr 2024"), ("Python 3.8", "EOL Oct 2024"), ("Ubuntu 20.04", "EOL May 2025")]):
    eol_problem.box(14 + i * 186, 30, 172, 100, t, "pink", sub=s, size=18, subsize=14)
eol_problem.note(380, 176, "extended support from 1 Apr: ≈ €650 a month, for the database alone", "red", size=16)
eol_problem.note(380, 214, "no list of versions or end dates", "pen", size=17)

eol_analogy = Doodle(760, 220, "Doodle of a family's paperwork drawer. Passports, the boiler service, the car's inspection, the home insurance: each has an expiry date. A wise family keeps one list with the dates and renews things a few months early, in a quiet month, not at the airport the night before.",
                    "Passports, boiler, car inspection: one list of expiry dates, renewed early, not at the airport.")
eol_analogy.icon("calendar", 60, 40, 1.5)
eol_analogy.box(170, 30, 576, 120, None, "paper")
for i, t in enumerate(["passports · Mar 2028 · renew Sep 2027", "boiler service · every Oct", "car inspection · Jun 2027"]):
    eol_analogy.text(190, 64 + i * 32, t, anchor="start", size=16)
eol_analogy.note(450, 190, "renew on your schedule, not at the airport", "pen", size=18)

eol_how = Doodle(760, 400, "Larder's lifecycle register from March 2027: 23 components, each with its version, end-of-support date, owner and planned upgrade. Rule: upgrade at least six months before end of support; reviewed every quarter. The 2027 catch-up: Postgres 13 to 16, a high-risk change scored 14, done on Tuesday 18 May 2027 at 05:00 by logical replication to a new server, switch in 4 minutes, the old server kept replicating back for a week as the way back, a restore practised on 11 May. Ubuntu 20.04 to 24.04: VMs rebuilt from code in June. Django 3.2 to 4.2 by July, to 5.2 by October. Python with Django. Extended support paid for April and May only, about 1,300 euros.",
                "One register, six months' notice, and a catch-up plan. Postgres 16 on 18 May: 4 minutes, with a way back.")
eol_how.box(14, 14, 732, 40, "component · version · end of support · owner · upgrade by", "paper", size=14)
for i, (t, s, f) in enumerate([("Postgres 13 → 16", "Tue 18 May 05:00 · 4 min · score 14 · way back 1 week", "green"),
                               ("Ubuntu 20.04 → 24.04", "VMs rebuilt from code · June", "green"),
                               ("Django 3.2 → 4.2 → 5.2", "Jul → Oct · Python with it", "y")]):
    eol_how.box(14, 66 + i * 64, 260, 54, t, f, size=15)
    eol_how.box(286, 66 + i * 64, 460, 54, s, "paper", size=13)
eol_how.note(380, 290, "rule: upgrade at least 6 months before end of support", "red", size=16)
eol_how.note(380, 326, "extended support paid for 2 months (≈ €1,300), not forever", "pen", size=16)
eol_how.note(380, 362, "register reviewed every quarter · 23 components", "pen", size=15)

END_OF_LIFE = dict(
    slug="end-of-life",
    kicker="a.k.a. “lifecycle management”",
    tldr="Every layer you run, from database to framework to operating system to device, has an <b>end-of-support date</b>, after which security fixes stop or cost extra. Keep a <b>lifecycle register</b> of versions and dates, review it <b>quarterly</b>, and upgrade <b>at least six months before</b> the end, in planned, reversible steps. Otherwise the vendor's calendar decides your priorities, usually in a hurry.",
    chips=[("Family", "keeping it current"), ("Lives in", "ops/lifecycle.md, reviewed quarterly"), ("Pairs with", "patching, rollback plans, risk scoring, the asset register (vol. 1)")],
    itil=dict(groups=["technical", "service"], chain=["plan", "improve", "build"], practices=["infrastructure and platform management", "IT asset management"],
              sre="(technical debt with a deadline)", principles=["Think and work holistically", "Progress iteratively with feedback"],
              older="ITIL v3: technical management, the configuration lifecycle"),
    problem_side="Larder, February 2027",
    problem="""  <p class="lead">In February a letter arrives from the cloud provider. <b>PostgreSQL 13</b> left community support in November 2025, and from <b>1 April 2027</b> extended support will cost extra, about <b>€650 a month</b>. Eli checks the rest. Larder Core runs <b>Django 3.2</b> (support ended April 2024) on <b>Python 3.8</b> (October 2024) on <b>Ubuntu 20.04</b> (standard support ended May 2025). <span class="hl-pink">Every layer of Larder Core is already out of support, and nobody had a list.</span></p>
  <ul>
    <li>Security fixes stopped arriving, silently.</li>
    <li>Upgrades that could have been small steps are now big jumps.</li>
    <li>The vendor's deadline now sets the plan.</li>
  </ul>""",
    problem_figs=[eol_problem],
    analogy_side="the family's expiry dates",
    analogy="""  <p>Passports, the boiler service, the car's inspection, the home insurance: each has an <b>expiry date</b>. A sensible family keeps <b>one list with the dates</b> and renews things a few months early, in a quiet month. Otherwise you find out <b>at the airport the night before</b>, when everything costs more and takes longer.</p>""",
    analogy_figs=[eol_analogy],
    map=[("The list of expiry dates", "The lifecycle register: version, end of support, owner"),
         ("Renewing months early", "Upgrading at least six months before end of support"),
         ("A quiet month", "A planned upgrade outside windows and freezes"),
         ("At the airport the night before", "A vendor letter and extended support fees"),
         ("Checking the drawer each season", "The quarterly review")],
    how_side="a register, six months' notice, and a catch-up plan",
    how="""  <p>Eli starts <code>ops/lifecycle.md</code> in March: <b>23 components</b>, each with its version, <b>end-of-support date</b>, owner and planned upgrade. The rule: <b>upgrade at least six months before</b> end of support, reviewed every quarter. Then comes the 2027 catch-up:</p>
  <ul>
    <li><b>Postgres 13 → 16</b>: a high-risk change (score <b>14</b>). A restore is practised on <b>11 May</b>. On <b>Tuesday 18 May at 05:00</b>, before the morning window, logical replication to a new server lets the switch take <b>4 minutes</b>. The old server keeps replicating back for <b>a week</b> as the way back.</li>
    <li><b>Ubuntu 20.04 → 24.04</b>: the VMs are rebuilt from code in June, one per night.</li>
    <li><b>Django 3.2 → 4.2</b> by July and <b>→ 5.2</b> by October, with Python along with it, as normal changes in the orders team's 20 % tech-debt time.</li>
  </ul>
  <p>Larder pays extended support for April and May only (about <b>€1,300</b>), not forever. The register also covers the handhelds' Android versions, which matter in vol. 5.</p>""",
    how_figs=[eol_how],
    steps=[("List every layer and its version", "Database, OS, language, framework, devices, SaaS plans."),
           ("Add end-of-support dates and owners", "From vendors' published lifecycles."),
           ("Set a notice rule", "Upgrade at least six months before the end."),
           ("Plan catch-ups as reversible steps", "Risk score, way back, practised restore."),
           ("Pay extended support only as a bridge", "With an end date."),
           ("Review the register quarterly", "New components, new dates.")],
    vocab=[("End of support (EOL)", "The date after which a vendor stops fixing a version."),
           ("Extended support", "Paid fixes after the normal end, usually for a limited time."),
           ("Lifecycle register", "The list of components, versions and end dates."),
           ("Major upgrade", "A jump between major versions; often not reversible in place."),
           ("Logical replication", "Copying data changes to another database server, even across versions."),
           ("Technical debt", "Work postponed that costs more the longer it waits.")],
    code=dict(file="ops/lifecycle.md", note="from March 2027 · reviewed quarterly", plain=True, src="""
component        version   end of support   owner   upgrade by      status
PostgreSQL       13 → 16   Nov 2025 (13)    Eli     18 May 2027     ✓ done, 4 min switch
Ubuntu (Core)    20.04     May 2025         Bram    Jun 2027        → 24.04, rebuilt from code
Python (Core)    3.8       Oct 2024         Ben     Oct 2027        with Django
Django           3.2       Apr 2024         Ben     Jul / Oct 2027  → 4.2 → 5.2 (LTS to 2028)
picker handheld  Android 11 (HH-2024)  vendor updates end 2027  Dee  vol. 5
Dispatch base    image     rebuilt weekly   Bram    —               ok
… 23 components

rule   upgrade ≥ 6 months before end of support · quarterly review (Mar, Jun, Sep, Dec)
bridge extended support Postgres 13: Apr + May 2027 only (≈ €1,300)
"""),
    tools="tools: one table in the repo, vendors' published lifecycle pages, and a quarterly calendar reminder.",
    ladder=[("found by vendor letters", ["Everything out of support.", "Big jumps in a hurry."]),
            ("a register and a notice rule", ["23 components, quarterly review.", "Upgrades planned six months ahead."]),
            ("versions read automatically", ["The register filled from the systems and images.", "Warnings a year before."]),
            ("always current", ["Small upgrades continuously.", "No catch-ups needed."])],
    ladder_now=1,
    baseline="Each line compares <b>finding out from a vendor's letter</b> to <b>a lifecycle register with six months' notice and planned upgrades</b>.",
    ratings=[(3, 3, "Neutral: upgrades planned around customers."),
             (2, 4, "Security fixes arrive again."),
             (3, 3, "Neutral."),
             (2, 3, "Upgrades planned as reversible steps."),
             (1, 4, "Every layer's version and end date on one page."),
             (3, 3, "Neutral."),
             (2, 4, "Extended support as a two-month bridge, not a habit."),
             (3, 3, "Neutral."),
             (3, 3, "An hour a quarter.")],
    pitfalls=[("Waiting for the letter", "The vendor sets the plan.", "a register with dates."),
              ("Skipping versions for years", "Small steps become one big jump.", "upgrade regularly."),
              ("Extended support forever", "A cost that hides the debt.", "a bridge with an end date."),
              ("Forgetting devices and SaaS plans", "Handhelds stop getting updates.", "the register covers every layer.")],
    use=["Nobody knows which versions you run.", "A vendor announces an end of support.", "Before a security questionnaire.", "Upgrades keep being postponed."],
    skip=["Fully managed services that upgrade themselves: track their notices instead."],
    related=["<b>Patching Without Fear</b> (this volume)", "<b>How Do We Undo It?</b> (this volume)", "<b>What Do We Own, and Where Is It?</b> (vol. 1)", "<b>Tech-Debt Talks</b> (Grace, vol. 3)"],
    quiz=[("What's in Larder's lifecycle register?", "Every component's version, end-of-support date, owner and planned upgrade."),
          ("What's the notice rule?", "Upgrade at least six months before end of support."),
          ("How was the Postgres 16 upgrade made reversible?", "Logical replication to a new server; the old one kept replicating back for a week as the way back."),
          ("Why pay extended support for only two months?", "As a bridge to the upgrade, not a way to postpone it forever."),
          ("What risk score did the Postgres upgrade get, and why?", "14: everything depends on it, hard to undo in place, first time, a big jump.")],
    quiz_sit=[("A SaaS tool you use announces it will retire your plan in nine months. Where does this go, and what happens next?", "Into the lifecycle register with the date and an owner; the owner plans the move to a new plan or tool well before the six-month mark, as a normal change.")],
    try_it="List every layer of your most important service with its version. Look up each end-of-support date. How many are already past, and which one ends next? Put the upgrade six months before it.",
    remember="Every layer has an <span class=\"hl\">expiry date</span>. Keep the list, upgrade <span class=\"hl\">six months early</span>, and don't let the vendor's letter set your plan.",
    sources=["AXELOS, <i>ITIL 4: Infrastructure and platform management</i> practice guide (2020).",
             "PostgreSQL Global Development Group, “Versioning Policy” (postgresql.org).",
             "Django Software Foundation, “Supported versions” (djangoproject.com)."],
)

NOTES = [PROD_ACCESS, PATCHING, END_OF_LIFE]
