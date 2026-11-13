# Docker & Kubernetes · a laminated reference card in four pages.
# Rendered by scripts/build_notes.py (render_cheatsheet); Graph, Diagram, cmd, code and box come from scripts/cheatsheet.py.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "docker-kubernetes"
TITLE = "Docker & Kubernetes"
SUBTITLE = "images, containers, kubectl, rollouts and troubleshooting"
DESC = ("A four-page Docker and Kubernetes cheat sheet: Docker commands, Dockerfiles and Compose, the Kubernetes object "
        "map, kubectl, rollouts, probes, resources, config and a pod troubleshooting guide.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages: Docker and Compose, the Kubernetes object map and kubectl, rollouts, probes and "
         "resources, and a pod troubleshooting decoder. Copy-paste commands for every day.")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<rect x="6" y="19" width="9" height="8" rx="1.5" fill="var(--b-dev)"/><rect x="16" y="19" width="9" height="8" rx="1.5" fill="var(--b-dev)"/>'
        '<rect x="11" y="10" width="9" height="8" rx="1.5" fill="var(--b-bug)"/>'
        '<circle cx="26" cy="9" r="5" fill="none" stroke="var(--b-rel)" stroke-width="2.4"/><circle cx="26" cy="9" r="1.6" fill="var(--b-rel)"/></svg>')

# ---------------------------------------------------------------- page 1 · docker
DOCKER = (Diagram("Docker lifecycle: a Dockerfile is built into an image, pushed to and pulled from a registry; "
                  "an image is run as a container that moves from created to running to stopped to removed.", 880, 222)
          .node("df", 14, 34, 116, 54, "Dockerfile", "the recipe", "ink")
          .node("img", 316, 34, 160, 54, "Image", "read-only layers · app:1.0", "dev")
          .node("reg", 666, 34, 200, 54, "Registry", "Hub · ECR · ACR · GHCR", "rel")
          .node("cr", 120, 146, 120, 46, "Created", None, "ink", "soft")
          .node("run", 330, 146, 120, 46, "Running", "PID 1 alive", "feat")
          .node("st", 540, 146, 120, 46, "Stopped", "exited (code)", "ink", "soft")
          .node("rm", 750, 146, 100, 46, "Removed", None, "ink", "ghost")
          .arrow("df", "img", "docker build -t app:1.0 .", tone="dev")
          .arrow("img", "reg", "docker push · docker pull", tone="rel")
          .arrow("img", "cr", "docker create", sides="bt", tone="ink", lx=225, ly=120)
          .arrow("img", "run", "docker run", sides="bt", tone="feat", lx=430, ly=120)
          .arrow("cr", "run", "start", tone="feat")
          .arrow("run", "st", "stop · crash", tone="ink")
          .arrow("st", "rm", "rm", tone="ink")
          .text(20, 214, "docker run = create + start  ·  a container lives exactly as long as its main process  ·  "
                         "docker start brings a stopped one back  ·  --rm removes it on exit"))

