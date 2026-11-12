# Vol. 6 · Infrastructure as code: IaC, GitOps, Immutable Infrastructure, Preview Environments.

# ------------------------------------------------------------------ 05 Infrastructure as Code
ic_problem = Doodle(760, 250, "Doodle of an engineer clicking through a cloud console to create a database, a load balancer and firewall rules, following a wiki page from two years ago. Staging and production were set up by different people and differ in thirty small ways. Nobody can recreate production if the account is lost.",
                    "Clicked together from an old wiki page: staging ≠ prod, and nobody could rebuild it.")
ic_problem.icon("screen", 30, 50, 1.6)
ic_problem.note(80, 170, "click, click, click…", "pen")
ic_problem.box(260, 40, 200, 70, "staging", "paper", sub="set up by Ana, 2023")
ic_problem.box(500, 40, 200, 70, "prod", "paper", sub="set up by Ben, 2024")
ic_problem.note(480, 150, "30 small differences", "red")
ic_problem.note(480, 190, "account lost? can't rebuild", "red")

ic_analogy = Doodle(760, 250, "Doodle of an architect's blueprint for a house. Builders follow the drawing, so any number of identical houses can be built. Changes are made on the drawing first, reviewed, and then built; nobody knocks down walls without updating the plans.",
                    "A blueprint: change the drawing first, review it, then build. Identical houses every time.")
ic_analogy.icon("map", 40, 50, 1.8, fill="blue")
ic_analogy.note(100, 190, "the blueprint", "pen")
ic_analogy.arrow(170, 110, 300, 110, label="build", lx=235, ly=96)
for i in range(3):
    ic_analogy.icon("store", 310 + i * 120, 70, 1.2, fill="y")
ic_analogy.note(490, 200, "identical houses", "green")

ic_how = Doodle(760, 290, "Infrastructure as code workflow. Resources are described in Terraform files in git. A pull request runs a plan showing exactly what will be created, changed or destroyed. A reviewer approves. On merge, the pipeline applies the change. State is stored remotely with locking. The same modules create staging and production with different variables.",
                "Describe resources in code, review the plan in a PR, apply from the pipeline. Same modules for every environment.")
ic_how.box(20, 40, 160, 70, "main.tf", "blue", sub="in git")
ic_how.arrow(186, 75, 266, 75, label="PR", lx=226, ly=61)
ic_how.box(272, 30, 200, 90, "plan", "y", sub="+2 ~1 −0")
ic_how.arrow(478, 75, 556, 75, color="green", label="approve", lx=517, ly=61)
ic_how.box(562, 40, 180, 70, "apply (CI)", "green")
ic_how.box(140, 170, 240, 60, "module: web-service", "paper", size=16)
ic_how.arrow(386, 190, 470, 170)
ic_how.arrow(386, 210, 470, 230)
ic_how.box(476, 150, 140, 40, "staging", "green", size=16)
ic_how.box(476, 210, 140, 40, "prod", "green", size=16)

