'''
Idrissa Jalloh
Franklin Nuth
Kareem Jones
CSC101 Lab 13
Part 1: Binary Search
April 28 2017
'''

import math
import random

def binarySearch(values, key):
  print("\tlow\thigh\tmid\tvalues[mid]")
  low = 0
  high = len(values) - 1
  while low <= high:
      mid = (low + high) // 2
      print('\t', low, '\t', high, '\t', mid, '\t', values[mid])
      if values[mid] == key:
          return mid
      elif values[mid] < key:
          low = mid + 1
      else:
        high = mid - 1
  print('\t', low, '\t', high, '\t', mid, '\t', values[mid])
  return -low - 1


values = eval(input("Enter a comma-separated list of values!: "))
key = eval(input("Enter your key!: "))

binarySearch(values,key)