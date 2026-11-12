# Vol. 5 · Secrets & data: Secrets Management, Envelope Encryption, Password Hashing.

# ------------------------------------------------------------------ 05 Secrets Management
sm_problem = Doodle(760, 260, "Doodle of a database password written in a config file, committed to git, copied into a dot env file shared over chat, and pasted into a CI variable. It has never been changed in three years. Bots scan public repositories and find committed secrets within minutes.",
                    "One password in code, chat, .env files and CI. Never rotated. Bots find it in minutes.")
sm_problem.box(20, 30, 300, 60, "DB_PASS=hunter2", "pink", stroke="red", size=18)
for i, t in enumerate(["config.ts (git)", ".env in chat", "CI variable", "old laptop"]):
    sm_problem.arrow(170, 96, 60 + i * 180, 160)
    sm_problem.box(10 + i * 180, 164, 160, 44, t, "paper", size=15)
sm_problem.note(560, 50, "unchanged since 2023", "red")
sm_problem.note(560, 80, "public repo? bots: 4 min", "red")
sm_problem.note(380, 242, "who has it? nobody knows", "red")

sm_analogy = Doodle(760, 250, "Doodle of a bank safe-deposit box room. Keys aren't left under doormats: each valuable is in a box in the vault, you sign in to open it, every visit is logged, and the bank can change the locks without you rewriting your house.",
                    "A bank vault: valuables in boxes, every visit signed and logged, locks changed on schedule.")
sm_analogy.icon("vault", 40, 50, 2.2, fill="y")
sm_analogy.note(110, 210, "the vault")
sm_analogy.note(330, 70, "✗ key under the doormat", "red", anchor="start")
sm_analogy.note(330, 120, "✓ sign in to open a box", "green", anchor="start")
sm_analogy.note(330, 160, "✓ every visit logged", "green", anchor="start")
sm_analogy.note(330, 200, "✓ locks changed on schedule", "green", anchor="start")

sm_how = Doodle(760, 290, "Secrets management flow. The app starts with no secrets in code or image. It authenticates to the vault with its workload identity, gets the database password at runtime, and keeps it in memory. The vault logs the access and rotates the password every thirty days, or issues a dynamic credential that expires in one hour. A secret scanner in CI blocks commits that contain keys.",
                "Apps fetch secrets at runtime with their own identity; the vault logs, rotates and expires them. Scanners block leaks in code.")
sm_how.box(20, 100, 160, 80, "app", "blue", sub="no secrets baked in")
sm_how.arrow(186, 120, 330, 100, label="① I am svc-billing", lx=258, ly=92)
sm_how.icon("vault", 340, 60, 1.6, fill="y")
sm_how.arrow(330, 160, 186, 160, color="green", label="② db creds · 1 h", lx=258, ly=184)
sm_how.note(540, 80, "logs every read", "pen", anchor="start")
sm_how.note(540, 110, "rotates every 30 days", "pen", anchor="start")
sm_how.note(540, 140, "or dynamic, per app", "pen", anchor="start")
sm_how.box(20, 230, 380, 50, "CI: secret scanner blocks commits", "green", size=15)

