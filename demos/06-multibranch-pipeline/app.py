"""Simple app for the multibranch pipeline demo."""

import os


def main():
    branch = os.environ.get("BRANCH_NAME", "unknown")
    print(f"Running on branch: {branch}")
    print("Multibranch pipeline demo — each branch gets its own job.")


if __name__ == "__main__":
    main()
