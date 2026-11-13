# Shell, network & connectivity diagnostics · a laminated reference card in five pages.
# Rendered by scripts/build_notes.py (render_cheatsheet); Graph, Diagram, cmd, code and box come from scripts/cheatsheet.py.
# Linux first; macOS and Windows equivalents on the last card.
# Boxes flow into a 3-column grid (dense packing), so order them to fill rows: wide (2) + narrow (1).

SLUG = "shell-network"
TITLE = "Shell & Network"
SUBTITLE = "shell power tools, connectivity diagnostics, HTTP, TLS, DNS and SSH tunnels"
DESC = ("A five-page cheat sheet for shell and network diagnostics: pipes and text tools, processes and disk, walking the "
        "network layers from DNS to the app, ports, curl timings, TLS certificates, tcpdump, an error-message decoder and SSH tunnels.")
VERSION = "v1 · Nov 2026"
BLURB = ("Five laminated pages: shell pipes and power tools, walking the network layers from DNS to the app, HTTP and "
         "TLS with curl and openssl, a decoder for the error messages you actually see, and SSH tunnels.")
LOGO = ('<svg viewBox="0 0 34 34" aria-hidden="true"><rect width="34" height="34" rx="8" fill="#FFFFFF" fill-opacity=".1"/>'
        '<path d="M7 11l5 4-5 4" fill="none" stroke="var(--b-feat)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M14 21h6" stroke="var(--b-feat)" stroke-width="2.4" stroke-linecap="round"/>'
        '<circle cx="25" cy="10" r="3" fill="var(--b-dev)"/><circle cx="25" cy="24" r="3" fill="var(--b-dev)"/>'
        '<path d="M25 13v8" stroke="var(--b-dev)" stroke-width="2"/></svg>')

# ---------------------------------------------------------------- page 1 · shell
def pipeline():
    d = Diagram("A shell pipeline: read access.log, keep lines with status 500, print the URL field, sort, count duplicates, "
                "sort by count descending, show the top 10: the URLs failing most often.", 880, 118)
    steps = [("access.log", "the input", "ink"), ("grep ' 500 '", "keep matches", "bug"), ("awk '{print $7}'", "pick field 7", "dev"),
             ("sort", "group equal lines", "feat"), ("uniq -c", "count each", "feat"), ("sort -rn", "biggest first", "rel"),
             ("head -10", "top 10", "main")]
    x = 14
    for i, (label, sub, tone) in enumerate(steps):
        d.node(f"s{i}", x, 16, 116, 50, label, sub, tone)
        if i:
            d.arrow(f"s{i - 1}", f"s{i}", "|", tone="ink", ly=37)
        x += 122
    d.text(14, 90, "$ grep ' 500 ' access.log | awk '{print $7}' | sort | uniq -c | sort -rn | head -10", "dt strong")
    d.text(14, 108, "→ “which URLs fail most?” in one line. Each tool does one thing; | passes stdout to the next tool's stdin.")
    return d.svg()


