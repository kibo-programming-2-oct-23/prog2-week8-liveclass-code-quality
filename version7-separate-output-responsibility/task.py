class Task:
    """
    Represents a task with a description and a due date.
    """

    def __init__(self, description, date):
        """
        Initializes a new Task instance.

        Args:
            description (str): The description of the task.
            date (datetime): The due date of the task.
        """
        self.description = description
        self.due_date = date

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: String representation of the task.
        """
        return f"{self.description} Due: {self.due_date}"