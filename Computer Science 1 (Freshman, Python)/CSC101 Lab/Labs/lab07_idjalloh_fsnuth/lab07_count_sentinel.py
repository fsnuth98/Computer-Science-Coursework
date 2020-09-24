'''
Idrissa Jalloh
Franklin Nuth
CSC101 Lab 7
Part 2: Exercise 5.1, p.158 using sentinel loop
March 3 2017
'''

import math

count_positive = 0
count_negative = 0
user = eval(input("Please enter a number or press 0 to finish: "))
loop = 0
total = 0


while user != 0:
   
    if user > 0:
        count_positive+=1
        loop+=1
        total += user
        user = eval(input("Please enter a number or press 0 to finish: "))
    elif user < 0:
        count_negative+=1
        loop+=1
        user = eval(input("Please enter a number or press 0 to finish: "))
        total += user
print("You have", count_positive, "positive numbers")
print("You have", count_negative, "negative numbers")
average=((total)/(count_positive+count_negative))
print("Your average is ", average)
print("Your total is ", total)