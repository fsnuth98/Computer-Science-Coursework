import turtle
import random
import math

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
   
def distance(x1, y1, x2, y2):
   distance= math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
   return distance

def is_point_in_circle(xc, yc, r, x, y):
      if distance(xc, yc, x, y) <= r:
         return True
      return False
   
def random_location():
   randx = random.randint(-25, 25) * 10
   randy = random.randint(-25, 25) * 10
   return randx, randy