IAC = dict(
    slug="infrastructure-as-code",
    kicker="a.k.a. “the blueprint”",
    tldr="Describe networks, databases, queues, DNS and permissions in <b>code files in git</b> (Terraform, OpenTofu, Pulumi, CloudFormation), and change them only through <b>pull requests</b> that show a <b>plan</b> of exactly what will change. A pipeline <b>applies</b> it. Environments become <b>reproducible</b>, changes become <b>reviewable</b>, and git becomes the history of your infrastructure.",
    chips=[("Family", "infrastructure"), ("Tools", "Terraform / OpenTofu, Pulumi, CloudFormation, CDK, Bicep"), ("Key idea", "declarative desired state + plan"), ("Pairs with", "GitOps, immutable infrastructure")],
    problem="""  <p class="lead">Infrastructure built by <span class="hl-pink">clicking in a console</span> lives only in that account and in someone's memory. Environments drift apart, changes aren't reviewed, and disaster recovery is guesswork.</p>
  <ul>
    <li>Staging and production differ in dozens of small settings.</li>
    <li>“Who opened port 22 to the world?” No record.</li>
    <li>Rebuilding after an account loss would take weeks.</li>
  </ul>""",
    problem_figs=[ic_problem],
    analogy_side="the blueprint",
    analogy="""  <p>Builders follow an <b>architect's blueprint</b>, so you can build <b>identical houses</b> again and again. Changes are drawn <b>on the plan first</b>, checked, then built. Nobody knocks down a wall without updating the drawing.</p>
  <ul>
    <li>The blueprint is your <b>IaC code</b>.</li>
    <li>Checking the drawing is <b>reviewing the plan</b>.</li>
    <li>A wall knocked down without updating plans is <b>drift</b>.</li>
  </ul>""",
    analogy_figs=[ic_analogy],
    map=[("The blueprint", "Terraform/Pulumi files in git"),
         ("Reviewing changes to the drawing", "PR with a <code>plan</code> diff"),
         ("Builders follow the plan", "CI runs <code>apply</code>"),
         ("Identical houses from one plan", "Same modules for staging and prod"),
         ("Unrecorded wall changes", "Drift from console edits")],
    how_side="plan, review, apply",
    how="""  <p>Most IaC tools are <b>declarative</b>: you describe the end state, the tool works out the steps. The <b>plan</b> is the most important safety feature: read it before every apply.</p>""",
    how_figs=[ic_how],
    steps=[("Start with what hurts", "Import or codify the most critical resources first (network, databases, IAM)."),
           ("Use modules", "Reusable building blocks (<code>web-service</code>, <code>postgres</code>) with environment variables."),
           ("Remote state with locking", "S3 + DynamoDB, Terraform Cloud, or your tool's backend."),
           ("Plan in every PR", "Post the plan as a comment; reviewers read it."),
           ("Apply only from CI", "Short-lived credentials; no laptop applies to production."),
           ("Detect drift", "Scheduled plans that alert when reality differs from code; lock down console write access.")],
    vocab=[("IaC", "Infrastructure defined in machine-readable files."),
           ("Declarative", "Describe the end state, not the steps."),
           ("State", "The tool's record of what it created."),
           ("Plan", "Preview of creates, updates and deletes."),
           ("Module", "A reusable group of resources."),
           ("Drift", "Real infrastructure differing from the code.")],
    code=dict(file="envs/prod/main.tf", note="Terraform / OpenTofu", src="""
terraform {
  backend "s3" {
    bucket         = "acme-tfstate"
    key            = "prod/web.tfstate"
    dynamodb_table = "tf-locks"          # state locking
  }
}

module "web" {
  source        = "../../modules/web-service"
  name          = "web"
  environment   = "prod"
  image_digest  = var.image_digest       # from the build pipeline
  min_instances = 3
  max_instances = 30
  tags          = { team = "storefront", cost_center = "cc-114" }
}

# PR:    terraform plan  → posted as a comment
# merge: terraform apply → from CI with a short-lived role
"""),
    tools="tools: Terraform / OpenTofu, Pulumi, AWS CloudFormation and CDK, Azure Bicep, Crossplane, Atlantis or Spacelift for PR plans, Checkov/tfsec/Trivy for policy checks, driftctl-style drift detection.",
    gains=["<b>Reproducible environments</b>.",
           "<b>Reviewed changes</b> with a visible plan.",
           "<b>History</b> in git: who changed what and why.",
           "<b>Faster recovery</b>: rebuild from code."],
    losses=["<b>Learning curve</b> and state management.",
            "<b>Plans can surprise</b> (replacements, deletions).",
            "<b>Slower for one-off experiments</b>.",
            "<b>Drift</b> if people still click in consoles."],
    baseline="Each line compares <b>infrastructure clicked together in consoles</b> to <b>infrastructure as code with PR plans and CI apply</b>.",
    ratings=[(3, 3, "More tooling; but everything is written down."),
             (2, 4, "New environments in minutes, not days."),
             (2, 4, "Plans show exactly what will change."),
             (2, 4, "Fewer config differences and manual mistakes."),
             (2, 4, "Modules stamp out more capacity easily."),
             (1, 4, "Rebuild from code after a disaster."),
             (2, 4, "Git history explains every change."),
             (3, 3, "Tool costs vs. fewer hours clicking."),
             (2, 4, "Self-service via reviewed PRs.")],
    pitfalls=[("Applying from laptops", "Two people apply at once; state corrupts.", "apply only from CI with locking."),
              ("Not reading the plan", "A rename destroys and recreates the database.", "review plans; protect critical resources (<code>prevent_destroy</code>)."),
              ("One giant state file", "Every plan takes 20 minutes and touches everything.", "split state by service and environment."),
              ("Secrets in code or state", "Passwords committed in .tf files.", "reference a secrets manager; encrypt state.")],
    use=["Any cloud infrastructure that matters.",
         "Multiple environments that should match.",
         "Teams that want reviewed, auditable changes."],
    skip=["Throwaway sandbox experiments (but codify what survives).",
          "Fully managed platforms with nothing to configure."],
    related=["<b>GitOps</b>", "<b>Immutable infrastructure</b>", "<b>Preview environments</b>", "<b>Least privilege</b> (Vol. 5)"],
    quiz=[("What does declarative mean in IaC?", "You describe the desired end state; the tool works out how to reach it."),
          ("Why review the plan?", "It shows exactly what will be created, changed or destroyed before anything happens."),
          ("What is drift?", "Differences between real infrastructure and the code, usually from manual changes."),
          ("Why apply only from CI?", "Locking, consistent credentials, audit trail, and no conflicting applies from laptops.")],
    remember="Change the <span class=\"hl\">blueprint</span> first, <span class=\"hl\">review</span> it, then build.",
    sources=["Kief Morris, <i>Infrastructure as Code</i> (2nd ed., O'Reilly).",
             "HashiCorp, “Terraform Recommended Practices”.",
             "OpenTofu documentation.",
             "Google Cloud, “Best practices for using Terraform”."],
)

