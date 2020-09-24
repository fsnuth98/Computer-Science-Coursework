''' 
Idrissa Jalloh 
Franklin Nuth
Kareem Jones
CSC101 Lab 12 
Part 1: Chinese Zodiac Redux 
April 21 2017
'''

import math
import random

year=eval(input("Enter a year:"))
zodiacYear=year % 12

list = ['monkey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep']

if zodiacYear==0:
    print(list[0])
elif zodiacYear==1:
    print(list[1])
elif zodiacYear==2:
    print(list[2])
elif zodiacYear==3:
    print(list[3])
elif zodiacYear==4:
    print(list[4])
elif zodiacYear==5:
    print(list[5])
elif zodiacYear==6:
    print(list[6])
elif zodiacYear==7:
    print(list[7])
elif zodiacYear==8:
    print(list[8])
elif zodiacYear==9:
    print(list[9])
elif zodiacYear==10:
    print(list[10])
else:
    print(list[11])
   