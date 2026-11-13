# Git Flow · a laminated reference card in four pages.
# Rendered by scripts/build_notes.py (render_cheatsheet) with the helpers in scripts/cheatsheet.py:
# Graph, cmd and box are injected into this module.
#
# Model: classic Git Flow. main = production, develop = integration (DEV/SIT), feature/* and bugfix/* off develop,
# release/* is what's deployed to UAT, hotfix/* off main for production emergencies.

SLUG = "git-flow"
TITLE = "Git Flow"
SUBTITLE = "branches, merges, releases, UAT and hotfixes"
DESC = ("A four-page Git Flow cheat sheet: the branch map, everyday feature and bug-fix work, merge strategies, "
        "conflicts, cutting a release, fixing UAT bugs, going live, hotfixes, rollbacks and undo commands.")
VERSION = "v1 · Nov 2026"
BLURB = ("Four laminated pages: the branch map, features and bug fixes, merge strategies, releases and UAT fixes, "
         "hotfixes, rollbacks and an undo table. Copy-paste commands for every scenario.")

# ---------------------------------------------------------------- page 1 · the map
MAP = (Graph("Git Flow at a glance: features merge into develop, a release branch is cut for UAT and merged into main "
             "and back into develop, a hotfix branches from main and merges into main and develop.",
             [("main", "main", "main", True), ("hot", "hotfix/*", "hot", False), ("rel", "release/*", "rel", False),
              ("dev", "develop", "dev", True), ("feat", "feature/*", "feat", False)], lane_h=50)
       .c("m0", 150, "main", tag="v1.0.0")
       .c("d0", 190, "dev")
       .c("f1", 240, "feat").c("f2", 290, "feat", note="small commits")
       .c("d1", 350, "dev", merge=True, note="PR merged", up=True)
       .c("d2", 400, "dev")
       .c("r0", 440, "rel", note="cut → UAT", up=True).c("r1", 510, "rel", note="UAT fix", up=True)
       .c("f3", 450, "feat").c("f4", 520, "feat", note="next release's work")
       .c("m1", 580, "main", tag="v1.1.0", merge=True)
       .c("d3", 600, "dev", merge=True)
       .c("h1", 660, "hot", note="prod fix", up=True)
       .c("d4", 680, "dev", merge=True)
       .c("m2", 750, "main", tag="v1.1.1", merge=True)
       .c("d5", 790, "dev", merge=True, note="back-merge", up=True)
       .e("m0", "d0").e("d0", "f1").e("f1", "f2").e("f2", "d1")
       .e("d2", "r0").e("r0", "r1").e("r1", "m1").e("r1", "d3")
       .e("d2", "f3").e("f3", "f4").e("f4", "d4")
       .e("m1", "h1").e("h1", "m2").e("h1", "d5"))

