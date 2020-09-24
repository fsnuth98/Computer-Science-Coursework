'''
Idrissa Jalloh
Kareem Jones
Franklin Nuth
CSC101 Lab 10
Part 1: Calculate Body Mass Index
April 7 2017
'''

import math
import random

def BMI_calculator():
    weight, height= get_user_data()
    BMI = calculate_BMI(weight, height)
    show_BMI_info(BMI)
def get_user_data():
    weight=eval(input("What is your weight?"))
    height=eval(input("what is your height?"))
    return weight, height
def calculate_BMI(weight, height):
    BMI=(weight)/((height)**2)
    return BMI
def show_BMI_info(BMI):
    if BMI >= 25:
        print("obesity")
    elif 18.5 <= BMI <= 24.9:
        print("Normal")
    else:
        print("under weight")
        
BMI_calculator()
    