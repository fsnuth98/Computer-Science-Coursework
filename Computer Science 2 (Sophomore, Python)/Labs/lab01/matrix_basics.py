"""
  CSC102 - Lab 01
  Part 1 - 2D Fundamental Manipulations
  Franklin Nuth
  Rasul Rasulov
  January 19th, 2018
"""

import random

def getMatrix():
   matrix =[]
   numberOfRows = int(input("Enter the number of rows: "))
   numberOfColumns = int(input("Enter the number of columns: "))
   for row in range(numberOfRows):
      matrix.append([])                     # Add an empty new row
      for column in range(numberOfColumns):
         value = int(input("Enter an element and press Enter: "))
         matrix[row].append(value)
   return matrix

def printMatrix(matrix):
   for row in range(len(matrix)):
      for col in range(len(matrix[row])):
         print(matrix[row][col], end = " ")
      print()

def sumValuesInMatrix(matrix):
   total = 0
   for row in range(len(matrix)):
      for col in range(len(matrix[row])):
         total+=matrix[row][col]
   return total

def createRandomMatrix():
   matrix = []
   numberOfRows = eval(input("Enter the number of rows: "))
   numberOfColumns = eval(input("Enter the number of columns: "))
   for row in range(numberOfRows):
      matrix.append([])
      for column in range(numberOfColumns):
         matrix[row].append(random.randint(0,99))
   return matrix

def main():
    m = getMatrix()
    print("The value in the matrix area: ")
    printMatrix(m)
    print("The sum of all values is:")
    print(sumValuesInMatrix(m))
        # pass m to the other functions    
    
    m2 = createRandomMatrix()
    print("The value in the matrix area: ")
    printMatrix(m2)    
    
    """print("The sum of all values is:")
    print((sumValuesInMatrix(m))
    # pass m to the other functions"""

main()   # run program