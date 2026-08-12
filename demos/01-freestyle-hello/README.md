# Demo 01: Freestyle Hello

## What this teaches

- Creating a **Freestyle project** in Jenkins
- Checking out code from Git (SCM)
- Running a shell build step
- Reading console output

This demo does **not** use a Jenkinsfile. You configure everything in the Jenkins UI.

## Instructor talking points

1. **Freestyle is the classic Jenkins job** — you configure SCM and build steps entirely in the UI; there is no Jenkinsfile yet.
2. **Git checkout + shell** — Jenkins pulls the repo, then runs a simple `python3 app.py` build step so students see the end-to-end flow.
3. **Console output is the first debugging tool** — open the build log and confirm the greeting and Python version printed successfully.

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

[02-config-not-in-repo](../02-config-not-in-repo/README.md) — see why storing build config only in Jenkins is a problem.
