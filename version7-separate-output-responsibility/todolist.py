from task import Task

class ToDoList:
    """
    Manages a collection of tasks in a to-do list.
    """

    def __init__(self):
        """
        Initializes a new ToDoList instance.
        """
        self.tasks = []

    def add_task(self, description, due_date):
        """
        Adds a new task to the to-do list.

        Args:
            description (str): The description of the task.
            due_date (datetime): The due date of the task.
        """
        self.tasks.append(Task(description, due_date))

    def get_tasks(self):
        """
        Retrieves all tasks in the to-do list.

        Returns:
            list: List of tasks.
        """
        return self.tasks

    def delete_task(self, task_index):
        """
        Deletes a task from the to-do list based on its index.

        Args:
            task_index (int): The index of the task to delete.

        Raises:
            IndexError: If the task index is invalid.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
        else:
            raise IndexError("Invalid task index.")