'''
CSC 102
Lab 10
Rasul Rasulov
Franklin Nuth
04/13/2018
'''
from LinkedList import  *

def show_menu():
    print('''
        ****** Menu ******
        [1] Add First
        [2] Add Last
        [3] Remove First
        [4] Remove Last
        [5] Get First
        [6] Get Last
        [7] Insert
        [8] Clear
        [9] is Empty?
        [10] Remove At
        [11] Print List
        [12] Find element function we are using?
        [0]  Quit
        ******************
        '''
        )

### Create the LinkedList object my_list here
my_list = LinkedList()


show_menu()
option = eval(input("Enter your option: "))
while option != 0:
    if option == 1:
        item = input("Enter item to add first: ")
        my_list.addFirst(item)  # object and the function method name from that class and it will only have paramtr only if its in the class have one
    elif option == 2:
        item = input("Enter item to add last: ")
        my_list.addLast(item)
    elif option == 3:
        print("Removed first.")
        item = my_list.removeFirst()
        print("The item removed is:",item)
    elif option == 4:
        print("Removed last.")
        item = my_list.removeLast()
        print("The item removed is:",item)
    elif option == 5:
        item = my_list.getFirst()
        print("The first item is:", item)
    elif option == 6:
        item = my_list.getLast()
        print("The last item is:", item)
    elif option == 7:
        index = eval(input("What index would you like to look at?"))
        m = input("What element do you like to insert?")
        my_list.insert(index,m)
    elif option == 8:
        my_list.clear()
        print("The list has been cleared.")
    elif option == 9:
        item= my_list.isEmpty()
        print("Is it empty:", item)
        
        
    elif option == 10:
        item = eval(input("What index do youwant to remove in the item?"))
        print("Removed Item: ", my_list.removeAt(item))
    elif option == 11:
        print(my_list)
    elif option == 12:
        item = input("Which element exists in the class?")
        print("It have been found ",my_list.contains(item))
    else:
        print("Invalid input")
        
    show_menu()
    option = eval(input("Enter your option:"))
    

