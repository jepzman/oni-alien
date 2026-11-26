# Handbook 2 · Identity and Access in the Cloud. DRAFT outline (parts → chapters) and book metadata.
# Status: proposal for owner review (see docs/HANDOFF-handbooks.md §6). Not yet listed in
# scripts/build_handbooks.py BOOKS, so it is not built or shown on the landing page.
# When approved: add "cloud-identity" to BOOKS; a chapter is written when
# content/handbooks/cloud-identity/<nn>-<slug>.html exists; the rest show as “coming”.

BOOK = dict(
    key="cloud-identity",
    series="Jef’s Handbooks",
    no=2,
    title="Identity and Access in the Cloud",
    subtitle="From passwords to permission guardrails",
    shelf_blurb="Authentication, OAuth and SSO, IAM policies, roles, workload identity, secrets and multi-account guardrails, with AWS as the main provider and Azure and Google Cloud compared.",
    audience=("Developers, operations people and new cloud engineers who copy IAM policies from the internet and "
              "hope. You can log in to a cloud console and run a CLI; by the end you can design least-privilege "
              "access for people and workloads on AWS, debug any “access denied”, and read the same setup on "
              "Azure or Google Cloud."),
    promise=("Twenty-five chapters in six parts. Part I is provider-neutral: how proving who you are and deciding "
             "what you may do actually work. Part II takes AWS IAM apart, down to how a single request is allowed "
             "or denied. Parts III and IV give access to people and to software, without passwords or long-lived "
             "keys. Part V scales it across many accounts, and Part VI is about running it: auditing, detection and "
             "identity as code. Every chapter ends with a lab or a design exercise and questions to check yourself. "
             "IAM itself is free, so nearly every lab costs nothing."),
    example=("The running example is <b>Larder</b>, the Amsterdam grocery-delivery company from the Practitioner’s "
             "Notebooks and Handbook 1. It begins with one AWS account its first CTO opened in 2024, shared IAM "
             "users and a deploy key with full admin. By the end, Larder has one identity per person, no "
             "long-lived keys, and guardrails across every account. You don’t need to have read the other books."),
    parts=[
        dict(no="I", title="How access works",
             blurb="Provider-neutral foundations: proving who you are, and deciding what you may do.",
             chapters=[
                 (1, "who-and-what", "Who are you, and what may you do?",
                  "Authentication and authorisation, principals and resources, and the life of one request from login to “allowed”. The mental model the book uses throughout.",
                  "identity vs authentication vs authorisation · principals · resources and actions · trust · the request lifecycle"),
                 (2, "proving-identity", "Passwords, MFA and passkeys",
                  "How people prove who they are, why passwords fail, and which second factors actually stop phishing.",
                  "password storage and hashing · TOTP · push fatigue · WebAuthn and passkeys · phishing resistance"),
                 (3, "tokens-sessions", "Sessions and tokens",
                  "What you carry after logging in: cookies, bearer tokens and JWTs, how they expire, and why revoking them is hard.",
                  "sessions and cookies · bearer tokens · JWT anatomy and signatures · expiry and refresh · revocation"),
                 (4, "oauth-oidc", "OAuth 2.0 and OpenID Connect",
                  "Delegated access and login for apps: the flows you'll meet, scopes, and ID tokens versus access tokens.",
                  "roles in OAuth · authorisation code + PKCE · client credentials · scopes · OIDC ID tokens · discovery and JWKS"),
                 (5, "saml-federation", "SAML and federation",
                  "Trusting someone else's login: identity providers, assertions, and why SAML still runs most enterprise SSO.",
                  "IdP and SP · assertions and signatures · metadata · IdP- vs SP-initiated · federation trust"),
                 (6, "access-models", "Access models: roles, attributes and relationships",
                  "Ways to write down who may do what, and the principles that keep them safe: least privilege and separation of duties.",
                  "ACLs · RBAC · ABAC · ReBAC · least privilege · separation of duties · default deny"),
             ]),
        dict(no="II", title="IAM on AWS",
             blurb="One account, understood properly: principals, policies, and how every request is decided.",
             chapters=[
                 (7, "account-root", "The AWS account and its root user",
                  "The account as a security boundary, what the root user can do that nobody else can, and locking it away. Larder finds a 2024 root access key.",
                  "accounts as boundaries · root user tasks · root MFA and no keys · account contacts · ARNs and account IDs"),
                 (8, "users-roles", "Users, groups and roles",
                  "Why IAM users are a legacy pattern, how roles and temporary credentials replace them, and what STS does when you assume a role.",
                  "IAM users and groups · roles and trust policies · AssumeRole · STS and session credentials · the credential chain"),
                 (9, "policies", "Reading and writing IAM policies",
                  "Policy JSON line by line: effects, actions, resources, conditions and variables, and how to write one that does exactly one job.",
                  "statements · actions and wildcards · resource ARNs · condition keys and operators · policy variables · managed vs inline · sample"),
                 (10, "evaluation", "How AWS decides: policy evaluation logic",
                  "Every policy type that can affect a request, and the order AWS checks them in. One flowchart you'll use for the rest of your career.",
                  "explicit deny · identity vs resource policies · permission boundaries · session policies · SCPs and RCPs · same vs cross account"),
                 (11, "access-denied", "Debugging “access denied”",
                  "A method for every permissions error: read the message, find the call in CloudTrail, work out which policy said no.",
                  "error messages and encoded reasons · CloudTrail lookup · policy simulator · Access Analyzer policy checks · lab"),
             ]),
        dict(no="III", title="Access for people",
             blurb="One identity per person, the right access for the job, and nothing left behind when they leave.",
             chapters=[
                 (12, "sso", "Single sign-on with IAM Identity Center",
                  "Connecting a company identity provider, permission sets and account assignments, and SSO from the CLI. Larder retires its shared IAM users.",
                  "external IdP · permission sets · account assignments · CLI and SDK SSO · Entra ID and Google Workspace as IdPs"),
                 (13, "lifecycle", "Joiners, movers and leavers",
                  "Automating access from HR to cloud with groups and SCIM, and access reviews that people actually do.",
                  "SCIM provisioning · group-based access · movers and privilege creep · access reviews · offboarding checklists"),
                 (14, "privileged-access", "Privileged access and break-glass",
                  "Admin rights only when needed, with approval and an audit trail, and a safe way in when SSO itself is down.",
                  "standing vs just-in-time access · approval flows · session recording · break-glass accounts · alerting on use"),
             ]),
        dict(no="IV", title="Access for software",
             blurb="Workloads, pipelines and partners: identities for things that aren't people, with no long-lived keys.",
             chapters=[
                 (15, "workload-identity", "Identities for workloads",
                  "How code on EC2, ECS and Lambda gets credentials without anyone handling a key, and the SDK credential chain that finds them.",
                  "instance profiles · IMDSv2 · ECS task roles · Lambda execution roles · Azure managed identities · GCP service accounts"),
                 (16, "kubernetes-identity", "Kubernetes and workload identity",
                  "Two permission systems in one cluster: Kubernetes RBAC for the API, and cloud roles for pods.",
                  "Kubernetes RBAC · service accounts · IRSA and EKS Pod Identity · access entries · AKS and GKE workload identity"),
                 (17, "ci-cd-oidc", "CI/CD without long-lived keys",
                  "Letting GitHub Actions deploy through OIDC federation, and the trust-policy conditions that stop other repositories doing the same. Larder deletes its deploy key.",
                  "OIDC federation · trust policy conditions on sub and aud · per-environment roles · deploy-time least privilege · lab"),
                 (18, "secrets-keys", "Secrets and encryption keys",
                  "Where secrets live, how they rotate, and how KMS key policies form a second permission system next to IAM.",
                  "Secrets Manager and Parameter Store · rotation · KMS keys and key policies · grants · envelope encryption"),
                 (19, "api-access", "Service-to-service and API access",
                  "Signed AWS requests, authorisers for your own APIs, and keys for partners that expire. Retells Larder's October 2026 security review.",
                  "SigV4 · API Gateway authorisers · Cognito and JWT validation · mTLS · partner API keys and rotation"),
             ]),
        dict(no="V", title="Many accounts",
             blurb="From one account to an organisation: guardrails, cross-account access and a data perimeter.",
             chapters=[
                 (20, "organizations", "AWS Organizations and guardrails",
                  "Why companies use many accounts, and the policies that hold for everyone in them, administrators included.",
                  "account per environment and team · OUs · SCPs · resource control policies · delegated administrators · Azure management groups and GCP org policies"),
                 (21, "cross-account", "Cross-account access and resource sharing",
                  "Roles across accounts, resource policies, and the confused deputy problem that external IDs solve.",
                  "cross-account roles · role chaining · resource-based policies · confused deputy and ExternalId · AWS RAM"),
                 (22, "data-perimeter", "Data perimeters",
                  "Making sure only your identities reach your data, and only from your networks. Picks up the endpoint policies from Handbook 1, Chapter 12.",
                  "aws:PrincipalOrgID and ResourceOrgID · VPC endpoint policies · SourceVpce · perimeter SCPs and RCPs · exceptions"),
             ]),
        dict(no="VI", title="Running it",
             blurb="Seeing who did what, catching what shouldn't happen, and changing access safely.",
             chapters=[
                 (23, "audit-detect", "Auditing and detecting misuse",
                  "An organisation-wide audit trail, finding unused and external access, and alerts for the events that matter.",
                  "CloudTrail organisation trail · Access Analyzer external and unused access · GuardDuty · credential reports · alerting"),
                 (24, "identity-as-code", "Identity as code and least privilege at scale",
                  "Managing roles, permission sets and SCPs in Terraform, generating policies from real activity, and testing them in CI.",
                  "Terraform for IAM · policy generation from CloudTrail · linting and validation · policy tests · review workflow"),
                 (25, "capstone", "Capstone: Larder's identity end to end",
                  "Put it together: people, workloads, pipelines, partners and guardrails for every Larder account, then review it against an attack.",
                  "inventory → people → workloads → guardrails → perimeter → detection → tabletop review"),
             ]),
    ],
    appendices=[
        ("A", "Policy cookbook", "Tested policies for the jobs you'll meet most: read one bucket, deploy one service, trust one repository, deny outside the org."),
        ("B", "AWS, Azure and Google Cloud translation table", "Every service and term in the book, side by side."),
        ("C", "Lab setup and safety", "A sandbox account, the CLI with SSO, budgets and alarms, and how to clean up roles and keys."),
        ("D", "Glossary", "Every key term from every chapter."),
        ("E", "Answers to the exercises", "Worked answers to every “check your understanding” question."),
    ],
)
