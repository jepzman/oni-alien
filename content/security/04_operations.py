# Vol. 5 · Building & running: Threat Modelling, Audit Logging, Supply-Chain Hygiene, Defence in Depth.

# ------------------------------------------------------------------ 12 Threat Modelling
tm_problem = Doodle(760, 250, "Doodle of a project timeline: design, build, test, launch, and only then a penetration test two days before launch, which finds that the file upload feature lets anyone read anyone's files. Fixing it now means redesigning storage and delaying launch.",
                    "Security checked two days before launch: the design flaw is found when it's most expensive to fix.")
for i, t in enumerate(["design", "build", "test", "pen test", "launch"]):
    tm_problem.box(20 + i * 146, 60, 128, 54, t, "pink" if t == "pen test" else "paper", stroke="red" if t == "pen test" else "", size=17)
    if i:
        tm_problem.arrow(20 + i * 146 - 16, 87, 20 + i * 146 - 2, 87)
tm_problem.note(458, 150, "“anyone can read anyone's files”", "red")
tm_problem.note(458, 180, "→ redesign storage, slip launch", "red")
tm_problem.note(84, 150, "↑ cheapest to fix here", "green")

tm_analogy = Doodle(760, 250, "Doodle of a family planning a holiday with the house plans on the table, asking what could go wrong: a burst pipe, a burglar through the back window, the cat. For each, they decide a fix: turn off the water, lock the window, ask the neighbour.",
                    "Before a holiday: look at the house plan, ask “what could go wrong?”, and decide a fix for each.")
tm_analogy.icon("map", 40, 60, 1.8, fill="y")
tm_analogy.note(100, 200, "the house plan", "pen")
for i, (r, f) in enumerate([("burst pipe", "water off"), ("back window", "lock it"), ("the cat", "ask neighbour")]):
    tm_analogy.note(300, 70 + i * 50, r, "red", anchor="start")
    tm_analogy.arrow(450, 64 + i * 50, 500, 64 + i * 50)
    tm_analogy.note(510, 70 + i * 50, f, "green", anchor="start")
tm_analogy.note(450, 230, "four questions, one afternoon", "pen")

tm_how = Doodle(760, 290, "Threat modelling session. Draw a data-flow diagram: browser, API, database, file storage, with a trust boundary between the internet and the API. Walk each element with STRIDE: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. Record threats and mitigations in a table, for example information disclosure on file storage mitigated by per-user signed URLs.",
                "Draw the data flow, mark trust boundaries, walk it with STRIDE, and write down mitigations.")
tm_how.box(20, 50, 120, 54, "browser", "blue", size=17)
tm_how.line("M170 30 v120", color="red", dash=True)
tm_how.note(170, 170, "trust boundary", "red")
tm_how.arrow(146, 77, 216, 77)
tm_how.box(222, 50, 110, 54, "API", "y", size=17)
tm_how.arrow(338, 70, 398, 50)
tm_how.arrow(338, 90, 398, 120)
tm_how.db(450, 30, None, w=90, h=36)
tm_how.box(400, 104, 110, 46, "files", "pink", size=16)
tm_how.box(560, 20, 190, 190, None, "paper")
for i, (l, w) in enumerate([("S", "spoofing"), ("T", "tampering"), ("R", "repudiation"), ("I", "info disclosure"), ("D", "denial of service"), ("E", "elevation")]):
    tm_how.text(576, 48 + i * 28, f"{l} · {w}", "t" + (" t-red" if l == "I" else ""), anchor="start", size=16)
tm_how.note(300, 240, "I on files → per-user signed URLs, 5 min expiry", "green")
tm_how.note(300, 272, "ticket it · re-check when the design changes", "pen")

