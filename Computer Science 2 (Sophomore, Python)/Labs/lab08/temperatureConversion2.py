'''
CSC102 - Lab 08
Problem 2: Arranging Components
Franklin Nuth
Rasul Rasulov
March 30th, 2018
'''

from tkinter import *
from random import *

class TemperatureConversion:
    
    def __init__(self):
        window = Tk()
        Label(window, text="Fahrenheit:").grid(row=0, column=0)
        self.inputTemperature = DoubleVar()
        Entry(window,textvariable=self.inputTemperature).grid(row=0, column=1)
        Label(window, text="Celsius:").grid(row=1, column=0)
        self.celsiusLabel = Label(window, text="0.0")
        self.celsiusLabel.grid(row=1, column=1)
        Button(window, text="Convert", command = self.fah2cel).grid(row=2,column=0, columnspan=2, sticky=W+E)
        window.mainloop()       
    
    def fah2cel(self):
        fahrenheit = self.inputTemperature.get()
        celsius = fahrenheit - 32 * .5556
        self.celsiusLabel["text"] = str(celsius)
          
TemperatureConversion()