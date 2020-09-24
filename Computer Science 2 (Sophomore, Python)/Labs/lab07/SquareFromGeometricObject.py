'''
CSC102 - Lab 07
Problem 1: Geometric Shapes
Franklin Nuth
Rasul Rasulov
March 2nd, 2018
'''

from GeometricObject import GeometricObject
from RectangleFromGeometricObject import Rectangle

class Square(GeometricObject):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height
    
    def getArea(self):
        return self.__width * self.__height    
    
    def getWidth(self):
        return self.__width
    
    def setWidth(self, width):
        self.__width = width    
        
    def setHeight(self, height):
        self.__height = self.__height        

    def getHeight(self):
        return self.__height    