# Demo 06: Parameterized Build

## What this teaches

- Defining **build parameters** in a Declarative Pipeline
- `string` and `choice` parameter types
- Accessing parameters via `params.PARAM_NAME`
- Passing parameters to shell steps as environment variables

## Instructor talking points

1. **Parameters make builds reusable** — one job can greet different names or choose options without editing the Jenkinsfile each time.
2. **First build discovers parameters** — after the initial run, Jenkins shows **Build with Parameters**; explain why the first build may look different.
3. **Params flow into the app** — `params.GREETING_NAME` becomes an env var that `greet.py` reads, connecting Pipeline config to runtime behavior.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-06-parameterized-build` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/06-parameterized-build/Jenkinsfile` |

> **Note:** After the first build, Jenkins discovers the parameters. Use **Build with Parameters** for subsequent builds.

## How to test

1. Run the job once (parameters will be registered).
2. Click **Build with Parameters**.
3. Set `GREETING_NAME` to your name (e.g. `Raghu`).
4. Select a `LANGUAGE` (currently display-only).
5. Click **Build**.

## Expected console output

With `GREETING_NAME=Raghu`:

```
Hello, Raghu!
This greeting was customized via a Jenkins build parameter.
```

## Files

| File | Purpose |
|------|---------|
| `greet.py` | Reads `GREETING_NAME` env var and prints greeting |
| `Jenkinsfile` | Pipeline with `string` and `choice` parameters |

## Next demo

[07-post-build-artifacts](../07-post-build-artifacts/README.md) — archive build artifacts and publish test reports.
