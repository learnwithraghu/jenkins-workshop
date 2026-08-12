# Demos

Guided examples that show specific Jenkins features. Work through them in order — each builds on concepts from the previous demo.

**Setup required:** [Install Jenkins](../docs/01-install-jenkins-native.md) and [connect to GitHub](../docs/03-connect-github.md) before starting.

| # | Demo | Jenkins feature | Job type | Script Path |
|---|------|-----------------|----------|-------------|
| 1 | [01-freestyle-hello](01-freestyle-hello/) | Freestyle project, shell build step | Freestyle | _(none)_ |
| 2 | [02-pipeline-declarative](02-pipeline-declarative/) | Declarative Pipeline, stages, post | Pipeline | `demos/02-pipeline-declarative/Jenkinsfile` |
| 3 | [03-pipeline-stages](03-pipeline-stages/) | Multiple stages, pytest | Pipeline | `demos/03-pipeline-stages/Jenkinsfile` |
| 4 | [04-parameterized-build](04-parameterized-build/) | Build parameters | Pipeline | `demos/04-parameterized-build/Jenkinsfile` |
| 5 | [05-post-build-artifacts](05-post-build-artifacts/) | Archive artifacts, JUnit reports | Pipeline | `demos/05-post-build-artifacts/Jenkinsfile` |
| 6 | [06-multibranch-pipeline](06-multibranch-pipeline/) | Multibranch Pipeline | Multibranch Pipeline | `demos/06-multibranch-pipeline/Jenkinsfile` |

## Conventions

- All builds use **Python 3** on the Jenkins host (`python3` / `/usr/bin/python3`).
- Tests use **pytest** (installed via `pip3 install -r requirements.txt`).
- No Docker builds or container agents.
- Repository URL for all jobs: `https://github.com/learnwithraghu/jenkins-workshop.git`

## Full workshop path

See the [workshop guide](../docs/04-workshop-guide.md) for the complete ordered checklist including challenges.
