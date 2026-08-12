# Demo 04: Pipeline from SCM (Jenkinsfile)

## What this teaches

- Storing the pipeline in a **`Jenkinsfile` in the repo**
- Jenkins reads the script from SCM — **Pipeline script from SCM**
- Build instructions are version-controlled alongside the code
- Declarative Pipeline syntax: `agent`, `stages`, `steps`, `post`

This demo solves the problems from Demo 02 and Demo 03. The pipeline lives in Git, not in the Jenkins UI.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-04-pipeline-declarative` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/04-pipeline-declarative/Jenkinsfile` |

## Expected console output

```
Hello from Jenkins Pipeline!
Python version: 3.x.x
```

The stage view should show two green stages: **Checkout** and **Run**.

## Why this matters

| Demo | Where the build config lives |
|------|------------------------------|
| 01, 02 | Jenkins UI only (Freestyle) |
| 03 | Jenkins UI only (inline Pipeline script) |
| **04** | **`Jenkinsfile` in the repo** |

Anyone who clones the repo sees exactly how Jenkins should build the project.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a greeting and Python version |
| `Jenkinsfile` | Declarative pipeline stored in the repo |

## Next demo

[05-pipeline-stages](../05-pipeline-stages/README.md) — multiple stages with dependency install and pytest.
