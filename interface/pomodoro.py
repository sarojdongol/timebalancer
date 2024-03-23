import tkinter as tk
#from tkinter import ttk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from config import Settings
from interface import Timer
from interface.taskhandler import TaskHandler
from collections import deque

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class PomodoroTimer(tk.Tk):

    def __init__(self, app, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        #self.style = Style(theme="superhero")
        self.app = app
        self.title("Pomodoro Timer")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.pomodoro_time = tk.StringVar(value=25)
        self.long_break_time = tk.StringVar(value=15)
        self.short_break_time = tk.StringVar(value=5)
        self.timer_order = [
            "Pomodoro", "Short Break", "Pomodoro", "Short Break", "Pomodoro",
            "Long Break"
        ]
        self.timer_schedule = deque(self.timer_order)
        container = ttk.Frame(app,style='info.TFrame')
        container.grid()
        container.columnconfigure(0, weight=1)

        self.frames = dict()
        timer_frame = Timer(container, self, lambda: self.show_frame(Settings))
        timer_frame.grid(row=0, column=0, sticky="NESW", padx=10, pady=10)

        settings_frame = Settings(container, self,
                                  lambda: self.show_frame(Timer))
        settings_frame.grid(row=0, column=0, sticky="NESW")

        task_frame = TaskHandler(container, self,
                                  lambda: self.show_frame(TaskHandler))
        task_frame.grid(row=0, column=0, sticky="NESW")

        self.frames[Timer] = timer_frame
        self.frames[Settings] = settings_frame
        self.frames[TaskHandler] = task_frame

        self.show_frame(Timer)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
