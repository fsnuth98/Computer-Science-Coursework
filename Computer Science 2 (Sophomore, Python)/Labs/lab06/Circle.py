'''
CSC102 - Lab 06
Problem 2: Playing With Circles
Franklin Nuth
Rasul Rasulov
February 23rd, 2018
'''
    
import math 

class Circle:
    # Construct a circle object 
    def __init__(self, new_radius = 1):
        self.__radius = new_radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi
          
    def setRadius(self,new_radius):
        print("set__radius was called")
        if new_radius>=0:    
            self.__radius = new_radius
        
    def getRadius(self):
        print("getRadius was called")
        return self.__radius
    
    Radius=property(getRadius,setRadius)
    
    def __add__(self,other_circle):
        new_circle=Circle()
        new_circle.Radius=self.Radius+other_circle.Radius
        return new_circle
    
    def __lt__(self,other_circle):
        if self.Radius < other_circle.Radius:
            return True
        else:
            return False
        
    def __ge__(self,other_circle):
        if self.Radius>=other_circle.Radius:
            return True
        else:
            return False
    
    def _mul_(self,number):
        new_circle=Cicle()
        new_circle.Radius=self.Radius*number
        return new_circle
    
    def __str__(self):
        return "<Circle: radius="+str(self.__radius)+">"
    