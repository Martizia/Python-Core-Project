
class Field:
    """Initialize a new Field instance with the given value.

        Args:
            value: The initial value to store in the field.

        Returns:
            None
        """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        """Return a string representation of the field's value.

                Returns:
                    str: A string representation of the stored value.
                """
        return str(self.value)

    
    def __get__(self, instance, owner):
        """Get the current value stored in the field.

                Returns:
                    The current value stored in the field.
                """
        return self.value

    
    def __set__(self, instance, new_value):
        """Set a new value in the field.

                Args:
                    new_value: The new value to store in the field.

                Returns:
                    None
                """
        self.value = new_value
