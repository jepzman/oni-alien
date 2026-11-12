# Vol. 5 · Identity & access: Zero Trust, Least Privilege, OAuth 2.0 with PKCE, Short-Lived Tokens.

# ------------------------------------------------------------------ 01 Zero Trust
zt_problem = Doodle(760, 260, "Doodle of a castle with a moat. Everything outside the wall is untrusted, everything inside is trusted. An attacker phishes one employee's laptop, gets inside the network through the VPN, and can then reach the database, the admin panel and the payroll service freely, because inside means trusted.",
                    "Castle-and-moat: one phished laptop gets past the wall, and inside, everything trusts everything.")
zt_problem.raw('<rect class="d f-y" x="20" y="40" width="420" height="200" rx="6"/>')
zt_problem.note(230, 30, "the “trusted” network", "pen")
for i, t in enumerate(["database", "admin panel", "payroll"]):
    zt_problem.box(270, 60 + i * 56, 150, 40, t, "paper", size=15)
zt_problem.box(36, 140, 160, 50, "phished laptop", "pink", stroke="red", size=15)
for i in range(3):
    zt_problem.arrow(202, 165, 266, 80 + i * 56, color="red")
zt_problem.arrow(600, 165, 446, 165, color="red", label="VPN", lx=520, ly=150)
zt_problem.note(620, 60, "phished once,", "red", anchor="start")
zt_problem.note(620, 86, "trusted everywhere", "red", anchor="start")

zt_analogy = Doodle(760, 250, "Doodle of a modern office building where you badge in at the front door and again at every floor and every room. Your badge only opens the rooms your job needs, and the guard checks it each time, even though you're already inside.",
                    "A modern office: badge in at every door, every time, even when you're already inside.")
zt_analogy.icon("keycard", 40, 70, 1.6, fill="y")
for i, t in enumerate(["front door", "floor 3", "server room"]):
    x = 230 + i * 170
    zt_analogy.icon("door", x, 50, 1.4, fill="green" if i < 2 else "pink")
    zt_analogy.note(x + 40, 170, t, "pen")
    zt_analogy.note(x + 40, 196, "✓ badge" if i < 2 else "✗ not your job", "green" if i < 2 else "red")
zt_analogy.note(380, 240, "checked at every door, not just the first", "pen")

zt_how = Doodle(760, 290, "Zero trust request flow. Every request from a user or a service goes through a policy check: who is it, verified by strong identity; is the device healthy; is this action allowed for this resource; is the context normal. Only then is the request forwarded, over an encrypted connection, to the one resource. The check repeats for every request.",
                "Every request is checked on identity, device and policy, then gets access to one thing, encrypted. Network location means nothing.")
zt_how.box(20, 110, 140, 64, "request", "blue")
zt_how.arrow(166, 142, 256, 142)
zt_how.box(262, 40, 220, 210, None, "y")
zt_how.head(372, 70, "policy check", size=19)
for i, t in enumerate(["✓ who? (strong identity)", "✓ device healthy?", "✓ allowed for this?", "✓ context normal?"]):
    zt_how.text(276, 108 + i * 34, t, "t", anchor="start", size=16)
zt_how.arrow(488, 142, 578, 142, color="green", label="mTLS", lx=533, ly=128)
zt_how.box(584, 110, 160, 64, "one resource", "green", size=17)
zt_how.note(380, 278, "repeat for every request · inside or outside the network", "pen")

