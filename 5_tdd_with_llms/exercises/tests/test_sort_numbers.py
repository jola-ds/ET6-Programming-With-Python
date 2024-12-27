"""
This module contains unit tests to validate the functionality of the `sort_numbers` function. 
The tests ensure the function behaves as expected across a range of inputs.

Test categories:
    - Standard cases: Typical lists with integers, floats, and mixed numbers.
    - Edge cases: Negative numbers, single elements, two elements, and already sorted lists.
    - Defensive tests: Handling of empty lists, invalid input types, and non-numeric elements.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..sort_numbers import sort_numbers

class TestSortNumbers(unittest.TestCase):
    """Test cases for the sort_numbers function"""

def test_unordered(self):
    """Should return the list sorted in ascending order."""    
    self.assertEqual(sort_numbers([7, 2, 3, 4, 5, 6]), [2, 3, 4, 5, 6, 7])

def test_ordered_list(self):
    """Should return the ordered list unchanged."""    
    self.assertEqual(sort_numbers([7, 8, 9]), [7, 8, 9])

def test_repeated_numbers(self):
    """Should handle repeated numbers and return them sorted."""   
    self.assertEqual(sort_numbers([5, 5, 4, 2, 2, 3, 1, 1]), [1, 1, 2, 2, 3, 4, 5, 5])

def test_range(self):
    """Should sort a range of numbers in ascending order."""    
    self.assertEqual(sort_numbers([7, 200, 30, 40000, 100, 1000]), [7, 30, 100, 200, 1000, 40000])

def test_single_element(self):
    """Should return a single element list unchanged."""    
    self.assertEqual(sort_numbers([7]), [7])

def test_two_elements(self):
    """Should sort a list of two elements in ascending order."""    
    self.assertEqual(sort_numbers([7, 2]), [2, 7])

def test_same_number(self):
    """Should return the list unchanged if all elements are the same."""  
    self.assertEqual(sort_numbers([7, 7, 7, 7, 7]), [7, 7, 7, 7, 7])

def test_negative(self):
    """Should sort negative numbers in ascending order."""    
    self.assertEqual(sort_numbers([-3, -1, -2, -4]), [-4, -3, -2, -1])

def test_negative_positive(self):
    """Should sort a mix of negative and positive numbers in ascending order."""    
    self.assertEqual(sort_numbers([-3, 3, 0, 1, -1, -2, 4, -4]), [-4, -3, -2, -1, 0, 1, 3, 4])

def test_floats(self):
    """Should sort float numbers in ascending order."""    
    self.assertEqual(sort_numbers([7.2, 2.9, 3.78, 6.9]), [2.9, 3.78, 6.9, 7.2])

def test_mixed(self):
    """Should handle both integers and floats, sorting them together in ascending order."""    
    self.assertEqual(sort_numbers([7.9, 7, 6.1, 6, 5.01, 5]), [5, 5.01, 6, 6.1, 7, 7.9])

def test_empty(self):
    """Should return an empty list if the input list is empty."""    
    self.assertEqual(sort_numbers([]), [])

def test_invalid_string(self):
    """Should raise an assertion error if the list contains non-numeric strings."""  
    with self.assertRaises(AssertionError):
        sort_numbers(["6", 3, "5", 2])

def test_invalid_none(self):
    """Should raise an assertion error if the input is not a list."""   
    with self.assertRaises(AssertionError):
        sort_numbers("3, 4, 5")

if __name__ == "__main__":
    unittest.main()
