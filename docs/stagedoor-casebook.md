# Stagedoor casebook

The running story of Series 3's second group of handbooks (Handbook 3 onwards). **Approved by the owner on
2026-11-27.** Larder stays with Handbooks 1–2 and the notebooks; nothing here may borrow Larder's people or facts.

Every fact a chapter adds goes here, book by book, with its chapter. Before writing a chapter, read this file; after
writing one, add what it made canon. Dates are checked against a calendar (weekday stated where it matters).

## 1. The company

**Stagedoor** sells tickets for small and mid-sized music venues, based in **Lisbon**. Venues sell through it; fans buy
on the web and in the app; door staff scan tickets on phones. Traffic is calm for weeks and then explodes for ten
minutes when a popular show goes on sale ("an on-sale"), so every layer is tested at once.

Domain names use the reserved `.example` TLD: `stagedoor.example` (site and API at `tickets.stagedoor.example`,
the door-scanning API at `scan.stagedoor.example`). Public IPs use documentation ranges (`203.0.113.0/24`,
`198.51.100.0/24`).

## 2. People (pronouns are canon; never infer them)

| Who | Pronouns | Role |
| --- | --- | --- |
| **Joana Matos** | she/her | co-founder and CEO; ran a venue's box office for eight years |
| **Leonor Ferreira** | she/her | co-founder and CTO; wrote the first version and built the first server in 2023 |
| **Rafaela Costa** | she/her | first operations engineer, joins **Mon 5 Jan 2026** from a hosting company; the patient mentor |
| **Tiago Neves** | he/him | junior developer, joins **Mon 2 Feb 2026** straight from university; the reader's stand-in |
| **Sasha Petrova** | she/her | backend lead since 2025; owns the ticketing service and the database schema |
| **Marco Antunes** | he/him | contractor in 2024; built the door-scanning API; left in Nov 2024, but his account and key remained (Handbook 3, ch. 4 and 16) |

## 3. Company arc

| When | What | Book |
| --- | --- | --- |
| Mar 2023 | Leonor rents one Debian server (`door-1`) and runs everything on it: the Python (FastAPI) app, nginx, PostgreSQL | background |
| 2025 | three servers at Atlantica Hosting (fictional, Lisbon); 600 venues in Portugal; 9 engineers | background |
| Jan–Nov 2026 | Rafaela and Tiago arrive; the servers are understood, fixed and made boring | **3 Linux** |
| 2027 | move to AWS (eu-west-1, Ireland), everything in Terraform from day one; Spain launch | 5 Terraform |
| 2027–2028 | the seat-hold double sell, locks behind a migration, bloat, RDS, read replicas, major upgrade | 6 PostgreSQL |
| 2028 | containers and EKS for ~25 services; Maré Festival's on-sale (200,000 fans in ten minutes) | 4 Kubernetes |
| 2028–2029 | tracing and SLOs; pipelines, canaries and supply chain | 7, 8 |

Reading order differs from the chronology: each book says where Stagedoor is at its start, and cross-book references
read "Handbook 5 tells how this was built", never "as you saw".

## 4. Handbook 3 · Linux for Cloud Engineers (Jan–Nov 2026)

### The servers (as found on 5 Jan 2026, ch. 1)

All three are virtual servers rented from Atlantica Hosting, on a private network `10.40.0.0/24` behind Atlantica's
load balancer (public address `203.0.113.40`).

| Host | Private IP | Built | OS (Jan 2026) | Size | Runs |
| --- | --- | --- | --- | --- | --- |
| `door-1` | `10.40.0.11` | Mar 2023, by Leonor | Debian 11 "bullseye" (security support ends **31 Aug 2026**, the end of Debian LTS) | 8 vCPU, 32 GB, 1 TB SSD | PostgreSQL 13, the nightly jobs (cron), the reports |
| `door-2` | `10.40.0.12` | Apr 2025 | Ubuntu 22.04 LTS | 4 vCPU, 8 GB, 160 GB | nginx + the app |
| `door-3` | `10.40.0.13` | Apr 2025 | Ubuntu 22.04 LTS | 4 vCPU, 8 GB, 160 GB | nginx + the app |

