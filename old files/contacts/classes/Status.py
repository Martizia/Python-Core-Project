from contacts.classes.Field import Field

class Status(Field):
    """A class representing the status of a Record in Address Book."""

    VALID_STATUSES = ["family", "work", "friends", "neighbor", "classmate", "colleague"]

    def __init__(self, value=None):
        if value is None:
            super().__init__("")
        else:
            self.validate_status(value)
            super().__init__(value)

    @staticmethod
    def is_valid_status(value):
        """Check if the status is valid."""
        return value.lower() in Status.VALID_STATUSES

    def validate_status(self, value):
        """Validate and set the status."""
        if not self.is_valid_status(value):
            raise ValueError(f"Invalid status: {value}. Valid statuses are {', '.join(Status.VALID_STATUSES)}")
