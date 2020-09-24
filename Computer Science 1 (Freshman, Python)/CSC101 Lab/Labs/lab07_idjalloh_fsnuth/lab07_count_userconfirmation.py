'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 7
Part 4: Exercise 5.1, p.158 using user confirmation loop
March 3 2017
'''

import math
count_positive = 0
count_negative = 0

n = int(input("Enter the amount of times:"))

while n != 0:
    if n>0:
        count_positive+=1
        n = int(input("Enter the amount of times:"))
    elif n<0:
        count_negative+=1
        n = int(input("Enter the amount of times:"))
        
print("Your positive numbers count is: ", count_positive)
print("Your negative numbers count is: ", count_negative)

            