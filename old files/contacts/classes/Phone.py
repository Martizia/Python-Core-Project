from contacts.classes.Field import Field


class Phone(Field):
    """class for validate phone number"""

    @staticmethod
    def is_valid_phone(value):
        """return boolean from check"""
        return value.isdigit() and 15 >= len(value) >= 10

    def __init__(self, value):
        if not Phone.is_valid_phone(value):
            raise ValueError("Phone number must be a ten digit string of digits")
        super().__init__(value)

    def __set__(self, instance, value):
        if not Phone.is_valid_phone(value):
            raise ValueError("Phone number must be a ten digit string of digits")
        super().__set__(instance, value)

