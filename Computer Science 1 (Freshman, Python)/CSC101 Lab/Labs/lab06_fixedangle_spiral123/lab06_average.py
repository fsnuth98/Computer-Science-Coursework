'''
Franklin Nuth
Idrissa Jalloh
CSC101 Lab 6
Part 4: Average Value
February 24 2017
'''

N= int(input("Enter number of items you want to purchase: "))
total= 0
if N <= 0:
       print("Cannot calculate average.") 
else:
       
       for i in range(N):   
           item= int(input("Enter the price for the item"))
           total += item
       average= total/N
       print("The average is:", average)