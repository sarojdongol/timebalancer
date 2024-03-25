from tkinter import Tk, Frame, Label, Button, Listbox, StringVar, messagebox, Entry, END
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import date
from ttkbootstrap.tableview import Tableview


class TaskHandler(ttk.Frame):
    def __init__(self, parent, controller, show_settings):
        super().__init__(parent, padding=(20, 10))

        # Create a frame to hold all the elements
        self.task_frame = ttk.Frame(parent)
        self.task_frame.grid(sticky="NESW")

        # Label for task description
        self.task_label = ttk.Label(self.task_frame, text="Task:")
        self.task_label.grid(row=0, column=0, sticky="EW")

        # Entry for task description
        self.task_entry = ttk.Entry(self.task_frame)
        self.task_entry.grid(row=0, column=1, sticky="EW", padx=2, pady=2)

        # Label to display due date (initially empty)
        self.due_date_label = ttk.Label(self.task_frame, text="Due Date: ")
        self.due_date_label.grid(row=0, column=2, sticky="EW")

        # Button to set due date
        self.date_button = ttk.DateEntry(
            self.task_frame, bootstyle=SUCCESS, startdate=date(2023, 2, 1)
        )
        self.date_button.grid(row=0, column=3, sticky="EW", padx=2, pady=2)

        self.status_label = ttk.Label(self.task_frame, text="Status:")
        self.status_label.grid(row=0, column=4, sticky="EW", padx=2, pady=2)

        self.status_button = ttk.Combobox(
            self.task_frame,
            values=["IN-PROGRESS", "DONE", "BACKLOG"],
            bootstyle=PRIMARY,
        )
        self.status_button.grid(row=0, column=5, sticky="EW", padx=2, pady=2)

        # Variable to store selected task index
        self.selected_task_index = StringVar()
        self.selected_task_index.set(-1)

        coldata = [
            {"text": "Task", "stretch": True},
            {"text": "Due Date", "stretch": False},
            {"text": "Status", "stretch": False},
        ]

        self.dt = Tableview(
            master=parent,
            coldata=coldata,
            paginated=True,
            bootstyle=PRIMARY,
            autoalign=True,
        )

        self.dt.grid(row=2, column=0, columnspan=3, sticky="NESW")

        # Button to add task
        self.add_button = ttk.Button(
            self.task_frame, text="Add Task", command=self.add_task, bootstyle=(INFO)
        )
        self.add_button.grid(row=0, column=6)

    def add_task(self):
        task_text = self.task_entry.get()
        due_date = self.date_button.entry.get()
        status = self.status_button.get()

        if task_text:
            self.dt.insert_row(END, values=(task_text, due_date, status))
            self.dt.load_table_data()

        else:
            messagebox.showinfo("Add Task", "Please enter a task description.")

    def create_edit_button(self, item_id):
        """
        Creates an edit button for the specified table row.
        """
        edit_button = ttk.Button(
            self.task_frame,
            text="Edit",
            command=lambda item=item_id: self.edit_task(item),
        )
        self.table.set(item_id, "#1", window=edit_button)

    def edit_task(self, item_id):
        """Prompts the user to update the task details and status."""
        task_data = self.tasks[int(item_id) - 1]
        new_task = ttk.simpledialog.askstring("Edit Task", f"Task: {task_data['task']}")
        new_description = ttk.simpledialog.askstring(
            "Edit Task", f"Description: {task_data['description']}"
        )
        if new_task or new_description:
            # Update task data if either task or description is changed
            if new_task:
                task_data["task"] = new_task
                self.table.set(item_id, "Task", new_task)
            if new_description:
                task_data["description"] = new_description
                self.table.set(item_id, "Description", new_description)
            # Update status using the combobox selection
            self.update_task_status(item_id, self.status_var.get())

    def update_task_status(self, item_id, new_status):
        """Updates the status of a task in the table view."""
        self.tasks[int(item_id) - 1]["status"] = new_status
        self.table.set(item_id, "Status", new_status)

    # Place button in the second column
