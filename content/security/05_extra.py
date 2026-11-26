# Vol. 5 · extra notes (November 2026): Passkeys, Signed Webhooks, Rate-Limited Login.
# Numbered 16–18 so earlier note URLs and PDF names stay the same. Defensive practice only.

# ------------------------------------------------------------------ 16 Passkeys
pk_problem = Doodle(760, 250, "Doodle of a phished password and code. A user gets an email that looks like it's from the shop and signs in on a look-alike site. They type their password and the six-digit code from their phone. The fake site passes both to the real one within seconds and takes over the account.",
                    "Password plus code, typed into the wrong site, works just as well for the attacker.")
pk_problem.box(20, 80, 150, 80, "user", "y", sub="password + code", size=18, subsize=13)
pk_problem.arrow(174, 120, 276, 120, color="red")
pk_problem.box(280, 70, 200, 100, "shop-1ogin.com", "pink", stroke="red", sub="looks just like the shop", size=17, subsize=13)
pk_problem.arrow(484, 120, 586, 120, color="red", label="replayed in seconds", lx=545, ly=192)
pk_problem.box(590, 80, 150, 80, "real shop", "blue", sub="account taken", size=17, subsize=13)
pk_problem.note(380, 222, "the code was real; it was just typed into the wrong place", "red", size=16)

pk_analogy = Doodle(760, 250, "Doodle of a key cut for one lock. Your house key only turns your own front door. If someone builds a fake door that looks like yours, the key simply doesn't fit, so there is nothing to steal by tricking you into using it there. And the key never leaves your keyring to be copied.",
                    "A key cut for one door: a fake door can't use it.")
pk_analogy.icon("key", 40, 70, 1.6, fill="y")
pk_analogy.box(220, 40, 220, 70, "your front door", "green", sub="key turns ✓", size=17, subsize=13)
pk_analogy.box(220, 140, 220, 70, "fake look-alike door", "pink", stroke="red", sub="key doesn't fit", size=17, subsize=13)
pk_analogy.note(600, 100, "the key never leaves", size=16)
pk_analogy.note(600, 126, "your keyring", size=16)

pk_how = Doodle(760, 290, "How passkey sign-in works. The site sends a random challenge. The browser checks the site's domain and asks the user's device for the passkey for that domain. The user unlocks it with a fingerprint, face or PIN. The device signs the challenge with the private key, which never leaves it. The site checks the signature with the public key it stored at registration.",
                "The site sends a challenge; the device signs it, only for the right domain; the private key never leaves.")
pk_how.box(20, 40, 170, 70, "site", "blue", sub="shop.example", size=18, subsize=13)
pk_how.box(570, 40, 170, 70, "user's device", "green", sub="private key, locked", size=18, subsize=13)
pk_how.arrow(194, 62, 566, 62, label="① challenge (random)", lx=380, ly=52)
pk_how.box(300, 120, 160, 60, "② unlock", "y", sub="face · finger · PIN", size=16, subsize=13)
pk_how.arrow(566, 98, 194, 98, color="green", label="③ signature, for shop.example only", lx=380, ly=92)
pk_how.box(20, 200, 400, 60, "④ check with the stored public key", "paper", size=15)
pk_how.note(590, 222, "nothing secret is stored at the site", "pen", size=15)
pk_how.note(590, 248, "a look-alike domain gets no signature", "pen", size=15)

