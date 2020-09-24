'''
CSC102 - Lab 08
Problem 3: More Components
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
        
        self.temperatureType = IntVar()
        self.temperatureType.set(1)
        Radiobutton(window,text="Freezing Point", variable = self.temperatureType, value=1).grid(row=3, column=0, columnspan=2, padx=10, sticky=W)
        Radiobutton(window,text="Boiling Point", variable = self.temperatureType, value=2).grid(row=4, column=0, columnspan=2, padx=10, sticky=W)
        Radiobutton(window,text="Room Temperature", variable = self.temperatureType, value=3).grid(row=5, column=0, columnspan=2, padx=10, sticky=W)
        
        Button(window, text="Show Temperature", command=self.showTemperatureClicked).grid(row=6, column=0, columnspan=2, sticky=W+E)
        
        window.mainloop()       
    
    def fah2cel(self):
        fahrenheit = self.inputTemperature.get()
        celsius = (fahrenheit - 32) * .5556
        self.celsiusLabel["text"] = str(celsius)
        
    def showTemperatureClicked(self):
        if self.temperatureType.get() == 1:
            self.inputTemperature.set(32)
        elif self.temperatureType.get() == 2:
            self.inputTemperature.set(212)
        elif self.temperatureType.get() == 3:
            self.inputTemperature.set(72)
        self.fah2cel()
        
TemperatureConversion()