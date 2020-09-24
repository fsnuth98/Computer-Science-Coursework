'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 11
Part 3: Caesar Cypher
date April 14 2017
'''

import math
import random

key = int(input("Please enter the encryption key: "))
word = input("Please enter the word: ")
cipher = " "

for char in word:
    shifted_char = chr(ord(char)+key)
    cipher += shifted_char
    
print("The shifted word is: ", cipher)