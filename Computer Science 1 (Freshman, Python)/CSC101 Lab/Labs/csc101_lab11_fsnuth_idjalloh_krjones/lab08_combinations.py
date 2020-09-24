'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 8
Part 5: All Possible Combinations
April 14, 2017
'''

import math
import random

for flavor in ['Chocolate', 'Vanilla', 'Strawberry']:
  for topping in ['Chocolate', 'Vanilla', 'Strawberry']:
    for topping2 in ['Chocolate', 'Vanilla', 'Strawberry']:
      if flavor in ['Chocolate', 'Vanilla', 'Strawberry'] and topping == topping2:
        print("Flavor:", flavor, "Topping: Double ", flavor)
      else:
        print("Flavor:", flavor, "Topping 1:", topping, "Topping 2:", topping2)