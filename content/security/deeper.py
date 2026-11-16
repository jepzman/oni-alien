# Vol. 5 · going deeper (November 2026): a longer chapter inside three key notes.
# Defensive practice only. Merged into the notes by scripts/build_notes.py (load_content).

# ------------------------------------------------------------------ OAuth with PKCE
oa_d1 = Doodle(760, 280, "A backend for frontend keeps tokens out of the browser. The single-page app talks only to its own backend, with an HttpOnly, Secure, SameSite session cookie. The backend runs the authorization code flow with PKCE, stores the access and refresh tokens server side, and adds the access token when it calls the APIs. JavaScript in the page never sees a token, so a cross-site scripting bug can't steal one.",
               "The browser holds a cookie; the tokens stay on the server.")
oa_d1.box(20, 90, 160, 90, "browser app", "y", sub="no tokens in JS", size=18, subsize=14)
oa_d1.arrow(184, 135, 316, 135, both=True, label="session cookie", lx=250, ly=124)
oa_d1.note(250, 166, "HttpOnly · Secure", size=14)
oa_d1.note(250, 186, "SameSite", size=14)
oa_d1.box(320, 80, 160, 110, "BFF", "green", sub="holds the tokens", size=20, subsize=14)
oa_d1.arrow(484, 110, 576, 60)
oa_d1.note(566, 40, "code + PKCE", anchor="end", size=15)
oa_d1.arrow(484, 160, 576, 210)
oa_d1.note(566, 244, "Bearer token", anchor="end", size=15)
oa_d1.box(580, 20, 160, 70, "identity provider", "paper", size=15)
oa_d1.box(580, 180, 160, 70, "APIs", "blue", size=18)
oa_d1.note(380, 270, "an XSS bug can act in the page, but can't take a token home", "pen", size=16)

OAUTH_DEEP = dict(
    side="where tokens live, checking them, signing out",
    intro="The note covers the flow: code, verifier, exchange. After the exchange you hold tokens, and most real problems are about what happens to them next: where they are stored, how an API checks them, and what “sign out” actually ends. This chapter covers the three.",
    parts=[
        ("Where the tokens live", """  <p>For a server-rendered app the answer is simple: tokens stay on the server, and the browser gets a session cookie. For a single-page app there are three options, from safest to riskiest:</p>
  <ul>
    <li><b>A backend for frontend (token handler).</b> A small server next to the app runs the OAuth flow, keeps the tokens, and gives the browser an <code>HttpOnly; Secure; SameSite</code> session cookie. The app calls its own backend, which adds the access token. JavaScript never sees a token. This is what current guidance recommends for browser apps.</li>
    <li><b>Tokens in memory only,</b> with short-lived access tokens and refresh-token rotation. Better than storage, but any script running in the page can still use them.</li>
    <li><b>Tokens in localStorage.</b> Avoid: every script on the page, including a compromised third-party one, can read them and send them elsewhere.</li>
  </ul>
  <p>Native mobile apps use the system browser for sign-in (not an embedded web view), PKCE, and the platform's secure storage (Keychain, Keystore) for the refresh token.</p>""", [oa_d1]),
        ("Checking an access token at the API", """  <p>When an API receives a JWT access token, it must check all of these, every time. Use a maintained library and configure it; don't parse tokens by hand.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Check</th><th scope="col">Why</th></tr></thead><tbody>
    <tr><td><b>Signature</b>, with the provider's published keys (JWKS), choosing the key by <code>kid</code></td><td>Anyone can write a JWT; only the provider can sign one. Cache the keys and refresh them when an unknown <code>kid</code> appears, so key rotation works.</td></tr>
    <tr><td><b>Algorithm</b> from a fixed allow-list (for example RS256 or ES256)</td><td>Never trust the token's own <code>alg</code> header; never accept <code>none</code>.</td></tr>
    <tr><td><b>Issuer</b> (<code>iss</code>) and <b>audience</b> (<code>aud</code>)</td><td>A valid token for another API, or from another tenant's issuer, must not work here.</td></tr>
    <tr><td><b>Expiry</b> (<code>exp</code>, <code>nbf</code>) with a small clock allowance (a minute)</td><td>Short lifetimes are only a defence if they're checked.</td></tr>
    <tr><td><b>Scopes or roles</b> for this endpoint</td><td>Authentication says who; scopes say what this token may do.</td></tr>
  </tbody></table></div>
  <p>Opaque (non-JWT) tokens are checked by asking the provider (token introspection), which also tells you if the token was revoked.</p>""", []),
        ("What signing out really ends", """  <p>“Sign out” can mean three different things, and users expect all of them:</p>
  <ul>
    <li><b>The app's session:</b> delete the session server side and clear the cookie.</li>
    <li><b>The tokens:</b> revoke the refresh token at the provider (the revocation endpoint), so it can't mint new access tokens.</li>
    <li><b>The provider's session:</b> redirect to the provider's logout endpoint, or the next “sign in” succeeds silently without a password.</li>
  </ul>
  <p>One thing you can't end early is a self-contained JWT access token that has already been issued: APIs accept it until it expires. That's the main reason access tokens should live <b>minutes, not hours</b>. For “sign out everywhere” after a stolen laptop, revoke all refresh tokens for the user and, for sensitive APIs, check a short revocation list or use introspection.</p>""", []),
    ],
)

