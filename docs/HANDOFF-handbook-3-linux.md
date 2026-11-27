# Handoff: Handbook 3 · Linux for Cloud Engineers

Status as of **2026-11-27**: **started. Part I (chapters 1–4) written and checked**; chapters 5–21 and appendices
A–C still to write (D and E are generated). `BOOK["next"] = 5`.

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
| Outline | `content/handbooks/linux/book.py` (key `linux`, no. 3, `next=5`) |
| Chapters | `content/handbooks/linux/<nn>-<slug>.html`; written: 01–04 |
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

## 5. Next

1. Part II (5–8). Ch. 5 can run here (Python server + signals). **Ch. 6 needs systemd**: try a Multipass or
   other VM; if none is available, write the unit files, check them with `systemd-analyze verify` if possible, and
   say plainly in the chapter and here what wasn't run. Ch. 7 (logrotate can run here; journald can't), ch. 8 (apt).
2. Then Parts III–VI in order, appendices A–C, then remove `next` from `book.py`.
3. After each part: the checks in `HANDOFF-handbooks-next.md` §0.8, update this file and the casebook.
