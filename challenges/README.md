# Challenges

Hands-on exercises where you fix or write Jenkins pipelines. Complete the [demos](../demos/README.md) first — they teach the concepts you'll need here.

## Rules

1. **Read the README** in each challenge folder for the goal and acceptance criteria.
2. **Create a Jenkins job** for each challenge (Pipeline type, script from SCM).
3. **Show your work** — be ready to demonstrate a green build and explain your changes.
4. **Hints are optional** — each challenge has a `HINTS.md` file. Try on your own first.

## Challenges

| # | Challenge | Your task | Starter state |
|---|-----------|-----------|---------------|
| 1 | [01-fix-failing-tests](01-fix-failing-tests/) | Fix broken tests so the pipeline passes | Tests intentionally fail |
| 2 | [02-add-missing-stage](02-add-missing-stage/) | Add a missing Test stage to the pipeline | Incomplete Jenkinsfile |
| 3 | [03-build-pipeline-from-scratch](03-build-pipeline-from-scratch/) | Write a full declarative pipeline from requirements | No Jenkinsfile |

## Jenkins job quick reference

| Setting | Value |
|---------|-------|
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `challenges/<challenge-folder>/Jenkinsfile` |

## Show your instructor

For each challenge:

1. Your Jenkinsfile (or the fixes you made to Python tests).
2. A green build in Jenkins.
3. Brief explanation of what you changed and why.

## Instructor note

Each challenge has a `solution/` folder with reference answers:

- [01-fix-failing-tests/solution/](01-fix-failing-tests/solution/)
- [02-add-missing-stage/solution/](02-add-missing-stage/solution/)
- [03-build-pipeline-from-scratch/solution/](03-build-pipeline-from-scratch/solution/)

Students should attempt the challenge before looking at solutions.

## Full workshop path

See the [workshop guide](../docs/04-workshop-guide.md) for the complete ordered checklist.
