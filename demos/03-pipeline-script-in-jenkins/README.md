# Demo 03: Pipeline Script in Jenkins

## What this teaches

- A **Pipeline** job can run a script typed directly into the Jenkins UI
- You get stages and a stage view — a step up from Freestyle
- But the pipeline script is **still not in the repo** — same problem as Demo 02

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-03-pipeline-script-in-jenkins` |
| Job type | Pipeline |
| Definition | **Pipeline script** _(not Pipeline script from SCM)_ |
| Script Path | _(none — paste script into Jenkins UI)_ |

### Pipeline script

Copy the contents of [inline-pipeline.groovy](inline-pipeline.groovy) and paste them into the **Pipeline script** text box in the Jenkins job configuration.

> **Important:** Set Definition to **Pipeline script**, not "Pipeline script from SCM". Jenkins will not look in the repo for this script.

## Expected console output

```
Hello from Jenkins Pipeline!
Python version: 3.x.x
Pipeline script is pasted into Jenkins — still not stored in this repo.
```

The stage view should show one green **Run** stage.

## The problem to notice

1. The pipeline works and shows stages — but the script lives in Jenkins, not in Git.
2. `inline-pipeline.groovy` in this folder is just a **reference copy** for the workshop. Jenkins does not use it automatically.
3. Change the script in Jenkins and nothing is committed to Git. Change the repo and Jenkins keeps the old script.
4. Every Jenkins server needs the script copy-pasted manually.

**The fix: put the pipeline in a `Jenkinsfile` in the repo.**

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a greeting |
| `inline-pipeline.groovy` | Reference script to paste into Jenkins UI — not a Jenkinsfile |

## Next demo

[04-pipeline-declarative](../04-pipeline-declarative/README.md) — store the pipeline in a `Jenkinsfile` in the repo. Jenkins reads it from SCM.