# ------------------------------------------------------------------ 06 GitOps
go_problem = Doodle(760, 250, "Doodle of a CI pipeline with cluster admin credentials pushing deployments into Kubernetes, while engineers also run kubectl apply by hand. Nobody knows what is actually running, a manual hotfix gets overwritten by the next deploy, and the CI system's credentials are a juicy target.",
                    "CI pushes with admin keys, people kubectl by hand: nobody knows what's really running.")
go_problem.box(20, 40, 160, 60, "CI (admin key)", "pink", stroke="red", size=16)
go_problem.box(20, 150, 180, 60, "kubectl by hand", "pink", stroke="red", size=16)
go_problem.arrow(186, 70, 380, 110, color="red")
go_problem.arrow(206, 180, 380, 130, color="red")
go_problem.icon("container", 390, 90, 1.2)
go_problem.note(600, 80, "what's running?", "red")
go_problem.note(600, 120, "hotfix overwritten", "red")
go_problem.note(600, 160, "admin key in CI", "red")

go_analogy = Doodle(760, 250, "Doodle of a thermostat. You set the desired temperature to twenty-one degrees. The thermostat keeps measuring the room and turns heating on or off to match. If someone opens a window, it corrects automatically. You change the setting, not the heater.",
                    "A thermostat: set the target; it measures and corrects, all day. You change the setting, not the heater.")
go_analogy.box(40, 60, 140, 110, "21 °C", "y", sub="desired", size=26)
go_analogy.arrow(186, 115, 300, 115, label="measure · correct", lx=243, ly=100)
go_analogy.icon("kitchen", 310, 80, 1.3)
go_analogy.note(470, 70, "window opened? → corrects", "green", anchor="start")
go_analogy.note(470, 130, "you change the setting,", "pen", anchor="start")
go_analogy.note(470, 156, "not the heater", "pen", anchor="start")

go_how = Doodle(760, 290, "GitOps loop. A config repository holds the desired state of each environment, for example image digest and replica count. An agent such as Argo CD or Flux runs inside the cluster, pulls the repo, compares it with what is running, and syncs any difference. Changes happen only by pull request to the repo. Manual changes are detected as drift and reverted. Rollback is a git revert.",
                "Git holds the desired state; an in-cluster agent pulls and keeps reality in sync. Rollback = git revert.")
go_how.box(20, 60, 200, 110, "config repo", "y", sub="prod: web@9c1e · 6 pods")
go_how.arrow(226, 100, 410, 100, label="② pull", lx=318, ly=86)
go_how.box(416, 50, 160, 70, "Argo CD / Flux", "green", size=16)
go_how.arrow(496, 124, 496, 176, label="③ diff + sync", lx=510, ly=156, anchor="start")
go_how.box(406, 180, 180, 60, "cluster", "blue")
go_how.box(20, 210, 200, 50, "① PR + review", "paper", size=16)
go_how.arrow(120, 206, 120, 174)
go_how.note(680, 110, "drift?", "red")
go_how.note(680, 136, "reverted", "red")