THREAT = dict(
    slug="threat-modeling",
    kicker="a.k.a. “what could go wrong while we're away?”",
    tldr="Before (and while) you build, sit down with a <b>diagram of how data flows</b>, mark the <b>trust boundaries</b>, and ask <b>“what can go wrong?”</b> for each part, using a checklist like <b>STRIDE</b>. Write down <b>threats, mitigations and owners</b>, turn them into tickets and tests, and revisit when the design changes. Design flaws are cheapest to fix on the whiteboard.",
    chips=[("Family", "secure design"), ("Frameworks", "STRIDE, LINDDUN (privacy), attack trees"), ("Four questions", "Adam Shostack"), ("Pairs with", "defence in depth, least privilege")],
    problem="""  <p class="lead">Security is often checked <span class="hl-pink">at the end</span>: a pen test just before launch. By then, the worst problems are <b>design flaws</b>, not bugs, and fixing them means rework and delays.</p>
  <ul>
    <li>“Anyone can read anyone's files” is a storage design problem.</li>
    <li>Nobody thought about what happens if the webhook sender is spoofed.</li>
    <li>Security reviews become a gate people try to dodge.</li>
  </ul>""",
    problem_figs=[tm_problem],
    analogy_side="planning for a holiday",
    analogy="""  <p>Before a family goes away, they look at the <b>house plan</b> and ask <b>“what could go wrong?”</b>: a burst pipe, a burglar through the back window, the cat. For each, they decide a <b>fix</b>: water off, lock the window, ask the neighbour. One afternoon, far cheaper than coming home to a flood.</p>
  <ul>
    <li>The house plan is a <b>data-flow diagram</b>.</li>
    <li>Doors and windows are <b>trust boundaries</b>.</li>
    <li>The list of fixes is your <b>mitigations</b>.</li>
  </ul>""",
    analogy_figs=[tm_analogy],
    map=[("The house plan", "A data-flow diagram"),
         ("Doors and windows", "Trust boundaries (internet → API, API → DB)"),
         ("“What could go wrong?”", "Walking each element with STRIDE"),
         ("Water off, window locked", "Mitigations, turned into tickets and tests"),
         ("Re-plan when you extend the house", "Revisit when the design changes")],
    how_side="four questions, on a diagram",
    how="""  <p>Shostack's four questions: <b>What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?</b> An hour with the team beats a perfect document nobody reads.</p>""",
    how_figs=[tm_how],
    steps=[("Draw it", "Users, services, data stores, external systems and the flows between them."),
           ("Mark trust boundaries", "Where data crosses from less trusted to more trusted."),
           ("Walk STRIDE per element", "Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege."),
           ("Decide and record", "Mitigate, accept, transfer or avoid; owner and ticket per threat."),
           ("Verify", "Turn mitigations into tests and review checks."),
           ("Keep it alive", "Update with each significant design change; keep it in the repo next to the code.")],
    vocab=[("Threat", "Something that could go wrong, caused by someone or something."),
           ("Data-flow diagram", "Picture of processes, stores and flows."),
           ("Trust boundary", "Where the level of trust changes."),
           ("STRIDE", "Mnemonic for six threat categories."),
           ("Mitigation", "A control that reduces a threat."),
           ("Residual risk", "Risk left after mitigations, accepted on purpose.")],
    code=dict(file="docs/threat-model/file-uploads.md", note="kept in the repo", src="""
## File uploads — threat model (v3, 2026-11)

Flow: browser → API → object storage (private bucket) → thumbnail worker

| # | STRIDE | Threat                                   | Mitigation                                   | Owner | Status |
|---|--------|------------------------------------------|----------------------------------------------|-------|--------|
| 1 | I      | User reads another user's files          | Per-user prefix + signed URLs, 5 min expiry  | ana   | done   |
| 2 | T      | Malicious file exploits the thumbnailer  | Sandbox worker, allow-list types, size limit | ben   | doing  |
| 3 | D      | 10 GB uploads exhaust storage            | 25 MB limit, per-user quota, rate limit       | cho   | done   |
| 4 | R      | “I never deleted that file”              | Audit log of upload/delete with user id      | ana   | todo   |

Accepted risk: EXIF metadata kept on originals (owner-only access).
"""),
    tools="tools: whiteboards and plain Markdown, OWASP Threat Dragon, Microsoft Threat Modeling Tool, threagile (threat models as code), the Elevation of Privilege card game, Adam Shostack's “Threat Modeling: Designing for Security”.",
    gains=["<b>Design flaws found early</b>, when cheap.",
           "<b>Shared understanding</b> of risks across the team.",
           "<b>Focused effort</b>: fix what matters most.",
           "<b>Documented decisions</b> for audits and newcomers."],
    losses=["<b>Meeting time</b>.",
            "<b>Can become paperwork</b> if over-formalised.",
            "<b>Goes stale</b> without updates.",
            "<b>Depends on who's in the room</b>."],
    baseline="Each line compares <b>only a pen test before launch</b> to <b>lightweight threat modelling during design</b>, kept in the repo.",
    ratings=[(3, 3, "A habit and a diagram, not a tool."),
             (3, 4, "Fewer last-minute security blockers."),
             (2, 4, "Disclosure paths found before building."),
             (2, 4, "Tampering and spoofing considered per flow."),
             (2, 4, "DoS threats get limits and quotas early."),
             (2, 4, "Trust boundaries drive isolation decisions."),
             (2, 4, "Decisions and accepted risks are written down."),
             (3, 3, "An hour now, weeks saved later."),
             (3, 4, "Teams learn to spot threats themselves.")],
    pitfalls=[("A 60-page document", "Nobody reads or updates it.", "a diagram and a table in the repo."),
              ("Only security people attend", "Developers don't own the outcome.", "the building team runs it; security coaches."),
              ("Once per project", "The design changes; the model doesn't.", "revisit with each significant change."),
              ("Threats without owners", "A long list that never turns into work.", "owner + ticket per mitigation.")],
    use=["New features handling sensitive data, money or uploads.",
         "New services, integrations and trust boundaries.",
         "Before big architecture changes."],
    skip=["Tiny UI tweaks with no new data flows.",
          "Don't model everything at once; start with the riskiest flow."],
    related=["<b>Defence in depth</b>", "<b>Least privilege</b>", "<b>Validate at the boundary</b>", "<b>Saga</b> (Vol. 1)"],
    quiz=[("What does STRIDE stand for?", "Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege."),
          ("What is a trust boundary?", "A place in the system where data or control passes between parts with different trust levels."),
          ("Name Shostack's four questions.", "What are we working on? What can go wrong? What are we going to do about it? Did we do a good job?"),
          ("When should you update a threat model?", "Whenever the design changes significantly, such as a new data flow, store or integration.")],
    remember="Look at the <span class=\"hl\">house plan</span>, ask what could go <span class=\"hl\">wrong</span>, and decide the <span class=\"hl\">fix</span> before you leave.",
    sources=["Adam Shostack, <i>Threat Modeling: Designing for Security</i> (2014).",
             "Threat Modeling Manifesto (threatmodelingmanifesto.org).",
             "OWASP, “Threat Modeling Cheat Sheet”.",
             "Microsoft, “The STRIDE Threat Model”."],
)

