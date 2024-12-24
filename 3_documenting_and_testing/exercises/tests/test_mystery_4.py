"""
This module contains unit tests to validate the functionality of the `mystery_4` function.

Test categories:
    - Standard cases: Typical comparisons between positive, negative, and mixed integers.
    - Edge cases: Zero values, equality scenarios, and negatives.
    - Defensive tests: Invalid inputs and assertion handling.

Created on: 2024-12-16
Author: Jola-Moses
"""
import unittest

from ..mystery_4 import mystery_4

class TestMystery4(unittest.TestCase):
    """Tests for mystery_4 function"""

    def test_mystery_4(self):
        """It should evaluate mystery_4(1) to [0]."""
        self.assertEqual(mystery_4(1), [0])

    def test_four(self):
        """It should evaluate mystery_4(5) to [0,1,2,3,4]."""
        self.assertEqual(mystery_4(5), [0,1,2,3,4])

    def test_ten(self):
        """It should evaluate mystery_4(10) to [0,1,2,3,4,5,6,7,8,9]."""
        self.assertEqual(mystery_4(10), [0,1,2,3,4,5,6,7,8,9])

    def test_negative_one(self):
        """It should evaluate mystery_4(-1) to []."""
        self.assertEqual(mystery_4(-1), [])

    def test_negative_twenty(self):
        """It should evaluate mystery_4([-20) to []."""
        self.assertEqual(mystery_4(-20), [])

    def test_zero(self):
        """It should evaluate mystery_4([0) to []."""
        self.assertEqual(mystery_4(0), [])

    def test_bool_true(self):
        """It should evaluate mystery_4([0) to []."""
        self.assertEqual(mystery_4(True), [0])

    def test_bool_false(self):
        """It should evaluate mystery_4([0) to []."""
        self.assertEqual(mystery_4(False), [])

    def test_string(self):
        """It should raise an assertion error if a is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_4("2")
    def test_float(self):
        """It should raise an assertion error if a is not an integer."""
        with self.assertRaises(AssertionError):
            mystery_4(2.5)

    def test_none(self):
        """It should raise an assertion error if a is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_4(None)

    if __name__ == "__main__":
        unittest.main()
