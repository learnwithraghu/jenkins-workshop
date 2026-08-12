# Hints for Challenge 02

<details>
<summary>Hint 1: Stage syntax</summary>

A stage looks like this:

```groovy
stage('StageName') {
    steps {
        sh 'your command here'
    }
}
```

Add it between the Install and Run stages in the Jenkinsfile.
</details>

<details>
<summary>Hint 2: The test command</summary>

```bash
cd challenges/02-add-missing-stage && python3 -m pytest test_app.py -v
```
</details>

<details>
<summary>Hint 3: Stage order matters</summary>

If tests fail, the Run stage should not execute. That's why Test comes before Run.
</details>
