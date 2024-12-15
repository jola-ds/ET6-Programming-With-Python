#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Reverse Program: String

A program that uses the function to reverse a user's input.

"""

# --- declare the helper function ---


def reverse_string(text: str) -> str:
    """Creates a reversed copy of a string"""
    backwards = ""  # initialise backwards with empty string to store reversed text
    for char in text:   # iterate over every character in text
        backwards = char + backwards  # add each character to the front of backwards
    return backwards


# --- use the helper function in a program ---

print("This program prints your input in reverse.\n")

user_text = ""  # store '' in user_text
while user_text == "":  # prompt until user enters text
    user_text = input("\nEnter some something to reverse: ")    # store user input in user_text
    if user_text == "": # check if user entered nothing and prompt user to enter text
        print("Nope, gotta enter something.  Try again.")  

reversed_text = reverse_string(user_text)   # store reversed text in reversed_text

print(user_text, " -> ", reversed_text)
