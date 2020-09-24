'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 7
Part 2: Rolling three 7s in a row
March 3 2017
'''

import math
import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)
user1 = eval(input("Please enter the amount of 7s you want: "))
roll7 = 0
nonroll7 = 0

while user1 != roll7:
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    if die1+die2 == 7:
        roll7 += 1
        print("die 1: ", die1, "die 2", die2, "*")
    else:
        nonroll7 += 1
        print("die 1: ", die1, "die 2", die2)
print("You rolled 7", roll7, "times and you rolled a total of ", nonroll7, "times.")