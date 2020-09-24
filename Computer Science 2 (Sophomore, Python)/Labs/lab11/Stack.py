from LinkedList import *

class Stack(LinkedList):
    
    def push(self, value):
        self.addFirst(value)
    
    def pop(self):
        return self.removeFirst()
    
    def peek(self):
        return self.getFirst()
        
if __name__=="__main__":
    s = Stack()
    print("Stack created. Current contents:", s)
    s.push(10)
    print("Pushing 10 onto the Stack. Current Stack:", s)
    n = s.pop()
    print("Value", n, "popped from the Stack. Current Stack:", s)
    print("Is the Stack empty?", s.isEmpty())