# ------------------------------------------------------------------ Threat modelling
tm_d1 = Doodle(760, 300, "A data-flow diagram for a CSV upload feature, with trust boundaries drawn as dashed lines. The browser uploads to the API across the internet boundary. The API stores the file in object storage and puts a job on a queue. A worker reads the file and writes rows to the database across an internal boundary. Each crossing is numbered so threats can refer to it.",
               "Draw the flows, dash the boundaries, number the crossings. Threats attach to the numbers.")
tm_d1.box(20, 110, 110, 60, "browser", "paper", size=17)
tm_d1.line("M165 20 V270", color="red", dash=True)
tm_d1.note(165, 290, "internet", "red", size=14)
tm_d1.box(200, 110, 110, 60, "API", "y", size=18)
tm_d1.arrow(134, 140, 196, 140)
tm_d1.note(150, 104, "① upload", anchor="middle", size=15)
tm_d1.db(420, 30, "file storage", w=80)
tm_d1.arrow(314, 125, 376, 66)
tm_d1.note(328, 82, "②", size=17)
tm_d1.box(370, 170, 110, 50, "queue", "blue", size=16)
tm_d1.arrow(314, 155, 366, 190)
tm_d1.note(326, 196, "③", size=17)
tm_d1.line("M530 20 V270", color="red", dash=True)
tm_d1.note(530, 290, "internal", "red", size=14)
tm_d1.box(570, 120, 110, 60, "worker", "green", size=17)
tm_d1.arrow(484, 195, 566, 170)
tm_d1.note(506, 216, "④", size=17)
tm_d1.arrow(464, 62, 566, 132, dash=True)
tm_d1.note(560, 84, "⑤ read file", anchor="start", size=15)
tm_d1.db(705, 220, "database", w=60)
tm_d1.arrow(650, 184, 690, 212)
tm_d1.note(650, 218, "⑥", size=17)

tm_d2 = Doodle(760, 280, "A simple three by three rating grid. Likelihood runs from rare to likely, impact from minor to severe. Threats in the top-right cells are fixed before release, the middle band gets a ticket with a date, and the bottom-left can be accepted by the owner in writing. Three example threats from the upload feature are placed on the grid.",
               "Rough is fine: the grid is for ordering the work, not for precision.")
labels_x = ["rare", "possible", "likely"]
labels_y = ["severe", "moderate", "minor"]
fills = [["y", "pink", "pink"], ["green", "y", "pink"], ["green", "green", "y"]]
for r in range(3):
    tm_d2.text(110, 66 + r * 64, labels_y[r], "t-head", anchor="end", size=15)
    for c in range(3):
        tm_d2.box(120 + c * 130, 36 + r * 64, 124, 58, None, fills[r][c])
for c in range(3):
    tm_d2.text(182 + c * 130, 244, labels_x[c], "t-head", size=15)
tm_d2.note(310, 270, "likelihood →", size=15)
tm_d2.note(450, 80, "A", "red", size=22)
tm_d2.note(320, 146, "B", size=22)
tm_d2.note(190, 210, "C", "green", size=22)
tm_d2.text(530, 60, "A · huge file fills the disk", "t", anchor="start", size=15)
tm_d2.text(530, 84, "→ fix before release", "t-s t-red", anchor="start", size=15)
tm_d2.text(530, 124, "B · formula in a cell", "t", anchor="start", size=15)
tm_d2.text(530, 148, "→ ticket, this quarter", "t-s", anchor="start", size=15)
tm_d2.text(530, 188, "C · worker log too chatty", "t", anchor="start", size=15)
tm_d2.text(530, 212, "→ accepted, in writing", "t-s t-green", anchor="start", size=15)

