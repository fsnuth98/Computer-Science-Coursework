# Franklin Nuth
# Rasul Rasulov
# CSC102. Lab 2: Students Grade
# January 26th, 2018


def show_intro():
    print("This program manages a simple list \n of students and their final grades.")

def add_student( students ):
    #name = input("Enter student's name: ")
    name = input("Enter student's name: ")
    #name = name.lower()     
    name = name.lower()
    # add student and grade to dictionary only if it is not already in it
    grade = input("Enter student's grade: ")
    if name not in students:
        students[name] = grade
        

def delete_student( students ):
    
    #name = input("Enter student's name: ")
    name = input("Enter student's name: ")
    #name = name.lower()
    name = name.lower()
    # delete student if it is in the dictionary
    if name in students:
        del students[name]
    # ask for confirmation before deleting using a ybbox()

                       
def list_by_name( students ):
    # turn dictionary student into a list of tuples using list(students.items())
    students.items()
    # sort list as it is
    list = students.items()
    # display student's names and grade\
    print(list)

    


def list_by_grade( students ):
    
    # turn dictionary student into a list of tuples using list(students.items())
    students.items()
    # create decorator list
    decorator = []
    myTuples = [(students)]
    # [ (grade, name), (90, 'tom'), ...]
    # create decorator so each tuple is (grade,name)
    # Since the grade is now the first element in the tuples, 
    # sort() will correctly arrange the data in ascending order
    # of grades
    myTuples.sort()
    # reverse the list to show the results from the lowest to the highest
    # using the reveSrse list method
    # display contents of decorator
    print(students)

#################### NO NEED TO MODIFY THE CODE BELOW ##################

def main():
    show_intro()

    students = {} # create dictionary
    
    option = None
    while option != 5 : # 5 = Quit
        option = get_menu_option()
        if option == 1:
            add_student( students )
        elif option ==  2:
            delete_student( students )
        elif option == 3:
            list_by_name( students )
        elif option == 4:
            list_by_grade( students )
            
                

def get_menu_option():
    option = 0
    while option < 1 or option > 5 :
        print('------------------------\n'
              '1 Add a student\n' 
              '2 Delete a student\n'
              '3 List students by name\n'
              '4 List students by grade\n'
              '5 Quit\n'
              '------------------------\n')
        
        option = int(input("Enter selection [1-5]: "))
    return option




main()