PAGE_SHELL = dict(
    title="Shell power tools",
    kicker="find it, slice it, count it, watch it",
    figure=pipeline(),
    boxes=[
        box("Find &amp; search", cmd('''
grep -rn "timeout" src/  # recursive, with line numbers
grep -rniE "error|fatal" --include=*.log .
rg "TODO" -g '!node_modules'  # ripgrep: faster, respects .gitignore
find . -name "*.log" -mtime -1  # changed in the last day
find / -type f -size +500M 2>/dev/null  # big files
find . -name "*.tmp" -delete  # ! check without -delete first
grep -c "500" access.log  # count matching lines
'''), "bug", "wide", "daily"),
        box("Redirects &amp; chaining", '''
<dl class="kv">
<dt><code>a | b</code></dt><dd>stdout of a → stdin of b</dd>
<dt><code>&gt; f</code> · <code>&gt;&gt; f</code></dt><dd>write · append to a file</dd>
<dt><code>2&gt;&amp;1</code></dt><dd>errors go where stdout goes</dd>
<dt><code>2&gt;/dev/null</code></dt><dd>throw errors away</dd>
<dt><code>| tee f</code></dt><dd>show and save</dd>
<dt><code>a &amp;&amp; b</code></dt><dd>b only if a succeeded</dd>
<dt><code>a || b</code></dt><dd>b only if a failed</dd>
<dt><code>$(cmd)</code></dt><dd>insert a command's output</dd>
<dt><code>echo $?</code></dt><dd>last exit code (0 = ok)</dd>
</dl>
<p class="fine">Scripts: start with <code>set -euo pipefail</code> so errors stop the script.</p>''', "ink"),
        box("Slice &amp; count text", cmd('''
awk -F, '{s += $3} END {print s}' sales.csv  # sum column 3
awk '$9 >= 500' access.log  # rows where field 9 ≥ 500
cut -d: -f1 /etc/passwd  # field 1, ':' separated
sed -n '100,120p' app.log  # print lines 100-120
sed -i 's/old/new/g' file  # replace in place (macOS: -i '')
sort | uniq -c | sort -rn  # frequency count
wc -l file  # count lines
cat urls.txt | xargs -n1 -P4 curl -sI  # 4 in parallel
'''), "dev", "wide"),
        box("JSON with jq", cmd('''
jq . file.json  # pretty print
jq -r '.items[].name' file.json
jq '.items[] | {name, status}' file.json
jq '.items | length' file.json
jq '.[] | select(.status == "failed")'
kubectl get pods -o json | jq -r '.items[].metadata.name'
'''), "feat"),
        box("Logs &amp; live views", cmd('''
tail -f app.log  # follow
tail -n 200 app.log | less  # / to search, n next
less +F app.log  # follow; Ctrl-C to scroll
journalctl -u nginx -f --since "10 min ago"
watch -n 2 'ss -s'  # rerun every 2 s
'''), "rel"),
        box("Processes, memory &amp; disk", cmd('''
ps aux --sort=-%mem | head  # memory hogs
pgrep -fa java  # find by command line
top  # or htop · P cpu, M memory
kill -TERM 1234  # ask nicely; -9 only as a last resort
free -h · uptime  # memory · load average
df -h  # disk full?
du -sh * | sort -h  # what is big here
df -i  # out of inodes (lots of tiny files)
'''), "main", "wide"),
        box("Keyboard savers", '''
<dl class="kv">
<dt><code>Ctrl-R</code></dt><dd>search history</dd>
<dt><code>!!</code> · <code>sudo !!</code></dt><dd>repeat the last command (as root)</dd>
<dt><code>!$</code></dt><dd>last argument of the last command</dd>
<dt><code>Ctrl-A / E</code></dt><dd>start / end of line</dd>
<dt><code>Ctrl-Z</code> · <code>bg</code></dt><dd>pause · continue in the background</dd>
<dt><code>nohup cmd &amp;</code></dt><dd>keep running after logout (or tmux)</dd>
<dt><code>time cmd</code></dt><dd>how long it took</dd>
</dl>''', "hot"),
    ],
)

# ---------------------------------------------------------------- page 2 · walk the layers
def layers():
    d = Diagram("Walk the layers from the bottom up: is my network up, does DNS resolve, is the host reachable, is the port "
                "open, does TLS work, does HTTP answer, is the app healthy. Each step has a command and a typical cause when "
                "it fails.", 880, 300)
    rows = [
        ("1 · My network up?", "ip -br a · ip route · ping -c3 <gateway>", "no IP, wrong gateway, VPN down", "ink"),
        ("2 · DNS resolves?", "dig +short api.example.com · getent hosts api…", "typo, NXDOMAIN, wrong resolver", "rel"),
        ("3 · Host reachable?", "ping -c3 host · mtr -rwc 20 host", "routing, firewall, host down", "bug"),
        ("4 · Port open?", "nc -vz -w3 host 443 · (server) ss -tlnp", "refused / timeout: see card 4", "dev"),
        ("5 · TLS OK?", "openssl s_client -connect host:443 -servername host", "expired, wrong name, missing chain", "hot"),
        ("6 · HTTP answers?", "curl -sv https://host/health -o /dev/null", "4xx / 5xx, proxy, redirects", "feat"),
        ("7 · App healthy?", "logs · metrics · status page · kubectl get pods", "the bug is finally in the app", "main"),
    ]
    for i, (step, how, why, tone) in enumerate(rows):
        y = 8 + i * 41
        d.node(f"s{i}", 14, y, 176, 33, step, None, tone)
        d.node(f"c{i}", 206, y, 420, 33, how, None, tone, "soft chip")
        d.node(f"w{i}", 642, y, 224, 33, why, None, tone, "ghost")
        d.arrow(f"s{i}", f"c{i}", None, tone=tone)
        if i:
            d.arrow(f"s{i - 1}", f"s{i}", None, sides="bt", tone="ink")
    return d.svg()


