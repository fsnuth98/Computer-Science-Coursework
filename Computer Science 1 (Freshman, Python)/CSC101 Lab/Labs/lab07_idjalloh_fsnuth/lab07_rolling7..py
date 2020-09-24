'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 7
Part 1: Rolling until 7
February 3 2017
'''

import math
import random


die1 = random.randint(1,6)
die2 = random.randint(1,6)

total = die1 + die2

while die1 + die2 != 7:
    total +=1
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print("die 1:", die1, " die 2:", die2, "*")
    print("die 1:", die1, " die 2:", die2)