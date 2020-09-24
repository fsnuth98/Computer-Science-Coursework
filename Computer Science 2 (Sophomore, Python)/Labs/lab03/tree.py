'''
CSC102 - Lab 03
Problem 3: Drawing Trees
Franklin Nuth
Rasul Rasulov
February 2nd, 2018
'''

import turtle
import random
turtle.left(90)
turtle.speed(90000001)
turtle.pensize(10)  

def drawTree(size, level):
    if level > 0:
        turtle.forward(size)
        turtle.left(30)    
        drawTree(size*0.6, level-1)
        turtle.right(60)
        drawTree(size*0.6, level-1)
        turtle.left(30)
        turtle.backward(size)
    else:
        turtle.dot(20, 0, 0.5+random.random()/2, 0)
    
drawTree(100,10)
turtle.done()