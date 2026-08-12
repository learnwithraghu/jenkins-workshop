# Demo 02: Config Not in Repo

## What this teaches

- Freestyle jobs store build steps **only in the Jenkins UI**
- The repo has the application code, but **no record of how Jenkins builds it**
- If Jenkins is reinstalled or you share the project, the build instructions are lost

This demo builds the same hello-world app as Demo 01. The difference is what you notice **after** the build works.

## Instructor talking points

1. **The build “works” — but the config is invisible in Git** — open the folder on GitHub and show that only `app.py` exists; the shell step lives only in Jenkins.
2. **UI-only config does not scale** — teammates cannot reproduce the job from the repo, and a fresh Jenkins means retyping every build step.
3. **This pain point motivates the Jenkinsfile** — frame Demos 03–04 as the path from “config in Jenkins” to “config in the repo.”

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-02-config-not-in-repo` |
| Job type | Freestyle project |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | _(none)_ |

### Build step (Execute shell)

```bash
cd demos/02-config-not-in-repo
python3 app.py
```

## Expected console output

```
Hello from Jenkins Workshop!
Python version: 3.x.x
Build steps for this demo are configured in the Jenkins UI — not in this repo.
```

## The problem to notice

1. Open this folder on GitHub. You see `app.py` — but **no build instructions**.
2. The shell script lives only in your Jenkins job configuration.
3. A teammate cloning the repo cannot know how to build this app in Jenkins.
4. Rebuilding Jenkins from scratch means re-entering every build step by hand.

**This is why we need a Jenkinsfile.**

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a greeting — no Jenkinsfile or build config in the repo |

## Next demo

[03-pipeline-script-in-jenkins](../03-pipeline-script-in-jenkins/README.md) — move the script into a Pipeline job, but it still lives in Jenkins, not in the repo.
