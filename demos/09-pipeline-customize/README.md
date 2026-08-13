# Demo 09: Conditional Stages and Previous-Build Recovery

## What this teaches

- Splitting which stages run with **`when { expression { ... } }`**
- Running a **Recover** stage only when the **previous build failed** (`currentBuild.previousBuild.result`)
- Passing **build parameters** into `app.py` so console output changes with the job
- Why Recover does **not** run on the failed build itself — later stages are skipped after a failure

## Instructor talking points

1. **`when` skips a stage without failing the build** — uncheck `RUN_TESTS` or leave `ENVIRONMENT=dev` and show Test / Deploy as skipped (not red).
2. **Recover looks at the previous build** — fail build N with `FORCE_FAIL`, then build N+1; Recover runs first because `currentBuild.previousBuild.result == 'FAILURE'`.
3. **Params flow into the app** — `APP_NAME`, `ENVIRONMENT`, `LOG_LEVEL`, and `RELEASE_NOTES` become env vars that `app.py` prints on the status card.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-09-pipeline-customize` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/09-pipeline-customize/Jenkinsfile` |

> **Note:** After the first build, Jenkins discovers the parameters. Use **Build with Parameters** for subsequent builds.

## How to test

1. Run **Build Now** once (parameters will be registered). Recover is skipped; Test + Run are green; Deploy is skipped (`ENVIRONMENT=dev`).
2. Click **Build with Parameters**.
3. **Skip a stage:** uncheck `RUN_TESTS` → Test is skipped.
4. **Run an extra stage:** set `ENVIRONMENT` to `prod` → Deploy runs (`Fake deploy of workshop-app to prod`).
5. **Previous-build failure:**
   - Build with `FORCE_FAIL` checked → Run fails, build is red. Recover does **not** run on this build.
   - Build again with `FORCE_FAIL` unchecked → Recover runs first, then Test + Run go green.

## Expected console output

Default status card (`ENVIRONMENT=dev`, `FORCE_FAIL` off):

```
App: workshop-app
Environment: dev
Log level: INFO
Release notes: First workshop release
```

After a failed build, the next build's Recover stage:

```
Recover stage — the previous Jenkins build failed.
Running extra checks before continuing.
```

## Why Recover waits for the next build

Declarative Pipeline skips later stages when an earlier stage fails. Recover is therefore gated on **the previous build's result**, not on a failed stage in the current build.

## Files

| File | Purpose |
|------|---------|
| `app.py` | `status` prints a release card; `recover` prints extra checks; `FORCE_FAIL=true` exits 1 |
| `test_app.py` | Stdlib unittest (no pytest) |
| `Jenkinsfile` | Recover / Test / Run / Deploy with `when` conditions |

## Try it

Change `APP_NAME` or `LOG_LEVEL=DEBUG` and rebuild. DEBUG adds Python version and a UTC timestamp to the status card.

Optional **Replay** (no git push): change Deploy `when` to also run for `staging`, or add `retry(2)` on Test.

## Next demo

[10-docker-ecr](../10-docker-ecr/README.md) — Docker build, image test/scan, push to ECR.
