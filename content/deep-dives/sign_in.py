# Deep dive 07 · Sign-in, Tokens & Sessions. Builds on Vol. 5 notes 03 (OAuth 2.0 with PKCE), 04 (short-lived tokens),
# 07 (password hashing) and 11 (CSRF protection). Example: the mug shop from the earlier dives. Customer 7 signs in on a
# laptop and on the phone app. The web app has a small backend (a backend for frontend) that holds the tokens; the
# Orders API checks a 10-minute access token on every call.
# Helpers (mn, full, tbl, drill, code, fig, checklist) are injected by scripts/build_notes.py from scripts/dive.py.

# ------------------------------------------------------------------ 1 recap
pieces_svg = '''
  <rect class="bx-y" x="420" y="14" width="200" height="50" rx="8"/><text class="lbl" x="520" y="45" text-anchor="middle">identity provider</text>
  <rect class="bx" x="10" y="130" width="120" height="56" rx="8"/><text class="lbl" x="70" y="156" text-anchor="middle">browser</text><text class="soft" x="70" y="176" text-anchor="middle">customer 7</text>
  <rect class="bx-g" x="250" y="130" width="160" height="56" rx="8"/><text class="lbl" x="330" y="163" text-anchor="middle">shop backend</text>
  <rect class="bx" x="600" y="130" width="150" height="56" rx="8"/><text class="lbl" x="675" y="163" text-anchor="middle">Orders API</text>
  <path class="ln-d" d="M70 128 Q120 40 416 40" marker-end="url(#a)"/><text class="soft" x="200" y="34" text-anchor="middle">signs in here, once</text>
  <path class="ln" d="M130 158 H248" marker-end="url(#a)"/><text class="soft" x="190" y="148" text-anchor="middle">session cookie</text>
  <path class="ln" d="M370 128 L470 66" marker-end="url(#a)"/><text class="soft" x="432" y="108">swap code for tokens</text>
  <path class="ln" d="M410 158 H598" marker-end="url(#a)"/><text class="soft" x="504" y="148" text-anchor="middle">access token, 10 min</text>
  <text class="soft" x="330" y="212" text-anchor="middle">the refresh token stays here</text>
  <text class="soft" x="675" y="212" text-anchor="middle">checks every token</text>
'''
recap = '''
<p>The security volume has four notes that are really one system. Customer 7 signs in to the mug shop on a laptop. The password is typed at the identity provider, never at the shop. The shop's backend receives tokens and gives the browser a cookie. The Orders API checks a token on every call.</p>
''' + tbl(["Note", "In one line", "Its part of the system"], [
    ["OAuth 2.0 with PKCE", "sign in at the provider; the app swaps a one-time code and a secret for tokens", "how a session starts"],
    ["Short-Lived Tokens", "access tokens that live minutes, refresh tokens that rotate on every use", "how a session continues"],
    ["Password Hashing", "store slow, salted hashes, or better, no passwords at all", "what the provider keeps"],
    ["CSRF Protection", "a cookie is sent whichever site asks; check the request really came from your page", "what a cookie session must defend"],
]) + fig(760, 230, "The pieces of one sign-in. Customer 7's browser signs in once at the identity provider. The browser holds only a session cookie for the shop backend. The shop backend swaps the one-time code for tokens at the provider and keeps the refresh token. It calls the Orders API with a ten-minute access token, which the API checks on every call.",
         pieces_svg, "Three parties, four kinds of credential. The browser never holds a token.") + mn("The OAuth note's own going-deeper chapter covers where tokens live and how an API checks one. This dive starts from there.") + '''
<p class="full">Each note is correct on its own. Put them together and the questions change. How long is customer 7 actually signed in, and by which of the four credentials? What does “sign out” end, and what keeps working for another ten minutes? When the shop removes someone's admin rights, when does the system notice? The answers are design decisions, and most teams make them by accident. This deep dive makes them on purpose.</p>
'''

