from datetime import datetime

from contacts.classes.Name import Name
from contacts.classes.Phone import Phone
from contacts.classes.Birthday import Birthday
from contacts.classes.Email import Email
from contacts.classes.Address import Address
from contacts.classes.Status import Status
from contacts.classes.Note import Note
from utils.record_func import days_to_birthday, add_birthday, edit_birthday
from utils.record_func import add_phone, remove_phone, edit_phone
from utils.record_func import find_phone, get_all_phones
from utils.contact_utils import edit_name, add_email, edit_email, add_address, edit_address
from utils.contact_utils import add_note, edit_note, add_status, edit_status


class Record:
    """Клас Record представляє запис контакту в телефонній книзі.

            Attributes:
                self.name (Name): Ім'я контакту.
                self.phones (list of Phone): Список телефонних номерів контакту.
                self.birthday (Birthday): Дата народження контакту.

            Methods:
                days_to_birthday(): Повертає кількість днів до наступного дня народження контакту,
                якщо вказана дата народження.
                add_birthday(value): Додає дату народження контакту.
                edit_birthday(new_value): Змінює дату народження контакту.
                add_phone(phone): Додає телефонний номер контакту.
                remove_phone(phone): Видаляє телефонний номер контакту.
                edit_phone(old_phone, new_phone): Редагує існуючий телефонний номер контакту.
                find_phone(phone): Знаходить телефонний номер контакту за значенням номера.
                get_all_phones(): Повертає список всіх телефонних номерів контакту.
            """

    def __init__(self, name, birthday=None, email=None, address = None, status=None, note=None):
        self.name = Name(name)
        self.birthday = Birthday(birthday) if birthday else None
        self.phones = []
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None
        self.status = Status(status) if status else None
        self.note = Note(note) if note else None


    def edit_name(self, new_name):
        self.name = Name(new_name)

    def days_to_birthday(self):
        return days_to_birthday(self.birthday)

    def add_birthday(self, value):
        add_birthday(self, value)

    def edit_birthday(self, new_value):
        edit_birthday(self, new_value)

    def add_phone(self, phone):
        add_phone(self, phone)

    def remove_phone(self, phone):
        remove_phone(self, phone)

    def edit_phone(self, old_phone, new_phone):
        edit_phone(self, old_phone, new_phone)

    def find_phone(self, phone):
        return find_phone(self, phone)

    def get_all_phones(self):
        return get_all_phones(self)

    def add_email(self, email):
        return  add_email(self, email)

    def edit_email(self, new_email):
        edit_email(self,new_email)


    def add_address(self, address):
        add_address(self, address)

    def edit_address(self, new_address):
        edit_address(self, new_address)

    def add_note(self, note):
        add_note(self, note)

    def edit_note(self, new_note):
        edit_note(self, new_note)

    def add_status(self, status):
        add_status(self, status)

    def edit_status(self, new_status):
        edit_status(self, new_status)

    def __str__(self):
        return (
            f"Contact name: {self.name.value},\n"
            f"birthday: {self.birthday},\n"
            f"phones: {'; '.join(p.value for p in self.phones)},\n"
            f"email: {self.email},\n"
            f"address: {self.address},\n"
            f"status: {self.status},\n"
            f"note: {self.note}"
        )
if __name__ =='__main__':
    pass