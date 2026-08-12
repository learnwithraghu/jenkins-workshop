# Challenge 01: Create a Pipeline Job

## Goal

Create a **Pipeline** job in Jenkins that reads its script from this repo and runs successfully. You do not need to edit any code — the `Jenkinsfile` and Python files are already set up.

## Instructor talking points

1. **Students only create the job** — code and `Jenkinsfile` are already in the repo; practice is Pipeline from SCM configuration.
2. **Success looks like two green stages** — Install then Test; confirm Script Path points at this challenge folder.
3. **Check understanding** — ask them to show job config, a green build, and briefly explain why the script comes from SCM.

## Acceptance criteria

- [ ] Jenkins job named `challenge-01-create-pipeline-job`
- [ ] Job pulls its pipeline script from this repo
- [ ] Build is green
- [ ] Stage view shows **Install** and **Test** stages passing

## Show your work

Be ready to show your job configuration, a green build, and the passing stages.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

All code in this folder is pre-configured. Students only create and configure the Jenkins job. The reference `Jenkinsfile` is at the folder root.