PASSKEYS = dict(
    slug="passkeys",
    kicker="a.k.a. “no password to steal”",
    tldr="A <b>passkey</b> replaces the password with a <b>key pair</b>: the private key stays on the user's device (or their password manager, synced between devices), the site stores only the <b>public key</b>. To sign in, the site sends a challenge, the user unlocks the device with a fingerprint, face or PIN, and the device signs it, <b>only for the real domain</b>. Nothing reusable crosses the network, so passkeys resist phishing, password reuse and database leaks. Built on WebAuthn / FIDO2.",
    chips=[("Family", "identity"), ("Standard", "WebAuthn (W3C) + FIDO2 (FIDO Alliance)"), ("Stops", "phishing, credential stuffing, leaked password hashes"), ("Pairs with", "short-lived tokens, rate-limited login, OAuth with PKCE")],
    problem="""  <p class="lead">A customer gets a convincing email, signs in on <code>shop-1ogin.com</code>, and types their password and the six-digit code from their phone. <span class="hl-pink">The fake site replays both to the real one within seconds</span> and takes over the account. The code was real; it was just typed into the wrong place.</p>
  <ul>
    <li>Passwords are <b>reused</b>, guessed and leaked in other sites' breaches.</li>
    <li>One-time codes by SMS or app stop guessing, but <b>not phishing</b>: a person can type them anywhere.</li>
    <li>Password resets and support calls are a large, ongoing cost.</li>
  </ul>""",
    problem_figs=[pk_problem],
    analogy_side="a key cut for one door",
    analogy="""  <p>Your house key turns <b>your</b> front door. If someone builds a fake door that looks exactly like yours, the key simply <b>doesn't fit</b>, so there's nothing to steal by tricking you into trying it. And the key <b>never leaves your keyring</b>: the door checks it, it doesn't keep a copy.</p>""",
    analogy_figs=[pk_analogy],
    map=[("Your key", "The private key, kept on the device or in a synced password manager"),
         ("The lock it's cut for", "The site's domain (relying party id)"),
         ("A fake look-alike door", "A phishing site on another domain: no matching passkey"),
         ("The door checking the key", "The site verifying a signature with the stored public key"),
         ("Unlocking the keyring", "Fingerprint, face or device PIN (user verification)")],
    how_side="a challenge, signed on the device",
    how="""  <p>At registration the device creates a key pair for this site and gives the site the <b>public key</b>. At sign-in the site sends a random <b>challenge</b>; the browser only offers passkeys for the site's own domain; the device asks the user to unlock and <b>signs</b> the challenge; the site checks the signature. The biometric never leaves the device, and the site holds nothing an attacker could reuse.</p>""",
    how_figs=[pk_how],
    steps=[("Use a maintained library", "SimpleWebAuthn, webauthn4j, py_webauthn or your identity provider; don't implement WebAuthn by hand."),
           ("Offer it where people already are", "“Create a passkey” after a successful sign-in, and in account settings. Keep the old method for now."),
           ("Use autofill", "<code>autocomplete=\"username webauthn\"</code> lets the browser offer passkeys right in the sign-in field."),
           ("Store per credential", "Public key, credential id, sign counter, a name and last-used date; let users see and remove them."),
           ("Plan recovery", "A second passkey, a recovery process with real checks, or a synced passkey provider. Recovery is the new weak spot.")],
    vocab=[("Passkey", "A FIDO credential (key pair) used instead of a password."),
           ("WebAuthn", "The browser API for creating and using passkeys."),
           ("Relying party", "The site the passkey is for, identified by its domain."),
           ("Challenge", "A random value the device signs to prove it holds the key."),
           ("Synced passkey", "A passkey backed up across a user's devices by their platform or password manager."),
           ("User verification", "The device checking it's really the user: biometric or PIN.")],
    code=dict(file="passkeys.ts", note="SimpleWebAuthn, server side", src="""
import { generateAuthenticationOptions, verifyAuthenticationResponse } from "@simplewebauthn/server";

const rpID = "shop.example";                    // passkeys only work for this domain

app.post("/passkeys/login/options", async (req, res) => {
  const options = await generateAuthenticationOptions({ rpID, userVerification: "preferred" });
  req.session.challenge = options.challenge;    // remember it: it may be used once
  res.json(options);                            // the browser calls navigator.credentials.get()
});

app.post("/passkeys/login/verify", async (req, res) => {
  const cred = await db.passkeys.findById(req.body.id);
  const result = await verifyAuthenticationResponse({
    response: req.body,
    expectedChallenge: req.session.challenge,
    expectedOrigin: "https://shop.example",
    expectedRPID: rpID,
    credential: { id: cred.id, publicKey: cred.publicKey, counter: cred.counter },
  });
  delete req.session.challenge;
  if (!result.verified) return res.status(401).end();
  await db.passkeys.touch(cred.id, result.authenticationInfo.newCounter);
  await startSession(res, cred.userId);
  res.status(204).end();
});
"""),
    tools="tools: SimpleWebAuthn (JS), py_webauthn, webauthn4j / java-webauthn-server, go-webauthn, Auth0 / Okta / Entra ID / Cognito passkey support, passkeys.dev for guides and device support.",
    gains=["<b>Phishing-resistant</b>: a look-alike site gets nothing usable.",
           "<b>Nothing to leak</b>: the site stores public keys only.",
           "<b>Faster sign-in</b>: a fingerprint instead of typing.",
           "<b>Fewer resets</b> and less support work."],
    losses=["<b>Recovery</b> when every device is lost needs careful design.",
            "<b>Mixed support</b> on older devices and in some enterprise setups.",
            "<b>Two methods for a while</b>: passwords stay during the transition.",
            "<b>New UX to explain</b> to users."],
    baseline="Each line compares <b>password plus one-time code</b> to <b>passkeys, with passwords kept as a fallback for now</b>.",
    ratings=[(3, 3, "A library does the cryptography; recovery is the hard part."),
             (2, 5, "Unlock with a fingerprint; nothing to remember."),
             (2, 5, "No shared secret to steal from the site."),
             (3, 5, "Signatures bound to the real domain."),
             (3, 4, "Less credential stuffing load."),
             (2, 5, "One site's breach exposes nothing reusable."),
             (3, 4, "Each credential has an id, a name and a last-used date."),
             (3, 3, "Fewer resets, some build work."),
             (3, 4, "Good libraries and identity providers.")],
    pitfalls=[("Recovery by email link only", "Passkeys are strong, but anyone with the user's email can reset them away.", "make recovery as strong as sign-in: a second passkey, identity checks, a waiting period with notifications."),
              ("Hiding the button", "Passkeys live on a settings page no one visits.", "offer to create one right after a successful sign-in, and use autofill."),
              ("Not binding to the domain", "Hand-rolled verification skips the origin or rpID check.", "use a library and always check origin, rpID and the challenge."),
              ("Reusing challenges", "The same challenge works twice.", "one random challenge per attempt, stored server side, deleted after use.")],
    use=["Consumer and staff sign-in on the web and mobile.",
         "Accounts worth phishing: money, data, admin rights.",
         "Replacing SMS codes as a second factor."],
    skip=["Machine-to-machine access (use workload identity and short-lived tokens).",
          "Shared kiosks with no personal device.",
          "You can't yet offer a sound recovery process; build that first."],
    related=["<b>Short-lived tokens</b>", "<b>Rate-limited login</b>", "<b>OAuth 2.0 with PKCE</b>", "<b>Password hashing</b>"],
    quiz=[("Why can't a phishing site use a passkey?", "The browser only offers and signs for passkeys registered to the real site's domain; a look-alike domain gets no signature."),
          ("What does the site store for a passkey?", "The public key, the credential id and a counter: nothing an attacker could use to sign in."),
          ("Does the fingerprint or face scan go to the site?", "No. It only unlocks the private key on the device."),
          ("What becomes the weak point once passkeys are used?", "Account recovery: if it's just an email link, attackers go after that instead.")],
    quiz_sit=[("Your bank app adds passkeys, but keeps “forgot password? we'll email you a link” as the only recovery, which also removes all passkeys. An attacker who has the user's email can now take over the account. What do you change?",
               "Make recovery at least as strong as sign-in: encourage a second passkey, require stronger identity checks for recovery, add a waiting period with notifications to every registered device, and don't let recovery silently delete existing passkeys.")],
    try_it="Clone a SimpleWebAuthn example (or your identity provider's passkey sample), run it on localhost, and register a passkey with your laptop or phone. Then change the expected rpID or origin in the server code and see the sign-in fail. Look in the database at what was stored for the credential: a public key, not a secret.",
    remember="A key cut for <span class=\"hl\">one door</span>, that never leaves <span class=\"hl\">your pocket</span>.",
    sources=["W3C, “Web Authentication: An API for accessing Public Key Credentials, Level 3”.",
             "FIDO Alliance, passkeys.dev and the FIDO2 specifications.",
             "NIST SP 800-63B, “Digital Identity Guidelines: Authentication and Lifecycle Management”.",
             "SimpleWebAuthn documentation."],
)

