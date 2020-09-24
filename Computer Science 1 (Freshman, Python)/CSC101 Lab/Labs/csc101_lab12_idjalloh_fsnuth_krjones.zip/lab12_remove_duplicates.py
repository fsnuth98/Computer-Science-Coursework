''' 
Idrissa Jalloh 
Franklin Nuth
Kareem Jones
CSC101 Lab 12 
Part 3: Remove Duplicates
April 21 2017
'''
import math
import random

lst = eval(input("Enter a list of values: "))

i = 0
while i < len(lst):
    if lst.count(lst[i])>1:
        lst.remove(lst[i])
    else:
        i += 1
        
print(lst)
                        
