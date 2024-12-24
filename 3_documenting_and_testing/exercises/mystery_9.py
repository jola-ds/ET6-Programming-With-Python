
"""
A module for sorting a list of numbers in ascending order.

Module Contents:

    - mystery_9(a) -> list:
    Sorts numbers in a list from lowest to highest.

Created on: 2024-12-18
Author: Jola-Moses

"""

def mystery_9(a) -> list:

    """
    Returns a list of numbers sorted in ascending order.

    Parameters:
        a: list, an unordered list of numbers to be sorted

    Returns -> list, a list of numbers sorted from lowest to highest.

    Raises:
        AssertionError: if a is not a list
        AssertionError: if elements in a are not integers or floats

    >>> [7, 2, 3, 6]
    [2, 3, 6, 7]
    
    >>> [5, 5, 2, 2]
    [2, 2, 5, 5]
    
    >>> [2, 1, 2]
    [1, 2, 2]
    
    """

    # Ensure a is a list or tuple
    assert isinstance(a, list),"a should be a list"
    # Ensure all elements in a are integers or floats
    assert all(isinstance(x, (int, float)) for x in a), "elements in a should be integers or floats"

    b = len(a)
    for c in range(b):
        for d in range(0, b - c - 1):
            if a[d] > a[d + 1]:
                a[d], a[d + 1] = a[d + 1], a[d]
    return a
