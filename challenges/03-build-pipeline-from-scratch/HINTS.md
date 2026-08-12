# Hints for Challenge 03

<details>
<summary>Hint 1: Start from a demo</summary>

Look at [demo 03](../../demos/03-pipeline-stages/Jenkinsfile) for a working three-stage pipeline. Copy its structure and change the paths and commands.
</details>

<details>
<summary>Hint 2: File location</summary>

Create the file at `challenges/03-build-pipeline-from-scratch/Jenkinsfile` in this repo. Jenkins reads it from SCM, so you need to commit and push (or work on a branch).
</details>

<details>
<summary>Hint 3: Post block</summary>

```groovy
post {
    success {
        echo 'Build succeeded!'
    }
    failure {
        echo 'Build failed!'
    }
}
```
</details>

<details>
<summary>Hint 4: All commands need the right directory</summary>

Every `sh` step should start with:

```bash
cd challenges/03-build-pipeline-from-scratch && ...
```
</details>
