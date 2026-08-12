# Demo 02: Declarative Pipeline

## What this teaches

- Creating a **Pipeline** job that reads a `Jenkinsfile` from SCM
- Declarative Pipeline syntax: `agent`, `stages`, `steps`
- `post` actions for success and failure

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-02-pipeline-declarative` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/02-pipeline-declarative/Jenkinsfile` |

## Expected console output

```
Hello from Jenkins Pipeline!
Python version: 3.x.x
```

The stage view should show two green stages: **Checkout** and **Run**.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a greeting and Python version |
| `Jenkinsfile` | Declarative pipeline with two stages |

## Next demo

[03-pipeline-stages](../03-pipeline-stages/README.md) — multiple stages with dependency install and pytest.