ZERO = dict(
    slug="zero-trust",
    kicker="a.k.a. “badge in at every door”",
    tldr="Stop trusting requests because they come from <b>inside the network</b>. In zero trust, <b>every request</b>, from a user or a service, proves <b>who it is</b> (strong identity), comes from a <b>healthy device</b>, is checked against <b>policy for that one resource</b>, and travels <b>encrypted</b>. A phished laptop or a compromised service then gets <b>very little</b>, not the keys to the kingdom.",
    chips=[("Family", "access architecture"), ("Origin", "John Kindervag (Forrester, 2010); Google BeyondCorp"), ("Standard", "NIST SP 800-207"), ("Pairs with", "least privilege, short-lived tokens")],
    problem="""  <p class="lead">The classic model is a <b>castle and moat</b>: a firewall around the office network, and <span class="hl-pink">anything inside is trusted</span>. Today people work from anywhere, apps live in several clouds, and attackers only need <b>one foothold</b>.</p>
  <ul>
    <li>One phished laptop on the VPN can reach the database and admin tools.</li>
    <li>A compromised internal service can call every other service.</li>
    <li>“It's only reachable internally” is used as a reason to skip authentication.</li>
  </ul>""",
    problem_figs=[zt_problem],
    analogy_side="the badge at every door",
    analogy="""  <p>In a modern office you <b>badge in at the front door</b>, then <b>again at your floor</b>, and <b>again at the server room</b>, which your badge doesn't open, because it's not your job. Being inside the building doesn't open every door.</p>
  <ul>
    <li>The badge is a <b>strong identity</b>.</li>
    <li>Each reader is a <b>policy check</b> for one resource.</li>
    <li>A lost badge only opens a few doors, and can be cancelled: <b>small blast radius</b>.</li>
  </ul>""",
    analogy_figs=[zt_analogy],
    map=[("The castle wall", "The network perimeter / VPN"),
         ("A badge reader on every door", "Authentication + authorization on every request"),
         ("Your badge only opens your rooms", "Per-resource policy (least privilege)"),
         ("Guard checks you look like you", "Device health and context checks"),
         ("Talking in a closed room", "Encrypted service-to-service traffic (mTLS)")],
    how_side="verify explicitly, every time",
    how="""  <p>Zero trust isn't a product. It's three habits: <b>verify explicitly</b>, <b>use least privilege</b>, and <b>assume breach</b>, so design as if an attacker is already inside.</p>""",
    how_figs=[zt_how],
    steps=[("Inventory", "List users, devices, services and the resources each needs."),
           ("Strong identity for people", "Single sign-on with phishing-resistant MFA (passkeys, security keys)."),
           ("Identity for services too", "Workload identities and mutual TLS instead of “internal network = trusted”."),
           ("Put a policy check in front of each app", "An identity-aware proxy or gateway decides per request: who, device, action, context."),
           ("Encrypt everything", "TLS everywhere, including inside the network."),
           ("Log and adapt", "Feed decisions into monitoring; step up checks when behaviour looks odd.")],
    vocab=[("Perimeter security", "Trust based on being inside the network."),
           ("Identity-aware proxy", "A gateway that checks identity and policy per request."),
           ("mTLS", "Mutual TLS: both client and server prove their identity."),
           ("Device posture", "Whether a device is managed, patched and encrypted."),
           ("Assume breach", "Design as if an attacker is already inside."),
           ("Lateral movement", "An attacker hopping from one system to the next.")],
    code=dict(file="policy.rego", note="Open Policy Agent", src="""
package app.authz

default allow := false

# every request: who, what, which resource, from which device
allow if {
  input.identity.verified_mfa
  input.device.managed
  input.device.disk_encrypted
  some role in input.identity.roles
  permitted[role][input.action][input.resource.type]
}

permitted := {
  "support": {"read":  {"ticket": true, "customer": true}},
  "billing": {"read":  {"invoice": true}, "refund": {"invoice": true}},
}
# no rule says "allow if source IP is internal"
"""),
    tools="tools: identity-aware proxies (Google IAP, Cloudflare Access, Pomerium, Tailscale), SSO with WebAuthn/passkeys (Okta, Entra ID), service meshes for mTLS (Istio, Linkerd), SPIFFE/SPIRE workload identity, Open Policy Agent.",
    gains=["<b>Small blast radius</b>: one stolen login reaches little.",
           "<b>Works anywhere</b>: office, home, cloud, no VPN needed.",
           "<b>Every access is logged</b> with identity and context.",
           "<b>Stops lateral movement</b> between services."],
    losses=["<b>A big programme</b>, not a switch.",
            "<b>More moving parts</b>: identity provider, proxies, policies.",
            "<b>Friction</b> if checks are clumsy.",
            "<b>Identity provider becomes critical</b>: if it's down, nobody gets in."],
    baseline="Each line compares a <b>castle-and-moat network</b> (VPN, trusted inside) to <b>zero-trust access</b> with per-request identity, device and policy checks.",
    ratings=[(4, 2, "Identity provider, proxies, policies and mTLS to run."),
             (3, 4, "SSO + passkeys often beats VPN clients."),
             (2, 4, "Encrypted everywhere; access per resource."),
             (3, 4, "Every request is authenticated, so forged ones fail."),
             (3, 3, "Depends on the identity provider staying up."),
             (1, 5, "One stolen login opens very little."),
             (2, 5, "Every decision is logged with who and why."),
             (4, 2, "Licences, setup and migration effort."),
             (3, 3, "Clear model, but more to configure.")],
    pitfalls=[("Buying a product called zero trust", "A new VPN box, same flat network behind it.", "change the model: identity and policy on every request."),
              ("Forgetting service-to-service traffic", "Users are checked; internal APIs still trust each other.", "give workloads identities and use mTLS."),
              ("Weak MFA", "SMS codes get phished or SIM-swapped.", "use phishing-resistant MFA (passkeys, security keys)."),
              ("All-or-nothing migration", "A two-year big bang that never ships.", "start with the most sensitive apps, one at a time.")],
    use=["Remote or hybrid teams.",
         "Apps spread across clouds and SaaS.",
         "Sensitive data or admin tools.",
         "Microservices that call each other."],
    skip=["Never skip the idea; scale the tooling to your size.",
          "A tiny team can start with SSO + MFA + no flat internal trust."],
    related=["<b>Least privilege</b>", "<b>Short-lived tokens</b>", "<b>Defence in depth</b>", "<b>Sidecar &amp; service mesh</b> (Vol. 1)"],
    quiz=[("What does zero trust stop trusting?", "Network location: being inside the network no longer grants access."),
          ("Name the three core principles.", "Verify explicitly, use least privilege, assume breach."),
          ("How do services prove identity to each other?", "Workload identities, typically with mutual TLS (often via a service mesh)."),
          ("Why does zero trust shrink the blast radius?", "Each request is checked for one resource, so a stolen credential or compromised device reaches only what it's allowed.")],
    remember="Being <span class=\"hl\">inside</span> opens nothing. Badge in at <span class=\"hl\">every door</span>.",
    sources=["NIST SP 800-207, “Zero Trust Architecture” (2020).",
             "Ward &amp; Beyer, “BeyondCorp: A New Approach to Enterprise Security” (;login:, 2014).",
             "CISA, “Zero Trust Maturity Model” v2.",
             "John Kindervag, “No More Chewy Centers” (Forrester, 2010)."],
)

