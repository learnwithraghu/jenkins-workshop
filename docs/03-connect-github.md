# Connect Jenkins to GitHub

This guide connects your Jenkins instance to the public workshop repository and creates your first jobs.

**Repository URL:** `https://github.com/learnwithraghu/jenkins-workshop.git`

Because the repo is public, Jenkins can clone it over HTTPS without credentials.

## Freestyle job: Hello World

This matches [demo 01](../demos/01-freestyle-hello/README.md) — a simple job with no Jenkinsfile.

1. In Jenkins, click **New Item**.
2. Enter name: `demo-01-freestyle-hello`.
3. Select **Freestyle project** → **OK**.
4. Under **Source Code Management**, select **Git**.
5. Set **Repository URL** to:

```
https://github.com/learnwithraghu/jenkins-workshop.git
```

6. Set **Branch Specifier** to `*/main`.
7. Under **Build Steps**, click **Add build step** → **Execute shell**.
8. Paste:

```bash
cd demos/01-freestyle-hello
python3 app.py
```

9. Click **Save**, then **Build Now**.
10. Open the build number → **Console Output**.

**Expected output:**

```
Hello from Jenkins Workshop!
Python version: 3.x.x
```

## Pipeline job: Declarative Pipeline from SCM

This matches [demo 04](../demos/04-pipeline-declarative/README.md) — Jenkins reads the `Jenkinsfile` from the repo.

1. Click **New Item** → name: `demo-04-pipeline-declarative`.
2. Select **Pipeline** → **OK**.
3. Scroll to the **Pipeline** section.
4. Set **Definition** to **Pipeline script from SCM**.
5. Set **SCM** to **Git**.
6. Set **Repository URL** to:

```
https://github.com/learnwithraghu/jenkins-workshop.git
```

7. Set **Branch Specifier** to `*/main`.
8. Set **Script Path** to:

```
demos/04-pipeline-declarative/Jenkinsfile
```

9. Click **Save**, then **Build Now**.
10. Click the build number → **Pipeline Steps** or **Console Output** to see stage progress.

## Triggering builds automatically

### Option A: Poll SCM (simple, no webhook setup)

In the job configuration, under **Build Triggers**, enable **Poll SCM** and set:

```
H/5 * * * *
```

Jenkins checks GitHub every 5 minutes for changes.

### Option B: GitHub webhook (instant builds)

Requires Jenkins to be reachable from the internet on port 8080 (or via a reverse proxy).

1. In Jenkins: **Manage Jenkins** → **System** → find **GitHub** section (if GitHub plugin is installed) or use the **Generic Webhook Trigger** plugin.
2. In GitHub: go to the repo → **Settings** → **Webhooks** → **Add webhook**.
3. Set **Payload URL** to `http://<EC2_PUBLIC_IP>:8080/github-webhook/`.
4. Set **Content type** to `application/json`.
5. Select **Just the push event** → **Add webhook**.

For a classroom workshop, polling is usually sufficient.

## Creating jobs for other demos

Each demo folder has its own README with the exact job type and Script Path. Quick reference:

| Demo folder | Job type | Script Path |
|-------------|----------|-------------|
| `demos/01-freestyle-hello` | Freestyle | _(none — use shell build step)_ |
| `demos/02-config-not-in-repo` | Freestyle | _(none — use shell build step)_ |
| `demos/03-pipeline-script-in-jenkins` | Pipeline | _(paste `inline-pipeline.groovy` in UI)_ |
| `demos/04-pipeline-declarative` | Pipeline | `demos/04-pipeline-declarative/Jenkinsfile` |
| `demos/05-pipeline-stages` | Pipeline | `demos/05-pipeline-stages/Jenkinsfile` |
| `demos/06-parameterized-build` | Pipeline | `demos/06-parameterized-build/Jenkinsfile` |
| `demos/07-post-build-artifacts` | Pipeline | `demos/07-post-build-artifacts/Jenkinsfile` |
| `demos/08-multibranch-pipeline` | Multibranch Pipeline | `demos/08-multibranch-pipeline/Jenkinsfile` |

See the full [workshop guide](04-workshop-guide.md) for the recommended order.

## Creating jobs for challenges

Challenges use the same Pipeline from SCM approach as the demos. See each [challenge README](../challenges/README.md) for the goal and acceptance criteria.

> **Note:** All Jenkinsfiles are pre-configured in the repo. Students only create and configure Jenkins jobs — no code editing required.

## Troubleshooting

**"Failed to connect to repository":** Verify the URL is correct and the EC2 instance has outbound internet access.

**"script not found":** Check the **Script Path** matches the Jenkinsfile location exactly (case-sensitive).

**Build succeeds but Python fails:** Ensure Python 3 is installed on the host. See the [native](01-install-jenkins-native.md) or [Docker](02-install-docker-jenkins.md) install guide.

## Next step

Follow the [workshop guide](04-workshop-guide.md) to work through all demos and challenges in order.
