"""
This module contains unit tests for the `repeat_character` function.
It validates the functionality of repeating characters in a string based on specified conditions.

Test categories:
    - Standard cases: Typical strings and character repetitions.
    - Edge cases: Single characters, special characters, and empty strings.
    - Defensive tests: Invalid inputs such as non-string characters and integers.

Created on: 2024-12-18
Author: Jola-Moses
"""

import unittest

from ..repeat_character import repeat_character

class TestRepeatCharacter(unittest.TestCase):
    """Test cases for the repeat_character function"""

    def test_mystique(self):
        """Should repeat 'i' four times and return 'Mystiiiique'."""
        self.assertEqual(repeat_character("Mystique", "i", 4), "Mystiiiique")

    def test_storm(self):
        """Should repeat 'o' five times and return 'Stooooorm'."""
        self.assertEqual(repeat_character("Storm", "o", 5), "Stooooorm")

    def test_case_logan(self):
        """Should repeat 'l' once and return 'logan'."""
        self.assertEqual(repeat_character("logan", "l", 1), "logan")

    def test_case_insensitive_lower(self):
        """Should repeat 'd' twice at every occurrence."""
        self.assertEqual(repeat_character("Deadpool", "d", 3), "DDDeadddpool")

    def test_case_insensitive_upper(self):
        """Should repeat 'c' twice at every occurrence."""
        self.assertEqual(repeat_character("Cyclops", "C", 2), "CCycclops")

    def test_duplicates(self):
        """Should repeat 's' thrice at every occurrence."""
        self.assertEqual(repeat_character("Scott Summers", "s", 3), "SSScott SSSummersss")

    def test_same_multiple_character(self):
        """Should repeat 's' five times and return 'Professssssor X'."""
        self.assertEqual(repeat_character("Professor X", "s", 3), "Professssssor X")

    def test_single_character(self):
        """Should handle single-character text and return 'z' five times."""
        self.assertEqual(repeat_character("Z", "z", 5), "ZZZZZ")

    def test_same_1_character(self):
        """Should repeat '8' two times at every occurrence."""
        self.assertEqual(repeat_character("88888", "8", 2), "8888888888")

    def test_same_2_character(self):
        """Should repeat '8' five times at every occurrence."""
        self.assertEqual(repeat_character("88", "8", 5), "8888888888")

    def test_special_character(self):
        """Should handle special characters and repeat '!' three times."""
        self.assertEqual(repeat_character("Jubilee!", "!", 3), "Jubilee!!!")

    def test_single_special_character(self):
        """Should handle special characters and repeat '$' five times."""
        self.assertEqual(repeat_character("$", "$", 5), "$$$$$")

    def test_negative_one(self):
        """Should remove every occurrence of specified character when n is negative."""
        self.assertEqual(repeat_character("Wolverine", "e", -1), "Wolvrin")

    def test_negative_five(self):
        """Should remove every occurrence of specified character when n is negative."""
        self.assertEqual(repeat_character("Scott", "t", -5), "Sco")

    def test_char_not_found(self):
        """Should return the text unchanged if the specified character is not found."""
        self.assertEqual(repeat_character("Shadowcat", "z", 5), "Shadowcat")

    def test_zero(self):
        """Should remove every occurrence of the specified character when n is zero."""
        self.assertEqual(repeat_character("Magneto", "o", 0), "Magnet")

    def test_zero_(self):
        """Should remove every occurrence of the specified character when n is zero."""
        self.assertEqual(repeat_character("The Xmen", "e", 0), "Th Xmn")

    def test_space(self):
        """Should handle and repeat spaces."""
        self.assertEqual(repeat_character("Jean Grey", " ", 3), "Jean   Grey")

    def test_empty_string_text(self):
        """Should return an empty string when the input text is empty."""
        self.assertEqual(repeat_character("", "w", 5), "")

    def test_non_string_character(self):
        """Should raise an AssertionError if the specified character is not a string."""
        with self.assertRaises(AssertionError):
            repeat_character("12345", 3, 2)

    def test_non_string_text(self):
        """Should raise an AssertionError if the input text is not a string."""
        with self.assertRaises(AssertionError):
            repeat_character(12345, "3", 2)

    def test_non_integer(self):
        """Should raise an AssertionError if n is not an integer."""
        with self.assertRaises(AssertionError):
            repeat_character("Peacemaker", "e", "2")

    def test_multiple_string_character(self):
        """Should raise an AssertionError if the specified character is not a single character."""
        with self.assertRaises(AssertionError):
            repeat_character("Bishop", "hop", 3)

    def test_empty_string(self):
        """Should raise an AssertionError if the specified character is an empty string."""
        with self.assertRaises(AssertionError):
            repeat_character("Rogue", "", 5)


if __name__ == "__main__":
    unittest.main()
