from rich.console import Console
from rich.table import Table

def help():
    console = Console()
    table = Table(title="Help", style="#e3db4b", header_style="#4bb0e3", title_style="#e3db4b")
    table.add_column("Command", style="#4bb0e3", min_width=10, max_width=50)
    table.add_column("Description", style="#4bb0e3", min_width=10, max_width=50)
    rows = [
        ("Contacts", ""),
        ("- Add", "Add new contact"),
        ("- Edit", "Edit name, phone, Birthday date, address and also delete phone"),
        ("- Find", "Search through every field in contacts"),
        ("- Delete", "Delete contact"),
        ("- Show all", "Show all existing contacts in Contact Book"),
        ("- Day's till Birthday", "Calculate day's till Birthday for selected contact"),
        ("Notes", ""),
        ("- Add", "Add new note"),
        ("- Edit", "Edit title, text, tags and also add and delete tags"),
        ("- Find", "Search through every field in notes"),
        ("- Delete", "Delete note"),
        ("- Show all", "Show all existing notes in Note Book"),
        ("Help", "Open guide with description of all commands"),
        ("Exit", "End of work and exit from app")
    ]

    for i, (command, description) in enumerate(rows):
        table.add_row(command, description)

    console.print(table)