SECRETS = dict(
    slug="secrets-management",
    kicker="a.k.a. “the bank vault”",
    tldr="Keep API keys, passwords and certificates <b>out of code, images and chat</b>. Store them in a <b>secrets manager</b>, let each app <b>fetch them at runtime with its own identity</b>, <b>log every read</b>, and <b>rotate</b> them automatically (or use <b>dynamic credentials</b> that expire). Add <b>secret scanning</b> so a key that slips into a commit is blocked or revoked within minutes.",
    chips=[("Family", "secrets"), ("Tools", "Vault, AWS/GCP/Azure secret managers, Doppler, 1Password"), ("Guards", "gitleaks, GitHub push protection"), ("Pairs with", "least privilege, short-lived tokens")],
    problem="""  <p class="lead">Secrets spread. A password starts in a config file, then lands in <span class="hl-pink">git history, chat, .env files and CI variables</span>. It never changes because nobody knows what would break, and leaked keys are found by bots within minutes.</p>
  <ul>
    <li>Deleting the line doesn't delete it from git history.</li>
    <li>Everyone who ever cloned the repo has the production password.</li>
    <li>Rotating means a scary, manual, all-hands change.</li>
  </ul>""",
    problem_figs=[sm_problem],
    analogy_side="the bank vault",
    analogy="""  <p>You don't leave your valuables under the doormat. A bank keeps them in a <b>vault</b>: you <b>prove who you are</b> to open your box, every visit is <b>logged</b>, and the bank can <b>change the locks</b> on a schedule without you rebuilding your house.</p>
  <ul>
    <li>The vault is the <b>secrets manager</b>.</li>
    <li>Proving who you are is the app's <b>workload identity</b>.</li>
    <li>Changing locks is <b>rotation</b>.</li>
  </ul>""",
    analogy_figs=[sm_analogy],
    map=[("Key under the doormat", "A password in code, .env or chat"),
         ("The bank vault", "A secrets manager"),
         ("Showing ID to open your box", "App authenticates with its workload identity"),
         ("The visitor log", "Audit log of every secret read"),
         ("Changing the locks", "Automatic rotation or dynamic credentials")],
    how_side="fetch at runtime, log, rotate",
    how="""  <p>The best secret is one nobody ever sees: <b>dynamic credentials</b> created per app, per hour, and destroyed automatically.</p>""",
    how_figs=[sm_how],
    steps=[("Find what you have", "Scan repos and history (gitleaks, trufflehog); list every secret and who uses it."),
           ("Move them into a manager", "One path per app and environment (<code>prod/billing/db</code>)."),
           ("Fetch at runtime", "The app authenticates with its identity (IAM role, Kubernetes service account) and reads only its own secrets."),
           ("Rotate automatically", "Scheduled rotation, or dynamic credentials with short leases."),
           ("Block new leaks", "Pre-commit hooks and push protection; revoke immediately if one slips through."),
           ("Revoke on leak", "Treat a committed secret as public: rotate first, then clean history.")],
    vocab=[("Secret", "Anything that grants access: keys, passwords, tokens, certificates."),
           ("Secrets manager", "A service that stores, controls and audits secrets."),
           ("Rotation", "Replacing a secret with a new one on a schedule."),
           ("Dynamic secret", "A credential created on demand with a short lease."),
           ("Secret sprawl", "Copies of a secret spreading across systems."),
           ("Push protection", "Blocking a push that contains a known secret format.")],
    code=dict(file="db.ts", note="AWS Secrets Manager", src="""
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

// the pod's IAM role allows reading ONLY prod/billing/db
const sm = new SecretsManagerClient({});

async function dbConfig() {
  const { SecretString } = await sm.send(
    new GetSecretValueCommand({ SecretId: "prod/billing/db" }));
  const { username, password, host } = JSON.parse(SecretString!);
  return { user: username, password, host, ssl: true };
}
// rotation is configured on the secret (every 30 days);
// the pool re-reads it on auth failure, so rotation needs no deploy

// .gitleaks.toml in CI + pre-commit: block anything that looks like a key
"""),
    tools="tools: HashiCorp Vault / OpenBao (dynamic secrets), AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Doppler, 1Password Secrets Automation, SOPS for encrypted files, External Secrets Operator (Kubernetes), gitleaks, trufflehog, GitHub secret scanning.",
    gains=["<b>No secrets in code</b>, images or chat.",
           "<b>Every access logged</b>.",
           "<b>Rotation without drama</b>.",
           "<b>Leaks caught early</b> by scanners."],
    losses=["<b>A critical dependency</b>: if the manager is down, apps can't start.",
            "<b>Setup and migration effort</b>.",
            "<b>Bootstrapping</b>: the app still needs an identity to log in.",
            "<b>Cost</b> per secret and per API call."],
    baseline="Each line compares <b>secrets in config files, env files and CI variables</b> to a <b>secrets manager with runtime fetch, rotation and scanning</b>.",
    ratings=[(3, 3, "One more service, but one clear place for secrets."),
             (3, 4, "Developers stop passing passwords around."),
             (1, 5, "Secrets leave code, chat and laptops."),
             (3, 4, "Audit trails show who read what."),
             (4, 3, "Apps depend on the manager at start-up; cache carefully."),
             (1, 4, "Per-app paths and short leases limit leaks."),
             (1, 5, "Every read is logged."),
             (4, 3, "Service fees and setup time."),
             (3, 4, "SDKs and operators make runtime fetch easy.")],
    pitfalls=[("Deleting instead of rotating", "The committed key is removed from the file, but still valid and in history.", "rotate immediately; then clean history."),
              ("One master secret for everything", "Every app reads every secret.", "per-app paths and policies."),
              ("Secrets in Docker images", "Baked in at build time; anyone with the image has them.", "inject at runtime."),
              ("Logging secrets", "A debug log prints the config object.", "redact secrets in logs and error reports.")],
    use=["Every production credential: databases, APIs, signing keys.",
         "CI/CD credentials (better: short-lived OIDC).",
         "Certificates and encryption keys."],
    skip=["Truly public values (publishable keys, feature flags) don't need a vault.",
          "Local dev can use dummy values."],
    related=["<b>Least privilege</b>", "<b>Short-lived tokens</b>", "<b>Envelope encryption</b>", "<b>Audit logging</b>"],
    quiz=[("A secret was committed to git. What's the first step?", "Rotate (revoke) it immediately; removing it from the file doesn't make it safe."),
          ("How does an app get secrets without a stored password?", "It authenticates to the manager with its workload identity (IAM role, service account)."),
          ("What's a dynamic secret?", "A credential created on demand for one app, with a short lease, then destroyed automatically."),
          ("Why not bake secrets into Docker images?", "Anyone who can pull the image can read them, and rotation requires a rebuild.")],
    remember="No keys under the <span class=\"hl\">doormat</span>. Sign in at the <span class=\"hl\">vault</span>, and change the <span class=\"hl\">locks</span> often.",
    sources=["OWASP, “Secrets Management Cheat Sheet”.",
             "HashiCorp Vault docs, “Dynamic Secrets”.",
             "GitHub docs, “About secret scanning” and “Push protection”.",
             "GitGuardian, “The State of Secrets Sprawl” (annual report)."],
)

