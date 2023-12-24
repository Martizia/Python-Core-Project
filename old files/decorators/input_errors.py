RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"


def input_errors(func):
    """Decorator to handle input errors.

        Args:
            func (function): The function to decorate.

        Returns:
            function: The decorated function that handles input errors.
        """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"{RED}{e}.{RESET}"
        except ValueError as e:
            return f"{RED}{e}.{RESET}"
        except IndexError as e:
            return f"{RED}{e}.{RESET}"

    return wrapper
