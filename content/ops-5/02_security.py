# Series 2 · Book 5 · The IT Operations Notebook · Vol. 5 · Security operations.
# Narrator: Eli (he/him). Facts: docs/larder-casebook.md, "Book 5, Vol. 5".

# ------------------------------------------------------------------ 07 Is the Alarm Real?
sm_problem = Doodle(760, 260, "Doodle of Larder's security signals in January 2028. Sign-ins live in the identity provider, kept 30 days. Cloud admin actions in the cloud's audit log, kept 90 days. The helpdesk and the business portal have their own logs, kept 14 days. Nobody looks at any of them unless something has already happened, and two of them would already have been deleted by the time anyone asked.",
                    "Sign-ins 30 days, cloud admin 90, the apps 14. Nobody looks until something has already happened.")
for i, (t, d) in enumerate([("sign-ins", "30 days"), ("cloud admin", "90 days"), ("helpdesk", "14 days"), ("business portal", "14 days")]):
    sm_problem.box(14 + i * 186, 30, 172, 100, t, "y", sub=d, size=17, subsize=15)
sm_problem.note(380, 180, "looked at only after the fact · some already gone", "red", size=18)

sm_analogy = Doodle(760, 220, "Doodle of a shop's security: cameras at the doors, the till and the stockroom, not everywhere; recordings kept for a month; and an alarm only for the few things that matter: a door opened at night, the safe opened outside hours. The guard isn't watching every screen; the alarm tells him where to look.",
                    "Cameras where it matters, recordings kept a month, and an alarm for a door opened at night.")
sm_analogy.icon("camera", 60, 50, 1.3)
sm_analogy.row([("doors · till · stockroom", "cameras", "blue"), ("kept a month", "recordings", "y"), ("door at night", "the alarm", "pink")], x=160, y=40, h=96, w=184, gap=12, size=15, subsize=13)
sm_analogy.note(450, 190, "collect where it matters, alarm on the few that count", "pen", size=17)

sm_how = Doodle(760, 400, "Larder's security monitoring from February 2028. Six sources sent to one log store: sign-ins, cloud admin actions, break-glass use, production access requests, helpdesk and portal data views and exports, and network traffic at the edge. Kept one year, agreed with Lena; restricted data in the logs is masked. Six alerts: impossible-travel sign-in, many failed sign-ins on one account, a new admin role granted, break-glass used, a large customer-data export, and a business API key used from an unexpected country. Alerts go to on-call as tickets, or pages for break-glass and exports. Tuning: 40 alerts a week in February, 4 a week by April.",
                "Six sources kept a year, six alerts that matter. 40 alerts a week tuned down to 4.")
for i, t in enumerate(["sign-ins", "cloud admin", "break-glass", "access requests", "data views + exports", "edge traffic"]):
    r, c = divmod(i, 3)
    sm_how.box(14 + c * 248, 14 + r * 62, 236, 52, t, "blue", size=15)
sm_how.box(14, 146, 732, 56, "one log store · kept 1 year (Lena) · restricted data masked", "y", size=15)
for i, t in enumerate(["impossible travel", "many failed sign-ins", "new admin role", "break-glass", "big export", "API key, odd country"]):
    r, c = divmod(i, 3)
    sm_how.box(14 + c * 248, 220 + r * 54, 236, 46, t, "pink", size=14)
sm_how.note(380, 354, "40 alerts a week (Feb) → 4 (Apr)", "green", size=17)
sm_how.note(380, 388, "the 9 March alert came from this list", "pen", size=15)

