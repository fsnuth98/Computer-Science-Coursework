'''
CSC102 - Lab 03
Problem 2: Greatest Common Divisor
Franklin Nuth
Rasul Rasulov
February 2nd, 2018
'''
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

print("This program calculates the greatest common divisor of two numbers.")
a = int(input("Enter first number: "))
b = int(input("Enter the second number: "))

# call the cgd function
# print the value returned by the function
result = gcd(a,b)
print("The value that the function returns is ", result)

#Calculating gcd(54,34):
#gcd(34,20)
#gcd(20,14)
#gcd(14,6)
#gcd(6,2)
#gcd(2,0)