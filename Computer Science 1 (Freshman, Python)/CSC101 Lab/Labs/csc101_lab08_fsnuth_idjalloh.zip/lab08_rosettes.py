'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 8
Part 1: Turtle Rosettes
March 24 2017
'''

import random
import turtle


N = eval(input("How many sides do you want in your polygon?: "))
R = eval(input("How many rotations do you want?: "))

turtle.pencolor((random.random(), random.random(), random.random())) 

 
for reps in range(R):
     turtle.pencolor((random.random(), random.random(), random.random()))
     for sides in range(N):
        turtle.forward(100)
        turtle.pencolor((random.random(), random.random(), random.random()))
        turtle.left(360/N)
     turtle.left(360/R)
    
turtle.done()