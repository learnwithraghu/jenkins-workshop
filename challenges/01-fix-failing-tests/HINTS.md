# Hints for Challenge 01

<details>
<summary>Hint 1: Which tests fail?</summary>

Run the tests locally to see which ones fail:

```bash
cd challenges/01-fix-failing-tests
pip3 install -r requirements.txt
python3 -m pytest test_math_utils.py -v
```

Two tests should fail: `test_multiply` and `test_is_even`.
</details>

<details>
<summary>Hint 2: test_multiply</summary>

What is 3 × 4? Check that your expected value matches.
</details>

<details>
<summary>Hint 3: test_is_even</summary>

`is_even(4)` should return `True`, not `False`. Fix the assertion, not the function.
</details>
