import tkinter as tk
from tkinter import ttk
from .timer import Timer
from collections import deque


class PomodoroTimer(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro = tk.StringVar(value=25)
        self.long_break = tk.StringVar(value=15)
        self.short_break = tk.StringVar(value=5)
        self.timer_order = [
            "Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro",
            "Long Break"
        ]
        self.timer_schedule = deque(self.timer_order)
        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        timer_frame = Timer(self, container)
        timer_frame.grid(row=0, column=0, sticky="NESW")
