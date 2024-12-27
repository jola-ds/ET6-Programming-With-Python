
"""
A module for sorting a list of numbers in ascending order.

Module Contents:

    - sort_numbers(l: list) -> list:
    Sorts numbers in a list from lowest to highest.

Created on: 2024-12-19
Author: Jola-Moses

"""

def sort_numbers(lst: list) -> list:
    """
    Returns a list of numbers sorted in ascending order.

    Parameters:
        l: list, an unordered list of numbers to be sorted

    Returns -> list, a list of numbers sorted from lowest to highest.

    Raises:
        AssertionError: if l is not a list
        AssertionError: if elements in l are not integers or floats

    >>> sort_numbers([7, 2, 3, 6])
    [2, 3, 6, 7]
    
    >>> sort_numbers([5, 5, 2, 2])
    [2, 2, 5, 5]
    
    >>> sort_numbers([2, 1, 2])
    [1, 2, 2]
    
    """

    # Ensure a is a list
    assert isinstance(lst, list), "lst should be a list"
    # Ensure all elements in a are integers or floats
    assert all(isinstance(x, (int, float)) for x in lst), "Elements should be integers or floats"

    l_copy = lst[:]
    n = len(l_copy)
    for x in range(n):
        for j in range(0, n - x - 1):
            if l_copy[j] > l_copy[j + 1]:
                l_copy[j], l_copy[j + 1] = l_copy[j + 1], l_copy[j]

    return l_copy

print(sort_numbers([2, 1, 2]))
