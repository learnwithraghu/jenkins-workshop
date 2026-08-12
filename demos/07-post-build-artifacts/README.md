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

## Prerequisite: JUnit plugin

The `junit` step comes from the **JUnit** plugin. If the build fails with `No such DSL method 'junit'`, install it:

1. **Manage Jenkins** → **Plugins** → **Available plugins**
2. Search for **JUnit** and install it (plugin ID: `junit`)
3. Restart Jenkins if prompted
4. Rebuild this job

> Tip: Choosing **Install suggested plugins** during the Jenkins setup wizard usually includes JUnit. Minimal installs often skip it.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-07-post-build-artifacts` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/07-post-build-artifacts/Jenkinsfile` |

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
