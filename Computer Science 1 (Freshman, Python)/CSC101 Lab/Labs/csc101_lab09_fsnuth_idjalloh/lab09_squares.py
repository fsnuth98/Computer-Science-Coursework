'''
CSC101 Lab 9
Part 2: Squares
Idrissa Jalloh
Franklin Nuth
March 31 2017
'''

import turtle
 
def move(x, y):
   turtle.penup()
   turtle.goto(x, y)
   turtle.pendown()
 
def draw_square(size):
   for i in range(4):
      turtle.forward(size)
      turtle.left(90)

def draw_square_at(x, y, size):
   move(x,y)
   draw_square(size)  

def draw_fill_square_at(x, y, size, outline_color, fill_color):
   turtle.fillcolor(fill_color)
   turtle.pencolor(outline_color)
   turtle.begin_fill()
   draw_square_at(x, y, size)
   turtle.end_fill()

draw_fill_square_at(-100, -100, 30, 'red', 'yellow')
draw_fill_square_at(-50, 100, 45, 'blue', 'green')
draw_fill_square_at(-70, 200, 60, 'red', 'gold')

turtle.done()  