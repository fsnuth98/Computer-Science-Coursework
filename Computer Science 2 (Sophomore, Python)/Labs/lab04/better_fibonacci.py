'''
CSC102 - Lab 04
Problem 3: Better Fibonacci
Franklin Nuth
Rasul Rasulov
February 9th, 2018
'''

import time

calculatedFib = {}
    
def betterFib(n):
    global calculatedFib
    
    # If the n-th fib number is in the dictionary, use this value
    if n in calculatedFib:
        return calculatedFib[n]
        
    # Base cases
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive step
    else:
        # Calculate and save fib of (n-2) 
        f2 = betterFib(n-2)
        calculatedFib[n-2] = f2
            
        # Calculate and save fib of (n-1)
        f1 = betterFib(n-1)
        calculatedFib[n-1] = f1
    
        # Calculate and save fib of n
        fn = f2 + f1
        calculatedFib[n] = fn
    
        return fn

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

n = int(input("Enter the Fibonacci number to calculate: "))   

start = time.time()
x = fib(n)
end = time.time()

elapsedFib = end-start

start = time.time()
x = betterFib(n)
end = time.time()

elapsedBetterFib = end-start

print("{:.10f}".format(elapsedFib),"\t", "{:.10f}".format(elapsedBetterFib))

"""
  n       fib       betterFib
--------------------------------
 10        0             0
 20    0.0030000210     0.0000000000
 30     0.4720001221    0.0000000000
 40    57.0920000076     0.0000000000
--------------------------------
"""