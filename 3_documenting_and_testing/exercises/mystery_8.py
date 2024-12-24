
"""
A module for filtering an iterable to return elements containing a specified substring..

Module contents:
    - mystery_8(a, b): Checks for the occurrence of a specified substring in an iterable.
                        Returns a list of strings containing the substring.

Created on 2024-12-18
Author: Jola-Moses
"""

def mystery_8(a, b) -> list:
    """
    Filters an iterable to return elements containing a specified substring.
    
    Args:
        a (str, list, tuple): The iterable to search.
        b (str): The substring to search for within elements of `a`.
    
    Returns:
        list: A list of elements from `a` that contain the substring `b`.
    
    Raises:
        AssertionError: If `a` is not a string, list, or tuple.
        AssertionError: If `b` is not a string.
        
        
    >>> mystery_8(["apple", "banana", "cherry"], "a")
    ["apple", "banana"]
    
    >>> mystery_8(("hello", "world", "python"), "o")
    ["hello", "world", "python"]
    
    >>> mystery_8("python", "o")
    ["o"]
    
    """
    # Defensive checks
    assert isinstance(a, (str, list, tuple)), "a must be a string, list, or tuple"
    assert isinstance(b, str), "b must be a string"

    c = []
    while a:
        if b in a[0]:
            c.append(a[0])
        a = a[1:]
    return c