PAGE_MAP = dict(
    title="The map",
    kicker="five kinds of branch, two that live forever",
    figure=MAP.svg(),
    legend=[("main", "main", "production · tagged"), ("dev", "develop", "integration · DEV/SIT"),
            ("feat", "feature/*", "new work"), ("bug", "bugfix/*", "non-urgent fixes"),
            ("rel", "release/*", "frozen for UAT"), ("hot", "hotfix/*", "production emergency")],
    boxes=[
        box("The branches", '''
<div class="tbl-wrap"><table class="tbl">
<thead><tr><th>Branch</th><th>From</th><th>Merges into</th><th>Lives</th><th>Deploys to</th></tr></thead>
<tbody>
<tr><td><b class="b main">main</b></td><td>—</td><td>—</td><td>forever</td><td>PROD (each tag)</td></tr>
<tr><td><b class="b dev">develop</b></td><td>main, once</td><td>—</td><td>forever</td><td>DEV / SIT, auto</td></tr>
<tr><td><b class="b feat">feature/*</b></td><td>develop</td><td>develop</td><td>days</td><td>preview / DEV</td></tr>
<tr><td><b class="b bug">bugfix/*</b></td><td>develop <i>or</i> release/*</td><td>its parent</td><td>hours</td><td>with its parent</td></tr>
<tr><td><b class="b rel">release/*</b></td><td>develop</td><td>main <b>+</b> develop</td><td>until go-live</td><td>UAT / staging</td></tr>
<tr><td><b class="b hot">hotfix/*</b></td><td>main</td><td>main <b>+</b> develop<sup>†</sup></td><td>hours</td><td>PROD, after a check</td></tr>
</tbody></table></div>
<p class="fine">† or into the open <b class="b rel">release/*</b> if there is one; it reaches develop when the release finishes.</p>''', "ink", "wide"),
        box("Found a bug? Where to branch", '''
<ol class="tree">
<li><span class="q">Not released yet, found in <b>DEV / SIT</b></span><span class="a"><b class="b bug">bugfix/*</b> from <b class="b dev">develop</b> → PR into develop</span></li>
<li><span class="q">In the release, found in <b>UAT</b></span><span class="a"><b class="b bug">bugfix/*</b> from <b class="b rel">release/x.y.0</b> → PR into the release, then back-merge to develop</span></li>
<li><span class="q">In <b>PROD</b>, it can wait</span><span class="a">a normal <b class="b bug">bugfix/*</b> on develop; it ships with the next release</span></li>
<li class="hot"><span class="q">In <b>PROD</b>, it can't wait</span><span class="a"><b class="b hot">hotfix/x.y.z</b> from <b class="b main">main</b> → main (tag) + develop</span></li>
</ol>''', "warn", "", "decide first"),
        box("Golden rules", '''
<ol class="rules">
<li><b>main is production.</b> Every merge into main is a release and gets a tag.</li>
<li><b>No direct commits</b> on main, develop or release/*: protect them, use PRs.</li>
<li><b>Everything flows back.</b> Whatever lands on main or a release must reach develop.</li>
<li><b>A release branch is frozen:</b> only fixes, version bumps and release notes.</li>
<li><b>Short-lived branches.</b> Sync with the parent daily; merge within days.</li>
<li><b>One fix, one branch, one PR</b>, with a test that failed before the fix.</li>
</ol>'''),
        box("Names &amp; versions", '''
<dl class="kv">
<dt>feature</dt><dd><code>feature/PROJ-123-checkout-coupon</code></dd>
<dt>bugfix</dt><dd><code>bugfix/PROJ-456-vat-rounding</code></dd>
<dt>release</dt><dd><code>release/1.4.0</code></dd>
<dt>hotfix</dt><dd><code>hotfix/1.4.1</code></dd>
<dt>tag</dt><dd><code>v1.4.0</code> annotated, on main only</dd>
</dl>
<p class="semver"><b>MAJOR</b>.<b>MINOR</b>.<b>PATCH</b> <span>release → MINOR +1 (MAJOR if it breaks things) · hotfix → PATCH +1</span></p>'''),
        box("Environments", '''
<ol class="pipe">
<li><b class="b feat">feature/*</b><span>preview</span></li>
<li><b class="b dev">develop</b><span>DEV / SIT</span></li>
<li><b class="b rel">release/*</b><span>UAT</span></li>
<li><b class="b main">main + tag</b><span>PROD</span></li>
</ol>
<p class="fine">Deploy <b>tags</b> to PROD, not branch heads: a rollback is then just “deploy the previous tag”.</p>''', "dev"),
    ],
)