THREAT_MODEL_DEEP = dict(
    side="a worked example, rating threats, fitting it into delivery",
    intro="The note gives the four questions and STRIDE. This chapter works through one real feature from diagram to tickets, shows a quick way to decide which threats to handle first, and covers how to make threat modelling a normal part of delivery instead of a one-off document.",
    parts=[
        ("A worked example: CSV uploads", """  <p>The feature: business customers upload a CSV of products; a worker imports it overnight. Draw the flows and number every place data crosses a trust boundary. Then ask the STRIDE questions at each crossing. A one-hour session produced this list:</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Where · STRIDE</th><th scope="col">Threat → mitigation</th></tr></thead><tbody>
    <tr><td>① · Denial of service</td><td>A 5 GB file fills the disk → size limit at the edge and in the API, streaming upload straight to storage.</td></tr>
    <tr><td>① · Spoofing</td><td>Someone uploads into another tenant's account → the tenant comes from the session, never from a form field.</td></tr>
    <tr><td>② · Information disclosure</td><td>Files readable by other tenants → private bucket, per-tenant prefix, short-lived download links only.</td></tr>
    <tr><td>⑤ · Tampering</td><td>A cell starting with <code>=</code> runs as a formula when staff open an export → escape such cells on export.</td></tr>
    <tr><td>⑥ · Elevation of privilege</td><td>The worker's database role can write every table → a role limited to the products table.</td></tr>
    <tr><td>④ · Repudiation</td><td>A customer says “we never uploaded that” → audit event with user, file hash and time.</td></tr>
  </tbody></table></div>
  <p>Six threats, six tickets, one hour. Most of them are cheap now and expensive after release.</p>""", [tm_d1]),
        ("Deciding what to handle first", """  <p>You will find more threats than you can fix at once. A rough <b>likelihood × impact</b> grid is enough to order them; don't spend the session arguing about decimal scores.</p>
  <ul>
    <li><b>Top right</b> (likely and serious): fix before release.</li>
    <li><b>The middle band:</b> a ticket with an owner and a date.</li>
    <li><b>Bottom left:</b> may be <b>accepted</b>, but only by the person who owns the risk (usually the product or service owner, not the engineer), in writing, with a date to look again.</li>
  </ul>
  <p>Every threat ends in one of four decisions: <b>mitigate</b> (build a control), <b>avoid</b> (drop the risky part of the feature), <b>transfer</b> (a provider or insurer carries it) or <b>accept</b>. What's left after the mitigation is the residual risk; write it down too, so the next review starts from facts.</p>""", [tm_d2]),
        ("Making it part of delivery", """  <p>Threat models fail when they are a document written once. They work when they are small, frequent and tied to the work:</p>
  <ul>
    <li><b>Clear triggers.</b> Hold a session when a change adds a new external input, a new data store, a new third party, a change to sign-in or permissions, or a new trust boundary. Put these questions in the design-doc or pull-request template.</li>
    <li><b>Delta sessions.</b> For a change to an existing feature, update the existing diagram in 30 minutes instead of starting over.</li>
    <li><b>The whole team in the room:</b> the people who built it know where the shortcuts are.</li>
    <li><b>Mitigations become tests.</b> “Upload over 50 MB is rejected”, “tenant A can't read tenant B's file”: abuse cases in the test suite, so the control can't silently disappear.</li>
    <li><b>Keep it in the repo</b> (<code>docs/threat-model/</code>), reviewed like code, so it changes when the code changes.</li>
  </ul>""", []),
    ],
)

# ------------------------------------------------------------------ Supply chain
sc_d1 = Doodle(760, 300, "Triage of a new vulnerability advisory. First: is the package in our software bill of materials? If not, nothing to do. If it is: is the vulnerable code reachable from our use, and is the service exposed? If yes and a fixed version exists, upgrade within the deadline for that severity. If no fix exists, add a mitigation such as a WAF rule or a config change. If not reachable, record the decision with a re-check date.",
               "Four questions turn a scary advisory into one of four actions.")
sc_d1.box(20, 20, 160, 64, "in our SBOM?", "y", size=17)
sc_d1.arrow(100, 88, 100, 126, label="no", lx=108, ly=112, anchor="start")
sc_d1.box(20, 130, 160, 50, "nothing to do", "green", size=15)
sc_d1.arrow(184, 52, 226, 52, label="yes", lx=205, ly=42)
sc_d1.box(230, 20, 230, 64, "reachable + exposed?", "y", size=17)
sc_d1.arrow(345, 88, 345, 196, label="no", lx=353, ly=146, anchor="start")
sc_d1.box(250, 200, 190, 70, "record it", "paper", sub="re-check date", size=16, subsize=13)
sc_d1.arrow(464, 52, 496, 52, label="yes", lx=480, ly=42)
sc_d1.box(500, 20, 240, 64, "fixed version?", "y", size=17)
sc_d1.arrow(580, 88, 580, 120, label="yes", lx=588, ly=108, anchor="start")
sc_d1.box(480, 124, 210, 56, "upgrade by deadline", "green", size=15)
sc_d1.arrow(718, 88, 718, 206, color="red", label="no", lx=712, ly=150, anchor="end")
sc_d1.box(480, 210, 260, 60, "mitigate meanwhile", "pink", stroke="red", sub="config, WAF rule, disable", size=15, subsize=13)

