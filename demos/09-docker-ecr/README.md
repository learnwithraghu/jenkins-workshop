# Demo 09: Build Docker Image and Push to ECR

## What this teaches

- A **Declarative Pipeline** that builds, tests, scans, and pushes a container image
- **Smoke-testing** the image with `docker run` + `curl` before push
- **Vulnerability scanning** with Trivy (local) and optional ECR basic scan
- Authenticating to **Amazon ECR** from Jenkins on EC2 via the **instance IAM role** (no long-lived keys in the job)

## Instructor talking points

1. **Pipeline shape first** — walk the stages in order: Test App → Build Image → Test Image → Scan → Login → Push → ECR Scan Status. Emphasize that push is last, after tests and scan.
2. **IAM role, not access keys** — Jenkins on EC2 uses the instance profile for `aws ecr get-login-password`; call out the `REPLACE_WITH_*` placeholders students must fill before the job can push.
3. **Test the image, not only the code** — unit tests run on the host; the Test Image stage proves the container actually serves the hello response; Scan fails the build on HIGH/CRITICAL findings.

## Prerequisites (EC2 / Jenkins host)

This demo assumes Jenkins runs **natively on EC2** (not the Docker Jenkins install from doc 02) with:

| Requirement | Notes |
|-------------|--------|
| Docker Engine | Installed; Jenkins user can run `docker` (e.g. in `docker` group) |
| AWS CLI v2 | Used for ECR login and optional scan APIs |
| Trivy | Installed on the host for the Scan stage |
| IAM instance role | Permissions to auth and push to your ECR repo (e.g. `ecr:GetAuthorizationToken`, `ecr:BatchCheckLayerAvailability`, `ecr:CompleteLayerUpload`, `ecr:InitiateLayerUpload`, `ecr:PutImage`, `ecr:UploadLayerPart`, plus scan APIs if you use that stage) |
| ECR repository | Already created — fill its name into the Jenkinsfile |

> **Fill-in values:** edit `demos/09-docker-ecr/Jenkinsfile` and replace `REPLACE_WITH_AWS_REGION`, `REPLACE_WITH_AWS_ACCOUNT_ID`, and `REPLACE_WITH_ECR_REPO_NAME` before building — or override them with Jenkins job parameters / environment if you prefer not to commit account IDs.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-09-docker-ecr` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/09-docker-ecr/Jenkinsfile` |

## Pipeline stages (what each one does)

| Stage | Purpose |
|-------|---------|
| **Test App** | Unit-test `app.py` on the host before any image work |
| **Build Image** | `docker build` a small `python:3.12-slim` image |
| **Test Image** | Run the container, `curl` port 18080, assert the hello body, then remove the container |
| **Scan Image** | `trivy image` — fail on HIGH/CRITICAL |
| **Login to ECR** | `aws ecr get-login-password` → `docker login` (IAM role) |
| **Push to ECR** | Tag with build number and `docker push` |
| **ECR Scan Status** | Best-effort `start-image-scan` / `describe-image-scan-findings` if basic scanning is enabled on the repo |

## Expected console highlights

```
Ran 4 tests in ...
OK
...
Successfully built ...
Successfully tagged jenkins-workshop-demo:<BUILD_NUMBER>
...
Hello from Jenkins Docker demo!
...
Login Succeeded
...
Image pushed: <ACCOUNT>.dkr.ecr.<REGION>.amazonaws.com/<REPO>:<BUILD_NUMBER>
```

## Files

| File | Purpose |
|------|---------|
| `app.py` | Tiny HTTP server on port 8080 |
| `test_app.py` | Stdlib unit tests (no pytest) |
| `Dockerfile` | Minimal Python image |
| `Jenkinsfile` | Full build → test → scan → push pipeline (with ECR placeholders) |

## Try it

1. Create an ECR repository (or reuse one) and note region, account ID, and repo name.
2. Replace the three `REPLACE_WITH_*` values in the Jenkinsfile (commit/push, or edit on a workshop branch).
3. Create the Pipeline job with the Script Path above and run it.
4. In the AWS console, confirm the image tag matches the Jenkins build number.

## Next

You've finished the Docker/ECR demo. Next: [10-plugins](../10-plugins/README.md) — Plugin Manager and using plugins in a Pipeline.