- `door-1` had been up **401 days** on 5 Jan 2026 (last boot 30 Nov 2024): kernel updates installed, never rebooted into.
- The app (`stagedoor`, Python 3.10, FastAPI under uvicorn) runs on `door-2`/`door-3` **as root**, from
  `/root/stagedoor`, started by hand with `nohup … &`; its output goes to `/root/stagedoor/nohup.out` (6.1 GB on
  `door-2` on 9 Feb 2026). Config, including the database password, in `/root/stagedoor/.env`. `/srv/app` is a
  symlink to `/root/stagedoor` that nginx's config refers to (ch. 3).
- The **root password** has been pinned in the team chat's `#ops` channel since 2023; everyone logs in as root (ch. 1).
  Changed and removed from the chat on **Wed 18 Feb 2026** (ch. 4).
- Uploads (venue posters and seating plans) live in `/srv/uploads` on `door-2` and `door-3` (kept in step by an
  `rsync` every five minutes from `door-2`), mode **777** (ch. 4).

### Part I (ch. 1–4)

- **Ch. 1 (Mon 5 Jan 2026):** Rafaela's first day; the inventory of the three servers above; she writes a one-page
  "server card" per host with a small script. Her first rule: nothing changes until it's written down.
- **Ch. 2 (Wed 4 Feb 2026):** Tiago's first week. Joana asks how many fans hit an error at checkout during Friday
  30 Jan's on-sale (Os Lumes at Sala Ribeira, Porto; fictional band and venue). Tiago's `grep 500 | wc -l` on
  `door-2` says **381**; counting the status field with `awk` says **27** failed checkout requests (500/502/504) from
  **26** addresses (one fan failed twice), all between **10:01 and 10:04**; `door-3`'s log is similar. `500` had
  matched the seat-map path `event=4500` and two response sizes. The figures are the lab's sample log (`makelog.py`,
  seed 2026, 2,000 lines from 09:58). Rafaela's wiki rule: *before you send a number, show the lines you counted*.
  Sasha's team asks for the app logs of those four minutes (cause not yet told; free for a later chapter).
- **Ch. 3 (week of 9 Feb 2026):** where the app lives (above); the agreed layout, applied over the following weeks:
  code in `/opt/stagedoor/releases/<version>` with a `current` symlink; config in `/etc/stagedoor/stagedoor.env`;
  data in `/var/lib/stagedoor` (uploads move to `/var/lib/stagedoor/uploads`); logs in `/var/log/stagedoor`.
  Releases switch by replacing the `current` symlink atomically (`ln -s … current.new && mv -T current.new current`).
  The 6.1 GB `nohup.out` stays for now: still open by the app (deleting it would free nothing).
- **Ch. 4 (Tue 17 – Wed 18 Feb 2026):** Rafaela's search for world-writable directories finds `/srv/uploads` (777)
  with files owned by `marco` among the posters. Fixes: a system user and group `stagedoor` for the app;
  `/var/lib/stagedoor/uploads` owned `stagedoor:www-data`, mode `2750` (setgid), files `640`, app umask `027`, so
  nginx (`www-data`) can read and only the app can write. Personal accounts `leonor`, `rafaela`, `tiago`, `sasha`
  in `sudo`; root password changed and deleted from the chat on 18 Feb. `marco`'s account locked and expired the
  same day (`usermod -L -e 1`). Not found yet: his public key in **root's** `authorized_keys` (ch. 16).
  The app still runs as root until it becomes a systemd service (ch. 6, with `UMask=0027`). The five-minute `rsync` from
  `door-2` to `door-3` now copies `/var/lib/stagedoor/uploads` with `rsync -a`. The new root password is in the
  company password manager, for emergencies only.

### Parts II and III (ch. 5–12), written 2026-11-27

