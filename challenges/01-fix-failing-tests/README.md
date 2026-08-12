# Challenge 01: Fix Failing Tests

## Goal

The pipeline runs, but two tests fail. Find and fix the bugs in `test_math_utils.py` so the build goes green.

Do **not** modify `math_utils.py` — the implementation is correct.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `challenge-01-fix-failing-tests` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `challenges/01-fix-failing-tests/Jenkinsfile` |

## Acceptance criteria

- [ ] All 5 tests pass (`pytest` exits with code 0)
- [ ] `math_utils.py` is unchanged
- [ ] Jenkins build is green

## Show your work

1. Show the failing build (before your fix).
2. Explain which assertions were wrong and why.
3. Show the green build after your fix.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

Solution test file is in [solution/test_math_utils.py](solution/test_math_utils.py).
