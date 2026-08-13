"""Stdlib tests for the pipeline-customize demo app."""

import os
import subprocess
import sys
import unittest
from pathlib import Path

APP = Path(__file__).resolve().parent / "app.py"


def run_app(mode="status", extra_env=None):
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    return subprocess.run(
        [sys.executable, str(APP), mode],
        capture_output=True,
        text=True,
        env=env,
    )


class TestStatus(unittest.TestCase):
    def test_default_status_succeeds(self):
        result = run_app("status")
        self.assertEqual(result.returncode, 0)
        self.assertIn("workshop-app", result.stdout)

    def test_invalid_environment_fails(self):
        result = run_app("status", {"ENVIRONMENT": "qa"})
        self.assertNotEqual(result.returncode, 0)

    def test_force_fail_exits_nonzero(self):
        result = run_app("status", {"FORCE_FAIL": "true"})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("FORCE_FAIL", result.stdout)

    def test_recover_mode(self):
        result = run_app("recover")
        self.assertEqual(result.returncode, 0)
        self.assertIn("previous Jenkins build failed", result.stdout)


if __name__ == "__main__":
    unittest.main()