# ------------------------------------------------------------------ 17 Signed webhooks
sw_problem = Doodle(760, 250, "Doodle of an unauthenticated webhook. The shop's endpoint accepts any POST that looks like a payment provider notice saying an order was paid. Someone who finds the URL sends their own payment succeeded message for order 812, and the order is shipped without any payment.",
                    "Anyone who finds the URL can say “order 812 is paid”.")
sw_problem.box(20, 30, 190, 70, "payment provider", "blue", sub="real notices", size=16, subsize=13)
sw_problem.box(20, 150, 190, 70, "anyone", "pink", stroke="red", sub="found the URL", size=16, subsize=13)
sw_problem.arrow(214, 65, 366, 110)
sw_problem.arrow(214, 185, 366, 140, color="red", label="“order 812 paid”", lx=300, ly=196)
sw_problem.box(370, 90, 170, 70, "/webhooks/pay", "y", sub="trusts every POST", size=16, subsize=13)
sw_problem.arrow(544, 125, 596, 125, color="red")
sw_problem.box(600, 90, 140, 70, "shipped", "pink", stroke="red", sub="never paid", size=16, subsize=13)

sw_analogy = Doodle(760, 250, "Doodle of a sealed letter. A notary's letter carries a wax seal pressed with a stamp only the notary has, and the date. The receiver checks that the seal is intact and matches, and that the date is recent. A forged letter has no matching seal; an old letter sent again is refused because of its date.",
                    "A wax seal only the sender can make, and a date so old letters can't be sent again.")
