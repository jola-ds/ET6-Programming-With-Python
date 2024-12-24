"""
A module for checking the length of an input 

Module Contents:

    - check_length: checks the length of an iterable input

Created on 2024-12-08

@author: Jola-Moses

"""


def check_length(a) -> int:

    """
    Checks the length of the input iterable and returns None if the input is empty.
    
    Parameters:
        a: str, list, tuple
        
    Returns -> int, the length of the input
            -> None, for an empty input
    
    Raises:
        AssertionError: if input is not a string, list or tuple
        

    >>> check_length(()) is None
    True
    >>> check_length(("")) is None
    True
    >>> check_length([]) is None
    True
    >>> check_length(("wow"))
    3
    >>> check_length((1,2,3,4,5))
    5
    """
    # a should be an iterable input
    assert isinstance (a, (str, list, tuple)), "a is not a string, list or tuple"
    if len(a) == 0:
        return None

    return len(a)

print(check_length([0, 1]))
print(check_length([[1, 2], [3, 4]]))
print(check_length([]))
