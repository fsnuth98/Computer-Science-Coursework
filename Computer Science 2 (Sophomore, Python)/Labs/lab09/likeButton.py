"""
CSC102 - Lab 09
Problem 2: Like Button with Counter
Franklin Nuth
Rasul Rasulov
April 6th, 2018
"""

from tkinter import *

class LikeButton(Button): #class LikeButton is a subclass of class Button.
    def __init__(self,window):
        self.likeImage = PhotoImage(file= "likebutton.gif") #Sets self.likeImage to the image 'likebutton.gif'.
        super().__init__(window, image=self.likeImage, text='0', compound=RIGHT, font='Arial 20', command = self.likeButtonClicked, bg='white') #Refers all information to parameter Button.
        self.likesCounter = 0
        
    def likeButtonClicked(self):
        self.likesCounter += 1
        self['text'] = " " + str(self.likesCounter)
        
    def getLikesCounter(self):
        return self.likesCounter
    
    def resetLikes(self):
        self.likesCounter = 0
        self["text"] = "0"

if __name__ == "__main__": #Code that is read globally.
    #Test stub
    class LikeButtonTestApp:
        def __init__(self):
            window = Tk()
            self.likeBtn = LikeButton(window)
            self.likeBtn.pack()
            Button(window, text="Report and Reset", command = self.reportLikes).pack()
            window.mainloop()
            
        def reportLikes(self):
            print("Current likes: ", self.likeBtn.getLikesCounter())
            self.likeBtn.resetLikes()
        
    LikeButtonTestApp()