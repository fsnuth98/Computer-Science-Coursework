''' 
Idrissa Jalloh 
Franklin Nuth
Kareem Jones
CSC101 Lab 12 
Part 2: To-Do List
April 21 2017
'''

import math
import random

def show_todo_items(todo_list):
    if len(todo_list) == 0:
        print("(List is empty)")
    else:
        for i in range(len(todo_list)):
            print(i + 1, todo_list[i]) 
            
def ask_menu_option(todo_list):
    print("====================================")
    print("  TO-DO List")
    print("====================================")
    print("  [A]dd      [R]emove ")
    print("  [Q]uit ")
    print("====================================")
    show_todo_items(todo_list)
    print("====================================")
 
    option = input("Enter an option and press ENTER: ")
    return option  

def add_list_item(todo_list):
    new_item = input("Enter item to add to the list:")
    todo_list.append(new_item)    

def remove_list_item(todo_list):
    remove_at = eval(input("Enter number of item to remove:"))
    #if remove_at is a valid position
    todo_list.pop(remove_at-1)
    #else
    #show message position is not valid

def main():
    todo_list = []
    option = ask_menu_option(todo_list)
    while option != 'Q':
        if option == 'A':
            add_list_item(todo_list)
        elif option == 'R':
            remove_list_item(todo_list)
            option = ask_menu_option(todo_list)
             
        option = ask_menu_option(todo_list)
    print("Bye") 

main() # call to start the program