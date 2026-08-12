# Challenge 03: Build Pipeline from Scratch

## Goal

There is no Jenkinsfile in this folder. Write a complete **Declarative Pipeline** from scratch that installs dependencies, runs tests, and executes the app.

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `challenge-03-build-pipeline-from-scratch` |
| Job type | Pipeline |
| Definition | Pipeline script from SCM |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Branch | `*/main` |
| Script Path | `challenges/03-build-pipeline-from-scratch/Jenkinsfile` |

You will need to **create** the `Jenkinsfile` in this folder (commit and push it, or use a local branch).

## Requirements

Your pipeline must:

1. Use `agent any`
2. Have an **Install** stage that runs `pip3 install -r requirements.txt`
3. Have a **Test** stage that runs `python3 -m pytest test_app.py -v`
4. Have a **Run** stage that runs `python3 app.py`
5. Include a `post` block that echoes success or failure
6. All `sh` steps should `cd` into `challenges/03-build-pipeline-from-scratch` first

## Acceptance criteria

- [ ] `Jenkinsfile` exists at `challenges/03-build-pipeline-from-scratch/Jenkinsfile`
- [ ] All 4 tests pass
- [ ] Run stage prints temperature conversions
- [ ] `post` block echoes a message on success or failure
- [ ] Jenkins build is green

## Expected Run output

```
100°C = 212.0°F
32°F = 0.0°C
```

## Show your work

1. Show your complete Jenkinsfile.
2. Show the stage view with Install, Test, and Run all green.
3. Walk through what each stage does.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

Solution Jenkinsfile is in [solution/Jenkinsfile](solution/Jenkinsfile).
