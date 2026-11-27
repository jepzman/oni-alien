# Handoff: Handbook 3 · Linux for Cloud Engineers

Status as of **2026-11-27**: **complete: all 21 chapters (Parts I–VI) and appendices A–E written and checked.**
`BOOK["next"]` has been removed. What remains is in §5 (runs on a real VM of what couldn't run here).

Read first: `docs/HANDOFF-handbooks.md` §1–2 (what a handbook is, voice, building blocks, look),
`docs/HANDOFF-handbooks-next.md` §0 (mechanics) and §3 (this book's outline), and **`docs/stagedoor-casebook.md`**
(the story; every fact a chapter adds goes there).

## 1. Owner decisions (2026-11-27)

1. **Stagedoor approved** as the story for the new handbooks (casebook created).
2. **21 chapters**, as outlined (no merging of 8 into 18 or 9 into 10).
3. **Ubuntu** is the main distribution; Debian, the RHEL family and Amazon Linux compared in an "Across
   distributions" section per chapter (it replaces Handbooks 1–2's "Across providers").
4. **cloud-init as sections**: introduced in ch. 1 (§1.4), built and tested in ch. 18 (hardening baseline); no chapter
   of its own.
5. Writing approved: placeholders plus Part I in this session.

## 2. Where things are

| What | Where |
| --- | --- |
| Outline | `content/handbooks/linux/book.py` (key `linux`, no. 3; complete, no `next`) |
| Chapters | `content/handbooks/linux/<nn>-<slug>.html`; written: 01–21; appendices A–C hand-written (`appendix-a-cheat-sheet.html`, `appendix-b-distributions.html`, `appendix-c-lab-setup.html`), D and E generated |
| Build | `BOOKS` in `scripts/build_handbooks.py` includes `linux`; `python3 scripts/build_notes.py` |
| Cover | `.book--hb3` in `public/assets/bujo.css` (graphite `#2A2A2A`, silver band `#B5B5B5`) |
| PDFs | `handbooks/linux` added to `rebuild` in `pdf-build.json` |
| Story | `docs/stagedoor-casebook.md` §4 |

## 3. Part I (chapters 1–4): written 2026-11-27

| Ch. | Story (casebook §4) | Lab | Run here? |
| --- | --- | --- | --- |
| 1 | Mon 5 Jan 2026, Rafaela's first day; three server cards (Table 1.3) | `servercard.sh` (read-only inventory) + `chmod -x` break | **run**; output is this sandbox's (a Firecracker microVM, PID 1 `process_api`), which the text uses as a teaching point |
| 2 | Wed 4 Feb, Joana's question; `grep 500` = 381 vs 27 failed checkouts from 26 fans | `makelog.py` (seed 2026) + pipelines, quoting, exit codes, `pipefail` | **run** |
| 3 | week of 9 Feb, the app in `/root/stagedoor`; the FHS layout (Table 3.4) | hard/symlinks, release switch with `mv -T`, `strace ln -sfn`, deleted-but-open file | **run** as an unprivileged user `tiago` |
| 4 | 17–18 Feb, `/srv/uploads` 777 with Marco's files; personal accounts + sudo | 777 abuse → `2750` + umask `027`, setgid break, ACL, sudoers drop-in + `visudo -c` | **run** (as root via `sudo`, users created and removed) |

How the chapters were produced (the scripts live only in the session scratchpad; rewrite them, they're short):
chapter templates with `<!--FILE:…-->` / `<!--OUT:…-->` markers were assembled into the content files, so every printed
lab script is the file that was run and every printed output was captured from a real run. Shell command sequences
shown in labs were run in the same order; where a demo was run through `bash -c`, the printed output matches what an
interactive shell prints (the only edit: bash's "no job control" noise dropped in ch. 1's `Permission denied` demo).

Facts worth knowing (all verified in this environment, Ubuntu 24.04, coreutils 9.4):
- `ln -sfn` in coreutils 9.4 replaces a symlink atomically (temporary name + `renameat`); ch. 3 says older versions
  (e.g. Ubuntu 22.04's) removed the old link first, and recommends `mv -T` everywhere. Not verified on 22.04 itself.
- Ubuntu's default `awk` is `mawk`; RHEL/Amazon Linux use `gawk` (ch. 2).
- `/proc/loadavg` is "empty" to `file` and size 0 to `ls` (ch. 3).
- `userdel -r` warns about a missing mail spool (ch. 4 says so).
- This sandbox has **no systemd as PID 1**: chapters 6 (systemd), 15 (nftables) and anything needing services must be
  run in a full VM (Multipass in Appendix C), or written as "not run here" and said so. `strace`, `acl`, `shellcheck`,
  `iproute2` and `tree` were installed with apt (they're not in the base image).

Checks run for Part I: lab files byte-identical in the built pages; outputs present verbatim; unique ids across
`all.html`, `aria-labelledby` and SVG markers resolve; every `#ch`/`#app` link is in range; all 9 figures inspected at
1280 px light and dark and 375 px dark (fixed: 1.1's labels, 2.2's arrowheads, 4.1's font sizes); no page-level
horizontal overflow; print (A4) of `all.html`: 0 clipped blocks, 79 pages. Contents page and shelf card checked
("4 of 21 chapters", next-up badge on ch. 5).

**Not run:** the cloud-config in §1.4 is labelled an illustration (ch. 18 builds a tested one); stretch goals.

## 3b. Parts II and III (chapters 5–12): written 2026-11-27

**How the systemd chapters were run.** This sandbox's PID 1 isn't systemd, but Docker works: `dockerd` was started by
hand and an Ubuntu 24.04 image with `systemd`, `nginx-light`, `logrotate`, `cron`, `needrestart` and
`unattended-upgrades` was run as a privileged container (`--privileged --cgroupns=host -v /sys/fs/cgroup:/sys/fs/cgroup:rw
--tmpfs /run --tmpfs /run/lock`, hostname `lab`) with `/sbin/init` as PID 1. systemd 255 runs properly there (units,
restarts, journal, timers, `systemd-run` with `MemoryMax=`). The chapters say outputs came from “an Ubuntu 24.04
system container on the test machine”. Quirks noted in the text: the `CGroup:` line in `systemctl status` shows a
`/docker/…` prefix; the container's nofile hard ceiling was 20,000 (so the nginx lab uses 16384); IPv6 is disabled in
this kernel, so nginx's default `listen [::]:80` had to be removed before nginx would start (not mentioned in the book).

| Ch. | Story (casebook §4) | Lab | Run where |
| --- | --- | --- | --- |
| 5 | 26 Feb deploy kills checkouts | `checkout.py` (graceful SIGTERM), `fans.sh`, `zombie.py` | VM (TERM/KILL/graceful, short deadline); zombie also in the systemd container (reaped there, **not** reaped by this VM's PID 1: used as a teaching point) |
| 6 | payouts cron PATH; app becomes a service | `app.py`, `stagedoor.service`, `.env`, `payouts.*` | systemd container: install, status, SIGKILL restart, graceful stop, drop-in, ExecStart typo → restart loop → “Start request repeated too quickly” → `reset-failed`; cron; timer; `systemd-analyze calendar` (winter and `--base-time` summer) |
| 7 | 20 Mar disk full from DEBUG log | `logger`/journalctl; `chatty.py` on an 8 MB tmpfs; truncate via `/proc/<pid>/fd/3`; logrotate `create` (fails) vs `copytruncate` | systemd container |
| 8 | updates disabled since 2025; `door-1` EOL plan | apt/dpkg questions, `apt-mark hold`, auto-upgrade config | VM (apt works here); config files and timers from the container |
| 9 | 8 May backup in UTC | `burn.sh` ×8, `nice` on one CPU, `dd oflag=direct` D-state load | VM (4 vCPU) |
| 10 | 5 Jun OOM kills a PG backend | page cache, VSZ/RSS, `oom_score_adj`, `hog.py` under `MemoryMax=200M` | VM + container (kernel OOM line from `dmesg`) |
| 11 | 25 Jun inode exhaustion; `door-1` grown | loop device, GPT, ext4 `-N 2048`, inode exhaustion, `growpart`, resize, `findmnt --verify` | VM |
| 12 | 10 Jul nginx errno 24 | `holdserver.py`, `crowd.py`; accept queue; nginx `LimitNOFILE` drop-in | VM + container |

**Verified facts and honest gaps** (all said in the chapters where relevant):
- Ubuntu 24.04's cron inherits a full `PATH` (incl. `/usr/local/bin`), per the comment in its `/etc/crontab`, confirmed.
  Debian 11's cron `PATH=/usr/bin:/bin` is **from documentation, not run**: `deb.debian.org` is blocked here, so the lab
  sets `PATH=/usr/bin:/bin` in the crontab explicitly to reproduce `door-1`.
- `dpkg -S /usr/bin/ss` finds nothing on Ubuntu 24.04; `dpkg -S /bin/ss` finds `iproute2` (/usr merge). Used in ch. 8.
- Holding `binutils` kept back four dependants (ch. 8).
- Online `resize2fs` was refused in this sandbox (“Permission denied to resize filesystem”); ch. 11 says so and shows
  the offline resize that ran. **LVM wasn't run** (no device-mapper in this kernel): ch. 11 explains it without a lab.
- Setting a negative `oom_score_adj` was refused even as root here; ch. 10 doesn't claim what score −1000 shows.
- systemd in the container reported OOM kills as result `signal` (hybrid cgroups); ch. 10 says a cgroup v2 system may
  report `oom-kill`. Not verified on a pure cgroup v2 VM.
- The ch. 12 accept-queue step was cut short (a 1,500-connection crowd takes minutes to give up); the `ss`/`nstat`
  output printed is from that run, and the text tells readers to stop the crowd.
- Every lab file printed in chapters 1–12 is byte-identical to the file run; every printed output is from a real run
  (a few blocks were split from one run into the steps where they belong).

Checks for Parts II–III: same as Part I (ids, references, figures at 1280 px light/dark and 375 px dark, 16 new
figures inspected); print of `all.html` (12 chapters): 0 clipped blocks, 218 A4 pages. After Part IV (16 chapters): 0 clipped, 294 pages.

## 3c. Part IV (chapters 13–16): written 2026-11-27

**The lab network.** Outbound DNS and most hosts are blocked in this sandbox (only the agent proxy's HTTPS CONNECT
works), so Part IV's labs build their own network: `netlab.sh` (printed in ch. 13) creates network namespaces
`door-2`, `door-3`, `door-4` (`10.40.0.12/.13/.14`) on a bridge `br-lab` with the host as `10.40.0.1`, and
per-namespace `/etc/netns/<name>/resolv.conf`. dnsmasq on `10.40.0.1` serves lab names. Docker's `FORWARD DROP`
policy (with `br_netfilter`) blocked bridged traffic, so the script adds an `ACCEPT` in `DOCKER-USER` when that chain
exists; ch. 13 and 15 explain why. Packages installed here: `iputils-ping dnsmasq-base traceroute dnsutils tcpdump
ufw openssh-server openssh-client netcat-openbsd`. IPv6 is disabled in this kernel (ufw shows no v6 rules).

| Ch. | Story (casebook §4) | Lab | Run? |
| --- | --- | --- | --- |
| 13 | `door-4` dry run: localhost-only Postgres, stale `/etc/hosts` | `netlab.sh`; `ip`, `ip route get`, `nc -lk` on 127.0.0.1 vs `10.40.0.14`, dnsmasq + `dig`, `getent` vs `dig` | **run** |
| 14 | Sunday certificate expiry | `mkcerts.sh` (private CA via `openssl ca` with exact dates), `openssl s_server`, `curl -v`/exit 60, `s_client`, `-checkend`, `tcpdump` of plain HTTP | **run** (proxy env vars had to be unset for curl in the lab) |
| 15 | assessment: everything reachable | `door4.nft`, `probe.sh`; missing established rule; reject vs drop; ufw in a namespace (69 chains) | **run** |
| 16 | Marco's key in root's file | `sshd_lab.conf`, `sshlab.sh` (sshd per namespace, own host keys and `authorized_keys`), TOFU prompt via `script`, ProxyJump, locked vs expired account, audit, agent, user CA certificate, expired certificate | **run** |

**Verified while testing ch. 16 (used in the text):** with `UsePAM no`, sshd refuses key logins to a
password-locked account (“account is locked”); with `UsePAM yes` (Ubuntu's default) a password-locked account
(`usermod -L`) still logs in with a key, while an expired one (`usermod -e 1`) is refused by PAM's account check.
This supports ch. 4's claim and the casebook (Marco's own account was expired; his key in root's file still worked).

**Not run / not verified:** netplan (the namespaces have no netplan; §13.5's YAML is labelled an illustration);
`resolvectl` (no systemd-resolved here); `traceroute -T` (mentioned only); firewalld (RHEL box, prose only); Session
Manager and host certificates (prose and a stretch goal). Online facts quoted with “at the time of writing”: CA/B
Forum lifetimes (200 days from March 2026, 100 from 2027, 47 from 2029).

Checks: same as before; 8 new figures inspected (13.2 and 16.2 fixed); print check below.

## 3d. Parts V and VI (chapters 17–21) and appendices: written 2026-11-27

| Ch. | Story (casebook §4) | Lab | Run where |
| --- | --- | --- | --- |
| 17 | clean-up script deletes uploads | `cleanup-v1.sh` (disaster in a scratch tree), ShellCheck, `cleanup-releases.sh`, `tmpdemo.sh` | VM |
| 18 | assessment's other findings; a baseline | inventory, `systemd-analyze security` 9.2 → 1.5 with `hardening.conf`, ProtectSystem break, `cloud-init schema` on `baseline.yaml`, Lynis | systemd container (image `hb3-systemd2` adds nftables, openssh-server, cloud-init, lynis, apache2-utils) |
| 19 | 10-second container stops, zombies | `unshare` one namespace at a time, `minibox.sh` on an exported `ubuntu:24.04` rootfs, overlayfs whiteout, shell vs exec `CMD`, `--init`, cgroup of a container, OOM | VM + Docker (`python:3.12-slim`) |
| 20 | Tiago's first on-call | `first5.sh`, `mystery.sh` (disguised `dd` loop) | fresh systemd container `door-2` |
| 21 | `door-5` built, drilled | `build-web.sh` + `files/` + `keys/`: check, build, idempotent re-run, drift, `ab` drill (fails: app backlog 5), release 2026.11.2, drill again, crash drill | fresh systemd container `door-5` |

**Bugs found by testing, kept in the text as lessons:** `cleanup-releases.sh` counted one empty “release” with no
matches (ch. 17 says so); `hardening.conf` first had end-of-line comments, which systemd reads as values (logged
“path is not absolute, ignoring”, settings silently skipped, score 1.8): found by ch. 20's `first5.sh`; ch. 6 §6.7
and ch. 18 §18.4/§18.7 examples were also changed to comments-on-their-own-line, and both chapters now say why;
`build-web.sh` drafts: `set -e` off inside `if`, `grep -q` + `pipefail` SIGPIPE, release switched without restart,
`/run/sshd` missing before `sshd -t` on 24.04 (ch. 21 §21.3 lists all four). sshd itself tolerates end-of-line
comments (tested), so ch. 16's files were left as they were.

**Real findings used in the text:** Python's `http.server` listen backlog of 5 caused the first drill's 504s (ch. 21);
Docker reported `OOMKilled false` for a container the kernel had OOM-killed (cgroup v1 here; ch. 19 says to trust
the kernel log); a PID-1 shell (`/bin/sh -c`, dash) and a PID-1 Python without a handler both ignore SIGTERM (10 s,
137); an orphan under a Python PID 1 stays a zombie, `--init` reaps it.

**Not run here:** auditd rules (no kernel audit in the container; ch. 18 says so); the cloud-init baseline was
validated, not booted; `ab` drills ran on one machine against itself (not a real load-balanced pair).

**Appendices:** A (cheat sheet, grouped by question, every row from a chapter), B (distributions compared,
consolidated from the chapters' boxes), C (lab setup: Multipass recommended, which chapters need a VM, the package
list, how the labs were tested and what the test machine couldn't do). D: 162 terms; E: 126 answers.

Final checks: lab files byte-identical (checker), outputs verbatim, unique ids and resolving references across
`all.html`, every figure screenshotted at 1280 px light and dark and 375 px dark (each inspected at least once, 7 fixed), every page checked for overflow, appendices and contents page with
no page overflow, print of `all.html` 408 A4 pages with 0 clipped blocks.

## 4. Promises Part I made (keep them)

- Ch. 5: exit code 137 = 128 + SIGKILL; graceful restart so in-flight requests finish (ch. 3 promised).
- Ch. 6: the app becomes a systemd service as user `stagedoor` with `UMask=0027`, `EnvironmentFile=/etc/stagedoor/stagedoor.env`
  (ch. 4 quiz answer: `/etc/stagedoor` is `root:stagedoor 750`, the file `640`); the 03:00 cron job and PATH (ch. 2's
  warning box); `systemctl list-units` vs hand-started processes (ch. 1).
- Ch. 7: the full disk; truncating vs deleting an open log (ch. 3); `/var/log/auth.log` for sudo (ch. 4).
- Ch. 8: `door-1`'s Debian 11 support ends 31 Aug 2026; pending reboots, `/var/run/reboot-required`; `dpkg -S`.
- Ch. 11: deleted-but-open files and `lsof +L1` in depth.
- Ch. 16: Marco's key in root's `authorized_keys`; locking a password doesn't stop key logins.
- Ch. 17: `set -euo pipefail`, `${var:?}`, `mktemp`; ch. 18: setuid audit, SELinux, a tested cloud-init baseline;
  ch. 19: PID 1 in containers (ch. 1's sandbox card); ch. 21: rebuild from a script.
- Appendix A collects commands from every chapter; B the distribution differences (Tables 3.5, 4.4 and the "Across
  distributions" sections); C the lab setup (a container or WSL for most chapters; Multipass VM for systemd,
  firewall and networking labs; `sudo apt install acl strace` notes).

Promises from Parts II–III for later chapters:
- Ch. 14: the Sunday certificate expiry (casebook). Ch. 16: Marco's key in root's `authorized_keys` (ch. 4 says
  locking his password didn't stop key logins).
- Ch. 17: `set -euo pipefail`, `${var:?}`, `mktemp`, `exec` in wrappers (ch. 5); the deploy and maintenance scripts
  from ch. 5, 6 and 8 are natural examples.
- Ch. 18: harden `stagedoor.service` with the sandboxing lines previewed in ch. 6 §6.7 (`systemd-analyze security`);
  setuid audit (ch. 4); SELinux on RHEL (ch. 3, 4); a tested cloud-init baseline (ch. 1).
- Ch. 19: PID 1 must reap zombies (ch. 5's lab showed an orphan zombie left by a non-systemd PID 1); cgroups from
  ch. 10 (`MemoryMax=`) and ch. 9 (`CPUQuota=`) are the same mechanism containers use.
- Ch. 20: the USE method should reuse ch. 9–12's commands (vmstat, `df -i`, `/proc/<pid>/limits`, `nstat`).
- Ch. 21: rebuild a web server from a script; a load test against a copy (Joana's question, ch. 12); the new database
  server built from a checklist by end of August (ch. 8, 11).

## 5. Open items

- [ ] Run the systemd chapters' labs (6, 7, 10, 18, 20, 21) once on a real Ubuntu 24.04 VM (Multipass), especially
  cgroup v2 behaviour (ch. 10's `oom-kill` result, ch. 19's `memory.max`), online `resize2fs` (ch. 11), LVM, auditd.
- [ ] Boot `baseline.yaml` once with `multipass launch --cloud-init` (ch. 18).
- [ ] Run ch. 6's cron step on a real Debian 11 machine to confirm its default `PATH` (documented, not run).
- [ ] Confirm the Pages workflow renders Handbook 3's PDFs (listed in `pdf-build.json`).
- Handbook 4 (Kubernetes) is next in `docs/HANDOFF-handbooks-next.md`; Stagedoor's 2028 is its story.
