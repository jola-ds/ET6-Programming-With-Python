#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" While Loops

While loops execute the same block of code as long as a condition is not met

"""

maybe_a_cat = ""

# stops running after user inputs "cat"
while maybe_a_cat.lower() != "cat":
    maybe_a_cat = input('Enter "cat": ')
# maybe_a_cat = cat

print("Thank you for the cat.")