GITOPS = dict(
    slug="gitops",
    kicker="a.k.a. “the thermostat”",
    tldr="Keep the <b>desired state</b> of each environment (what image, how many replicas, which config) in a <b>git repository</b>. An <b>agent inside the cluster</b> (Argo CD, Flux) <b>pulls</b> that repo and continuously <b>reconciles</b> reality to match. All changes go through <b>pull requests</b>; manual changes show up as <b>drift</b> and are reverted; <b>rollback is git revert</b>.",
    chips=[("Family", "deployment / operations"), ("Coined by", "Weaveworks (2017)"), ("Tools", "Argo CD, Flux, Rancher Fleet"), ("Pairs with", "IaC, build once, immutable infrastructure")],
    problem="""  <p class="lead">When CI <span class="hl-pink">pushes</span> into clusters with admin credentials and people also change things by hand, nobody can say what's running, and every change path is a different risk.</p>
  <ul>
    <li>A manual hotfix is silently overwritten by the next deploy.</li>
    <li>CI holds cluster-admin keys, a high-value target.</li>
    <li>Rolling back means rebuilding someone's memory of the last good state.</li>
  </ul>""",
    problem_figs=[go_problem],
    analogy_side="the thermostat",
    analogy="""  <p>You set a <b>thermostat</b> to 21 °C. It <b>measures</b> the room all day and turns the heating on or off to match. Open a window and it <b>corrects automatically</b>. You change the <b>setting</b>, never the heater directly.</p>
  <ul>
    <li>The setting is the <b>git repo</b>.</li>
    <li>The thermostat is the <b>GitOps agent</b>.</li>
    <li>The open window is <b>drift</b> from manual changes.</li>
  </ul>""",
    analogy_figs=[go_analogy],
    map=[("Target temperature", "Desired state in git"),
         ("The thermostat measuring", "Agent comparing cluster vs repo"),
         ("Heating on/off", "Sync: apply the difference"),
         ("Window opened", "Manual change → drift, reverted"),
         ("Change the dial", "Pull request to the config repo")],
    how_side="pull and reconcile",
    how="""  <p>Because the agent <b>pulls</b> from inside the cluster, CI never needs cluster credentials: it only opens a PR (or commits) bumping the image digest.</p>""",
    how_figs=[go_how],
    steps=[("Separate config from app code", "A config repo (or folder) per environment with manifests, Helm values or Kustomize overlays."),
           ("Install the agent", "Argo CD or Flux in each cluster, with read access to the repo."),
           ("CI updates git, not the cluster", "After a build, CI opens a PR bumping the digest for staging."),
           ("Promote by PR", "Promotion to prod is a reviewed change to the prod folder."),
           ("Self-heal and alert on drift", "Auto-sync reverts manual edits; alerts tell you it happened."),
           ("Roll back with git", "<code>git revert</code> the bad change; the agent syncs.")],
    vocab=[("Desired state", "What should be running, written in git."),
           ("Reconciliation", "Making actual state match desired state."),
           ("Pull-based deploy", "The cluster fetches changes instead of CI pushing."),
           ("Sync", "Applying differences to the cluster."),
           ("Drift", "Live state differing from git."),
           ("Environment promotion", "Moving a version to the next environment via PR.")],
    code=dict(file="apps/web-prod.yaml", note="Argo CD Application", src="""
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata: { name: web-prod, namespace: argocd }
spec:
  project: storefront
  source:
    repoURL: https://github.com/acme/deploy-config
    path: envs/prod/web            # kustomization with the image digest
    targetRevision: main
  destination: { server: https://kubernetes.default.svc, namespace: web }
  syncPolicy:
    automated:
      prune: true                  # delete what git no longer lists
      selfHeal: true               # revert manual changes (drift)
# CI's only job after building: open a PR changing the digest in envs/staging/web
"""),
    tools="tools: Argo CD, Flux, Rancher Fleet, Kargo (promotion), Kustomize and Helm for manifests, Renovate or image-updater bots for digest bumps, Terraform/Crossplane for GitOps-managed cloud resources.",
    gains=["<b>Git is the truth</b> for what runs.",
           "<b>Rollback = git revert</b>.",
           "<b>No cluster credentials in CI</b>.",
           "<b>Drift detected and fixed</b> automatically."],
    losses=["<b>More repos and moving parts</b>.",
            "<b>Secrets need a separate approach</b> (sealed secrets, external secrets).",
            "<b>Emergency changes</b> still go through git.",
            "<b>Mostly Kubernetes-centric</b> tooling."],
    baseline="Each line compares <b>CI pushing to clusters plus manual kubectl</b> to <b>pull-based GitOps with an in-cluster agent</b>.",
    ratings=[(3, 3, "An agent and a config repo to learn."),
             (3, 4, "Deploys are just merged PRs."),
             (2, 4, "Every change reviewed; rollback is a revert."),
             (2, 4, "Self-heal fixes accidental changes."),
             (3, 4, "Same pattern across many clusters."),
             (2, 5, "Rebuild a cluster by pointing an agent at git."),
             (2, 4, "Sync status and history per app."),
             (3, 3, "Open-source tools; some ops effort."),
             (2, 4, "Self-service through PRs and a UI.")],
    pitfalls=[("Secrets in the config repo", "Plain-text secrets in git.", "External Secrets, Sealed Secrets or SOPS."),
              ("Manual changes during incidents", "Someone kubectl-edits; the agent reverts it mid-incident.", "make the fix in git, or pause sync deliberately."),
              ("CI pushes and agent syncs", "Two systems fighting over the same resources.", "one source of truth: git."),
              ("Huge monorepo of manifests", "Every sync touches everything.", "split by team or app; use app-of-apps.")],
    use=["Kubernetes platforms with several services and environments.",
         "Teams that need audit trails and easy rollback.",
         "Many clusters that should stay consistent."],
    skip=["A single small app on a PaaS (its own deploy is enough).",
          "Infrastructure without a reconciling agent (use IaC pipelines)."],
    related=["<b>Infrastructure as code</b>", "<b>Build once, deploy many</b>", "<b>Immutable infrastructure</b>", "<b>Secrets management</b> (Vol. 5)"],
    quiz=[("What does the GitOps agent do?", "Continuously compares the cluster with the desired state in git and syncs any difference."),
          ("Why is pull-based deployment more secure?", "CI doesn't need cluster credentials; the in-cluster agent pulls changes."),
          ("How do you roll back?", "Revert the commit in the config repo; the agent syncs the previous state."),
          ("What happens to a manual kubectl change?", "It's detected as drift and reverted (with self-heal on).")],
    remember="Change the <span class=\"hl\">setting</span>, not the heater. The <span class=\"hl\">thermostat</span> does the rest.",
    sources=["OpenGitOps, “GitOps Principles v1.0” (CNCF).",
             "Weaveworks, “GitOps: Operations by Pull Request” (2017).",
             "Argo CD documentation.",
             "Flux documentation."],
)

