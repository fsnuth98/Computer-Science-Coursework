'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 11
Part 4: English to Leet
April 14 2017
'''

import math

input_str = input("Enter a word: ")
output_str = ''
index = 0
while index < len(input_str):
    current_letter = input_str[index]
    if current_letter == 'A':
        new_letter = '4'
    elif current_letter.upper() == 'G':
        new_letter = '6'
    elif current_letter == 'E':
        new_letter = '3'
    elif current_letter == 'I':
        new_letter = '1'
    else:
        new_letter = current_letter
    output_str += new_letter
    index += 1
    
print("The word in leet is: ", output_str)