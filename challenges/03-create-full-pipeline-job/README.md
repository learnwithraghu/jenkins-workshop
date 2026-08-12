# Challenge 03: Create a Full Pipeline Job

## Goal

Create a **Pipeline** job for a project that installs dependencies, runs tests, executes the app, and prints a success or failure message in a `post` block. You do not need to edit any code — the `Jenkinsfile` is already in the repo.

## Acceptance criteria

- [ ] Jenkins job named `challenge-03-create-full-pipeline-job`
- [ ] Job pulls its pipeline script from this repo
- [ ] Build is green
- [ ] Stage view shows **Install**, **Test**, and **Run** stages passing
- [ ] Console output includes `Build succeeded!` and temperature conversions

## Expected Run output

```
100°C = 212.0°F
32°F = 0.0°C
```

## Show your work

Be ready to show your job configuration, a green build, and the console output.

## Hints

See [HINTS.md](HINTS.md) if you get stuck.

## Instructor note

All code in this folder is pre-configured. Students only create and configure the Jenkins job. Reference `Jenkinsfile` is in [solution/Jenkinsfile](solution/Jenkinsfile).
