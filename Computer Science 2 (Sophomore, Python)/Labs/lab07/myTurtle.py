'''
CSC102 - Lab 07
Problem 2: My Turtle
Franklin Nuth
Rasul Rasulov
March 2nd, 2018
'''

from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')

    def forward(self,distance):
        super().forward(distance)
        self.write(self.position())
        return self
        
    def backward(self,distance):
        super().backward(distance)
        self.write(self.position())
        return self
        
    def goto(x,y):
        super().goto(x,y)
        self.write(self.position())        
        return self
    
    def pencolor(self, color):
        super().pencolor(color)   
        return self
    
    def right(self,distance):
        super().right(distance)
        return self
    
    def left(self,distance):
        super().left(distance)
        return self
    
    def pensize(self,size):
        super().pensize(size)
        return self
"""
if __name__ == "__main__":
    # place your test code here
    tom = MyTurtle()
    
    for i in range(4):
        tom.pencolor('blue').pensize(1).forward(100).right(120)
        tom.pencolor('red').pensize(5).forward(100).right(120)
        tom.pencolor('green').pensize(10).forward(100)

done()
"""