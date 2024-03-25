from interface import PomodoroTimer
import ttkbootstrap as ttk


app = ttk.Window(themename="flatly", title="Pomodoro Timer")
root = PomodoroTimer(app)
root.mainloop()