# ------------------------------------------------------------------ 06 Envelope Encryption
ee_problem = Doodle(760, 250, "Doodle of an app that encrypts every customer file with one AES key stored in its config. The key sits next to the data on the same server. Anyone who steals the server gets both. Rotating the key means re-encrypting ten terabytes.",
                    "One encryption key, in the config, next to the data. Steal the server, get both.")
ee_problem.db(110, 80, "10 TB files", w=120, h=70)
ee_problem.icon("key", 280, 90, 1.2, fill="pink")
ee_problem.note(320, 180, "AES key in config.ts", "red")
ee_problem.raw('<rect class="d d-dash d-red" x="20" y="40" width="420" height="170" rx="8" style="fill:none"/>')
ee_problem.note(230, 236, "same server", "red")
ee_problem.note(600, 80, "server stolen →", "red")
ee_problem.note(600, 106, "data + key", "red")
ee_problem.note(600, 160, "rotate key →", "red")
ee_problem.note(600, 186, "re-encrypt 10 TB", "red")

ee_analogy = Doodle(760, 250, "Doodle of a hotel safe inside each room. Your valuables are locked with your own small safe code. The codes themselves are kept in the hotel's master vault, which never leaves the building and only the manager can open. Changing the master vault lock doesn't require opening every room safe.",
                    "Room safes with their own codes; the codes live in a master vault that never leaves the building.")
for i in range(3):
    ee_analogy.icon("lock", 40 + i * 90, 60, 1.0, fill="y")
ee_analogy.note(170, 160, "room safes (data keys)", "pen")
ee_analogy.arrow(320, 100, 450, 100, dash=True, label="codes kept in", lx=385, ly=86)
ee_analogy.icon("vault", 470, 50, 1.6, fill="green")
ee_analogy.note(530, 190, "master vault (KMS)", "green")
ee_analogy.note(530, 216, "never leaves the building", "pen")

