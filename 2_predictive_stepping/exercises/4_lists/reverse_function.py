#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Testing Functions with Lists

Assertion tests to understand the function's behavior.

"""

# --- declare function ---


def reverse_list(items: list) -> list:
    """Creates a reversed copy of a list"""
    backwards = []  # initialise backwards with empty list
    for item in items:  # iterate over every element in list
        backwards.insert(0, item)   # add each item to the beginning of backwards
    return backwards


# --- test function ---

_1_arg = ["x", "y", "z"]    # store ['x', 'y', 'z'] in _1_arg
_1_returned = reverse_list(_1_arg)      # store reversed _1_arg in _1_returned
assert _1_returned == ["z", "y", "x"], "Test 1" # confirm _1_returned is ['z', 'y', 'x']

_2_arg = [True, False]  # store bool values in _2_arg
_2_returned = reverse_list(_2_arg)  # store reversed _2_arg in _2_returned
assert _2_returned == [False, True], "Test 2" # confirm _2_returned is [False, True]

_3_arg = [1729]     # store [1729] in _3_arg
_3_returned = reverse_list(_3_arg)  # store reversed _3_arg in _3_returned
assert _3_returned == [1729], "Test 3"   # confirm _3_returned is [1729]

_4_arg = []     # store [] in _4_arg
_4_returned = reverse_list(_4_arg)  # store reversed _4_arg in _4_returned
assert _4_returned == [], "Test 4"  # confirm _4_returned is []
