"""Generates a simple report file for the artifacts demo."""

import json
from datetime import datetime, timezone


def generate_report():
    report = {
        "project": "jenkins-workshop",
        "demo": "05-post-build-artifacts",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "success",
        "tests_run": 3,
        "tests_passed": 3,
    }
    with open("report.txt", "w") as f:
        f.write(f"Build Report\n")
        f.write(f"============\n")
        f.write(f"Project: {report['project']}\n")
        f.write(f"Demo: {report['demo']}\n")
        f.write(f"Generated: {report['generated_at']}\n")
        f.write(f"Status: {report['status']}\n")
        f.write(f"Tests: {report['tests_passed']}/{report['tests_run']} passed\n")

    with open("report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("Report generated: report.txt, report.json")


if __name__ == "__main__":
    generate_report()
