
"""
A module for checking if an item exists in at least one list.

Module Contents:

    - is_in_both(item: str, b: list, d: list) -> bool: 
    Checks whether a specified item is present in at least one list.

Created on: 2024-12-18
Author: Jola-Moses
"""

def is_in(item: str, b: list, d: list) -> bool:

    """
    Checks if an item is present in at least one list. 
    Returns True if item is in at least one list, otherwise False.

    Parameters:
        item: str, item to check
        b: list, first list to check
        d: list, second list to check

    Returns -> bool, True if item in at least one list, False if in neither.

    Raises:
        AssertionError: if item is not a string
        AssertionError: if b and d are not lists

    >>> b = ["yellow", "orange", "pink"]
    >>> d = ["white", "indigo", "purple"]
    
    >>> is_in("pink", b, d)
    True
    
    >>> is_in("orange", b, d)
    True
    
    >>> is_in("purple", b, d)
    True

    """

    # assert 'item' is a string
    assert isinstance(item, str), "item should be a string"
    #assert 'b' is a list
    assert isinstance(b, list), "b should be a list"
    # assert 'd' is a list
    assert isinstance(d, list), "d should be a list"

    # return true if item is in either b or d, else false
    if item in b or item in d:
        return True
    return False