# ------------------------------------------------------------------ 02 Least Privilege
lp_problem = Doodle(760, 260, "Doodle of a small reporting script that only needs to read the sales table, running with the database admin account. When its API key leaks on a public repository, the attacker can read every table, delete backups and create new admin users.",
                    "A report script with admin rights: one leaked key, and the attacker owns everything.")
lp_problem.box(20, 90, 180, 70, "sales report", "blue", sub="needs: read sales")
lp_problem.arrow(206, 125, 300, 125, label="db_admin key", lx=253, ly=110)
lp_problem.box(306, 40, 190, 170, None, "pink", stroke="red")
for i, t in enumerate(["read all tables", "DROP backups", "CREATE admin", "export customers"]):
    lp_problem.text(320, 76 + i * 36, t, "t t-red", anchor="start", size=16)
lp_problem.note(630, 90, "key leaked on", "red")
lp_problem.note(630, 116, "a public repo →", "red")
lp_problem.note(630, 142, "game over", "red")

lp_analogy = Doodle(760, 250, "Doodle of a hotel key card that opens only your room and the gym, and only until check-out. The cleaner's card opens the rooms on one floor during working hours. Only the manager has a master key, kept in a safe.",
                    "Hotel key cards: your room and the gym, until check-out. The master key stays in the safe.")
for i, (t, sub, f) in enumerate([("guest", "room 214 + gym · until Sun", "green"), ("cleaner", "floor 2 · 8:00–16:00", "y"), ("manager", "master · in the safe", "pink")]):
    x = 20 + i * 250
    tl = lp_analogy
    tl.icon("keycard", x + 70, 30, 1.4, fill=f)
    tl.note(x + 110, 150, t, "pen")
    tl.note(x + 110, 176, sub)
lp_analogy.note(380, 230, "each card opens only what its holder needs", "green")

lp_how = Doodle(760, 290, "Least privilege applied. The sales report gets a role that can only select from the sales table. The billing service can read invoices and insert refunds. Deploys use a separate migration role. A human admin uses just-in-time elevation that expires after one hour and is approved and logged. Unused permissions are found by access analysis and removed.",
                "One narrow role per job, time-boxed elevation for humans, and regular clean-up of unused rights.")
roles = [("report_reader", "SELECT sales", "green"), ("billing_svc", "read invoices · insert refunds", "green"), ("migrator", "ALTER (deploys only)", "y")]
for i, (t, sub, f) in enumerate(roles):
    lp_how.box(20, 20 + i * 80, 300, 64, t, f, sub=sub, size=18)
lp_how.box(400, 40, 340, 90, "admin: just-in-time", "pink", sub="approved · 1 hour · logged", size=18)
lp_how.icon("clock", 690, 140, 0.8)
lp_how.box(400, 170, 340, 70, "unused for 90 days → removed", "blue", size=16)

