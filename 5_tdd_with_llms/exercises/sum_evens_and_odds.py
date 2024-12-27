"""
A module for adding the sum of even and odd numbers to a dictionary.

Module Contents:

    - sum_evens_and_odds(a: list) -> dict:
    Returns sum of even and sum of odd numbers in a dictionary.

Created on: 2024-12-18
Author: Jola-Moses

"""


def sum_evens_and_odds(a: list) -> dict:

    """
    Checks if a number is even or odd.
    Returns a sum of even numbers and the sum of odd numbers in a dictionary

    Parameters:
        a: list, a list of numbers to check

    Returns -> dict, 
    A dictionary with keys 'Evens' for sum of even numbers and 'Odds' for sum of odd numbers.

    Raises:
        AssertionError: if a is not a list
        AssertionError: if elements in a are not integers or floats

    >>> sum_evens_and_odds([7, 2, 3, 6])
    {'Evens': 8, 'Odds': 10})
    
    >>> sum_evens_and_odds([5, 5, 2, 2])
    {'Evens': 4, 'Odds': 10}
    
    >>> sum_evens_and_odds([2, 1, 2])
    {'Evens': 1, 'Odds': 4}
    """


    assert isinstance(a, list), "a should be a list"
    assert all(isinstance(x, (int, float)) for x in a), "elements should be integers or floats"


    d = {"Evens": 0, "Odds": 0}
    # Iterate over each element in the input list `a`.
    for x in a:
    # Check if the current element `x` is even.
        if x % 2 == 0:
            d["Evens"] += x   # Add the even number to the "Evens" total.
        else:
            d["Odds"] += x    # Add the odd number to the "Odds" total.

    # Return the dictionary containing the sums of evens and odds.
    return d
