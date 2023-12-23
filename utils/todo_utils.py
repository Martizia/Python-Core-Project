from todo.todo_manager import ToDoRecord
from todo.todo_manager import ToDoBook
from decorators.input_errors import input_errors
from rich.console import Console
from rich.table import Table

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[43m"
PINK = "\033[95m"
RESET = "\033[0m"


filename = 'outputs/todo.json'
def load_todo_from_file():
    try:
        return ToDoBook.load_from_file('outputs/todo.json')
    except (FileNotFoundError, EOFError) as e:
        print(f"{RED}Error loading To Do List: {e}{RESET}")
        print(f"{YELLOW}Creating a new To Do entrance.{RESET}")
        return ToDoBook()  # Creating a new instance

def add_todo_record_to_file(todobook, task, begin, end, status, tags):
    print(tags)
    # list_tags = ToDoRecord.add_tags(tags)
    record = ToDoRecord(task, begin, end, status, tags)
    if record is None:
        record = ToDoRecord()
    todobook.add_to_do_record(record)

    todobook.save_to_file_todo('outputs/todo.json')
    return f"{GREEN}Task {task} was added successfully!{RESET}"


def show_todo(todobook, chunk_size = None):
    console = Console()

    table = Table(title="To Do List")
    table.add_column("Task", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("Begin Date", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("End Date", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("Status", style="#5cd15a", justify="center", min_width=10, max_width=50)
    table.add_column("Tags", style="#5cd15a", justify="center", min_width=10, max_width=50)
    list_todos = []
    for task, value in todobook.data.items():
        begin = value.begin
        end = value.end
        status = value.status
        tags = value.tags
        list_todos.append((task, begin, end, status, tags))
    num_records = len(list_todos)
    if chunk_size is None or chunk_size > num_records:
        chunk_size = num_records
    i = 0
    while num_records > i:
        chunk = list_todos[i:i + chunk_size]  # list_note[0:len(list_notes)]
        for record in chunk:
            task = record[0]
            begin = record[1]
            end = record[2]
            status = record[3]
            tags = ", ".join([str(tag) for tag in record[4]])
            table.add_row(task, begin, end, status, tags)
            if chunk_size is not None:
                i += chunk_size
            table.add_row("-" * 50, "-" * 50, "-" * 50, "-" * 50, "-" * 50, style="#5cd15a")

        if i < num_records:
            # Если chunk_size указано и есть еще записи, ожидаем Enter для продолжения
            console.print(table)
            input(f"{PINK}Press Enter to show the next chunk...{RESET}")
        else:
            i = num_records
    console.print(table)