- **Ch. 5 (Thu 26 Feb 2026, 15:10):** the deploy script's `pkill -9 -f uvicorn` kills three checkouts mid-payment;
  three fans charged without tickets, refunded by Joana. New deploy: fail health check → `SIGTERM`, wait 30 s
  (slowest normal checkout ~8 s) → `SIGKILL` only if needed → start → health check → next server (`door-2` first).
- **Ch. 6 (Mon 2 – Wed 4 Mar):** the payouts cron job on `door-1` (03:00) failed from Wed 25 Feb to Sun 1 Mar:
  Leonor reinstalled the report tool with `pip` on Tue 24 Feb (now `/usr/local/bin`); Debian 11's cron `PATH` is
  `/usr/bin:/bin`; errors went to `/var/mail/root`. Replaced by `payouts.service` + `payouts.timer`
  (`OnCalendar=*-*-* 03:00:00 Europe/Lisbon`, `Persistent=true`, full path); alert on failed units. Wed 4 Mar:
  the app becomes `stagedoor.service` (user `stagedoor`, `UMask=0027`, `EnvironmentFile=/etc/stagedoor/stagedoor.env`,
  release `/opt/stagedoor/releases/2026.03.1`); `nohup.out` deleted and the space freed. Deploys: unpack, `mv -T`,
  `systemctl restart`, one server at a time. The app still writes `/var/log/stagedoor/stagedoor.log` at DEBUG.
- **Ch. 7 (Fri 20 Mar, 10:04–10:11):** `door-2`'s disk full: `stagedoor.log` 131 GB (DEBUG since February);
  `door-3` at 97%. Deleting didn't free it; truncated through `/proc/<pid>/fd`. Seven minutes of failed checkouts;
  the tour sold out in forty. Fixes: INFO level, a DEBUG switch that turns itself off after an hour, app logs to
  stdout/journal, journald capped (4 GB, 20 GB kept free), disk alert at 80%. Wiki rule: *every log has an owner, a
  level, a size limit and a destination*.
- **Ch. 8 (Tue 7 – Tue 14 Apr):** unattended-upgrades had been disabled since June 2025 (an automatic update restarted
  the app during an on-sale); ~140 pending updates per web server. Policy (Figure 8.2): security updates daily,
  needrestart `'l'`, no automatic reboots; Tuesdays 05:00 Lisbon maintenance, one server at a time, skipped on on-sale
  days. 14 Apr: `door-1` rebooted after 500 days. Decision: a **new database server on Ubuntu 24.04**, built from a
  checklist by end of August 2026, data moved to it (Handbook 6 tells the database side); not an in-place upgrade.
- **Ch. 9 (Fri 8 May, 10:02):** alert “door-1 load average 14.2” (8 vCPU); CPUs 30% busy, I/O wait > 50%, ~10
  threads in `D`: a weekly full backup timer `OnCalendar=Fri 08:00` (UTC; 09:00 Lisbon in summer) ran into the 10:00
  on-sale, taking 80 min instead of 40. Stopped at 10:05; moved to `Sun 04:00 Europe/Lisbon` with `Nice=10`,
  `IOSchedulingClass=idle`; load alert replaced by CPU-busy and I/O-wait alerts. Handbook 6: back up from a replica.
- **Ch. 10 (Fri 5 Jun, 10:12, 40 s outage):** the kernel OOM-killed a PostgreSQL backend (19 GB RSS) running an
  analyst's settlement report with `work_mem` set to 4 GB; PostgreSQL restarted all connections and ran crash
  recovery. 32 GB, no swap, 8 GB shared buffers, ~200 connections. Fixes: a report role with `work_mem` 64 MB and a
  statement timeout, reports outside on-sales, an 8 GB swap file on `door-1`, postmaster `OOMScoreAdjust=-1000`,
  alert on `MemAvailable` < 10%. Handbook 6: a read replica for reports.
- **Ch. 11 (Thu 25 Jun, 14:20–15:05):** `door-2` uploads fail with “No space left on device” at 61% used: inodes
  exhausted by 9.8 million thumbnails in `/var/cache/stagedoor/thumbs` (~10 million inodes on the 160 GB ext4 root).
  Fixes: delete thumbnails unused for 30 days (nightly timer), three standard sizes instead of one per device,
  inode alert at 80%. Same week: Atlantica grows `door-1`'s disk from 1 TB to 1.5 TB; `growpart` + `resize2fs`
  online. The new database server will keep data on its own volume.
