
"""
A module for checking if an item exists in two lists.

Module Contents:

    - is_in_both(item: str, b: list, d: list) -> bool: 
    Checks whether a specified item is present in both lists.

Created on: 2024-12-18
Author: Jola-Moses
"""

def is_in_both(item: str, b: list, d: list) -> bool:


    """
    Checks if item is present in two lists. 
    Returns True if present and False otherwise.

    Parameters:
        item: str, item to check
        b: list, first list to check
        d: list, second list to check

    Returns -> bool, True if item in both lists, otherwise False

    Raises:
        AssertionError: if item is not a string
        AssertionError: if b and d are not lists

    >>> b = ["yellow", "orange", "silver", "pink", "indigo"]
    >>> d = ["white", "silver", "indigo", "purple", "pink"]
    
    >>> is_in_both("pink", b, d)
    True
    
    >>> is_in_both("silver", b, d)
    True
    
    >>> is_in_both("indigo", b, d)
    True

    """
    assert isinstance(item, str), "item is not a string"
    assert isinstance(b, list), "b is not a list"
    assert isinstance(d, list), "d is not a list"

    # return True if iem is in both b and d, else False
    if item in b and item in d:
        return True
    return False