# ------------------------------------------------------------------ 07 Immutable Infrastructure
im_problem = Doodle(760, 250, "Doodle of a server called web-03 that has been running for four years. Engineers SSH in to patch packages, edit config files and restart services. It is now unlike any other server, nobody knows exactly what's on it, and everyone is afraid to reboot it.",
                    "web-03: four years of hand patches. A unique snowflake nobody dares to reboot.")
im_problem.icon("server", 40, 60, 1.6, fill="pink")
im_problem.note(90, 170, "web-03 · up 1,460 days", "red")
for i, t in enumerate(["ssh: apt upgrade", "ssh: vim nginx.conf", "ssh: “quick fix”"]):
    im_problem.note(320, 60 + i * 40, t, "pen", anchor="start")
im_problem.note(560, 200, "“don't reboot it!”", "red")

im_analogy = Doodle(760, 250, "Doodle of disposable paper cups versus a treasured mug. The mug gets chipped, glued, and has a unique history; when it breaks, it's a crisis. Paper cups are all identical; if one is damaged you take a fresh one from the stack.",
                    "Pets vs cattle, or a treasured mug vs paper cups: a damaged cup is replaced, not repaired.")
im_analogy.icon("cup", 60, 60, 1.8, fill="pink")
im_analogy.note(110, 190, "the treasured mug", "red")
im_analogy.note(110, 216, "(glued 3 times)", "red")
for i in range(5):
    im_analogy.icon("cup", 330 + i * 70, 70, 1.0, fill="y")
im_analogy.note(500, 190, "identical cups: take a fresh one", "green")

im_how = Doodle(760, 290, "Immutable infrastructure. A pipeline bakes a machine image or container image with the OS, patches and app. Instances are launched from that image and never modified. To patch or change config, bake a new image and roll it out, replacing old instances. SSH access is off. Instances can be destroyed at any time.",
                "Bake a new image for every change; replace instances instead of patching them. No SSH.")
im_how.box(20, 40, 180, 80, "bake image", "y", sub="OS + patches + app")
im_how.arrow(206, 80, 286, 80, label="v42", lx=246, ly=66)
for i in range(3):
    im_how.icon("server", 300 + i * 80, 50, 1.0, fill="green")
im_how.note(400, 140, "launched from v42", "green")
im_how.arrow(400, 160, 400, 200, dash=True)
im_how.box(250, 204, 300, 50, "patch? bake v43, replace", "blue", size=16)
im_how.note(660, 70, "SSH: off", "red")
im_how.note(660, 100, "edit in place: never", "red")

