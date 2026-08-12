"""Tests for the report generator."""

import os
from generate_report import generate_report


def test_generate_report_creates_files():
    generate_report()
    assert os.path.exists("report.txt")
    assert os.path.exists("report.json")


def test_report_txt_contains_status():
    generate_report()
    with open("report.txt") as f:
        content = f.read()
    assert "Status: success" in content


def test_report_json_is_valid():
    import json
    generate_report()
    with open("report.json") as f:
        data = json.load(f)
    assert data["status"] == "success"
    assert data["tests_passed"] == 3
