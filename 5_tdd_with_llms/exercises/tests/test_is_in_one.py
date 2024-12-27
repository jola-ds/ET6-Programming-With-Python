"""
This module contains unit tests to validate `is_in_one` function.
It checks if an item is present in only one of the input lists.

Test categories:
    - Standard cases: Typical lists with common items.
    - Edge cases: Empty lists, single elements, and special characters.
    - Defensive tests: Non-list inputs and non-string items to ensure proper assertion handling.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..is_in_one import is_in_one

class TestIsInOne(unittest.TestCase):
    """Test cases for the is_in_one function"""

    def test_in_one_first(self):
        """Should return True if item is in only b"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_one("yellow", b, d), True)

    def test_in_one_second(self):
        """Should return True if item is in only d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_one("orange", b, d), True)

    def test_single_element(self):
        """Should return True if item is in only b"""
        b = ["grey"]
        d = ["orange"]
        self.assertEqual(is_in_one("grey", b, d), True)

    def test_duplicates(self):
        """Should return True if item is in only d"""
        b = ["yellow", "orange", "pink", "orange"]
        d = ["white", "indigo", "purple", "pink", "white"]
        self.assertEqual(is_in_one("orange", b, d), True)

    def test_empty_string(self):
        """Should return True if empty string is in only b"""
        b = [""]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_one("", b, d), True)

    def test_space(self):
        """Should return True if space character is in only d"""
        b = ["white", "indigo", "purple"]
        d = ["white", "indigo", "purple", "pink", " "]
        self.assertEqual(is_in_one(" ", b, d), True)

    def test_in_both(self):
        """Should return False if item is in both b and d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_one("pink", b, d), False)

    def test_in_neither(self):
        """Should return False if item is in neither b nor d"""
        b = ["yellow", "orange", "pink"]
        d = ["white", "indigo", "purple", "pink"]
        self.assertEqual(is_in_one("black", b, d), False)

    def test_case_sensitive(self):
        """Should return False if item is not found due to case sensitivity"""
        b = ["silver", "gold", "magenta"]
        d = ["gold", "Magenta", "pink"]
        self.assertEqual(is_in_one("Pink", b, d), False)

    def test_empty_list(self):
        """Should return False if item is not in b or d (both empty)"""
        b = []
        d = []
        self.assertEqual(is_in_one("indigo", b, d), False)

    def test_not_list(self):
        """Should raise AssertionError if b or d is not a list"""
        b = ("white", "violet", "black")
        d = ["white", "indigo"]
        with self.assertRaises(AssertionError):
            is_in_one("violet", b, d)

    def test_not_string(self):
        """Should raise AssertionError if item is not a string"""
        b = [1, "2", "3"]
        d = ["8", 7, 6]
        with self.assertRaises(AssertionError):
            is_in_one(1, b, d)

    def test_none(self):
        """Should raise AssertionError if item is None"""
        b = [None, "cyan"]
        d = []
        with self.assertRaises(AssertionError):
            is_in_one(None, b, d)

if __name__ == "__main__":
    unittest.main()
