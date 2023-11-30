def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    print()

def add_task(task_list):
    """
    Adds a new task to the task list.

    Parameters:
    task_list (list): The list where the task will be added.
    """
    task = input("Enter a task: ")
    task_list.append(task)

def view_tasks(task_list):
    """
    Displays all tasks in the task list.

    Parameters:
    task_list (list): The list of tasks to be displayed.
    """
    if task_list:
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks in the list.")

def delete_task(task_list):
    """
    Deletes a task from the task list based on the task number.

    Parameters:
    task_list (list): The list from which the task will be removed.
    """
    task_number = int(input("Enter the task number to delete: "))
    if 0 < task_number <= len(task_list):
        task_list.pop(task_number-1)
    else:
        print("Invalid task number.")

def main():
    """
    The main function to run the to-do list program.
    """
    task_list = []
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            delete_task(task_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
