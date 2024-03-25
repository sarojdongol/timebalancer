import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window()
colors = app.style.colors

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

dt = Tableview(
    master=app,c
    coldata=coldata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    autoalign=True,
    stripecolor=(colors.light, None),
)
dt.pack(fill=X, padx=10, pady=10)
#dt.grid(row=0, column=0, sticky="NSEW")

dt.insert_row('end', ['Marzale LLC', 26])


app.mainloop()