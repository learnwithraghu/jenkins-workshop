"""Simple app for the pollSCM demo."""

import datetime


def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    print("Poll SCM demo — this build was started by Jenkins.")
    print(f"Current time: {now}")
    print("If you just pushed to main, the cause is likely: Started by an SCM change.")


if __name__ == "__main__":
    main()