ee_how = Doodle(760, 300, "Envelope encryption. For each file the app asks the key management service for a new data key. The service returns the plaintext data key and the same key encrypted under the master key. The app encrypts the file with the plaintext data key, discards it, and stores the encrypted data key next to the file. To read, the app sends the encrypted data key to the service, which decrypts it if the app is allowed and logs the request.",
                "A fresh data key per file; store it wrapped by a master key that never leaves the KMS.")
ee_how.box(20, 40, 150, 70, "app", "blue")
ee_how.arrow(176, 60, 456, 60, label="① GenerateDataKey", lx=316, ly=46)
ee_how.box(462, 30, 180, 90, "KMS", "y", sub="master key stays here")
ee_how.arrow(456, 100, 176, 100, color="green", label="② key + wrapped key", lx=316, ly=124)
ee_how.box(20, 170, 300, 90, None, "paper")
ee_how.text(36, 200, "file.enc  (AES-256-GCM)", "t", anchor="start", size=16)
ee_how.text(36, 230, "+ wrapped data key", "t", anchor="start", size=16)
ee_how.note(170, 286, "③ encrypt, discard plaintext key", "pen")
ee_how.note(560, 200, "④ read: KMS unwraps", "green")
ee_how.note(560, 226, "if allowed · logged", "green")

