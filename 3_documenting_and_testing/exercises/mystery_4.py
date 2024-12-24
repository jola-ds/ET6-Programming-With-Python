"""
A module for generating a sequence of consecutive integers.

Module Contents:

    def mystery_4(a: int) -> list:

Created on 2024-12-16

@author: Jola-Moses
"""

def mystery_4(a: int) -> list:
    """
    Returns a list of consecutive integers starting from 0 to a-1.

    Parameters:
        a: int, the count of integers in the returned list       

    Returns -> list, a list of consecutive numbers starting from 0 to a-1.

    Raises:
        AssertionError: if a is not a int
        
    >>> mystery_4(1)
    [0]
    
    >>> mystery_4(5)
    [0,1,2,3,4]
    
    >>> mystery_4(10)
    [0,1,2,3,4,5,6,7,8,9]
    """

    assert isinstance (a, int), "a should be an integer or float"
    b = []

    c = 0
    while len(b) < a:
        b.append(c)
        c = c + 1

    return b