sw_analogy.icon("envelope", 40, 70, 1.6, fill="y")
sw_analogy.icon("seal", 120, 120, 1.0)
sw_analogy.box(260, 40, 230, 70, "seal matches?", "green", sub="only the sender has the stamp", size=17, subsize=13)
sw_analogy.box(260, 140, 230, 70, "dated today?", "green", sub="old letters refused", size=17, subsize=13)
sw_analogy.note(620, 110, "both yes → open it", "green", size=16)
sw_analogy.note(620, 140, "otherwise → bin", "red", size=16)

sw_how = Doodle(760, 280, "Verifying a signed webhook. The sender computes an HMAC with a shared secret over the timestamp and the exact raw body, and sends it in a header. The receiver reads the raw body before any JSON parsing, recomputes the HMAC, compares it in constant time, rejects timestamps older than five minutes, and skips event ids it has already handled.",
                "Raw body + timestamp → HMAC with the shared secret → constant-time compare → fresh? new event id?")
sw_how.row([("raw body", "exact bytes", "paper"), ("HMAC", "secret + time", "y"), ("compare", "constant time", "blue"), ("fresh?", "≤ 5 min old", "green"), ("new id?", "not seen before", "green")],
           x=10, y=50, h=80, gap=34, size=16, subsize=12, arrows=True)
sw_how.note(380, 176, "any check fails → 400 or 401, and nothing is processed", "red", size=16)
sw_how.note(380, 208, "all pass → 2xx quickly, do the work in the background", "green", size=16)

