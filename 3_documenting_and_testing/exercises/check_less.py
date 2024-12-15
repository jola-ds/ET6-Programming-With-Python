"""
A module for checking if an integer is less than another, eor the sum of two integers.

Module Contents:

    - check_greater_less: Compares two integers and returns the smaller or their sum if equal.

Created on 2024-12-10

@author: Jola-Moses
"""

def check_less(a: int, b: int) -> int:
    """Checks if an integer a is less than integer b, otherwise finds the sum of a and b if equal.

    Parameters:
        a: int, first integer to check
        b: int, second integer to check

    Returns -> int, the smaller or sum of the two integers

    Raises:
        AssertionError: if the argument is not an integer
        AssertionError: if both arguments are zero


    >>> check_less(28, 300)
    28
    >>> check_less(0, 5)
    0
    >>> check_less(6, 6)
    12
    """
    # Both arguments must be integers
    assert isinstance(a, int) and isinstance(b, int), "Argument is not an integer"
    assert not (a == 0 and b == 0), "Both arguments cannot be zero"

    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a + b
