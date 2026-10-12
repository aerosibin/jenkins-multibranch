import unittest
from app import greet
from app import login


class TestApp(unittest.TestCase):

    def test_greet(self):
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins!")

    def test_greet_with_spaces(self):
        self.assertEqual(greet("  Sibin  "), "Hello, Sibin!")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")

    def test_whitespace_name(self):
        with self.assertRaises(ValueError):
            greet("   ")

    #new login tests
    def test_login_success(self):
        self.assertTrue(login("admin", "secret123"))

    def test_login_failure_wrong_password(self):
        self.assertFalse(login("admin", "wrongpassword"))

    def test_login_failure_wrong_user(self):
        self.assertFalse(login("unknown", "secret123"))

    def test_login_empty_credentials(self):
        self.assertFalse(login("", ""))

if __name__ == "__main__":
    unittest.main()