PAGE_DOCKER = dict(
    title="Docker",
    kicker="build an image, run a container",
    figure=DOCKER.svg(),
    boxes=[
        box("Everyday commands", cmd('''
docker build -t app:1.0 .
docker run -d --name web -p 8080:80 app:1.0
docker ps  # running · -a for all
docker logs -f --tail 100 web
docker exec -it web sh  # a shell inside
docker stop web && docker rm web
docker images
docker tag app:1.0 registry.example.com/team/app:1.0
docker push registry.example.com/team/app:1.0
'''), "dev", "wide", "daily"),
        box("Compose", cmd('''
docker compose up -d
docker compose up -d --build  # rebuild first
docker compose ps
docker compose logs -f api
docker compose exec api sh
docker compose down  # -v deletes volumes too
''') + '<p class="fine">Services reach each other by service name: <code>postgres://db:5432</code>, not localhost.</p>', "bug"),
        box("A Dockerfile that behaves", code('''
FROM node:22-alpine AS build  # 1 · build
WORKDIR /app
COPY package*.json ./  # cached layer
RUN npm ci
COPY . .
RUN npm run build
FROM node:22-alpine  # 2 · runtime
WORKDIR /app
ENV NODE_ENV=production
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/dist ./dist
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
'''), "feat", "", "multi-stage"),
        box("Dockerfile rules", '''
<ol class="rules">
<li><b>Order by change rate:</b> dependencies first, source last, so the cache works.</li>
<li><b>.dockerignore</b> <code>.git</code>, <code>node_modules</code>, <code>.env</code>, build output.</li>
<li><b>Pin the base</b> <code>node:22-alpine</code>, never <code>latest</code>.</li>
<li><b>Run as non-root</b> with <code>USER</code>.</li>
<li><b>Exec-form CMD</b> <code>["node","app.js"]</code> so SIGTERM reaches the app.</li>
<li><b>No secrets in layers.</b> <code>--secret</code> at build, env at runtime.</li>
<li><b>One process</b> per container, logging to stdout.</li>
</ol>''', "feat"),
        box("docker run flags", '''
<dl class="kv">
<dt><code>-d</code></dt><dd>in the background</dd>
<dt><code>-p 8080:80</code></dt><dd>host : container port</dd>
<dt><code>-e K=v</code></dt><dd>env var · <code>--env-file</code></dd>
<dt><code>-v data:/x</code></dt><dd>named volume (kept)</dd>
<dt><code>-v $PWD:/app</code></dt><dd>bind-mount a folder</dd>
<dt><code>--rm</code></dt><dd>delete on exit</dd>
<dt><code>-it</code></dt><dd>interactive terminal</dd>
<dt><code>--restart</code></dt><dd><code>unless-stopped</code></dd>
<dt><code>--memory</code></dt><dd><code>512m</code> · <code>--cpus 1</code></dd>
<dt><code>--network</code></dt><dd>reach others by name</dd>
</dl>''', "ink"),
        box("Won't stay up? Exit codes", '''
<dl class="kv two">
<dt><code>0</code></dt><dd>main process ended: nothing kept it running</dd>
<dt><code>1</code></dt><dd>app error: read the logs</dd>
<dt><code>125</code></dt><dd>docker run itself failed</dd>
<dt><code>126 · 127</code></dt><dd>not executable · command not found</dd>
<dt><code>137</code></dt><dd>SIGKILL: out of memory or killed</dd>
<dt><code>143</code></dt><dd>SIGTERM: stopped politely</dd>
</dl>''' + cmd('''
docker ps -a  # STATUS shows the exit code
docker run -it --entrypoint sh app:1.0  # poke around inside
'''), "main", "wide"),
        box("Clean up disk", cmd('''
docker system df  # what uses space
docker container prune
docker image prune -a  # unused images
docker builder prune  # build cache
docker volume prune  # ! deletes data
'''), "warn"),
    ],
)