LEAST = dict(
    slug="least-privilege",
    kicker="a.k.a. “the hotel key card”",
    tldr="Give every person, service and key <b>only the permissions its job needs</b>, on <b>only the resources</b> it touches, for <b>only as long</b> as it needs them. Use <b>narrow roles</b> per workload, <b>just-in-time</b> elevation for humans, and <b>remove unused rights</b> regularly. When something leaks, it can only do a little.",
    chips=[("Family", "access control"), ("Origin", "Saltzer &amp; Schroeder, 1975"), ("Tools", "IAM roles, RBAC/ABAC, JIT access, access analyzers"), ("Pairs with", "zero trust, secrets management")],
    problem="""  <p class="lead">Permissions are granted generously (“just give it admin so it works”) and <span class="hl-pink">almost never taken away</span>. Every over-powered key is a bigger prize for an attacker, and a bigger mess when someone makes a mistake.</p>
  <ul>
    <li>A read-only report runs as the database admin.</li>
    <li>Ex-employees and old services still have access years later.</li>
    <li>A typo in a script deletes production because the script could.</li>
  </ul>""",
    problem_figs=[lp_problem],
    analogy_side="the hotel key card",
    analogy="""  <p>Your hotel card opens <b>your room and the gym</b>, and stops working at <b>check-out</b>. The cleaner's card opens <b>one floor, during the shift</b>. The <b>master key</b> lives in the manager's safe and is signed out when needed.</p>
  <ul>
    <li>Your card is a <b>narrow role</b>.</li>
    <li>“Until Sunday” is an <b>expiry</b>.</li>
    <li>Signing out the master key is <b>just-in-time elevation</b>, with a log.</li>
  </ul>""",
    analogy_figs=[lp_analogy],
    map=[("Card opens room 214 + gym", "A role with only the needed actions and resources"),
         ("Stops working at check-out", "Time-limited grants and short-lived credentials"),
         ("Cleaner: one floor, one shift", "Scoped service roles"),
         ("Master key signed out from the safe", "Just-in-time admin access, approved and logged"),
         ("Cancel cards of departed guests", "Access reviews and removing unused permissions")],
    how_side="narrow, short, reviewed",
    how="""  <p>Least privilege works best when it's the <b>default</b>: new roles start empty, and every permission has a reason, an owner and, ideally, an expiry.</p>""",
    how_figs=[lp_how],
    steps=[("One identity per workload", "No shared “app” user; each service, job and person has its own identity."),
           ("Start from zero", "Grant specific actions on specific resources (<code>SELECT</code> on <code>sales</code>), not wildcards."),
           ("Separate duties", "Runtime roles can't change schema; deploy roles can't read customer data."),
           ("Time-box human admin", "Just-in-time elevation with approval, expiry and logs; no standing admin."),
           ("Review and prune", "Use access analyzers and last-used data; remove what hasn't been used in 90 days.")],
    vocab=[("Principle of least privilege", "Only the access needed, nothing more."),
           ("RBAC", "Role-based access control: permissions grouped into roles."),
           ("ABAC", "Attribute-based: decisions use attributes like team or region."),
           ("Just-in-time access", "Temporary elevation granted when needed."),
           ("Standing privilege", "Access held permanently, used or not."),
           ("Separation of duties", "No single identity can do every risky step.")],
    code=dict(file="roles.sql + reader-policy.json", note="PostgreSQL + AWS IAM", src="""
-- the report can read one table, and nothing else
CREATE ROLE report_reader LOGIN;
GRANT SELECT ON sales TO report_reader;
ALTER ROLE report_reader SET statement_timeout = '30s';

-- the invoice worker can read one bucket prefix
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::acme-invoices/2026/*"
  }]
}
// not "Action": "s3:*", not "Resource": "*"
"""),
    tools="tools: cloud IAM (AWS, GCP, Azure) with access analyzers and last-accessed data, Kubernetes RBAC, database roles, Teleport / StrongDM / cloud PIM for just-in-time access, policy linters like Checkov and tfsec.",
    gains=["<b>Small blast radius</b> for leaks and mistakes.",
           "<b>Clear ownership</b>: every permission has a reason.",
           "<b>Easier audits</b> and compliance.",
           "<b>Fewer accidents</b>: scripts can't do what they shouldn't."],
    losses=["<b>More roles</b> to define and maintain.",
            "<b>“Permission denied” friction</b> while getting it right.",
            "<b>Reviews take time</b>.",
            "<b>Too narrow</b> can break things in production."],
    baseline="Each line compares <b>broad, standing admin-style access</b> to <b>narrow per-workload roles with JIT elevation and regular reviews</b>.",
    ratings=[(4, 3, "More roles, but each one is simple."),
             (4, 3, "Occasional “access denied” until roles settle."),
             (2, 5, "Each identity sees only its own data."),
             (2, 4, "Fewer identities can change things."),
             (3, 4, "Mistaken deletes and rogue scripts are limited."),
             (1, 5, "A leaked key reaches one table or prefix."),
             (2, 4, "Grants have owners, reasons and expiry."),
             (4, 3, "Design and review time."),
             (3, 3, "Needs good templates to stay easy.")],
    pitfalls=[("Wildcards “for now”", "<code>\"Action\": \"*\"</code> ships and stays for years.", "start from zero; lint policies for wildcards."),
              ("Shared accounts", "Five services use one database user.", "one identity per workload."),
              ("Standing admin for humans", "Every engineer is always admin.", "just-in-time elevation with expiry."),
              ("Never removing access", "Old services and leavers keep permissions.", "automated reviews using last-used data.")],
    use=["Every system, every identity: it's a default, not a feature.",
         "Especially service accounts, CI pipelines and API keys.",
         "Admin access to production and customer data."],
    skip=["Don't skip it; just don't spend weeks on throwaway prototypes with no real data."],
    related=["<b>Zero trust</b>", "<b>Secrets management</b>", "<b>Short-lived tokens</b>", "<b>Bulkhead</b> (Vol. 1)"],
    quiz=[("What does least privilege limit?", "Which actions, on which resources, for how long each identity can act."),
          ("What's just-in-time access?", "Temporary elevated access granted when needed, with approval and an expiry, instead of standing admin rights."),
          ("Why one identity per workload?", "So each one gets only its own permissions, and logs and revocation are precise."),
          ("How do you find permissions to remove?", "Use last-used data and access analyzers; remove what hasn't been used in a set period.")],
    remember="Each card opens <span class=\"hl\">your room</span>, until <span class=\"hl\">check-out</span>. The master key stays in the <span class=\"hl\">safe</span>.",
    sources=["Saltzer &amp; Schroeder, “The Protection of Information in Computer Systems” (1975).",
             "NIST SP 800-53, AC-6 “Least Privilege”.",
             "AWS docs, “Apply least-privilege permissions” and IAM Access Analyzer.",
             "OWASP Top 10 (2021), A01 “Broken Access Control”."],
)

# ------------------------------------------------------------------ 03 OAuth 2.0 with PKCE
oa_problem = Doodle(760, 260, "Doodle of a third-party app that asks for the user's email password so it can read their calendar. The app now holds the full password, can read all mail, and the user can't revoke just that app without changing their password everywhere.",
                    "“Give us your Google password and we'll read your calendar.” Now the app can do anything, forever.")
