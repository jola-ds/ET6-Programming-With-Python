
"""
A module for checking if an item exists in only one list.

Module Contents:

    - is_in_both(item: str, b: list, d: list) -> bool: 
    Checks whether an item is present in only one list.

Created on: 2024-12-18
Author: Jola-Moses
"""

def is_in_one(item: str, b: list, d: list) -> bool:

    """
    Checks if an item is present in one list. 
    Returns True if item is in only one list, False otherwise.

    Parameters:
        item: str, item to check
        b: list, first list to check
        d: list, second list to check

    Returns -> bool, True if item is in only one list, False otherwise

    Raises:
        AssertionError: if item is not a string
        AssertionError: if b and d are not lists

    >>> b = ["yellow", "orange", "pink"]
    >>> d = ["white", "indigo", "purple"]
    
    >>> is_in_one("pink", b, d)
    True
    
    >>> is_in_one("orange", b, d)
    True
    
    >>> is_in_one("purple", b, d)
    True

    """

    # assert 'item' is a string
    assert isinstance(item, str), "item should be a string"
    # assert 'b' is a list
    assert isinstance(b, list), "b should be a list"
    # assert 'd' is a list
    assert isinstance(d, list), "d should be a list"

    # return True if item is in exactly one of b or d (but not both)
    return (item in b) ^ (item in d)