IMMUTABLE = dict(
    slug="immutable-infrastructure",
    kicker="a.k.a. “paper cups, not the treasured mug”",
    tldr="Never change a running server. <b>Bake</b> everything (OS, patches, runtime, app) into an <b>image</b>, launch instances from it, and to change anything <b>bake a new image and replace</b> the old instances. Servers become <b>identical and disposable</b> (cattle, not pets), drift disappears, and rollback is launching the previous image.",
    chips=[("Family", "infrastructure"), ("Phrase", "“cattle, not pets” (Bill Baker / Randy Bias)"), ("Tools", "containers, Packer, managed instance groups, Bottlerocket"), ("Pairs with", "build once, IaC, autoscaling")],
    problem="""  <p class="lead">Servers that are <span class="hl-pink">patched by hand</span> slowly become unique snowflakes. Nobody knows exactly what's on them, they can't be recreated, and everyone is afraid to touch them.</p>
  <ul>
    <li>“It works on web-01 but not web-03.”</li>
    <li>A security patch applied to 9 servers out of 10.</li>
    <li>Rebooting is a risk; replacing is impossible.</li>
  </ul>""",
    problem_figs=[im_problem],
    analogy_side="paper cups vs the treasured mug",
    analogy="""  <p>A <b>treasured mug</b> gets chipped, glued and repaired, and when it finally breaks it's a crisis. <b>Paper cups</b> are all identical; if one is damaged you just <b>take a fresh one</b> from the stack. Nobody repairs a paper cup.</p>
  <ul>
    <li>The mug is a <b>pet server</b>.</li>
    <li>Paper cups are <b>instances from an image</b>.</li>
    <li>The stack of cups is your <b>image</b>, reproducible on demand.</li>
  </ul>""",
    analogy_figs=[im_analogy],
    map=[("A treasured, repaired mug", "A long-lived server patched by hand"),
         ("A stack of identical cups", "Instances launched from one image"),
         ("Take a fresh cup", "Replace an instance instead of fixing it"),
         ("A new cup design", "Bake a new image version"),
         ("Throw the damaged cup away", "Terminate unhealthy instances freely")],
    how_side="replace, don't repair",
    how="""  <p>Containers made this the default for apps; the same idea applies to VMs (golden images) and even to node operating systems.</p>""",
    how_figs=[im_how],
    steps=[("Bake images in CI", "Container images or VM images (Packer) with OS patches and the app."),
           ("Launch from images only", "Instance groups or Kubernetes pull a specific image version."),
           ("Externalise state", "Data in databases, object storage and volumes, not on the instance disk."),
           ("Roll out by replacement", "Rolling, blue–green or canary replacement of instances."),
           ("Remove SSH", "Use logs, metrics and ephemeral debug sessions instead of shell access."),
           ("Rebuild regularly", "Bake weekly even without app changes, to pick up patches.")],
    vocab=[("Immutable server", "Never modified after launch."),
           ("Golden image", "A pre-built machine image used for all instances."),
           ("Pets vs cattle", "Unique, hand-cared servers vs identical, replaceable ones."),
           ("Configuration drift", "Servers diverging through manual changes."),
           ("Stateless instance", "Holds no data that must survive replacement."),
           ("Rolling replacement", "Replacing instances a few at a time.")],
    code=dict(file="web.pkr.hcl", note="Packer (VM images)", src="""
source "amazon-ebs" "web" {
  region        = "eu-west-1"
  instance_type = "t3.small"
  source_ami_filter { filters = { name = "al2023-ami-*-x86_64" } most_recent = true owners = ["amazon"] }
  ami_name      = "web-${formatdate("YYYYMMDD-hhmm", timestamp())}"
}

build {
  sources = ["source.amazon-ebs.web"]
  provisioner "shell" { inline = ["sudo dnf -y update", "sudo dnf -y install nginx"] }
  provisioner "file"  { source = "dist/", destination = "/srv/web" }
}
# the instance group's launch template points at the new AMI;
# an instance refresh replaces servers one by one. Nobody SSHes in.
"""),
    tools="tools: container images on Kubernetes / ECS / Cloud Run, Packer for VM images, AWS instance refresh and GCP managed instance groups, Bottlerocket / Talos / Flatcar (immutable node OS), Systems Manager Session Manager for break-glass access.",
    gains=["<b>No drift</b>: every instance is identical.",
           "<b>Easy rollback</b>: launch the previous image.",
           "<b>Fearless replacement</b> and autoscaling.",
           "<b>Smaller attack surface</b> without SSH."],
    losses=["<b>Every change needs a bake</b> and rollout.",
            "<b>Image pipelines</b> to build and maintain.",
            "<b>State must live elsewhere</b>.",
            "<b>Debugging</b> without shell access takes new habits."],
    baseline="Each line compares <b>long-lived servers patched by hand</b> to <b>instances launched from baked images and replaced on change</b>.",
    ratings=[(2, 4, "Every server is the same; no mystery state."),
             (3, 4, "Changes flow through one image pipeline."),
             (2, 4, "Known images, replaced gradually."),
             (2, 4, "No snowflakes; unhealthy instances just get replaced."),
             (2, 5, "Identical instances scale out freely."),
             (2, 4, "Recreate anything from an image."),
             (3, 3, "Needs good logs and metrics instead of SSH."),
             (3, 3, "Bake time vs. hours of manual patching."),
             (3, 4, "No “special server” knowledge needed.")],
    pitfalls=[("Data on the instance", "Uploads stored on local disk vanish on replacement.", "object storage, databases, persistent volumes."),
              ("Break-glass SSH becomes normal", "“Just this once” edits return.", "audit any access; bake the fix into the next image."),
              ("Stale images", "Images built months ago with old patches.", "rebuild on a schedule."),
              ("Slow bakes", "45-minute image builds discourage fixes.", "layered images, caching, smaller base images.")],
    use=["Stateless app servers, workers, container nodes.",
         "Fleets that autoscale.",
         "Security-sensitive environments."],
    skip=["Stateful databases without a managed service (handle carefully).",
          "Legacy systems that can't be automated yet (start by codifying them)."],
    related=["<b>Build once, deploy many</b>", "<b>Infrastructure as code</b>", "<b>Autoscaling</b>", "<b>Defence in depth</b> (Vol. 5)"],
    quiz=[("What does “cattle, not pets” mean?", "Servers are identical and replaceable rather than unique and hand-maintained."),
          ("How do you patch an immutable server?", "Bake a new image with the patch and replace the instances."),
          ("What must happen to state?", "It must live outside the instance (databases, object storage, volumes)."),
          ("Why remove SSH?", "It prevents drift from manual changes and removes an attack path.")],
    remember="Don't glue the <span class=\"hl\">mug</span>. Take a fresh <span class=\"hl\">cup</span> from the <span class=\"hl\">stack</span>.",
    sources=["Chad Fowler, “Trash Your Servers and Burn Your Code: Immutable Infrastructure” (2013).",
             "Martin Fowler, “ImmutableServer” and “SnowflakeServer” (bliki).",
             "Randy Bias, “The History of Pets vs Cattle”.",
             "HashiCorp Packer documentation."],
)

