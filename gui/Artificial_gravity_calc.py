from tkinter import *
from tkinter import ttk
import math

def findgra(*args):
    try:
	    radius1 = float(radius.get())
	    rpm1 = float(rpm.get())
	    gravity.set(round(((radius1*(math.pow(((3.14*rpm1)/30),2)))/9.81),4))
    except ValueError:
        pass

def findrad(*args):
    try:
	    gravity1 = float(gravity.get())
	    rpm1 = float(rpm.get())
	    radius.set(round((9.81*gravity1)/(math.pow(((3.14*rpm1)/30),2)),4))
    except ValueError:
        pass

def findrpm(*args):
    try:
	    gravity1 = float(gravity.get())
	    radius1 = float(radius.get())
	    rpm.set(round(((30*(math.sqrt(((9.81*gravity1)/radius1))))/3.14),4))
    except ValueError:
        pass
    
root = Tk()
root.title("Gravity")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)#, sticky=(N, W, E, S))
# when expanding window how fast do columns/rows grow
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

gravity = StringVar()
radius = StringVar()
rpm = StringVar()

# text entry field
# __________________________________
# |          |          |          |
# | TXT ENTY | TXT ENTY | TXT ENTY |
# |          |          |          |
# ----------------------------------
gravity_entry = ttk.Entry(mainframe, width=7, textvariable=gravity)
gravity_entry.grid(column=1, row=2, sticky=(W, E))
radius_entry = ttk.Entry(mainframe, width=7, textvariable=radius)
radius_entry.grid(column=2, row=2, sticky=(W, E))
radius_entry = ttk.Entry(mainframe, width=7, textvariable=rpm)
radius_entry.grid(column=3, row=2, sticky=(W, E))


# changing fields
# __________________________________
# |          |          |          |
# |          |          |          |
# |CHGIN LBL |CHGIN LBL |CHGIN LBL |
# ----------------------------------
ttk.Label(mainframe, textvariable=gravity).grid(column=1, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=radius).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=rpm).grid(column=3, row=3, sticky=(W, E))


# calc buttons
# _____________________________________________
# |          |          |          | BUTTON1  |
# |          |          |          | BUTTON2  |
# |          |          |          | BUTTON3  |
# ---------------------------------------------
ttk.Button(mainframe, text="Find Gra", command=findgra).grid(column=4, row=1, sticky=W)
ttk.Button(mainframe, text="Find Rad", command=findrad).grid(column=4, row=2, sticky=W)
ttk.Button(mainframe, text="Find RPM", command=findrpm).grid(column=4, row=3, sticky=W)

# text only section
# __________________________________
# | Gravity  |  Radius  |   RPM    |
# |          |          |          |
# |          |          |          |
# ----------------------------------
ttk.Label(mainframe, text="Gravity").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Radius").grid(column=2, row=1, sticky=W)
ttk.Label(mainframe, text="RPM").grid(column=3, row=1, sticky=W)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

gravity_entry.focus()

root.mainloop()
