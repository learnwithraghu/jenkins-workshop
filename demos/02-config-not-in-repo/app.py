"""Simple hello-world script — same app, but build config lives only in Jenkins."""

import sys


def main():
    print("Hello from Jenkins Workshop!")
    print(f"Python version: {sys.version.split()[0]}")
    print("Build steps for this demo are configured in the Jenkins UI — not in this repo.")


if __name__ == "__main__":
    main()
