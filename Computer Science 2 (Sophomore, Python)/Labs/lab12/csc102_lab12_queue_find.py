from queue import *
from random import *

def findItemInQueue(item, queue):
    helperQ = Queue()
    found = False
    
    while not queue.isEmpty():
        n = queue.dequeue()
        helperQ.enqueue(n)
        if n == item:
            found = True
            
    while not helperQ.isEmpty():
        queue.enqueue(helperQ.dequeue())
        
    return found

def main():
    # create a queue with 10 random values, between 1 and 100
    q = Queue()
    for i in range(10):
        q.enqueue(randint(1,100))

    print("Values in queue:", q)

    # Try finding a value in the queue
    item = int(input("What value to find? "))
    
    if findItemInQueue(item, q):
        print("Value found!")
        
    else:
        print("Sorry, value not found.") 

main() 