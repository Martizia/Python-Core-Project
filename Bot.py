from ContactBook import ContactBook
from Contacts import Contact
from dashtable import data2rst

class Bot:
    def __init__(self):
        self.contacts_from_file = ContactBook.load_contacts_from_json_file("Output/contacts.json")

    def run(self, action):
        if action == 1:
            table = [["1. Add", "2. Edit", "3. Find", "4. Delete", "5. Show all", "6. exit"]]
            print(data2rst(table))
            action_contact = int(input("Please make your choice: "))
            if action_contact == 1:
                name = input("Name: ")
                phone = input("Phone: ")
                birthday = input("Birthday: ")
                email = input("Email: ")
                address = input("Address: ")
                contact = Contact(name, phone, birthday, email, address)
                self.contacts_from_file.add_contact(contact)
                self.contacts_from_file.save_contacts_to_json_file("Output/contacts.json")
                print(data2rst(table))
            elif action_contact == 7:
                pass