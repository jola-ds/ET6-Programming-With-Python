#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Testing Functions with Strings

Assertion tests to understand the function's behavior.

"""

# --- declare function ---


def reverse_string(text: str) -> str:
    """Creates a reversed copy of a string"""
    backwards = ""  # initialise backwards with empty string to store reversed text
    for char in text:   # iterate over every character in text
        backwards = char + backwards    # add every character to the front of backwards
    return backwards


# --- test function ---
# store 'xyz' in _1_arg
_1_arg = "xyz"
_1_returned = reverse_string(_1_arg)    # store 'zyx' in _1_returned
assert _1_returned == "zyx", "Test 1"   # confrim _1_returned is zyx

_2_arg = "Malayalam" # store 'Malaylam' in _2_arg
_2_returned = reverse_string(_2_arg)    # store 'malayalaM' in _2_returned
assert _2_returned == "malayalaM", "Test 2" # confirm _2_returned is 'malayalaM' 

_3_arg = "1729"     # store '1729' in _3_arg
_3_returned = reverse_string(_3_arg)    # store 9271 in _3_returned
assert _3_returned == "9271", "Test 3"  # confirm  _3_returned is 9271 

_4_arg = "" # store "" in _4_arg
_4_returned = reverse_string(_4_arg)    # store '' in new var
assert _4_returned == "", "Test 4"  # confirm new var is ''
