"""
CSC102 - Lab 09
Problem 1: MyPaint Program
Franklin Nuth
Rasul Rasulov
April 6th, 2018
"""



from tkinter import *

class MyPaintProgram:
    def __init__(self):
        window = Tk()
        
        self.canvas = Canvas(window, bg='white')
        self.canvas.pack(fill=BOTH, expand=1) #Expand helps to fill the window vertically.
        self.canvas.bind("<Button-1>", self.mouseDownHandler)
        self.canvas.bind("<B1-Motion>", self.mouseDraggingHandler) #Bind the function to when the mouse first button is pressed and dragged.
        Button(window, text='Clear', command = self.clearButtonClick).pack()
        
        self.pensize = 1
        Button(window,text='Pensize +', command = self.pensizeUp).pack()
        Button(window,text='Pensize -', command = self.pensizeDown).pack()
        self.pensizeLabel = Label(window, text='Pensize: 1')
        self.pensizeLabel.pack()
        
        self.pen_color = 'black'
        Button(window, text='Black', command = self.blackButtonClicked).pack()
        Button(window, text='Orange', command = self.orangeButtonClicked).pack()
        
        self.lastX = 0
        self.lastY = 0
        
        window.mainloop()
        
    def blackButtonClicked(self):
        self.pen_color = 'black'
        
    def orangeButtonClicked(self):
        self.pen_color = 'orange'
        
    def pensizeUp(self):
        if self.pensize < 20:
            self.pensize += 1
            self.pensizeLabel["text"] = "Pensize " + str(self.pensize) #Same as Line 32.
    
    def pensizeDown(self):
        if self.pensize > 1:
            self.pensize -= 1
            self.pensizeLabel["text"] = "Pensize " + str(self.pensize) #Changes the string value of self.pensizeLabel to the string value of the current pensize.
    
    def mouseDraggingHandler(self, event):
        self.canvas.create_line(self.lastX, self.lastY, event.x, event.y, width=self.pensize, fill=self.pen_color, tag='doodle') #Width now equals self.pensize, and line color equal to self.pen_color.
        self.lastX = event.x
        self.lastY = event.y    
        
    def clearButtonClick(self):
        self.canvas.delete('doodle') #No tag= needed since the parameter is tag by default.
      
    def mouseDownHandler(self,event): #The parameter event helps to print out x and y.
        self.lastX = event.x
        self.lastY = event.y
        
MyPaintProgram()