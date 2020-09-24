from Stack import *

s = Stack()

n = int(input("Enter a number or -1 to quit: "))
while n != -1:
    s.push(n)
    n = int(input("Enter a number or -1 to quit: "))
   
print("The values you entered in reverse order are: ")
while s.isEmpty() == False:
    n = s.pop()
    print(n, end=" ")
    
print()
print("Done")