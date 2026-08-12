# Demo 10: Jenkins Plugins

## What this teaches

- What **plugins** are and why most Jenkins features come from them
- Using **Manage Jenkins → Plugins** to find, install, and update plugins
- Installing **Timestamper** and **HTML Publisher**, then using them in a Pipeline
- Reading plugin docs / step names when a Pipeline step is “missing”

This is an instructor-led UI session first, then a short Pipeline job that proves the plugins work.

## Instructor talking points

1. **Jenkins core is small — plugins add the rest** — Git, Pipeline, JUnit, Docker helpers, HTML reports, Slack, etc. are plugins. The setup wizard’s “Install suggested plugins” already pulled in many of them.
2. **Plugin Manager is the control plane** — show Updates / Available / Installed; install Timestamper + HTML Publisher live; mention restart-when-required vs install-without-restart.
3. **Pipelines call plugin steps** — `timestamps()` and `publishHTML` only work after those plugins are installed; a missing step usually means a missing plugin, not a Groovy typo.

## Session flow (instructor)

### 1. Orient in the UI (~5 min)

1. Open **Manage Jenkins → Plugins**.
2. Show the tabs:
   - **Updates** — security and bugfix patches
   - **Available** — marketplace to install new capability
   - **Installed** — what this controller already has (search for `Pipeline`, `Git`, `JUnit`)
3. Call out that demos 01–09 already depended on plugins (Pipeline, Git, JUnit, …).

### 2. Install two plugins (~5–10 min)

In **Available**, search and install:

| Plugin | Why |
|--------|-----|
| **Timestamper** | Adds timestamps to console logs via `options { timestamps() }` |
| **HTML Publisher** | Publishes an HTML report on the build page via `publishHTML` |

Restart Jenkins if the UI asks for it, then confirm both appear under **Installed**.

### 3. Run the demo job (~5 min)

Create the Pipeline job below, build once, then show:

1. **Console output** — lines prefixed with timestamps (Timestamper).
2. **Build page** — **Demo Report** link (HTML Publisher) opening the generated HTML.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-10-plugins` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/10-plugins/Jenkinsfile` |

## Expected results

Console (timestamps present):

```
... 00:00:01.234  Wrote report.html
...
... Open the build page and click "Demo Report" ...
```

Build page:

- Side panel / summary link **Demo Report** → HTML page saying the report published successfully.

## If Publish HTML fails

1. Confirm **HTML Publisher** is installed (**Manage Jenkins → Plugins → Installed**).
2. Restart Jenkins if the plugin was just installed and the step is still unknown.
3. Confirm `report.html` was created under `demos/10-plugins` in the workspace.

## Files

| File | Purpose |
|------|---------|
| `generate_report.py` | Writes a tiny `report.html` |
| `Jenkinsfile` | Uses `timestamps()` + `publishHTML` |

## Optional extras (time permitting)

- Show **Plugin Manager → Updates** and discuss keeping plugins current for security.
- Search [plugins.jenkins.io](https://plugins.jenkins.io/) for one plugin students care about (Slack, Email Extension, Docker Pipeline) — install only if you have time to demo it.
- Ask: “Which plugin already powered Demo 07’s test results?” → **JUnit**.

## Next demo

[11-poll-scm](../11-poll-scm/README.md) — pollSCM so a push to main triggers a build.
