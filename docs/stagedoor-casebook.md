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
| Jan–Oct 2026 | Rafaela and Tiago arrive; the servers are understood, fixed and made boring | **3 Linux** |
| 2027 | move to AWS (eu-west-1, Ireland), everything in Terraform from day one; Spain launch | 5 Terraform |
| 2027–2028 | the seat-hold double sell, locks behind a migration, bloat, RDS, read replicas, major upgrade | 6 PostgreSQL |
| 2028 | containers and EKS for ~25 services; Maré Festival's on-sale (200,000 fans in ten minutes) | 4 Kubernetes |
| 2028–2029 | tracing and SLOs; pipelines, canaries and supply chain | 7, 8 |

Reading order differs from the chronology: each book says where Stagedoor is at its start, and cross-book references
read "Handbook 5 tells how this was built", never "as you saw".

## 4. Handbook 3 · Linux for Cloud Engineers (Jan–Oct 2026)

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
