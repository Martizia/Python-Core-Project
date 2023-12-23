from contacts.classes.Field import Field

class Note(Field):
    """class for validate note field"""

    def __init__(self, value):
        if not self.is_valid_note(value):
            raise ValueError("Note must be at least one character long")
        super().__init__(value)

    @staticmethod
    def is_valid_note(value):
        """return boolean from check"""
        return len(value.strip()) > 0