# ------------------------------------------------------------------ 08 Preview Environments
pe_problem = Doodle(760, 250, "Doodle of one shared staging environment with five teams queueing for it. Team A's half-finished change breaks staging for everyone, the designer can't review the new page because staging has someone else's branch, and reviews happen by reading code diffs only.",
                    "One shared staging, five teams in the queue, and someone's half-finished change breaks it for all.")
for i in range(5):
    pe_problem.circle(40 + i * 46, 120, 18, "paper")
pe_problem.note(130, 170, "waiting for staging…", "pen")
pe_problem.arrow(270, 120, 380, 120)
pe_problem.box(386, 70, 200, 100, "staging", "pink", stroke="red", sub="Team A's branch, broken")
pe_problem.note(670, 90, "designer can't", "red")
pe_problem.note(670, 116, "see the new page", "red")

pe_analogy = Doodle(760, 250, "Doodle of a pop-up market stall. Each vendor gets their own stall for the day to show their goods. It's set up in minutes from a standard kit, customers can try things, and it's packed away in the evening. Nobody has to share one stall.",
                    "Pop-up stalls: each vendor gets one for the day, from a standard kit, packed away at night.")
for i in range(3):
    pe_analogy.icon("store", 40 + i * 150, 60, 1.3, fill=["y", "green", "blue"][i])
    pe_analogy.note(85 + i * 150, 180, f"PR #{101 + i}", "pen")
pe_analogy.note(580, 90, "set up in minutes", "green")
pe_analogy.note(580, 130, "packed away tonight", "green")

pe_how = Doodle(760, 290, "Preview environment lifecycle. Opening a pull request triggers the pipeline to build the image and create a namespace pr-142 with the app, a seeded database branch and a unique URL, posted as a PR comment. Reviewers, designers and product managers test it. Pushing updates redeploys it. Merging or closing the PR destroys everything, and a time-to-live cleans up anything forgotten.",
                "Every PR gets its own short-lived copy with a URL. Merge or close it, and it's destroyed.")
pe_how.box(20, 40, 160, 70, "PR #142", "blue", sub="opened")
pe_how.arrow(186, 75, 266, 75, label="deploy", lx=226, ly=61)
pe_how.box(272, 30, 260, 110, "pr-142.preview.acme.dev", "green", sub="app + seeded DB branch", size=15)
pe_how.arrow(538, 85, 600, 85)
pe_how.note(680, 70, "reviewers, PMs,", "pen")
pe_how.note(680, 96, "designers test it", "pen")
pe_how.box(252, 190, 300, 60, "merged / closed → destroy", "pink", stroke="red", size=15)
pe_how.arrow(402, 144, 402, 186, dash=True, color="red")
pe_how.note(140, 230, "TTL: 3 days idle", "pen")