SIGNED_WEBHOOKS = dict(
    slug="signed-webhooks",
    kicker="a.k.a. “prove it came from them, and that it's new”",
    tldr="A webhook endpoint is a public URL that changes things (“order paid”, “subscription cancelled”). Anyone who finds it can call it. <b>Verify every request</b>: the sender signs the <b>exact raw body plus a timestamp</b> with a shared secret (HMAC), you recompute and compare in <b>constant time</b>, reject <b>old timestamps</b> to stop replays, and ignore <b>event ids you've already handled</b>. Then answer quickly and process in the background.",
    chips=[("Family", "untrusted input"), ("Mechanism", "HMAC-SHA256 over timestamp + raw body"), ("Standard", "Standard Webhooks spec; Stripe, GitHub, Slack all sign"), ("Pairs with", "idempotent consumer, validate at the boundary, secrets management")],
    problem="""  <p class="lead">A shop's <code>/webhooks/payment</code> endpoint ships an order whenever it receives a JSON body saying “paid”. Someone who finds the URL (in a log, a browser extension, a guess) <span class="hl-pink">sends their own “order 812 paid”</span>, and the order ships without payment.</p>
  <ul>
    <li>Webhook URLs are <b>public</b> by nature; obscurity is not protection.</li>
    <li>A captured real notice can be <b>sent again</b> later (replay).</li>
    <li>Providers retry deliveries, so the same event can legitimately arrive <b>twice</b>.</li>
  </ul>""",
    problem_figs=[sw_problem],
    analogy_side="a sealed, dated letter",
    analogy="""  <p>A notary's letter carries a <b>wax seal</b> pressed with a stamp only the notary has, and a <b>date</b>. You open it only if the seal is intact and matches, and the date is recent. A forged letter has no matching seal; an old genuine letter posted again is refused because of its date.</p>""",
    analogy_figs=[sw_analogy],
    map=[("The notary's stamp", "The shared webhook signing secret"),
         ("The wax seal", "The HMAC signature header"),
         ("An intact seal over the whole letter", "Signature over the exact raw body"),
         ("The date on the letter", "The signed timestamp; reject if older than ~5 minutes"),
         ("A letter you've already filed", "An event id already processed: ignore it")],
    how_side="five checks before you trust it",
    how="""  <p>The sender computes <code>HMAC-SHA256(secret, timestamp + "." + raw_body)</code> and sends it in a header with the timestamp. You recompute it over the bytes you received, before parsing (re-serialised JSON won't match), and compare with a <b>constant-time</b> function. Check the timestamp is recent and the event id is new, then return 2xx quickly and queue the work.</p>""",
    how_figs=[sw_how],
    steps=[("Keep the raw body", "Configure the route to give you the bytes (express.raw, request.get_data()) before any JSON parsing."),
           ("Recompute and compare", "HMAC-SHA256 with the endpoint's secret over the exact signed string; compare with a timing-safe function."),
           ("Reject stale timestamps", "Older than ~5 minutes (or in the future): refuse, so captured requests can't be replayed later."),
           ("Deduplicate by event id", "Store processed ids with a unique constraint; a retry of the same event is a no-op."),
           ("Answer fast, work later", "Return 2xx within a second or two and process from a queue, or the sender retries and duplicates pile up.")],
    vocab=[("Webhook", "An HTTP call a provider makes to your URL when something happens."),
           ("HMAC", "A keyed hash: only holders of the secret can produce the right value."),
           ("Constant-time compare", "Comparing without leaking how many characters matched."),
           ("Replay", "Sending a captured, genuine request again later."),
           ("Event id", "A unique id per event, used to drop duplicates."),
           ("Secret rotation", "Switching to a new signing secret while accepting both for a while.")],
    code=dict(file="webhooks.ts", note="Node.js + Express", src="""
import crypto from "node:crypto";

app.post("/webhooks/payment", express.raw({ type: "application/json" }), async (req, res) => {
  const ts = req.header("webhook-timestamp") ?? "";
  const sig = req.header("webhook-signature") ?? "";
  const age = Math.abs(Date.now() / 1000 - Number(ts));
  if (!ts || age > 300) return res.status(400).send("stale or missing timestamp");

  const expected = crypto.createHmac("sha256", process.env.WEBHOOK_SECRET!)
    .update(`${ts}.`).update(req.body)                 // the exact raw bytes
    .digest("base64");
  const ok = sig.length === expected.length &&
             crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expected));
  if (!ok) return res.status(401).send("bad signature");

  const event = JSON.parse(req.body.toString("utf8"));
  const isNew = await db.webhookEvents.insertIfAbsent(event.id);   // unique on id
  if (isNew) await queue.publish("payment-events", event);          // work happens later
  res.status(204).end();
});
"""),
    tools="tools: Standard Webhooks libraries (standardwebhooks.com), Stripe <code>constructEvent</code>, GitHub <code>X-Hub-Signature-256</code>, Svix (sending and verifying), smee.io / ngrok for local testing, secrets managers for the signing secrets.",
    gains=["<b>Only the real sender</b> can trigger the endpoint.",
           "<b>Replays are refused</b> by the timestamp check.",
           "<b>Duplicates are harmless</b> with event ids.",
           "<b>Cheap</b>: a hash per request."],
    losses=["<b>A secret to manage</b> and rotate per endpoint.",
            "<b>Raw body handling</b> trips up frameworks that parse JSON first.",
            "<b>Clock skew</b> can reject genuine requests if servers drift.",
            "<b>Every provider differs</b> in header names and formats."],
    baseline="Each line compares <b>a webhook endpoint that trusts any POST</b> to <b>one that verifies signature, timestamp and event id</b>.",
    ratings=[(4, 3, "Five checks, best done by a library."),
             (4, 4, "Invisible to users."),
             (3, 4, "The body can't be read or forged in transit (with HTTPS) or forged at all."),
             (1, 5, "Forged and altered requests are rejected."),
             (3, 4, "Junk is rejected cheaply; work is queued."),
             (2, 4, "A leaked URL alone is useless."),
             (2, 4, "Rejected deliveries can be logged with reasons."),
             (4, 4, "Neutral."),
             (3, 3, "Raw-body setup surprises people once.")],
    pitfalls=[("Verifying parsed JSON", "The framework parsed and re-serialised the body; the signature never matches, so someone disables the check.", "verify the raw bytes before parsing."),
              ("Plain string compare", "<code>sig === expected</code> leaks timing information.", "use a constant-time comparison."),
              ("No timestamp check", "A captured genuine notice can be sent again weeks later.", "sign the timestamp and reject anything older than a few minutes."),
              ("Slow handler", "The endpoint does all the work before answering; the provider times out and retries, and orders ship twice.", "answer 2xx fast, queue the work, and deduplicate by event id.")],
    use=["Every incoming webhook that changes state: payments, subscriptions, deployments.",
         "Sending webhooks to customers: sign them the same way.",
         "Internal callbacks between systems over the internet."],
    skip=["The sender can't sign: then allow-list its IPs and use mutual TLS, and treat the payload as a hint to fetch the real state.",
          "Read-only notifications with no effect (still cheap to verify, though).",
          "Calls inside a private network already authenticated by mTLS."],
    related=["<b>Idempotent consumer</b> (Vol. 1)", "<b>Validate at the boundary</b>", "<b>Secrets management</b>", "<b>Audit logging</b>"],
    quiz=[("Why must the signature be checked over the raw body?", "The signature covers exact bytes; parsing and re-serialising JSON changes spacing or order, so the check would fail or be skipped."),
          ("What does the timestamp check prevent?", "Replays: a captured genuine request sent again later is rejected as too old."),
          ("Why compare signatures in constant time?", "A normal comparison can leak, through timing, how much of a guessed signature was right."),
          ("Why store event ids?", "Providers retry deliveries; the id lets you process each event only once.")],
    quiz_sit=[("Your endpoint verifies signatures correctly, but customers are sometimes charged twice for one order. The provider's dashboard shows many retries after timeouts on your endpoint. What do you change?",
               "Answer 2xx as soon as the request is verified and recorded, and do the work from a queue; and deduplicate by the event id with a unique constraint, so a retried delivery is ignored. Make the charge-side action idempotent too.")],
    try_it="Add signature checking to one webhook endpoint (or write a toy one). Send it a request with the right signature, one with a changed body, one with a timestamp from an hour ago, and the same valid request twice. Check that only the first valid request is processed, and that each rejection is logged with its reason.",
    remember="Check the <span class=\"hl\">seal</span>, check the <span class=\"hl\">date</span>, and never open the same letter twice.",
    sources=["Standard Webhooks specification (standardwebhooks.com).",
             "Stripe documentation, “Check the webhook signatures”.",
             "GitHub documentation, “Validating webhook deliveries”.",
             "RFC 2104, “HMAC: Keyed-Hashing for Message Authentication”."],
)

