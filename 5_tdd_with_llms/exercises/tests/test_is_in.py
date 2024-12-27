"""
This module contains unit tests to validate `is_in` function.
It checks if an item is present in either of the input lists.

Test categories:
    - Standard cases: Typical lists with common items.
    - Edge cases: Empty lists, single elements, and special characters.
    - Defensive tests: Non-list inputs and non-string items to ensure proper assertion handling.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..is_in import is_in

class TestIsIn(unittest.TestCase):
    """Test cases for the is_in function"""

    def test_in_one_first(self):
        """Should return True if item is in b or d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in("yellow", b, d), True)

    def test_in_one_second(self):
        """Should return True if item is in b or d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in("orange", b, d), True)

    def test_in_both(self):
        """Should return True if item is in b or d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in("pink", b, d), True)

    def test_in_neither(self):
        """Should return False if item is not in b or d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in("black", b, d), False)

    def test_single_element(self):
        """Should return True if item is in b or d"""
        b = ["grey"]
        d = ["orange"]
        self.assertEqual(is_in("grey", b, d), True)

    def test_duplicates(self):
        """Should return True if item is in b or d"""
        b = ["yellow", "orange", "pink", "orange"]
        d = ["white", "indigo", "purple", "pink", "orange"]
        self.assertEqual(is_in("orange", b, d), True)

    def test_empty_string(self):
        """Should return True if empty string is in b or d"""
        b = [""]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in("", b, d), True)

    def test_space(self):
        """Should return True if space character is in b or d"""
        b = ["white", "indigo", "purple"]
        d = ["white", "indigo", "purple", "pink", " "]
        self.assertEqual(is_in(" ", b, d), True)

    def test_case_sensitive(self):
        """Should return False if item is not found due to case sensitivity"""
        b = ["silver", "gold", "magenta"]
        d = ["gold", "Magenta", "pink"]
        self.assertEqual(is_in("Pink", b, d), False)

    def test_empty_list(self):
        """Should return False if item is not in b or d (both empty)"""
        b = []
        d = []
        self.assertEqual(is_in("indigo", b, d), False)

    def test_not_list(self):
        """Should raise AssertionError if b or d is not a list"""
        b = ("white", "violet", "black")
        d = ["white", "indigo"]
        with self.assertRaises(AssertionError):
            is_in("violet", b, d)

    def test_not_string(self):
        """Should raise AssertionError if item is not a string"""
        b = [1, "2", "3"]
        d = ["8", 7, 6]
        with self.assertRaises(AssertionError):
            is_in(1, b, d)

    def test_none(self):
        """Should raise AssertionError if item is None"""
        b = [None, "cyan"]
        d = []
        with self.assertRaises(AssertionError):
            is_in(None, b, d)

if __name__ == "__main__":
    unittest.main()
