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
| 2 | [02-pipeline-declarative](../demos/02-pipeline-declarative/README.md) | Declarative Pipeline, stages, post actions | Pipeline | Stage view shows Checkout + Run stages green |
| 3 | [03-pipeline-stages](../demos/03-pipeline-stages/README.md) | Multiple stages, install deps, run tests | Pipeline | Test stage passes with pytest output |
| 4 | [04-parameterized-build](../demos/04-parameterized-build/README.md) | Build parameters (`choice`, `string`) | Pipeline | Build with custom name shows personalized greeting |
| 5 | [05-post-build-artifacts](../demos/05-post-build-artifacts/README.md) | Archive artifacts, JUnit test reports | Pipeline | `report.txt` visible under Build Artifacts |
| 6 | [06-multibranch-pipeline](../demos/06-multibranch-pipeline/README.md) | Multibranch Pipeline, branch discovery | Multibranch Pipeline | Jenkins discovers and builds the `main` branch |

### Show your instructor (demos)

For each demo, be ready to show:

1. The Jenkins job configuration (job type, repo URL, Script Path).
2. A successful build (green ball or blue wave).
3. Console output or stage view for pipeline demos.

---

## Part 2: Challenges

After completing the demos, tackle the challenges. Each challenge gives you starter code — you write or fix the pipeline.

| # | Challenge | Your task | Starter state |
|---|-----------|-----------|---------------|
| 1 | [01-fix-failing-tests](../challenges/01-fix-failing-tests/README.md) | Fix broken tests so the pipeline passes | Tests intentionally fail |
| 2 | [02-add-missing-stage](../challenges/02-add-missing-stage/README.md) | Add the missing Test stage to the pipeline | Incomplete Jenkinsfile |
| 3 | [03-build-pipeline-from-scratch](../challenges/03-build-pipeline-from-scratch/README.md) | Write a full declarative pipeline from requirements | No Jenkinsfile provided |

### Show your instructor (challenges)

For each challenge, be ready to show:

1. Your Jenkinsfile (or the fixes you made).
2. A green build in Jenkins.
3. Brief explanation of what you changed and why.

---

## Suggested timeline

| Segment | Duration | Content |
|---------|----------|---------|
| Setup | 45–60 min | EC2 + Jenkins install + GitHub connection |
| Demos 1–3 | 45 min | Freestyle, basic pipeline, stages + tests |
| Demos 4–6 | 45 min | Parameters, artifacts, multibranch |
| Challenges | 60–90 min | Hands-on pipeline exercises |
| Wrap-up | 15 min | Review, Q&A |

---

## Tips

- **Use absolute Python path with Docker Jenkins:** `/usr/bin/python3` instead of `python3`.
- **Read the console output first** when a build fails — Jenkins shows the exact error.
- **One job per demo** keeps things organized. Name jobs to match the folder (e.g. `demo-03-pipeline-stages`).
- **Challenges are open-ended** — there may be more than one correct solution. Focus on a green build that meets the acceptance criteria.

## Reference

- [Demos index](../demos/README.md)
- [Challenges index](../challenges/README.md)
- [Connect Jenkins to GitHub](03-connect-github.md)