ENVELOPE = dict(
    slug="envelope-encryption",
    kicker="a.k.a. “room safes and a master vault”",
    tldr="Encrypt each piece of data with its own <b>data key</b>, then encrypt (“wrap”) that data key with a <b>master key</b> that lives in a <b>KMS or HSM</b> and <b>never leaves it</b>. Store the wrapped key next to the data. Stealing the disk gets <b>ciphertext and wrapped keys only</b>; every unwrap is <b>authorised and logged</b>; and rotating the master key means <b>re-wrapping small keys</b>, not re-encrypting terabytes.",
    chips=[("Family", "encryption at rest"), ("Services", "AWS KMS, Google Cloud KMS, Azure Key Vault, HSMs"), ("Algorithms", "AES-256-GCM data keys"), ("Pairs with", "secrets management, least privilege")],
    problem="""  <p class="lead">“We encrypt everything” often means one key, <span class="hl-pink">stored next to the data</span>. Whoever gets the server or the backup gets the key too, and changing the key means re-encrypting everything.</p>
  <ul>
    <li>The AES key sits in a config file on the same machine.</li>
    <li>Backups contain both encrypted data and the key.</li>
    <li>Nobody can tell who decrypted what.</li>
  </ul>""",
    problem_figs=[ee_problem],
    analogy_side="room safes and a master vault",
    analogy="""  <p>A hotel room has a <b>small safe</b> with its own code. The hotel doesn't write codes on the doors; they're kept in a <b>master vault</b> that <b>never leaves the building</b>, and only authorised staff can look one up, with a log entry.</p>
  <ul>
    <li>Each room safe's code is a <b>data key</b>.</li>
    <li>The master vault is the <b>KMS</b>.</li>
    <li>Changing the vault's lock doesn't mean opening every room safe: <b>cheap master-key rotation</b>.</li>
  </ul>""",
    analogy_figs=[ee_analogy],
    map=[("A room safe's code", "A data key (one per file or record)"),
         ("Codes kept in the master vault", "Data keys stored wrapped by the master key"),
         ("Vault never leaves the building", "Master key never leaves the KMS/HSM"),
         ("Staff log to look up a code", "IAM-checked, logged Decrypt calls"),
         ("Re-keying the vault, not the rooms", "Rotating the master key re-wraps small keys")],
    how_side="wrap the key that wraps the data",
    how="""  <p>Big data is encrypted locally and fast with the data key; only the tiny data key travels to the KMS. That's how cloud storage encryption works under the hood.</p>""",
    how_figs=[ee_how],
    steps=[("Create a master key in KMS", "Non-exportable, with a key policy naming who may encrypt and decrypt."),
           ("Generate a data key per object", "<code>GenerateDataKey</code> returns plaintext + wrapped copies."),
           ("Encrypt locally", "AES-256-GCM with a fresh nonce; then wipe the plaintext key from memory."),
           ("Store the wrapped key with the data", "In the file header or a column next to the ciphertext."),
           ("Decrypt via KMS", "Send the wrapped key to <code>Decrypt</code>; permission checked, call logged."),
           ("Rotate and shred", "Rotate master keys yearly; destroying a tenant's key makes their data unreadable (crypto-shredding).")],
    vocab=[("Data key (DEK)", "Key that encrypts the actual data."),
           ("Key-encryption key (KEK)", "Key that encrypts other keys."),
           ("KMS", "Key Management Service holding master keys."),
           ("HSM", "Tamper-resistant hardware that holds keys."),
           ("Wrapping", "Encrypting a key with another key."),
           ("Crypto-shredding", "Deleting data by destroying its key.")],
    code=dict(file="vault-files.ts", note="AWS KMS + Node crypto", src="""
import { KMSClient, GenerateDataKeyCommand, DecryptCommand } from "@aws-sdk/client-kms";
import { createCipheriv, randomBytes } from "node:crypto";

const kms = new KMSClient({});

export async function encryptFile(plain: Buffer, tenantKeyId: string) {
  const { Plaintext, CiphertextBlob } = await kms.send(
    new GenerateDataKeyCommand({ KeyId: tenantKeyId, KeySpec: "AES_256" }));
  const iv = randomBytes(12);
  const c = createCipheriv("aes-256-gcm", Plaintext!, iv);
  const body = Buffer.concat([c.update(plain), c.final()]);
  Plaintext!.fill(0);                                  // drop the plaintext key
  return { wrappedKey: CiphertextBlob, iv, tag: c.getAuthTag(), body };
}

export async function unwrap(wrappedKey: Uint8Array) {
  return (await kms.send(new DecryptCommand({ CiphertextBlob: wrappedKey }))).Plaintext!;
}
"""),
    tools="tools: AWS KMS + Encryption SDK, Google Cloud KMS + Tink, Azure Key Vault, HashiCorp Vault Transit, cloud HSMs, database TDE and column encryption that use the same model.",
    gains=["<b>Keys never sit next to data</b>.",
           "<b>Every decrypt is authorised and logged</b>.",
           "<b>Cheap master-key rotation</b>.",
           "<b>Per-tenant keys</b> and crypto-shredding."],
    losses=["<b>KMS calls</b> add latency and cost.",
            "<b>KMS availability</b> becomes critical.",
            "<b>Crypto details</b> (nonces, modes) are easy to get wrong by hand.",
            "<b>Doesn't protect data in use</b> by a compromised app."],
    baseline="Each line compares <b>one static encryption key in app config</b> to <b>envelope encryption with per-object data keys and a KMS master key</b>.",
    ratings=[(3, 2, "Two kinds of keys and a KMS to understand."),
             (3, 3, "Invisible to users."),
             (2, 5, "Stolen disks and backups hold only ciphertext."),
             (3, 4, "Authenticated encryption (GCM) detects tampering."),
             (4, 3, "Reads depend on KMS; cache data keys briefly."),
             (1, 5, "Per-object and per-tenant keys limit exposure."),
             (1, 5, "KMS logs every decrypt with the caller."),
             (4, 3, "KMS fees per key and per call."),
             (2, 4, "SDKs (Encryption SDK, Tink) hide the hard parts.")],
    pitfalls=[("Rolling your own crypto", "Reused nonces, ECB mode, no auth tag.", "use the Encryption SDK or Tink."),
              ("Keeping plaintext data keys", "Cached forever in memory or logged.", "wipe after use; short, bounded caches only."),
              ("Over-broad key policies", "Every role can call Decrypt on every key.", "least privilege on key policies; per-tenant keys."),
              ("Calling KMS per tiny record", "Thousands of KMS calls per second.", "data-key caching with limits, or encrypt batches.")],
    use=["Files and blobs with sensitive data.",
         "Per-tenant encryption and crypto-shredding.",
         "Field-level encryption of personal data."],
    skip=["When managed storage encryption already meets your needs.",
          "Data that's public anyway."],
    related=["<b>Secrets management</b>", "<b>Least privilege</b>", "<b>Multitenancy</b> (Vol. 3)", "<b>Audit logging</b>"],
    quiz=[("Why not store the encryption key next to the data?", "Whoever steals the data (server, backup) gets the key too."),
          ("What does the KMS return from GenerateDataKey?", "A plaintext data key to use now, and the same key encrypted under the master key to store."),
          ("Why is master-key rotation cheap?", "Only the small wrapped data keys need re-wrapping, not the data itself."),
          ("What is crypto-shredding?", "Making data unreadable by destroying the key that protects it.")],
    remember="A <span class=\"hl\">safe</span> per room, codes in the <span class=\"hl\">master vault</span>, and the vault never <span class=\"hl\">leaves</span>.",
    sources=["AWS docs, “Envelope encryption” (AWS KMS concepts).",
             "Google Cloud docs, “Envelope encryption”.",
             "NIST SP 800-57, “Recommendation for Key Management”.",
             "Google Tink documentation."],
)