# ---------------------------------------------------------------- page 2 · kubernetes map
K8S = (Diagram("Kubernetes object map: a client reaches an Ingress, which routes to a Service, which load-balances to Pods "
               "chosen by label selector. A Deployment manages a ReplicaSet which keeps the Pods running; an HPA scales the "
               "Deployment; ConfigMaps, Secrets and PersistentVolumeClaims are mounted into the Pods.", 880, 228)
       .node("cl", 14, 40, 90, 50, "Client", "browser · app", "ink", "soft")
       .node("ing", 150, 40, 130, 50, "Ingress", "host / path rules", "rel")
       .node("svc", 330, 40, 140, 50, "Service", "stable IP + DNS name", "dev")
       .group("pods", 520, 10, 190, 210, "pods · app=web", "feat")
       .node("p1", 536, 32, 158, 44, "Pod", "container(s) · own IP", "feat")
       .node("p2", 536, 96, 158, 44, "Pod", "container(s) · own IP", "feat")
       .node("p3", 536, 160, 158, 44, "Pod", "container(s) · own IP", "feat")
       .node("dep", 150, 160, 130, 50, "Deployment", "desired state · rollouts", "main")
       .node("rs", 330, 160, 140, 50, "ReplicaSet", "keeps N pods alive", "hot")
       .node("hpa", 14, 165, 90, 40, "HPA", None, "ink", "soft")
       .node("cm", 760, 22, 104, 38, "ConfigMap", None, "bug", "soft")
       .node("sec", 760, 72, 104, 38, "Secret", None, "bug", "soft")
       .node("pvc", 760, 130, 104, 38, "PVC", None, "rel", "soft")
       .node("pv", 760, 180, 104, 42, "PV", "disk · StorageClass", "rel", "soft")
       .arrow("cl", "ing", None, tone="ink")
       .arrow("ing", "svc", None, tone="rel")
       .arrow("svc", "pods", None, tone="dev")
       .arrow("dep", "rs", "owns", tone="main")
       .arrow("rs", "pods", "creates", tone="hot", ly=178)
       .arrow("hpa", "dep", "scales", tone="ink")
       .arrow("cm", "pods", None, sides="lr", tone="bug")
       .arrow("sec", "pods", None, sides="lr", tone="bug")
       .arrow("pvc", "pods", None, sides="lr", tone="rel")
       .arrow("pvc", "pv", "binds", sides="bt", tone="rel", lx=840, ly=176))

PAGE_K8S = dict(
    title="Kubernetes: the map",
    kicker="objects, kubectl and a minimal app",
    figure=K8S.svg(),
    boxes=[
        box("kubectl essentials", cmd('''
kubectl get pods -o wide  # node + pod IP
kubectl get all -n shop
kubectl get pods -A -l app=web  # all namespaces, by label
kubectl describe pod web-7d9f-abcde  # events at the bottom
kubectl apply -f k8s/  # create or update
kubectl delete -f k8s/
kubectl get deploy web -o yaml
kubectl explain deploy.spec.strategy  # built-in docs
kubectl api-resources  # kinds + short names
'''), "dev", "wide", "daily"),
        box("Contexts &amp; namespaces", cmd('''
kubectl config get-contexts
kubectl config use-context prod  # ! careful
kubectl config set-context --current --namespace=shop
kubectl get ns
''') + '<p class="fine">Show the context in your prompt (kube-ps1) and switch with kubectx / kubens.</p>', "warn"),
        box("Core objects", '''
<dl class="kv two">
<dt>Pod</dt><dd>containers sharing an IP; disposable</dd>
<dt>Deployment</dt><dd>stateless apps: replicas + rollouts</dd>
<dt>StatefulSet</dt><dd>stable names + own disk (databases)</dd>
<dt>DaemonSet</dt><dd>one pod per node (agents)</dd>
<dt>Job · CronJob</dt><dd>run to completion · on a schedule</dd>
<dt>Service</dt><dd>stable address in front of pods</dd>
<dt>Ingress</dt><dd>HTTP(S) routing by host / path</dd>
<dt>ConfigMap · Secret</dt><dd>config and credentials, env or files</dd>
<dt>PVC · PV</dt><dd>a claim for storage · the disk</dd>
<dt>HPA</dt><dd>scales replicas on metrics</dd>
<dt>Namespace</dt><dd>a folder for objects, quotas, access</dd>
<dt>ServiceAccount</dt><dd>a pod's identity for RBAC</dd>
</dl>''', "ink", "wide"),
        box("Service types", '''
<dl class="kv">
<dt>ClusterIP</dt><dd>default; inside the cluster only</dd>
<dt>NodePort</dt><dd>port 30000–32767 on every node</dd>
<dt>LoadBalancer</dt><dd>cloud load balancer, external IP</dd>
<dt>Headless</dt><dd><code>clusterIP: None</code> → pod IPs</dd>
<dt>ExternalName</dt><dd>DNS alias to the outside</dd>
</dl>
<p class="fine">DNS: <code>web</code> in the same namespace, <code>web.shop</code> across, <code>web.shop.svc.cluster.local</code> in full.</p>''', "dev"),
        box("A minimal app", code('''
apiVersion: apps/v1
kind: Deployment
metadata: { name: web }
spec:
  replicas: 3
  selector: { matchLabels: { app: web } }
  template:
    metadata: { labels: { app: web } }  # must match
    spec:
      containers:
        - name: web
          image: ghcr.io/team/web:1.4.0
          ports: [{ containerPort: 8080 }]
---
apiVersion: v1
kind: Service
metadata: { name: web }
spec:
  selector: { app: web }  # finds the pods
  ports: [{ port: 80, targetPort: 8080 }]
'''), "main", "wide", "deployment + service"),
        box("Who does what", '''
<dl class="kv">
<dt>api-server</dt><dd>the front door; everything talks to it</dd>
<dt>etcd</dt><dd>stores the cluster's state</dd>
<dt>scheduler</dt><dd>picks a node for each new pod</dd>
<dt>controllers</dt><dd>loop: make actual = desired</dd>
<dt>kubelet</dt><dd>per node: starts pods, runs probes</dd>
<dt>kube-proxy</dt><dd>per node: routes Service traffic</dd>
<dt>runtime</dt><dd>containerd / CRI-O runs containers</dd>
</dl>''', "ink"),
    ],
)

