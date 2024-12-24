"""
A module for generating a list of consecutive integers

Module Contents:

    - mystery_6(a:int, b:int) -> list:

Created on 2024-12-19

@author: Jola-Moses
"""

def mystery_6(a:int, b:int) -> list:

    """
    Returns a list of 'a' consecutive integers, starting from the specified `start` value.

    Parameters:
    - a, int: The number of consecutive integers to generate. 
    - b, int: The starting value of the sequence.

    Returns:
    - list: A list of 'a' consecutive integers, beginning from `b`.
    
    Raises:
    - AssertionError if count 'a' is not an integer.
    - AssertionError if start 'b' is not an integer.
    
    
    >>> mystery_6(3, 2)
    [2, 3, 4]
    
    >>> mystery_6(2, 1)
    [1, 2])
    
    >>> mystery_6(1, 1)
    [1])
    """

    assert isinstance(a, int), "the argument should be an integer"
    assert isinstance(b, (int, float)), "the argument should be an integer"

    if a == 0:
        return []

    c = []
    while len(c) < a:
        c.append(b)
        b = b + 1

    return c
