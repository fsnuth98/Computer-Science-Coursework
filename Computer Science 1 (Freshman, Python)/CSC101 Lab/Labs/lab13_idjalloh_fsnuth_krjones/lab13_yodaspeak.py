'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 13
Part 2: Yoda Speak
April 28 2017
'''

import random

#Read sentence from user
sentence = input("Enter a sentence:")
#Break sentence into words
words = sentence.split()
#Assemble Yoda-speak
yoda_speak = words[2:]+ [','] + words[0:2]
#Display Yoda speak as a single string
print("Yoda-speak: "," ".join(yoda_speak))
