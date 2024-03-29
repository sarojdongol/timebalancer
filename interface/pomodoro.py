import tkinter as tk

# from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from config import Settings
from interface import Timer
from interface.taskhandler import TaskHandler
from interface.excercise_selector import ExcerciseSelector
from collections import deque

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer():
    def __init__(self, app, *args, **kwargs):
        self.app = app
        self.pomodoro_time = ttk.StringVar(value=25)
        self.long_break_time = ttk.StringVar(value=15)
        self.short_break_time = ttk.StringVar(value=5)
        self.timer_order = [
            "Pomodoro",
            "Short Break",
            "Pomodoro",
            "Short Break",
            "Pomodoro",
            "Long Break",
        ]
        self.timer_schedule = deque(self.timer_order)
        container = ttk.Frame(app, style="info.TFrame")
        container.grid()
        container.columnconfigure((0, 1, 2, 3, 4), weight=1)
        container.rowconfigure((0, 1, 2, 3, 4), weight=1)

        self.frames = dict()
        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW", padx=5, pady=5)

        settings_frame = Settings(container, self, lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NESW")

        task_frame = TaskHandler(container, self, lambda: self.show_frame(TaskHandler))
        task_frame.grid(row=0, column=0, sticky="NESW")

        excercise_frame = ExcerciseSelector(
            container,
            self,
            lambda: self.show_frame(ExcerciseSelector),
            lambda: self.show_frame(Timer),
        )
        excercise_frame.grid(row=0, column=0, sticky="EW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame
        self.frames[TaskHandler] = task_frame
        self.frames[ExcerciseSelector] = excercise_frame

        self.show_frame(Timer)

        self.app.mainloop()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