SECURITY_MONITORING = dict(
    slug="security-monitoring",
    kicker="a.k.a. “security monitoring and log retention”",
    tldr="You can't respond to an attack you can't see, or investigate one whose logs were deleted. Collect the <b>few logs that show attacks</b> (sign-ins, admin actions, access to customer data, exports, unusual API use) in <b>one place</b>, keep them <b>as long as an investigation needs</b> (agreed with legal), and alert on a <b>handful of signals that matter</b>, tuned until each alert is worth reading. Like operational alerts, security alerts must be actionable.",
    chips=[("Family", "security operations"), ("Lives in", "one log store, six alert rules, ops/security/monitoring.md"), ("Pairs with", "security incidents, access reviews, production access (vol. 3)")],
    itil=dict(groups=["general", "service"], chain=["deliver", "improve"], practices=["information security management", "monitoring and event management"],
              sre="(actionable alerting applied to security)", principles=["Keep it simple and practical", "Focus on value"],
              older="ITIL v3: information security management, event management"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">Eli checks Larder's security signals in January. <b>Sign-ins</b> are in the identity provider, kept 30 days. <b>Cloud admin actions</b> are in the cloud's audit log, kept 90 days. The <b>helpdesk</b> and the <b>business portal</b> have their own logs, kept 14 days. <span class="hl-pink">Nobody looks at any of them unless something has already happened</span>, and two of them would already be deleted by the time anyone asked. Korenwolf's supplier questionnaire, due in March, asks exactly how long logs are kept and who watches them.</p>
  <ul>
    <li>Attacks are found by their consequences, not their signs.</li>
    <li>Investigations hit deleted logs.</li>
    <li>Signals sit in four places with four retention periods.</li>
  </ul>""",
    problem_figs=[sm_problem],
    analogy_side="the shop's cameras and alarm",
    analogy="""  <p>A shop has cameras at <b>the doors, the till and the stockroom</b>, not everywhere. Recordings are <b>kept for a month</b>. And there's an alarm for only a few things: <b>a door opened at night</b>, the safe opened outside hours. The guard isn't watching every screen; the alarm tells him where to look, and the recordings let him find out what happened.</p>""",
    analogy_figs=[sm_analogy],
    map=[("Cameras at doors, till, stockroom", "Sign-ins, admin actions, data views and exports"),
         ("Recordings kept a month", "Logs kept a year (agreed with Lena)"),
         ("The door opened at night", "Impossible travel, break-glass, a big export"),
         ("The guard", "On-call, with a short list of security alerts"),
         ("Not every corridor", "Not every log: the few that show attacks")],
    how_side="six sources, one place, a year's retention, six alerts",
    how="""  <p>From <b>February</b>, six sources go to <b>one log store</b>: sign-ins, cloud admin actions, break-glass use, production access requests, <b>views and exports of customer data</b> in the helpdesk and portal, and network traffic at the edge. They're kept for <b>one year</b>, agreed with Lena, with restricted data masked in the logs themselves.</p>
  <p>Six alerts, to on-call:</p>
  <ul>
    <li><b>Impossible travel</b>: one account signing in from two far-apart places within an hour.</li>
    <li><b>Many failed sign-ins</b> on one account.</li>
    <li>A <b>new admin role</b> granted.</li>
    <li><b>Break-glass</b> used (a page).</li>
    <li>A <b>large customer-data export</b> (a page).</li>
    <li>A <b>business API key</b> used from an unexpected country.</li>
  </ul>
  <p>The first week brings <b>40 alerts</b>, mostly staff on VPNs and travel. Tuning (known VPN exits, travel notices) brings it to <b>4 a week by April</b>, each one worth reading. On <b>9 March</b>, the impossible-travel alert is the one that matters (next note).</p>""",
    how_figs=[sm_how],
    steps=[("List the logs that would show an attack", "Sign-ins, admin, data access, exports, API use."),
           ("Send them to one place", "With the same clock and fields."),
           ("Agree retention with legal", "Long enough to investigate; mask personal data."),
           ("Write a few alerts that matter", "Each with a runbook."),
           ("Tune until each alert is worth reading", "Known exits, travel, service accounts."),
           ("Review the alert list quarterly", "Add what incidents teach.")],
    vocab=[("Security monitoring", "Watching for signs of attack or misuse."),
           ("Audit log", "A record of who did what, when, from where."),
           ("Retention", "How long logs are kept."),
           ("SIEM", "A security information and event management tool: one place for security logs and alerts."),
           ("Impossible travel", "Sign-ins from places too far apart for the time between them."),
           ("False positive", "An alert for something harmless.")],
    code=dict(file="ops/security/monitoring.md", note="from February 2028", plain=True, src="""
sources (one log store, kept 1 year, restricted data masked · agreed with Lena 2 Feb)
  identity provider sign-ins · cloud audit (admin) · break-glass · /prod-access
  helpdesk + portal: customer record views and exports · edge network flows

alerts                                    to         runbook
impossible-travel sign-in                 ticket     SEC-01
> 10 failed sign-ins / account / 10 min   ticket     SEC-02
new admin role granted                    ticket     SEC-03
break-glass used                          page       SEC-04
customer export > 500 rows                page       SEC-05
business API key, unexpected country      ticket     SEC-06

tuning   VPN exits known · travel notices · service accounts excluded from SEC-01
         Feb: 40 alerts/week → Apr: 4/week
"""),
    tools="tools: the identity provider, the cloud audit log, the apps' access logs, one log store (a SIEM or a managed log service), and six rules.",
    ladder=[("logs scattered, unread", ["Found after the fact.", "Some already deleted."]),
            ("one store, a year, six alerts", ["Tuned to be worth reading.", "Runbooks for each."]),
            ("detections improve", ["New rules from incidents and threat models.", "Coverage reviewed quarterly."]),
            ("watched around the clock", ["A security operations partner or team.", "Response measured."])],
    ladder_now=1,
    baseline="Each line compares <b>scattered logs with short retention</b> to <b>one log store, a year's retention and six tuned alerts</b>.",
    ratings=[(2, 4, "An account takeover found in minutes, not weeks."),
             (3, 3, "Neutral."),
             (2, 4, "Investigations have the logs they need."),
             (3, 3, "Neutral."),
             (1, 4, "Who did what is answerable for a year."),
             (3, 3, "Neutral."),
             (3, 3, "A log store costs money; a breach costs more."),
             (3, 3, "Four alerts a week, not forty."),
             (3, 3, "A week to set up, an hour a quarter.")],
    pitfalls=[("Collecting everything", "Expensive and unreadable.", "the few logs that show attacks."),
              ("Too short retention", "The investigation finds nothing.", "agree it with legal."),
              ("Alerts nobody can act on", "Security fatigue, like alert fatigue.", "few, tuned, with runbooks."),
              ("Personal data in logs", "Logs become a privacy risk.", "mask restricted data.")],
    use=["Nobody would notice an account takeover.", "A client asks how long logs are kept.", "After a security review or a near miss.", "Before letting more people access customer data."],
    skip=["Never: at least sign-ins and admin actions belong in one place."],
    related=["<b>Audit Logging</b> (security, vol. 5)", "<b>When the Incident Is a Security Incident</b> (next note)", "<b>Which Alerts Deserve a Human?</b> (vol. 1)", "<b>Data Classification & Residency</b> (Ana, vol. 5)"],
    quiz=[("Which logs did Larder collect?", "Sign-ins, cloud admin actions, break-glass, production access requests, customer data views and exports, edge traffic."),
          ("How long are they kept, and who agreed it?", "One year, agreed with Lena; restricted data masked."),
          ("Name three of the six alerts.", "Impossible travel, many failed sign-ins, new admin role, break-glass, big export, API key from an unexpected country."),
          ("Why tune alerts?", "Untuned, 40 a week were mostly harmless; tuned, 4 a week are worth reading."),
          ("Why mask personal data in logs?", "Otherwise the logs themselves become a privacy risk.")],
    quiz_sit=[("An impossible-travel alert fires for Mo's account: Amsterdam at 09:00, Lisbon at 09:20. Mo is in the office. What do you do?", "Treat it as possibly real: confirm with Mo by phone (not chat), and if it isn't him, follow the security incident steps: revoke sessions, reset, preserve the logs.")],
    try_it="List where your sign-ins, admin actions and customer-data exports are logged, and how long each is kept. Could you answer “who exported customer data last March?” today? Write one alert you'd want.",
    remember="See attacks by their <span class=\"hl\">signs</span>, not their consequences: a few logs, kept long enough, and <span class=\"hl\">a few alerts worth reading</span>.",
    sources=["AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020).",
             "NIST SP 800-92, <i>Guide to Computer Security Log Management</i>.",
             "CIS Critical Security Controls v8: control 8, audit log management."],
)

# ------------------------------------------------------------------ 08 When the Incident Is a Security Incident
si_problem = Doodle(760, 260, "Doodle of Thursday 9 March 2028, 09:40. The impossible-travel alert fires for a support agent's account: signed in from Amsterdam at 08:55 and from abroad at 09:31. The agent had approved a sign-in prompt on their phone without thinking, after a phishing email. The on-call engineer's first instinct, from every other incident: reset the password and restart things. That would destroy the evidence of what the attacker did.",
                    "An account taken over. The usual incident instinct (reset and restart) would wipe the evidence.")
si_problem.box(14, 30, 230, 100, "09:31", "pink", sub="sign-in from abroad", size=21, subsize=14)
si_problem.box(264, 30, 230, 100, "phishing", "y", sub="prompt approved by habit", size=20, subsize=14)
si_problem.box(514, 30, 232, 100, "“reset + restart”", "paper", sub="destroys evidence", size=18, subsize=14)
si_problem.note(380, 186, "what did they see? for how long? whose data?", "red", size=18)

si_analogy = Doodle(760, 220, "Doodle of a burglary at a shop. The owner's instinct is to tidy up and get trading. The police say: lock the broken door so nobody else gets in, don't touch anything, write down what's missing, and call the insurer today because there's a deadline. Contain, preserve, assess, report.",
                    "After a burglary: secure the door, touch nothing, list what's missing, call the insurer within the deadline.")
si_analogy.row([("secure the door", "contain", "pink"), ("touch nothing", "preserve", "y"), ("list what's gone", "assess", "blue"), ("call the insurer", "report on time", "green")], y=40, h=96, gap=14, size=16, subsize=13)
si_analogy.note(380, 190, "the tidy-up comes last", "pen", size=18)

si_how = Doodle(760, 400, "How Larder handled 9 March 2028, and the security incident steps that came from it. 09:44 contain: disable the account and revoke its sessions, but keep it, don't delete. 09:50 preserve: export the sign-in, helpdesk and portal logs for that account to a locked folder. 10:05 bring in Lena: she owns the legal assessment. 11:30 assess: in 18 minutes the attacker viewed 37 customer orders (names, addresses, phone numbers), exported nothing. Lena decides it is a personal data breach to notify: the Dutch data protection authority is told on Friday 10 March, within 72 hours, and the 37 customers on 13 March. Fix: number-matching sign-in prompts for everyone, and passkeys for support and admin accounts by May. The agent is not blamed; the review is blameless.",
                "Contain without deleting, preserve the logs, bring in legal, assess, notify within 72 hours, fix the cause.")
for i, (t, s, f) in enumerate([("09:44 contain", "disable + revoke, don't delete", "pink"), ("09:50 preserve", "export logs, lock them", "y"),
                               ("10:05 legal", "Lena owns the assessment", "blue"), ("11:30 assess", "37 orders viewed, 18 min", "y"),
                               ("10 Mar notify", "regulator < 72 h · customers 13 Mar", "green"), ("fix", "number matching · passkeys by May", "green")]):
    r, c = divmod(i, 3)
    si_how.box(14 + c * 248, 14 + r * 110, 236, 96, t, f, sub=s, size=17, subsize=12)
si_how.note(380, 270, "blameless: the prompt design was the weakness, not the agent", "red", size=16)
si_how.note(380, 306, "security incidents: the incident process + legal + evidence + deadlines", "pen", size=15)

SECURITY_INCIDENTS = dict(
    slug="security-incidents",
    kicker="a.k.a. “security incident management”",
    tldr="A security incident uses the normal incident process <b>plus four things</b>: <b>contain without destroying evidence</b> (disable, don't delete; isolate, don't wipe), <b>preserve the logs</b>, bring in <b>legal early</b> because the law may set <b>deadlines</b> (personal data breaches: 72 hours to the regulator in the EU), and <b>assess exactly what was touched</b> before deciding who to tell. Then fix the weakness, without blaming the person who was tricked.",
    chips=[("Family", "security operations"), ("Lives in", "ops/security/incident.md; SEC runbooks"), ("Pairs with", "security monitoring, incident roles (vol. 2), access reviews")],
    itil=dict(groups=["general", "service"], chain=["deliver", "engage", "improve"], practices=["information security management", "incident management"],
              sre="(incident command with a security lead)", principles=["Think and work holistically", "Collaborate and promote visibility"],
              older="ITIL v3: security incident handling"),
    pager=dict(when="Thu 9 Mar 2028 · Bram on call", lines=[
        ("09:40", "<b>ALERT</b> SEC-01 impossible travel · support agent · AMS 08:55 → abroad 09:31"),
        ("09:42", "Bram declares SEV2 (security) · Eli lead · calls the agent: “not me”"),
        ("09:44", "account disabled, sessions revoked (not deleted)"),
        ("09:50", "logs for the account exported to the locked evidence folder"),
        ("10:05", "Lena joins · legal assessment owner"),
        ("11:30", "found: 37 orders viewed in 18 min · no export · no other accounts"),
        ("Fri 10 Mar", "regulator notified (< 72 h) · customers told Mon 13 Mar")]),
    problem_side="Larder, Thursday 9 March 2028",
    problem="""  <p class="lead">At <b>09:40</b> the impossible-travel alert fires for a support agent's account: signed in from Amsterdam at 08:55, and from abroad at <b>09:31</b>. After a phishing email, the agent had <b>approved a sign-in prompt on their phone</b> by habit. Bram's first instinct, from every other incident, is to <b>reset the password and restart things</b>. <span class="hl-pink">That would destroy the evidence of what the attacker did</span>, and Larder would need that evidence to decide what to tell the regulator and its customers.</p>
  <ul>
    <li>The normal incident reflex (restore fast) can erase what you need to know.</li>
    <li>Legal deadlines start when you become aware, not when you finish.</li>
    <li>Blaming the agent would make the next person hide a mistake.</li>
  </ul>""",
    problem_figs=[si_problem],
    analogy_side="the shop after a burglary",
    analogy="""  <p>After a burglary, a shop owner's instinct is to tidy up and get trading. The police say otherwise: <b>secure the broken door</b> so nobody else gets in, <b>touch nothing</b>, <b>write down what's missing</b>, and <b>call the insurer today</b>, because there's a deadline. Tidying up comes last.</p>""",
    analogy_figs=[si_analogy],
    map=[("Securing the door", "Disable the account, revoke sessions"),
         ("Touching nothing", "Don't delete the account; export and lock the logs"),
         ("Listing what's missing", "37 orders viewed, nothing exported"),
         ("The insurer's deadline", "72 hours to notify the regulator"),
         ("Tidying up last", "Number-matching prompts and passkeys")],
    how_side="contain, preserve, legal, assess, notify, fix",
    how="""  <p>Eli takes the lead at 09:42 and follows the incident roles, with four security steps added:</p>
  <ul>
    <li><b>Contain without destroying</b> (09:44): disable the account and revoke its sessions. Don't delete it.</li>
    <li><b>Preserve</b> (09:50): export the account's sign-in, helpdesk and portal logs to a locked evidence folder.</li>
    <li><b>Legal early</b> (10:05): Lena joins and owns the legal assessment.</li>
    <li><b>Assess exactly</b> (11:30): in <b>18 minutes</b> the attacker viewed <b>37 customer orders</b> (names, addresses, phone numbers) and exported nothing. No other accounts were touched.</li>
  </ul>
  <p>Lena decides it's a personal data breach to notify. The Dutch data protection authority is told on <b>Friday 10 March</b>, within 72 hours, and the 37 customers on <b>13 March</b>, with Sam's team ready for calls. The fix is aimed at the weakness: <b>number-matching sign-in prompts</b> for everyone, and <b>passkeys</b> for support and admin accounts by May. The review is blameless. The weakness was a prompt that could be approved by habit, not the agent who approved it.</p>""",
    how_figs=[si_how],
    steps=[("Declare it as a security incident", "Normal roles, plus a security note."),
           ("Contain without destroying", "Disable, revoke, isolate; don't delete or wipe."),
           ("Preserve the evidence", "Export and lock the logs early."),
           ("Bring in legal at once", "Deadlines start at awareness."),
           ("Assess exactly what was touched", "Whose data, which fields, how long."),
           ("Notify on time, then fix the weakness", "Blameless review; fix the design.")],
    vocab=[("Security incident", "An event that threatens confidentiality, integrity or availability through misuse or attack."),
           ("Containment", "Stopping the attacker's access without destroying evidence."),
           ("Evidence preservation", "Keeping logs and systems as they were, for investigation."),
           ("Personal data breach", "Personal data accessed, lost or changed without authorisation."),
           ("72-hour rule", "Under the GDPR, notify the supervisory authority within 72 hours of becoming aware, where required."),
           ("Phishing", "Tricking someone into giving access, often by email or prompts.")],
    code=dict(file="ops/security/incident.md", note="security incident steps · after 9 March 2028", plain=True, src="""
# Security incident (on top of the normal incident roles)

1 declare     SEV by impact + "security" · lead names a security fixer
2 contain     disable account / revoke sessions / isolate host
              NOT: delete accounts, wipe machines, restart before step 3
3 preserve    export logs for the affected accounts and hosts → /evidence (locked)
4 legal       Lena (or Maarten in Belgium) joins at once: owns the legal assessment
              clock starts at awareness: regulator ≤ 72 h if required
5 assess      whose data · which fields · how long · exported?
6 notify      regulator / customers / clients as Lena decides · Sam ready · Mo for clients
7 fix         the weakness, not the person · blameless review ≤ 1 week

9 Mar 2028   support account, 18 min, 37 orders viewed, no export
             → regulator 10 Mar · customers 13 Mar · number matching (Mar) · passkeys (May)
"""),
    tools="tools: the identity provider's session revocation, the log store, a locked evidence folder, Lena's phone number, and templates for notifications.",
    ladder=[("restore fast, ask later", ["Evidence wiped.", "Legal deadlines missed."]),
            ("security steps on top of incidents", ["Contain, preserve, legal, assess, notify.", "Blameless."]),
            ("practised", ["Security scenarios in game days.", "Notification templates ready."]),
            ("weaknesses designed out", ["Phishing-resistant sign-in everywhere.", "Least access limits what an attacker sees."])],
    ladder_now=1,
    baseline="Each line compares <b>handling a security incident like any outage</b> to <b>contain, preserve, legal, assess, notify, fix</b>.",
    ratings=[(2, 4, "37 customers told the truth, on time."),
             (2, 4, "Phishing-resistant sign-in for the riskiest accounts."),
             (2, 3, "Contained in 4 minutes."),
             (3, 3, "Neutral."),
             (2, 4, "Exactly what was touched is known."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "A few extra steps, written in advance.")],
    pitfalls=[("Wiping before looking", "No way to know what happened.", "contain, then preserve, then fix."),
              ("Legal last", "Deadlines missed.", "legal at once."),
              ("Guessing the scope", "Over- or under-notifying.", "assess exactly from the logs."),
              ("Blaming the person", "The next one hides it.", "fix the design; blameless review.")],
    use=["An account, device or key may be in the wrong hands.", "Customer data may have been seen or taken.", "A security alert looks real.", "Planning game days (add a security scenario)."],
    skip=["Ordinary outages with no sign of misuse: the normal process is enough."],
    related=["<b>Is the Alarm Real?</b> (this volume)", "<b>Passkeys</b> (security, vol. 5)", "<b>Who Is in Charge?</b> (vol. 2)", "<b>Working with Legal & Privacy</b> (Grace, vol. 5)"],
    quiz=[("What's different about containment in a security incident?", "Disable and revoke, but don't delete or wipe: evidence must be kept."),
          ("Why bring legal in at once?", "Deadlines (like the GDPR's 72 hours) start when you become aware."),
          ("What did the attacker do on 9 March?", "Viewed 37 customer orders in 18 minutes; exported nothing."),
          ("Who was notified, and when?", "The data protection authority on 10 March (within 72 hours), the 37 customers on 13 March."),
          ("What was fixed?", "Number-matching sign-in prompts for everyone and passkeys for support and admin accounts.")],
    quiz_sit=[("A developer's laptop is stolen from a car. It had production database credentials in a file. What are the first steps?", "Declare a security incident: rotate the credentials at once (contain), check the database logs for use since the theft (preserve and assess), bring in Lena, and decide on notification from what the logs show.")],
    try_it="Write the first six steps your team would take if a staff account were taken over this morning. Who decides about notifying the regulator, and how would they know the deadline? What would you be careful not to delete?",
    remember="In a security incident, <span class=\"hl\">contain without destroying</span>, bring in legal <span class=\"hl\">at once</span>, and fix the weakness, not the person.",
    sources=["NIST SP 800-61 Rev. 2, <i>Computer Security Incident Handling Guide</i>.",
             "European Data Protection Board, <i>Guidelines on personal data breach notification</i> (2022).",
             "AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020)."],
)

# ------------------------------------------------------------------ 09 Who Still Has Access?
ar_problem = Doodle(760, 260, "Doodle of Larder's first access review, January 2028: 14 tools, 412 active accounts. In May 2027 Lena's review had found a support leaver with helpdesk and billing access for three weeks. Now: 23 accounts that shouldn't exist, 9 of them agency pickers who had left, because agency workers were never on HR's hiring form, so the joiners-leavers process never saw them leave.",
                    "412 accounts, 23 that shouldn't exist, 9 of them agency pickers the leavers process never saw.")
ar_problem.box(14, 30, 230, 100, "14 tools", "paper", sub="412 accounts", size=20, subsize=15)
ar_problem.box(264, 30, 230, 100, "23 to remove", "pink", sub="should not exist", size=20, subsize=15)
ar_problem.box(514, 30, 232, 100, "9 agency pickers", "pink", sub="never on HR's form", size=19, subsize=14)
ar_problem.note(380, 186, "the leavers process can't remove what it never saw join", "red", size=17)

ar_analogy = Doodle(760, 220, "Doodle of a sports club's members list. Once a season the treasurer sends each team captain the list of key fobs for their team's changing room. Captains tick who's still playing; the rest are switched off. The fobs of the guest players from the summer tournament, given out by the bar, never were on any team list.",
                    "Each season, captains tick their team's fobs. The bar's fobs for summer guests were on nobody's list.")
ar_analogy.icon("keycard", 60, 50, 1.3)
ar_analogy.box(170, 40, 270, 100, "captains tick their list", "green", sub="once a season", size=17, subsize=14)
ar_analogy.box(470, 40, 276, 100, "the bar's guest fobs", "pink", sub="on nobody's list", size=17, subsize=14)
ar_analogy.note(450, 190, "the owner of each door confirms who may use it", "pen", size=18)

ar_how = Doodle(760, 400, "Larder's quarterly access review from January 2028. For each of the 14 tools, its owner gets the list of accounts and roles, compares it with the staff list (now including agency and contract workers), and marks each one keep, change or remove within two weeks. Privileged roles are reviewed by two people. Removals happen the same week, logged. Fix to the cause: agency and contract workers are added to HR's form by the store managers, with an end date; accounts without an end date or owner are flagged monthly. Q1: 412 accounts, 23 removed, 31 roles reduced. Q2 in April: 6 removed. Evidence of each review is kept for the auditor.",
                "Each owner confirms their tool's list quarterly; agency workers now on the form with an end date. Q1: 23 removed; Q2: 6.")
ar_how.box(14, 14, 236, 110, "per tool owner", "blue", sub="list vs staff list · 2 weeks", size=18, subsize=13)
ar_how.box(262, 14, 236, 110, "keep · change · remove", "y", sub="privileged: two reviewers", size=17, subsize=13)
ar_how.box(510, 14, 236, 110, "removed that week", "green", sub="logged · evidence kept", size=17, subsize=13)
ar_how.box(14, 150, 732, 64, "fix the cause: agency + contract workers on HR's form, with an end date", "pink", size=15)
ar_how.row([("Q1 (Jan)", "412 · 23 removed · 31 reduced", "y"), ("Q2 (Apr)", "6 removed", "green")], x=110, y=240, h=86, w=250, gap=40, size=18, subsize=13, arrows=True)
ar_how.note(380, 362, "the review checks the process; the process does the daily work", "pen", size=15)

ACCESS_REVIEWS = dict(
    slug="access-reviews",
    kicker="a.k.a. “periodic access reviews”",
    tldr="Joiners-leavers processes remove access when they see someone leave. An <b>access review</b> catches what they miss: agency workers, role changes, exceptions that were never ended. Every quarter, <b>each tool's owner confirms who has access and why</b>, against a staff list that includes everyone (contractors and agency staff too). Remove the rest that week, review privileged roles twice, keep the evidence, and <b>fix the cause</b> of every miss.",
    chips=[("Family", "security operations"), ("Lives in", "a quarterly calendar entry per tool owner; ops/security/access-reviews/"), ("Pairs with", "joiners and leavers (vol. 1), production access (vol. 3), audit evidence")],
    itil=dict(groups=["general"], chain=["improve", "deliver"], practices=["information security management", "IT asset management"],
              sre="(least privilege, verified)", principles=["Think and work holistically", "Keep it simple and practical"],
              older="ITIL v3: access management, user access reviews"),
    problem_side="Larder, January 2028",
    problem="""  <p class="lead">In May 2027 Lena's review for Ana's identity work found a <b>support leaver who kept helpdesk and billing access for three weeks</b>. Eli runs Larder's first full access review in January 2028: <b>14 tools, 412 active accounts</b>. <b>23</b> shouldn't exist. <b>9</b> of them belong to <b>agency pickers</b> who had left. <span class="hl-pink">Agency workers were never on HR's hiring form, so the leavers process never saw them leave.</span></p>
  <ul>
    <li>A process can only remove access it knew about.</li>
    <li>Role changes add access more often than they remove it.</li>
    <li>Nobody owns the question “is this list still right?”</li>
  </ul>""",
    problem_figs=[ar_problem],
    analogy_side="the sports club's key fobs",
    analogy="""  <p>Once a season, a sports club's treasurer sends each <b>team captain</b> the list of key fobs for their changing room. Captains tick who's still playing, and the rest are switched off. But the fobs the bar handed to <b>guest players at the summer tournament</b> were never on any team's list, so they still open the door.</p>""",
    analogy_figs=[ar_analogy],
    map=[("Each team captain", "Each tool's owner"),
         ("The season's list", "The quarterly access list"),
         ("Ticking who's still playing", "Keep, change or remove"),
         ("The bar's guest fobs", "Agency pickers never on HR's form"),
         ("Putting guests on a list", "Agency and contract workers on the form, with an end date")],
    how_side="each owner confirms quarterly, and every miss fixes the process",
    how="""  <p>From <b>January</b>, every quarter:</p>
  <ul>
    <li>Each of the <b>14 tools' owners</b> gets the list of accounts and roles and compares it with a staff list that now includes <b>agency and contract workers</b>.</li>
    <li>They mark each account <b>keep, change or remove</b> within <b>two weeks</b>. Privileged roles are reviewed by <b>two people</b>.</li>
    <li>Removals happen <b>that week</b> and are logged. The review's evidence (who reviewed, what changed) is kept for auditors.</li>
  </ul>
  <p>Every miss gets its cause fixed. Agency and contract workers now go onto <b>HR's form</b>, entered by store managers, with an <b>end date</b>. Accounts without an end date or owner are flagged monthly. Q1 removes <b>23 accounts</b> and reduces <b>31 roles</b>. Q2 (April) removes only <b>6</b>: the process is catching more on its own. The review checks the process; the process does the daily work.</p>""",
    how_figs=[ar_how],
    steps=[("List every tool and its owner", "From the catalogue and the asset register."),
           ("Build a complete staff list", "Including agency and contract workers."),
           ("Send each owner their list quarterly", "Keep, change or remove in two weeks."),
           ("Review privileged roles twice", "Two people."),
           ("Remove that week; keep evidence", "Logged."),
           ("Fix the cause of each miss", "So the next review finds less.")],
    vocab=[("Access review", "A regular check by owners that every account and role is still needed."),
           ("Recertification", "Another name for confirming access is still valid."),
           ("Privileged role", "Access that can change systems or see sensitive data."),
           ("Access creep", "People collecting access over time as roles change."),
           ("End date", "When a temporary worker's access should stop."),
           ("Evidence", "The record that a review happened and what it changed.")],
    code=dict(file="ops/security/access-reviews/2028-Q1.md", note="January 2028 · 14 tools", plain=True, src="""
tool                owner    accounts   keep   change   remove   reviewers
helpdesk            Sam      61         54     4        3        Sam
billing SaaS        Cho      12         10     1        1        Cho + Marco (privileged)
rota tool           Joost    188        173    6        9 ← agency pickers
device management   Dee      9          8      1        0        Dee + Eli (privileged)
cloud console       Eli      14         11     3        0        Eli + Bram (privileged)
… 14 tools          total    412        358    31       23

cause of the 9     agency workers never on HR's form
fix                store managers add agency + contract workers with an END DATE (from 1 Feb)
monthly            accounts with no end date or no owner → flagged
Q2 (Apr): 6 removed
"""),
    tools="tools: exports from each tool, a complete staff list, a quarterly reminder, and a folder for evidence.",
    ladder=[("nobody checks", ["Access collected for years.", "Leavers missed silently."]),
            ("quarterly owner reviews", ["Privileged roles twice.", "Each miss fixes the process."]),
            ("reviews from the identity provider", ["Lists generated; owners click keep or remove.", "Evidence automatic."]),
            ("access expires by default", ["Temporary access ends by itself.", "Reviews find almost nothing."])],
    ladder_now=1,
    baseline="Each line compares <b>trusting the leavers process alone</b> to <b>quarterly owner reviews, with every miss fixing the process</b>.",
    ratings=[(3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (2, 4, "Who has what, confirmed by the owner, quarterly."),
             (3, 3, "Neutral."),
             (2, 3, "Unused seats removed."),
             (3, 3, "Neutral."),
             (3, 3, "Two weeks of light work per quarter.")],
    pitfalls=[("Reviewing without fixing the cause", "The same misses every quarter.", "fix the process for each miss."),
              ("A staff list without temporary workers", "Agency staff never appear.", "everyone who gets an account."),
              ("Rubber-stamping", "Owners tick “keep” for everything.", "two reviewers for privileged roles; spot checks."),
              ("No evidence kept", "Auditors can't see it happened.", "keep who reviewed what, and what changed.")],
    use=["You've found access for someone who left.", "Temporary or agency workers get accounts.", "Clients or auditors ask about access control.", "Before a security questionnaire."],
    skip=["Tools with access that expires on its own and is checked automatically."],
    related=["<b>Forty New People on Monday</b> (vol. 1)", "<b>Who May Touch Production?</b> (vol. 3)", "<b>Identity Federation & SSO</b> (Ana, vol. 4)", "<b>Prove It to the Auditor</b> (this volume)"],
    quiz=[("What does an access review catch that joiners-leavers doesn't?", "Accounts the process never saw: agency workers, role changes, unended exceptions."),
          ("Who reviews each tool's list?", "Its owner; privileged roles by two people."),
          ("Why did 9 agency pickers still have access?", "Agency workers were never on HR's form, so the leavers process never saw them leave."),
          ("How was the cause fixed?", "Store managers add agency and contract workers to HR's form with an end date."),
          ("What did Q2 show?", "Only 6 removals: the process catches more on its own.")],
    quiz_sit=[("A tool owner marks all 61 accounts “keep” in five minutes. What do you do?", "Spot-check a few against the staff list; if any are wrong, ask the owner to redo it properly, and consider a second reviewer for that tool. A review that changes nothing for a growing team is a warning sign.")],
    try_it="Export the accounts from one important tool and compare them with a complete staff list, including temporary workers. How many shouldn't exist? Why did your process miss them?",
    remember="The leavers process removes what it <span class=\"hl\">saw join</span>. A quarterly review by <span class=\"hl\">each owner</span> catches the rest, and fixes the process.",
    sources=["AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020).",
             "NIST SP 800-53 Rev. 5: AC-2(3) and AC-2(j), account review.",
             "CIS Critical Security Controls v8: control 5, account management."],
)

# ------------------------------------------------------------------ 10 Rotating the Keys
sk_problem = Doodle(760, 260, "Doodle of Larder's secrets inventory, April 2028: 61 secrets, from database passwords and payment provider keys to webhook signing secrets and certificates. 19 have never been rotated. The oldest is the payment provider key Jasper created in 2024. Three secrets are in a configuration file in the repository's history. Ana's October 2027 security review had already found business API keys that never expired.",
                    "61 secrets, 19 never rotated, the oldest from 2024, and three in the repository's history.")
sk_problem.box(14, 30, 180, 100, "61 secrets", "paper", size=20)
sk_problem.box(206, 30, 180, 100, "19 never rotated", "pink", size=18)
sk_problem.box(398, 30, 180, 100, "oldest: 2024", "pink", sub="Jasper's PSP key", size=18, subsize=13)
sk_problem.box(590, 30, 156, 100, "3 in git", "pink", sub="history", size=18, subsize=13)
sk_problem.note(380, 180, "nobody knows who owns half of them, or what breaks if one changes", "red", size=16)

sk_analogy = Doodle(760, 220, "Doodle of an office's keys after the locks are changed. A key cabinet with a list: which key opens what, who has a copy, when the lock was last changed. Locks are changed every few years, and immediately when someone leaves with a key. The first time, it takes a whole day to find out which doors each old key opened.",
                    "A key cabinet with a list: what each opens, who has a copy, when the lock was last changed.")
sk_analogy.icon("cabinet", 60, 40, 1.5)
sk_analogy.box(170, 40, 576, 100, "key · opens · copies · lock changed", "y", sub="changed on a schedule, and when someone leaves", size=17, subsize=14)
sk_analogy.note(450, 190, "the first full change takes a day; after that, an hour", "pen", size=18)

sk_how = Doodle(760, 400, "Larder's secrets practice from April 2028. Every secret lives in the vault, not in files or the repository; the three in the repository's history were rotated first and the history scanned in the pipeline from then on. Each secret has an owner, a purpose and a maximum age: database passwords rotated automatically every 30 days; API keys and signing secrets every 90 days; certificates on automatic renewal. Business API keys for clients expire after a year, with a reminder. A rotation drill on Tuesday 23 May 2028: rotate everything in one day. 58 of 61 rotated by 17:00; 3 needed the vendor's help and were done that week. The drill is repeated every year, and when someone with secret access leaves.",
                "In the vault, an owner and a maximum age for each, rotated automatically where possible, and a yearly rotate-everything drill.")
sk_how.box(14, 14, 236, 110, "in the vault", "blue", sub="not files · not git", size=19, subsize=13)
sk_how.box(262, 14, 236, 110, "owner + max age", "y", sub="DB 30 d · keys 90 d · certs auto", size=18, subsize=12)
sk_how.box(510, 14, 236, 110, "scan the pipeline", "green", sub="no secret merges", size=18, subsize=13)
sk_how.box(14, 150, 732, 64, "client API keys expire after a year, with a reminder (Ana's 2027 review)", "paper", size=15)
sk_how.row([("drill · 23 May", "rotate everything", "y"), ("by 17:00", "58 of 61", "green"), ("that week", "3 with vendors", "green")], x=14, y=240, h=86, gap=40, size=17, subsize=14, arrows=True)
sk_how.note(380, 364, "yearly, and whenever someone with secret access leaves", "pen", size=16)

SECRETS_ROTATION = dict(
    slug="secrets-rotation",
    kicker="a.k.a. “secrets and certificate management”",
    tldr="Passwords, API keys, signing secrets and certificates are the keys to your systems, and old keys get copied, leaked and forgotten. Keep every secret in a <b>vault</b> (never in files or the repository), give each an <b>owner, a purpose and a maximum age</b>, <b>rotate automatically</b> where you can, scan the pipeline so none slip in, and hold a yearly <b>rotate-everything drill</b>. Then rotating after a leak or a leaver is an hour's work, not a crisis.",
    chips=[("Family", "security operations"), ("Lives in", "the vault; ops/security/secrets.md; the pipeline's secret scan"), ("Pairs with", "access reviews, security incidents, patching (vol. 3)")],
    itil=dict(groups=["general", "technical"], chain=["deliver", "improve"], practices=["information security management", "infrastructure and platform management"],
              sre="(secrets as configuration, rotated automatically)", principles=["Optimise and automate"],
              older="ITIL v3: information security management (key management)"),
    problem_side="Larder, April 2028",
    problem="""  <p class="lead">After 9 March, Eli inventories Larder's secrets: <b>61</b> in all, from database passwords and payment provider keys to webhook signing secrets and certificates. <b>19 have never been rotated.</b> The oldest is the payment provider key <b>Jasper created in 2024</b>. <b>Three</b> are in a configuration file in the repository's history. Ana's October 2027 security review had already found business API keys that never expired. <span class="hl-pink">Nobody knows who owns half of them, or what breaks if one changes.</span></p>
  <ul>
    <li>An old secret has had years to be copied somewhere.</li>
    <li>Rotating feels risky because it has never been done.</li>
    <li>When someone leaves, their secret knowledge doesn't.</li>
  </ul>""",
    problem_figs=[sk_problem],
    analogy_side="the office key cabinet",
    analogy="""  <p>A well-run office has a <b>key cabinet with a list</b>: which key opens what, who has a copy, when the lock was last changed. Locks are changed every few years, and <b>immediately</b> when someone leaves with a key. The first time, it takes a whole day to find out which doors each old key opened. After that, it takes an hour.</p>""",
    analogy_figs=[sk_analogy],
    map=[("The key cabinet", "The vault"),
         ("The list", "Owner, purpose, maximum age per secret"),
         ("Changing the locks", "Rotating secrets"),
         ("When someone leaves with a key", "When someone with secret access leaves"),
         ("The first full change takes a day", "The 23 May drill: 58 of 61 by 17:00")],
    how_side="a vault, owners and ages, automatic rotation, and a yearly drill",
    how="""  <p>Bram leads the work in <b>April and May</b>:</p>
  <ul>
    <li><b>In the vault</b>: every secret moves to the vault. The three in the repository's history are <b>rotated first</b>, and from then on the pipeline <b>scans every change</b> for secrets and refuses to merge one.</li>
    <li><b>Owner, purpose, maximum age</b>: database passwords rotate <b>automatically every 30 days</b>; API keys and signing secrets every <b>90 days</b>; certificates are on <b>automatic renewal</b>. Business API keys for clients <b>expire after a year</b>, with a reminder to the client.</li>
    <li><b>A rotation drill</b>: on <b>Tuesday 23 May</b>, rotate everything in one day. <b>58 of 61</b> are done by 17:00. Three needed the vendor's help, and those are done that week. Jasper's 2024 payment key is finally retired.</li>
  </ul>
  <p>The drill is held <b>every year</b>, and the relevant secrets are rotated whenever someone with secret access leaves. Rotating after an incident like 9 March is now an hour's work.</p>""",
    how_figs=[sk_how],
    steps=[("Inventory every secret", "Where it lives, what uses it, who owns it."),
           ("Move them into a vault", "Out of files, chats and repositories."),
           ("Rotate anything ever exposed, first", "Like secrets in git history."),
           ("Set a maximum age per kind", "And automate rotation where possible."),
           ("Scan the pipeline", "So new secrets can't slip in."),
           ("Drill a full rotation yearly", "And after leavers with secret access.")],
    vocab=[("Secret", "Anything that grants access: password, API key, token, private key."),
           ("Vault", "A system that stores secrets securely and controls access to them."),
           ("Rotation", "Replacing a secret with a new one and retiring the old."),
           ("Maximum age", "How long a secret may live before rotation."),
           ("Secret scanning", "Checking code and history for secrets."),
           ("Short-lived credential", "A secret that expires by itself within minutes or hours.")],
    code=dict(file="ops/security/secrets.md", note="from April 2028 · drill Tue 23 May", plain=True, src="""
kind                  count  max age     rotation             owner examples
DB passwords          9      30 days     automatic (vault)    Eli, Bram
vendor API keys       14     90 days     reminder + runbook   Cho (PSP), Eli (WMS B)
webhook signing       8      90 days     reminder + runbook   Cho, Ben
client API keys       17     1 year      expire + reminder    Mo / Ben
certificates          13     auto-renew  automatic            Eli

first        3 secrets in git history → rotated 4 Apr · pipeline scan from 5 Apr
drill        Tue 23 May: 58 / 61 by 17:00 · 3 with vendors by 26 May
retired      PSP key from 2024 (Jasper) · 19 never-rotated secrets → 0
leavers      secret owners leaving → their secrets rotated within 1 week
"""),
    tools="tools: a vault (cloud or self-hosted), automatic database credential rotation, a secret scanner in the pipeline, and a calendar for the drill.",
    ladder=[("secrets anywhere, never rotated", ["Files, git, chats.", "Owners unknown."]),
            ("vault, owners, ages, a yearly drill", ["Automatic where possible.", "Pipeline scan."]),
            ("short-lived credentials", ["Services get credentials that expire in hours.", "Few long-lived secrets."]),
            ("secretless where possible", ["Workload identity instead of keys.", "Rotation rarely needed."])],
    ladder_now=1,
    baseline="Each line compares <b>61 secrets scattered and unrotated</b> to <b>a vault, owners and ages, automatic rotation and a yearly drill</b>.",
    ratings=[(3, 3, "Neutral."),
             (2, 3, "Rotation no longer feared; leaks contained fast."),
             (2, 4, "A leaked secret replaced in an hour."),
             (2, 3, "Rotations rehearsed, so they don't cause incidents."),
             (2, 4, "Every secret's owner and age known."),
             (2, 3, "Database passwords rotate themselves."),
             (3, 3, "Neutral."),
             (3, 3, "Neutral."),
             (3, 3, "A day a year for the drill.")],
    pitfalls=[("Secrets in git history", "Deleting the file doesn't remove it.", "rotate it, then scan."),
              ("No owner", "Nobody dares rotate it.", "an owner and a purpose per secret."),
              ("Rotation never practised", "The first one breaks production.", "a yearly drill."),
              ("Keys that never expire", "Clients' keys live forever.", "expiry with reminders.")],
    use=["You can't list your secrets and their owners.", "A secret may have leaked.", "Someone with access to secrets leaves.", "A client or auditor asks about key management."],
    skip=["Systems already using short-lived, automatic credentials end to end."],
    related=["<b>Secrets Management</b> (security, vol. 5)", "<b>Short-Lived Tokens</b> (security, vol. 5)", "<b>Who May Touch Production?</b> (vol. 3)", "<b>Who Still Has Access?</b> (this volume)"],
    quiz=[("What did the inventory find?", "61 secrets, 19 never rotated, the oldest from 2024, and three in the repository's history."),
          ("What happens to a secret found in git history?", "It's rotated (deleting the file isn't enough), and the pipeline scans for secrets from then on."),
          ("What are Larder's maximum ages?", "Database passwords 30 days (automatic), API keys and signing secrets 90 days, certificates auto-renew, client API keys 1 year."),
          ("What was the drill's result?", "58 of 61 rotated by 17:00 on 23 May; 3 with vendors that week."),
          ("When else are secrets rotated?", "When someone with access to them leaves.")],
    quiz_sit=[("An engineer pastes a database password into a team chat by mistake. What happens?", "Rotate that password now (it's in the vault, so it's quick), delete the message, and note it as a near miss. No blame; the fix is the rotation, not the apology.")],
    try_it="List ten secrets your service depends on. For each: where is it stored, who owns it, when was it last rotated? Rotate the oldest one this week, and time how long it takes.",
    remember="Every secret has <span class=\"hl\">an owner and an age</span>. Keep them in a vault, rotate on a schedule, and <span class=\"hl\">practise rotating everything</span> once a year.",
    sources=["OWASP, <i>Secrets Management Cheat Sheet</i>.",
             "NIST SP 800-57 Part 1 Rev. 5, <i>Recommendation for Key Management</i>.",
             "AXELOS, <i>ITIL 4: Information security management</i> practice guide (2020)."],
)

NOTES = [SECURITY_MONITORING, SECURITY_INCIDENTS, ACCESS_REVIEWS, SECRETS_ROTATION]