oa_problem.box(20, 80, 200, 80, "Cool Calendar App", "blue", size=17)
oa_problem.box(20, 180, 200, 50, "password: ●●●●●●", "pink", stroke="red", size=16)
oa_problem.arrow(226, 120, 420, 120, color="red", label="logs in as you", lx=323, ly=106)
oa_problem.box(426, 60, 300, 120, None, "pink", stroke="red")
for i, t in enumerate(["read all mail", "delete files", "change password"]):
    oa_problem.text(440, 92 + i * 32, t, "t t-red", anchor="start", size=16)
oa_problem.note(500, 220, "revoke? change your password", "red")

oa_analogy = Doodle(760, 250, "Doodle of a valet key. You give the parking attendant a special valet key that starts the car and opens the driver's door, but not the boot or the glovebox. You never hand over your house keys, and you can cancel the valet key at any time.",
                    "A valet key: it drives the car, but can't open the boot. You keep your real keys.")
oa_analogy.icon("key", 40, 60, 1.8, fill="y")
oa_analogy.note(110, 170, "valet key", "pen")
oa_analogy.icon("truck", 260, 60, 1.6)
oa_analogy.note(560, 70, "✓ start the car", "green", anchor="start")
oa_analogy.note(560, 110, "✗ open the boot", "red", anchor="start")
oa_analogy.note(560, 150, "✗ your house keys", "red", anchor="start")
oa_analogy.note(560, 200, "cancel it any time", "pen", anchor="start")

oa_how = Doodle(760, 300, "Authorization code flow with PKCE. Step one, the app makes a random code verifier and sends its hash, the code challenge, when redirecting the user to the identity provider. Step two, the user signs in and approves the scope calendar read, at the provider. Step three, the provider redirects back with a one-time code. Step four, the app exchanges the code plus the original verifier for tokens. An attacker who steals the code can't use it without the verifier.",
                "The user signs in at the provider; the app gets a code, then trades it plus a secret verifier for scoped tokens.")
oa_how.box(20, 40, 160, 70, "your app", "blue")
oa_how.box(580, 40, 160, 70, "identity provider", "y", size=16)
oa_how.arrow(186, 60, 574, 60, label="① redirect + challenge = hash(verifier)", lx=380, ly=46)
oa_how.icon("badge", 650, 116, 0.9)
oa_how.note(630, 150, "② user signs in, approves “calendar.read”", "pen", anchor="end")
oa_how.arrow(574, 96, 186, 96, color="green", label="③ back with a one-time code", lx=380, ly=88)
oa_how.arrow(100, 116, 560, 250, label="④ code + verifier →", lx=280, ly=200, anchor="end")
oa_how.box(566, 236, 180, 50, "scoped tokens", "green", size=17)
oa_how.note(160, 266, "stolen code alone is useless", "green")