# ---------------------------------------------------------------- page 2 · everyday work
def mini(kind):
    lanes = [("dev", "develop", "dev", True), ("feat", "feature/x", "feat", False)]
    if kind == "merge":
        g = (Graph("Merge commit: the feature's commits stay, joined by a merge commit on develop.", lanes,
                   width=300, label_w=84, lane_h=44, pad_top=30, pad_bot=26)
             .c("d0", 110, "dev").c("f1", 150, "feat").c("f2", 195, "feat").c("d1", 250, "dev", merge=True, note="merge commit", up=True)
             .e("d0", "f1").e("f1", "f2").e("f2", "d1"))
    elif kind == "squash":
        g = (Graph("Squash: the feature's commits become one new commit on develop.", lanes,
                   width=300, label_w=84, lane_h=44, pad_top=30, pad_bot=26)
             .c("d0", 110, "dev").c("f1", 150, "feat", ghost=True).c("f2", 195, "feat", ghost=True)
             .c("d1", 250, "dev", cls="feat", note="1 new commit", up=True)
             .e("d0", "f1", dashed=True).e("f1", "f2", dashed=True).e("f2", "d1", dashed=True))
    else:
        g = (Graph("Rebase and fast-forward: the feature's commits are replayed on top of develop, in a straight line.", lanes,
                   width=300, label_w=84, lane_h=44, pad_top=30, pad_bot=26)
             .c("d0", 110, "dev").c("f1", 145, "feat", ghost=True).c("f2", 180, "feat", ghost=True)
             .c("d1", 175, "dev", note="others'", up=True)
             .c("r1", 222, "dev", cls="feat").c("r2", 262, "dev", cls="feat", note="replayed", up=True)
             .e("d0", "f1", dashed=True).e("f1", "f2", dashed=True))
    return g.svg()


PAGE_DAILY = dict(
    title="Everyday work",
    kicker="features, bug fixes, merging and conflicts",
    strategies=[
        ("Merge commit", "--no-ff", mini("merge"), "Keeps every commit and where the branch joined.",
         "<b>Use for</b> release → main, hotfix → main, all back-merges."),
        ("Squash", "--squash", mini("squash"), "One tidy commit per feature; branch commits are dropped.",
         "<b>Use for</b> feature/bugfix → develop. <b>Never</b> for release/hotfix."),
        ("Rebase + fast-forward", "rebase", mini("rebase"), "Straight-line history; rewrites the branch's commits.",
         "<b>Use for</b> updating your own private branch. Never on shared branches."),
    ],
    boxes=[
        box("Feature: start → merged", cmd('''
git switch develop && git pull
git switch -c feature/PROJ-123-coupon
# small commits, each one green
git add -p && git commit -m "PROJ-123 Add coupon field"
git push -u origin feature/PROJ-123-coupon
# open a PR → base: develop · CI green · 1+ review
# merge (squash), then tidy up
git switch develop && git pull
git branch -d feature/PROJ-123-coupon
'''), "feat", "wide", "the daily loop"),
        box("Bug fix, not yet released", cmd('''
git switch develop && git pull
git switch -c bugfix/PROJ-456-vat-rounding
# 1 write a test that fails
# 2 fix it, see it pass
git commit -am "PROJ-456 Round VAT per line"
git push -u origin bugfix/PROJ-456-vat-rounding
# PR → develop, merge (squash)
''') + '<p class="fine">Found in UAT or PROD instead? Turn the page.</p>', "bug"),
        box("Keep your branch up to date", '''
<p><b>A · rebase</b> <span class="pill">your own branch</span></p>''' + cmd('''
git fetch origin
git rebase origin/develop
git push --force-with-lease  # never plain --force
''') + '''<p><b>B · merge</b> <span class="pill">shared branch</span></p>''' + cmd('''
git fetch origin
git merge origin/develop
git push
''') + '<p class="fine">Do it daily: small syncs = small conflicts.</p>', "dev"),
        box("Resolve a conflict", '''
<ol class="cs-steps">
<li><code>git status</code> lists the conflicted files</li>
<li>Edit each one: keep the right code, delete the <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> <code>=======</code> <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> markers</li>
<li>Run the tests, then <code>git add &lt;file&gt;</code></li>
<li>Finish: <code>git commit</code> (merge) or <code>git rebase --continue</code></li>
</ol>''' + cmd('''
git merge --abort  # bail out of a merge
git rebase --abort  # bail out of a rebase
git checkout --theirs path/file  # take their side (in a merge)
git config --global rerere.enabled true  # remember resolutions
''') + '<p class="fine">In a <b>rebase</b>, <code>--ours</code> and <code>--theirs</code> are swapped: “ours” is the branch you rebase onto.</p>', "warn"),
        box("PR checklist", '''
<ul class="checks">
<li><b>Base branch</b> is right (develop · release/* · main)</li>
<li>Title has the ticket: <code>PROJ-123 …</code></li>
<li>Branch is up to date with its base</li>
<li>CI green, tests added for the change</li>
<li>Reviewed: 1+ approval, comments resolved</li>
<li>Strategy picked: squash or merge commit</li>
<li>Delete the branch after merging</li>
</ul>''', "ink"),
    ],
)

