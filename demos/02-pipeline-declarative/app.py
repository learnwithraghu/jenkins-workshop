"""Simple hello-world script for the declarative pipeline demo."""

import sys


def main():
    print("Hello from Jenkins Pipeline!")
    print(f"Python version: {sys.version.split()[0]}")


if __name__ == "__main__":
    main()
