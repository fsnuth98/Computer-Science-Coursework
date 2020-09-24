'''
CSC102 - Lab 08
Problem 1: Temperature Conversion
Franklin Nuth
Rasul Rasulov
March 30th, 2018
'''

from tkinter import *
from random import *

class TemperatureConversion:
    
    def __init__(self):
        window = Tk()
        Label(window, text="Fahrenheit:").pack()
        self.inputTemperature = DoubleVar()
        Entry(window,textvariable=self.inputTemperature).pack()
        Label(window, text="Celsius:").pack()
        self.celsiusLabel = Label(window, text="0.0")
        self.celsiusLabel.pack()
        Button(window, text="Convert", command = self.fah2cel).pack()
        window.mainloop()       
    
    def fah2cel(self):
        fahrenheit = self.inputTemperature.get()
        celsius = fahrenheit - 32 * .5556
        self.celsiusLabel["text"] = str(celsius)
          
TemperatureConversion()