# ---------------------------------------------------------------- page 3 · releases & UAT
RELEASE = (Graph("A release: release/1.4.0 is cut from develop and deployed to UAT; a UAT bug is fixed on a bugfix branch "
                 "off the release and back-merged to develop; after sign-off the release merges into main as v1.4.0 and "
                 "back into develop. New features keep merging into develop for the next release.",
                 [("main", "main", "main", True), ("rel", "release/1.4.0", "rel", False), ("bug", "bugfix/*", "bug", False),
                  ("dev", "develop", "dev", True), ("feat", "feature/*", "feat", False)], label_w=124, lane_h=50)
           .c("m0", 160, "main", tag="v1.3.0")
           .c("d1", 220, "dev")
           .c("r0", 265, "rel", note="cut + bump", up=True)
           .c("b1", 345, "bug", note="UAT bug", up=True).c("b2", 395, "bug")
           .c("r2", 450, "rel", merge=True, note="redeploy UAT", up=True)
           .c("d3", 500, "dev", merge=True)
           .c("r3", 590, "rel", note="sign-off ✓", up=True)
           .c("f1", 300, "feat").c("f2", 400, "feat", note="not in 1.4.0")
           .c("d5", 560, "dev", merge=True)
           .c("m1", 680, "main", tag="v1.4.0", merge=True)
           .c("d4", 730, "dev", merge=True, note="back-merge", up=True)
           .c("x", 820, "main", note="deploy PROD", up=True, ghost=True)
           .e("m0", "d1").e("d1", "r0").e("r0", "b1").e("b1", "b2").e("b2", "r2")
           .e("r2", "d3").e("r2", "r3").e("r3", "m1").e("r3", "d4")
           .e("d1", "f1").e("f1", "f2").e("f2", "d5"))

