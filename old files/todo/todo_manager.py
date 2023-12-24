from collections import UserDict
from datetime import datetime
import json
from contacts.classes.Field import Field
from contacts.classes.Birthday import Birthday

class ToDoRecord:
    def __init__(self, task, begin, end, status=None, tags=None):
        self.task = task
        self.begin = begin
        self.end = end
        self.status = status
        self.tags = list(tags)

    # {'task def add_task(self, task, date, status, tags):
    #     #     self.tasks.append(': task, 'date': date, 'status': status, 'tags': tags})
    #     print(f'You had added "{task}" for your to do list.')

    # adding tags while creating ToDoRecord class instance
    def add_tags(self, tag):
        if not isinstance(tag, Field):
            tag = Field(tag)
        self.tags.append(tag)

    # possibility of editing the tag if the user made a mistake
    def edit_tags(self, wrong_tag, right_tag):
        if not wrong_tag:
            print("Please enter tag to edit")
        elif not right_tag:
            print("Please enter a new tag")
        else:
            for i, p in enumerate(self.tags):
                if p.value == wrong_tag:
                    self.tags[i] = Field(right_tag)

# removing unnecessary tag
    def delete_tags(self, tag_to_delete):
        if not tag_to_delete:
            print("Please enter tag to delete")
        else:
            for i, p in enumerate(self.tags):
                if p.value == tag_to_delete:
                    self.tags.remove(p)

    # searching by tag
    #     def search_by_tag(self, tag_to_find):
    #         search_result = []
    #         if not tag_to_find:
    #             print("Please enter tag to find")
    #         else:
    #             for i in self.tasks:
    #                 if tag_to_find in i['tags']:
    #                     search_result.append(i)
    #         if not search_result:
    #             return f"Sorry, task with that tag is absent in your To Do List"
    #         else:
    #             return search_result

    # searching by one or two literal
    def search_by_part_word(self, part_word):
        searching_tasks = []
        for task in self.tasks:
            if part_word.lower() in task["task"].lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Name", part_word)

    # searching by date
    def search_by_date(self, date):
        searching_tasks = []
        for task in self.tasks:
            if task['date'] in date:
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Date", date)

        # It can also work by this
        # searching_tasks = [task for task in self.tasks if task['date'] == date]
        # self._search_results(searching_tasks, 'Date', date)

    # searching by status
    def search_by_status(self, status):
        searching_tasks = []
        for task in self.tasks:
            if task['status'].lower() in status.lower():
                searching_tasks.append(task)

        self._search_results(searching_tasks, "Status", status)

        # It can also work by this
        # esarching_tasks = [task for task in self.tasks if task['status'].lower() == status.lower()]
        # self._search_results(searching_tasks, 'Status', status)

    # completely change the task
    def change_task(self, new_task):
        self.task = new_task

    # partially modify task
    def edit_task(self, wrong_part, new_part):
        part_of_task = self.task.find(wrong_part)
        if part_of_task == -1:
            print(f'Task has no letters {wrong_part}. Please try again.')
        else:
            new_task = self.task.replace(wrong_part, new_part)
            self.task = new_task

    # changing begin date
    def edit_begin_date(self, new_date):
        if not isinstance(new_date, Birthday):
            new_date = Birthday(new_date)
        self.begin = new_date

    # changing end date
    def edit_end_date(self, new_date):
        if not isinstance(new_date, Birthday):
            new_date = Birthday(new_date)
        self.end = new_date

    # changing task status
    def edit_status(self, new_status):
        self.status = new_status

    # def __str__(self):
    #     return f"{self.task}: start - {self.begin}, end - {self.end}, current status is {self.status}, tags: {', '.join(p.value for p in self.tags)}"


