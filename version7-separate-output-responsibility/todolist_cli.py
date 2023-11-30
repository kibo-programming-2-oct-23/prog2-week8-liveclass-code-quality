from todolist import ToDoList
from datetime import datetime

class ToDoListCli:
    """
    Interface for interacting with the ToDoList. Handles user input and output.
    """

    def __init__(self):
        """
        Initializes a new ToDoListInterface instance.
        """
        self.todo_list = ToDoList()

    def run(self):
        """
        Runs the main loop of the application.
        """
        while True:
            self.display_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete a task")
        print("4. Exit")
        print()

    def add_task(self):
        """
        Handles the addition of a new task.
        """
        description = input("Enter a task: ")
        deadline_str = input("Enter the deadline for this task (YYYY-MM-DD): ")
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d")
            self.todo_list.add_task(description, deadline)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def view_tasks(self):
        """
        Handles displaying all tasks in the to-do list.
        """
        tasks = self.todo_list.get_tasks()
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")

    def delete_task(self):
        """
        Handles the deletion of a task.
        """
        task_number = int(input("Enter the task number to delete: "))
        try:
            self.todo_list.delete_task(task_number - 1)
        except IndexError:
            print("Invalid task number.")