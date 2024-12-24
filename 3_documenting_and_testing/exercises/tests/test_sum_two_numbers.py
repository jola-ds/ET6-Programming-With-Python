"""
This module contains unit tests to validate the functionality of the `sum_two_numbers` function.
It performs basic addition for two numbers and supports integer and float inputs.

Test categories:
    - Standard cases: Typical addition of positive and negative integers and floats.
    - Edge cases: Zero values, negative numbers, and mixed types.
    - Defensive tests: Invalid inputs and assertion checks.

Created on: 2024-12-08
Author: Jola-Moses
"""


import unittest
from..sum_two_numbers import sum_two_numbers

class TestSumTwoNumbers(unittest.TestCase):
    """Test the sum_two_numbers function."""

    def test_zero_one(self):
        """It should evaluate sum_two_numbers(0, 1) to 1."""
        self.assertEqual(sum_two_numbers(0, 1), 1)

    def test_one_two(self):
        """It should evaluate sum_two_numbers(1, 2) to 3."""
        self.assertEqual(sum_two_numbers(1, 2), 3)

    def test_add_negative_and_positive_number(self):
        """It should evaluate sum_two_numbers(3, -2) to 1."""
        self.assertEqual(sum_two_numbers(3, -2), 1)

    def test_add_two_negative_numbers(self):
        """It should evaluate sum_two_numbers(-2, -3) to -5."""
        self.assertEqual(sum_two_numbers(-2, -3), -5)

    def test_add_negative_number_and_zero(self):
        """It should evaluate sum_two_numbers(-4, 0) to -4."""
        self.assertEqual(sum_two_numbers(-4, 0), -4)

    def test_add_two_floats(self):
        """It should evaluate sum_two_numbers(5.3, 2.4) to 7.7."""
        self.assertAlmostEqual(sum_two_numbers(5.3, 2.4), 7.7, places=1)

    def test_add_float_and_integer(self):
        """It should evaluate sum_two_numbers(2.5, 3) to 5.5."""
        self.assertAlmostEqual(sum_two_numbers(2.5, 3), 5.5)

    def test_add_float_with_negative(self):
        """It should evaluate sum_two_numbers(5.0, -2.5) to 2.5."""
        self.assertAlmostEqual(sum_two_numbers(5.0, -2.5), 2.5)

    def test_zero_zero(self):
        """It should raise an assertion error if the argument are both 0"""
        with self.assertRaises(AssertionError):
            sum_two_numbers(0,0)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            sum_two_numbers("6",3)

if __name__ == "__main__":
    unittest.main()
