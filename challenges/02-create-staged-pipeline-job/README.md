# Challenge 02: Create a Staged Pipeline Job

## Goal

Create a **Pipeline** job for a project that runs three stages: Install, Test, and Run. You do not need to edit any code — the `Jenkinsfile` is already complete.

## Instructor talking points

1. **Same skill as Challenge 01, more stages** — students configure Pipeline from SCM; the `Jenkinsfile` already defines Install → Test → Run.
2. **Stage order matters** — acceptance requires all three stages green, in that order, on the stage view.
3. **Check understanding** — ask what each stage does and where the Script Path points; reference `solution/Jenkinsfile` if they get stuck.

## Acceptance criteria

- [ ] Jenkins job named `challenge-02-create-staged-pipeline-job`
- [ ] Job pulls its pipeline script from this repo
- [ ] Build is green
- [ ] Stage view shows **Install**, **Test**, and **Run** stages passing (in that order)

## Show your work

Be ready to show your job configuration, a green build, and explain what each stage does.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

All code in this folder is pre-configured. Students only create and configure the Jenkins job. Reference `Jenkinsfile` is in [solution/Jenkinsfile](solution/Jenkinsfile).