PAGE_LAYERS = dict(
    title="Walk the layers",
    kicker="bottom up: the first step that fails is your problem",
    figure=layers(),
    boxes=[
        box("DNS", cmd('''
dig +short api.example.com  # just the answer
dig api.example.com  # TTL, which server answered
dig @1.1.1.1 api.example.com  # ask another resolver
dig api.example.com CNAME +short  # follow aliases
dig example.com MX · TXT · NS
dig +trace example.com  # from the root down
dig -x 10.0.0.5  # reverse lookup
getent hosts api.example.com  # what apps see (/etc/hosts too)
''') + '<p class="fine"><b>dig skips /etc/hosts</b>; <code>getent</code> doesn\'t. Changed a record? Old answers live until the TTL runs out. Flush: <code>resolvectl flush-caches</code>.</p>', "rel", "wide", "it's always DNS"),
        box("Reachability", cmd('''
ping -c 3 host
mtr -rwc 20 host  # loss per hop
traceroute -T -p 443 host  # TCP: passes firewalls
ip route get 10.0.0.5  # which way out
''') + '<p class="fine">No ping reply ≠ down: many hosts and clouds block ICMP. Test the real port instead.</p>', "bug"),
        box("Ports: who listens, who answers", cmd('''
nc -vz -w 3 db.internal 5432  # client: can I connect?
ss -tlnp  # server: what listens, which process
ss -tlnp | grep :8080
lsof -i :8080  # who holds this port
ss -tnp state established  # live connections
curl -v telnet://host:6379  # no nc? curl can do it
''') + '<p class="fine">Listening on <code>127.0.0.1:8080</code> = only this machine. On <code>0.0.0.0</code> / <code>[::]</code> = every interface.</p>', "dev", "wide"),
        box("My machine's network", cmd('''
ip -br a  # interfaces + IPs
ip route  # default gateway
cat /etc/resolv.conf  # which DNS
resolvectl status  # systemd-resolved
env | grep -i proxy  # proxy set?
curl -s ifconfig.me  # my public IP
'''), "ink"),
        box("Firewalls &amp; filters", '''
<ul class="checks">
<li>Host: <code>sudo nft list ruleset</code> · <code>iptables -L -n -v</code> · <code>ufw status</code></li>
<li>Cloud: security group <b>and</b> network ACL <b>and</b> route table</li>
<li>Kubernetes: a NetworkPolicy may deny by default</li>
<li>Corporate: proxy, VPN split tunnel, egress allow-list</li>
<li>Both ways: the reply has to get back too</li>
</ul>''', "main"),
        box("CIDR quick math", '''
<dl class="kv two">
<dt><code>/32</code></dt><dd>1 address</dd>
<dt><code>/24</code></dt><dd>256 (254 hosts)</dd>
<dt><code>/28</code></dt><dd>16</dd>
<dt><code>/20</code></dt><dd>4,096</dd>
<dt><code>/26</code></dt><dd>64</dd>
<dt><code>/16</code></dt><dd>65,536</dd>
</dl>
<p class="fine">Private: <code>10.0.0.0/8</code> · <code>172.16.0.0/12</code> · <code>192.168.0.0/16</code>. Cloud subnets reserve ~5 addresses each.</p>''', "feat"),
    ],
)