# ------------------------------------------------------------------ 13 Audit Logging
al_problem = Doodle(760, 250, "Doodle of an incident review. Someone downloaded the entire customer export last month. The application logs only say GET slash export 200, with no user, no tenant and no IP, and logs older than seven days were deleted. An admin account could also have edited the logs.",
                    "“Who exported all customers last month?” The logs say: GET /export 200. And they were deleted after 7 days.")
al_problem.box(20, 40, 340, 120, None, "paper", rx=3)
al_problem.text(36, 76, "GET /export 200", "t", anchor="start", size=17)
al_problem.text(36, 106, "GET /export 200", "t", anchor="start", size=17)
al_problem.text(36, 136, "(older: deleted)", "t t-soft", anchor="start", size=16)
al_problem.note(560, 60, "who? no user id", "red")
al_problem.note(560, 100, "which tenant? unknown", "red")
al_problem.note(560, 140, "admins can edit logs", "red")
al_problem.note(380, 220, "breach confirmed, scope unknown", "red")

al_analogy = Doodle(760, 250, "Doodle of a ship's logbook written in ink with numbered pages. Every entry has the time, who was on watch and what happened. Pages can't be torn out unnoticed because they're numbered, and copies are sent to the harbour office.",
                    "A ship's logbook: ink, numbered pages, who and when for every entry, copies sent ashore.")
al_analogy.icon("ledger", 40, 40, 2.2, fill="y")
for i, t in enumerate(["06:00 · Ana on watch · course 270", "06:40 · Ben · engine checked", "07:15 · Ana · storm warning"]):
    al_analogy.note(220, 70 + i * 40, t, "pen", anchor="start")
al_analogy.note(220, 200, "numbered pages · copy sent ashore", "green", anchor="start")

al_how = Doodle(760, 290, "Audit logging pipeline. The app writes a structured audit event for each sensitive action: who the actor is, the tenant, the action such as customer export, the target, the result, the time, the IP and a request id. Events are shipped to a separate append-only store with write-once retention for one year, which admins of the app can't modify. Alerts fire on unusual patterns like bulk exports at night.",
                "Structured events for sensitive actions, shipped to a separate, append-only store. Alerts on the unusual.")
al_how.box(20, 40, 160, 70, "app", "blue")
al_how.box(20, 140, 330, 120, None, "y")
for i, t in enumerate(["actor: ana@acme · tenant: 42", "action: customers.export", "target: all · result: ok", "ip · request_id · time"]):
    al_how.text(34, 166 + i * 26, t, "t", anchor="start", size=15)
al_how.arrow(186, 75, 440, 75, label="ship", lx=313, ly=61)
al_how.box(446, 40, 180, 90, "audit store", "green", sub="append-only · 1 year")
al_how.note(536, 160, "app admins: read-only", "pen")
al_how.arrow(632, 85, 700, 150, color="red")
al_how.note(690, 186, "alert: bulk", "red")
al_how.note(690, 210, "export at 3 am", "red")

