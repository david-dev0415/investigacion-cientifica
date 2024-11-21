''' 
  Task | task module (tareas)

  Provides a simple interface for creating tasks.
  .- The Task class is used to create tasks with the following attributes:
    .- nameTask: Task name
    .- deadline: Task deadline
    .- category: Task category
    .- hoursDedicated: Hours dedicated to the task
  .- The Task class has a __str__ method that returns a string with the task information.

'''
from datetime import datetime

class Task():
    def __init__(self, nameTask, deadline, category, hoursDedicated):
        
        if not isinstance(nameTask, str):
            raise ValueError("You must enter a string for the name of the task. Example: 'Task 1', 'Task 2', etc.")
        elif not isinstance(deadline, datetime.strftime(deadline, "%d/%m/%Y")):
            raise ValueError(f"You must enter a datetime object for the deadline of the task. Example: ${datetime.strftime(datetime.now, '%d/%m/%Y')}")
        elif not isinstance(category, str):
            raise ValueError("You must enter a string for the category of the task. Example: 'Work', 'Personal', 'Study', etc.")
        elif not isinstance(hoursDedicated, float):
            raise ValueError("You must enter an float for the hours dedicated to the task. Example: 1.5, 2.0, 3.0, etc.")

        self.name = nameTask
        self.deadline = deadline
        self.deadline = deadline
        self.category = category
        self.hoursDedicated = hoursDedicated

    def __str__(self):
        return f"Task: {self.name}, Deadline: {self.deadline}, Category: {self.category}, Hours dedicated: {self.hoursDedicated}"
        