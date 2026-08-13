# Demo 12: Poll SCM

## What this teaches

- Declarative Pipeline **`triggers { pollSCM(...) }`**
- Jenkins checks GitHub on a schedule and starts a build when `main` changes
- Polling is simple for a workshop (no webhook or public callback URL required)
- Difference between **poll** (~5 minute lag) and **webhook** (near-instant)

## Instructor talking points

1. **Build Now once first** — the Jenkinsfile must be loaded before `pollSCM` is registered on the job.
2. **Push to main → wait up to ~5 minutes** — schedule `H/5 * * * *` means about every 5 minutes; look for cause **Started by an SCM change**.
3. **Webhook is faster** — if students ask “why isn’t it instant?”, point to [Option B in connect GitHub](../../docs/03-connect-github.md).

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-12-poll-scm` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/12-poll-scm/Jenkinsfile` |

> **Important:** Click **Build Now** once after creating the job so Jenkins registers the trigger.

## Show pollSCM: push to main → build starts

1. Create the job and run **Build Now** once.
2. Confirm **Configure** → **Build Triggers** shows Poll SCM with `H/5 * * * *`.
3. Make a small change on `main` (for example edit a comment in `app.py`) and **push** to GitHub.
4. Stay on the Jenkins job page — within about **five minutes** a new build should appear without clicking Build Now.
5. Open that build → cause should be **Started by an SCM change**.

## Expected console output

```
Poll SCM demo — this build was started by Jenkins.
Current time: ...
If you just pushed to main, the cause is likely: Started by an SCM change.
```

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints a short message and timestamp |
| `Jenkinsfile` | `pollSCM` trigger + Run stage |

## Next

Back to the [demos index](../README.md), or continue with any remaining challenges.
