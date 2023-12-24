

def edit_contact(book):
    search_param = input("Enter the search parameter: ")
    book.edit_contact(search_param)

def edit_notes(notesbook):
    notesbook.search_notes_record()

def edit_todo_list(todobook):
    todobook.edit_todo()


