'''
CSC101 Lab 9
Part 4: Points in circle 
Idrissa Jalloh
Franklin Nuth
March 31 2017
'''

import turtle 
import random
import mytools

turtle.bgcolor('darkgray') # set background color

# PROGRAM STARTS HERE
xc, yc = eval(input("Please enter the x and y of your center circle!: "))
r = eval(input("Please enter the radius of your circle!: "))

turtle.tracer(False) # Animation Off

for i in range(2000):
   x, y = mytools.random_location()
   mytools.move (x,y) # make turtle jump to location (x,y)
   if mytools.is_point_in_circle(xc, yc, r, x, y):
      turtle.dot(10, 'blue')
   else:
      turtle.dot(5, 'orange')
 
turtle.update() # Show all points at once
turtle.done()