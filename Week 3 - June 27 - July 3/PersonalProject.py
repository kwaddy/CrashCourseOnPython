# Title: Binary Computation
# Written by Kayla Waddy
# June 28th, 2023
# Description: This personal project will explore how to write
# a program in python to convert a binary input from the user
# to a decimal number (i.e. from 10111000 to the decimal
# equivalent). This wil explore the connection between two
# different classes I am taking and how one's teachings
# can be cross translated. Will update this as need be.

# Defining how a function will read the user input
# Specificially the input has to be done in ones and zeros
def reading_input(x): 
    str_binary = str(x) # Converts the input into a string
    # Checks the length of the string and then determines weather
    # a null number will print out or the length of the string.
    # This was done to make sure that the program is working properly
    # BEFORE further implementation
    if (len(str_binary) < 8): 
        return 0
    return len(str_binary)
print(reading_input())