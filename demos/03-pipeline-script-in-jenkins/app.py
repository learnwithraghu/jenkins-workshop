"""Simple hello-world script for the inline pipeline demo."""

import sys


def main():
    print("Hello from Jenkins Pipeline!")
    print(f"Python version: {sys.version.split()[0]}")
    print("Pipeline script is pasted into Jenkins — still not stored in this repo.")


if __name__ == "__main__":
    main()