PREVIEW = dict(
    slug="preview-environments",
    kicker="a.k.a. “pop-up stalls”",
    tldr="Give <b>every pull request its own short-lived environment</b> with a unique URL: the app, its dependencies and a <b>seeded database</b>, created by the pipeline from your infrastructure code. Reviewers, designers and product managers can <b>try the change</b> before merge. When the PR is <b>merged or closed</b>, everything is <b>destroyed</b>, with a time-to-live as a safety net.",
    chips=[("Family", "developer workflow"), ("a.k.a.", "ephemeral / review apps, PR environments"), ("Tools", "Vercel, Netlify, Render, Argo CD ApplicationSet, Neon branches"), ("Pairs with", "IaC, build once, feature flags")],
    problem="""  <p class="lead">A single <span class="hl-pink">shared staging</span> environment becomes a queue and a battlefield: one broken branch blocks everyone, and non-developers can't see changes until they're merged.</p>
  <ul>
    <li>Teams wait for their turn on staging.</li>
    <li>Someone's half-finished change breaks it for everyone else.</li>
    <li>Design and product review happens after merge, when fixes are slower.</li>
  </ul>""",
    problem_figs=[pe_problem],
    analogy_side="pop-up market stalls",
    analogy="""  <p>At a market, each vendor gets a <b>pop-up stall</b> for the day, set up in minutes from a <b>standard kit</b>. Customers can try things, and in the evening it's <b>packed away</b>. Nobody has to share one stall and wait their turn.</p>
  <ul>
    <li>Each stall is a <b>preview environment</b>.</li>
    <li>The standard kit is your <b>IaC + build</b>.</li>
    <li>Packing up is <b>automatic teardown</b>.</li>
  </ul>""",
    analogy_figs=[pe_analogy],
    map=[("A stall per vendor", "An environment per pull request"),
         ("The standard kit", "Shared IaC modules and the PR's image"),
         ("Customers trying goods", "Reviewers testing the real change"),
         ("Packed away at night", "Destroyed on merge/close"),
         ("Market closes at 6 p.m.", "Time-to-live for forgotten environments")],
    how_side="create on open, destroy on close",
    how="""  <p>The hardest part is usually <b>data</b>: use seeded fixtures or cheap database branches, never a copy of production personal data.</p>""",
    how_figs=[pe_how],
    steps=[("Make environments cheap to create", "IaC modules and small, scaled-down resources."),
           ("Trigger from PR events", "On open/push: build, deploy to <code>pr-&lt;n&gt;</code>; post the URL."),
           ("Seed the data", "Fixtures or database branches (Neon, PlanetScale); no production PII."),
           ("Stub expensive dependencies", "Shared sandbox accounts for payments and email."),
           ("Destroy automatically", "On merge/close, plus a TTL for idle environments."),
           ("Protect them", "SSO or basic auth in front; they're not public sites.")],
    vocab=[("Ephemeral environment", "Created for a short time, then destroyed."),
           ("Review app", "Heroku's name for a per-PR app."),
           ("TTL", "Time-to-live after which a resource is deleted."),
           ("Database branch", "A copy-on-write database clone for a branch."),
           ("Namespace", "An isolated slice of a Kubernetes cluster."),
           ("Seed data", "Known, fake data loaded for testing.")],
    code=dict(file=".github/workflows/preview.yml", note="per-PR namespace", src="""
on:
  pull_request: { types: [opened, synchronize, reopened, closed] }

jobs:
  preview:
    if: github.event.action != 'closed'
    steps:
      - run: ./build.sh                             # image tagged with the PR sha
      - run: |
          helm upgrade --install pr-${{ github.event.number }} ./chart \\
            --namespace pr-${{ github.event.number }} --create-namespace \\
            --set image.digest=$DIGEST --set db.branch=pr-${{ github.event.number }} \\
            --set ingress.host=pr-${{ github.event.number }}.preview.acme.dev
      - run: gh pr comment ${{ github.event.number }} --body "Preview ready"

  teardown:
    if: github.event.action == 'closed'
    steps:
      - run: kubectl delete namespace pr-${{ github.event.number }}
"""),
    tools="tools: Vercel and Netlify preview deploys, Render/Heroku review apps, Argo CD ApplicationSet pull-request generator, Okteto, Uffizzi, Neon / PlanetScale / Supabase database branching, kube-janitor for TTL cleanup.",
    gains=["<b>No staging queue</b>.",
           "<b>Review the real thing</b> before merge.",
           "<b>Isolated</b>: one broken PR breaks only itself.",
           "<b>Proves IaC works</b> many times a day."],
    losses=["<b>Cloud cost</b> if teardown fails.",
            "<b>Data seeding</b> takes effort.",
            "<b>Not production-sized</b>: performance differs.",
            "<b>External integrations</b> need sandboxes."],
    baseline="Each line compares <b>one shared staging environment</b> to <b>an automatic preview environment per pull request</b>.",
    ratings=[(3, 3, "More automation; each environment is simple."),
             (2, 5, "No waiting; review in parallel."),
             (3, 4, "Problems found before merge."),
             (3, 3, "Neutral for production."),
             (2, 4, "Scales with the number of teams."),
             (3, 4, "Environments are recreated constantly from code."),
             (3, 3, "Neutral."),
             (3, 3, "Many small environments; TTL keeps it in check."),
             (2, 5, "Share a link instead of a screenshot.")],
    pitfalls=[("No teardown", "200 forgotten environments on the bill.", "destroy on close + TTL + cost alerts."),
              ("Copying production data", "Customer PII in dozens of temporary environments.", "seeded fake data or anonymised subsets."),
              ("Public preview URLs", "Unreleased features indexed by search engines.", "SSO/basic auth, noindex."),
              ("Full-size infrastructure per PR", "Each preview costs as much as staging.", "scale down; share heavy dependencies.")],
    use=["Web apps and APIs with frequent PRs.",
         "Teams where design and product review matter.",
         "Several teams sharing one staging environment."],
    skip=["Systems too heavy to clone (use shared integration environments + flags).",
          "Very early prototypes with one developer."],
    related=["<b>Infrastructure as code</b>", "<b>Build once, deploy many</b>", "<b>Feature flags</b>", "<b>Throwaway containers</b> (Vol. 4)"],
    quiz=[("What triggers a preview environment's creation and deletion?", "Opening/updating a pull request creates or updates it; merging or closing destroys it."),
          ("Why add a TTL?", "To clean up environments that were never torn down and keep costs under control."),
          ("What data should previews use?", "Seeded fake data or database branches from safe data, never raw production PII."),
          ("What's the main benefit over shared staging?", "No queue and no interference: each change is reviewed in isolation before merge.")],
    remember="A <span class=\"hl\">stall</span> per vendor, set up from the <span class=\"hl\">kit</span>, packed away <span class=\"hl\">tonight</span>.",
    sources=["Heroku docs, “Review Apps”.",
             "Vercel docs, “Preview Deployments”.",
             "Argo CD docs, “ApplicationSet: Pull Request Generator”.",
             "Neon docs, “Database branching”."],
)

NOTES = [IAC, GITOPS, IMMUTABLE, PREVIEW]
