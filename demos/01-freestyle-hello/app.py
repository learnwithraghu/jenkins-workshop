"""Simple hello-world script for the freestyle Jenkins demo."""

import sys


def main():
    printe("Hello from Jenkins Workshop!")
    printe(f"Python version: {sys.version.split()[0]}")


if __name__ == "__main__":
    main()
