'''
CSC 102
Lab 10
Rasul Rasulov
Franklin Nuth
04/13/2018
'''
from LinkedList import LinkedList
import time
"""
startTime = time.time()
list1 = LinkedList()
for i in range(100000):
   list1.insert(0, "Chicago")
elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")

startTime = time.time()
pylist = []
for i in range(100000):
   pylist.insert(0, "Chicago")
elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")

#Time for LinkedList is 0.14046692848205566 seconds
#Time for list is 2.1262378692626953 seconds
#____________________________________
"""

startTime=time.time()
list2 = LinkedList()
for i in range(100000):
   list2.insert(0, "Chicago")
for i in range(100000):
   list2.removeLast
elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")




startTime = time.time()
pylist1 = []
for i in range(100000):
   pylist1.insert(0, "Chicago")
for i in range(100000):
   pylist1.pop
elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")

#Time for LinkedList is 0.15630197525024414 seconds
#Time for list is 1.98826003074646 seconds
#___________________________
startTime=time.time()
list3 = LinkedList()
for i in range(100000):
   list3.insert(0, "Chicago")
for i in range(100000):
   list3.removeLast
for i in range(100000):
   list3.removeFirst
elapsedTime = time.time() - startTime
print("Time for LinkedList is", elapsedTime, "seconds")


startTime = time.time()
pylist2 = []
for i in range(100000):
   pylist2.insert(0, "Chicago")
for i in range(100000):
   pylist2.pop
for i in range(100000):
   pylist2.pop(0)
   
elapsedTime = time.time() - startTime
print("Time for list is", elapsedTime, "seconds")

#Time for LinkedList is 0.17386102676391602 seconds
#Time for list is 2.08778715133667 seconds
#Time for LinkedList is 0.18643689155578613 seconds
#Time for list is 3.902529001235962 seconds