OAUTH = dict(
    slug="oauth-pkce",
    kicker="a.k.a. “the valet key”",
    tldr="Never ask users for their password to another service. With <b>OAuth 2.0</b>, the user signs in <b>at the provider</b> and approves a <b>narrow scope</b>; your app gets a <b>one-time code</b> and swaps it for <b>tokens</b>. <b>PKCE</b> ties the code to a secret only your app knows, so an intercepted code is useless. Use the <b>authorization code flow + PKCE</b> for every client type, and <b>OpenID Connect</b> on top for sign-in.",
    chips=[("Family", "delegated authorization"), ("Specs", "OAuth 2.0 (RFC 6749), PKCE (RFC 7636), OAuth 2.1 draft"), ("Sign-in layer", "OpenID Connect"), ("Pairs with", "short-lived tokens, least privilege")],
    problem="""  <p class="lead">Apps used to ask for your <span class="hl-pink">actual password</span> to another service to get your data. That hands over <b>everything</b>, forever, with no way to revoke one app. And rolling your own sign-in is where most auth bugs come from.</p>
  <ul>
    <li>The app can read all your mail when it only needed your calendar.</li>
    <li>Revoking it means changing your password everywhere.</li>
    <li>Old “implicit” flows leaked tokens in browser URLs and history.</li>
  </ul>""",
    problem_figs=[oa_problem],
    analogy_side="the valet key",
    analogy="""  <p>Some cars come with a <b>valet key</b>: it starts the car and opens the driver's door, but <b>not the boot or glovebox</b>. You hand that to the attendant, never your house keys, and you can <b>cancel</b> it any time.</p>
  <ul>
    <li>The valet key is an <b>access token</b> with a <b>scope</b>.</li>
    <li>The car maker issuing it is the <b>authorization server</b>.</li>
    <li>Your house keys (password) never leave your pocket.</li>
  </ul>""",
    analogy_figs=[oa_analogy],
    map=[("Your real car and house keys", "The user's password, only typed at the provider"),
         ("The valet key", "An access token"),
         ("“Drive only, no boot”", "Scopes like <code>calendar.read</code>"),
         ("Ticket you swap for the key", "The one-time authorization code"),
         ("Only you know the ticket's secret word", "PKCE code verifier")],
    how_side="code flow + PKCE",
    how="""  <p>PKCE (“pixy”) is small: hash a random secret, send the hash first, prove you know the secret later. It protects mobile apps, SPAs and server apps alike, which is why OAuth 2.1 makes it mandatory.</p>""",
    how_figs=[oa_how],
    steps=[("Use a provider and a library", "Don't hand-roll: use your identity provider's SDK or a certified OIDC client."),
           ("Generate verifier + challenge", "A random <code>code_verifier</code>; send <code>S256</code> hash as <code>code_challenge</code>, plus a random <code>state</code>."),
           ("Redirect to the provider", "The user signs in and consents to narrow scopes; your app never sees the password."),
           ("Exchange the code", "Back-channel POST with the code and the verifier; check <code>state</code>."),
           ("Validate tokens", "Check signature, issuer, audience and expiry of the ID token; store tokens safely (server side or secure cookies)."),
           ("Avoid old flows", "No implicit flow, no password grant.")],
    vocab=[("OAuth 2.0", "A framework for delegated access with tokens."),
           ("OpenID Connect", "A sign-in layer on OAuth that adds an ID token."),
           ("Authorization code", "A one-time code swapped for tokens."),
           ("PKCE", "Proof Key for Code Exchange: binds the code to the client."),
           ("Scope", "What a token may do (<code>calendar.read</code>)."),
           ("Redirect URI", "Pre-registered address the provider sends users back to.")],
    code=dict(file="login.ts", note="oauth4webapi-style, server side", src="""
// ① start sign-in
const verifier = generateRandomCodeVerifier();
const challenge = await calculatePKCECodeChallenge(verifier);   // S256
const state = generateRandomState();
session.set({ verifier, state });

redirect(`${issuer}/authorize?` + new URLSearchParams({
  response_type: "code", client_id, redirect_uri,
  scope: "openid email calendar.read",
  code_challenge: challenge, code_challenge_method: "S256", state,
}));

// ③ callback: check state, swap code + verifier for tokens
const params = validateAuthResponse(as, client, callbackUrl, session.state);
const res = await authorizationCodeGrantRequest(as, client, params, redirect_uri, session.verifier);
const { id_token, access_token } = await processAuthorizationCodeOpenIDResponse(as, client, res);
"""),
    tools="tools: identity providers (Auth0, Okta, Entra ID, Keycloak, Cognito, Google), libraries like oauth4webapi, openid-client, Auth.js, Spring Security, AppAuth for mobile.",
    gains=["<b>No password sharing</b> with third-party apps.",
           "<b>Narrow, revocable access</b> via scopes and tokens.",
           "<b>Intercepted codes are useless</b> thanks to PKCE.",
           "<b>Sign-in handled by experts</b> (MFA, passkeys, lockouts)."],
    losses=["<b>More concepts</b>: flows, tokens, scopes, redirects.",
            "<b>Dependency</b> on an identity provider.",
            "<b>Misconfiguration risks</b>: redirect URIs, token validation.",
            "<b>Extra redirects</b> in the user journey."],
    baseline="Each line compares <b>collecting and storing users' passwords for other services</b> (or hand-rolled login) to <b>authorization code flow + PKCE with an identity provider</b>.",
    ratings=[(3, 2, "More moving parts; libraries hide most of it."),
             (3, 4, "“Sign in with…” and SSO are familiar and quick."),
             (1, 5, "Passwords never reach your app."),
             (2, 4, "Signed tokens, state checks, PKCE binding."),
             (3, 3, "Depends on the provider's uptime."),
             (1, 4, "A leaked token is scoped and expires."),
             (2, 4, "Consents and sign-ins are logged by the provider."),
             (3, 3, "Provider costs, less custom auth code."),
             (3, 4, "Good SDKs make the safe path easy.")],
    pitfalls=[("Implicit flow or password grant", "Tokens in URLs or apps handling passwords.", "use authorization code + PKCE everywhere."),
              ("Loose redirect URIs", "Wildcards let attackers receive codes.", "register exact redirect URIs."),
              ("Not validating ID tokens", "Accepting any token that parses.", "check signature, issuer, audience, expiry, nonce."),
              ("Huge scopes", "Asking for “full access” when you need one calendar.", "request the narrowest scopes, incrementally.")],
    use=["Any “sign in with…” or SSO.",
         "Third-party access to user data (APIs, integrations).",
         "SPAs, mobile and desktop apps (PKCE is essential)."],
    skip=["Machine-to-machine calls with no user (use client credentials or workload identity).",
          "Internal tools already behind an identity-aware proxy."],
    related=["<b>Short-lived tokens</b>", "<b>Zero trust</b>", "<b>Least privilege</b>", "<b>API gateway</b> (Vol. 1)"],
    quiz=[("What problem does OAuth solve?", "Delegated access: an app gets limited, revocable access to a user's data without ever seeing their password."),
          ("What does PKCE protect against?", "An intercepted authorization code being exchanged by someone else: they don't have the code verifier."),
          ("What does OpenID Connect add?", "Sign-in: an ID token that tells the app who the user is."),
          ("Which flows should you avoid?", "The implicit flow and the resource-owner password grant.")],
    remember="Hand over a <span class=\"hl\">valet key</span>, never your <span class=\"hl\">house keys</span>, and bind the ticket with a <span class=\"hl\">secret word</span>.",
    sources=["RFC 6749, “The OAuth 2.0 Authorization Framework”.",
             "RFC 7636, “Proof Key for Code Exchange by OAuth Public Clients”.",
             "RFC 9700, “Best Current Practice for OAuth 2.0 Security”.",
             "OpenID Connect Core 1.0."],
)

