"""
This module contains unit tests to validate the functionality of the mystery_7 function. 
The tests cover various scenarios to understand the implementation.

Test categories:
    - Standard cases: Typical lists, tuples, and dictionaries with different character matches.
    - Edge cases: Empty strings, missing characters, and handling of whitespace.
    - Defensive tests: Assertion handling for invalid inputs and type mismatches.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..mystery_7 import mystery_7

class TestMystery7(unittest.TestCase):
    """Tests for mystery_7 function"""

    def test_string(self):
        """It should return the list when the specified character is in one of its elements."""
        self.assertEqual(mystery_7(["hello world"], "o"), ["hello world"])

    def test_long_string(self):
        """It should return the list when the specified character is in the string."""
        self.assertEqual(mystery_7(["hello this is python"], "i"), ["hello this is python"])

    def test_multiple_matches(self):
        """It should return a list of strings containing the specified character."""
        self.assertEqual(mystery_7(["Water", "Money", "cat"], "a"), ["Water", "cat"])

    def test_case_sensitive_match(self):
        """It should match characters case-sensitively."""
        self.assertEqual(mystery_7(["Baby", "noble", "Bamboo"], "B"), ["Baby", "Bamboo"])

    def test_match_with_duplicates(self):
        """It should return a list of duplicate strings with the specified character"""
        self.assertEqual(mystery_7(["B", "C", "c", "d", "C", "c"], "c"), ["c", "c"])

    def test_match_in_tuple(self):
        """It should work with tuples and return strings containing the specified character."""
        self.assertEqual(mystery_7(("Jola", "Mum", "father"), "a"), ["Jola", "father"])

    def test_dictionary(self):
        """It should process dictionaries, checking both keys and values, and return matches."""
        self.assertEqual(mystery_7({'name': 'Jola', 'course': 'Data Scientist'}, "o"), ["course"])

    def test_empty_character(self):
        """It should return the full input list when the specified character is an empty string."""
        self.assertEqual(mystery_7(["Baby", "noble", "Bamboo"], ""), ["Baby", "noble", "Bamboo"])

    def test_split_string(self):
        """It should handle split strings and return parts containing the specified character."""
        self.assertEqual(mystery_7(("hello world this is python".split()), "i"), ["this", "is"])

    def test_match_for_space_character(self):
        """It should match strings containing spaces when specified character is a space."""
        self.assertEqual(mystery_7(("hello world", "python"), " "), ["hello world"])

    def test_numeric_strings(self):
        """It should find the specified digit within numeric strings."""
        self.assertEqual(mystery_7(("123", "5647", "10", "2364", "2"), "2"), ["123", "2364", "2"])

    def test_no_match_found(self):
        """It should return an empty list if the specified character is not found in any string."""
        self.assertEqual(mystery_7(["cat", "dog", "fish"], "z"), [])

    def test_non_iterable_input(self):
        """It should raise an assertion error if `a` is not an iterable of strings."""
        with self.assertRaises(AssertionError):
            mystery_7([1, 2, 3, 4, 5], "1")

    def test_non_string_character(self):
        """It should raise an assertion error if `b` is not a string."""
        with self.assertRaises(AssertionError):
            mystery_7(["111", "2546"], 1)


    if __name__ == '__main__':
        unittest.main()