class ToDoBook(UserDict):
    def add_to_do_record(self, record: ToDoRecord):
        self.data[record.task] = record
        return self.data

    def search_todo(self):
        try:
            search_info = input("Enter info for search: ").lower()
            result_list = []
            for task in self.data.values():
                search_by_task = task.task.lower().find(search_info)
                search_by_date1 = str(task.begin).find(search_info)
                search_by_date2 = str(task.end).find(search_info)
                search_by_status = task.status.lower().find(search_info)
                search_by_tags = str([tag.lower() for tag in task.tags]).find(search_info)
                if search_by_task > -1 or search_by_date1 > -1 or search_by_date2 > -1 or search_by_status > -1 or search_by_tags > -1:
                    result_list.append(task)
            dict_with_number = dict(zip([i + 1 for i in range(len(result_list))], [i.task for i in result_list]))
            print(dict_with_number)
            return dict_with_number
        except ValueError:
                print("Invalid input. Please enter a valid info for search.")

    def edit_todo(self):
        try:
            dict_with_number = self.search_todo()
            choice = int(input('Please choose task number to edit: '))
            for key, value in dict_with_number.items():
                if key == choice:
                    task_for_edit = self.data[value]
                    part_of_task_to_edit = input("Please choose field to edit (title/begin/end/status/tags): ")
                    if part_of_task_to_edit == 'title':
                        new_title = input("Enter new task title: ")
                        self.data[new_title] = self.data[task_for_edit.task]
                        del self.data[task_for_edit.task]
                        task_for_edit.task = new_title
                    elif part_of_task_to_edit == 'begin':
                        new_begin = input("Enter new begin date: ")
                        task_for_edit.begin = new_begin
                    elif part_of_task_to_edit == 'end':
                        new_end = input("Enter new end date: ")
                        task_for_edit.end = new_end
                    elif part_of_task_to_edit == 'status':
                        new_status = input("Enter new status (Done/In_progress): ")
                        task_for_edit.status = new_status
                    elif part_of_task_to_edit == 'tags':
                        old_tag = input("Enter tag to edit: ")
                        new_tag = input("Enter new tag: ")
                        for tag in task_for_edit.tags:
                            if tag == old_tag:
                                task_for_edit.tags.remove(old_tag)
                                task_for_edit.tags.append(new_tag)
            self.save_to_file_todo('outputs/todo.json')
        except ValueError:
                print("Invalid input. Please enter a valid number.")

    def delete_task(self):
        try:
            dict_with_number = self.search_todo()
            delete_i = int(input("Please choose task number: "))
            for key, value in dict_with_number.items():
                if key == delete_i:
                    del self.data[value]
            self.save_to_file_todo('outputs/todo.json')
        except ValueError:
                print("Invalid input. Please enter a valid info for delete.")

    def delete_tag_in_todo(self):
        try:
            dict_with_number = self.search_todo()
            task_for_tag = int(input("Please choose task number: "))
            tag_to_delete = input("Please enter tag to delete: ")
            for key, value in dict_with_number.items():
                if key == task_for_tag:
                    delete_tag = self.data[value]
                    for tag in delete_tag.tags:
                        if tag == tag_to_delete:
                            confirmation = input(f"Do you really want to delete {tag_to_delete} (y/n)? ")
                            if confirmation == 'y':
                                delete_tag.tags.remove(tag_to_delete)
                                print("Delete is complete successfully")
                            else:
                                continue
            self.save_to_file_todo('outputs/todo.json')
        except ValueError:
            print("Invalid input. Please enter a valid info for delete.")

    def add_tag(self):
        try:
            dict_with_number = self.search_todo()
            task_for_tag = int(input("Please choose task number: "))
            tag_to_add = input("Please enter tag to add: ")
            for key, value in dict_with_number.items():
                if key == task_for_tag:
                    add_tag = self.data[value]
                    add_tag.tags.append(tag_to_add)
                    print("Tag has been successfully add")
            self.save_to_file_todo('outputs/todo.json')
        except ValueError:
            print("Invalid input. Please enter a valid info for delete.")

    def convert_to_serializable_todo(todobook):
        serializable_data = {}
        for key, record in todobook.items():
            serializable_data[str(key)] = {
                "task": record.task,
                "begin date": record.begin,
                "end date": record.end,
                "status": record.status,
                "tags": record.tags
            }
        return serializable_data
    def save_to_file_todo(self, filename):
        data_to_serialize = ToDoBook.convert_to_serializable_todo(self)
        try:
            with open(filename, "w", encoding="utf-8") as json_file:
                json.dump(data_to_serialize, json_file, indent=4)
                json_file.write('\n')
            print(f'Tasks saved to {filename} successfully.')
        except Exception as e:
            print(f'Error saving tasks to {filename}: {e}')


    def load_from_file(filename):
        try:
            with open(filename, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            todobook = ToDoBook()
            for key, value in data.items():
                task = key
                begin = value["begin date"]
                end = value["end date"]
                status = value["status"]
                tags = value["tags"]
                record =  ToDoRecord(task, begin, end, status, tags)
                todobook.add_to_do_record(record)
            # print(f'Notes loaded from {filename} successfully.')
            return todobook
        except Exception as e:
            print(f'Error loading tags from {filename}: {e}')
            return ToDoBook()  # Return a new instance in case of an error


# class ToDoListSave(ToDoRecord):
#     def save_list(self):
#         with open(self.file, "w", encoding="utf-8") as f:
#             json.dump((self.date, self.task), f)


if __name__ == '__main__':
    to_do_list = ToDoBook()

    task1 = ToDoRecord("Buy some food", "13.12.2023", "17.12.2023", "Done", 'food')
    task1.add_tags("food")
    task1.add_tags("store")
    to_do_list.add_to_do_record(task1)

    task2 = ToDoRecord("Buy shampoo", "16.12.2023", "20.12.2023", "In progress", "beauty")
    task2.add_tags("beauty")
    task2.add_tags("store")
    to_do_list.add_to_do_record(task2)

    task3 = ToDoRecord("Get my nails done", "17.12.2023", "28.12.2023", "In progress", "beauty")
    task3.add_tags("beauty")
    to_do_list.add_to_do_record(task3)

    # task3.edit_tags('beauty', 'salon')
    # task2.delete_tags('beauty')
    # task2.edit_task("shampoo", "soap")
    # task2.edit_begin_date("2023-12-17")
    # task2.edit_end_date("2023-12-21")
    # task2.edit_status("Done")

    # to_do_list.search_task()
    # to_do_list.delete_task()

    for name, record in to_do_list.data.items():
        print(record)
