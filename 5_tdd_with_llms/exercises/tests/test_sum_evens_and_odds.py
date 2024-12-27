"""
Unit tests for sum_evens_and_odds function.

This test suite validates sum_evens_and_odds function 
by testing basic functionality, handling of edge cases, and defensive checks.
"""

import unittest

from ..sum_evens_and_odds import sum_evens_and_odds


class TestSumEvensAndOdds(unittest.TestCase):
    """Testing sun_evens_and_odds function"""

    def test_basic(self):
        """It should evaluate [7, 2, 3, 6] to Evens:8, Odds:10."""
        self.assertEqual(sum_evens_and_odds([7, 2, 3, 6]), {'Evens': 8, 'Odds': 10})

    def test_repeated_numbers(self):
        """It should evaluate [5, 5, 2, 2] to Evens:4, Odds:10."""
        self.assertEqual(sum_evens_and_odds([5, 5, 2, 2]), {'Evens': 4, 'Odds': 10})

    def test_all_odds(self):
        """It should evaluate [7, 7, 7, 7, 7] to Evens:0, Odds:35."""
        self.assertEqual(sum_evens_and_odds([7, 7, 7, 7, 7]), {'Evens': 0, 'Odds': 35})

    def test_all_evens(self):
        """It should evaluate [2, 2, 2, 2, 2] to Evens:10, Odds:0."""
        self.assertEqual(sum_evens_and_odds([2, 2, 2, 2, 2]), {'Evens': 10, 'Odds': 0})

    def test_single_number_odd(self):
        """It should evaluate [1] to Evens:0, Odds:1."""
        self.assertEqual(sum_evens_and_odds([1]), {'Evens': 0, 'Odds': 1})

    def test_single_number_even(self):
        """It should evaluate [12] to Evens:12, Odds:0."""
        self.assertEqual(sum_evens_and_odds([12]), {'Evens': 12, 'Odds': 0})

    def test_zero(self):
        """It should evaluate [0] to Evens:0, Odds:0."""
        self.assertEqual(sum_evens_and_odds([0]), {'Evens': 0, 'Odds': 0})

    def test_range(self):
        """It should sum a range of integers."""
        self.assertEqual(sum_evens_and_odds([7, 40000, 50, 1, 1000]), {'Evens': 41050, 'Odds': 8})

    def test_negative_numbers(self):
        """It should sum a list of negative integers."""
        self.assertEqual(sum_evens_and_odds([-3, -1, -2, -4]), {'Evens': -6, 'Odds': -4})

    def test_negative_positive(self):
        """It should sum a list of negative and positive integers."""
        self.assertEqual(sum_evens_and_odds([-3, 3, 0, 1, -1, -2, 4, -4]), {'Evens': -2, 'Odds': 0})

    def test_floats(self):
        """It should sum floats as odd numbers."""
        self.assertEqual(sum_evens_and_odds([8.2, 2.4, 3.78, 6.2]), {'Evens': 0, 'Odds': 20.58})

    def test_floating_point_integers(self):
        """It should sum floating-point integers as evens and odds."""
        self.assertEqual(sum_evens_and_odds([7.0, 6.0, 5.0, 4.0]), {'Evens': 10.0, 'Odds': 12.0})

    def test_floats_integers(self):
        """It should sum a list of floats and integers."""
        self.assertEqual(sum_evens_and_odds([2.2, 2.0, 3.4, 6, 5]), {'Evens': 8.0, 'Odds': 10.6})

    def test_empty_list(self):
        """It should evaluate an empty list to Evens:0, Odds:0."""
        self.assertEqual(sum_evens_and_odds([]), {'Evens': 0, 'Odds': 0})

    def test_string(self):
        """It should raise an assertion error if the list contains non-integers/floats."""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds(["6", 3, "5", 2])

    def test_none(self):
        """It should raise an assertion error if the list contains None."""
        with self.assertRaises(AssertionError):
            sum_evens_and_odds([None])


if __name__ == "__main__":
    unittest.main()
