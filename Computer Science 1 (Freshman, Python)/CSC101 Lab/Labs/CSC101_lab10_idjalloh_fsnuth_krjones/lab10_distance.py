'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 10
Part 2: Distance Between Points
April 7th, 2017
'''
import math
import random
import turtle
import UsefulTurtleFunctions
import mytools

def main():
   x1, y1, x2, y2 = collect_coordinates()
   d = mytools.distance(x1, y1, x2, y2)
   draw_output(x1, y1, x2, y2, d)
   turtle.done()

def collect_coordinates():
   x1, y1 = ask_for_point("Enter X and Y for first point: ")
   x2, y2 = ask_for_point("Enter X and Y for second point: ")
   return x1, y1, x2, y2   

def ask_for_point(message):
   x, y = eval(input(message))
   return x, y

def draw_output(x1, y1, x2, y2, d):
   draw_line_and_points(x1, y1, x2, y2)
   show_distance_in_middle_of_line(x1, y1, x2, y2, d)   

def draw_line_and_points(x1, y1, x2, y2):
   show_point(x1, y1)
   show_point(x2, y2)
   UsefulTurtleFunctions.drawLine(x1, y1, x2, y2)  

def show_point(x, y):
   UsefulTurtleFunctions.drawPoint(x, y)
   UsefulTurtleFunctions.writeText( "(" + str(x) + "," + str(y) + ")" ,x, y)

#def draw_line(x1,y1,x2,y2):
   #UsefulTurtleFunctions.drawLine(x1, y1, x2, y2)
   #return x1, x2, y1, y2

def show_distance_in_middle_of_line(x1,y1,x2,y2,d):
   midx, midy = calculate_midpoint(x1, y1, x2, y2)
   show_distance(midx, midy, d)   

def calculate_midpoint(x1,y1,x2,y2):
   midx = (x1 + x2) / 2
   midy = (y1 + y2) / 2
   return midx, midy 

def show_distance(midx,midy,d):
   UsefulTurtleFunctions.writeText( "d=" + str(d), midx, midy)
   
main()

