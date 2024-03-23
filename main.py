from interface import PomodoroTimer
import ttkbootstrap as ttk


app = ttk.Window(themename="darkly", title="Pomodoro Timer", size=(500, 500))
root = PomodoroTimer(app)
root.mainloop()