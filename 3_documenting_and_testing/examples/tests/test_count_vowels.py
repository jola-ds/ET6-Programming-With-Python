import unittest

from ..count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    """Test the count_vowels function - some tests are buggy!"""

    # TODO: as an exercise, write more tests!
    
    def test_empty_string(self):
        """It should return 0 for an empty string"""
        self.assertEqual(count_vowels(""), 0)
        
    def test_no_vowels(self):
        """It should return 0 for strings without vowels"""
        self.assertEqual(count_vowels("cry"), 0)
        
    def test_all_vowels(self):
        """It should count all vowels in a string"""
<<<<<<< HEAD:4_debugging/exercises/1_buggy_tests/tests/test_count_vowels.py
        self.assertEqual(count_vowels("AUDIO"), 4)
=======
        self.assertEqual(count_vowels("AUIO"), 4)
>>>>>>> origin/main:3_documenting_and_testing/examples/tests/test_count_vowels.py
        
    def test_mixed_case(self):
        """It should handle mixed case strings"""
        self.assertEqual(count_vowels("Hello World"), 3)
        
    def test_not_string(self):
        """It should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            count_vowels(123)
