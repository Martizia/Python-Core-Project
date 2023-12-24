from datetime import datetime, date
import re


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        while True:
            if value:
                self.value = value
                break
            else:
                self.value = input("Empty field! Please provide at least one symbol as a name: ")
                break


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        while True:
            self.value = []
            invalid_phone = ''
            if value:
                self.values = value
                # print(self.values.split(' '))
            else:
                self.values = input("Enter phone number (not more than 15 digits): ")
            try:
                for phone in self.values.split(' '):
                    if len(phone) <= 15 and phone.isdigit():
                        self.value.append(phone)
                    else:
                        invalid_phone = phone
                        raise ValueError
            except ValueError:
                print(f"Phone {invalid_phone} has incorrect format!")
            break


class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date(dd/mm/YYYY): ")
            try:
                if datetime.strptime(value, '%d/%m/%Y'):
                    date_value = datetime.strptime(self.value.strip(), '%d/%m/%Y')
                    self.value = datetime.strftime(date_value, '%d.%m.%Y')
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')


class Email(Field):
    def __init__(self, value=''):
        super().__init__(value)
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
                if re.fullmatch(regex, self.value) or self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')
                break


class Address(Field):
    def __init__(self, value):
        super().__init__(value)
        while True:
            if value:
                self.value = value
                break
            else:
                self.value = input("Empty field! Please provide at least one symbol as an address: ")
                break


class Contact:
    def __init__(self, name, birthday='', email='', address=''):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None
        self.email = Email(email) if email else None
        self.address = Address(address) if address else None

    def add_phone(self, phone):
        # if not isinstance(phone, Phone):
        #     phone = Phone(phone)
        self.phones = Phone(phone)


    def edit_phone(self, old_phone, new_phone):
        is_found_old_phone = False
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                is_found_old_phone = True
        if not is_found_old_phone:
            raise ValueError('Phone not found')

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
        return self.phones

    # def find_phone(self, phone):
    #     for p in self.phones:
    #         if p.value == phone:
    #             return p

    def days_to_birthday(self):
        today = datetime.now()
        if self.birthday:
            birthday_date = datetime.strptime(str(self.birthday), '%d/%m/%Y').replace(year=today.year)
            if today > birthday_date:
                birthday_date = birthday_date.replace(year=today.year + 1)
            delta = birthday_date - today
            return delta.days
        else:
            return None

    def add_birthday(self, value):
        self.birthday = Birthday(value)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(p for p in self.phones.value)}, birthday is {self.birthday}"