# ------------------------------------------------------------------ 2 three sessions
day_svg = '''
  <text x="140" y="44" text-anchor="end">provider session</text><rect class="bx-g" x="150" y="26" width="590" height="26" rx="4"/><text class="soft" x="445" y="45" text-anchor="middle">signed in at the provider: days</text>
  <text x="140" y="84" text-anchor="end">shop session</text><rect class="bx-y" x="150" y="66" width="590" height="26" rx="4"/><text class="soft" x="445" y="85" text-anchor="middle">cookie: ends after 30 idle days</text>
  <text x="140" y="124" text-anchor="end">refresh token</text>
  <rect class="bx" x="190" y="106" width="34" height="26" rx="3"/><text class="soft" x="207" y="125" text-anchor="middle">r1</text>
  <rect class="bx" x="230" y="106" width="34" height="26" rx="3"/><text class="soft" x="247" y="125" text-anchor="middle">r2</text>
  <rect class="bx" x="270" y="106" width="34" height="26" rx="3"/><text class="soft" x="287" y="125" text-anchor="middle">r3</text>
  <rect class="bx" x="310" y="106" width="34" height="26" rx="3"/><text class="soft" x="327" y="125" text-anchor="middle">r4</text>
  <rect class="bx" x="540" y="106" width="34" height="26" rx="3"/><text class="soft" x="557" y="125" text-anchor="middle">r5</text>
  <rect class="bx" x="580" y="106" width="34" height="26" rx="3"/><text class="soft" x="597" y="125" text-anchor="middle">r6</text>
  <rect class="bx" x="620" y="106" width="34" height="26" rx="3"/><text class="soft" x="637" y="125" text-anchor="middle">r7</text>
  <text x="140" y="164" text-anchor="end">access token</text>
  <rect class="bx-r" x="190" y="146" width="34" height="26" rx="3"/><rect class="bx-r" x="230" y="146" width="34" height="26" rx="3"/>
  <rect class="bx-r" x="270" y="146" width="34" height="26" rx="3"/><rect class="bx-r" x="310" y="146" width="34" height="26" rx="3"/>
  <rect class="bx-r" x="540" y="146" width="34" height="26" rx="3"/><rect class="bx-r" x="580" y="146" width="34" height="26" rx="3"/>
  <rect class="bx-r" x="620" y="146" width="34" height="26" rx="3"/>
  <path class="ln-d" d="M352 140 H532"/><text class="soft" x="442" y="132" text-anchor="middle">away: nothing to refresh</text>
  <text class="soft" x="267" y="198" text-anchor="middle">morning: browsing</text><text class="soft" x="597" y="198" text-anchor="middle">evening: checkout</text>
'''
sessions = '''
<p>Ask a team “how long does a session last?” and you will get four different answers, all correct. A signed-in customer is held up by four separate credentials, each with its own clock.</p>
''' + fig(760, 210, "One day of customer 7's session as four rows. The provider session lasts days. The shop session cookie ends after 30 idle days. The refresh token rotates: r1 to r4 in the morning while browsing, r5 to r7 in the evening at checkout, and nothing in between while the customer is away. Each refresh produces a new ten-minute access token.",
          day_svg, "Four layers, four clocks. Signing out has to deal with each one.") + tbl(["Layer", "Lives in", "Typical life", "Ends when"], [
    ["<b>Provider session</b>", "a cookie on the identity provider's own domain", "days", "the customer signs out at the provider, or it expires"],
    ["<b>Shop session</b>", "a cookie on the shop's domain, and a row in the shop's session store", "30 idle days, 90 days at most", "sign-out deletes the row, or it expires"],
    ["<b>Refresh token</b>", "the shop backend, or the phone's keychain", "replaced on every use; 14 idle days", "it is used, revoked or expires"],
    ["<b>Access token</b>", "the backend's memory; sent to the APIs", "10 minutes", "it expires. Usually nothing can end it earlier"],
], hot=(3,)) + mn("The ID token is missing on purpose. It says who signed in, once. It is not a session and it is not for calling APIs.") + '''
<h3>What one request does</h3>
<ol>
  <li>The browser sends the shop cookie. The backend looks up the session row: does it exist, has it expired?</li>
  <li>The row points at the stored tokens. If the access token has more than a minute left, use it.</li>
  <li>If not, send the refresh token to the provider. Store the new access token and the new refresh token; the old refresh token is now dead.</li>
  <li>Call the Orders API with the access token. The API checks the signature, issuer, audience and expiry.</li>
</ol>
''' + full('''<p>Two kinds of expiry appear in the table, and a design needs both. <b>Idle</b> expiry ends a session nobody is using: 30 days without a visit. <b>Absolute</b> expiry ends every session eventually, however busy: 90 days, then sign in again. Idle without absolute gives a stolen session eternal life as long as the thief keeps it busy.</p>
<h3>Recent sign-in for risky actions</h3>
<p>A 30-day session is right for browsing mugs and wrong for changing the email address on the account. The usual answer is not a shorter session. It is asking again for the few actions that matter: change email, change password, add a payment card, see stored addresses. The session records <b>when</b> the customer last proved who they are, and those actions require that to be within ten minutes. If it is older, the shop sends the customer to the provider with a request to sign in again (in OpenID Connect, <code>max_age</code> or <code>prompt=login</code>) and checks the time in the new ID token.</p>
<p>That way a stolen laptop with an open session can buy mugs, which is annoying, but cannot take over the account, which is a disaster.</p>''')

# ------------------------------------------------------------------ 3 sessions or tokens
stateful = '''
<p>There are two ways to remember that someone signed in, and the argument between them has gone on for years. Both are right in different places.</p>
''' + tbl(["", "A session id (stateful)", "A self-contained token (JWT)"], [
    ["What the client holds", "a random id that means nothing by itself", "signed data: who, which roles, until when"],
    ["Checking it", "look the id up in a store", "check the signature; no lookup"],
    ["Ending it early", "delete the row; works on the next request", "hard. It stays valid until it expires"],
    ["Size", "about 30 bytes", "often 1 KB or more, on every request"],
    ["Who can read it", "nobody: it is a random number", "anyone. It is encoded, not encrypted"],
    ["Fits", "a browser talking to its own backend", "one service calling another; APIs called by many clients"],
]) + mn("“Stateless sessions” is a slogan. The day you need a sign-out button, you have state again.") + '''
<h3>The shape most systems end up with</h3>
''' + tbl(["Link", "Credential", "Why"], [
    ["browser → shop backend", "an opaque session cookie", "short, unreadable, ends the moment the row is deleted"],
    ["shop backend → APIs", "a 10-minute JWT access token", "APIs check it without a call to anyone; short life limits the damage"],
    ["shop backend → provider", "an opaque refresh token, stored server side", "used rarely, checked by lookup, so it can be revoked"],
]) + code("set-cookie.http", "the shop's session cookie", '''
Set-Cookie: __Host-sid=k7Qe3w...; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=2592000
''', plain=True) + full('''<p>Each attribute does one job. <code>Secure</code>: only over HTTPS. <code>HttpOnly</code>: no script in the page can read it, so a cross-site scripting bug cannot steal it. <code>SameSite=Lax</code>: not sent with forms posted from other sites, which removes most CSRF attacks. The <code>__Host-</code> prefix makes the browser refuse the cookie unless it is <code>Secure</code>, has <code>Path=/</code> and no <code>Domain</code>, so a careless subdomain cannot overwrite it.</p>
<h3>What goes inside an access token</h3>
<p>Little. The user id, the audience, the expiry, the scopes. Every claim is a promise that cannot be withdrawn until the token expires (drill 4), and anyone holding the token can decode it. No email address, no name, no address: if a token ends up in a log, it should not also be a data leak.</p>
<p>The checks an API makes are listed in the OAuth note's going-deeper chapter. Two are worth repeating because they are skipped so often. Check the <b>audience</b>: a token issued for the Loyalty API must not be accepted by the Orders API, or one weak service can lend its tokens to all the others. And fix the <b>algorithm</b> in configuration: never let the token's own header choose it.</p>''')