# ---------------------------------------------------------------- page 3 · deploy & operate
def roll():
    d = Diagram("A rolling update with maxSurge 1 and maxUnavailable 0: a new pod starts and becomes ready before an old "
                "one is removed, until all pods run the new version.", 880, 196)
    stages = [("1 · start", 3, 0), ("2 · surge: +1 new", 3, 1), ("3 · new ready, old out", 2, 2), ("4 · done", 0, 3)]
    x = 14
    for i, (label, old, new) in enumerate(stages):
        d.group(f"g{i}", x, 14, 200, 150, label, "ink")
        for k in range(old):
            d.node(f"o{i}{k}", x + 12 + k * 60, 44, 52, 40, "v1", None, "dev", "chip")
        for k in range(new):
            d.node(f"n{i}{k}", x + 12 + k * 60, 104, 52, 40, "v2", None, "feat", "chip")
        if i == 2:
            d.node("gone", x + 132, 44, 52, 40, "v1", None, "dev", "ghost")
        x += 216
    for i in range(3):
        d.arrow(f"g{i}", f"g{i + 1}", None, tone="ink")
    d.text(14, 186, "RS v1 (top row) scales down while RS v2 (bottom row) scales up · readiness probes gate every step · "
                    "kubectl rollout undo flips the two ReplicaSets back")
    return d.svg()


