'''
Idrissa Jalloh
Franklin Nuth
CSC101 Lab 8
Part 2: Tiling
March 24 2017
'''

import turtle
import math
import random

nRows=eval(input("what is the number of rows:?"))
nCols=eval(input("What is the number of circles in a columns:?"))
xSeparation=eval(input("What is the Separation between circle horizontally:?"))
ySeparation=eval(input("What is the separation between circles vertically:?"))

y = 0
for lines in range(nRows):
    x = 0
    for circles in range(nCols):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.fillcolor(random.random(), random.random(), 0)
        turtle.circle(15)
        turtle.end_fill()        
        turtle.circle(15)
        x += xSeparation
    y += ySeparation
    
turtle.done()