# ------------------------------------------------------------------ 4 drills
drills = mn("Cover the bottom half of each card. What happens next?") + '''
<ul class="drill-index" aria-label="The six drills">
  <li><a href="#drill-1">1 · stolen refresh token</a></li><li><a href="#drill-2">2 · two tabs</a></li><li><a href="#drill-3">3 · sign-out</a></li>
  <li><a href="#drill-4">4 · former admin</a></li><li><a href="#drill-5">5 · fixation</a></li><li><a href="#drill-6">6 · fast clock</a></li>
</ul>
''' + drill(1, "The refresh token is copied off the phone", [
    ("Timeline", "Malware on customer 7's phone copies the refresh token <code>r5</code>. From another machine the attacker uses it and receives a fresh pair, <code>r6</code> and an access token. A minute later the real app, still holding <code>r5</code>, tries to refresh."),
    ("Without rotation", "Nothing happens at all. A refresh token that is never replaced works for the attacker for 14 days, renewing itself each time, and nobody can tell the two users apart.", True),
    ("What saves you", "Rotation with reuse detection. <code>r5</code> was already used, so its second appearance means two parties hold it. The provider cannot tell which is real, so it revokes the whole family: <code>r6</code> stops working too. Both are signed out. The customer signs in again with a password or passkey; the attacker cannot."),
], "rotate refresh tokens on every use, and treat a reused one as theft: revoke everything that descends from it.") + drill(2, "Two tabs refresh at the same moment", [
    ("Timeline", "Customer 7 has the shop open in two browser tabs that each hold tokens (a design the shop later dropped). Both access tokens expire at 10:00. Both tabs refresh within 40 ms using the same <code>r3</code>."),
    ("What you see", "The second request looks exactly like drill 1. The family is revoked and a paying customer is signed out for no reason. Support hears “your site keeps logging me out”, mostly from the most active customers.", True),
    ("What saves you", "Make refreshing happen in one place: the backend holds the tokens and refreshes under a lock per session, so concurrent requests wait for one refresh. Where clients must refresh themselves, give reuse a short grace period: within a few seconds, a repeat from the same client gets the same new pair back instead of a revocation."),
], "real clients race with themselves. Serialise the refresh, or forgive an immediate repeat.") + drill(3, "Signed out, and signed straight back in", [
    ("Timeline", "On a library computer customer 7 clicks “Sign out”. The shop deletes its cookie. The next person clicks “Sign in”, is sent to the provider, and is let straight through: the provider session is still alive. They are now customer 7."),
    ("What else is still alive", "The refresh token, if the shop only cleared its cookie and kept the tokens. And the last access token, for up to ten minutes, wherever it was copied.", True),
    ("What saves you", "Sign-out ends every layer you can reach: delete the session row, revoke the refresh token at the provider, then send the browser to the provider's sign-out endpoint so its session ends too (in OpenID Connect, RP-initiated logout). The access token's remaining minutes are the price of not checking it; chapter 5 shows how to shorten that window when it matters."),
], "sign-out must end the provider session and the refresh token, not just your own cookie.") + drill(4, "The admin who is no longer an admin", [
    ("Timeline", "At 10:00 a staff member's admin role is removed because they are leaving. Their access token, issued at 9:58, contains <code>\"role\": \"admin\"</code> and expires at 10:08. At 10:05 they export the customer list."),
    ("What you see", "The audit log shows an admin export after the role was removed. Every system did what it was told: the token was valid, and it said admin. With the 24-hour tokens some teams use, the window is a day.", True),
    ("What saves you", "Treat claims in a token as a promise that lasts until expiry, and choose what you put in that promise. Keep privileged tokens short. For the few dangerous actions (exports, refunds, role changes), check the permission at the source at the moment of the action, not from the token. And push removals through one of the revocation mechanisms in chapter 5."),
], "whatever a token says stays true until it expires. Check dangerous permissions live.") + drill(5, "The session id the attacker chose", [
    ("Timeline", "The shop gives every visitor a session cookie before sign-in, to hold the basket. An attacker visits, gets <code>sid=abc</code>, and plants that cookie in the victim's browser through a vulnerable subdomain. The victim signs in. The shop marks <code>abc</code> as signed in."),
    ("What you see", "The attacker, holding <code>abc</code>, is now signed in as the victim. No password was stolen and no token was copied.", True),
    ("What saves you", "Issue a new session id at sign-in and at every change of privilege, and copy the basket across. The old id stays an anonymous basket. The <code>__Host-</code> cookie prefix from chapter 3 also stops a subdomain from setting the cookie in the first place."),
], "a session id never survives sign-in. Always issue a new one.") + drill(6, "One server's clock is three minutes fast", [
    ("Timeline", "One of six API servers lost its time sync after a host move. Its clock is three minutes ahead. Every access token it sees in the last three minutes of its life is already expired."),
    ("What you see", "About one request in six gets a 401 near the end of a token's life, the client refreshes, and sometimes the refresh lands in drill 2. The reports say “random logouts”. Nobody can reproduce them on a laptop.", True),
    ("What saves you", "Keep clocks synced and alert when one drifts by more than a second or two. Allow a small leeway, 30 to 60 seconds, when checking <code>exp</code> and <code>nbf</code>. Refresh tokens a minute before they expire, not after a 401."),
], "token checks depend on clocks. Sync them, watch them, and allow a minute of leeway.") + full('''<h3>What the six drills add up to</h3>
''' + tbl(["Decision", "Drill"], [
    ["refresh tokens rotate; reuse revokes the family", "1"],
    ["refreshing happens in one place, or tolerates an immediate repeat", "2"],
    ["sign-out reaches the provider and revokes the refresh token", "3"],
    ["tokens carry few privileges; dangerous actions check live", "4"],
    ["a new session id at every sign-in", "5"],
    ["synced clocks and a small leeway", "6"],
]))

