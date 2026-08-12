# Demo 01: Freestyle Hello

## What this teaches

- Creating a **Freestyle project** in Jenkins
- Checking out code from Git (SCM)
- Running a shell build step
- Reading console output

This demo does **not** use a Jenkinsfile. You configure everything in the Jenkins UI.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-01-freestyle-hello` |
| Job type | Freestyle project |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | _(none)_ |

### Build step (Execute shell)

```bash
cd demos/01-freestyle-hello
python3 app.py
```

## Expected console output

```
Hello from Jenkins Workshop!
Python version: 3.x.x
```

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a greeting and Python version |

## Next demo

[02-pipeline-declarative](../02-pipeline-declarative/README.md) — the same hello-world, but using a Declarative Pipeline Jenkinsfile.
