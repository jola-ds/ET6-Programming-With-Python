#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Variables: Cat Detector

Asks the use for the input "cat", throws an assertion error if the input is wrong

"""
# prompt user to enter 'cat' in console
maybe_cat = input('Enter "cat": ') # store user input 'cat' in varible maybe_cat
is_cat = maybe_cat == "cat" # store 'cat' in variable is_cat

# confirm is_cat is 'cat'
assert is_cat, 'you should have entered "cat"'  # raise error if not 'cat'

print("thank you for the cat") # print 'thank you for coming' in console
