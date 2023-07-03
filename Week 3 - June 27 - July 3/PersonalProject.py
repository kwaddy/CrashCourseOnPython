# Title: Binary Computation
# Written by Kayla Waddy
# June 28th, 2023
# Description: This personal project will explore how to write
# a program in python to convert a binary input from the user
# to a decimal number (i.e. from 10111000 to the decimal
# equivalent). This wil explore the connection between two
# different classes I am taking and how one's teachings
# can be cross translated. Will update this as need be.

# Intializing a matrix so my fill matrix function works
# and stores the different parts of the user input within
binary_number_matrix = []

# A function that checks to make sure that the user input is
# the proper length
def checking_input(x): 
    # Importing regular expression operations to iterate
    # through the string to check and make sure all the
    # characters the user inputed equals a specific
    # pattern of characters
    import re
    pattern = r'[^\.0-1]'
    str_binary = str(x) # Converts the input into a string
    # Checks the length of the string and then determines weather
    # a null number will print out or the length of the string.
    # This was done to make sure that the program is working properly
    # BEFORE further implementation.
    
    # Iterates through the str_binary to see if any of the characters
    # doesn't match the pattern that was stated before
    if (len(str_binary) != 8) or (re.search(pattern, str_binary)): 
        return 0
    return len(str_binary)

# The function to store the length of the binary
# length_of_binary = checking_input(x)

# A function that splits the user input into different
# cells for the computer to run through. Calls length
# of binary so that the program has something to iterate
# through
def fill_matrix(length_of_binary):
    x = 0

#print(checking_input())# Used to check whether the function was working properly