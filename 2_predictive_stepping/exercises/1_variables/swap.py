#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Swapping Values

Fill in the blanks to pass the assertions.

"""



a = 2  # Assign 2 to variable 'a'
b = 1  # Assign 1 to variable 'b'

# Check initial values
assert a == 2, "a's initial value"  # Confirm 'a' is 2
assert b == 1, "b's initial value"  # Confirm 'b' is 1

temp = a  # Store the value of 'a' (2) in variable 'temp'
assert temp == 2, "temp's final value"  # Confirm 'temp' is 2

a = b  # Assign the value of 'b' (1) to 'a'
assert a == 1, "a's final value"  # Confirm 'a' is now 1

b = temp  # Assign the value of 'temp' (2) to 'b'
assert b == 2, "b's final value"  # Confirm 'b' is now 2
