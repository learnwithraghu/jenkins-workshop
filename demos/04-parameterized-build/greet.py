"""Greeting script that reads a name from an environment variable."""

import os


def main():
    name = os.environ.get("GREETING_NAME", "World")
    print(f"Hello, {name}!")
    print("This greeting was customized via a Jenkins build parameter.")


if __name__ == "__main__":
    main()