# ------------------------------------------------------------------ 18 Rate-limited login
rl_problem = Doodle(760, 250, "Doodle of credential stuffing. Attackers take 2 million email and password pairs leaked from other sites and try them on the shop's login, spread over thousands of IP addresses at a few attempts each. About one in 200 works because people reuse passwords: thousands of accounts are taken over without any single IP looking suspicious.",
                    "Leaked passwords from other sites, tried here from thousands of IPs: 0.5% get in.")
rl_problem.box(14, 50, 220, 80, "2 million leaked pairs", "pink", stroke="red", sub="from other sites", size=15, subsize=13)
for i in range(5):
    rl_problem.arrow(238, 90, 366, 30 + i * 30, dash=True, color="red")
rl_problem.box(370, 20, 160, 140, "login", "y", sub="no limits", size=19, subsize=14)
rl_problem.arrow(534, 90, 596, 90, color="red")
rl_problem.box(600, 50, 140, 80, "≈ 10,000", "pink", stroke="red", sub="accounts taken", size=18, subsize=13)
rl_problem.note(380, 214, "5,000 IPs × a few tries each: no single IP looks odd", "red", size=16)

rl_analogy = Doodle(760, 250, "Doodle of a bank card at a cash machine. Three wrong PINs and the machine keeps the card. Separately, the bank watches for many cards failing at the same machine, and for one machine trying many cards: each pattern triggers its own response.",
                    "Three wrong PINs and the card is kept. The bank also watches the machine, not just the card.")
rl_analogy.icon("keycard", 40, 70, 1.6, fill="y")
rl_analogy.box(230, 30, 240, 60, "per card", "green", sub="3 wrong PINs → kept", size=17, subsize=13)
rl_analogy.box(230, 110, 240, 60, "per machine", "blue", sub="many cards failing → alarm", size=17, subsize=13)
rl_analogy.box(230, 190, 240, 50, "whole network", "paper", sub="unusual spike → review", size=16, subsize=12)
rl_analogy.note(620, 140, "three different patterns,", size=16)
rl_analogy.note(620, 166, "three different limits", size=16)

rl_how = Doodle(760, 280, "Layered limits on login. Per account: after 5 failures, add delays and a challenge, never a permanent lock. Per IP and per network: cap attempts, with higher limits for known shared networks. Globally: watch the overall failure rate and switch on extra checks during an attack. Also check passwords against known breached lists and offer passkeys.",
                "Limits per account, per source, and overall, because attacks spread across all three.")
rl_how.row([("per account", "5 fails → slow + challenge", "green"), ("per IP / network", "cap, shared nets higher", "blue"), ("whole site", "failure rate spike → step up", "y")],
           x=20, y=40, h=90, gap=30, size=17, subsize=13)
rl_how.note(380, 176, "same answer for “wrong password” and “no such user”", "pen", size=16)
rl_how.note(380, 206, "block breached passwords · offer passkeys · alert the user on new sign-ins", "pen", size=15)
rl_how.note(380, 244, "no permanent lockout: attackers could lock out anyone", "red", size=15)

