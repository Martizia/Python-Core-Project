import json
from rich.console import Console
from dashtable import data2rst
from rich.table import Table
from Notes import Note
from collections import UserDict


class NoteBook(UserDict):
    def add_note(self, note: Note):
        self.data[note.note_title] = note
        return self.data

    def convert_to_serializable_note(self):
        serializable_data = {}
        for key, note in self.data.items():
            serializable_data[str(key)] = {
                "title": note.note_title,
                "text": note.note_text,
                "tags": note.note_tags
            }
        return serializable_data

    def save_notes_to_json_file(self, filename):
        data_to_serialize = self.convert_to_serializable_note()
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file, indent=4)
                json_file.write('\n')
            print(f'Notes saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving notes to {filename}: {e}')

    def load_notes_from_json_file(filename):
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            loaded_notes = NoteBook()
            for key, value in data.items():
                title = key
                text = value["text"]
                tags = " ".join(tag for tag in value["tags"])
                note_record = Note(title, text, tags)
                loaded_notes.add_note(note_record)
            print(f'Notes loaded from {filename} successfully.')
            return loaded_notes
        except Exception as e:
            print(f'Error loading from {filename}: {e}')
            return NoteBook()  # Return a new instance in case of an error

    def find_note(notes_from_file):
        try:
            search_info = input("Enter info for search: ").lower()
            result_list = []
            for item in notes_from_file.values():
                search_by_title = item.note_title.lower().find(search_info)
                search_by_text = item.note_text.lower().find(search_info)
                search_by_tags = str([tag.lower() for tag in item.note_tags]).find(search_info)
                if search_by_title > -1 or search_by_text > -1 or search_by_tags > -1:
                    result_list.append(item)
            dict_with_number = dict(zip([i + 1 for i in range(len(result_list))], [i.note_title for i in result_list]))
            print(dict_with_number)
            return dict_with_number
        except ValueError:
            print("Invalid input. Please enter a valid info for search.")

    def delete_note(notes_from_file):
        try:
            dict_with_number = notes_from_file.find_note()
            delete_i = int(input("Please choose note number: "))
            for key, value in dict_with_number.items():
                if key == delete_i:
                    del notes_from_file.data[value]
            notes_from_file.save_notes_to_json_file("Output/notes.json")
        except ValueError:
            print("Invalid input. Please enter a valid info for delete.")

    def show_all_notes(notes_from_file):
        console = Console()

        table = Table(title="Notes List", style="#e3db4b", header_style="#4bb0e3", title_style="#e3db4b")
        table.add_column("Title", style="#4bb0e3", min_width=10, max_width=50)
        table.add_column("Text", style="#4bb0e3", min_width=10, max_width=50)
        table.add_column("Tags", style="#4bb0e3", min_width=10, max_width=50)
        list_notes = []
        for key, value in notes_from_file.data.items():
            title = value.note_title
            text = value.note_text
            tags = value.note_tags
            list_notes.append((title, text, tags))
        for t in list_notes:
            title = t[0]
            text = t[1]
            tags = ", ".join([str(p) for p in t[2]])
            table.add_row(title, text, tags)
        console.print(table)

    def edit_note(notes_from_file):
        try:
            dict_with_number = notes_from_file.find_note()
            choice = int(input("Please choose contact to edit: "))
            for key, value in dict_with_number.items():
                if key == choice:
                    note_for_edit = notes_from_file[value]
                    table = [["1. Title", "2. Text", "3. Add tag", "4. Edit tag", "5. Delete tag", "6. Return"]]
                    print(data2rst(table))
                    part_of_note_to_edit = int(input("Please choose field to edit: "))
                    if part_of_note_to_edit == 1:
                        new_title = input("Enter new note title: ")
                        notes_from_file[new_title] = notes_from_file[note_for_edit.note_title]
                        del notes_from_file[note_for_edit.note_title]
                        note_for_edit.note_title = new_title
                    elif part_of_note_to_edit == 2:
                        new_text = input("Enter new text for note: ")
                        note_for_edit.note_text = new_text
                    elif part_of_note_to_edit == 3:
                        new_tag = input("Enter new tag to add: ")
                        note_for_edit.add_tag(new_tag)
                    elif part_of_note_to_edit == 4:
                        old_tag = input("Enter tag to edit: ")
                        new_tag = input("Enter new tag: ")
                        note_for_edit.edit_tag(old_tag, new_tag)
                    elif part_of_note_to_edit == 5:
                        tag_to_delete = input("Enter tag to delete: ")
                        note_for_edit.delete_tag(tag_to_delete)
                    elif part_of_note_to_edit == 6:
                        pass
            notes_from_file.save_notes_to_json_file("Output/notes.json")
        except ValueError:
            print("Invalid input. Please enter a valid number.")