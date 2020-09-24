'''
CSC102 - Lab 07
Problem 1: Geometric Shapes
Franklin Nuth
Rasul Rasulov
March 2nd, 2018
'''

from GeometricObject import GeometricObject

class Ellipse(GeometricObject):
    def __init__(self, radius1 = 1, radius2 = 1):
        super().__init__()
        self.__radius1 = radius1
        self.__radius2 = radius2
        
    def __str__(self):
        return super().__str__() + "radius1: " + str(self.__radius1) + "radius2: " + str(self.__radius2)     
    
    def getRadius1(self):
        return self.__radius1

    def setWidth(self, radius1):
        self.__radius1 = radius1

    def getRadius2(self):
        return self.__radius2

    def setHeight(self, radius2):
        self.__radius2 = radius2
        
    def getArea(self):
        return self.__radius1 * self.__radius2      