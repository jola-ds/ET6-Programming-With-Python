"""
A module for basic addition mathematical operation

Module Contents:

    - sum_two_numbers: Adds two integers or floats

Created on 2024-12-08

@author: Jola-Moses

"""



def sum_two_numbers(a, b) -> int:
    """Adds two integers a and b

    Parameters:
        a: int, first integer
        b: int, second integer

    Returns -> int, sum of a and b

    Raises:
        AssertionError: if input is not an integer
        AssertionError: if both inputs are zero

    >>> sum_two_numbers(3,4)
    7

    >>> sum_two_numbers(1,2)
    3

    >>> sum_two_numbers(5,6)
    11
    """

    

    # both arguments must be integers or floats
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Argument is not an integer or float"
    assert not (a == 0 and b == 0), "Both arguments cannot be zero"

    return a + b
