from notes.note_manager import NotesRecord
from notes.note_manager import Notes
from decorators.input_errors import input_errors
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


filename = 'outputs/notes.json'
def load_notes_from_file():
    try:
        return Notes.load_from_file('outputs/notes.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading address book: {e}{RESET}")
        print(f"{YELLOW}Creating a new address book.{RESET}")
        return Notes()  # Creating a new instance

@input_errors
def add_note_record_to_notes(notesbook, title, notes=None):
    """Add a note to the notes book.

    Args:
        book (NotesBook): The NotesBook instance.
        title (str): The title of the note.
        *notes (str): One or more notes to associate with the note.

    Returns:
        str: A message indicating the result of the operation.
    """
    # notes_list = []
    # notes =notes[0]
    # notes1 = ' '.join(notes)
    # notes_list.append(notes[0])
    record = NotesRecord(title, notes)
    if record is None:
        record = NotesRecord()
    notesbook.add_note_record(record)
    notesbook.save_to_file_notes('outputs/notes.json')
    return f"{GREEN}Note {title} was added successfully!{RESET}"


# def add_note_to_book(book):
#     title = input("Enter the title for the note: ")
#     note = input("Enter a note to add: ")
#     note_record = NotesRecord(title)
#     note_record.add_notes(note)
#     print('note_record from notas_utils: ', note_record)
#     book.add_note_record(note_record)
#     print(f'Note "{title}" has been added successfully.')


def edit_note_in_book(book):
    title = input("Enter the title of the note to edit: ")
    if title in book.data:
        note_record = book.data[title]
        new_title = input(f"Enter a new title for the note (press Enter to keep '{title}'): ")
        new_notes = input(f"Enter new notes for the note (press Enter to keep the existing notes): ")
        note_record.edit_notes(new_title or title, new_notes)
        print(f'Note "{title}" has been edited successfully.')
    else:
        print(f'Note "{title}" not found in the book.')


def delete_note_from_book(book):
    title = input("Enter the title of the note to delete: ")
    book.delete_note_record(title)

def show_notes(notebook, chunk_size = None):
    """Display all contacts in the address book.

    Returns:
        None
    """
    console = Console()

    table = Table(title="Notes Book")
    table.add_column("Title", style="blue", justify="center", min_width=10, max_width=50)
    table.add_column("Notes", style="blue", justify="center", min_width=10, max_width=50)
    list_notes = []
    for title, value in notebook.data.items():
        # notes = value.notes[0][0]
        notes = value.notes
        list_notes.append((title,notes))
    num_records = len(list_notes)
    if chunk_size is None or chunk_size > num_records:
        chunk_size = num_records
    i = 0
    while num_records > i:
        chunk = list_notes[i:i + chunk_size]  # list_note[0:len(list_notes)]
        # print("CHANKK:  ", chunk)
        for record in chunk:
            title = record[0]
            # notes_to_print = []
            # notes = record[1]

            # for note in record[1]:
            #     notes_to_print.extend(note)
            notes = ", ".join([str(notes) for notes in record[1]])
            table.add_row(title, notes)
            if chunk_size is not None:
                table.add_row("=" * 50, "=" * 50)
            i += chunk_size

        if i < num_records:
            # Если chunk_size указано и есть еще записи, ожидаем Enter для продолжения
            console.print(table)
            input(f"{PINK}Press Enter to show the next chunk...{RESET}")
        else:
            i = num_records
    console.print(table)

