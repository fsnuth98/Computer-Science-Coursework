'''
CSC102 - Lab 06
Problem 1: Contacts List
Franklin Nuth
Rasul Rasulov
February 23rd, 2018
'''

class Contact:
    def __init__(self, new_name='noname', new_phone='nophone', new_email='noemail'):
        self.name=new_name
        self.phone=new_phone
        self.email=new_email
        
    def __str__(self):
        return "Name:" + self.name + "\tPhone: " + self.phone + "\Email:" + self.email
    
    def add_contact(contacts_list):
        contacts_list.append(new_contact)
    
    def find_contact(contacts_list):
        contact_found=False
        for a_contact in contacts_list:
            if name_to_find in a_contact.name:
                print("Found:", a_contact)
                contact_found=True
        if not contact_found:
            print("No contact found with that name.")
    
    
    def print_contact(contacts_list):
        print("Current contacts:")
        for a_contact in contacts_list:
            print(a_contact)
    
    def read_option():
        option = input("MENU: " +\
                       "(A)dd a contact, " +\
                       "(F)ind a contact, " +\
                       "(P)rint all contacts, " +\
                       "(Q)uit : ").upper()
        return option        
    
    def main():
        print("Contacts List with OOP")
       
        contacts_list = []
     
        action = read_option()
        
        while action != 'Q':
            if action == 'A':
                add_contact(contacts_list)
            elif action == 'F':
                find_contact(contacts_list)
            elif action == 'P':
                print_contact(contacts_list)
            action = read_option()
            
        print("Bye")

main()