# ------------------------------------------------------------------ 5 revocation
revocation = '''
<p>Short-lived tokens were adopted to avoid a hard problem: checking, on every request, whether a credential is still good. A token nobody checks again cannot be taken back. Revocation is buying back some of that checking, and it is worth deciding how much you need for each kind of event.</p>
<h3>Six events that should end access</h3>
''' + tbl(["Event", "How fast must it work?"], [
    ["customer signs out on this device", "now, on this device"],
    ["“sign out of all devices”", "within a minute"],
    ["password changed or reset", "within a minute, everywhere except the device that changed it"],
    ["phone reported stolen", "now"],
    ["admin role removed, employee leaves", "now for dangerous actions; minutes for the rest"],
    ["a token appears in a log or a public repository", "now"],
]) + '''
<h3>Six mechanisms, cheapest first</h3>
''' + tbl(["Mechanism", "How", "Cost", "Delay"], [
    ["<b>Wait</b>", "do nothing; the access token expires", "none", "up to its lifetime: 10 minutes"],
    ["<b>Revoke the refresh token</b>", "delete it at the provider", "none extra", "no new access tokens; the current one lives on"],
    ["<b>Delete the session row</b>", "the shop backend stops using the session", "a lookup the backend already does", "immediate for the web app"],
    ["<b>User version</b>", "tokens carry <code>sv: 7</code>; the user record holds 7; bump it to 8 to end every older token", "one cached lookup per request, per user", "as long as the cache: say 30 seconds"],
    ["<b>Deny list</b>", "list revoked token ids (<code>jti</code>); entries expire when the tokens would", "one lookup per request", "seconds"],
    ["<b>Introspection</b>", "ask the provider about every token", "a network call per request; the provider becomes critical", "none"],
], hot=(3,)) + mn("The user-version row is the workhorse: one number per user, and every token older than it is dead.") + code("require-current-user.ts", "end every older token by bumping one number", '''
export async function requireCurrentUser(token: Claims) {
  // cached for 30 s: a revocation takes effect within half a minute
  const current = await cache.get(`user-version:${token.sub}`, 30, () =>
    db.value("SELECT session_version FROM users WHERE id = $1", [token.sub]));

  if (token.sv < current) throw new Unauthorized("Session ended, please sign in again");
}

// "sign out everywhere", password change, role removal:
// UPDATE users SET session_version = session_version + 1 WHERE id = $1;
''') + full('''<h3>Choosing per event</h3>
''' + tbl(["Event", "Use"], [
    ["sign out on this device", "delete the session row, revoke its refresh token, end the provider session (drill 3)"],
    ["sign out of all devices, password change", "bump the user version; revoke every refresh token of the user"],
    ["phone stolen", "revoke that device's refresh token family; bump the user version if in doubt"],
    ["admin role removed", "bump the user version, and check dangerous actions live anyway (drill 4)"],
    ["token leaked in a log", "deny-list its id until it would expire; find out why tokens reach logs"],
    ["signing key leaked", "rotate the key. Every token signed with it dies, which signs everyone out. Accept it"],
]) + '''<p>Most of the shop needs nothing beyond the first two mechanisms and the user version. Introspection on every request is rarely worth it; if a service needs that much certainty, it can call introspection for the few calls that matter.</p>
<h3>When the provider can tell you</h3>
<p>Identity providers can also push events to the applications that rely on them. OpenID Connect back-channel logout sends a signed message to the shop when a session ends at the provider, so the shop can delete its own row. Newer standards for sharing security signals between services (CAEP, part of the OpenID Shared Signals framework) carry events such as “credentials changed” or “session revoked”. They do not remove the need for short lifetimes, because a message can be lost. They shorten the window on a good day.</p>''')

