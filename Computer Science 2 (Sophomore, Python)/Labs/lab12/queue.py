from LinkedList import *

class Queue(LinkedList):
    def enqueue(self,value):
        self.addLast(value)
    
    def dequeue(self):
        return self.removeFirst()
        
    def peek(self):
        return self.getFirst()
        
if __name__=="__main__":
    q = Queue()
    q.enqueue(15)
    print("Adding 15 to the current queue. Current queue:", q)
    q.enqueue(30)
    print("Adding 30 to the current queue. Current queue:", q)
    q.enqueue(45)
    print("Adding 45 to the current queue. Current queue:", q)
    
    n = q.dequeue()
    n = q.dequeue()
    n = q.dequeue()
    
    print("Value", n, "removed from the queue. Current queue:", q)
    
    print("Is the queue empty?", q.isEmpty())
    
    print("Queue created. Current contents:", q)
    