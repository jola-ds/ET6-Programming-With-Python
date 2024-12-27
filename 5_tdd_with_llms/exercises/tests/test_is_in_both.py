"""
This module contains tests to validate the functionality of the `is_in_both` function.
It checks if an item is present in both of the input lists.

Test categories:
    - Standard cases: Typical lists with common items.
    - Edge cases: Empty lists and lists with a single element.
    - Defensive tests: Non-list inputs and non-string items to ensure proper assertion handling.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..is_in_both import is_in_both

class TestIsInBoth(unittest.TestCase):
    """Test cases for the is_in_both function"""

    def test_in_both(self):
        """Should return True if item is in both lists"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_both("pink", b, d), True)

    def test_single_element(self):
        """Should return True if item is in both lists with only one element"""
        b = ["orange"]
        d = ["orange"]
        self.assertEqual(is_in_both("orange", b, d), True)

    def test_duplicates(self):
        """Should return True if item is in both lists with duplicates"""
        b = ["yellow", "orange", "pink", "orange"]
        d = ["white", "indigo", "purple", "pink", "orange"]
        self.assertEqual(is_in_both("orange", b, d), True)

    def test_space(self):
        """Should return True if space character is in both lists"""
        b = [" "]
        d = ["white", "indigo", "purple", "pink", " "]
        self.assertEqual(is_in_both(" ", b, d), True)

    def test_empty_string(self):
        """Should return True if empty string is in both lists"""
        b = [""]
        d = ["white", "indigo", "purple", "pink", ""]
        self.assertEqual(is_in_both("", b, d), True)

    def test_in_neither(self):
        """Should return False if item is in neither list"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_both("black", b, d), False)

    def test_case_sensitive(self):
        """Should return False if item is not in both lists due to case sensitivity"""
        b = ["silver", "gold", "magenta"]
        d = ["gold", "Magenta", "pink"]
        self.assertEqual(is_in_both("Magenta", b, d), False)

    def test_not_list(self):
        """Should raise AssertionError if b or d is not a list"""
        b = ("white", "black")
        d = ["white", "indigo", "purple", "pink", " "]
        with self.assertRaises(AssertionError):
            is_in_both("white", b, d)

    def test_not_string(self):
        """Should raise AssertionError if item is not a string"""
        b = ["white", "black"]
        d = ["white", "indigo", "purple", "pink", " "]
        with self.assertRaises(AssertionError):
            is_in_both(1, b, d)

    def test_none(self):
        """Should raise AssertionError if item is None"""
        b = [None, "cyan"]
        d = []
        with self.assertRaises(AssertionError):
            is_in_both(None, b, d)

if __name__ == "__main__":
    unittest.main()