# ------------------------------------------------------------------ 6 numbers
numbers = '''
<p>Lifetimes are usually copied from a tutorial. Here they are worked out for the shop, each from what it protects.</p>
''' + tbl(["Setting", "Reasoning", "Value"], [
    ["<b>Access token</b>", "the longest a revoked user may keep calling an API without a live check", "10 min"],
    ["<b>Refresh token</b>, idle", "a shopper who comes back after a fortnight should not have to sign in", "14 days"],
    ["<b>Refresh token</b>, absolute", "every device proves itself again eventually", "90 days"],
    ["<b>Shop session</b>, idle and absolute", "the same as the refresh token it uses", "30 / 90 days"],
    ["<b>Recent sign-in</b> for risky actions", "long enough to finish changing an email address", "10 min"],
    ["<b>Clock leeway</b>", "covers small drift, not a broken clock (drill 6)", "60 s"],
    ["<b>Refresh before expiry</b>", "no request ever meets an expired token", "1 min early"],
    ["<b>Refresh grace</b>", "an immediate repeat from the same client is not theft (drill 2)", "10 s"],
    ["<b>User-version cache</b>", "how late “sign out everywhere” may take effect", "30 s"],
]) + mn("Write the reasoning next to each number in the config. Next year somebody will want to change it.") + '''
<h3>What the refresh traffic costs</h3>
<p>At the evening peak 20,000 customers are active. Each refreshes once per access-token lifetime, every ten minutes: 20,000 ÷ 600 s ≈ <b>33 refreshes a second</b>. Shortening access tokens to two minutes would make it 167 a second, five times the load on the provider, to close a window that the user version already closes in 30 seconds. Shorter is not automatically safer; it is a cost you should be able to name.</p>
''' + full('''<h3>Rotating the signing key</h3>
<p>APIs check access tokens against the provider's public keys, published as a JSON Web Key Set and cached. Each token names its key with <code>kid</code>. A key change done in one step signs everyone out: new tokens are signed with a key the APIs have not fetched yet, and old tokens stop verifying the moment the old key disappears.</p>
''' + tbl(["When", "Step"], [
    ["day 0", "publish the new key in the key set, next to the old one. Keep signing with the old key"],
    ["day 1", "start signing with the new key. Every API has fetched the set by now"],
    ["day 1 + 10 min + cache time", "the last token signed with the old key has expired"],
    ["day 2", "remove the old key from the set"],
]) + '''<p>APIs cache the key set for a few hours and fetch it again when they meet an unknown <code>kid</code>, with a limit on how often, so a stream of tokens with made-up key ids cannot turn into a stream of fetches.</p>''')

# ------------------------------------------------------------------ 7 front door
frontdoor = '''
<p>Everything so far starts after sign-in. The sign-in itself, and the paths around it, are where accounts are actually taken. If the shop runs its own passwords instead of using a provider, this chapter is its job; if not, it is a list of things to check that the provider does.</p>
<h3>Credential stuffing</h3>
<p>Billions of email and password pairs from other sites' leaks are for sale. Attackers try them against every login page, slowly and from many addresses. The password-hashing note protects stolen hashes; it does nothing against a correct password that was stolen somewhere else.</p>
''' + tbl(["Defence", "Stops"], [
    ["limit attempts per account, with growing delays", "many guesses at one customer"],
    ["limit attempts per address and per network", "one machine trying many accounts"],
    ["watch the overall failure rate", "the slow, spread-out attack the first two miss: an alert when failures jump from 5 % to 40 %"],
    ["refuse passwords that appear in known leaks", "the reused password at the door; checked by sending a short hash prefix, never the password"],
    ["a second factor, or passkeys", "a correct password on its own"],
]) + mn("Passkeys end this chapter's first half: there is nothing to stuff. Offer them, and make them the default where you can.") + '''
<h3>The hash on the login path</h3>
''' + tbl(["Quantity", "Value"], [
    ["Argon2id settings", "64 MB of memory, 3 passes: about 50 ms per hash"],
    ["Logins at the evening peak", "40 a second"],
    ["CPU busy hashing", "40 × 0.05 s = 2 cores"],
    ["Memory while hashing", "40 × 0.05 × 64 MB ≈ 130 MB in flight"],
    ["An attacker sending 2,000 a second", "100 cores. Cap concurrent hashes and refuse early"],
]) + full('''<p>The slow hash that protects a leaked table is also an easy way to overload the login service. Put the rate limits in front of the hash, and a bulkhead around it: a fixed number of hashes at once, and a fast “try again” beyond that.</p>
''' + code("verify-password.ts", "check, and upgrade old hashes on the way", '''
export async function checkPassword(user: User | null, password: string) {
  // unknown email: hash anyway, so the answer takes the same time
  const stored = user?.passwordHash ?? DUMMY_HASH;
  const ok = await argon2.verify(stored, password);
  if (!user || !ok) return false;

  if (argon2.needsRehash(stored, CURRENT_SETTINGS)) {        // settings raised since this hash was made
    await users.setPasswordHash(user.id, await argon2.hash(password, CURRENT_SETTINGS));
  }
  return true;
}
''') + '''<p>Two habits are in those lines. An unknown email address takes the same time and gets the same message as a wrong password, so the login form cannot be used to find out who has an account. And old hashes are upgraded the next time their owner signs in, which is the only moment the shop ever has the password in hand.</p>
<h3>Recovery is the real front door</h3>
<p>An account is only as strong as the easiest way to get back into it. A reset email that anyone can trigger, with a link that never expires, is a password that the attacker gets to choose.</p>
<ul>
  <li><b>Reset links</b> work once, expire in 30 minutes, and are stored as a hash, like a password.</li>
  <li><b>A completed reset</b> ends every other session (bump the user version) and sends a notice to the customer.</li>
  <li><b>Changing the email address</b> needs a recent sign-in and a confirmation at the old address, or the first thing an attacker does is move the account out of reach.</li>
  <li><b>Support staff</b> who can reset accounts by phone are part of the sign-in system. Their process needs the same thought as the code.</li>
</ul>''')