- **Ch. 12 (Fri 10 Jul, 10:00:38–10:07):** biggest on-sale yet (a stadium date); nginx on `door-2` hits errno 24
  and “768 worker_connections are not enough” (soft limit 1024 per worker). Fixed live, then properly: `LimitNOFILE=65536`
  drop-ins for nginx and `stagedoor.service`, `worker_rlimit_nofile 65536`, `worker_connections 8192`,
  `listen … backlog=4096`, keep-alive to the app; alerts on `TcpExtListenOverflows` and descriptors per worker. Sold
  out at 10:31. Joana's question leads to load tests before big on-sales, against a copy of the servers.

### Part IV (ch. 13–16), written 2026-11-27

- **Ch. 13 (Mon 24 – Thu 27 Aug 2026):** the new database server **`door-4`** (Ubuntu 24.04, `10.40.0.14`), built
  from Rafaela's checklist. Internal name `db.stagedoor.internal` (internal DNS zone `stagedoor.internal`). Dry run
  on Mon 24 Aug: `door-2` refused (PostgreSQL on `127.0.0.1:5432` only; fixed with
  `listen_addresses = 'localhost, 10.40.0.14'` and `pg_hba.conf` for the two web servers); `door-3` connected to the
  old `10.40.0.11` because of a 2025 `/etc/hosts` line (Leonor, during a DNS outage). Rule: *internal names live in
  DNS, and nowhere else*. Move Thu 27 Aug 23:00–01:30; `door-1` read-only until Mon 31 Aug, then switched off.
- **Ch. 14 (Sun 13 Sep 2026, 18:40–19:20):** `scan.stagedoor.example`'s certificate (commercial CA, bought by Marco
  in 2024, renewed by hand by Leonor in Sep 2025) expired at 17:59 Lisbon (`notAfter=Sep 13 16:59:00 2026 GMT`);
  reminders went to Marco's bouncing address. Door staff at two Lisbon venues checked names by hand. Let's Encrypt
  certificate in place at 19:05, queues gone by 19:20. After: certbot for every public name (timer, reload hook,
  copy to the other web server), external expiry check alerting 21 days ahead, supplier contacts → `ops@`.
- **Ch. 15 (Tue 6 – Thu 15 Oct 2026):** a security assessment (for a group of twelve venues) reports every port on
  every server reachable from the web servers, incl. SSH everywhere and a forgotten metrics exporter on `door-4:9100`.
  Thu 8 Oct: nftables default-deny rulesets per role in Git (web: 80/443 from anywhere, SSH from the **office VPN**;
  `door-4`: PostgreSQL from the web servers, SSH from the VPN), rolled out with an automatic undo; exporter removed
  (a push agent replaces it). Retest 15 Oct clean. In AWS each becomes a security group too (Handbook 5).
- **Ch. 16 (Mon 19 Oct 2026):** root's `authorized_keys` on `door-2`/`door-3` held `leonor@macbook` (2023),
  `deploy@old-ci` (CI switched off 2025) and `marco@contractor-laptop` (Apr 2024); `PermitRootLogin` allowed keys;
  password SSH was still on (thousands of guesses a day). All root keys removed; drop-in: no root, no passwords,
  `AllowGroups ssh-users`, `LogLevel VERBOSE`; personal keys with passphrases; SSH only from the VPN, `door-2` as
  jump host for `door-4`. Local logs went back four weeks: no use of Marco's key found; earlier use unknowable.
  Auth logs now shipped with a year's retention. Plan: short-lived SSH certificates, or Session Manager after the
  move to AWS. Leaver checklist gains: keys in every account, supplier contacts, certificates.

### Parts V and VI (ch. 17–21), written 2026-11-27