PAGE_RELEASE = dict(
    title="Releases &amp; UAT",
    kicker="cut, test, fix, sign off, go live",
    figure=RELEASE.svg(),
    boxes=[
        box("1 · Cut the release", cmd('''
git switch develop && git pull
git switch -c release/1.4.0
# bump the version (package.json, pom.xml, …)
npm version 1.4.0 --no-git-tag-version
git commit -am "Bump version to 1.4.0"
git push -u origin release/1.4.0
> pipeline deploys release/1.4.0 → UAT
'''), "rel", "", "feature freeze"),
        box("2 · Fix a UAT bug", cmd('''
git switch release/1.4.0 && git pull
git switch -c bugfix/PROJ-789-uat-totals
# test + fix
git commit -am "PROJ-789 Fix basket totals"
git push -u origin bugfix/PROJ-789-uat-totals
# PR → base: release/1.4.0 (not develop!)
> merged → UAT redeploys → retest
'''), "bug", "", "UAT fix"),
        box("3 · Back-merge to develop", cmd('''
git switch develop && git pull
git merge --no-ff release/1.4.0
git push
# or a PR: release/1.4.0 → develop
''') + '<p class="fine">After every UAT fix, or at least daily, so develop never loses a fix. Merge, don\'t squash.</p>', "dev"),
        box("4 · Sign-off → go live", cmd('''
git switch main && git pull
git merge --no-ff release/1.4.0
git tag -a v1.4.0 -m "Release 1.4.0"
git push origin main v1.4.0
> deploy tag v1.4.0 → PROD
git switch develop && git pull
git merge --no-ff release/1.4.0 && git push
git push origin --delete release/1.4.0
git branch -d release/1.4.0
'''), "main", "", "finish"),
        box("Release scenarios", '''
<dl class="scen">
<dt>A feature fails UAT and must come out</dt>
<dd>Revert it on the release: <code>git revert -m 1 &lt;merge-sha&gt;</code> (merged) or <code>git revert &lt;sha&gt;</code> (squashed). Back-merge as usual. <b>!</b> To ship it later, first revert the revert on develop: <code>git revert &lt;revert-sha&gt;</code>.</dd>
<dt>New work is ready during UAT</dt>
<dd>It merges into <b class="b dev">develop</b> and waits for the next release. Never merge features into a release.</dd>
<dt>The release needs one fix that's already on develop</dt>
<dd><code>git switch release/1.4.0</code> then <code>git cherry-pick -x &lt;sha&gt;</code> (<code>-x</code> records where it came from).</dd>
<dt>UAT drags on, develop has moved far ahead</dt>
<dd>Keep fixing on the release. Don't re-cut it from develop: that pulls in untested work.</dd>
<dt>Two releases at once</dt>
<dd>Avoid it. Finish 1.4.0 first, then cut 1.5.0 from develop. If you must, merge 1.4.0's fixes forward into 1.5.0 too.</dd>
</dl>''', "warn", "wide"),
        box("Go-live checklist", '''
<ul class="checks">
<li>Version bumped on the release branch</li>
<li>Release notes / changelog written</li>
<li>UAT sign-off recorded (who, when)</li>
<li>DB migrations reviewed, backward compatible</li>
<li>Rollback plan: previous tag, data steps</li>
<li>Merged with <code>--no-ff</code>, tag pushed</li>
<li>Back-merged to develop, branch deleted</li>
</ul>''', "ink"),
    ],
)

# ---------------------------------------------------------------- page 4 · hotfixes, emergencies & undo
HOTFIX = (Graph("A hotfix while a release is open: hotfix/1.4.1 branches from main at v1.4.0, merges into main as v1.4.1 "
                "and into the open release/1.5.0; when 1.5.0 finishes, the fix reaches develop with it.",
                [("main", "main", "main", True), ("hot", "hotfix/1.4.1", "hot", False), ("rel", "release/1.5.0", "rel", False),
                 ("dev", "develop", "dev", True)], label_w=124, lane_h=50)
          .c("m0", 170, "main", tag="v1.4.0")
          .c("d0", 200, "dev")
          .c("h1", 235, "hot", note="from main!", up=True).c("h2", 345, "hot", note="fix + bump 1.4.1", up=True)
          .c("r0", 290, "rel", note="cut", up=True)
          .c("m1", 420, "main", tag="v1.4.1", merge=True)
          .c("r1", 460, "rel", merge=True, note="hotfix in", up=True)
          .c("r2", 560, "rel", note="UAT fix", up=True)
          .c("m2", 690, "main", tag="v1.5.0", merge=True)
          .c("d2", 740, "dev", merge=True, note="fix reaches develop", up=True)
          .e("m0", "h1").e("h1", "h2").e("h2", "m1").e("h2", "r1")
          .e("d0", "r0").e("r0", "r1").e("r1", "r2").e("r2", "m2").e("r2", "d2"))

