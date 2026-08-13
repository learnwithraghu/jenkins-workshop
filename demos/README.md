# Demos

Guided examples that show specific Jenkins features. Work through them in order — each builds on concepts from the previous demo.

**Setup required:** [Install Jenkins](../docs/01-install-jenkins-native.md) and [connect to GitHub](../docs/03-connect-github.md) before starting.

| # | Demo | Jenkins feature | Job type | Script Path |
|---|------|-----------------|----------|-------------|
| 1 | [01-freestyle-hello](01-freestyle-hello/) | Freestyle project, shell build step | Freestyle | _(none)_ |
| 2 | [02-config-not-in-repo](02-config-not-in-repo/) | Why UI-only config is a problem | Freestyle | _(none)_ |
| 3 | [03-pipeline-script-in-jenkins](03-pipeline-script-in-jenkins/) | Inline pipeline script in Jenkins UI | Pipeline | _(paste script in UI)_ |
| 4 | [04-pipeline-declarative](04-pipeline-declarative/) | Jenkinsfile in repo, Pipeline from SCM | Pipeline | `demos/04-pipeline-declarative/Jenkinsfile` |
| 5 | [05-pipeline-stages](05-pipeline-stages/) | Multiple stages, pytest | Pipeline | `demos/05-pipeline-stages/Jenkinsfile` |
| 6 | [06-parameterized-build](06-parameterized-build/) | Build parameters | Pipeline | `demos/06-parameterized-build/Jenkinsfile` |
| 7 | [07-post-build-artifacts](07-post-build-artifacts/) | Archive artifacts, JUnit reports | Pipeline | `demos/07-post-build-artifacts/Jenkinsfile` |
| 8 | [08-parallel-stages](08-parallel-stages/) | Parallel stages | Pipeline | `demos/08-parallel-stages/Jenkinsfile` |
| 9 | [09-pipeline-customize](09-pipeline-customize/) | Conditional stages, recover after failed build | Pipeline | `demos/09-pipeline-customize/Jenkinsfile` |
| 10 | [10-docker-ecr](10-docker-ecr/) | Docker build, image test/scan, push to ECR | Pipeline | `demos/10-docker-ecr/Jenkinsfile` |
| 11 | [11-plugins](11-plugins/) | Plugin Manager, Timestamper, HTML Publisher | Pipeline | `demos/11-plugins/Jenkinsfile` |
| 12 | [12-poll-scm](12-poll-scm/) | pollSCM auto-build on push | Pipeline | `demos/12-poll-scm/Jenkinsfile` |
| 13 | [13-deploy-static-site](13-deploy-static-site/) | Deploy index.html on the Jenkins host | Pipeline | `demos/13-deploy-static-site/Jenkinsfile` |
| 14 | [14-deploy-s3](14-deploy-s3/) | Deploy index.html to S3 (`S3_BUCKET` parameter) | Pipeline | `demos/14-deploy-s3/Jenkinsfile` |

## Conventions

- Builds use **Python 3** on the Jenkins host (`python3` / `/usr/bin/python3`).
- Demos that need **pytest** install with `pip3 install --break-system-packages` (PEP 668 blocks plain system-wide `pip install` on Debian/Ubuntu). Demos 09 and 10 use stdlib `unittest`.
- Demos 01–09 do not build containers. **Demo 10** requires Docker, AWS CLI, Trivy, and an EC2 IAM role with ECR access.
- **Demo 07** requires the **JUnit** plugin (`junit` Pipeline step). **Demo 11** requires **Timestamper** and **HTML Publisher** (guided in that README). Demo 13 also uses HTML Publisher and opens TCP **18081** on the EC2 security group.
- **Demo 14** needs an S3 bucket in **us-east-1**, and Access Key + Secret entered on **Build with Parameters**. The job installs AWS CLI if missing. Do not commit keys.
- Repository URL for all jobs: `https://github.com/learnwithraghu/jenkins-workshop.git`

## Full workshop path

See the [workshop guide](../docs/04-workshop-guide.md) for the complete ordered checklist including challenges.
