#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Cat Detector: while

This program continually prompts until it gets a cat.

"""

user_text = ""  # initialise user_text with empty string


while user_text.lower() != "cat":  # loop until the user enters "cat" (case-insensitive)
    
    # prompt the user for input and store it in user_text
    user_text = input("Please enter a cat: ")  

    # check if user entered nothing
    if user_text == "":
        print("You entered nothing, try again.") # prompt user to try again

    
    # check if user input is neither empty nor cat
    elif user_text.lower() != "cat":
        print('"' + user_text + '" is not  a cat, try again.') # prompt user to try again


# print thank-you message once user enters correct input
print("thank you for the cat")
