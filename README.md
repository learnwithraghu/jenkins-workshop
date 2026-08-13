# Jenkins Workshop

A hands-on workshop for learning Jenkins on Amazon Linux EC2. Install Jenkins (native or Docker), connect it to this GitHub repo, and work through demos and challenges using simple Python builds.

**Repository:** [github.com/learnwithraghu/jenkins-workshop](https://github.com/learnwithraghu/jenkins-workshop)

## Goals

1. **Install Jenkins on Amazon Linux EC2** — step-by-step native install guide
2. **Run Jenkins via Docker** — install Docker and run Jenkins in a container
3. **Connect Jenkins to this repo** — clone from public GitHub, no credentials needed
4. **Learn Jenkins job types** — freestyle, why Jenkinsfile matters, declarative pipeline, stages, parameters, artifacts, parallel, conditional stages
5. **Build and push a container** — simple Docker image, image smoke test + scan, push to Amazon ECR from EC2 (IAM role)
6. **Use Jenkins plugins** — Plugin Manager, Timestamper, HTML Publisher in a Pipeline
7. **Deploy a static site** — serve `index.html` from the Jenkins host, or upload it to S3
8. **Practice with challenges** — create Jenkins jobs for pre-built pipelines

Demos 01–09 use **Python 3 on the Jenkins host**. Demo 10 adds Docker build/push to ECR (native Jenkins on EC2 with Docker + IAM role — not Docker-in-Docker). Demo 11 is a plugins UI session plus a short Pipeline. Demo 12 shows **pollSCM** auto-builds after pushes to `main`. Demo 13 deploys `index.html` on the Jenkins host and serves it on an open port. Demo 14 uploads `index.html` to an S3 bucket in us-east-1 (bucket name and AWS keys are build parameters).

## Prerequisites

- AWS account with permission to launch EC2 instances
- Basic Linux and SSH familiarity
- A web browser to access the Jenkins UI

## Getting started

Follow the docs in order:

| Step | Guide | What you'll do |
|------|-------|----------------|
| 1 | [Prerequisites](docs/00-prerequisites.md) | Launch an Amazon Linux 2023 EC2 instance |
| 2a | [Install Jenkins (native)](docs/01-install-jenkins-native.md) | Java + Jenkins RPM install |
| 2b | [Install Jenkins (Docker)](docs/02-install-docker-jenkins.md) | Docker + Jenkins container |
| 3 | [Connect to GitHub](docs/03-connect-github.md) | Create your first Jenkins job |
| 4 | [Workshop guide](docs/04-workshop-guide.md) | Full demo and challenge path |

Pick **either** 2a or 2b — both work for the rest of the workshop.

## Demos

Each demo folder contains small Python code and a README explaining the Jenkins feature and how to configure the job.

| Demo | Jenkins feature | Job type |
|------|-----------------|----------|
| [01-freestyle-hello](demos/01-freestyle-hello/) | Freestyle project, shell build step | Freestyle |
| [02-config-not-in-repo](demos/02-config-not-in-repo/) | Why UI-only config is a problem | Freestyle |
| [03-pipeline-script-in-jenkins](demos/03-pipeline-script-in-jenkins/) | Inline pipeline script in Jenkins UI | Pipeline |
| [04-pipeline-declarative](demos/04-pipeline-declarative/) | Jenkinsfile in repo, Pipeline from SCM | Pipeline |
| [05-pipeline-stages](demos/05-pipeline-stages/) | Multiple stages, pytest | Pipeline |
| [06-parameterized-build](demos/06-parameterized-build/) | Build parameters | Pipeline |
| [07-post-build-artifacts](demos/07-post-build-artifacts/) | Archive artifacts, JUnit reports | Pipeline |
| [08-parallel-stages](demos/08-parallel-stages/) | Parallel stages | Pipeline |
| [09-pipeline-customize](demos/09-pipeline-customize/) | Conditional stages, recover after a failed build | Pipeline |
| [10-docker-ecr](demos/10-docker-ecr/) | Docker build, test/scan, push to ECR | Pipeline |
| [11-plugins](demos/11-plugins/) | Plugin Manager, Timestamper, HTML Publisher | Pipeline |
| [12-poll-scm](demos/12-poll-scm/) | pollSCM — auto-build after push to main | Pipeline |
| [13-deploy-static-site](demos/13-deploy-static-site/) | Deploy index.html on the Jenkins host | Pipeline |
| [14-deploy-s3](demos/14-deploy-s3/) | Deploy index.html to S3 (bucket parameter) | Pipeline |

See the [demos index](demos/README.md) for details.

## Challenges

Hands-on exercises where you create Jenkins jobs in the UI. All pipeline scripts are pre-configured in the repo — no code editing required.

| Challenge | Your task |
|-----------|-----------|
| [01-create-pipeline-job](challenges/01-create-pipeline-job/) | Create a Pipeline job with Install and Test stages |
| [02-create-staged-pipeline-job](challenges/02-create-staged-pipeline-job/) | Create a Pipeline job with Install, Test, and Run stages |
| [03-create-full-pipeline-job](challenges/03-create-full-pipeline-job/) | Create a Pipeline job with a post-build success message |

See the [challenges index](challenges/README.md) for rules and submission guidelines.

## Repository structure

```
jenkins-workshop/
├── docs/           # Setup and workshop guides
├── demos/          # Guided Jenkins feature demos
└── challenges/     # Hands-on pipeline exercises
```

## License

This workshop material is provided for educational use.
