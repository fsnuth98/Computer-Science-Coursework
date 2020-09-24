# Franklin Nuth
# Rasul Rasulov
# CSC102, Lab 2 : Set Calculator
# January 26th, 2018

def show_intro():
    print("This program allows you to make a simple \n"
           "operations with sets.")
    
def show_menu_options():
    print("""
              ---------------------------------------
                  MENU
              ---------------------------------------
              1 Change Set 1
              2 Change Set 2
              3 Intersection (Set 1 & Set 2)
              4 Union (Set 1 | Set 2)
              5 Difference (Set 1 - Set 2)
              6 Symmetric Difference (Set 1 ^ Set 2)
              0 Quit
              --------------------------------------
              """)

def get_menu_option():
    option = -1
    while option < 0 or option > 6 :
        show_menu_options()
        option = int(input('Type an option number and press ENTER: '))
    return option


def readSetFromUser():
    """Reads a comman separated string of values
       and turns it into a set"""
    stringOfItems = input("Enter a comma-separated sequence of values: ")  
    listOfitems = stringOfItems.split(',')          # turn string into a list
    print(listOfitems)
    tempSet = set(listOfitems)                      # turn values into a set
    return tempSet                                  # return set

def showSets(set1, set2):
        """ show current value of the sets"""
        print()
        print("Set 1 = ", set1)
        print("Set 2 = ", set2)
        print()    

def main():
    show_intro()

    set1 = set()
    set2 = set()
    
    option = -1
    while option != 0 : # 0 = Quit
        showSets(set1, set2)

        option = get_menu_option()

        if option == 1:
            set1 = readSetFromUser()
        elif option == 2:
            set2 = readSetFromUser()
        elif option == 3:
            print(set1 & set2)
        elif option == 4:
            print(set1 | set2)
        elif option == 5:
            print(set1 - set2)
        elif option == 6:
            print(set1 ^ set2)
        # add rest of options here
                               


main()