# ------------------------------------------------------------------ 04 Short-Lived Tokens
st_problem = Doodle(760, 250, "Doodle of an API key created in 2021 that never expires. It has been copied into three laptops, a CI system and a chat message. When it leaks, nobody knows which copy, and rotating it would break unknown systems, so it stays valid.",
                    "A key from 2021 that never expires, copied everywhere. Leaked? Nobody dares rotate it.")
st_problem.icon("key", 30, 80, 1.6, fill="y")
st_problem.note(140, 200, "created 2021 · expires: never", "red")
for i, t in enumerate(["laptop", "CI", "chat", "wiki", "old VM"]):
    st_problem.arrow(150, 110, 396, 38 + i * 44)
    st_problem.box(400, 20 + i * 44, 130, 36, t, "paper", size=15)
st_problem.note(650, 120, "leaked from", "red")
st_problem.note(650, 146, "which one?", "red")

st_analogy = Doodle(760, 250, "Doodle of a cinema ticket valid for one showing today, and a membership card that issues a new ticket each visit. If you drop a ticket, it's useless by tonight. If you lose the membership card, you cancel it once.",
                    "A cinema ticket is good for one showing; the membership card gets you a fresh one each time.")
st_analogy.icon("ticket", 60, 60, 1.6, fill="y")
st_analogy.note(110, 170, "ticket: today, 19:30 only", "green")
st_analogy.icon("keycard", 380, 60, 1.4, fill="green")
st_analogy.note(420, 170, "membership card", "pen")
st_analogy.note(420, 196, "→ fresh ticket each visit", "pen")
st_analogy.note(380, 236, "drop a ticket? useless by tonight", "green")

st_how = Doodle(760, 290, "Short-lived token design. The client holds an access token valid for ten minutes and a refresh token stored securely. When the access token expires, the client sends the refresh token to the auth server, which issues a new access token and a new refresh token and invalidates the old refresh token, called rotation. If an old refresh token is reused, the auth server sees reuse and revokes the whole session.",
                "Access tokens live minutes. Refresh tokens rotate on every use; reusing an old one revokes the session.")
st_how.box(20, 40, 180, 70, "access token", "green", sub="10 minutes")
st_how.box(20, 150, 180, 70, "refresh token", "y", sub="rotates, httpOnly")
st_how.arrow(206, 185, 380, 120, label="expired → refresh", lx=300, ly=196)
st_how.box(386, 70, 180, 90, "auth server", "blue")
st_how.arrow(572, 100, 640, 60, color="green", label="new pair", lx=640, ly=44)
st_how.arrow(572, 140, 640, 200, color="red", label="old token reused?", lx=640, ly=226)
st_how.box(600, 236, 150, 44, "revoke all", "pink", stroke="red", size=16)
st_how.note(380, 280, "workloads: no refresh, just fetch a new 1-hour token", "pen")

