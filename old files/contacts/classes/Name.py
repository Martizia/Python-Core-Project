from contacts.classes.Field import Field


class Name(Field):
    """class for validate name field"""

    def __init__(self, value):
        if not self.is_valid_name(value):
            raise ValueError("Name must be at least one character long")
        super().__init__(value)

    @staticmethod
    def is_valid_name(value):
        """return boolean from check"""
        return len(value.strip()) > 0
    