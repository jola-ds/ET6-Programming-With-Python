"""
This module contains unit tests to validate the functionality of the `check_less` function.
It determines the smaller of two integers or returns their sum if the integers are equal.

Test categories:
    - Standard cases: Typical comparisons between positive, negative, and mixed integers.
    - Edge cases: Zero values, equality scenarios, and negatives.
    - Defensive tests: Invalid inputs and assertion handling.

Created on: 2024-12-10
Author: Jola-Moses
"""


import unittest

from ..check_less import check_less

class TestCheckLess(unittest.TestCase):
    """Tests for check_less function"""

    def test_three_five(self):
        """It should evaluate check_less(3, 5) to 3."""
        self.assertEqual(check_less(3, 5), 3)

    def test_ten_five(self):
        """It should evaluate check_less(10, 5) to 5."""
        self.assertEqual(check_less(10, 5), 5)

    def test_negative_positive(self):
        """It should evaluate check_less(-15, 15) to -15."""
        self.assertEqual(check_less(-15, 15), -15)

    def test_positive_zero(self):
        """It should evaluate check_less(35, 0) to 0."""
        self.assertEqual(check_less(35, 0), 0)

    def test_zero_positive(self):
        """It should evaluate check_less(0, 40) to 0."""
        self.assertEqual(check_less(0, 40), 0)

    def test_negative_zero(self):
        """It should evaluate check_less(-13, 0) to -13."""
        self.assertEqual(check_less(-13, 0), -13)

    def test_zero_negative(self):
        """It should evaluate check_less(0, -9) to -9."""
        self.assertEqual(check_less(0, -9), -9)

    def test_equal_negative(self):
        """It should evaluate check_less(-9, -9) to -18."""
        self.assertEqual(check_less(-9, -9), -18)

    def test_equal_positive(self):
        """It should evaluate check_less(30, 30) to 60."""
        self.assertEqual(check_less(30, 30), 60)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            check_less(3.2, 3)

    def test_zero_zero(self):
        """It should raise an assertion error if both arguments are zero"""
        with self.assertRaises(AssertionError):
            check_less(0, 0)


if __name__ == "__main__":
    unittest.main()
