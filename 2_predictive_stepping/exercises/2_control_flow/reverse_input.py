#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Reverse Input

This program reverses the user's input.

"""

user_text = ""  # initialise user_text with empty string

while user_text == "":  # prompt until user enters input
    user_text = input("Enter some text to reverse: ")  # prompt user to enter a text
    
    
    if user_text == "": # check if user entered nothing, prompt to try again
        print("nope, you have to enter something")

backwards = ""  # initialise backwards to store reversed text

for character in user_text:  # iterate over each character in user_text
    backwards = character + backwards  # add every  character to backwards at index 0

print("here is your reversed input: " + backwards)  # print reversed text