PAGE_OPS = dict(
    title="Deploy &amp; operate",
    kicker="rollouts, scaling, probes, resources, config",
    figure=roll(),
    boxes=[
        box("Ship a version · roll back", cmd('''
kubectl apply -f k8s/  # image tag changed in git
kubectl rollout status deploy/web
kubectl rollout history deploy/web
kubectl rollout undo deploy/web  # previous version
kubectl rollout undo deploy/web --to-revision=3
kubectl rollout restart deploy/web  # new pods, same spec
kubectl set image deploy/web web=registry.example.com/team/web:1.5.0  # quick, drifts from git
'''), "main", "wide", "release"),
        box("Scale", cmd('''
kubectl scale deploy/web --replicas=5
kubectl autoscale deploy/web --min=2 --max=10 --cpu-percent=70
kubectl get hpa
kubectl top pods  # needs metrics-server
''') + '<p class="fine">The HPA scales on CPU <b>requests</b>: no requests, no autoscaling.</p>', "dev"),
        box("Probes", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th>asks</th><th>on failure</th></tr></thead>
<tbody>
<tr><th>startup</th><td>has it booted?</td><td>others wait; restart if it never passes</td></tr>
<tr><th>readiness</th><td>can it take traffic?</td><td>removed from the Service; <b>not</b> restarted</td></tr>
<tr><th>liveness</th><td>is it stuck?</td><td>container restarted</td></tr>
</tbody></table></div>''' + code('''
readinessProbe:
  httpGet: { path: /ready, port: 8080 }
  periodSeconds: 5
livenessProbe:
  httpGet: { path: /healthz, port: 8080 }
  initialDelaySeconds: 10
''') + '<p class="fine">Keep liveness cheap and free of dependencies: a slow database must not restart every pod.</p>', "feat"),
        box("Requests &amp; limits", code('''
resources:
  requests: { cpu: 250m, memory: 256Mi }  # reserved
  limits:   { memory: 512Mi }  # hard cap
''') + '''
<dl class="kv">
<dt>CPU over</dt><dd>throttled (slow, not killed)</dd>
<dt>Memory over</dt><dd>OOMKilled · exit 137</dd>
<dt>Guaranteed</dt><dd>requests = limits: evicted last</dd>
<dt>Burstable</dt><dd>requests &lt; limits</dd>
<dt>BestEffort</dt><dd>none set: evicted first</dd>
</dl>''', "hot"),
        box("Config &amp; secrets", cmd('''
kubectl create configmap web-config --from-file=app.yaml
kubectl create secret generic db --from-literal=PASSWORD=s3cret
kubectl get secret db -o jsonpath='{.data.PASSWORD}' | base64 -d
kubectl rollout restart deploy/web  # pick up new env values
''') + '<p class="fine">Secrets are base64, <b>not</b> encrypted: add encryption at rest and RBAC, or use External Secrets / Sealed Secrets. Env vars only change when pods restart; mounted files update by themselves.</p>', "bug"),
        box("Strategy, jobs &amp; disruptions", code('''
strategy:
  type: RollingUpdate  # or Recreate
  rollingUpdate: { maxSurge: 1, maxUnavailable: 0 }
''') + cmd('''
kubectl get cronjobs
kubectl create job once --from=cronjob/nightly  # run now
kubectl logs job/once
''') + '<p class="fine"><b>Recreate</b> when two versions can\'t run side by side. Add a <b>PodDisruptionBudget</b> so node drains keep enough pods up.</p>', "rel"),
    ],
)

# ---------------------------------------------------------------- page 4 · troubleshooting
def flow():
    d = Diagram("Pod troubleshooting flow: run kubectl get pods and read the status. Pending: describe the pod and read the "
                "events. ImagePullBackOff: check the image name, tag and pull secret. CrashLoopBackOff: read logs with "
                "--previous. Running but not ready: check the readiness probe. Ready but no traffic: check the Service "
                "endpoints, selector and ports.", 880, 300)
    d.node("root", 14, 123, 150, 54, "kubectl get pods", "read STATUS / READY", "ink")
    rows = [
        ("pend", "Pending", "warn", "describe pod → Events: no CPU/memory, unbound PVC, taints"),
        ("pull", "ImagePullBackOff", "rel", "image name / tag typo? private registry → imagePullSecrets"),
        ("crash", "CrashLoopBackOff", "main", "logs --previous · OOMKilled? exit code · missing config"),
        ("ready", "Running · 0/1 Ready", "hot", "readiness probe failing: path, port, timing → describe"),
        ("traf", "Ready, no traffic", "dev", "get endpoints · selector labels · targetPort · Ingress"),
    ]
    for i, (nid, label, tone, act) in enumerate(rows):
        y = 10 + i * 58
        d.node(nid, 240, y, 190, 44, label, None, tone)
        d.node(nid + "a", 490, y, 376, 44, act, None, tone, "soft")
        d.arrow("root", nid, None, tone=tone)
        d.arrow(nid, nid + "a", None, tone=tone)
    return d.svg()


PAGE_DEBUG = dict(
    title="Troubleshooting",
    kicker="read the status, then follow the clue",
    figure=flow(),
    boxes=[
        box("Debug commands", cmd('''
kubectl describe pod <pod>  # Events: the first clue
kubectl logs <pod> -c <container> --previous  # the crash before the restart
kubectl logs deploy/web -f --since=10m
kubectl get events -n shop --sort-by=.lastTimestamp
kubectl exec -it <pod> -- sh
kubectl debug -it <pod> --image=busybox:1.36 --target=web  # no shell in the image?
kubectl port-forward svc/web 8080:80  # test from your laptop
kubectl top pod --containers
kubectl get pod <pod> -o yaml  # the real spec + status
'''), "dev", "wide", "first five minutes"),
        box("Docker → kubectl", '''
<dl class="kv">
<dt><code>ps</code></dt><dd><code>kubectl get pods</code></dd>
<dt><code>logs -f</code></dt><dd><code>kubectl logs -f</code></dd>
<dt><code>exec -it</code></dt><dd><code>kubectl exec -it p -- sh</code></dd>
<dt><code>inspect</code></dt><dd><code>kubectl describe</code> · <code>-o yaml</code></dd>
<dt><code>stats</code></dt><dd><code>kubectl top pod</code></dd>
<dt><code>-p 8080:80</code></dt><dd><code>kubectl port-forward</code></dd>
<dt><code>compose up</code></dt><dd><code>kubectl apply -f</code></dd>
</dl>''', "ink"),
        box("Status decoder", '''
<dl class="kv two">
<dt>Pending</dt><dd>no node fits: requests, PVC, taints, nodeSelector</dd>
<dt>ContainerCreating</dt><dd>stuck on a volume, secret or network</dd>
<dt>ErrImagePull</dt><dd>wrong image / tag, or no pull secret</dd>
<dt>CrashLoopBackOff</dt><dd>starts, exits, retries with growing delay</dd>
<dt>OOMKilled</dt><dd>over the memory limit: raise it or fix the leak</dd>
<dt>CreateContainer­ConfigError</dt><dd>a ConfigMap / Secret or key is missing</dd>
<dt>Evicted</dt><dd>node ran short of memory or disk</dd>
<dt>Terminating forever</dt><dd>finalizers or a dead node: describe first</dd>
</dl>''', "main", "wide"),
        box("Stay safe", '''
<ul class="checks">
<li><b>Check the context</b> before apply / delete</li>
<li><code>kubectl diff -f k8s/</code> before <code>apply</code></li>
<li>Generate YAML: <code>--dry-run=client -o yaml</code></li>
<li>No <code>kubectl edit</code> in prod: git wins</li>
<li>Never <code>:latest</code>; pin tags or digests</li>
<li>Requests + limits on every container</li>
<li><code>--force --grace-period=0</code>: last resort</li>
</ul>''', "warn"),
        box("No traffic? Walk the path", '''
<ol class="steps">
<li><code>kubectl get endpoints web</code>: empty means the selector doesn't match the pod labels, or no pod is Ready.</li>
<li><code>port-forward</code> to a pod, then to the Service: which hop fails?</li>
<li>DNS from inside: <code>kubectl run tmp --rm -it --image=busybox:1.36 -- nslookup web.shop</code></li>
<li><code>targetPort</code> = the port the container really listens on? Ingress: <code>describe ingress</code> for host, path, <code>ingressClassName</code>, TLS secret. Still nothing? A NetworkPolicy may block it.</li>
</ol>''', "bug", "full"),
    ],
)

PAGES = [PAGE_DOCKER, PAGE_K8S, PAGE_OPS, PAGE_DEBUG]