# ---------------------------------------------------------------- page 3 · HTTP & TLS
def timeline():
    d = Diagram("Where a request's time goes, as curl reports it: DNS lookup, TCP connect, TLS handshake, server processing "
                "until the first byte, then the download. time_namelookup, time_connect, time_appconnect, "
                "time_starttransfer and time_total are cumulative.", 880, 160)
    segs = [("DNS", "lookup", 14, 120, "rel"), ("TCP", "connect", 134, 130, "bug"), ("TLS", "handshake", 264, 170, "hot"),
            ("Server", "waiting for the first byte", 434, 290, "dev"), ("Download", "body", 724, 142, "feat")]
    for i, (label, sub, x, w, tone) in enumerate(segs):
        d.node(f"t{i}", x, 22, w, 46, label, sub, tone)
    marks = [(134, "time_namelookup"), (264, "time_connect"), (434, "time_appconnect"), (724, "time_starttransfer"), (866, "time_total")]
    for i, (x, var) in enumerate(marks):
        y = 92 if i % 2 == 0 else 110
        d.raw(f'<path class="ar t-ink" d="M{x} 70 V{y - 12}"/>')
        d.text(x, y, var, "dt strong", "end" if i == 4 else "middle")
    d.text(14, 138, "Slow DNS → resolver · slow TCP → distance or packet loss · slow TLS → handshake, OCSP, no keep-alive · ")
    d.text(14, 154, "slow first byte → the app, the database, a downstream call · slow download → size, compression, bandwidth")
    return d.svg()


PAGE_HTTP = dict(
    title="HTTP &amp; TLS",
    kicker="curl for requests, openssl for certificates",
    figure=timeline(),
    boxes=[
        box("curl recipes", cmd('''
curl -v https://api.example.com/health  # headers + TLS details
curl -sSI https://example.com  # response headers only
curl -sSL https://example.com  # follow redirects
curl -H "Authorization: Bearer $TOKEN" https://api.example.com/me
curl -X POST -H "Content-Type: application/json" -d '{"sku":"A1","qty":2}' https://api.example.com/orders
curl --resolve api.example.com:443:10.0.0.5 https://api.example.com/  # test one server, real hostname
curl --connect-timeout 3 --max-time 10 https://slow.example.com
curl -x http://proxy:8080 https://example.com  # through a proxy
curl -sS -o /dev/null -w '%{http_code} dns=%{time_namelookup} tcp=%{time_connect} tls=%{time_appconnect} ttfb=%{time_starttransfer} total=%{time_total}\\n' https://example.com
'''), "feat", "wide", "daily"),
        box("Status codes when debugging", '''
<dl class="kv">
<dt><code>301/302</code></dt><dd>redirect: <code>-L</code> to follow; loops?</dd>
<dt><code>400</code></dt><dd>bad request: body, headers, JSON</dd>
<dt><code>401</code></dt><dd>no or bad credentials</dd>
<dt><code>403</code></dt><dd>known, but not allowed (or WAF)</dd>
<dt><code>404</code></dt><dd>wrong path, host or Ingress rule</dd>
<dt><code>407</code></dt><dd>the proxy wants credentials</dd>
<dt><code>429</code></dt><dd>rate limited: back off</dd>
<dt><code>502</code></dt><dd>proxy got a bad reply: upstream crashed / wrong port</dd>
<dt><code>503</code></dt><dd>no healthy upstream / overloaded</dd>
<dt><code>504</code></dt><dd>upstream too slow for the proxy's timeout</dd>
</dl>''', "dev"),
        box("Certificates with openssl", cmd('''
openssl s_client -connect host:443 -servername host </dev/null  # handshake + chain
openssl s_client -connect host:443 -servername host </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates -ext subjectAltName
openssl x509 -in cert.pem -noout -text  # read a file
openssl s_client -connect smtp.example.com:587 -starttls smtp
'''), "hot", "wide", "TLS"),
        box("TLS errors decoded", '''
<dl class="kv stack">
<dt>expired</dt><dd>check <code>notAfter</code>; renew; automate it</dd>
<dt>name mismatch</dt><dd>host not in SAN; wrong <code>-servername</code> (SNI)</dd>
<dt>unable to get local issuer</dt><dd>missing intermediate on the server, or a corporate CA not trusted by the client</dd>
<dt>self-signed</dt><dd>trust that CA explicitly; never <code>-k</code> in prod</dd>
<dt>handshake failure</dt><dd>no common TLS version / cipher; mTLS cert missing</dd>
</dl>''', "main"),
        box("Proxies &amp; trust", '''
<ul class="checks">
<li><code>HTTPS_PROXY</code>, <code>HTTP_PROXY</code>, <code>NO_PROXY</code> (some tools only read lowercase)</li>
<li><code>NO_PROXY</code> must list internal hosts, <code>localhost</code>, cluster domains</li>
<li>TLS-inspecting proxy? Add its CA: <code>/usr/local/share/ca-certificates</code> + <code>update-ca-certificates</code></li>
<li>Node, Python, Java keep their own trust stores: <code>NODE_EXTRA_CA_CERTS</code>, <code>REQUESTS_CA_BUNDLE</code>, <code>keytool</code></li>
</ul>''', "rel", "wide"),
        box("Headers worth reading", '''
<dl class="kv">
<dt>server, via</dt><dd>which proxy / CDN answered</dd>
<dt>x-cache, age</dt><dd>served from a cache?</dd>
<dt>location</dt><dd>where a redirect points</dd>
<dt>www-authenticate</dt><dd>which auth is expected</dd>
<dt>retry-after</dt><dd>when to try again</dd>
<dt>x-request-id</dt><dd>quote it to the API owner</dd>
</dl>''', "ink"),
    ],
)

