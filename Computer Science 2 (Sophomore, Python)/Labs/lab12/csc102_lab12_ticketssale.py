from random import *
from queue import *
from LinkedList import *

ticket_line = Queue()
minutes = 0
tickets_left = 200

while tickets_left > 0:
    r = random()
    if r < 0.5:
        nro_customers = 1
    if r < 0.8:
        nro_customers = 2
    else:
        nro_customers = 3
        
    for i in range(nro_customers):
        ticket_line.enqueue(randint(1,4))
        
    if not ticket_line.isEmpty():
        buying = ticket_line.dequeue()    
        if buying > tickets_left:
            buying = tickets_left
        tickets_left -= buying
        
    minutes += 1
    
    print("Minute:", minutes)
    print("Customers:", ticket_line)
    print("Tickets left:", tickets_left)
    print()
        
print("It took", minutes, "minutes to sell", "all the tickets")
print("Customers without tickets:", nro_customers)