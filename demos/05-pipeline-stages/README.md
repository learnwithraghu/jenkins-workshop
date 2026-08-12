# Demo 05: Pipeline Stages

## What this teaches

- Multiple pipeline **stages** (Install → Test → Run)
- Installing Python dependencies in a build step
- Running **pytest** in a pipeline stage
- Stage failure stops the build (try breaking a test to see this)

## Instructor talking points

1. **Stages mirror a real CI flow** — Install dependencies, run tests, then run the app; each stage is visible in the stage view.
2. **Tests belong in the pipeline** — pytest runs as a first-class stage, not a manual afterthought.
3. **A failed stage stops later stages** — break a test (or discuss doing so) to show Test turning red and Run being skipped.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-05-pipeline-stages` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/05-pipeline-stages/Jenkinsfile` |

## Expected console output

The Test stage should show pytest output like:

```
test_calculator.py::test_add PASSED
test_calculator.py::test_subtract PASSED
test_calculator.py::test_multiply PASSED
test_calculator.py::test_divide PASSED
test_calculator.py::test_divide_by_zero PASSED
```

The Run stage should print:

```
2 + 3 = 5
```

## Files

| File | Purpose |
|------|---------|
| `calculator.py` | Simple math functions |
| `test_calculator.py` | pytest tests for calculator |
| `requirements.txt` | pytest dependency |
| `Jenkinsfile` | Three-stage pipeline |

## Try it

Break a test in `test_calculator.py`, push to GitHub, and rebuild. Notice the Test stage turns red and the Run stage is skipped.

## Next demo

[06-parameterized-build](../06-parameterized-build/README.md) — pass a name parameter into the build.
