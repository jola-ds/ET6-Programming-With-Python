"""
A module for sorting a list of numbers in ascending order.

Module Contents:

    - mystery_5(a: list, b=None) -> list:
    Sorts numbers in a list from lowest to highest.

Created on: 2024-12-19
Author: Jola-Moses

"""

def mystery_5(a: list, b=None):

    """
    Returns a list of numbers sorted in ascending order.

    Parameters:
        a: list, an unordered list of numbers to be sorted.
        b: None, a list to which sorted numbers from `a` will be appended. 
        

    Returns -> list, a list of numbers sorted from lowest to highest.

    Raises:
        AssertionError: if a is not a list
        AssertionError: if elements in a are not integers or floats

    >>> mystery_5([7, 2, 3, 6])
    [2, 3, 6, 7]
    
    >>> mystery_5([5, 5, 2, 2])
    [2, 2, 5, 5]
    
    >>> mystery_5([2, 1, 2])
    [1, 2, 2]
    
    """

    assert isinstance(a,list), "a should be a list"
    assert all(isinstance(x, (int, float)) for x in a), "elements in a should be integers or floats"
    if b is None:
        b = []
    while a:
        c = min(a)
        a.remove(c)
        b.append(c)

    return b
