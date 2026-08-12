"""Unit tests for the hello app (stdlib only — no pytest required)."""

import unittest

from app import MESSAGE, PORT, create_server


class TestApp(unittest.TestCase):
    def test_message_content(self):
        self.assertEqual(MESSAGE, b"Hello from Jenkins Docker demo!\n")

    def test_message_is_utf8_text(self):
        text = MESSAGE.decode("utf-8")
        self.assertTrue(text.startswith("Hello"))

    def test_default_port(self):
        self.assertEqual(PORT, 8080)

    def test_create_server_binds_expected_port(self):
        server = create_server(port=0)  # ephemeral port
        try:
            host, port = server.server_address
            self.assertEqual(host, "0.0.0.0")
            self.assertGreater(port, 0)
        finally:
            server.server_close()


if __name__ == "__main__":
    unittest.main()
