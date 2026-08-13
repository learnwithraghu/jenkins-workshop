# Demo 13: Deploy a Static Site on the Jenkins Server

## What this teaches

- A **Deploy** stage that publishes a real `index.html` (not a fake echo)
- Serving the site from the **same machine as Jenkins** with `python3 -m http.server`
- Opening an **EC2 security group port** so you can browse the site
- Two ways to open the page **without** a third-party host: Jenkins UI, or `http://<EC2_IP>:<port>/`

No extra accounts, tokens, or SaaS deploy targets.

## Instructor talking points

1. **Deploy can stay on the Jenkins host** — copy `index.html` to `/tmp/jenkins-workshop-site` and serve it; students see a public URL without Surge or GitHub Pages.
2. **Security group is the firewall** — Jenkins on 8080 is already open; this demo adds TCP **18081** so browsers can reach the site.
3. **ProcessTreeKiller** — background servers die when the step ends unless `JENKINS_NODE_COOKIE=dontKillMe` (and `setsid`) keep them alive. Call that out in the Jenkinsfile.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-13-deploy-static-site` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/13-deploy-static-site/Jenkinsfile` |

> **Plugin:** **HTML Publisher** (installed in [demo 11](../11-plugins/README.md)). After the first build, use **Build with Parameters** to change `SITE_TITLE` or `SITE_PORT`.

## 1. Open the port on EC2

In **AWS Console → EC2 → Security Groups** → the instance’s group → **Edit inbound rules** → **Add rule**:

| Type | Port | Source | Purpose |
|------|------|--------|---------|
| Custom TCP | 18081 | Your IP (or `0.0.0.0/0` for a classroom) | Static site (`http.server`) |

Save the rules. Jenkins stays on **8080**; the website is **18081**.

### Docker Jenkins extra

The default `docker run` only publishes 8080. Recreate (or add) the mapping so 18081 leaves the container:

```bash
docker stop jenkins && docker rm jenkins

docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -p 18081:18081 \
  -v jenkins_home:/var/jenkins_home \
  -v /usr/bin/python3:/usr/bin/python3:ro \
  -v /usr/bin/pip3:/usr/bin/pip3:ro \
  jenkins/jenkins:lts
```

Native Jenkins (doc 01) needs only the security group rule — no Docker port mapping.

## 2. Create the job and build

1. New Item → `demo-13-deploy-static-site` → **Pipeline**.
2. **Pipeline script from SCM** → Git → repo URL above → Script Path `demos/13-deploy-static-site/Jenkinsfile`.
3. **Save** → **Build Now** (or **Build with Parameters** after the first run).

## 3. Open index.html (three ways)

### A. From the Jenkins build (no extra port)

1. Open the green build.
2. Click **Workshop Site** in the side panel (HTML Publisher) — the page opens in Jenkins.
3. Or click **Build Artifacts** → `index.html` to download / view the file.

### B. Website on the Jenkins / EC2 server

After a successful Deploy stage, the console prints a curl of the homepage. In your browser:

```
http://<EC2_PUBLIC_IP>:18081/
```

You should see **Deployed from Jenkins** and the site title.

If the page does not load:

1. Confirm the security group allows **18081** from your IP.
2. From the EC2 host: `curl -s http://127.0.0.1:18081/` — if this works but the browser does not, the SG (or Docker `-p`) is the problem.
3. Check the server log: `cat /tmp/jenkins-workshop-site/server.log`

### C. On the Jenkins host itself (SSH)

```bash
curl -s http://127.0.0.1:18081/
# or
python3 -m http.server 18081 --bind 0.0.0.0 --directory /tmp/jenkins-workshop-site
```

The pipeline already starts that server; you only need the manual command if you stopped it.

## Expected console highlights

```
Wrote .../site/index.html
...
Deployed from Jenkins
...
Open index.html from this build ... or browse http://<EC2_PUBLIC_IP>:18081/
```

## Files

| File | Purpose |
|------|---------|
| `index.html` | Page template (placeholders filled at build time) |
| `generate_site.py` | Writes `site/index.html` with title, build number, time |
| `Jenkinsfile` | Generate → Deploy (`http.server` + archive + HTML Publisher) |

## Try it

Rebuild with `SITE_TITLE` set to your name. Refresh `http://<EC2_PUBLIC_IP>:18081/` — the heading should change.

To stop the site on the host:

```bash
kill "$(cat /tmp/jenkins-workshop-site/server.pid)"
```

## Next

[14-deploy-s3](../14-deploy-s3/README.md) — upload `index.html` to an S3 bucket (bucket name is a build parameter).
