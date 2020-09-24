from Stack import *

def compute(v1, op, v2):
   if op == "+":
      return (v1 + v2)
   elif op == "-":
      return (v1 - v2)
   elif op == "*":
      return (v1 * v2)
   elif op == "/":
      return (v1 / v2)
   
valueStack = Stack()
operatorStack = Stack()   

expression = input("Please enter an expression:")       

for token in expression:    
   if token is '(':
      pass    
   elif token in "1234567890":
      valueStack.push(float(token))
   elif token in "+-*/":
      operatorStack.push(token)      
   elif token == ')':
      v2 = valueStack.pop()
      v1 = valueStack.pop()
      op = operatorStack.pop()
      r = compute(v1, op, v2)
      valueStack.push(r)
      
print("Final value =", valueStack.pop())


   # add the rest of the operations using elif's