AUDIT = dict(
    slug="audit-logging",
    kicker="a.k.a. “the ship's logbook”",
    tldr="For every <b>security-relevant action</b> (sign-ins, permission changes, exports, deletes, admin actions), write a <b>structured audit event</b>: <b>who</b>, <b>what</b>, <b>on which target</b>, <b>result</b>, <b>when</b>, <b>from where</b>. Ship it to a <b>separate, append-only store</b> that app admins <b>can't edit</b>, keep it long enough, and <b>alert</b> on unusual patterns. Never log secrets or more personal data than needed.",
    chips=[("Family", "detection &amp; forensics"), ("Log", "who · what · target · result · when · where"), ("Store", "append-only / WORM, separate account"), ("Pairs with", "history tables (Vol. 3), zero trust")],
    problem="""  <p class="lead">When something goes wrong, the first questions are <b>who, what and when</b>. Application logs are built for debugging, so they often <span class="hl-pink">can't answer them</span>, or they've already been rotated away.</p>
  <ul>
    <li>“GET /export 200” with no user or tenant.</li>
    <li>Logs deleted after 7 days; the breach is noticed after 40.</li>
    <li>An attacker with admin rights quietly deletes the evidence.</li>
  </ul>""",
    problem_figs=[al_problem],
    analogy_side="the ship's logbook",
    analogy="""  <p>A ship keeps a <b>logbook in ink</b> with <b>numbered pages</b>. Every entry says the time, <b>who was on watch</b> and what happened. A torn-out page would be noticed, and copies are <b>sent ashore</b>, beyond the crew's reach.</p>
  <ul>
    <li>Entries are <b>audit events</b>.</li>
    <li>Ink and numbered pages are <b>append-only, tamper-evident</b> storage.</li>
    <li>Copies ashore are a <b>separate account</b> the app's admins can't touch.</li>
  </ul>""",
    analogy_figs=[al_analogy],
    map=[("An entry in ink", "A structured audit event"),
         ("Who was on watch", "The actor (user or service id)"),
         ("Numbered pages", "Append-only, tamper-evident storage"),
         ("Copies sent ashore", "Shipped to a separate account / SIEM"),
         ("Captain reviews odd entries", "Alerts on unusual patterns")],
    how_side="structured, separate, append-only",
    how="""  <p>Audit logs are a <b>product feature</b> for your security team and your customers' admins: define the events, their fields and retention on purpose, not by accident.</p>""",
    how_figs=[al_how],
    steps=[("List auditable actions", "Sign-in/out, MFA changes, role changes, exports, deletes, settings, admin and support access."),
           ("Use a fixed schema", "actor, actor type, tenant, action, target, result, timestamp (UTC), IP, user agent, request id."),
           ("Write at the decision point", "Log where the action is authorised and performed, including failures."),
           ("Ship to a separate store", "Different account/project; append-only or WORM retention."),
           ("Protect privacy", "No passwords, tokens or full card numbers; minimise personal data."),
           ("Alert and review", "Rules for bulk exports, privilege changes, impossible travel; regular reviews.")],
    vocab=[("Audit event", "A record of a security-relevant action."),
           ("Actor", "Who or what performed the action."),
           ("Non-repudiation", "Being able to prove who did something."),
           ("WORM storage", "Write once, read many: can't be altered."),
           ("SIEM", "Security information and event management system."),
           ("Retention", "How long logs are kept.")],
    code=dict(file="audit.ts", note="structured audit events", src="""
type AuditEvent = {
  at: string; actor: { id: string; type: "user" | "service" }; tenantId: string;
  action: string; target: string; result: "ok" | "denied" | "error";
  ip?: string; requestId: string; meta?: Record<string, unknown>;
};

export function audit(e: Omit<AuditEvent, "at">) {
  auditSink.write({ ...e, at: new Date().toISOString() });   // separate pipeline
}

// at the decision point, success AND failure
if (!can(user, "customers.export", tenant)) {
  audit({ actor: { id: user.id, type: "user" }, tenantId: tenant.id,
          action: "customers.export", target: "all", result: "denied", requestId, ip });
  throw new Forbidden();
}
audit({ actor: { id: user.id, type: "user" }, tenantId: tenant.id,
        action: "customers.export", target: "all", result: "ok", requestId, ip,
        meta: { rows: count } });
"""),
    tools="tools: cloud audit trails (CloudTrail, GCP Audit Logs, Azure Activity Log), S3 Object Lock / immutable storage, SIEMs (Splunk, Elastic Security, Microsoft Sentinel, Panther), OpenTelemetry logs for shipping, WorkOS / Retraced-style audit log products.",
    gains=["<b>Answer who, what, when</b> after an incident.",
           "<b>Detect abuse</b> early with alerts.",
           "<b>Evidence</b> that survives an admin compromise.",
           "<b>Compliance</b> and customer trust (admin audit views)."],
    losses=["<b>Storage costs</b> for long retention.",
            "<b>Privacy risk</b> if logs hold too much personal data.",
            "<b>Alert fatigue</b> with noisy rules.",
            "<b>Effort</b> to define and maintain events."],
    baseline="Each line compares <b>debug-style app logs only</b> to <b>structured audit events in a separate append-only store with alerts</b>.",
    ratings=[(3, 3, "A schema and a pipeline to maintain."),
             (3, 3, "Invisible to users; admins may get an audit view."),
             (3, 3, "Neutral, if secrets are kept out of logs."),
             (2, 4, "Tamper-evident record of changes."),
             (3, 3, "Neutral."),
             (2, 4, "Fast detection limits how far an attacker gets."),
             (1, 5, "Who did what, when and from where."),
             (4, 3, "Storage, SIEM and review time."),
             (3, 4, "One audit() helper with a fixed schema.")],
    pitfalls=[("Logging secrets", "Tokens and passwords end up in the audit store.", "redact by schema; never log credentials."),
              ("Same account as the app", "An attacker with app admin deletes the logs.", "ship to a separate account with append-only retention."),
              ("Only successes", "Failed attempts, which show probing, are missing.", "log denied and failed actions too."),
              ("Unstructured text", "“User did export” can't be searched or alerted on.", "fixed fields, machine-readable JSON.")],
    use=["Authentication, authorization and admin actions.",
         "Exports, deletes, payments and settings changes.",
         "Support staff accessing customer data."],
    skip=["Every page view or debug detail (that's for app logs/metrics).",
          "Data you aren't allowed to keep (minimise)."],
    related=["<b>Zero trust</b>", "<b>Defence in depth</b>", "<b>History tables</b> (Vol. 3)", "<b>Change data capture</b> (Vol. 3)"],
    quiz=[("What fields should an audit event have?", "Actor, action, target, result, timestamp, tenant, source IP and a request id."),
          ("Why ship audit logs to a separate account?", "So an attacker or insider with app admin rights can't alter or delete them."),
          ("Should denied actions be logged?", "Yes; failed attempts reveal probing and abuse."),
          ("What must never appear in audit logs?", "Secrets such as passwords and tokens, and more personal data than needed.")],
    remember="Write it in <span class=\"hl\">ink</span>: who, what, when. And send a copy <span class=\"hl\">ashore</span>.",
    sources=["OWASP, “Logging Cheat Sheet” and “Logging Vocabulary Cheat Sheet”.",
             "NIST SP 800-92, “Guide to Computer Security Log Management”.",
             "OWASP Top 10 (2021), A09 “Security Logging and Monitoring Failures”.",
             "AWS docs, “S3 Object Lock”."],
)

