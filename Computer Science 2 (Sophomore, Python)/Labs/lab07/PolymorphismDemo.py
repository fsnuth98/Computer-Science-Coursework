'''
CSC102 - Lab 07
Problem 1: Geometric Shapes
Franklin Nuth
Rasul Rasulov
March 2nd, 2018
'''

from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle
from EllipseFromGeometricObject import Ellipse
from SquareFromGeometricObject import Square

def main():
    # Display circle and rectangle properties
    c = Circle(4)
    r = Rectangle(1, 3)
    e = Ellipse(5,5)
    s = Square(5,5)
    
    all_shapes = [c,r,e,s]    
    print(all_shapes)    
    
    displayObject(c)
    displayObject(r)
    displayObject(e)
    displayObject(s)
    print("Are the circle and rectangle the same size?", 
        isSameArea(c, r))
    isSameArea(c,e)
    isSameArea(c,s)
    isSameArea(r,c)
    isSameArea(r,e)
    isSameArea(r,s)
    isSameArea(e,c)
    isSameArea(e,r)
    isSameArea(e,s)
    isSameArea(s,c)
    isSameArea(s,r)
    isSameArea(s,e)
    
    new_list = sorted(all_shapes, key=area_of_shape)
    print(new_list)        
    
# Display geometric object properties 
def displayObject(g):
    print(g.__str__())

# Compare the areas of two geometric objects 
def isSameArea(g1, g2):
    return g1.getArea() == g2.getArea()

def area_of_shape(s):
    return s.getArea()

main() # Call the main function
