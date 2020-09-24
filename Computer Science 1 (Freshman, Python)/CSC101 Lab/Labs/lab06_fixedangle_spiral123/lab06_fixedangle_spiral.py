




import turtle
angle = int(input("Enter turning angle": ))
linecolor = input("What color to use for the outline of the shape? ")
insidecolor = input("What color to use for the inside of the shape? ")
N = int(input("Enter number of sides: "))
sideLength = 5
turtle.pensize(4)
turtle.pencolor(linecolor)
turtle.fillcolor(insidecolor)
turtle.begin_fill()

for i in range (N):
    turtle.forward(sideLength)
    turtle.left(angle)
    sideLength += 5
    
    turtle.done()