PAGE_HOTFIX = dict(
    title="Hotfixes &amp; emergencies",
    kicker="production is broken: branch from main",
    figure=HOTFIX.svg(),
    boxes=[
        box("Hotfix, step by step", cmd('''
git switch main && git pull
git switch -c hotfix/1.4.1
# test + fix + bump the version to 1.4.1
git commit -am "Fix payment timeout; bump to 1.4.1"
git push -u origin hotfix/1.4.1
# PR → base: main · quick check on staging
git switch main && git pull
git tag -a v1.4.1 -m "Hotfix 1.4.1"
git push origin v1.4.1
> deploy tag v1.4.1 → PROD
# then bring the fix back (merge, not squash):
git switch develop && git pull  # or release/1.5.0 if open
git merge --no-ff hotfix/1.4.1 && git push
git push origin --delete hotfix/1.4.1
'''), "hot", "", "urgent"),
        box("Which fix is it?", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th></th><th><b class="b bug">bugfix</b></th><th><b class="b rel">UAT fix</b></th><th><b class="b hot">hotfix</b></th></tr></thead>
<tbody>
<tr><th>Found in</th><td>DEV / SIT</td><td>UAT</td><td>PROD</td></tr>
<tr><th>Branch from</th><td>develop</td><td>release/x.y.0</td><td>main</td></tr>
<tr><th>PR into</th><td>develop</td><td>release/x.y.0</td><td>main</td></tr>
<tr><th>Then</th><td>—</td><td>back-merge → develop</td><td>→ develop or open release</td></tr>
<tr><th>Version</th><td>—</td><td>unchanged</td><td>PATCH +1, tag</td></tr>
<tr><th>Ships</th><td>next release</td><td>this release</td><td>now</td></tr>
</tbody></table></div>''', "ink"),
        box("Emergency scenarios", '''
<dl class="scen">
<dt>The release is bad, roll back now</dt>
<dd>Redeploy the previous tag (<code>v1.4.0</code>) from the pipeline: no git change. Then fix forward with a hotfix.</dd>
<dt>Undo a merge that's already on main</dt>
<dd><code>git revert -m 1 &lt;merge-sha&gt;</code> on a hotfix branch → PR → tag <code>v1.4.2</code>. <code>-m 1</code> keeps main's side.</dd>
<dt>Forgot to bring a hotfix back</dt>
<dd><code>git switch develop</code>, <code>git merge --no-ff v1.4.1</code>. Spot it: <code>git log --oneline develop..main</code> should show only merge commits.</dd>
<dt>Also needed on an older version</dt>
<dd><code>git switch -c support/1.3 v1.3.2</code>, <code>git cherry-pick -x &lt;sha&gt;</code>, tag <code>v1.3.3</code>.</dd>
<dt>Committed on develop by mistake (not pushed)</dt>
<dd><code>git branch feature/x</code>, <code>git reset --hard origin/develop</code>, <code>git switch feature/x</code>.</dd>
<dt>Pushed a password or key</dt>
<dd><b>Rotate it first</b>: it is already leaked. Then scrub history with <code>git filter-repo</code>, with the whole team.</dd>
</dl>''', "warn", "wide"),
        box("Undo table", '''
<div class="tbl-wrap"><table class="tbl undo">
<tbody>
<tr><th>Unstage a file</th><td><code>git restore --staged f</code></td></tr>
<tr><th>Throw away local edits</th><td><code>git restore f</code></td></tr>
<tr><th>Fix the last commit (unpushed)</th><td><code>git commit --amend</code></td></tr>
<tr><th>Undo last commit, keep changes</th><td><code>git reset --soft HEAD~1</code></td></tr>
<tr><th>Undo a pushed commit</th><td><code>git revert &lt;sha&gt;</code></td></tr>
<tr><th>Park work in progress</th><td><code>git stash push -m wip</code> · <code>git stash pop</code></td></tr>
<tr><th>Find a “lost” commit</th><td><code>git reflog</code></td></tr>
</tbody></table></div>
<p class="fine"><b>Pushed?</b> Then revert, don't reset: others already have those commits.</p>''', "dev"),
        box("Health checks &amp; git-flow CLI", cmd('''
git log --oneline --graph --decorate --all
git branch --merged develop  # safe to delete
git log --oneline develop..main  # missing back-merges
git flow init -d
git flow feature start PROJ-123-coupon
git flow release start 1.4.0
git flow release finish 1.4.0  # merges + tags
git flow hotfix start 1.4.1
git push origin main develop --tags
''') + '<p class="fine"><code>git flow</code> (git-flow AVH) only automates the merges above. It never pushes for you.</p>', "ink"),
    ],
)

PAGES = [PAGE_MAP, PAGE_DAILY, PAGE_RELEASE, PAGE_HOTFIX]
