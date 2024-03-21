#add task in tkfram
from tkinter import ttk
import tkinter as tk

# implement tk inter to create task list with date field and status field into the frame
class TaskList(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.task_list = []
        self.create_widgets()

    def create_widgets(self):
        # create a label for the task list
        self.task_list_label = ttk.Label(self, text="Task List")
        self.task_list_label.pack(pady=10)

        # create a frame for the task list
        self.task_list_frame = ttk.Frame(self)
        self.task_list_frame.pack(pady=10)

        # create a label for the date field
        self.date_label = ttk.Label(self.task_list_frame, text="Date")
        self.date_label.grid(row=0, column=0, padx=5, pady=5)

        # create a label for the status field
        self.status_label = ttk.Label(self.task_list_frame, text="Status")





