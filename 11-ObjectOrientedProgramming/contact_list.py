from contact import Contact
class Contact_list:
    
    def __init__(self):
        self.list = []

    def create_new_contact(self):
        new_name = input('Enter name: ')
        new_email = input('Enter email: ')
        new_number = input('Enter number: ')
        new_contact = Contact(new_name,new_email,new_number)
        self.list.append(new_contact)

    def show_info(self):
        for i in self.list:
            print(i)
            


        
        
    

        
