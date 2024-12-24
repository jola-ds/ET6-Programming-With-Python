
"""
A module for checking the occurrence of a specified character.

Module contents:
    - mystery_7(a: Union[List, Tuple, Dict], b: str) -> List: 
        Checks for the occurrence of a specified character in an iterable.
        Returns a list of strings containing the character.

Created on 2024-12-18
Author: Jola-Moses
"""

from typing import Union, List, Tuple, Dict

def mystery_7(a: Union[List, Tuple, Dict], b: str) -> List:
    """
    Checks for the occurrence of a specified character in a list, tuple, or dictionary.
    Returns a list of strings containing the character.

    Parameters:
    - a (list, tuple, or dict): The iterable to check for the occurrence of a character.
    - b , str: The specified character to check.

    Returns:
    - list: A list of strings containing the character.
    
    Raises:
    - AssertionError: If `a` is not a list, tuple, or dict of strings.
    - AssertionError: If `b` is not a single character string.
    
    Examples:
    >>> mystery_7(["hello world"], "o")
    ["hello world"]
    
    >>> mystery_7(["Water", "Money", "cat"], "a")
    ["Water", "cat"]

    >>> mystery_7(["hello world this is python"], "i")
    ["hello world this is python"]
    """

    assert isinstance(a, (list, tuple, dict)), "a should be a list, tuple, or dictionary"
    assert all(isinstance(x, str) for x in a), "values in a should b strings"
    assert isinstance(b, str), "b should be a string"


    c = []

    for d in a:
        if b in d:
            c.append(d)
    return c
