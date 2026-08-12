# Demo 08: Parallel Stages

## What this teaches

- Declarative Pipeline **`parallel`** blocks
- Two stages running at the same time (visible in the stage view)
- A failed parallel branch fails the parent stage and skips later stages
- Same **Pipeline from SCM** job type as demos 04–07 (no Multibranch)

## Instructor talking points

1. **Parallel stages save wall-clock time** — Unit A and Unit B start together; the stage view shows side-by-side branches under **Parallel Checks**.
2. **Fail-fast still applies** — break a test in `test_left.py` or `test_right.py`, rebuild, and show the failed branch turning red and **Summary** being skipped.
3. **Still one Pipeline job** — students do not need a Multibranch job type to use `parallel`.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-08-parallel-stages` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `demos/08-parallel-stages/Jenkinsfile` |

## What to look for after a successful build

1. **Stage view** — **Parallel Checks** splits into **Unit A** and **Unit B** side by side.
2. **Console** — pytest output from both `test_left.py` and `test_right.py`.
3. **Summary** — echo: `Both parallel branches finished`.

## Expected console output (excerpt)

```
test_left.py::test_string_upper PASSED
test_left.py::test_list_length PASSED
...
test_right.py::test_sum PASSED
test_right.py::test_dict_lookup PASSED
Both parallel branches finished
```

## Try it

Break a test in `test_left.py` (or `test_right.py`), push, and rebuild. Notice one parallel branch turns red and **Summary** is skipped.

## Files

| File | Purpose |
|------|---------|
| `test_left.py` | pytest tests for parallel branch Unit A |
| `test_right.py` | pytest tests for parallel branch Unit B |
| `requirements.txt` | pytest dependency |
| `Jenkinsfile` | Install → Parallel Checks → Summary |

## Next demo

[09-docker-ecr](../09-docker-ecr/README.md) — Docker build, image test/scan, push to ECR.