SHORT = dict(
    slug="short-lived-tokens",
    kicker="a.k.a. “today's cinema ticket”",
    tldr="Credentials that <b>never expire</b> become a time bomb. Issue <b>access tokens that live minutes</b>, pair them with <b>refresh tokens that rotate</b> on every use (reuse = revoke the session), and give workloads <b>automatically issued credentials</b> instead of static keys. A stolen token is <b>soon useless</b>, and revocation becomes routine.",
    chips=[("Family", "credentials"), ("Typical lifetimes", "access 5–15 min · refresh hours–days"), ("Workloads", "cloud workload identity, OIDC federation"), ("Pairs with", "OAuth + PKCE, secrets management")],
    problem="""  <p class="lead">Long-lived API keys and passwords get copied into laptops, CI, chats and wikis. When one leaks, it works <span class="hl-pink">until someone notices</span>, and rotating it might break systems nobody remembers.</p>
  <ul>
    <li>A key from 2021 still works, and nobody knows every place it's used.</li>
    <li>Sessions stay valid for months after a laptop is stolen.</li>
    <li>CI holds cloud admin keys that never expire.</li>
  </ul>""",
    problem_figs=[st_problem],
    analogy_side="today's cinema ticket",
    analogy="""  <p>A cinema ticket is valid for <b>one showing, today</b>. Drop it on the street and it's <b>useless by tonight</b>. Your <b>membership card</b> gets you a fresh ticket each visit, and if you lose the card, you <b>cancel it once</b>.</p>
  <ul>
    <li>The ticket is an <b>access token</b>.</li>
    <li>The membership card is a <b>refresh token</b>, kept safe.</li>
    <li>A ticket showing up twice is a sign of <b>theft</b>.</li>
  </ul>""",
    analogy_figs=[st_analogy],
    map=[("Ticket for tonight only", "Access token with a 10-minute expiry"),
         ("Membership card", "Refresh token, stored securely"),
         ("Fresh ticket each visit", "Refresh rotation: new pair every use"),
         ("Same ticket used twice", "Refresh-token reuse detection → revoke"),
         ("Staff badge printed each shift", "Workload identity: auto-issued, short-lived credentials")],
    how_side="expire fast, rotate on use",
    how="""  <p>Short lifetimes turn revocation from a crisis into a default: even if you can't find every copy, the copies <b>stop working on their own</b>.</p>""",
    how_figs=[st_how],
    steps=[("Short access tokens", "5–15 minutes; validate expiry on every request."),
           ("Rotating refresh tokens", "Each refresh returns a new refresh token and invalidates the old one."),
           ("Detect reuse", "If an already-used refresh token appears, revoke the whole token family."),
           ("Store them safely", "Browser: httpOnly, Secure, SameSite cookies, not localStorage. Mobile: OS keychain."),
           ("No static keys for workloads", "CI and services get credentials via OIDC federation or cloud workload identity, valid for an hour."),
           ("Make revocation easy", "Sign-out, password change and admin action revoke refresh tokens immediately.")],
    vocab=[("Access token", "Short-lived credential sent with each API call."),
           ("Refresh token", "Longer-lived credential used only to get new access tokens."),
           ("Rotation", "Replacing a credential on every use or on a schedule."),
           ("Reuse detection", "Spotting an old refresh token being used again."),
           ("Workload identity", "Credentials issued automatically to a running service."),
           ("OIDC federation", "Trading a signed identity token (from CI) for cloud credentials.")],
    code=dict(file=".github/workflows/deploy.yml", note="no stored cloud keys", src="""
permissions:
  id-token: write          # CI gets a signed OIDC token for this run
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::123456789012:role/deploy-web
          aws-region: eu-west-1
          role-duration-seconds: 3600      # credentials expire in 1 hour
      - run: ./deploy.sh
# the role trusts only this repo + branch (sub: repo:acme/web:ref:refs/heads/main)
"""),
    tools="tools: identity providers with refresh-token rotation (Auth0, Okta, Keycloak), GitHub/GitLab OIDC to AWS/GCP/Azure, cloud workload identity (IRSA, GKE Workload Identity, Azure managed identity), SPIFFE/SPIRE, HashiCorp Vault dynamic credentials.",
    gains=["<b>Leaks expire on their own</b>.",
           "<b>Theft is detectable</b> via refresh reuse.",
           "<b>No static keys in CI</b> or config.",
           "<b>Revocation is routine</b>, not an emergency."],
    losses=["<b>More token plumbing</b>: refresh logic, storage.",
            "<b>Clock and expiry edge cases</b>.",
            "<b>Dependence on the token issuer</b> being available.",
            "<b>Revoking access tokens</b> mid-life still needs extra work."],
    baseline="Each line compares <b>long-lived API keys and sessions</b> to <b>short access tokens, rotating refresh tokens and workload identity</b>.",
    ratings=[(4, 3, "Refresh and rotation logic to get right."),
             (3, 4, "Silent refresh; users rarely notice."),
             (2, 4, "Stolen tokens stop working within minutes."),
             (3, 4, "Reuse detection reveals stolen refresh tokens."),
             (3, 3, "Issuer must be up for refreshes."),
             (1, 5, "A leak is bounded in time."),
             (2, 4, "Each token issue and refresh is logged."),
             (3, 3, "Mostly configuration; some engineering."),
             (2, 4, "No more key copying and manual rotation.")],
    pitfalls=[("Long access tokens", "“Short-lived” tokens valid for 30 days.", "minutes for access, rotate refresh."),
              ("Tokens in localStorage", "Any XSS can read and exfiltrate them.", "httpOnly secure cookies or a backend-for-frontend."),
              ("Static keys in CI", "Cloud admin keys stored as CI secrets forever.", "OIDC federation with short role sessions."),
              ("No reuse detection", "A stolen refresh token keeps working alongside the real one.", "rotate and revoke the family on reuse.")],
    use=["User sessions in web and mobile apps.",
         "API access by third parties.",
         "CI/CD and services calling cloud APIs."],
    skip=["Truly offline devices that can't refresh (use other controls).",
          "Legacy systems that only accept static keys (wrap them in a vault with rotation)."],
    related=["<b>OAuth 2.0 with PKCE</b>", "<b>Secrets management</b>", "<b>Least privilege</b>", "<b>Zero trust</b>"],
    quiz=[("Why keep access tokens short-lived?", "So a stolen one stops working within minutes, without needing to find and revoke it."),
          ("What's refresh-token rotation?", "Each refresh returns a new refresh token and invalidates the old one."),
          ("What should happen if an old refresh token is reused?", "Treat it as theft and revoke the whole session (token family)."),
          ("How can CI deploy to the cloud without stored keys?", "With OIDC federation: CI presents a signed identity token and receives short-lived role credentials.")],
    remember="A <span class=\"hl\">ticket</span> for tonight, a <span class=\"hl\">card</span> kept safe, and a fresh ticket <span class=\"hl\">every visit</span>.",
    sources=["RFC 9700, “OAuth 2.0 Security Best Current Practice” (refresh token protection).",
             "Auth0 docs, “Refresh Token Rotation”.",
             "GitHub docs, “About security hardening with OpenID Connect”.",
             "OWASP, “JSON Web Token Cheat Sheet” and “Session Management Cheat Sheet”."],
)

NOTES = [ZERO, LEAST, OAUTH, SHORT]
