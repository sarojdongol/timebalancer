from interface import PomodoroTimer
import ttkbootstrap as ttk


app = ttk.Window(themename="flatly", title="Pomodoro Timer")
PomodoroTimer(app)

