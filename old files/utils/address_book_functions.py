from contacts.classes.Record import Record
from contacts.classes.AddressBook import AddressBook
from rich.console import Console

from decorators.input_errors import input_errors
from utils.sanitize_phone_nr import sanitize_phone_number


RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


console = Console()
def greeting():
    """Greet the user.

    Returns:
        str: A greeting message.
    """
    notification = (
        "Greetings! 🌟 Welcome to Cyber Sentinel's Helper App! 🚀\n\n"
        "Explore the possibilities at your fingertips:\n"
        "1. Open the address book and discover your contacts.\n"
        "2. Dive into your notes and uncover hidden insights.\n"
        "3. Manage your to-do list and conquer your tasks.\n"
        "4. Embark on a journey to sort folders in the directory.\n\n"
        "For a guiding light, type 'help' to reveal the magic commands. ✨"
    )


    return notification

def good_bye():
        """Bid farewell to the user.

        Returns:
            str: A farewell message.
        """
        return "Good bye!"

@input_errors
def load_address_book():
    try:
        return AddressBook.load_from_file('outputs/address_book.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading address book: {e}{RESET}")
        print(f"{YELLOW}Creating a new address book.{RESET}")
        return AddressBook()  # Creating a new instance


@input_errors
def add_contact(book, name, *phones):
    """Add a contact to the address book.

    Args:
        book (AddressBook): The address book instance.
        name (str): The name of the contact.
        *phones (str): One or more phone numbers to associate with the contact.

    Returns:
        str: A message indicating the result of the operation.
    """
    contact = book.find_name(name)
    if contact is None:
        contact = Record(name)
    phones = phones[0]
    for phone in phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.isdigit():
            contact.add_phone(sanitized_phone)
        else:
            return f"{RED}Phone {phone} is not valid and not added to {name}{RESET}"
    print(contact)
    book.add_record(contact)
    book.save_to_file('outputs/address_book.json')
    book.save_to_file('outputs/address_book.csv')
    return f"{GREEN}Contact {name} was added successfully!{RESET}"
