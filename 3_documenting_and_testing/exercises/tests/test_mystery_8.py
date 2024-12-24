"""
This module contains unit tests to validate the functionality of the mystery_8 function. 
The tests cover various scenarios to understand the implementation.

Test categories:
    - Standard cases: Typical lists, tuples, and strings with different substring matches.
    - Edge cases: Empty iterables, empty substrings and missing substrings.
    - Defensive tests: Assertion handling for invalid inputs and type mismatches.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..mystery_8 import mystery_8

class TestMystery8(unittest.TestCase):
    """Tests for mystery_8 function"""

    # Standard Cases
    def test_list(self):
        """It should return all list elements containing the specified substring."""
        self.assertEqual(mystery_8(["apple", "banana", "cherry"], "a"), ["apple", "banana"])

    def test_tuple(self):
        """It should return all tuple elements containing the specified substring."""
        self.assertEqual(mystery_8(("hello", "world", "python"), "o"), ["hello", "world", "python"])

    def test_string(self):
        """It should return characters from a string containing the specified substring."""
        self.assertEqual(mystery_8("python", "o"), ["o"])

    # Edge Cases
    def test_empty_iterable(self):
        """It should return an empty list for an empty iterable."""
        self.assertEqual(mystery_8([], "a"), [])
        self.assertEqual(mystery_8("", "a"), [])

    def test_empty_substring(self):
        """It should return all elements of the iterable when the substring is empty."""
        self.assertEqual(mystery_8(["banana", "cherry"], ""), ["banana", "cherry"])

    def test_no_matches(self):
        """It should return an empty list if no elements contain the specified substring."""
        self.assertEqual(mystery_8(["dog", "cat", "fish"], "z"), [])

    # Defensive Tests
    def test_invalid_iterable_type(self):
        """It should raise an assertion error if the first argument is not an iterable."""
        with self.assertRaises(AssertionError):
            mystery_8(123, "a")

    def test_invalid_substring_type(self):
        """It should raise an assertion error if the second argument is not a string."""
        with self.assertRaises(AssertionError):
            mystery_8(["dog", "cat"], 123)

    if __name__ == '__main__':
        unittest.main()
