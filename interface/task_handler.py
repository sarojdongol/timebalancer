

from tkinter import Tk, Frame, Label, Button, Listbox, StringVar, messagebox, Entry, END
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import date

class TaskList:
  def __init__(self, master):
    
    self.master = master
    master.title("Task List")

    # Create a frame to hold all the elements
    self.task_frame = Frame(master)
    self.task_frame.pack(padx=10, pady=10)

    # Label for task description
    self.task_label = ttk.Label(self.task_frame, text="Task:")
    self.task_label.grid(row=0, column=0,sticky="EW")

    # Entry for task description
    self.task_entry = Entry(self.task_frame)
    self.task_entry.grid(row=0, column=1,sticky="EW",padx=5, pady=5)

    # Label to display due date (initially empty)
    self.due_date_label = Label(self.task_frame, text="Due Date: ")
    self.due_date_label.grid(row=0, column=2,sticky="EW")

     # Button to set due date
    self.date_button = ttk.DateEntry(self.task_frame,bootstyle=SUCCESS, startdate=date(2023,2,1))
    self.date_button.grid(row=0, column=3, sticky="EW",padx=5,pady=5)

    # Listbox to display tasks
    self.task_list = Listbox(self.task_frame,width=50,height=50,selectbackground="magenta")
    self.task_list.grid(row=2, columnspan=3)

    # Variable to store selected task index
    self.selected_task_index = StringVar()
    self.selected_task_index.set(-1) 

    # Button to add task
    self.add_button = ttk.Button(self.task_frame, text="Add Task", command=self.add_task,bootstyle=(INFO, OUTLINE))
    self.add_button.grid(row=0, column=5)

  def add_task(self):
    task_text = self.task_entry.get()
    due_date = self.date_button.entry.get()
    if task_text:
      self.task_list.insert(END, task_text + " " + due_date)
      self.task_entry.delete(0, END)  # Clear entry field after adding task
      self.due_date_label.config(text="Due Date: ")  # Reset due date label
    else:
      messagebox.showinfo("Add Task", "Please enter a task description.")

if __name__ == "__main__":
  root = ttk.Window(themename="superhero",position=(1000,1000),resizable=(False,False))
  task_list = TaskList(root)
  root.mainloop()



# uses DatePickerPopup() from ttkbootstrap to Date
