from Contacts import Contact
from collections import UserDict


class ContactBook(UserDict):
    def add_contact(self, contact: Contact):
        self.data[contact.name.value] = contact
        return self.data

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


# class AddressBookInFile:
#     def __init__(self, filename: str, addressbook: AddressBook):
#         if addressbook is None:
#             addressbook = []
#         self.filename = filename
#         self.addressbook = addressbook
#         self.addressbooklist = list(addressbook.values())

    # def save_to_file(self, filename):
    #     with open(self.filename, 'w', newline='') as file:
    #         field_names = ['name', 'phones', 'birthday']
    #         writer = csv.DictWriter(file, fieldnames=field_names)
    #         writer.writeheader()
    #         for item in self.addressbooklist:
    #             writer.writerow({'name': item.name, 'phones': ', '.join([phone.value for phone in item.phones]),
    #                              'birthday': item.birthday})
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

    user1 = Contact("Kate", "15/8/1990", "kate@gmail.com")
    user1.add_phone('888888888 88777dhydhy')
    print(user1.phones.value)

    book.add_contact(user1)

    for name, record in book.data.items():
        print(f'show all {record}')