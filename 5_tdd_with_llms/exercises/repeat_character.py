
"""
A module for repeating a specified character n times in a string.

Module Contents:

    - repeat_character(text:str, x: str, n: int) -> str:
    Repeats each occurrence of a character n times.

Created on: 2024-12-18
Author: Jola-Moses

"""

def repeat_character(text:str, x: str, n: int) -> str:
    """
        Returns a string with each occurrence of the character repeated n times.

        Parameters:
            text: str, a string with the character to repeat.
            x: str, the character to repeat. 
            n, int, the number of times to repeat the character 'x'
            

        Returns -> str, a str with each occurrence of the specified character repeated n times.


        Raises:
            AssertionError: if text is not a string
            AssertionError: if x is not a string
            AssertionError: if n is not an integer
            AssertionError: if x is not a single character

        >>> repeat_character("Mystique", "i", 4)
        "Mystiiiique"
        
        >>> repeat_character("Storm", "o", 5)
        "Stooooorm"
        
        >>> repeat_character("logan", "l", 1)
        "logan"
        
        """

    # Assert 'text' is a string
    assert isinstance(text, str), "text is not a string"
    # Assert 'x' is a string
    assert isinstance(x, str), "x is not a string"
    # Assert 'n' is an integer
    assert isinstance(n, int), "n is not an integer"
    # Assert 'x' is a single character
    assert len(x) == 1, "x must be a single character"

    char_repeated = ""

    # loop through each character in 'text'
    for char in text:
        # Repeat 'x' 'n' times, otherwise add the character as is
        if char.lower() == x.lower(): # Convert character to lowercase
            char_repeated += char * n
        else:
            char_repeated += char
    return char_repeated
