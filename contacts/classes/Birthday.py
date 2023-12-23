from datetime import datetime
from contacts.classes.Field import Field

R = "\033[91m"
RES = "\033[0m"


class Birthday(Field):

    @classmethod
    def is_valid_birthday(cls, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def __init__(self, value):
        if not Birthday.is_valid_birthday(value):
            print(f"{R}The birthday date don't added to record{RES}")
            raise ValueError("Not valid birthday date")
        super().__init__(value)

    def __set__(self, instance, new_value):
        if not Birthday.is_valid_birthday(new_value):
            raise ValueError(f"{R}Not valid birthday date{RES}")
        super().__set__(new_value)

if __name__ == '__main__':
    b = Birthday('2024-10-30')
    print(b)