# ------------------------------------------------------------------ 07 Password Hashing
ph_problem = Doodle(760, 250, "Doodle of a users table that stores passwords as plain text in one version and as unsalted MD5 in another. After a breach, plain passwords are read directly, and the MD5 hashes are reversed in seconds with lookup tables because many users share the same password.",
                    "Plain text or fast, unsalted hashes: a leaked table becomes a list of real passwords.")
ph_problem.table(20, 30, "users (plain)", ["ana · Summer2024!", "ben · hunter2"], w=230, fill="pink", stroke="red")
ph_problem.table(300, 30, "users (md5)", ["ana · 5f4dcc3b5aa7…", "cho · 5f4dcc3b5aa7…"], w=240, fill="pink", stroke="red")
ph_problem.note(420, 150, "same hash = same password", "red")
ph_problem.note(420, 180, "lookup table: 0.2 s", "red")
ph_problem.note(130, 150, "read directly", "red")
ph_problem.note(380, 236, "and reused on their email, bank…", "red")

ph_analogy = Doodle(760, 250, "Doodle of a meat grinder turning a steak into mince. You can check if a new steak would make the same mince, but you can't turn mince back into steak. A pinch of a unique spice per steak makes identical steaks give different mince, and a deliberately slow grinder makes guessing millions of steaks impractical.",
                    "A slow grinder with a unique spice: easy to check, impossible to reverse, too slow to brute-force.")
ph_analogy.box(40, 70, 120, 70, "steak", "pink", size=18)
ph_analogy.arrow(166, 105, 280, 105, label="+ unique spice", lx=223, ly=90)
ph_analogy.icon("kitchen", 290, 70, 1.3, fill="y")
ph_analogy.arrow(390, 105, 500, 105, label="slowly…", lx=445, ly=90)
ph_analogy.box(506, 70, 120, 70, "mince", "y", size=18)
ph_analogy.note(380, 200, "mince → steak? impossible", "green")
ph_analogy.note(380, 230, "a million guesses? a million slow grinds", "green")

ph_how = Doodle(760, 280, "Password hashing with Argon2id. At sign-up, the password plus a random salt goes through a slow, memory-hard function with tuned cost parameters, producing a string that contains the algorithm, parameters, salt and hash, which is stored. At login, the same function runs with the stored salt and parameters and the results are compared in constant time. If the parameters are outdated, the hash is upgraded after a successful login.",
                "Store argon2id(password, random salt, cost). Login re-hashes and compares. Raise the cost over time.")
ph_how.box(20, 40, 160, 70, "password", "blue")
ph_how.box(20, 140, 160, 60, "random salt", "y", size=17)
ph_how.arrow(186, 75, 290, 110)
ph_how.arrow(186, 170, 290, 130)
ph_how.box(296, 70, 190, 100, "argon2id", "green", sub="64 MB · 3 passes")
ph_how.arrow(492, 120, 542, 120)
ph_how.box(548, 80, 204, 80, None, "paper")
ph_how.text(558, 112, "$argon2id$v=19$", "t", anchor="start", size=14)
ph_how.text(558, 136, "m=65536,t=3$salt$hash", "t", anchor="start", size=13)
ph_how.note(380, 240, "login: re-hash with stored salt + params, compare in constant time", "pen")