# ------------------------------------------------------------------ 14 Supply-Chain Hygiene
sc_problem = Doodle(760, 260, "Doodle of an app with five direct dependencies that pull in eight hundred transitive packages. One small package deep in the tree gets a malicious new version, and because versions use caret ranges and the build pulls latest, the next build ships the malicious code to production. The Docker base image is also latest and two years unpatched.",
                    "5 direct packages, 800 transitive ones, floating versions: one poisoned update ships in the next build.")
sc_problem.box(20, 100, 120, 60, "your app", "blue", size=17)
for i in range(5):
    sc_problem.arrow(146, 130, 230, 40 + i * 44)
    sc_problem.box(236, 24 + i * 44, 110, 32, None, "paper", rx=4)
for i in range(10):
    sc_problem.line(f"M346 {40 + (i // 2) * 44} L420 {30 + i * 21}", thin=True)
sc_problem.note(480, 40, "800 transitive", "pen", anchor="start")
sc_problem.box(450, 120, 290, 50, "tiny-pkg 1.3.7: malicious", "pink", stroke="red", size=16)
sc_problem.note(470, 210, "FROM node:latest (2 yrs old)", "red", anchor="start")
sc_problem.note(470, 240, "next build ships it", "red", anchor="start")

sc_analogy = Doodle(760, 250, "Doodle of a restaurant kitchen receiving deliveries. Each crate is checked against the order sheet, sealed packages only, from known suppliers, with a label listing every ingredient. Recalled batches are pulled immediately because the kitchen knows exactly which batch went into which dish.",
                    "A kitchen checks every delivery: known suppliers, sealed, labelled, and recalls traced to the dish.")
sc_analogy.icon("truck", 30, 80, 1.6)
sc_analogy.arrow(140, 110, 230, 110)
sc_analogy.icon("parcel", 240, 70, 1.4, fill="y")
sc_analogy.icon("seal", 290, 120, 0.7, fill="green")
for i, t in enumerate(["✓ known supplier", "✓ seal intact", "✓ ingredient label", "✓ batch number logged"]):
    sc_analogy.note(430, 60 + i * 40, t, "green", anchor="start")

sc_how = Doodle(760, 300, "Supply-chain controls. A lockfile pins every package to an exact version and integrity hash. Dependency update bots open small pull requests that run tests. Scanners check for known vulnerabilities and malicious packages. The build produces a software bill of materials, signs the image, and records provenance. Deploys only accept signed images from the trusted build. Base images are minimal and pinned by digest.",
                "Pin and hash, update in small reviewed steps, scan, produce an SBOM, sign the build, and only deploy what you signed.")
steps_sc = [("lockfile", "exact + hash", "y"), ("update bot", "small PRs", "blue"), ("scan", "CVEs · malware", "pink"), ("SBOM", "what's inside", "green"), ("sign", "provenance", "green")]
for i, (t, sub, f) in enumerate(steps_sc):
    sc_how.box(10 + i * 150, 50, 136, 84, t, f, sub=sub, size=18, subsize=15)
    if i:
        sc_how.arrow(10 + i * 150 - 12, 92, 10 + i * 150 - 2, 92)
sc_how.arrow(700, 140, 700, 200, color="green")
sc_how.box(500, 204, 250, 56, "deploy: signed only", "green", size=17)
sc_how.note(240, 236, "base image: minimal, pinned by digest", "pen")

