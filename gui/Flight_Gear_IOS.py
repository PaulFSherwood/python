from tkinter import *
from tkinter import ttk
import sys
import urllib.request

def setND1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/nd/range?value=10&submit=update").read()
   pass

def setND2():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/nd/range?value=100&submit=update").read()
   pass


root = Tk()
root.title("Flight Gear IOS")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

# resize stuff
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# buttons
ttk.Button(mainframe, text="ND 10", command=setND1).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="ND 100", command=setND2).grid(column=1, row=1, sticky=W)

# slider
Slider_1 = Scale(root, orient=HORIZONTAL, length=300, width=20, sliderlength=10, from_=0,to=50, tickinterval=5).grid(column=1, row=2, sticky=W)

Slider_1.on_changed(update)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