# ------------------------------------------------------------------ 8 running
running = '''
<p>Sign-in fails in two ways that look alike from outside. Customers cannot get in, or customers keep falling out. The graphs need to tell those apart.</p>
''' + tbl(["Metric", "Healthy", "It means trouble when"], [
    ["<b>Sign-in success rate</b>", "steady, most attempts succeed", "it falls: an outage, or a stuffing attack raising the failures"],
    ["<b>Refresh failures</b>, by reason", "a few expired, almost no reuse", "reuse jumps: drill 2 after a front-end change, or real theft"],
    ["<b>Token rejections at the APIs</b>, by reason: expired, signature, audience, not yet valid", "almost all “expired”", "“signature” rises: key rotation went wrong. “Not yet valid”: a fast clock"],
    ["<b>Sessions per customer</b>", "a few devices", "one account with hundreds: a shared or stolen account"],
    ["<b>Resets and email changes</b>", "a steady trickle", "a spike: someone is taking accounts through recovery"],
]) + mn("Splitting rejections by reason is the single most useful graph here. One number for “401s” hides every cause.") + '''
<h3>Audit log</h3>
<p>Record sign-in, sign-out, refresh-token reuse, password and email changes, second-factor changes, role changes and every revocation. Each entry says who, from which device and network, when, and why. This is the log the security team will read on its worst day.</p>
''' + full('''<h3>Never log a credential</h3>
<p>Tokens leak into logs more than anywhere else: an <code>Authorization</code> header in a request dump, a token in a URL, a session cookie in an error report. Redact those fields in the logging library, not in each service, and test that the redaction works. Keep tokens out of URLs altogether, since a URL ends up in browser history, proxy logs and the <code>Referer</code> header sent to other sites.</p>
<h3>Runbook: “customers are being logged out at random”</h3>
<ol>
  <li><b>Look at the rejection reasons.</b> “Signature” points at keys. “Not yet valid” or early “expired” points at a clock. Reuse in the refresh failures points at drill 2.</li>
  <li><b>Did keys change?</b> An old key removed before its tokens expired, or an API that cached the key set and never fetched the new one.</li>
  <li><b>Did cookies change?</b> A new cookie name, domain or <code>SameSite</code> setting in the last release can drop sessions for some browsers.</li>
  <li><b>Did servers change?</b> Two versions of the backend behind one load balancer, each with a different cookie secret, sign each other's customers out.</li>
</ol>
<h3>Runbook: “a token has leaked”</h3>
<ol>
  <li><b>An access token:</b> deny-list its id until it would expire, or bump the user's version. Find how it reached the place it leaked.</li>
  <li><b>A refresh token:</b> revoke its family. The customer signs in again.</li>
  <li><b>Many tokens, or a signing key:</b> rotate the key at once and accept that everyone signs in again. Then tell the customers what happened.</li>
</ol>''')

# ------------------------------------------------------------------ 9 testing
testing = '''
<p>Sign-in code is usually tested on the happy path: sign in, see the page. The failures above are all about tokens and sessions in the wrong state, and each can be written as a short test.</p>
''' + tbl(["Test", "Expect"], [
    ["an access token one second past expiry, beyond the leeway", "401"],
    ["a token for another audience (the Loyalty API's)", "401"],
    ["a token with <code>alg: none</code>, or signed with a key that is not in the set", "401"],
    ["a token signed with the previous key, during rotation", "accepted until it expires"],
    ["the same refresh token used twice, a minute apart", "the second fails, and the family is revoked"],
    ["the same refresh token used twice within the grace period", "both get the same new pair"],
    ["sign out, then use the old session cookie and refresh token", "both rejected"],
    ["sign in with an existing anonymous session", "a new session id; the basket is still there"],
    ["password change on the laptop", "the phone's next request after 30 s is rejected"],
    ["a POST from another origin with the session cookie and no CSRF token", "403"],
    ["sign-in with an unknown email and with a wrong password", "the same message, in about the same time"],
], hot=(4, 8)) + mn("Most of these are three lines with a test helper that mints tokens. Write the helper first.") + code("refresh.test.ts", "drill 1, as a test", '''
test("a reused refresh token revokes the whole family", async () => {
  const { refresh: r1 } = await signIn("customer-7");
  const { refresh: r2 } = await refreshWith(r1);       // normal rotation

  await clock.advance("1m");
  await expect(refreshWith(r1)).rejects.toThrow("reuse");   // r1 again: theft
  await expect(refreshWith(r2)).rejects.toThrow("revoked"); // and r2 is dead too
});
''') + full('''<h3>Check the cookie, not just the code</h3>
<p>A unit test can pass while the real response sends the cookie without <code>HttpOnly</code>, because a proxy or framework setting changed it. Add one end-to-end check that signs in through a real browser and reads the cookie's flags as the browser stored them. The same test can try a cross-site form post against the real stack and expect it to fail.</p>
<h3>Test the provider's settings too</h3>
<p>Much of this system is configuration at the identity provider: lifetimes, rotation, reuse detection, allowed redirect addresses. Export that configuration, keep it in the repository, and review changes to it like code. A refresh lifetime changed from 14 days to 14 months in a console, by one person on a Friday, is a security change with no pull request.</p>''')