SUPPLY = dict(
    slug="supply-chain",
    kicker="a.k.a. “check the deliveries”",
    tldr="Most of your app is <b>other people's code</b>. Keep it under control: <b>lock</b> exact versions with integrity hashes, take updates through <b>small automated PRs</b> that run your tests, <b>scan</b> for known vulnerabilities and malicious packages, produce an <b>SBOM</b> so you know what's inside, <b>sign builds</b> with provenance, and <b>deploy only what you signed</b>, on minimal, pinned base images.",
    chips=[("Family", "software supply chain"), ("Frameworks", "SLSA, OpenSSF Scorecard, NIST SSDF"), ("Artefacts", "lockfiles, SBOM (CycloneDX/SPDX), signatures"), ("Pairs with", "least privilege, defence in depth")],
    problem="""  <p class="lead">A typical app has a handful of direct dependencies and <span class="hl-pink">hundreds of transitive ones</span>, plus base images, CI actions and build tools. Any of them can be vulnerable, abandoned, typosquatted or hijacked.</p>
  <ul>
    <li>Floating versions pull a malicious release into the next build.</li>
    <li>Nobody can say whether a newly announced vulnerability affects you.</li>
    <li>A two-year-old base image carries dozens of known CVEs.</li>
    <li>A CI action pinned to a tag is quietly changed upstream.</li>
  </ul>""",
    problem_figs=[sc_problem],
    analogy_side="checking the deliveries",
    analogy="""  <p>A good kitchen checks every delivery: <b>known suppliers</b>, <b>seals intact</b>, an <b>ingredient label</b> on every package, and a <b>batch number</b> logged. When a supplier recalls a batch, the kitchen knows <b>exactly which dishes</b> used it.</p>
  <ul>
    <li>The order sheet is your <b>lockfile</b>.</li>
    <li>The ingredient label is the <b>SBOM</b>.</li>
    <li>The seal is a <b>signature</b>; the batch log is <b>provenance</b>.</li>
  </ul>""",
    analogy_figs=[sc_analogy],
    map=[("The order sheet", "Lockfile with exact versions and hashes"),
         ("Known suppliers only", "Trusted registries, scoped packages, reviewed new deps"),
         ("Intact seals", "Integrity hashes and signature verification"),
         ("Ingredient labels", "An SBOM for every build"),
         ("Recall traced to the dish", "Knowing which services use a vulnerable package")],
    how_side="lock, update, scan, sign, verify",
    how="""  <p>Small, frequent updates are <b>safer</b> than rare big ones: each PR is easy to review and test, and you're never years behind when a critical fix lands.</p>""",
    how_figs=[sc_how],
    steps=[("Lock everything", "Commit lockfiles; install with <code>npm ci</code>; pin CI actions and base images by digest/SHA."),
           ("Review new dependencies", "Is it maintained? How many maintainers? Install scripts? Prefer fewer, well-known packages."),
           ("Automate updates", "Dependabot or Renovate: small PRs, tests, grouped minor updates, auto-merge only for low risk."),
           ("Scan continuously", "Known vulnerabilities (OSV, npm audit) and malicious package feeds; fail builds on criticals."),
           ("Generate an SBOM", "CycloneDX or SPDX per build, stored with the artefact."),
           ("Sign and verify", "Sign images with provenance (Sigstore/cosign, SLSA); admission control accepts only signed images.")],
    vocab=[("Transitive dependency", "A dependency of a dependency."),
           ("Lockfile", "Exact resolved versions and hashes of all packages."),
           ("SBOM", "Software bill of materials: what's inside a build."),
           ("Provenance", "Signed record of how and where an artefact was built."),
           ("Typosquatting", "Malicious packages with names like popular ones."),
           ("SLSA", "Framework of levels for build integrity.")],
    code=dict(file=".github/workflows/build.yml", note="pinned, scanned, signed", src="""
steps:
  - uses: actions/checkout@08eba0b27e820071cde6df949e0beb9ba4906955   # pinned SHA
  - run: npm ci --ignore-scripts          # exact lockfile, no install scripts
  - run: npx osv-scanner --lockfile=package-lock.json
  - run: docker build -t $IMAGE .         # FROM node:22.11-slim@sha256:…
  - run: syft $IMAGE -o cyclonedx-json > sbom.json
  - run: cosign sign --yes $IMAGE         # keyless, via the CI's OIDC identity
  - run: cosign attest --yes --type cyclonedx --predicate sbom.json $IMAGE

# cluster admission policy: only images signed by this repo's workflow may run
"""),
    tools="tools: Dependabot, Renovate, npm/pnpm lockfiles, OSV-Scanner, Snyk, Socket (malicious package detection), Syft/Trivy/Grype, CycloneDX, Sigstore cosign, SLSA GitHub generator, OpenSSF Scorecard, Kyverno / Sigstore policy-controller.",
    gains=["<b>Reproducible builds</b>: the same code every time.",
           "<b>Fast answers</b> to “are we affected?”",
           "<b>Poisoned updates blocked</b> or caught early.",
           "<b>Only trusted artefacts</b> reach production."],
    losses=["<b>A steady stream of update PRs</b>.",
            "<b>Scanner noise</b> and false positives.",
            "<b>Pipeline complexity</b> for signing and verification.",
            "<b>Pinned versions</b> need active updating."],
    baseline="Each line compares <b>floating versions, latest base images and no scanning</b> to <b>lockfiles, automated small updates, scanning, SBOMs and signed deploys</b>.",
    ratings=[(3, 3, "More pipeline steps, mostly automated."),
             (3, 3, "Invisible to users."),
             (2, 4, "Malicious packages are blocked before they ship."),
             (1, 5, "Only signed, provenance-checked builds deploy."),
             (3, 4, "Fewer emergency upgrades during incidents."),
             (2, 4, "SBOMs show exactly where a bad package is used."),
             (2, 5, "Every artefact says what's in it and how it was built."),
             (3, 3, "Tooling is mostly free; reviews take time."),
             (3, 3, "Update PRs are a constant, small chore.")],
    pitfalls=[("Ignoring the update PRs", "200 open Dependabot PRs; nobody looks.", "group updates, auto-merge low-risk, own the queue."),
              ("Pinning but never updating", "Locked to versions with known CVEs for years.", "small, regular updates."),
              ("Install scripts", "A package's postinstall runs arbitrary code in CI.", "<code>--ignore-scripts</code> where possible; review packages that need them."),
              ("Unpinned CI actions", "<code>uses: some/action@v1</code> changes underneath you.", "pin third-party actions by commit SHA.")],
    use=["Every project with dependencies (all of them).",
         "Container images and CI pipelines.",
         "Software you ship to customers."],
    skip=["Don't skip; scale it. A small project can start with a lockfile, Dependabot and one scanner."],
    related=["<b>Defence in depth</b>", "<b>Least privilege</b>", "<b>Short-lived tokens</b>", "<b>Parallel &amp; selective runs</b> (Vol. 4)"],
    quiz=[("Why are transitive dependencies a risk?", "They make up most of your code, and you didn't choose or review them directly."),
          ("What is an SBOM for?", "Knowing exactly which components and versions are in a build, so you can answer “are we affected?” quickly."),
          ("Why pin CI actions by commit SHA?", "Tags can be moved to point at different code; a SHA can't change."),
          ("What does signing images with provenance give you?", "Proof that an image was built by your trusted pipeline, which deploys can verify.")],
    remember="Check every <span class=\"hl\">delivery</span>: known supplier, intact <span class=\"hl\">seal</span>, and a <span class=\"hl\">label</span> on the box.",
    sources=["SLSA specification (slsa.dev).",
             "NIST SP 800-218, “Secure Software Development Framework (SSDF)”.",
             "OpenSSF, “Concise Guide for Evaluating Open Source Software”.",
             "CISA, “Software Bill of Materials (SBOM)”."],
)