sc_d2 = Doodle(760, 220, "The chain from source to cluster. A commit is built by CI in an isolated runner with pinned tools. CI produces the image, an SBOM and a provenance statement, signs them, and pushes them to the registry. At deploy, the cluster's admission policy checks the signature and the provenance and refuses anything that wasn't built by the expected pipeline from the expected repository.",
               "Each step leaves evidence the next one checks.")
sc_d2.row([("commit", "reviewed, main", "paper"), ("CI build", "isolated, pinned", "y"), ("signed", "SBOM + provenance", "blue"),
           ("registry", "image + proofs", "paper"), ("admission", "verify or refuse", "green")], x=10, y=40, h=84, gap=34, size=16, subsize=11, arrows=True)
sc_d2.note(380, 178, "a stolen registry password can push an image, but not a valid signature from your CI", "pen", size=16)

SUPPLY_CHAIN_DEEP = dict(
    side="choosing packages, handling advisories, build to cluster",
    intro="The note lists the controls: lockfiles, updates, scanning, SBOMs, signing. This chapter is about the decisions in between: whether to add a dependency in the first place, what to do in the first hour after a vulnerability advisory, and how the build evidence is checked all the way to the cluster.",
    parts=[
        ("Before you add a dependency", """  <p>Every package you add brings its own dependencies and its maintainers' habits. Two minutes of checking before <code>npm install</code> is cheaper than removing it later.</p>
  <div class="table-scroll"><table class="map"><thead><tr><th scope="col">Look at</th><th scope="col">Warning sign</th></tr></thead><tbody>
    <tr><td>What it pulls in (<code>npm ls</code>, the lockfile diff)</td><td>A small helper that brings 80 transitive packages.</td></tr>
    <tr><td>Maintainers and activity</td><td>One maintainer, no release in two years, issues unanswered.</td></tr>
    <tr><td>Install scripts (<code>preinstall</code>, <code>postinstall</code>)</td><td>Scripts that download or run code at install time.</td></tr>
    <tr><td>The name</td><td>One letter off a popular package (typosquatting), or very new with few users.</td></tr>
    <tr><td>Security practice (OpenSSF Scorecard)</td><td>No branch protection, no signed releases, no security policy.</td></tr>
    <tr><td>Licence</td><td>A licence your company can't ship.</td></tr>
  </tbody></table></div>
  <p>And ask the plain question: is ten lines of our own code better than this package? For small utilities, often yes.</p>""", []),
        ("The first hour after an advisory", """  <p>A critical advisory lands for a library you have heard of. Panic-upgrading everything is risky; ignoring it is worse. Work through four questions:</p>
  <ol>
    <li><b>Do we have it?</b> Search the SBOMs of every deployed service, not just the main repository. This is what SBOMs are for: the answer takes minutes, not days.</li>
    <li><b>Can it be reached?</b> Is the vulnerable function used, and is that service exposed to the input the attack needs? Reachability tools help; a quick code search often does too.</li>
    <li><b>Is there a fix?</b> Upgrade through the normal pipeline, with tests, within the deadline your policy sets for that severity (for example 2 days for critical and internet-facing, 30 days for medium).</li>
    <li><b>If not, mitigate:</b> turn off the feature, add a WAF rule, change the config the advisory names, and track the real fix.</li>
  </ol>
  <p>Write down “not affected, because …” decisions with a date to check again: reachability changes when code changes.</p>""", [sc_d1]),
        ("From build to cluster", """  <p>Signing is only useful if something checks the signature. The chain looks like this:</p>
  <ul>
    <li><b>The build</b> runs in CI on a fresh, isolated runner, from a reviewed commit on a protected branch, with pinned tools and actions. No one builds release images on a laptop.</li>
    <li><b>CI produces evidence</b>: the image, an SBOM, and a <b>provenance</b> statement (which repository, which commit, which workflow built it), and signs them with a short-lived identity (Sigstore keyless signing), so there is no long-lived signing key to steal.</li>
    <li><b>The cluster checks it.</b> An admission policy (Kyverno, Gatekeeper or the platform's own) refuses images that aren't signed by your CI identity or whose provenance names another repository.</li>
  </ul>
  <p>SLSA describes these steps as levels. You don't need the top level on day one; a protected branch, a CI-only build, signed images and an admission check already stop the most common attacks: a stolen registry password and a tampered build machine.</p>""", [sc_d2]),
    ],
)

REVISIONS = {
    "oauth-pkce": dict(deep_dive=OAUTH_DEEP),
    "threat-modeling": dict(deep_dive=THREAT_MODEL_DEEP),
    "supply-chain": dict(deep_dive=SUPPLY_CHAIN_DEEP),
}
