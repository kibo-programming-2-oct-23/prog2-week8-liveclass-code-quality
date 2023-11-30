class ToDoList:
    
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the list.")

    def delete_task(self):
        task_number = int(input("Enter the task number to delete: "))
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
        else:
            print("Invalid task number.")

