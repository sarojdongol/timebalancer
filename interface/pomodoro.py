import tkinter as tk
from tkinter import ttk
from .timer import Timer


class PomodoroTimer(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(container)
        timer_frame.grid(row=0, column=0, sticky="NESW")
 