# ------------------------------------------------------------------ 15 Defence in Depth
dd_problem = Doodle(760, 250, "Doodle of a single wall protecting everything. The application relies only on a firewall. When one bug in the login code lets an attacker through, there's nothing else: no least privilege, no encryption at rest, no monitoring, so the whole database is exported unnoticed.",
                    "One wall, one bug, nothing behind it.")
dd_problem.raw('<rect class="d f-y" x="300" y="20" width="40" height="210" rx="3"/>')
dd_problem.note(320, 245, "the only wall", "pen")
dd_problem.arrow(120, 120, 296, 120, color="red")
dd_problem.raw('<path class="d d-red" d="M310 110 l20 20 M330 110 l-20 20"/>')
dd_problem.arrow(344, 120, 520, 120, color="red", label="one bug → through", lx=432, ly=106)
dd_problem.db(600, 90, None, w=100, h=50)
dd_problem.note(650, 190, "all data, unnoticed", "red")
dd_problem.icon("dummy", 40, 80, 1.0, color="red")

dd_analogy = Doodle(760, 250, "Doodle of a medieval castle: a moat, an outer wall, an inner wall, guards at the keep, and the treasure in a locked chest. An attacker who crosses the moat still faces walls, guards and the lock, and the watchmen raise the alarm at each step.",
                    "A castle: moat, two walls, guards, a locked chest, and lookouts who raise the alarm.")
dd_analogy.raw('<ellipse class="d d-thin f-blue" cx="380" cy="130" rx="340" ry="110"/>')
dd_analogy.raw('<ellipse class="d f-paper" cx="380" cy="130" rx="260" ry="80"/>')
dd_analogy.raw('<ellipse class="d f-y" cx="380" cy="130" rx="170" ry="52"/>')
dd_analogy.icon("castle", 350, 92, 0.9)
dd_analogy.note(80, 130, "moat", "pen")
dd_analogy.note(175, 135, "wall", "pen")
dd_analogy.note(260, 138, "wall", "pen")
dd_analogy.icon("eye", 620, 40, 0.7)
dd_analogy.note(650, 100, "lookouts", "pen")

dd_how = Doodle(760, 300, "Layered defences for one web app. From outside in: a web application firewall and rate limits; strong identity and MFA; input validation and parameterized queries in the app; least-privilege database roles; encryption at rest with a KMS; and audit logs with alerts watching all layers. Each layer catches different failures; any single one can fail without a breach.",
                "Independent layers, each catching different failures. Monitoring watches them all.")
layers = [("WAF · rate limits", "blue"), ("identity · MFA", "y"), ("validation · safe queries", "green"), ("least-privilege roles", "y"), ("encryption · KMS", "green")]
for i, (t, f) in enumerate(layers):
    pad = i * 34
    dd_how.box(20 + pad, 20 + i * 44, 560 - 2 * pad, 40, t, f, size=16, rx=6)
dd_how.box(600, 20, 150, 216, None, "pink", stroke="red")
dd_how.head(675, 110, "audit +", size=18)
dd_how.head(675, 136, "alerts", size=18)
dd_how.note(675, 170, "watch every", "red")
dd_how.note(675, 194, "layer", "red")
dd_how.note(300, 278, "one layer fails → the next one still holds", "green")

