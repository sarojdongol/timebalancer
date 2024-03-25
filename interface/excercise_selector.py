from tkinter import Tk, Frame, Label, Button, Listbox, StringVar, messagebox, Entry, END
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import date
import os
from pathlib import Path
from PIL import Image, ImageTk


class ExcerciseSelector(ttk.Frame):
    def __init__(self, parent, controller, show_settings, previous_timer):
        super().__init__(parent, padding=(20, 10))

        # Create a frame to hold all the elements
        self.task_frame = ttk.Frame(parent)
        self.task_frame.grid(sticky="NESW")

        # Label for task description
        self.task_label = ttk.Label(self.task_frame, text="Excercise for Today: ")
        self.task_label.grid(row=0, column=0, sticky="W")

        image = Image.open(
            os.path.join(Path.cwd(), "assets/short_break_excercise/excercise_1.jpg")
        )
        python_image = ImageTk.PhotoImage(image)
        image_label = ttk.Label(self, image=python_image)
        image_label.image = python_image
        image_label.grid(row=0, column=3, sticky="W")

        image_button = ttk.Button(
            self.task_frame,
            text="Short Break Exercise",
            command=show_settings,
            style=(INFO, OUTLINE),
            cursor="hand2",
        )
        image_button.grid(row=0, column=0, sticky="W")

        previous_timer = ttk.Button(
            self.task_frame,
            text="<- Back",
            command=previous_timer,
            bootstyle=(INFO, OUTLINE),
            cursor="hand2",
        )
        previous_timer.grid(column=1, row=0, sticky="W", padx=2)


def excercise_on_break(self):
    pass
