"""
CSC102 - Lab 09
Problem 3: Custom Canvas-Based Widget
Franklin Nuth
Rasul Rasulov
April 6th, 2018
"""

from tkinter import *

class FavWidget(Canvas):
    def __init__(self, window):
        self.fillstarImage = PhotoImage(file="star_filled.gif")
        self.emptystarImage = PhotoImage(file="star_empty.gif")
        super().__init__(window, width=20, height=20, bg='white') #Parameters set the window to 20x20 with white background.
        self.create_image(12,12, anchor=CENTER, image = self.emptystarImage) #Size of picture and positon.
        self.state = 0
        self.bind("<Button-1>", self.changeImage)
        
    def changeImage(self,event):
        self.delete("star")
        if self.state == 0:
            self.create_image(12,12, anchor=CENTER, image=self.fillstarImage, tag = "star")
            self.state = 1
        else:
            self.create_image(12,12, anchor=CENTER, image=self.emptystarImage, tag = "star")
            self.state = 0           
    
if __name__ == "__main__":
    class FavWidgetTestApp:
        def __init__(self):
            window = Tk()
            
            FavWidget(window).pack()
            
            window.mainloop()
            
    FavWidgetTestApp()