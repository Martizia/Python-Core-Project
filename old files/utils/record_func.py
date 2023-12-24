from datetime import datetime
from contacts.classes.Birthday import Birthday
from contacts.classes.Phone import Phone
from decorators.input_errors import input_errors

@input_errors
def days_to_birthday(birthday):
    today = datetime.now()
    if birthday:
        birthday_date = datetime.strptime(str(birthday), '%Y-%m-%d').replace(year=today.year)
        if today > birthday_date:
            birthday_date = birthday_date.replace(year=today.year + 1)
        delta = birthday_date - today
        return delta.days
    else:
        return None
@input_errors
def add_birthday(record, value):
    record.birthday = Birthday(value)

@input_errors
def edit_birthday(record, new_value):
    if not new_value:
        record.birthday = None
    else:
        record.birthday = Birthday(new_value)

@input_errors
def add_phone(record, phone):
    """Додає телефонний номер контакту.

    Args:
        record (Record): Об'єкт класу Record.
        phone (str): Телефонний номер для додавання.
    """
    if not isinstance(phone, Phone):
        phone = Phone(phone)
    record.phones.append(phone)

@input_errors
def remove_phone(record, phone):
    """Видаляє телефонний номер контакту.

    Args:
        record (Record): Об'єкт класу Record.
        phone (str): Телефонний номер для видалення.
    """
    if phone in [p.value for p in record.phones]:
        record.phones = [p for p in record.phones if p.value != phone]

@input_errors
def edit_phone(record, old_phone, new_phone):
    """Редагує існуючий телефонний номер контакту.

    Args:
        record (Record): Об'єкт класу Record.
        old_phone (str): Старий телефонний номер для редагування.
        new_phone (str): Новий телефонний номер.

    Raises:
        ValueError: Якщо старий телефонний номер не знайдено.
    """
    is_found_old_phone = False
    for i, p in enumerate(record.phones):
        if p.value == old_phone:
            record.phones[i] = Phone(new_phone)
            is_found_old_phone = True
    if not is_found_old_phone:
        raise ValueError('Phone not found')

@input_errors
def find_phone(record, phone):
    """Знаходить телефонний номер контакту за значенням номера.

    Args:
        record (Record): Об'єкт класу Record.
        phone (str): Телефонний номер для пошуку.

    Returns:
        Phone or None: Знайдений телефоний номер або None, якщо не знайдено.
    """
    for p in record.phones:
        if p.value == phone:
            return p

@input_errors
def get_all_phones(record):
    """Повертає список всіх телефонних номерів контакту.

    Args:
        record (Record): Об'єкт класу Record.

    Returns:
        list of str: Список телефонних номерів контакту.
    """
    result = [p.value for p in record.phones]
    return result

