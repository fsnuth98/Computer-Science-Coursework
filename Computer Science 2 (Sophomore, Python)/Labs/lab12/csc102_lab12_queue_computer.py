from queue import *

def main():
    print("Queue computer.")
    print("Enter a sequence of + and - characters (no spaces).")
    queue_program = input("Enter queue program: ")
    q = Queue()
    count = 1
    
    for character in queue_program:
        if character == '+':
            q.enqueue(count)
            count += 1
        elif character == '-':
            v = q.dequeue() 
            print(v, end = " ")
        
    print()
    
    if q.isEmpty():
        print("String sucessfully processed.")
        
    else:
        print("The following items were left in the queue.")
        
        while not q.isEmpty():
            v = q.dequeue()
            print(v, end = " ")
        print()
        
main()