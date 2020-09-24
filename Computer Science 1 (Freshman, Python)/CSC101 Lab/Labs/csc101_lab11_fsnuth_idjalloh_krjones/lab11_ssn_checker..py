'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 11
Part 1: Check SSN
date April 14 2017
'''

import random
import math

SSN = input("Enter SSN: ")

if SSN[:3].isdigit() and SSN[4:6].isdigit() and SSN[7:11].isdigit() and SSN[3] =='-' and SSN[6] == '-' and len(SSN) == 11:
  print("Valid social security number.")
  
else:
  print("Invalid number.")

