# Demo 05: Post-Build Artifacts

## What this teaches

- **Archiving artifacts** with `archiveArtifacts`
- Publishing **JUnit test reports** with `junit`
- Using `post { always { ... } }` to run steps regardless of build result
- Viewing artifacts and test results in the Jenkins UI

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-05-post-build-artifacts` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/05-post-build-artifacts/Jenkinsfile` |

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

[06-multibranch-pipeline](../06-multibranch-pipeline/README.md) — discover and build branches automatically.
