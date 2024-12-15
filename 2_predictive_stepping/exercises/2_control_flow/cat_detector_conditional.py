#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Cat Detector: conditional

This program asks the user for "cat", 
then responds differently if they did provide a cat or not.

"""
# prompt user to enter 'cat'
user_text = input('Please enter "cat": ') # store user input in variable user_input

if user_text == "": # check if user entered nothing
    response = "You entered nothing"  # store 'you entered nothing' in response

elif user_text == "cat": # check if user entered 'cat'
    response = "Thank you for the cat"  # store 'thank you for the cat' in response

else:        # check any input that is neither empty nor 'cat'
    response = '"' + user_text + '" is not "cat"'  # store 'user input' is not 'cat' in response

# print response determined by condtion in console
print(response)
