"""
This module contains unit tests for the `mystery_6` function, which generates a list of numbers 
starting from a given number and incremented by 1 for a specified count.

Test Categories:
    - Standard tests: Valid combinations of count and starting numbers.
    - Edge cases: Negative counts, non-integer inputs, large starting numbers.
    - Defensive tests: Assertion handling for invalid inputs.

Created on: 2024-12-19
Author: Jola-Moses
"""

import unittest

from ..mystery_6 import mystery_6

class TestMystery6(unittest.TestCase):
    """Tests  for mystery_6 function"""

    def test_one(self):
        """It should return a list of one number starting from 1, incremented by 1."""
        self.assertEqual(mystery_6(1, 1), [1])

    def test_two(self):
        """It should return a list of two numbers starting from 1, incremented by 1."""
        self.assertEqual(mystery_6(2, 1), [1, 2])

    def test_three(self):
        """It should return a list of three numbers starting from 2, incremented by 1."""
        self.assertEqual(mystery_6(3, 2), [2, 3, 4])

    def test_four(self):
        """It should return a list of four numbers starting from 3, incremented by 1."""
        self.assertEqual(mystery_6(4, 3), [3, 4, 5, 6])

    def test_five(self):
        """It should return a list of five numbers starting from 4, incremented by 1."""
        self.assertEqual(mystery_6(5, 4), [4, 5, 6, 7, 8])

    def test_six(self):
        """It should return a list of six numbers starting from 5, incremented by 1."""
        self.assertEqual(mystery_6(6, 5), [5, 6, 7, 8, 9, 10])

    def test_floats(self):
        """It should return a list of four numbers starting from 2.5, incremented by one."""
        self.assertEqual(mystery_6(4, 2.5), [2.5, 3.5, 4.5, 5.5])

    def test_negative_start_one(self):
        """It should return a list of three numbers starting from negative 1, incremented by 1."""
        self.assertEqual(mystery_6(3, -1), [-1, 0, 1])

    def test_negative_start_three(self):
        """It should return a list of seven numbers starting from negative 1, incremented by 1."""
        self.assertEqual(mystery_6(7, -3), [-3, -2, -1, 0, 1, 2, 3])

    def test_zero_start(self):
        """It should return a list of three numbers starting from 0, incremented by 1."""
        self.assertEqual(mystery_6(3, 0), [0, 1, 2])

    def test_large_start(self):
        """It should handle a large starting number."""
        self.assertEqual(mystery_6(4, 10230), [10230, 10231, 10232, 10233])

    def test_zero_count(self):
        """It should handle a count of zero by returning an empty list."""
        self.assertEqual(mystery_6(0, 4), [])

    def test_negative_count(self):
        """It should handle a negative count by returning an empty list."""
        self.assertEqual(mystery_6(-3, 4), [])

    def test_non_integer_start(self):
        """It should raise an assertion error if the starting number is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_6(6, "6")

    def test_non_integer_count(self):
        """It should raise an assertion error if count number is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_6(3.5, 3)

if __name__ == '__main__':
    unittest.main()
