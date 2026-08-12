# Challenge 03: Create a Full Pipeline Job

## Goal

Create a **Pipeline** job for a project that installs dependencies, runs tests, executes the app, and prints a success or failure message in a `post` block. You do not need to edit any code — the `Jenkinsfile` is already in the repo.

## Instructor talking points

1. **Full pipeline shape** — Install, Test, Run, plus a `post` success message; this pulls together stages and post-build behavior from the demos.
2. **Console proof** — green stages alone are not enough; look for `Build succeeded!` and the temperature conversion lines.
3. **Check understanding** — ask them to point at the `post` block in the Jenkinsfile (or solution) and explain when that message runs.

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