# ------------------------------------------------------------------ 10 tools, lab, checklist
tools = '''
<h3>What to build and what to buy</h3>
''' + tbl(["Part", "Usually", "Why"], [
    ["Sign-in, passwords, passkeys, second factor, recovery", "an identity provider: Auth0, Okta, Microsoft Entra ID, AWS Cognito, Keycloak, Zitadel", "the hardest part to get right, and the most attacked"],
    ["The OAuth flow in your app", "a certified OpenID Connect client library", "state, verifier, nonce and token checks are easy to get subtly wrong"],
    ["Token checks at APIs", "a maintained JWT library, configured strictly", "never parse tokens by hand"],
    ["Your session, CSRF, cookie settings", "yours", "the provider does not see your cookies"],
    ["Revocation inside your APIs", "yours", "only your APIs can check a user version"],
    ["Who may do what", "yours", "the provider knows who someone is, not what they may do in your shop"],
]) + mn("Buying the provider moves the front door out of your code. It does not move the house.") + '''
<h3>Lab</h3>
<p>The shop adds two features. Customers get a “Sign out of all devices” button in their account settings. Staff get an admin area, and when a staff member's admin role is removed, it must stop working within one minute, and exports must stop at once.</p>
<ol class="keep">
  <li>What happens, layer by layer, when “Sign out of all devices” is pressed on the laptop?</li>
  <li>What does the phone app see, and when?</li>
  <li>How do you meet “within one minute” for the admin role without checking the provider on every request?</li>
  <li>How do you meet “at once” for exports?</li>
  <li>A staff member is in the middle of a 40-minute export when the role is removed. What should happen?</li>
</ol>
<div class="check quiz"><h3>model answer</h3>
<details><summary>1 · The button</summary><p>The shop bumps customer 7's user version, revokes every refresh token the provider holds for that user, deletes the session rows for the other devices, and keeps the laptop's own session, re-issuing its tokens with the new version. Optionally it ends the provider sessions too, so no device can sign straight back in (drill 3).</p></details>
<details><summary>2 · The phone</summary><p>Its current access token carries the old version. Within 30 seconds, when the cache expires, the APIs reject it. The app tries to refresh, the refresh token is revoked, and it shows the sign-in screen. Worst case: about 30 seconds, not ten minutes.</p></details>
<details><summary>3 · Within a minute</summary><p>Removing the role bumps the staff member's user version. Every API already checks the version with a 30-second cache, so their tokens die within half a minute. New tokens are issued without the role.</p></details>
<details><summary>4 · Exports at once</summary><p>The export endpoint does not trust the token's role. It asks the permission store, live, at the moment the export starts. One extra lookup on a rare, dangerous action is cheap.</p></details>
<details><summary>5 · The long export</summary><p>The job checks the permission again between batches and stops when it fails, recording who started it, when it stopped and why. A long job that only checked at the start is the long-lived token problem in another shape.</p></details>
</div>
<h3>The review checklist</h3>
''' + checklist([
    ("Sessions", ["Every layer is listed with its lifetime: provider, shop, refresh, access", "Sessions have idle and absolute expiry", "Risky actions require a recent sign-in", "A new session id at every sign-in and privilege change"]),
    ("Cookies and the browser", ["Session cookie is __Host-, Secure, HttpOnly, SameSite=Lax or Strict", "The browser holds no tokens; the backend holds them", "State-changing requests check a CSRF token or the Origin", "No state changes on GET"]),
    ("Tokens", ["Access tokens live minutes and carry few claims, none personal", "APIs check signature, issuer, audience, expiry, with the algorithm fixed", "Refresh tokens rotate; reuse revokes the family; immediate repeats are forgiven", "Signing keys rotate in steps, with both keys published for a while", "Clocks are synced and checks allow a small leeway"]),
    ("Ending access", ["Sign-out deletes the session, revokes the refresh token and ends the provider session", "A user version lets one update end every older token", "Dangerous actions check permissions live", "Password reset and email change end other sessions and notify the customer"]),
    ("The front door", ["Rate limits per account, per address and on the overall failure rate", "Leaked passwords are refused; passkeys are offered", "Unknown accounts get the same answer in the same time", "Reset links are single-use, short-lived and stored hashed"]),
    ("Tests and operations", ["Tests cover expiry, audience, reuse, sign-out, fixation and CSRF", "A real-browser test reads the cookie flags", "Token rejections are graphed by reason", "Credentials are redacted from logs, and tokens never appear in URLs", "Provider settings are kept and reviewed in the repository"]),
])

