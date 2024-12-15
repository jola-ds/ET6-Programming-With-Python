#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Contains Cat

This program continually prompts until their input contains "cat".

"""

user_text = ""  # initialise user_text with empty string

while "cat" not in user_text.lower(): # loop until the user enters input containing "cat" (case-insensitive)
    user_text = input('Please enter something containing "cat": ')

    
  # check if user entered nothing and prompt user to try again
    if user_text == "":
        print("You entered nothing, try again.")

    # check if user input does not contain cat and prompt to try agai
    elif "cat" not in user_text.lower():
        print('"' + user_text + '" does not contain cat, try again.')


# print message if user input contains cat
print("thank you for the cat")
