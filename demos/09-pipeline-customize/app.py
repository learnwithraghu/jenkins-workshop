"""Release status app driven by Jenkins pipeline parameters."""

import os
import sys
from datetime import datetime, timezone

ALLOWED_ENVIRONMENTS = ("dev", "staging", "prod")


def env(name, default=""):
    return os.environ.get(name, default)


def force_fail_enabled():
    return env("FORCE_FAIL", "false").lower() in ("1", "true", "yes")


def print_status_card():
    app_name = env("APP_NAME", "workshop-app")
    environment = env("ENVIRONMENT", "dev")
    log_level = env("LOG_LEVEL", "INFO")
    notes = env("RELEASE_NOTES", "First workshop release")

    print(f"App: {app_name}")
    print(f"Environment: {environment}")
    print(f"Log level: {log_level}")
    print(f"Release notes: {notes}")

    if log_level.upper() == "DEBUG":
        print(f"Python version: {sys.version.split()[0]}")
        print(f"UTC time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")

    if environment not in ALLOWED_ENVIRONMENTS:
        print(
            f"ERROR: ENVIRONMENT must be one of {ALLOWED_ENVIRONMENTS}, "
            f"got {environment!r}"
        )
        return 1

    if force_fail_enabled():
        print("ERROR: FORCE_FAIL is set — failing this Run stage on purpose.")
        print("Rebuild with FORCE_FAIL=false to see the Recover stage on the next build.")
        return 1

    return 0


def print_recover():
    print("Recover stage — the previous Jenkins build failed.")
    print("Running extra checks before continuing.")
    print(f"App: {env('APP_NAME', 'workshop-app')}")
    print(f"Environment: {env('ENVIRONMENT', 'dev')}")
    print(f"Log level: {env('LOG_LEVEL', 'INFO')}")
    return 0


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "status"
    if mode == "recover":
        code = print_recover()
    elif mode == "status":
        code = print_status_card()
    else:
        print("Usage: app.py [status|recover]")
        code = 2
    sys.exit(code)


if __name__ == "__main__":
    main()
