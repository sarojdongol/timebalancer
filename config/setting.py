import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk


class Settings(ttk.Frame):
    """
    Generate Tuple Config
    """

    def __init__(self, parent, controller, show_timer):
        super().__init__(parent)
        #self["style"] = "Background.TFrame"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)
        settings_container = ttk.Frame(self, padding="30 15 30 15")
        settings_container.grid(row=0, column=0, sticky="EW", padx=10, pady=10)
        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(1, weight=1)

        pomodoro_label = ttk.Label(settings_container, text="Pomodoro: ")

        pomodoro_label.grid(column=0, row=0, sticky="W")

        pomodoro_input = tk.Spinbox(settings_container,
                                    from_=0,
                                    to=120,
                                    increment=1,
                                    justify="center",
                                    textvariable=controller.pomodoro_time,
                                    width=10)

        pomodoro_input.grid(column=1, row=0, sticky="EW")
        pomodoro_input.focus()

        long_break_label = ttk.Label(settings_container,
                                     text="Long Break time: ")

        long_break_label.grid(column=0, row=1, sticky="W")

        long_break_input = tk.Spinbox(settings_container,
                                      from_=0,
                                      to=60,
                                      increment=1,
                                      justify="center",
                                      textvariable=controller.long_break_time,
                                      width=10)

        long_break_input.grid(column=1, row=1, sticky="EW")
        long_break_input.focus()

        short_break_label = ttk.Label(settings_container,
                                      text="Short Break Time: ")

        short_break_label.grid(column=0, row=2, sticky="W")

        short_break_input = tk.Spinbox(settings_container,
                                       from_=0,
                                       to=30,
                                       increment=1,
                                       justify="center",
                                       textvariable=controller.short_break_time,
                                       width=10)

        short_break_input.grid(column=1, row=2, sticky="EW")
        short_break_input.focus()

        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)

        button_container = ttk.Frame(self)
        button_container.grid(sticky="EW", padx=10)
        button_container.columnconfigure(0, weight=1)

        timer_button = ttk.Button(button_container,
                                  text="<- Back",
                                  command=show_timer,
                                   bootstyle=(INFO, OUTLINE),
                                  cursor="hand2")
        timer_button.grid(column=0, row=0, sticky="EW", padx=2)
