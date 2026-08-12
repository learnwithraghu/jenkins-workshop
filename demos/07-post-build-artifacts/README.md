# Demo 07: Post-Build Artifacts

## What this teaches

- **Archiving artifacts** with `archiveArtifacts`
- Publishing **JUnit test reports** with `junit`
- Using `post { always { ... } }` to run steps regardless of build result
- Viewing artifacts and test results in the Jenkins UI

## Instructor talking points

1. **Artifacts outlive the workspace** — `report.txt` / `report.json` are archived so students can download them from the build page after the run.
2. **JUnit reports make tests browsable** — `junit` turns pytest XML into the **Test Result** UI, not just console text.
3. **`post { always }` runs either way** — publishing and archiving should not depend only on a green build; call out why that matters for failed builds.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-07-post-build-artifacts` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/07-post-build-artifacts/Jenkinsfile` |

## If the build fails: `No such DSL method 'junit'`

The stages may succeed, then the `post { always }` block fails because the **JUnit** plugin is missing. Fix it and rebuild:

1. Open the failed build → **Console Output** and confirm the error mentions `No such DSL method 'junit'`.
2. Go to **Manage Jenkins** → **Plugins** → **Available plugins**.
3. Search for **JUnit** (plugin ID: `junit`) and install it.
4. Restart Jenkins if prompted.
5. Open the job again and click **Build Now**.
6. Confirm the build is green, then continue with **What to look for after a successful build** below.

> Tip: Choosing **Install suggested plugins** during the Jenkins setup wizard usually includes JUnit. Minimal installs often skip it.

## What to look for after a successful build

1. **Test Result** — on the build page, click **Test Result** to see 3 passing tests.
2. **Build Artifacts** — on the build page, find `report.txt` and `report.json` under **Artifacts**. Click to download.

## Expected console output

```
Report generated: report.txt, report.json
```

## Files

| File | Purpose |
|------|---------|
| `generate_report.py` | Creates `report.txt` and `report.json` |
| `test_generate_report.py` | pytest tests for the report generator |
| `requirements.txt` | pytest dependency |
| `Jenkinsfile` | Pipeline with junit and archiveArtifacts |

## Next demo

[08-multibranch-pipeline](../08-multibranch-pipeline/README.md) — discover and build branches automatically.
