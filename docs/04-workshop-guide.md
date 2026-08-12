# Workshop Guide

Work through the sections below in order. Each step builds on the previous one.

**Repository:** [github.com/learnwithraghu/jenkins-workshop](https://github.com/learnwithraghu/jenkins-workshop)

## Setup checklist

- [ ] [EC2 instance launched](00-prerequisites.md)
- [ ] Jenkins installed ([native](01-install-jenkins-native.md) or [Docker](02-install-docker-jenkins.md))
- [ ] Python 3 available on the host
- [ ] [GitHub connected](03-connect-github.md) — first freestyle job runs successfully

---

## Part 1: Demos

Complete each demo in order. Read the README in each folder for job configuration details.

| # | Demo | Jenkins feature | Job type | Checkpoint |
|---|------|-----------------|----------|------------|
| 1 | [01-freestyle-hello](../demos/01-freestyle-hello/README.md) | Freestyle project, shell build step | Freestyle | Console shows "Hello from Jenkins Workshop!" |
| 2 | [02-config-not-in-repo](../demos/02-config-not-in-repo/README.md) | Build config lives only in Jenkins UI | Freestyle | Repo has no build instructions |
| 3 | [03-pipeline-script-in-jenkins](../demos/03-pipeline-script-in-jenkins/README.md) | Inline pipeline script in Jenkins UI | Pipeline | Stages work, but script still not in repo |
| 4 | [04-pipeline-declarative](../demos/04-pipeline-declarative/README.md) | Jenkinsfile in repo, Pipeline from SCM | Pipeline | Stage view shows Checkout + Run stages green |
| 5 | [05-pipeline-stages](../demos/05-pipeline-stages/README.md) | Multiple stages, install deps, run tests | Pipeline | Test stage passes with pytest output |
| 6 | [06-parameterized-build](../demos/06-parameterized-build/README.md) | Build parameters (`choice`, `string`) | Pipeline | Build with custom name shows personalized greeting |
| 7 | [07-post-build-artifacts](../demos/07-post-build-artifacts/README.md) | Archive artifacts, JUnit test reports | Pipeline | `report.txt` visible under Build Artifacts |
| 8 | [08-multibranch-pipeline](../demos/08-multibranch-pipeline/README.md) | Multibranch Pipeline, branch discovery | Multibranch Pipeline | Jenkins discovers and builds the `main` branch |

### Show your instructor (demos)

For each demo, be ready to show:

1. The Jenkins job configuration (job type, repo URL, Script Path).
2. A successful build (green ball or blue wave).
3. Console output or stage view for pipeline demos.

---

## Part 2: Challenges

After completing the demos, tackle the challenges. Each challenge asks you to **create a Jenkins job** in the UI. All pipeline scripts are already in the repo — you do not edit code or Jenkinsfiles.

| # | Challenge | Your task |
|---|-----------|-----------|
| 1 | [01-create-pipeline-job](../challenges/01-create-pipeline-job/README.md) | Create a Pipeline job with Install and Test stages |
| 2 | [02-create-staged-pipeline-job](../challenges/02-create-staged-pipeline-job/README.md) | Create a Pipeline job with Install, Test, and Run stages |
| 3 | [03-create-full-pipeline-job](../challenges/03-create-full-pipeline-job/README.md) | Create a Pipeline job with a post-build success message |

### Show your instructor (challenges)

For each challenge, be ready to show your job configuration, a green build, and a brief explanation of how you set it up.

---

## Suggested timeline

| Segment | Duration | Content |
|---------|----------|---------|
| Setup | 45–60 min | EC2 + Jenkins install + GitHub connection |
| Demos 1–4 | 45 min | Freestyle, why Jenkinsfile, Pipeline from SCM |
| Demos 5–8 | 45 min | Stages, parameters, artifacts, multibranch |
| Challenges | 30–45 min | Create Jenkins jobs for pre-built pipelines |
| Wrap-up | 15 min | Review, Q&A |

---

## Tips

- **Use absolute Python path with Docker Jenkins:** `/usr/bin/python3` instead of `python3`.
- **Read the console output first** when a build fails — Jenkins shows the exact error.
- **One job per demo** keeps things organized. Name jobs to match the folder (e.g. `demo-05-pipeline-stages`).
- **Challenges focus on job creation** — all code is pre-configured. Focus on correct job settings and a green build.

## Reference

- [Demos index](../demos/README.md)
- [Challenges index](../challenges/README.md)
- [Connect Jenkins to GitHub](03-connect-github.md)
