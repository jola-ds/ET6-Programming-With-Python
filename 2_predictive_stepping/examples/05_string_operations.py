#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" String Operations

Python has features to help with lots of common string manipulations.
None of these operations modify the string they use as input!

"""

text = "Python"

# slicing single characters

sliced = text[0]    # sliced = P    
sliced = text[5]     # Sliced = n

# slicing substrings

sliced = text[0:5]  # sliced = Pytho
sliced = text[0:4]   # sliced = Pyth
sliced = text[0:3]     # sliced = Pyt
sliced = text[1:4]      # sliced = yth
sliced = text[2:4]       # sliced = th


# getting the length of a string

length = len(text)  # length = 6


# replacing substrings

replaced = text.replace("P", "Z")   # replaced = Zython

replaced = text.replace("p", "z")    # replaced is "Python" (case sensitivity)

replaced = text.replace("on", "agoras")   # replaced = Pythagoras


# setting strings to lower or opper case

upper = text.upper()    # upper = PYTHON

lower = text.lower()    # lower = python


# remove whitespace from the ends of a string

stripped = "  Python  ".strip()  # stripped = "Python"

print("end of script")