DEPTH = dict(
    slug="defense-in-depth",
    kicker="a.k.a. “the castle”",
    tldr="Every control fails sometimes: a bug, a misconfiguration, a phished password. So stack <b>independent layers</b> (edge protection, strong identity, input handling, least privilege, encryption, monitoring), each catching <b>different failures</b>, so <b>no single mistake means a breach</b>. Choose layers that fail <b>for different reasons</b>, and make sure you'd <b>notice</b> when one is crossed.",
    chips=[("Family", "security architecture"), ("Origin", "military strategy; NSA guidance (2000s)"), ("Related idea", "the Swiss cheese model"), ("Pairs with", "zero trust, threat modelling, audit logging")],
    problem="""  <p class="lead">Many systems rely on <span class="hl-pink">one strong wall</span>: a firewall, a login page, or “it's internal”. When that one control has a bug, there's nothing behind it, and often nobody notices.</p>
  <ul>
    <li>A single auth bug exposes every record.</li>
    <li>The database user is admin, data isn't encrypted, and nothing alerts.</li>
    <li>“The WAF will catch it” replaces safe code.</li>
  </ul>""",
    problem_figs=[dd_problem],
    analogy_side="the castle",
    analogy="""  <p>A castle doesn't rely on one wall. There's a <b>moat</b>, an <b>outer wall</b>, an <b>inner wall</b>, <b>guards at the keep</b>, and the treasure in a <b>locked chest</b>. <b>Lookouts</b> raise the alarm at each step, so defenders have time to respond.</p>
  <ul>
    <li>Each obstacle is a <b>layer</b>.</li>
    <li>Different obstacles stop different attacks: <b>diversity</b>.</li>
    <li>Lookouts are <b>monitoring</b>: a layer crossed is a signal.</li>
  </ul>""",
    analogy_figs=[dd_analogy],
    map=[("The moat", "Edge: WAF, DDoS protection, rate limits"),
         ("The outer wall", "Strong identity and MFA"),
         ("The inner wall", "Input validation, safe queries, CSP"),
         ("Guards at the keep", "Least-privilege roles and service identities"),
         ("Locked chest + lookouts", "Encryption at rest + audit logs and alerts")],
    how_side="layers that fail differently",
    how="""  <p>Think of slices of Swiss cheese: each has holes, but the holes rarely line up. A breach needs <b>every</b> layer to fail at once.</p>""",
    how_figs=[dd_how],
    steps=[("Start from the threat model", "List the main threats and which layers stop each one."),
           ("Cover prevent, detect, respond", "Not only walls: logging, alerts and a practised incident plan."),
           ("Make layers independent", "Different mechanisms and owners, so one mistake doesn't disable several."),
           ("Assume each layer can fail", "Ask: if this layer is bypassed, what's the next one?"),
           ("Don't let layers excuse each other", "“The WAF will catch it” is not a reason for unsafe code."),
           ("Test the layers", "Pen tests, chaos-style game days, alert drills.")],
    vocab=[("Layer / control", "One mechanism that reduces risk."),
           ("Swiss cheese model", "Breaches happen when holes in all layers line up."),
           ("Preventive control", "Stops an attack (MFA, validation)."),
           ("Detective control", "Notices an attack (logs, alerts)."),
           ("Corrective control", "Limits damage and recovers (backups, revocation)."),
           ("Single point of failure", "One control whose failure exposes everything.")],
    code=dict(file="layers.md", note="one feature, many layers", src="""
Feature: customer data export

edge        rate limit 5 exports/hour/tenant · WAF managed rules
identity    SSO + passkey · re-authenticate before export (step-up)
app         schema-validated params · parameterized queries · tenant RLS
privilege   export worker role: SELECT on customers only · no DELETE
data        export file encrypted (KMS, per-tenant key) · signed URL, 10 min
detect      audit: customers.export (ok/denied) · alert on >3 exports/day
respond     runbook: revoke sessions, rotate keys, notify tenant admin

If any one line fails, which line still protects the data?
"""),
    tools="tools: everything in this volume, combined: WAF/CDN (Cloudflare, AWS WAF), identity provider with MFA, framework protections, database RLS and roles, KMS, SIEM and alerting, backups with restore tests, incident runbooks.",
    gains=["<b>No single point of failure</b>.",
           "<b>Time to detect and respond</b> before real damage.",
           "<b>Resilient to bugs</b> and misconfigurations.",
           "<b>Smaller breaches</b> when one happens."],
    losses=["<b>More cost and complexity</b>.",
            "<b>Possible friction</b> if layers stack up for users.",
            "<b>False confidence</b> if layers aren't independent.",
            "<b>More things to monitor</b> and maintain."],
    baseline="Each line compares <b>one strong perimeter control</b> to <b>independent layers across prevent, detect and respond</b>.",
    ratings=[(4, 2, "More layers, each simple, all to understand."),
             (4, 3, "Step-up checks add a little friction."),
             (2, 5, "Several layers must fail before data leaks."),
             (2, 4, "Tampering must beat validation, roles and logs."),
             (2, 4, "Edge protection and limits absorb attacks."),
             (1, 5, "Each layer limits how far a breach spreads."),
             (2, 5, "Detective layers record each step."),
             (4, 2, "More tools and more upkeep."),
             (3, 3, "Good defaults help; it's still a lot to know.")],
    pitfalls=[("Layers that share a weakness", "Three checks all trusting the same header.", "use different mechanisms and data sources."),
              ("Only preventive layers", "Walls but no lookouts: breaches go unnoticed for months.", "invest in detection and response too."),
              ("Layers as excuses", "“The WAF blocks SQL injection, so we skip parameters.”", "every layer must stand on its own."),
              ("Stacking friction on users", "Five prompts to change a setting; users find workarounds.", "put friction where risk is highest (step-up).")],
    use=["Any system with valuable data or money.",
         "Systems exposed to the internet.",
         "As the lens for reviewing every other pattern in this volume."],
    skip=["Don't add layers that duplicate an existing one without adding independence."],
    related=["<b>Threat modelling</b>", "<b>Zero trust</b>", "<b>Audit logging</b>", "<b>Bulkhead</b> (Vol. 1)"],
    quiz=[("What's the core idea of defence in depth?", "Multiple independent layers, so no single failure leads to a breach."),
          ("Why must layers be independent?", "If they share a weakness, one failure disables several layers at once."),
          ("Name the three kinds of controls.", "Preventive, detective and corrective (respond/recover)."),
          ("Is a WAF a reason to skip parameterized queries?", "No. Each layer must stand on its own; the WAF is an extra layer, not a replacement.")],
    remember="A <span class=\"hl\">moat</span>, two <span class=\"hl\">walls</span>, guards, a locked chest, and <span class=\"hl\">lookouts</span> on every tower.",
    sources=["NSA, “Defense in Depth: A practical strategy for achieving Information Assurance” (2001).",
             "James Reason, “Human error: models and management” (BMJ, 2000), Swiss cheese model.",
             "NIST SP 800-53 Rev. 5, “Security and Privacy Controls”.",
             "OWASP, “Secure Product Design Cheat Sheet”."],
)

NOTES = [THREAT, AUDIT, SUPPLY, DEPTH]
