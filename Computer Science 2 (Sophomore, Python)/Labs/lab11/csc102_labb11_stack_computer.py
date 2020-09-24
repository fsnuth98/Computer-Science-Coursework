from Stack import *

def main():
    print("Stack computer.")
    print("Enter a sequence of + and - characters (no spaces).")
    s = Stack()
    stack_program = input("Enter stack program: ")
    count = 1
    for character in stack_program:
        if character == '+':
            s.push(count)
            count += 1
        elif character == '-':
            n = s.pop()
            print(n, end= " ")
            
    if s.isEmpty():
        print("String sucessfully processed.")
    else:
        print("The following items were left in the Stack: ")
        while count != 0:
            n = s.pop()
            print(n, end = " ")
            count -= 1
        print()
              
main()