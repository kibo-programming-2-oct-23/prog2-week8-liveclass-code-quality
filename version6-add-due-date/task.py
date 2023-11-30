class Task:
    def __init__(self, description, date):
        self.description = description
        self.due_date = date

    def __str__(self):
        return f"{self.description} Due: {self.due_date}"
