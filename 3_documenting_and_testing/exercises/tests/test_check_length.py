"""
A module for checking the length of an input 

Module Contents:

    - check_length: checks the length of an iterable input

"""

import unittest

from ..check_length import check_length

class TestCheckLength(unittest.TestCase):

    def test_list(self):
        """It should evaluate check_length([0, 1]) to 2."""
        self.assertEqual(check_length([0, 1]), 2)

    def test_empty_list(self):
        """It should evaluate check_length([]) to None."""
        self.assertEqual(check_length([]), None)

    def test_nested_list(self):
        """It should evaluate check_length([[1, 2], [3, 4]]) to 2."""
        self.assertEqual(check_length([[1, 2], [3, 4]]), 2)

    def test_string(self):
        """It should evaluate check_length(("Damaged")) to 7."""
        self.assertEqual(check_length(("Damaged")), 7)

    def test_white_space_string(self):
        """It should evaluate check_length(("   ")) to 3."""
        self.assertEqual(check_length(("   ")), 3)

    def test_empty_string(self):
        """It should evaluate check_length(("")) to None."""
        self.assertEqual(check_length(("")), None)

    def test_tuple(self):
        """It should evaluate check_length(("water", 45, 600)) to 3."""
        self.assertEqual(check_length(("water", 45, 600)), 3)

    def test_nested_tuple(self):
        """It should evaluate check_length(("do", 45), (be, 600)) to 2."""
        self.assertEqual(check_length((("do", 45), ("be", 600))), 2)

    def test_empty_tuple(self):
        """It should evaluate check_length(()) to None."""
        self.assertEqual(check_length(()), None)

    def test_not_iterable_input(self):
        """It should raise an assertion error if the argument is not an iterable input"""
        with self.assertRaises(AssertionError):
            check_length(30)


if __name__ == "__main__":
   unittest.main()