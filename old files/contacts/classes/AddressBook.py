import json
import csv
from collections import UserDict
from contacts.classes.Record import Record

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


class AddressBook(UserDict):
    """A class representing an address book that stores records."""

    def add_record(self, record):
        """Add a record to the address book.

        Args:
            record (Record): The record to add.

        Returns:
            None
        """
        if not isinstance(record, Record):
            record = Record(record)
        self.data[record.name.value] = record
    
    def del_record(self, name_to_delete):
        """Delete a record from the address book.

        Args:
            name_to_delete (str): The name of the record to delete.

        Returns:
            None
        """
        try:
            if name_to_delete in self.data:
                del self.data[name_to_delete]
                self.save_to_file('outputs/address_book.json')  # Save changes to file
                self.save_to_file('outputs/address_book.csv')
                print(f"{GREEN}Contact '{name_to_delete}' deleted successfully{RESET}")
            else:
                print(f"{RED}No contact found with the name '{name_to_delete}'{RESET}")
        except Exception as e:
            print(f"{RED}Error deleting contact: {e}{RESET}")

    def edit_contact(self, search_param):
        if len(search_param) < 3:
            print("Sorry, the search parameter must be at least 3 characters.")
            return

        matching_records = []
        for record in self.values():
            if search_param.lower() in record.name.value.lower() or search_param in record.get_all_phones():
                matching_records.append(record)

        if not matching_records:
            print("No records found for the given parameter.")
            return

        print("Matching records:")
        for i, record in enumerate(matching_records, start=1):
            print(f"{i}. {record.name.value}")

        try:
            choice = int(input("Enter the number of the contact to edit: "))
            if 1 <= choice <= len(matching_records):
                selected_record = matching_records[choice - 1]
                field_name = input("Enter the field to edit (name, birthday, email, status, note, phone, address): ")

                # Check if the entered field name is valid
                if field_name == "name":
                    new_value = input("Enter the new name: ")
                    selected_record.edit_name(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "birthday":
                    new_value = input("Enter the new birthday: ")
                    selected_record.edit_birthday(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "email":
                    new_value = input("Enter the new email: ")
                    selected_record.edit_email(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "status":
                    new_value = input("Enter the new status: ")
                    selected_record.edit_status(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "note":
                    new_value = input("Enter the new note: ")
                    selected_record.edit_note(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "phone":
                    old_phone = input("Enter the old phone: ")
                    new_phone = input("Enter the new phone: ")
                    selected_record.edit_phone(old_phone, new_phone)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                elif field_name == "address":
                    new_value = input("Enter the new address: ")
                    selected_record.edit_address(new_value)
                    print(f"Contact '{selected_record.name.value}' updated successfully.")
                else:
                    print("Invalid field name. Please enter a valid field name.")
                    return  # Add a return statement here to prevent saving in case of an invalid field

                # After editing, save the changes to the file
                self.save_to_file('outputs/address_book.json')
                self.save_to_file('outputs/address_book.csv')

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def find_name(self, name):
        """Find a record by name.

        Args:
            name (str): The name to search for.

        Returns:
            Record or None: The record if found, or None if not found.
        """
        if name in self.data:
            return self.data[name]
        else:
            return None

    def delete(self, name):
        """Delete a record by name.

        Args:
            name (str): The name of the record to delete.

        Returns:
            None
        """
        if name in self.data:
            del self.data[name]

    def get_records(self):
        """Return a list of all records in the address book.

        Returns:
            list: A list of records."""
        return list(self.values())

    def __str__(self):
        """Return a string representation of the address book.

        Returns:
            str: A string representation of the address book.
        """
        return '\n'.join([str(r) for r in self.values()])

    def iterator(self, chunk_size=1):
        """Iterate over records in the address book in chunks.

        Args:
            chunk_size (int): The number of records to yield in each iteration.

        Yields:
            list: A list of records.
        """
        records = list(self.values())
        i = 0
        while i < len(records):
            yield records[i:i + chunk_size]
            i += chunk_size

    @staticmethod
    def convert_to_serializable(address_book):
        """Converts the AddressBook object to a serializable format.

            Args:
                address_book (AddressBook): The AddressBook object to convert.

            Returns:
                dict: A dictionary containing the serialized data.
            """
        serializable_data = {}
        for key, record in address_book.items():
            serializable_data[key] = {
                "name": record.name.value,
                "phones": record.get_all_phones(),
                "birthday": str(record.birthday) if record.birthday else None,
                "email": record.email.value if record.email else None,
                "address": record.address.value if record.address else None,
                "status": record.status.value if record.status else None,
                "note": record.note.value if record.note else None
            }
        return serializable_data

    def save_to_file(self, file_name):
        """
        Save the instance to a JSON file and a CSV file.

        Args:
            file_name (str): The name of the file to save the instance. The extension will determine the format.

        Returns:
            None
        """
        data_to_serialize = AddressBook.convert_to_serializable(self)

        # Determine the file format based on the extension
        file_format = file_name.split('.')[-1].lower()

        if file_format == 'json':
            with open(file_name, 'w', encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file,  indent=4)
        elif file_format == 'csv':
            with open(file_name, 'w', newline='', encoding="utf-8") as csv_file:
                csv_writer = csv.writer(csv_file)

                # Write the header
                header = ["name", "phones", "birthday", "email", "address", "status", "note"]
                csv_writer.writerow(header)

                # Write each record
                for record in self.values():
                    csv_writer.writerow([
                        record.name.value,
                        ';'.join(p.value for p in record.phones),
                        str(record.birthday) if record.birthday else "",
                        record.email.value if record.email else "",
                        record.address.value if record.address else "",
                        record.status.value if record.status else "",
                        record.note.value if record.note else ""
                    ])
        else:
            raise ValueError(f"Unsupported file format: {file_format}")

    @staticmethod
    def load_from_file(file_name):
        """
        Load an instance from a JSON file.

        Args:
            file_name (str): The name of the file to load the instance from.

        Returns:
            AddressBook: The loaded instance.
        """
        try:
            with open(file_name, 'r', encoding="utf-8") as f:
                data = json.load(f)
                address_book = AddressBook()
                for name, record_data in data.items():
                    new_record = Record(record_data.get('name', ''))
                    phones = record_data.get('phones', [])
                    birthday = record_data.get('birthday', None)
                    email = record_data.get('email', None)
                    address = record_data.get('address', None)
                    status = record_data.get('status', None)
                    note = record_data.get('note', None)
                    for phone in phones:
                        new_record.add_phone(phone)
                    if birthday == 'null':
                        birthday = None
                    if birthday is not None:
                        new_record.add_birthday(birthday)
                    if email == 'null':
                        email = None
                    if email is not None:
                        new_record.add_email(email)
                    if status == 'null':
                        status = None
                    if status is not None:
                        new_record.add_status(status)
                    if note == 'null':
                        note = None
                    if note is not None:
                        new_record.add_note(note)
                    if address == 'null':
                        address = None
                    if address is not None:
                        new_record.add_address(address)
                    address_book.add_record(new_record)
                return address_book
        except (FileNotFoundError, EOFError):
            # Handle the case where the file is not found or empty
            return AddressBook()

    def find(self, param):
        """
        Find records that match the given parameter.

        Args:
            param (str): The search parameter.

        Returns:
            str: A string containing the matching records, separated by newline.

        Note:
            If the search parameter is less than 3 characters, it returns an error message.
        """
        if len(param) < 3:
            return "Sorry, the search parameter must be at least 3 characters."

        result = []

        for i, record in enumerate(self.values()):

            if param.lower() in record.name.value.lower():
                result.append(str(record))
                result.append('=' * 30)
            elif param.isdigit():
                matching_phones = [phone for phone in record.get_all_phones() if param in phone]
                if matching_phones:
                    result.append(str(record))
                    result.append('=' * 30)
            elif record.birthday and param in str(record.birthday):
                result.append(str(record))
                result.append('=' * 30)
            elif record.email and param.lower() in record.email.value.lower():
                result.append(str(record))
                result.append('=' * 30)
            elif record.address and param.lower() in record.address.value.lower():
                result.append(str(record))
                result.append('=' * 30)
            elif record.status and param.lower() in record.status.value.lower():
                result.append(str(record))
                result.append('=' * 30)
            elif record.note and param.lower() in record.note.value.lower():
                result.append(str(record))
                result.append('=' * 30)

        if not result:
            return "No records found for the given parameter."


        return '\n'.join(result)

    def delete_contact(self):
        delete_info = input("Enter the search parameter: ").lower()
        result_list = []
        for record in self.data.values():
            search_by_name = record.name.value.lower().find(delete_info)
            search_by_phones = str([p.value.lower() for p in record.phones]).find(delete_info)
            if search_by_name > -1 or search_by_phones > -1:
                result_list.append(record)
        dict_with_number = dict(zip([i+1 for i in range(len(result_list))], [i.name.value for i in result_list]))
        print(dict_with_number)
        delete_i = int(input('Please choose contact number to delete? '))
        for key, value in dict_with_number.items():
            if key == delete_i:
                del self.data[value]
        
        self.save_to_file('outputs/address_book.json')



if __name__ =='__main__':
    print("Loading address book from file...")
    book = AddressBook.load_from_file('../../outputs/address_book.json')
    print(book.find('sergio'))