LOGIN_THROTTLING = dict(
    slug="login-throttling",
    kicker="a.k.a. “slow the guessers, not the users”",
    tldr="Login is attacked by <b>guessing</b> (one account, many passwords) and <b>credential stuffing</b> (many accounts, passwords leaked elsewhere, from thousands of IPs). One limit can't stop both. Layer them: <b>per account</b> (growing delays and a challenge after a few failures, never a permanent lock), <b>per IP and network</b>, and <b>site-wide</b> (step up checks when the failure rate spikes). Add breached-password checks, identical error messages, new-sign-in alerts, and passkeys.",
    chips=[("Family", "identity"), ("Stops", "password guessing, credential stuffing"), ("Builds on", "rate limiter (Vol. 1)"), ("Pairs with", "passkeys, password hashing, audit logging")],
    problem="""  <p class="lead">Attackers take <b>2 million</b> email/password pairs leaked from other sites and try them on the shop's login, spread over <b>5,000 IP addresses</b> at a few attempts each. About 0.5% work, because people reuse passwords: <span class="hl-pink">roughly 10,000 accounts taken over</span>, and no single IP ever looked unusual.</p>
  <ul>
    <li>A per-IP limit alone misses attacks spread over many IPs.</li>
    <li>A per-account <b>permanent lock</b> lets attackers lock out anyone, including your biggest customers.</li>
    <li>Different error messages for “no such user” and “wrong password” tell attackers which emails exist.</li>
  </ul>""",
    problem_figs=[rl_problem],
    analogy_side="the cash machine",
    analogy="""  <p>Three wrong PINs and the cash machine <b>keeps the card</b>. But the bank also watches <b>the machine</b> (many cards failing at the same one) and <b>the whole network</b> (an unusual spike of failures everywhere). Each pattern gets its own limit and its own response.</p>""",
    analogy_figs=[rl_analogy],
    map=[("Wrong PINs on one card", "Failures per account"),
         ("Many cards failing at one machine", "Failures per IP address or network"),
         ("A spike across the network", "The site-wide failure rate"),
         ("Keeping the card", "Delays and a challenge (and a reset path), not a silent permanent lock"),
         ("The bank calling you", "An email or push alert about a new sign-in")],
    how_side="three layers of limits, plus fewer passwords",
    how="""  <p>Count failures in a fast store (Redis) by account, by IP and network, and overall, with sliding windows. Respond in steps: a short delay, then a challenge (CAPTCHA or proof of work), then a temporary block for that source. Give the same message for unknown user and wrong password. Reduce what's worth stealing: block known-breached passwords, and move people to passkeys.</p>""",
    how_figs=[rl_how],
    steps=[("Count by account, source and overall", "Failures per account (15 min), per IP and per /24 or ASN (1 h), and site-wide per minute."),
           ("Respond in steps", "Delay, then challenge, then temporary block for the source. Never a permanent account lock without a recovery path."),
           ("Hide which accounts exist", "The same response and timing for unknown user and wrong password, also on reset and sign-up pages."),
           ("Block breached passwords", "Check new and changed passwords against known breach lists (k-anonymity range queries)."),
           ("Watch and alert", "Alert on failure-rate spikes; notify users of sign-ins from new devices; log every attempt for the audit trail.")],
    vocab=[("Credential stuffing", "Trying username/password pairs leaked from other sites."),
           ("Brute force", "Trying many passwords against one account."),
           ("Password spraying", "Trying a few common passwords against many accounts."),
           ("Lockout", "Blocking an account after failures; risky if permanent."),
           ("Step-up challenge", "An extra check (CAPTCHA, second factor) when risk is high."),
           ("Account enumeration", "Learning which usernames exist from different responses.")],
    code=dict(file="login-limits.ts", note="Node.js + Redis (rate-limiter-flexible)", src="""
import { RateLimiterRedis } from "rate-limiter-flexible";

const perAccount = new RateLimiterRedis({ storeClient: redis, keyPrefix: "fail:acct", points: 5, duration: 15 * 60 });
const perIp      = new RateLimiterRedis({ storeClient: redis, keyPrefix: "fail:ip",   points: 50, duration: 60 * 60 });

app.post("/login", async (req, res) => {
  const email = normalise(req.body.email);
  const [acct, ip] = await Promise.all([perAccount.get(email), perIp.get(req.ip)]);
  if ((ip?.consumedPoints ?? 0) >= 50) return res.status(429).json({ error: "Too many attempts. Try again later." });
  if ((acct?.consumedPoints ?? 0) >= 5 && !(await verifyChallenge(req))) {
    return res.status(401).json({ error: "Please complete the check.", challenge: true });
  }

  const user = await users.findByEmail(email);
  const ok = await verifyPassword(user?.passwordHash ?? DUMMY_HASH, req.body.password);  // same timing
  if (!user || !ok) {
    await Promise.all([perAccount.penalty(email), perIp.penalty(req.ip)]);
    audit("login.failed", { email, ip: req.ip });
    return res.status(401).json({ error: "Email or password is incorrect." });  // same message
  }
  await perAccount.delete(email);
  await startSession(res, user, req);   // and alert the user if this device is new
});
"""),
    tools="tools: rate-limiter-flexible, express-rate-limit with a Redis store, Cloudflare / AWS WAF bot and login protection, Have I Been Pwned Pwned Passwords range API, Cloudflare Turnstile or hCaptcha, identity providers' built-in attack protection.",
    gains=["<b>Stuffing and guessing slowed down</b> by orders of magnitude.",
           "<b>No easy lockout</b> attacks on real users.",
           "<b>Fewer accounts with leaked passwords</b>.",
           "<b>Attacks become visible</b> in metrics and logs."],
    losses=["<b>Some real users</b> see delays or challenges.",
            "<b>Shared IPs</b> (offices, mobile carriers) need higher limits.",
            "<b>Tuning</b>: limits that are too strict or too loose.",
            "<b>Doesn't fix password reuse</b>: passkeys do."],
    baseline="Each line compares <b>a login with no limits</b> to <b>layered limits, breached-password checks and identical errors</b>.",
    ratings=[(4, 3, "Three counters and a step-up path."),
             (4, 3, "A few users meet a challenge."),
             (2, 4, "Far fewer accounts taken over."),
             (3, 4, "Fewer attacker sessions acting as users."),
             (2, 4, "Floods of login attempts are cut off early."),
             (2, 4, "A stuffing run gets a few accounts, not thousands."),
             (2, 4, "Every attempt logged; spikes alert."),
             (4, 3, "A Redis store and maybe a challenge service."),
             (3, 3, "Libraries help; tuning takes care.")],
    pitfalls=[("Only per-IP limits", "Stuffing spread over thousands of IPs passes untouched.", "add per-account and site-wide limits."),
              ("Permanent lockout", "Attackers lock out real users on purpose by failing their logins.", "delays and challenges instead; temporary blocks for sources, not accounts."),
              ("Telling attackers who exists", "“No account with that email” on login, reset or sign-up.", "the same message and timing for every case."),
              ("Forgetting other doors", "Login is limited, but the mobile API, password reset and the old v1 endpoint are not.", "apply the same limits to every way of checking a password or sending a reset.")],
    use=["Every password login, reset and second-factor check.",
         "APIs that accept username and password (move them to tokens if you can).",
         "Sign-up and reset forms that reveal whether an account exists."],
    skip=["Passkey-only sign-in has less to guess (still limit, more loosely).",
          "Machine credentials: use short-lived tokens, not passwords.",
          "Never: there's no login that shouldn't have limits."],
    related=["<b>Passkeys</b>", "<b>Password hashing</b>", "<b>Rate limiter</b> (Vol. 1)", "<b>Audit logging</b>"],
    quiz=[("Why isn't a per-IP limit enough?", "Credential stuffing spreads attempts across thousands of IPs, so no single IP reaches the limit."),
          ("Why avoid permanent account lockouts?", "Attackers can lock out real users on purpose just by failing their logins."),
          ("What is account enumeration?", "Learning which emails have accounts because responses or timing differ for unknown users."),
          ("What reduces the value of leaked passwords most?", "Blocking known-breached passwords and moving users to passkeys.")],
    quiz_sit=[("Overnight, failed logins jump from 2,000 to 900,000 an hour, spread over 40,000 IPs, at about 20 attempts per IP. Successful logins from new devices also rise. What do you do first?",
               "Treat it as credential stuffing: switch on site-wide step-up (a challenge for all logins, or for logins from new devices), tighten per-account and per-network limits, and alert or force resets for accounts that signed in from new devices during the attack. Then review the logs and offer passkeys.")],
    try_it="On your own login in a local or staging environment, send 20 wrong passwords for one account and then 20 for 20 different accounts from one IP (a small script). Check what each layer did. Then compare the responses and timing for a real and a non-existent email, and make them identical.",
    remember="Limit by <span class=\"hl\">account</span>, by <span class=\"hl\">source</span> and <span class=\"hl\">overall</span>. Slow the guessers, never lock out the users.",
    sources=["OWASP Cheat Sheet Series, “Authentication” and “Credential Stuffing Prevention”.",
             "NIST SP 800-63B, section 5.2.2, “Rate Limiting (Throttling)”.",
             "Troy Hunt, Pwned Passwords and the k-anonymity range API.",
             "OWASP Automated Threats to Web Applications, OAT-008 (Credential Stuffing)."],
)

NOTES = [PASSKEYS, SIGNED_WEBHOOKS, LOGIN_THROTTLING]