# ---------------------------------------------------------------- page 4 · symptoms, capture, other systems
PAGE_DECODE = dict(
    title="Errors decoded",
    kicker="what the message means, where to look next",
    boxes=[
        box("Error message → likely cause → check", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>You see</th><th>It usually means</th><th>Check</th></tr></thead>
<tbody>
<tr><th>Connection refused</th><td>host reached, <b>nothing listening</b> on that port (or app bound to 127.0.0.1)</td><td><code>ss -tlnp</code> on the server; right port?</td></tr>
<tr><th>Connection timed out</th><td>packets <b>silently dropped</b>: firewall, security group, routing, host down</td><td>SG / NACL / NetworkPolicy; <code>mtr</code>; from another host</td></tr>
<tr><th>No route to host</th><td>no route, or a firewall answering with reject</td><td><code>ip route get</code>; VPN; subnet</td></tr>
<tr><th>Could not resolve host · NXDOMAIN</th><td>DNS: typo, missing record, wrong resolver, private zone</td><td><code>dig</code>, <code>getent hosts</code>, <code>resolv.conf</code></td></tr>
<tr><th>Connection reset by peer</th><td>the other side or a middlebox <b>killed</b> it: crash, idle timeout, TLS vs plain HTTP</td><td>server logs; LB idle timeout; http vs https</td></tr>
<tr><th>SSL certificate problem</th><td>expired, name mismatch, untrusted / missing chain</td><td><code>openssl s_client</code> (card 3)</td></tr>
<tr><th>502 · 504 from the LB</th><td>502: upstream down / wrong port · 504: upstream too slow</td><td>targets healthy? timeouts on each hop</td></tr>
<tr><th>Works by IP, not by name</th><td>DNS, or the server needs the <b>Host / SNI</b> name</td><td><code>curl --resolve</code></td></tr>
<tr><th>Works locally, not in a container</th><td><code>localhost</code> inside a container is the container itself</td><td>use the service name / <code>host.docker.internal</code></td></tr>
<tr><th>Sometimes fails</th><td>one bad backend, DNS round-robin, exhausted pool, MTU</td><td>repeat 50×; per-backend logs; <code>ping -M do -s 1472</code></td></tr>
</tbody></table></div>''', "main", "full"),
        box("Capture packets", cmd('''
sudo tcpdump -i any -nn port 443  # watch traffic on a port
sudo tcpdump -i any -nn host 10.0.0.5 and port 5432
sudo tcpdump -i any -nn -w cap.pcap port 8080  # save → open in Wireshark
sudo tcpdump -i any -nn 'tcp[tcpflags] & tcp-rst != 0'  # who sends resets
''') + '<p class="fine">SYN sent, no reply → dropped (firewall). SYN answered by RST → refused (nothing listening).</p>', "dev", "wide"),
        box("Containers &amp; Kubernetes", cmd('''
docker network inspect bridge
docker exec -it web sh -c 'nc -vz db 5432'
kubectl run net --rm -it --image=nicolaka/netshoot -- bash
kubectl exec -it web -- curl -sv http://api.shop:8080/health
kubectl get endpoints api -n shop
'''), "bug"),
        box("macOS &amp; Windows", '''
<div class="tbl-wrap"><table class="tbl cmp">
<thead><tr><th>Linux</th><th>macOS</th><th>Windows (PowerShell)</th></tr></thead>
<tbody>
<tr><td><code>ip a</code></td><td><code>ifconfig</code></td><td><code>ipconfig /all</code></td></tr>
<tr><td><code>dig</code> / <code>getent</code></td><td><code>dig</code> · <code>dscacheutil -q host -a name h</code></td><td><code>Resolve-DnsName h</code></td></tr>
<tr><td><code>nc -vz h 443</code></td><td><code>nc -vz h 443</code></td><td><code>Test-NetConnection h -Port 443</code></td></tr>
<tr><td><code>ss -tlnp</code></td><td><code>lsof -nP -iTCP -sTCP:LISTEN</code></td><td><code>netstat -ano | findstr LISTEN</code></td></tr>
<tr><td><code>traceroute</code> · <code>mtr</code></td><td><code>traceroute</code></td><td><code>tracert</code> · <code>pathping</code></td></tr>
<tr><td><code>resolvectl flush-caches</code></td><td><code>sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder</code></td><td><code>ipconfig /flushdns</code></td></tr>
</tbody></table></div>''', "ink", "wide"),
        box("Ports to know", '''
<dl class="kv two">
<dt><code>22</code></dt><dd>SSH</dd>
<dt><code>53</code></dt><dd>DNS</dd>
<dt><code>80 · 443</code></dt><dd>HTTP · HTTPS</dd>
<dt><code>25 · 587</code></dt><dd>SMTP</dd>
<dt><code>5432</code></dt><dd>Postgres</dd>
<dt><code>3306</code></dt><dd>MySQL</dd>
<dt><code>1433</code></dt><dd>SQL Server</dd>
<dt><code>6379</code></dt><dd>Redis</dd>
<dt><code>27017</code></dt><dd>MongoDB</dd>
<dt><code>9092</code></dt><dd>Kafka</dd>
<dt><code>5672</code></dt><dd>RabbitMQ</dd>
<dt><code>6443</code></dt><dd>K8s API</dd>
</dl>''', "feat"),
    ],
)

# ---------------------------------------------------------------- page 5 · ssh & tunnels
def tunnels():
    d = Diagram("SSH tunnels. Local forward: a port on your laptop reaches a private database through a bastion. Remote "
                "forward: a port on the server reaches a service on your laptop. Dynamic forward: a SOCKS proxy on your "
                "laptop sends any traffic out through the server. Jump host: SSH to a private host through a bastion.",
                880, 246)
    rows = [
        ("-L  local", "ssh -L 5432:db.internal:5432 bastion", "laptop", "localhost:5432", "bastion", "ssh :22",
         "db.internal", ":5432 (private)", "dev"),
        ("-R  remote", "ssh -R 8080:localhost:3000 server", "server", "localhost:8080", "ssh link", "back to you",
         "laptop", "localhost:3000", "feat"),
        ("-D  dynamic", "ssh -D 1080 bastion", "browser / curl", "SOCKS 127.0.0.1:1080", "bastion", "ssh :22",
         "any host", "the bastion can reach", "rel"),
        ("-J  jump", "ssh -J bastion app.internal", "laptop", "ssh", "bastion", "relays :22",
         "app.internal", "shell on a private host", "hot"),
    ]
    for i, (kind, cmdline, a, asub, b, bsub, c, csub, tone) in enumerate(rows):
        y = 6 + i * 60
        d.node(f"k{i}", 14, y + 3, 112, 38, kind, None, tone, "chip")
        d.node(f"a{i}", 150, y, 150, 44, a, asub, tone, "soft")
        d.node(f"b{i}", 400, y, 150, 44, b, bsub, "ink", "soft")
        d.node(f"c{i}", 650, y, 216, 44, c, csub, tone)
        d.arrow(f"a{i}", f"b{i}", "encrypted", tone=tone, ly=y + 16)
        d.arrow(f"b{i}", f"c{i}", "plain", tone=tone, ly=y + 16)
        d.text(150, y + 56, cmdline, "dt strong")
    return d.svg()


PAGE_SSH = dict(
    title="SSH &amp; tunnels",
    kicker="reach private hosts safely; forward ports both ways",
    figure=tunnels(),
    boxes=[
        box("Tunnels", cmd('''
ssh -N -L 5432:db.internal:5432 bastion  # then: psql -h localhost -p 5432
ssh -N -L 8443:10.0.1.20:443 -L 6379:redis.internal:6379 bastion  # several at once
ssh -N -R 8080:localhost:3000 server  # show your laptop's :3000 on server:8080
ssh -N -D 1080 bastion  # then: curl --socks5-hostname localhost:1080 http://intranet/
ssh -J bastion app.internal  # jump; chain: -J bastion1,bastion2
ssh -f -N -o ExitOnForwardFailure=yes -L 5432:db.internal:5432 bastion  # background
autossh -M 0 -N -o ServerAliveInterval=30 -L 5432:db.internal:5432 bastion  # reconnects
'''), "dev", "wide", "-N = no shell, just the tunnel"),
        box("Read a forward", '''
<p><code>-L <b>5432</b>:<b>db.internal</b>:<b>5432</b> bastion</code></p>
<dl class="kv">
<dt>1st</dt><dd>port opened <b>on your side</b></dd>
<dt>2nd</dt><dd>target host, resolved <b>by the bastion</b></dd>
<dt>3rd</dt><dd>target port</dd>
<dt>last</dt><dd>the SSH server in the middle</dd>
</dl>
<p class="fine"><code>-R</code> is the mirror: the 1st port opens on the <b>server</b>, the target is reached from <b>your</b> side. Tunnels listen on 127.0.0.1 unless you say otherwise.</p>''', "ink"),
        box("~/.ssh/config", code('''
Host bastion
    HostName bastion.example.com
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host *.internal
    ProxyJump bastion  # every internal host via the bastion

Host db-tunnel
    HostName bastion.example.com
    LocalForward 5432 db.internal:5432
    SessionType none  # OpenSSH 8.7+ (older: ssh -N)
'''), "feat", "", "then: ssh db-tunnel"),
        box("Keys &amp; basics", cmd('''
ssh-keygen -t ed25519 -C "jef@laptop"
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host
ssh-add ~/.ssh/id_ed25519  # load into the agent
ssh -i key.pem -p 2222 user@host
scp -J bastion file app.internal:/tmp/
rsync -avz -e "ssh -J bastion" dir/ app.internal:/srv/dir/
ssh -vvv host  # debug: which keys, where it stops
'''), "rel"),
        box("SSH errors decoded", '''
<dl class="kv stack">
<dt>Permission denied (publickey)</dt><dd>wrong user or key; <code>chmod 700 ~/.ssh</code>, <code>600</code> on the key; check <code>ssh -v</code></dd>
<dt>Host key verification failed</dt><dd>the host changed (rebuilt?) or something is in the middle. Verify, then <code>ssh-keygen -R host</code></dd>
<dt>Too many authentication failures</dt><dd>the agent offers every key: <code>IdentitiesOnly yes</code></dd>
<dt>bind: Address already in use</dt><dd>local port taken: <code>lsof -i :5432</code>, pick another</dd>
<dt>channel open failed: administratively prohibited</dt><dd>server has <code>AllowTcpForwarding no</code></dd>
<dt>connect failed: Connection refused</dt><dd>the <b>bastion</b> can't reach the target host:port</dd>
</dl>''', "main", "wide"),
        box("Safer habits", '''
<ul class="checks">
<li><code>-J</code> instead of <code>-A</code>: agent forwarding lets the bastion use your keys</li>
<li>Keep forwards on <code>127.0.0.1</code>; <code>GatewayPorts</code> only on purpose</li>
<li>Close tunnels when done: <code>~.</code> quits a stuck session</li>
<li>Cloud options without open port 22: AWS SSM, <code>gcloud … --tunnel-through-iap</code>, Azure Bastion, <code>kubectl port-forward</code></li>
</ul>''', "warn"),
    ],
)

PAGES = [PAGE_SHELL, PAGE_LAYERS, PAGE_HTTP, PAGE_DECODE, PAGE_SSH]