- **Ch. 17 (Thu 22 Oct 2026, 03:15–07:40):** the nightly release clean-up timer (`stagedoor` user, working directory
  `/var/lib/stagedoor`; a typo in the unit's variable name left `RELEASES_DIR` unset) ran `cd $RELEASES_DIR` →
  failed → `ls -t | tail -n +6 | xargs rm -rf` in `/var/lib/stagedoor`, deleting `uploads` and `exports`. Restored
  from `door-3` (rsync without `--delete`; `door-3`'s timer has a random delay) by 07:40; exports regenerated.
  Uploads now backed up nightly to Atlantica's object storage. Rules: strict mode + `${VAR:?}`, dry runs, ShellCheck
  in CI blocking merges, failed-unit alerts.
- **Ch. 18 (Thu 29 Oct – Thu 12 Nov):** the assessment's remaining seven findings. Baseline written three ways
  (checklist, `baseline.yaml` checked with `cloud-init schema` in CI, a build script). Sandbox drop-ins:
  `stagedoor.service` 9.2 → 1.5, nginx 9.6 → 4.1. auditd for sudoers, SSH config, firewall, root commands; shipped.
  A leftover FTP server removed from `door-3`. Lynis on `door-2`: 58 → 81. Findings closed 12 Nov.
- **Ch. 19 (Thu 5 Nov):** the app's first container image (Sasha's team, for laptops, later the cloud): shell-form
  `CMD` → 10 s stops and 137; ~4,000 zombie PDF-helper processes after a load test. Fixed: exec form, `tini`
  entrypoint, non-root, read-only root, uploads on a volume. Decision: the payment service must not share a kernel
  with other services; on AWS it gets its own VMs or Fargate (Firecracker).
- **Ch. 20 (Fri 13 Nov, 19:40–19:52):** Tiago's first solo on-call: event pages at 10 s. `first5.sh`: `door-2`'s data
  disk 94% busy, queue 30, I/O wait 40%, `find` in `D` from `thumbs-cleanup.service`, made hourly by Sasha's team on
  Thu 12 Nov. Stopped at 19:48 (pages 280 ms); 20:00 on-sale fine. Timer back to nightly 03:30 Lisbon with `Nice=10`
  and `IOSchedulingClass=idle`; the app deletes a poster's thumbnails when the poster changes.
- **Ch. 21 (Thu 19 – Thu 26 Nov):** `door-5` (Ubuntu 24.04, replacing `door-2`, whose 22.04 support ends April 2027)
  built at Atlantica by `build-web.sh` in four minutes; second run changes nothing. Drill Tue 24 Nov at 3× July's
  peak: 3% failures, cause uvicorn started with `--backlog 64` from a 2023 config; release 2026.11.2 fixed it; second
  drill clean. Crash drill: one app process per server = a 2-second outage per crash; `door-5` joins `door-3` behind
  Atlantica's load balancer (health check removes a server in 1 s). `door-2` switched off Thu 26 Nov. Next: AWS in
  2027 (Handbook 5) with the same baseline as Terraform and images. Not yet in the script: auditd, log shipping,
  certificates (certbot on `door-3`), monitoring, uploads sync and backups, the data volume.

### Promised for later chapters (keep consistent)

- Ch. 5: a deploy kills requests mid-checkout (uvicorn killed with `kill -9` by the deploy script).
- Ch. 6: the app becomes a systemd service as user `stagedoor`; the nightly payouts report on `door-1` (cron, 03:00)
  works by hand but not from cron (PATH); replaced by a timer.
- Ch. 7: the on-sale night the disk filled with logs (`nohup.out`, no logrotate for the app).
- Ch. 8: `door-1`'s Debian 11 support ends 31 Aug 2026; plan its replacement.
- Ch. 10: a report on `door-1` during a sale; the OOM killer kills PostgreSQL.
- Ch. 12: "too many open files" at nginx in the first ten minutes of a big on-sale.
- Ch. 14: a certificate that expired on a Sunday.
- Ch. 16: Marco's key in root's `authorized_keys`; password and root SSH login switched off.
- Ch. 21: servers rebuilt from a checklist and a script, ready for the move to AWS (Handbook 5).
