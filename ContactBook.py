from Contacts import Contact
from collections import UserDict
import json


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
        # filename = "Output/contacts.json"
        data_to_serialize = self.convert_to_serializable_contact()
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file, indent=4)
                json_file.write('\n')
            print(f'Contacts saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving contacts to {filename}: {e}')

    def load_contacts_from_json_file(self, filename):
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

        # with open(filename, 'w', newline='') as file:
        #     field_names = ['name', 'phones', 'birthday']
        #     writer = csv.DictWriter(file, fieldnames=field_names)
        #     writer.writeheader()
        #     for item in self.addressbooklist:
        #         writer.writerow({'name': item.name, 'phones': ', '.join([phone.value for phone in item.phones]),
        #                          'birthday': item.birthday})

    # def find(self, name):
    #     if name in self.data:
    #         return self.data[name]
    #     else:
    #         return None

    # def find_partial(self):
    #     self.dict = list(self.data)
    #     symbols = input('Print letters or numbers to find contact: ')
    #
    #     for contact_name in self.dict:
    #         if symbols in contact_name:
    #             print(self.data[contact_name])
    #         else:
    #             for contact_phones in self.data[contact_name].phones:
    #                 list_phones = contact_phones.value
    #                 if symbols in list_phones:
    #                     print(self.data[contact_name])

    # def delete(self, name):
    #     if name in self.data:
    #         del self.data[name]


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

    print(user1.days_to_birthday())

    book.save_contacts_to_json_file("Output/contacts.json")
    book.load_contacts_from_json_file("Output/contacts.json")

    for name, record in book.data.items():
        print(f'show all {record}')
