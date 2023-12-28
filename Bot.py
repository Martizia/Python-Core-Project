from ContactBook import ContactBook
from Contacts import Contact
from NoteBook import NoteBook
from Notes import Note
from dashtable import data2rst

class Bot:
    def __init__(self):
        self.contacts_from_file = ContactBook.load_contacts_from_json_file("Output/contacts.json")
        self.notes_from_file = NoteBook.load_notes_from_json_file("Output/notes.json")

    def run(self, action):
        if action == 1:
            table = [["1. Add", "2. Edit", "3. Find", "4. Delete", "5. Show all", "6. Day's till Birthday", "7. Return"]]
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
            elif action_contact == 2:
                self.contacts_from_file.edit_contact()
            elif action_contact == 3:
                self.contacts_from_file.find_contact()
            elif action_contact == 4:
                self.contacts_from_file.delete_contact()
            elif action_contact == 5:
                self.contacts_from_file.show_all_contacts()
            elif action_contact == 6:
                dict_with_number = self.contacts_from_file.find_contact()
                days_input = int(input("Please choose contact number: "))
                for key, value in dict_with_number.items():
                    if key == days_input:
                        contact_from_dict = self.contacts_from_file[value]
                        days_till_bd = self.contacts_from_file.days_to_birthday(contact_from_dict)
                        print(f"It's {days_till_bd} day(s) till {value}'s Birthday")
            elif action_contact == 7:
                pass
        elif action == 2:
            table = [["1. Add", "2. Edit", "3. Find", "4. Delete", "5. Show all", "6. Return"]]
            print(data2rst(table))
            action_contact = int(input("Please make your choice: "))
            if action_contact == 1:
                title = input("Note title: ")
                text = input("Note text: ")
                tags = input("Tags: ")
                note = Note(title, text, tags)
                self.notes_from_file.add_note(note)
                self.notes_from_file.save_notes_to_json_file("Output/notes.json")
            elif action_contact == 2:
                self.notes_from_file.edit_note()
            elif action_contact == 3:
                self.notes_from_file.find_note()
            elif action_contact == 4:
                self.notes_from_file.delete_note()
            elif action_contact == 5:
                self.notes_from_file.show_all_notes()
            elif action_contact == 6:
                pass