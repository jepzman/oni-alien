# Revisions to Vol. 6 (November 2026): one situational quiz question and a “try it” per note.
# Merged into the notes by scripts/build_notes.py (load_content).

REVISION_NOTE = ("Nov 2026", "every note gains a “what would you do?” question and a try it; related notes are links now")

REVISIONS = {
    "blue-green": dict(
        quiz_add=[("The new release renames a database column. You switch traffic to green, errors rise, and you switch back to blue, which now fails too. What went wrong, and how do you plan the next one?",
                   "Both colours share the database, and the migration broke the old version. Change the schema with expand and contract: add the new column first so both versions work, switch traffic, and remove the old column in a later release.")],
        try_it="In a local Kubernetes cluster, run two Deployments (blue and green) behind one Service, and switch traffic by changing the Service selector while curl runs in a loop. Count failed requests during the switch, and switch back.",
    ),
    "canary": dict(
        quiz_add=[("A canary at 5% shows error rate and latency equal to stable, so it goes to 100%. An hour later the payment success rate has fallen from 97% to 91%. What was missing from the analysis?",
                   "A business metric compared between canary and stable (payment success, orders per minute), not just technical signals. Add it to the analysis, and hold each step long enough to collect enough data at 5%.")],
        try_it="Use Argo Rollouts or Flagger in a local cluster to roll out a version that returns 500 for one request in ten. Set a canary step at 10% with an error-rate check, and watch it abort and shift traffic back on its own.",
    ),
    "feature-flags": dict(
        quiz_add=[("The codebase has 340 feature flags, some from 2023. Last month an old flag was toggled by mistake and switched a retired checkout flow back on. What do you put in place?",
                   "Give every flag an owner, a type (release, experiment, operational) and an expiry date; release flags are removed after launch with a ticket created when the flag is. Report stale flags weekly and fail CI on flags past their date.")],
        try_it="Put one new feature in your app behind a flag with OpenFeature (or a simple config check) that defaults to off. Turn it on for yourself only, then for 10% of users. Write the ticket to delete the flag before you merge.",
    ),
    "build-once": dict(
        quiz_add=[("A bug appears in production that you can't reproduce in staging. Each environment runs its own docker build from the same commit. What could differ, and what do you change?",
                   "Base images, dependency versions or build arguments may have changed between builds. Build one image per commit, deploy it everywhere by its digest, and give each environment only its configuration at runtime.")],
        try_it="Build your app's image twice from the same commit a day apart and compare the digests and installed package versions. Then change the pipeline to build once, push, and deploy the same digest to two environments with different config.",
    ),
    "infrastructure-as-code": dict(
        quiz_add=[("Someone changed a production security group in the console during an incident. The next Terraform apply quietly removes the change and the problem returns. How do you handle console changes from now on?",
                   "Run a scheduled plan to detect drift and alert on it. After an incident, bring any emergency change back into code through a pull request. Make console write access in production the exception (break-glass), and logged.")],
        try_it="Describe one small resource you manage by hand (a bucket, a DNS record) in Terraform or OpenTofu, import it, and run plan until it shows no changes. Change it in the console and run plan again to see the drift.",
    ),
    "gitops": dict(
        quiz_add=[("During an incident someone scales a deployment from 3 to 10 replicas with kubectl. Two minutes later it is back to 3 and the outage continues. What happened, and what is the right way?",
                   "The GitOps agent reconciled the cluster back to the state in git. Change the replica count in git (a quick, reviewed pull request), or pause auto-sync for that app during the incident and record it.")],
        try_it="Install Argo CD or Flux in a local cluster and point it at a repository with one Deployment. Change the image tag in git and watch it roll out. Then edit the Deployment with kubectl and watch the agent put it back.",
    ),
    "immutable-infrastructure": dict(
        quiz_add=[("A critical OpenSSL patch is out. Your servers are immutable images built with Packer, and SSH is disabled. Walk through how the patch reaches production.",
                   "Update the base image, rebuild the server image in the pipeline, test it, and roll it out by replacing instances a few at a time (a rolling or blue–green update). Nobody logs in; old instances are terminated.")],
        try_it="Build a small VM or container image with Packer or a Dockerfile that includes your app. Launch two instances, change one line, build a new image, and replace the instances without logging into either.",
    ),
    "preview-environments": dict(
        quiz_add=[("Preview environments cost more than production last month: 140 of them are still running for pull requests closed weeks ago. What do you add?",
                   "Delete the environment when the pull request closes or merges, add a time-to-live (for example 48 hours without a push), scale previews to zero when idle, and report their cost per team.")],
        try_it="Add a pipeline job that deploys each pull request to its own namespace with a unique URL and a seeded database, and a second job that deletes it on close. Open and close a test pull request and check nothing is left.",
    ),
    "health-checks": dict(
        quiz_add=[("The database has a two-minute blip. Kubernetes restarts all 30 API pods because their liveness check queries the database, and recovery takes 10 minutes. What do you change?",
                   "Keep liveness about the process itself (it responds at all). Put dependency checks in readiness so pods stop taking traffic during the blip instead of restarting, and come back by themselves when the database returns.")],
        try_it="Add /livez and /readyz endpoints to a service in a local cluster: liveness checks the process, readiness checks the database. Stop the database and see pods become not ready but keep running. Then point liveness at the database and repeat.",
    ),
    "autoscaling": dict(
        quiz_add=[("A queue worker scales on CPU, which stays at 20% while the queue grows to 2 hours of work, because the workers wait on an external API. What signal do you scale on, and what limit do you set?",
                   "Queue length or age (with KEDA, for example), so instances follow the work waiting. Set a maximum that the external API can handle, or more workers will only hit its rate limit.")],
        try_it="Deploy a service with a Horizontal Pod Autoscaler in a local cluster and send load with hey or k6. Watch replicas go up and down, then change the scale-down stabilisation window and compare how often it flaps.",
    ),
    "observability": dict(
        quiz_add=[("Checkout is slow for some users. The dashboard shows average latency at 300 ms, which looks fine, and logs don't have a request id. Where do you start, and what do you add?",
                   "Look at the p95 and p99 latency, which the average hides. Add tracing (OpenTelemetry) with a trace id in every log line, so a slow request can be followed across services to the step that takes the time.")],
        try_it="Add OpenTelemetry to two services that call each other and send traces to a local Jaeger. Make one call slow on purpose, find it in a trace, and then find its log lines by trace id.",
    ),
    "slo-error-budgets": dict(
        quiz_add=[("The checkout SLO is 99.9% over 28 days. By day 10 you have used 80% of the error budget, and two big features are due next week. What do you do?",
                   "Slow down risky change: freeze or gate non-urgent releases, spend the time on the reliability problems that used the budget, and agree this with product. That is what the budget is for. Ship the features once the burn rate is back to normal.")],
        try_it="Pick one user journey and define its SLI from data you already have (share of requests under 500 ms without errors). Set an SLO, calculate the error budget in minutes for 28 days, and write a burn-rate alert for 2% of the budget used in one hour.",
    ),
    "disaster-recovery": dict(
        quiz_add=[("Ransomware encrypts your production database and the backups, which were in the same cloud account with the same admin credentials. What should the backup setup have been?",
                   "At least one immutable copy (object lock or vault lock) in a separate account and region, with different credentials, plus regular restore drills that prove you meet your RPO and RTO.")],
        try_it="Restore yesterday's backup of one database into a fresh environment, timing each step from “go” to “app works”. Compare the time with your RTO and the data you'd have lost with your RPO.",
    ),
    "postmortems": dict(
        quiz_add=[("At 02:00 checkout is failing and three engineers are debugging in different directions while customers wait. A deploy went out at 01:40. What should the incident commander do first?",
                   "Mitigate before diagnosing: roll back the 01:40 deploy, assign one person to communicate status, and keep notes for the timeline. Root cause analysis comes after service is restored.")],
        try_it="Pick a recent incident or near miss and write a one-page blameless postmortem: timeline, impact, contributing factors, what went well, and three actions with owners and dates. Review it with the team and track the actions to done.",
    ),
    "finops": dict(
        quiz_add=[("The cloud bill rose 40% in a quarter and nobody can say which team caused it. A third of resources have no tags. What do you do first?",
                   "Enforce tags for team, service and environment in infrastructure code and policy, tag the existing resources, and show cost per team. Then look at the biggest items: idle non-production environments, oversized instances and storage nobody owns.")],
        try_it="Run Infracost on your infrastructure code to see the monthly cost of one change in a pull request. Then list your ten most expensive resources, find their owner, and switch off one non-production environment outside working hours.",
    ),
}

for _rev in REVISIONS.values():
    _rev.setdefault("revised", ("Nov 2026", "a “what would you do?” question and a try it"))
