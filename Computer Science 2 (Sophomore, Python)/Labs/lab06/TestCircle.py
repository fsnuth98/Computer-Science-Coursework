'''
CSC102 - Lab 06
Problem 2: Playing With Circles
Franklin Nuth
Rasul Rasulov
February 23rd, 2018
'''



from Circle import Circle

def main():
    # Create a circle with Radius 1
    circle1 = Circle()
    print("The area of the circle of Radius",
        circle1.Radius, "is", circle1.getArea())

    # Create a circle with Radius 25
    circle2 = Circle(25)
    print("The area of the circle of Radius",
        circle2.Radius, "is", circle2.getArea())

    # Create a circle with Radius 125
    circle3 = Circle(125)
    print("The area of the circle of Radius",
        circle3.Radius, "is", circle3.getArea())

    # Modify circle Radius
    circle2.Radius = 100
    print("The area of the circle of Radius", 
        circle2.Radius, "is", circle2.getArea())

    circle4=circle1+circle2
    print("The sum of circles 1 and 2 are: ", circle4)

main() # Call the main function