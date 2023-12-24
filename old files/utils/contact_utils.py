from contacts.classes.Name import Name
from contacts.classes.Email import Email
from contacts.classes.Address import Address
from contacts.classes.Note import Note
from contacts.classes.Status import Status
from decorators.input_errors import input_errors

@input_errors
def edit_name(record, new_value):
    """Редагує ім'я контакту.

    Args:
        record (Record): Об'єкт класу Record.
        new_value (str): Нове ім'я контакту.
    """
    record.name = Name(new_value)

@input_errors
def add_email(record, value):
    """Додає електронну пошту контакту.

    Args:
        record (Record): Об'єкт класу Record.
        value (str): Рядок з електронною поштою контакту.
    """
    record.email = Email(value)

@input_errors
def edit_email(record, new_value):
    """Редагує електронну пошту контакту.

    Args:
        record (Record): Об'єкт класу Record.
        new_value (str): Нова електронна пошта контакту.
    """
    record.email = Email(new_value)

@input_errors
def add_address(record, value):
    """Додає адресу контакту.

    Args:
        record (Record): Об'єкт класу Record.
        value (str): Рядок з адресою контакту.
    """
    record.address = Address(value)

@input_errors
def edit_address(record, new_value):
    """Редагує адресу контакту.

    Args:
        record (Record): Об'єкт класу Record.
        new_value (str): Нова адреса контакту.
    """
    record.address = Address(new_value)

@input_errors
def add_note(record, value):
    """Додає примітку до контакту.

    Args:
        record (Record): Об'єкт класу Record.
        value (str): Рядок з приміткою до контакту.
    """
    record.note = Note(value)

@input_errors
def edit_note(record, new_value):
    """Редагує примітку контакту.

    Args:
        record (Record): Об'єкт класу Record.
        new_value (str): Нова примітка контакту.
    """
    record.note = Note(new_value)

@input_errors
def add_status(record, value):
    """Додає статус контакту.

    Args:
        record (Record): Об'єкт класу Record.
        value (str): Рядок зі статусом контакту.
    """
    record.status = Status(value)

@input_errors
def edit_status(record, new_value):
    """Редагує статус контакту.

    Args:
        record (Record): Об'єкт класу Record.
        new_value (str): Новий статус контакту.
    """
    record.status = Status(new_value)