PASSWORDS = dict(
    slug="password-hashing",
    kicker="a.k.a. “the slow grinder”",
    tldr="Never store passwords, and never “encrypt” them. Store a <b>slow, salted, memory-hard hash</b>: <b>Argon2id</b> (or scrypt / bcrypt) with a <b>unique random salt</b> per user and a <b>cost</b> tuned so one hash takes tens of milliseconds. A stolen table then costs attackers <b>years</b>, not seconds. Better still, offer <b>passkeys</b> so there's no password to steal.",
    chips=[("Family", "credential storage"), ("Use", "Argon2id · scrypt · bcrypt"), ("Never", "plain text, MD5, SHA-1/256 alone, reversible encryption"), ("Pairs with", "MFA / passkeys, rate limiting")],
    problem="""  <p class="lead">Databases leak. If passwords are stored in <span class="hl-pink">plain text or fast hashes</span>, the leak becomes a list of real passwords, and people reuse them for email and banking.</p>
  <ul>
    <li>Plain text: readable immediately.</li>
    <li>MD5/SHA-256: billions of guesses per second on one GPU.</li>
    <li>No salt: identical passwords share a hash; lookup tables crack them instantly.</li>
  </ul>""",
    problem_figs=[ph_problem],
    analogy_side="the slow grinder",
    analogy="""  <p>Put a steak through a <b>grinder</b> and you get mince. You can check whether another steak makes <b>the same mince</b>, but you can never turn mince <b>back into steak</b>. Add a <b>unique pinch of spice</b> per steak so identical steaks give different mince, and use a <b>deliberately slow grinder</b> so trying a million steaks takes forever.</p>
  <ul>
    <li>Grinding is <b>hashing</b> (one-way).</li>
    <li>The spice is the <b>salt</b>.</li>
    <li>The slow grinder is the <b>work factor</b>.</li>
  </ul>""",
    analogy_figs=[ph_analogy],
    map=[("Steak → mince, one-way", "A hash function"),
         ("A unique pinch of spice", "A random salt per user"),
         ("A slow, heavy grinder", "Argon2id cost: time and memory"),
         ("Checking a new steak", "Re-hashing at login and comparing"),
         ("Buying a slower grinder later", "Re-hashing with higher cost on next login")],
    how_side="salted, slow, upgradable",
    how="""  <p>Modern hash strings carry their own algorithm, parameters and salt, so you can raise the cost later and <b>upgrade hashes as users log in</b>.</p>""",
    how_figs=[ph_how],
    steps=[("Pick Argon2id", "OWASP baseline: m=19 MiB, t=2, p=1 or stronger; bcrypt cost ≥ 10 if Argon2 isn't available."),
           ("Use a library", "It generates the salt and encodes parameters in the hash string."),
           ("Verify in constant time", "Use the library's verify function; don't compare strings yourself."),
           ("Rehash when needed", "If the stored parameters are outdated, re-hash after a successful login."),
           ("Protect the endpoint", "Rate limits, breached-password checks (k-anonymity APIs), MFA."),
           ("Offer passkeys", "WebAuthn passkeys remove shared secrets entirely.")],
    vocab=[("Hash", "One-way function from input to fixed-size output."),
           ("Salt", "Random value stored with each hash so equal passwords differ."),
           ("Work factor", "How expensive one hash is (time, memory)."),
           ("Memory-hard", "Needs lots of RAM, which slows GPU cracking."),
           ("Pepper", "An extra secret kept outside the database (optional)."),
           ("Credential stuffing", "Trying leaked passwords on other sites.")],
    code=dict(file="passwords.ts", note="@node-rs/argon2", src="""
import { hash, verify } from "@node-rs/argon2";

const PARAMS = { memoryCost: 65536, timeCost: 3, parallelism: 1 };   // ~50 ms on our servers

export async function setPassword(userId: string, password: string) {
  if (await isBreached(password)) throw new WeakPassword("found in a known breach");
  const h = await hash(password, PARAMS);         // salt generated and embedded
  await db.query("UPDATE users SET password_hash = $1 WHERE id = $2", [h, userId]);
}

export async function checkPassword(user: User, password: string) {
  const ok = await verify(user.password_hash, password);   // constant-time
  if (ok && needsRehash(user.password_hash, PARAMS)) {
    await setPassword(user.id, password);         // upgrade old hashes on login
  }
  return ok;
}
"""),
    tools="tools: Argon2 libraries (@node-rs/argon2, argon2-cffi, libsodium), bcrypt, Django/Rails/Spring/ASP.NET Identity defaults, Have I Been Pwned “Pwned Passwords” range API, WebAuthn/passkey libraries (SimpleWebAuthn).",
    gains=["<b>Leaks don't reveal passwords</b> quickly.",
           "<b>Each guess is expensive</b> for attackers.",
           "<b>Upgradable</b> as hardware gets faster.",
           "<b>Simple</b> with a good library."],
    losses=["<b>CPU and memory per login</b>.",
            "<b>Login DoS risk</b> if unthrottled.",
            "<b>Weak passwords still fall</b> eventually.",
            "<b>Doesn't stop phishing</b> (passkeys do)."],
    baseline="Each line compares <b>plain text or fast unsalted hashes</b> to <b>Argon2id with per-user salts, upgrade on login and breached-password checks</b>.",
    ratings=[(4, 4, "One library call to hash, one to verify."),
             (4, 4, "Tens of milliseconds at login; invisible."),
             (1, 4, "Leaked hashes take years to crack for decent passwords."),
             (2, 4, "Constant-time verify; no reversible storage."),
             (4, 3, "Costly hashes need rate limiting at login."),
             (1, 4, "A breach no longer exposes reused passwords."),
             (3, 3, "Neutral."),
             (4, 3, "Some extra CPU on login servers."),
             (3, 4, "Framework defaults are usually right.")],
    pitfalls=[("Encrypting passwords", "Reversible: whoever has the key has every password.", "hash, never encrypt."),
              ("Fast hashes", "SHA-256 is designed to be fast; GPUs love it.", "Argon2id, scrypt or bcrypt."),
              ("One global salt", "Equal passwords still share hashes.", "a unique random salt per hash (libraries do it)."),
              ("Never raising the cost", "2012 parameters on 2026 hardware.", "store params in the hash; rehash on login.")],
    use=["Any system that stores user passwords.",
         "API keys you only need to verify, not read (hash them too)."],
    skip=["When you can avoid passwords entirely (passkeys, SSO).",
          "Secrets you must read back (use a secrets manager instead)."],
    related=["<b>OAuth 2.0 with PKCE</b>", "<b>Secrets management</b>", "<b>Rate limiter</b> (Vol. 1)", "<b>Defence in depth</b>"],
    quiz=[("Why is SHA-256 a bad password hash?", "It's fast, so attackers can try billions of guesses per second."),
          ("What does a salt prevent?", "Identical passwords producing identical hashes, and precomputed lookup tables."),
          ("How do you upgrade old hashes?", "Store parameters in the hash and re-hash with new parameters after a successful login."),
          ("Why should passwords never be encrypted?", "Encryption is reversible; anyone with the key can recover every password.")],
    remember="<span class=\"hl\">Grind</span>, don't lock. Add a unique <span class=\"hl\">spice</span>, and use a <span class=\"hl\">slow</span> grinder.",
    sources=["OWASP, “Password Storage Cheat Sheet”.",
             "RFC 9106, “Argon2 Memory-Hard Function for Password Hashing”.",
             "NIST SP 800-63B, “Digital Identity Guidelines: Authentication”.",
             "Troy Hunt, “Pwned Passwords” k-anonymity API."],
)

NOTES = [SECRETS, ENVELOPE, PASSWORDS]
