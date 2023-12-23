import os
from contacts.classes.AddressBook import AddressBook
from notes.note_manager import Notes
from todo.todo_manager import ToDoBook
from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.completion import WordCompleter
from decorators.input_errors import input_errors
from utils.sanitize_phone_nr import sanitize_phone_number
from rich.console import Console
from rich.table import Table
from file_manager.norton_commander import display_directory_contents
from utils.help import help
from utils.address_book_functions import add_contact, greeting, good_bye, load_address_book
from utils.notes_utils import load_notes_from_file, add_note_record_to_notes, show_notes
from utils.todo_utils import load_todo_from_file, add_todo_record_to_file, show_todo
from utils.edit_helper import edit_contact, edit_notes, edit_todo_list


# I'm applying the decorator directly, overwriting the function
sanitize_phone_number = input_errors(sanitize_phone_number)

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


#  ================================

class Bot:
    # noinspection PyTypeChecker
    def __init__(self):
        self.__known_commands = (
            "help", "add-contact", "add-note", "add-todo", 'add-tag', "edit-contact", "edit-note", "edit-todo",
            "find_all_in_contacts", "delete-contact", "delete-note", "delete-todo", 'delete-tag-in-todo', "show-contact", "show-notes", "show-todos", "hello",
            "days-to-birthday", "file-manager")
        self.__exit_commands = ("goodbye", "close", "exit", ".")
        self.book = load_address_book()
        self.notesbook = load_notes_from_file()
        self.todobook = load_todo_from_file()
        self.session = PromptSession(
            history=FileHistory('outputs/history.txt'),
            # completer=WordCompleter(self.__known_commands + self.__exit_commands),
            completer=self.get_completer(),
        )

    def get_completer(self):
        return WordCompleter(self.__known_commands + self.__exit_commands)

    @input_errors
    def showall(self, chunk_size = None):
        """Display all contacts in the address book.

        Returns:
            None
        """
        console = Console()

        table = Table(title="Address Book")
        table.add_column("Name", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Phones", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Birthday", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Email", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Address", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Status", style="blue", justify="center", min_width=10, max_width=30)
        table.add_column("Note", style="blue", justify="center", min_width=10, max_width=30)

        records = list(self.book.values())
        # print(records[1].phones)
        # print(records[1].name)
        num_records = len(records)
        if chunk_size is None or chunk_size > num_records:
            chunk_size = num_records
        i = 0
        while i < num_records:
            chunk = records[i:i + chunk_size]
            # print(len(chunk))
            for record in chunk:
                name = record.name.value
                phones = "; ".join([str(phone) for phone in record.phones])
                birthday = str(record.birthday) if record.birthday else "N/A"
                email = record.email.value if record.email else "N/A"
                address = record.address.value if record.address else "N/A"
                status = record.status.value if record.status else "N/A"
                note = record.note.value if record.note else "N/A"

                table.add_row(name, phones, birthday, email, address, status, note)

            if chunk_size is not None:
                table.add_row("=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30, "=" * 30)
                i += chunk_size

                if i < num_records:
                    # Если chunk_size указано и есть еще записи, ожидаем Enter для продолжения
                    console.print(table)
                    input(f"{PINK}Press Enter to show the next chunk...{RESET}")
            else:
                i = num_records

        console.print(table)


    @input_errors
    def get_phone(self, name):
        """Retrieve the phone numbers associated with a contact.

            Args:
                name (str): The name of the contact.

            Returns:
                str: A message containing the contact's name and phone numbers.
            """
        if name in self.book.data:
            record = self.book.data[name]
            return f"{GREEN}{name} was found with phones - {'; '.join(record.get_all_phones())}{RESET}"
        else:
            return f"{RED}There is no contact with this name!{RESET}"

    @input_errors
    def days_to_birthday(self, name):
        """Calculate the number of days to the next birthday for a contact.

        Args:
            name (str): The name of the contact.

        Returns:
            str: A message indicating the number of days to the next birthday or an error message.
        """
        contact = self.book.find_name(name)

        if contact is None:
            return f"{RED}There is no contact with the name '{name}'{RESET}"

        if contact.birthday:
            days = contact.days_to_birthday()
            if days > 0:
                return f"{GREEN}{name} has {days} days before their next birthday{RESET}"
            elif days == 0:
                return f"{GREEN}{name}'s birthday is today!{RESET}"
            else:
                # will never be executed.... because of Record class....
                return f"{GREEN}{name}'s birthday is in {-days} days{RESET}"
        else:
            return f"{RED}{name} has no birthday set{RESET}"


    def run(self):
        """Main function for user interaction.

               Returns:
                   None
               """
        try:
            book = AddressBook.load_from_file('outputs/address_book.json')
            notesbook = Notes.load_from_file('outputs/notes.json')

        except (FileNotFoundError, EOFError) as e:
            print(f"{RED}Error loading address book: {e}{RESET}")
            print(f"{YELLOW}Creating a new address book.{RESET}")
            book = AddressBook()  # Creating a new instance
        while True:
            print(f"{YELLOW}If don't know the commands, enter 'help' please{RESET}")
            user_input = self.session.prompt("... ")
            if user_input == "":
                print(f"{RED}Empty input !!!{RESET}")
                continue
            input_data = user_input.split()
            input_command = input_data[0].lower()
            if input_command in self.__exit_commands:
                print(f"{RED}{good_bye()}{RESET}")
                break
            elif input_command in self.__known_commands:
                match input_command:
                    case 'help':
                        help()
                    case 'hello':
                        print(f"{BLUE}{greeting()} {RESET}")
                    case "find_all_in_contacts":
                        try:
                            search_param = input_data[1]
                            result = book.find(search_param)
                            print(f"{GREEN}Matching records:\n{result}{RESET}")
                        except IndexError:
                            print(f"{RED}You have to provide a search parameter after 'find'.{RESET}")

                    case "file-manager":
                        try:
                            start_path = os.path.expanduser("~")
                            display_directory_contents(start_path)
                            print(f"{GREEN}Folder was sorted{RESET}")
                        except Exception as e:
                            # print(f"{RED}Error: '{e}'{RESET}")
                            pass
                    case "show-contact":
                        try:
                            self.book = AddressBook.load_from_file('outputs/address_book.json')
                            self.showall(int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case "show-notes":
                        try:
                            self.notesbook = Notes.load_from_file('outputs/notes.json')
                            show_notes(self.notesbook, int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case "show-todos":
                        try:
                            self.todobook = ToDoBook.load_from_file('outputs/todo.json')
                            show_todo(self.todobook, int(input_data[1]) if len(input_data) > 1 else None)
                        except IndexError:
                            print(f"{RED}You have to put correct chunk size. Example: \nshow <chunk size>{RESET}")

                    case 'add-contact':
                        try:
                            print(add_contact(self.book, input_data[1], input_data[2:]))
                        except IndexError:
                            print(f"{RED}You have to put name(or name-surname) and phone(s) after add-contact. Example: \n"
                                  f"add-contact <name> <phone1> <phone2> ...{RESET}")
                    case 'add-note':
                        if len(input_data) >= 2:
                            print(add_note_record_to_notes(self.notesbook, input_data[1], input_data[2:]))
                        else:
                            print("Invalid input. Usage: add-note <title> <note1> <note2> ...")

                    case 'add-todo':
                        if len(input_data) >= 6:
                            print(add_todo_record_to_file(self.todobook, input_data[1], input_data[2], input_data[3], input_data[4], input_data[5:]))
                        else:
                            print("Invalid input. Usage: add-todo <title> <begin date> <end date> <status> <tags> ...")

                    case 'add-tag':
                        self.todobook.add_tag()

                    case 'edit-contact':
                        edit_contact(self.book)

                    case 'edit-note':
                        edit_notes(self.notesbook)

                    case 'edit-todo':
                        edit_todo_list(self.todobook)
                            
                    case 'delete-contact':
                        self.book.delete_contact()
                    
                    case 'delete-note':
                        self.notesbook.delete_note()

                    case 'delete-todo':
                        self.todobook.delete_task()

                    case 'delete-tag-in-todo':
                        self.todobook.delete_tag_in_todo()

                    case "days-to-birthday":
                        if len(input_data) < 2:
                            print(
                                f"{RED}You need to provide a name after 'days-to-birthday'. "
                                f"Example: days-to-birthday <name>{RESET}"
                            )
                        else:
                            print(self.days_to_birthday(input_data[1]))


            else:
                print(f"{RED}Don't know this command{RESET}")

