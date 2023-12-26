from Contacts import Contact, Birthday, Address
from collections import UserDict
import json
from rich.table import Table
from rich.console import Console
from datetime import datetime
from  dashtable import data2rst


class ContactBook(UserDict):
    def add_contact(self, contact: Contact):
        self.data[contact.name.value] = contact
        return self.data

    def add_contact_to_file(self):
        pass

    def convert_to_serializable_contact(self):
        serializable_data = {}
        for key, contact in self.data.items():
            serializable_data[str(key)] = {
                "contact": contact.name.value,
                "phones": contact.phones.value,
                "birthday": contact.birthday.value,
                "email": contact.email.value,
                "address": contact.address.value
            }
        return serializable_data

    def save_contacts_to_json_file(self, filename):
        data_to_serialize = self.convert_to_serializable_contact()
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file, indent=4)
                json_file.write('\n')
            print(f'Contacts saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving contacts to {filename}: {e}')

    def load_contacts_from_json_file(filename):
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            loaded_contacts = ContactBook()
            for key, value in data.items():
                contact = key
                phones = " ".join(phone for phone in value["phones"])
                birthday = value["birthday"]
                email = value["email"]
                address = value["address"]
                contact_record = Contact(contact, phones, birthday, email, address)
                loaded_contacts.add_contact(contact_record)
            print(f'Notes loaded from {filename} successfully.')
            return loaded_contacts
        except Exception as e:
            print(f'Error loading from {filename}: {e}')
            return ContactBook()  # Return a new instance in case of an error

    def find_contact(contacts_from_file):
        try:
            search_info = input("Enter info for search: ").lower()
            result_list = []
            for item in contacts_from_file.values():
                search_by_name = item.name.value.lower().find(search_info)
                search_by_phones = str([phone.lower() for phone in item.phones.value]).find(search_info)
                search_by_birthday = str(item.birthday).find(search_info)
                search_by_email = item.email.value.lower().find(search_info)
                search_by_address = item.address.value.lower().find(search_info)
                if search_by_name > -1 or search_by_phones > -1 or search_by_birthday > -1 or search_by_email > -1 or search_by_address > -1:
                    result_list.append(item)
            dict_with_number = dict(zip([i + 1 for i in range(len(result_list))], [i.name.value for i in result_list]))
            print(dict_with_number)
            return dict_with_number
        except ValueError:
            print("Invalid input. Please enter a valid info for search.")

    def edit_contact(contacts_from_file):
        try:
            dict_with_number = contacts_from_file.find_contact()
            choice = int(input("Please choose contact to edit: "))
            for key, value in dict_with_number.items():
                if key == choice:
                    contact_for_edit = contacts_from_file[value]
                    table = [["1. Name", "2. Edit phone", "3. Delete phone", "4. Birthday", "5. Address", "6. Return"]]
                    print(data2rst(table))
                    part_of_contact_to_edit = int(input("Please choose field to edit: "))
                    if part_of_contact_to_edit == 1:
                        new_name = input("Enter new contact name: ")
                        contacts_from_file[new_name] = contacts_from_file[contact_for_edit.name.value]
                        del contacts_from_file[contact_for_edit.name.value]
                        contact_for_edit.name.value = new_name
                    elif part_of_contact_to_edit == 2:
                        old_phone = input("Enter old phone number: ")
                        new_phone = input("Enter new phone number: ")
                        contacts_from_file.edit_phone(contact_for_edit, old_phone, new_phone)
                    elif part_of_contact_to_edit == 3:
                        phone_to_delete = input("Enter phone to delete: ")
                        contacts_from_file.delete_phone(contact_for_edit, phone_to_delete)
                    elif part_of_contact_to_edit == 4:
                        new_birthday = input("Enter new Birthday date: ")
                        contact_for_edit.birthday = Birthday(new_birthday)
                    elif part_of_contact_to_edit == 5:
                        new_address = input("Enter new address: ")
                        contact_for_edit.address = Address(new_address)
            contacts_from_file.save_contacts_to_json_file("Output/contacts.json")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


    def edit_phone(contacts_from_file, phones, old_phone, new_phone):
        is_found_old_phone = False
        for i, p in enumerate(phones.phones.value):
            if p == old_phone:
                phones.phones.value[i] = new_phone
                is_found_old_phone = True
        if not is_found_old_phone:
            raise ValueError('Phone not found')


    def delete_phone(contacts_from_file, phones, phone_to_delete):
        for p in phones.phones.value:
            if p == phone_to_delete:
                phones.phones.value.remove(phone_to_delete)


    def delete_contact(contacts_from_file):
        try:
            dict_with_number = contacts_from_file.find_contact()
            delete_i = int(input("Please choose contact number: "))
            for key, value in dict_with_number.items():
                if key == delete_i:
                    del contacts_from_file.data[value]
            contacts_from_file.save_contacts_to_json_file("Output/contacts.json")
        except ValueError:
            print("Invalid input. Please enter a valid info for delete.")

    def show_all_contacts(contacts_from_file):
        console = Console()

        table = Table(title="Contact List", style="#e3db4b", header_style="#4bb0e3", title_style="#e3db4b")
        table.add_column("Name", style="#4bb0e3", min_width=10, max_width=50)
        table.add_column("Phones", style="#4bb0e3", min_width=10, max_width=50)
        table.add_column("Birthday", style="#4bb0e3", justify="center", min_width=10, max_width=50)
        table.add_column("Email", style="#4bb0e3", min_width=10, max_width=50)
        table.add_column("Address", style="#4bb0e3", min_width=10, max_width=50)
        list_contacts = []
        for key, value in contacts_from_file.data.items():
            name_c = value.name.value
            phones = value.phones.value
            birthday = value.birthday.value
            email = value.email.value
            address = value.address.value
            list_contacts.append((name_c, phones, birthday, email, address))
        for t in list_contacts:
            name_c = t[0]
            phones = ", ".join([str(p) for p in t[1]])
            birthday = t[2]
            email = t[3]
            address = t[4]
            table.add_row(name_c, phones, birthday, email, address)
            # table.add_row("-" * 50, "-" * 50, "-" * 50, "-" * 50, "-" * 50, style="#5cd15a")
        console.print(table)

    def days_to_birthday(self, name_c: Contact):
        today = datetime.now()
        if name_c.birthday:
            birthday_date = datetime.strptime(str(name_c.birthday), '%d.%m.%Y').replace(year=today.year)
            if today > birthday_date:
                birthday_date = birthday_date.replace(year=today.year + 1)
            delta = birthday_date - today
            return delta.days



        # with open(filename, 'w', newline='') as file:
        #     field_names = ['name', 'phones', 'birthday']
        #     writer = csv.DictWriter(file, fieldnames=field_names)
        #     writer.writeheader()
        #     for item in self.addressbooklist:
        #         writer.writerow({'name': item.name, 'phones': ', '.join([phone.value for phone in item.phones]),
        #                          'birthday': item.birthday})




# class AddressBookIterator():
#     def __init__(self, addressbook: AddressBook, index):
#         self.addressbook = addressbook
#         self.addressbooklist = list(addressbook.values())
#         self.index = index
#         self.counter = -1
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.counter += 1
#         if self.counter >= self.index:
#             raise StopIteration
#         record = self.addressbooklist[self.counter]
#         return record





#
# def read_from_file(self, filename):
#     with open(self.filename, 'r', newline='') as file:
#         reader = csv.DictReader(file)
#         result = []
#         for row in reader:
#             result.append(row)
#     return result

if __name__ == "__main__":
    book = ContactBook()

    user1 = Contact("Kate", "88888888 66565555", "31.12.1990", "kate@gmail.com", "Zaporizhzhia, Sobornyi 156")


    book.add_contact(user1)

    print(book.days_to_birthday(user1))

    # book.save_contacts_to_json_file("Output/contacts.json")
    # book.load_contacts_from_json_file("Output/contacts.json")

    for name, record in book.data.items():
        print(f'show all {record}')
