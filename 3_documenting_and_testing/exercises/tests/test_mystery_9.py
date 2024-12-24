"""
This module contains unit tests to validate the functionality of the mystery_9 function. 


Test categories:
- Standard cases: Typical lists with integers, floats, and mixed numbers.
- Edge cases: Lists with negative numbers, single elements, two elements, and already sorted lists.
- Defensive tests: Handling of empty lists, invalid input types, and non-numeric elements.

Created on: 2024-12-18
Author: Jola-Moses
"""


import unittest

from ..mystery_9 import mystery_9

class TestMystery9(unittest.TestCase):
    """Tests for mystery_9 function"""

    def test_unordered(self):
        """It should sort the list in ascending order."""    
        self.assertEqual(mystery_9([7, 2, 3 ,4, 5, 6]), [2, 3, 4, 5, 6, 7])

    def test_ordered_list(self):
        """It should return an ordered list unchanged."""    
        self.assertEqual(mystery_9([7, 8, 9]), [7, 8, 9])

    def test_repeated_numbers(self):
        """It should handle repeated numbers and sort them in ascending order"""   
        self.assertEqual(mystery_9([5, 5, 4, 2, 2, 3, 1, 1]), [1, 1, 2, 2, 3, 4, 5, 5])

    def test_range(self):
        """It should handle a range of numbers and sort them in ascending order."""    
        self.assertEqual(mystery_9([7, 200, 30 ,40000, 100, 1000]), [7, 30, 100, 200, 1000, 40000])

    def test_single_element(self):
        """It should return a single element list unchanged."""    
        self.assertEqual(mystery_9([7]), [7])

    def test_two_elements(self):
        """It should sort a list of two in ascending order."""    
        self.assertEqual(mystery_9([7, 2]), [2, 7])

    def test_same_number(self):
        """It should return the list unchanged if all elements are the same."""  
        self.assertEqual(mystery_9([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])

    def test_negative(self):
        """It should sort negative numbers in ascending order."""    
        self.assertEqual(mystery_9([-3, -1, -2, -4]), [-4, -3, -2, -1])

    def test_negative_positive(self):
        """It should sort negative and positive numbers in ascending order"""    
        self.assertEqual(mystery_9([-3, 3, 0, 1, -1 -2, 4, -4]), [-4, -3, -3, 0, 1, 3, 4])

    def test_floats(self):
        """It should sort floats in ascending order."""    
        self.assertEqual(mystery_9([7.2, 2.9, 3.78, 6.9]), [2.9, 3.78, 6.9, 7.2])

    def test_mixed(self):
        """It should handle floats and integers and sort them in ascending order."""    
        self.assertEqual(mystery_9([6.1, 6, 5.01, 5, 4.0, 4]), [4.0, 4, 5, 5.01, 6, 6.1])

    def test_empty(self):
        """It should return an empty list if list is empty."""    
        self.assertEqual(mystery_9([]), [])

    def test_invalid_string(self):
        """It should raise an assertion error if list element is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_9(["6", 3, "5", 2])

    def test_invalid_none(self):
        """It should raise an assertion error if not list"""
        with self.assertRaises(AssertionError):
            mystery_9("3, 4, 5")

    if __name__ == "__main__":
        unittest.main()
