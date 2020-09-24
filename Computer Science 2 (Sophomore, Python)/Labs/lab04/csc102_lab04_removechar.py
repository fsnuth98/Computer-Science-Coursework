'''
CSC102 - Lab 04
Problem 1: Remove All Occurences of a Character in a String
Franklin Nuth
Rasul Rasulov
February 9th, 2018
'''

def removeChar(text, char):
    if text == "":
        return ""
    elif char == text[0]:
        return removeChar(text[1:], char)
    else: 
        return text[0] + removeChar(text[1:], char)
print(removeChar('Mississippi','i'))