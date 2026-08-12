# Jenkins Workshop

A hands-on workshop for learning Jenkins on Amazon Linux EC2. Install Jenkins (native or Docker), connect it to this GitHub repo, and work through demos and challenges using simple Python builds.

**Repository:** [github.com/learnwithraghu/jenkins-workshop](https://github.com/learnwithraghu/jenkins-workshop)

## Goals

1. **Install Jenkins on Amazon Linux EC2** — step-by-step native install guide
2. **Run Jenkins via Docker** — install Docker and run Jenkins in a container
3. **Connect Jenkins to this repo** — clone from public GitHub, no credentials needed
4. **Learn Jenkins job types** — freestyle, declarative pipeline, stages, parameters, artifacts, multibranch
5. **Practice with challenges** — fix broken pipelines and build new ones from scratch

All builds use **Python 3 on the Jenkins host**. No Docker-in-Docker or container builds.

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
| [02-pipeline-declarative](demos/02-pipeline-declarative/) | Declarative Pipeline, basic stages | Pipeline |
| [03-pipeline-stages](demos/03-pipeline-stages/) | Multiple stages, pytest | Pipeline |
| [04-parameterized-build](demos/04-parameterized-build/) | Build parameters | Pipeline |
| [05-post-build-artifacts](demos/05-post-build-artifacts/) | Archive artifacts, JUnit reports | Pipeline |
| [06-multibranch-pipeline](demos/06-multibranch-pipeline/) | Multibranch Pipeline | Multibranch Pipeline |

See the [demos index](demos/README.md) for details.

## Challenges

Hands-on exercises where you write or fix Jenkins pipelines. Starter code is provided; solutions are in each challenge's `solution/` folder for instructors.

| Challenge | Your task |
|-----------|-----------|
| [01-fix-failing-tests](challenges/01-fix-failing-tests/) | Fix broken tests so the pipeline passes |
| [02-add-missing-stage](challenges/02-add-missing-stage/) | Add a missing Test stage to the pipeline |
| [03-build-pipeline-from-scratch](challenges/03-build-pipeline-from-scratch/) | Write a full declarative pipeline from requirements |

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
