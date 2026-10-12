import unittest
from app import greet


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


if __name__ == "__main__":
    unittest.main()