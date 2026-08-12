# Challenge 02: Add Missing Stage

## Goal

The Jenkinsfile has Install and Run stages, but it's missing a **Test** stage. Add a Test stage that runs pytest between Install and Run.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `challenge-02-add-missing-stage` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `challenges/02-add-missing-stage/Jenkinsfile` |

## Acceptance criteria

- [ ] Pipeline has three stages: Install, Test, Run (in that order)
- [ ] Test stage runs `python3 -m pytest test_app.py -v`
- [ ] All tests pass
- [ ] Run stage executes after Test passes
- [ ] Jenkins build is green

## Show your work

1. Show your updated Jenkinsfile.
2. Show the stage view with all three stages green.
3. Explain why the Test stage should come before Run.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

Solution Jenkinsfile is in [solution/Jenkinsfile](solution/Jenkinsfile).