# ------------------------------------------------------------------ the dive
DIVE = dict(
    slug="sign-in-tokens-sessions", no=7, title="Sign-in, Tokens & Sessions",
    sub="Four credentials with four clocks: how long a customer is really signed in, what “sign out” ends, and how to take access back.",
    summary="A deep dive on sign-in, tokens and sessions: the four layers of a session, session ids and JWTs, six failure drills, revocation, lifetimes and key rotation, credential stuffing and recovery, operations and testing.",
    builds_on="Vol. 5, notes 03, 04, 07 and 11",
    builds_on_links=[("OAuth 2.0 with PKCE", "../../security/notes/oauth-pkce.html"), ("Short-Lived Tokens", "../../security/notes/short-lived-tokens.html"),
                     ("Password Hashing", "../../security/notes/password-hashing.html"), ("CSRF Protection", "../../security/notes/csrf-protection.html")],
    notes=[("security", "oauth-pkce"), ("security", "short-lived-tokens"), ("security", "password-hashing"), ("security", "csrf-protection")],
    facts=[("Example", "customer 7, a laptop and a phone, signed in to the mug shop")],
    blurb="Four layers of a session, six failure drills, revocation, lifetimes and key rotation, credential stuffing and account recovery.",
    chapters=[
        dict(id="recap", nav="Recap", title="Four notes in sixty seconds",
             gist="OAuth with PKCE starts a session, short-lived tokens keep it going, password hashing protects what the provider stores, and CSRF protection guards the cookie. Together they form one system, and the hard questions are about the whole: how long a customer is signed in, what sign-out ends, and how access is taken back.",
             body=recap),
        dict(id="sessions", nav="Four layers", title="Four layers, four clocks",
             gist="A signed-in customer is held up by a provider session, the shop's own session, a refresh token and an access token, each with its own lifetime. Sessions need idle and absolute expiry. Risky actions such as changing the email address ask for a recent sign-in instead of shortening every session.",
             body=sessions,
             check=[("A stolen laptop has an open 30-day session. What stops the thief from taking over the account?", "Changing the email or password requires a sign-in within the last ten minutes, which the thief cannot do without the password or passkey."),
                    ("Why have absolute expiry when idle expiry already ends unused sessions?", "A session that is used regularly, for example by a thief, would otherwise never end.")]),
        dict(id="stateful", nav="Ids or tokens", title="Session ids or tokens",
             gist="A session id must be looked up but can be ended at once. A signed token needs no lookup and cannot be ended early. Most systems use both: an opaque cookie between browser and backend, short signed access tokens between services, and an opaque refresh token kept on the server.",
             body=stateful,
             check=[("Why is a JWT a poor choice for the browser's session cookie?", "It is large, readable by anyone who holds it, and stays valid until it expires, so sign-out cannot end it. A random id does none of that."),
                    ("The Orders API accepts any valid token from the provider. What is missing?", "The audience check. A token issued for another service, perhaps a weaker one, would be accepted.")]),
        dict(id="drills", nav="Failure drills", title="Failure drills",
             gist="Six ways sessions go wrong: a stolen refresh token, two tabs that look like a theft, a sign-out that leaves the provider session open, a removed admin whose token still says admin, a session id chosen by the attacker, and one server with a fast clock.",
             body=drills,
             check=[("Customers who keep many tabs open are being signed out several times a day. Which drill, and which fix?", "Drill 2: concurrent refreshes look like reuse. Refresh in one place under a lock, or allow a short grace period for immediate repeats."),
                    ("After sign-out on a shared computer, the next person signs in as the previous customer without a password. What did sign-out miss?", "The provider session. Sign-out must also send the browser to the provider's sign-out endpoint.")]),
        dict(id="revocation", nav="Revocation", title="Taking access back: the hard problem",
             gist="A token nobody checks cannot be taken back, so revocation means buying back some checking. Revoking refresh tokens stops renewals; a user version in every token, checked with a short cache, ends all older tokens within seconds; dangerous actions check permissions live. Choose the mechanism per event.",
             body=revocation,
             check=[("Why is a user version cheaper than a deny list of tokens?", "It is one number per user, cached, and one bump ends every older token. A deny list needs an entry for each token and a lookup of each one."),
                    ("A signing key has leaked. What is the only complete fix, and its cost?", "Rotate the key at once. Every token signed with it stops working, so every user signs in again.")]),
        dict(id="numbers", nav="Numbers", title="Lifetimes, worked out",
             gist="Each lifetime follows from what it protects: ten-minute access tokens bound how long a revoked user keeps going, fourteen idle days keep returning shoppers signed in, and a recent sign-in guards risky actions. Shorter access tokens multiply refresh traffic. Rotate signing keys in steps so both keys are published for a while.",
             body=numbers,
             check=[("Halving the access-token lifetime from 10 to 5 minutes: what does it cost, and what does it buy if user versions are already in place?", "It doubles refresh traffic to the provider. It buys little: the user version already ends revoked tokens within 30 seconds."),
                    ("Why publish the new signing key a day before using it?", "APIs cache the key set. They must have the new key before any token signed with it arrives.")]),
        dict(id="frontdoor", nav="Front door", title="The front door: login and recovery",
             gist="Stolen passwords from other sites are tried against every login page, so limit attempts per account, per address and on the overall failure rate, refuse leaked passwords, and offer passkeys. The slow hash needs a cap of its own. Account recovery is part of sign-in and must be as strong.",
             body=frontdoor,
             check=[("Why hash a dummy value when the email address is unknown?", "So the answer takes the same time as a wrong password, and the form cannot be used to discover which emails have accounts."),
                    ("A reset link is valid for 7 days and can be used repeatedly. Name two problems.", "Anyone who sees the email later, or finds it in a forwarded thread, can take the account; and it remains usable after the customer has reset their password.")]),
        dict(id="running", nav="Running it", title="Running it",
             gist="Graph sign-in success, refresh failures and token rejections, each split by reason, so a key problem, a fast clock and a refresh race look different. Keep an audit log of every security event. Redact credentials from logs and keep tokens out of URLs.",
             body=running,
             check=[("Token rejections with reason “signature” jump after a deploy. Likely cause?", "A signing-key change: tokens signed with a key the APIs have not fetched, or the old key removed too early."),
                    ("Why should log redaction live in the logging library and not in each service?", "One missed service is enough to leak tokens, and a shared library is tested once and applies everywhere.")]),
        dict(id="testing", nav="Testing", title="Testing it",
             gist="Write the drills as short tests: expiry with leeway, wrong audience, unknown key, refresh reuse with and without the grace period, sign-out, a new session id at sign-in, password change ending other devices, CSRF. Check the real cookie flags in a browser, and keep the provider's settings under review.",
             body=testing,
             check=[("All unit tests pass, but the session cookie arrives without HttpOnly. How?", "Something between the code and the browser changed it: a proxy or framework setting. Only a test through a real browser sees the cookie as stored."),
                    ("Why export the identity provider's settings into the repository?", "Lifetimes and rotation rules are security decisions. Kept as files, changes to them are reviewed like code.")]),
        dict(id="tools", nav="Tools & lab", title="Build or buy, a lab and the checklist",
             gist="Buy the provider and the client library; keep your session, CSRF defences, revocation checks and permissions, because only your code can do them. The lab adds “sign out of all devices” and admin removal within a minute, and the checklist turns the deep dive into review questions.",
             body=tools),
    ],
    sources="RFC 6749 (OAuth 2.0), RFC 7636 (PKCE) and the OAuth 2.1 draft. RFC 9700, “Best Current Practice for OAuth 2.0 Security” (2025). The IETF draft “OAuth 2.0 for Browser-Based Applications”. OpenID Connect Core, RP-Initiated Logout and Back-Channel Logout. OWASP Cheat Sheets on Session Management, Authentication, Credential Stuffing Prevention and Forgot Password. NIST SP 800-63B, Digital Identity Guidelines: Authentication.",
)
