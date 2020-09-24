'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 11
Part 2: Password Checker
date April 14 2017
'''
import math
import random 

def main():
    psswd = input("Enter password to verify: ")
    if psswd_has_min_length(psswd) == True and psswd_has_only_letters_and_numbers(psswd) == True and psswd_has_two_digits(psswd) == True:
        print("Password is valid.")
    else:
        print("Password is invalid.")

# This function returns True if the password has at least
# 8 characters; the function returns False otherwise
def psswd_has_min_length(psswd):
    if len(psswd) >= 8:
        return True
    else:
        return False
    


# This function returns True if the password is alphanumeric
# the function returns False otherwise
def psswd_has_only_letters_and_numbers(psswd):
    if psswd.isalnum():
        return True
    else:
        return False
    


# This function counts the number of digits in the password
# and returns True if it finds at least two; the function
# returns False otherwise
def psswd_has_two_digits(psswd):
    
    count_digits = 0
    for character in psswd:
        if character.isdigit() == True:
            count_digits += 1
    if count_digits >= 2:
        return True
    else:
        return False

main() # run the program