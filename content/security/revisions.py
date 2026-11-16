# Revisions to Vol. 5 (November 2026): one situational quiz question and a “try it” per note.
# Every try it is for your own code or a local lab you own. Merged by scripts/build_notes.py (load_content).

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; related notes are links now")

REVISIONS = {
    "zero-trust": dict(
        quiz_add=[("An attacker phished a support agent's VPN password and then read the billing database, because “inside the network” was trusted. Which three changes would have stopped them at different points?",
                   "Phishing-resistant MFA (passkeys) and a device check on sign-in; per-resource policy so a support role can't reach the billing database at all; and service-to-service identity (mTLS) on the database, so network position alone grants nothing.")],
        try_it="List every internal service you can reach from your laptop on the office network or VPN without signing in again. For one of them, write down what identity, device and policy check it should require, and turn that into a ticket.",
    ),
    "least-privilege": dict(
        quiz_add=[("A reporting job runs with the database owner role “because it was easier”. A bug in the job runs DELETE without WHERE on the orders table. What should the job's role have been?",
                   "A role that can only SELECT from the tables and views the report reads, with its own login. The faulty DELETE would have failed with “permission denied” instead of removing orders.")],
        try_it="Pick one service account or API key your team uses. List what it is allowed to do, then check its last 90 days of activity (cloud access logs or pg_stat_statements). Write a narrower policy with only the actions it used, and test the service with it in a non-production environment.",
    ),
    "oauth-pkce": dict(
        quiz_add=[("A mobile app asks users for their bank login and stores the password to fetch transactions. The bank now offers OAuth. What changes for the user and for your app?",
                   "The user signs in on the bank's own page and approves a narrow scope (read transactions). Your app uses the authorization code flow with PKCE, gets tokens, never sees the password, and the user can revoke access at the bank.")],
        try_it="Run a local identity provider (Keycloak in Docker) and sign in to a small app with the authorization code flow and PKCE. Capture the authorization code from the redirect and try to exchange it without the code_verifier, and read the error.",
    ),
    "short-lived-tokens": dict(
        quiz_add=[("A deploy key with full cloud admin rights has been stored in CI secrets since 2022 and was copied into three repositories. What do you replace it with?",
                   "Federated workload identity (OIDC from the CI provider to the cloud), so each run gets a short-lived credential for one role scoped to one repository and branch. Then revoke the old key, and check the audit logs for its past use.")],
        try_it="Change one CI pipeline that deploys with a stored cloud key to use OIDC federation (GitHub Actions to AWS, GCP or Azure). Restrict the role to one repository and branch, delete the stored key, and run the deploy.",
    ),
    "secrets-management": dict(
        quiz_add=[("A developer pasted a production database password into the team chat to help a colleague. What do you do in the first hour, and what stops it happening again?",
                   "Rotate the password now (treat it as leaked; chat history is copied and backed up), check the database logs for unusual access, and remove the message. Then give developers a secrets manager with access by role, so nobody needs to pass passwords around.")],
        try_it="Run gitleaks or trufflehog over your repository's full history. For each finding, decide whether it is live, rotate the live ones, and add the scanner as a pre-commit hook and a CI step.",
    ),
    "envelope-encryption": dict(
        quiz_add=[("A customer asks you to delete all their uploaded documents, but copies exist in backups you can't edit for 35 days. Their documents are encrypted with a per-customer data key. What can you do?",
                   "Crypto-shredding: delete the customer's wrapped data key. The backed-up documents become unreadable ciphertext, and the backups expire later on their own schedule.")],
        try_it="With a local KMS emulator (LocalStack) or a key in a file standing in for one, encrypt three files with their own data keys, store the wrapped keys beside them, and decrypt one. Then rotate the master key and see which files you had to re-encrypt.",
    ),
    "password-hashing": dict(
        quiz_add=[("You inherit a user table with unsalted SHA-1 password hashes. You can't ask every user to reset at once. How do you move to Argon2id?",
                   "Wrap the old hashes now: store Argon2id(sha1_hash) for every user, so the table is protected today. On each successful sign-in, re-hash the plain password with Argon2id directly and mark the row upgraded.")],
        try_it="Hash the same password with SHA-256, bcrypt and Argon2id in a small script and time 1,000 of each. Then tune Argon2id's memory and time cost until one hash takes about 50 ms on your server, and write down the parameters.",
    ),
    "input-validation": dict(
        quiz_add=[("A PATCH /users/me endpoint passes the request body straight to the ORM's update. A user sends {\"role\": \"admin\"} and becomes an admin. What do you change?",
                   "Validate the body against an allow-list schema of the fields a user may change (name, avatar) and drop or reject everything else. Role changes go through a separate, authorised admin endpoint.")],
        try_it="Pick one endpoint in your app that accepts JSON and add a Zod, Pydantic or JSON Schema check with exact types, lengths and no unknown fields. Send ten malformed requests (wrong types, extra fields, huge strings) and check each gets a clear 400.",
    ),
    "parameterized-queries": dict(
        quiz_add=[("A search endpoint lets users sort by any column: ORDER BY ${req.query.sort}. Placeholders can't be used for column names. How do you make it safe?",
                   "Map the input to an allow-list of known column names (for example {\"date\": \"created_at\", \"price\": \"price\"}) and reject anything else. Only values go through placeholders; identifiers come from your own list.")],
        try_it="In a local test app (never someone else's system), write a login query by string concatenation and bypass it with ' OR '1'='1. Rewrite it with placeholders and repeat the input. Then search your own codebase for queries built with + or template strings.",
    ),
    "output-encoding": dict(
        quiz_add=[("Product wants users to write comments with bold, links and lists. A developer plans to render them with dangerouslySetInnerHTML. What do you do instead?",
                   "Accept Markdown (or a small set of tags), convert it to HTML on the server and sanitise it with an allow-list (DOMPurify or similar), strip javascript: links, and keep a strict nonce-based CSP as the second layer.")],
        try_it="In a local copy of your app, put <img src=x onerror=alert(1)> into every text field and see which pages show an alert. Fix any you find by removing raw HTML rendering, then add a Content-Security-Policy header in report-only mode and read the reports.",
    ),
    "csrf-protection": dict(
        quiz_add=[("Your app moved from a cookie session to bearer tokens in localStorage for the API, but the admin panel still uses a session cookie and has a POST /users/:id/delete form. Which part needs CSRF protection?",
                   "The admin panel: the browser sends its cookie automatically with a cross-site form post. Use SameSite=Lax or Strict cookies and a CSRF token on every state-changing request. The bearer-token API isn't sent automatically, so it isn't open to CSRF in the same way.")],
        try_it="In your local app, write an HTML page on another port with a hidden form that posts to a state-changing endpoint, and open it while signed in. See whether the action happens. Then set SameSite on the session cookie and add a CSRF token, and try again.",
    ),
    "threat-modeling": dict(
        quiz_add=[("The team will add a feature where customers upload CSV files that are processed overnight. Release is in three weeks. What does a one-hour threat-modelling session produce?",
                   "A data-flow sketch with trust boundaries (browser to API, API to storage, worker to database), a STRIDE pass on each boundary (huge files, formula injection, other tenants' files, a worker with too many rights), and a short list of mitigations with owners as tickets.")],
        try_it="Draw the data flow of one feature you're building on one page, mark the trust boundaries, and spend 30 minutes asking the STRIDE questions at each one. Turn the top three threats into tickets with a test for each.",
    ),
    "audit-logging": dict(
        quiz_add=[("A customer says an employee exported their data. Your logs say “export completed” with a timestamp, and the log store is editable by the same admins. What was missing?",
                   "Who did it, for which customer, from where, and whether it succeeded, in a structured event; and a separate, append-only store that app admins can't change. Without both, you can't answer the customer or prove the log wasn't edited.")],
        try_it="List the ten most sensitive actions in your app (exports, role changes, deletes, sign-ins). Check which already write an audit event with actor, action, target, result, time and source IP. Add the missing ones and send them to a store the app can't edit.",
    ),
    "supply-chain": dict(
        quiz_add=[("A popular package you use transitively publishes a malicious version, and your Docker builds run npm install without a lockfile. How many of your services are affected, and what would have limited it?",
                   "Every service built since the release could have pulled it, and you can't easily tell which. A committed lockfile with integrity hashes and npm ci, updates through reviewed automated pull requests, and an SBOM per image would have limited and shown the impact.")],
        try_it="Generate an SBOM for one of your images or projects with Syft and scan it with Grype or osv-scanner. Pin your CI actions by commit SHA, turn on Dependabot or Renovate, and check that builds use the lockfile only.",
    ),
    "defense-in-depth": dict(
        quiz_add=[("After an incident, management proposes buying a web application firewall “so we don't need to fix the injection bugs”. What do you answer?",
                   "A WAF is one useful layer, but it can be bypassed and misconfigured. Fix the bugs with parameterized queries and validation, keep the WAF as an extra layer, and add monitoring so a bypass is noticed. Layers are for when one fails, not instead of one.")],
        try_it="Take one sensitive feature (password reset, file download) and list each layer that protects it: edge, identity, input handling, authorisation, encryption, logging. For each layer, write what failure it catches. Find the place where one mistake would be enough to cause harm.",
    ),
}

for _rev in REVISIONS.values():
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question and a try it"))
