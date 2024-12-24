"""
This module contains unit tests to validate the functionality of the mystery_5 function. 
The tests ensure the function behaves as expected across a range of inputs.

Test categories:
- Standard cases: Typical lists with integers and floats to validate correct sorting.
- Edge cases: Lists with negative numbers, single elements, two elements, and already sorted lists.
- Defensive tests: Handling of empty lists, invalid input types, and non-numeric elements.

Created on: 2024-12-18
Author: Jola-Moses
"""


import unittest

from ..mystery_5 import mystery_5

class TestMystery5(unittest.TestCase):
    """Tests for mystery_5 function"""

    def test_unordered(self):
        """It should sort the list in ascending order."""    
        self.assertEqual(mystery_5([7, 2, 3 ,4, 5, 6]), [2, 3, 4, 5, 6, 7])

    def test_ordered_list(self):
        """It should return an ordered list unchanged."""    
        self.assertEqual(mystery_5([7, 8, 9]), [7, 8, 9])

    def test_repeated_numbers(self):
        """It should handle repeated numbers and sort them in ascending order"""   
        self.assertEqual(mystery_5([5, 5, 4, 2, 2, 3, 1, 1]), [1, 1, 2, 2, 3, 4, 5, 5])

    def test_range(self):
        """It should handle a range of numbers and sort them in ascending order."""    
        self.assertEqual(mystery_5([200, 30 ,40000, 1, 100, 1000]), [1, 30, 100, 200, 1000, 40000])

    def test_single_element(self):
        """It should return a single element list unchanged."""    
        self.assertEqual(mystery_5([7]), [7])

    def test_two_elements(self):
        """It should sort a list of two in ascending order."""    
        self.assertEqual(mystery_5([7, 2]), [2, 7])

    def test_same_number(self):
        """It should return the list unchanged if all elements are the same."""  
        self.assertEqual(mystery_5([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])

    def test_negative(self):
        """It should sort negative numbers in ascending order."""    
        self.assertEqual(mystery_5([-3, -1, -2, -4]), [-4, -3, -2, -1])

    def test_negative_positive(self):
        """It should sort negative and positive numbers in ascending order"""    
        self.assertEqual(mystery_5([-3, 3, 0, 1, -1 -2, 4, -4]), [-4, -3, -3, 0, 1, 3, 4])

    def test_floats(self):
        """It should sort floats in ascending order."""    
        self.assertEqual(mystery_5([7.2, 2.9, 3.78, 6.9]), [2.9, 3.78, 6.9, 7.2])

    def test_mixed(self):
        """It should handle floats and integers and sort them in ascending order."""    
        self.assertEqual(mystery_5([7.9, 7, 6.1, 6, 5.01, 5]), [5, 5.01, 6, 6.1, 7, 7.9])

    def test_empty(self):
        """It should return an empty list if list is empty."""    
        self.assertEqual(mystery_5([]), [])

    def test_invalid_string(self):
        """It should raise an assertion error if list element is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_5(["6", 3, "5", 2])

    def test_invalid_none(self):
        """It should raise an assertion error if not list"""
        with self.assertRaises(AssertionError):
            mystery_5("3, 4, 5")

    if __name__ == "__main__":
        unittest.main()
