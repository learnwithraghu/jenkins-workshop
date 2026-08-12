# Demo 08: Multibranch Pipeline

## What this teaches

- Creating a **Multibranch Pipeline** that discovers branches automatically
- Each branch gets its own sub-job with the same `Jenkinsfile`
- Jenkins sets `BRANCH_NAME` automatically in multibranch builds
- Scanning the repo for new branches

## Jenkins job setup

| Setting | Value |
|---------|-------|
| Job name | `demo-08-multibranch-pipeline` |
| Job type | **Multibranch Pipeline** |
| Branch Sources | Git |
| Repository URL | `https://github.com/learnwithraghu/jenkins-workshop.git` |
| Behaviors | Discover branches |
| Script Path | `demos/08-multibranch-pipeline/Jenkinsfile` |

### Step-by-step

1. Click **New Item** → name: `demo-08-multibranch-pipeline`.
2. Select **Multibranch Pipeline** → **OK**.
3. Under **Branch Sources**, click **Add source** → **Git**.
4. Set **Project Repository** to `https://github.com/learnwithraghu/jenkins-workshop.git`.
5. Under **Build Configuration**, set **Script Path** to `demos/08-multibranch-pipeline/Jenkinsfile`.
6. Click **Save**. Jenkins will scan branches and create jobs.

## Expected behavior

- Jenkins discovers the `main` branch and runs the pipeline.
- Console output shows:

```
Running on branch: main
Multibranch pipeline demo — each branch gets its own job.
```

## Try it: add a feature branch

To see multibranch in action, create a branch locally and push:

```bash
git checkout -b feature/demo-branch
# make any small change, commit, and push
git push -u origin feature/demo-branch
```

Click **Scan Repository Now** on the multibranch job. Jenkins should discover `feature/demo-branch` and build it.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Prints the current branch name |
| `Jenkinsfile` | Simple two-stage pipeline |

## Workshop complete!

You've finished all demos. Head to the [challenges](../../challenges/README.md) to practice creating Jenkins jobs yourself.
