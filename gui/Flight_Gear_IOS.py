from tkinter import *
from tkinter import ttk
import sys
import urllib.request

def setND(val):
   # geting the variable
   currentAddress = "http://127.0.0.1:5555/instrumentation/nd/range?value={0}&submit=update".format(str(val))
   # currentAddress = "http://127.0.0.1:5555/instrumentation/nd/range?value=10&submit=update")
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen(currentAddress).read()
   # print(val)
   pass
# SC840 Navigation Control Panel (is that right?)
def setOFF1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/primus2000/sc840/nav1ptr?value=0&submit=update").read()
   adVal = 10
   pass

def setVOR1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/primus2000/sc840/nav1ptr?value=1&submit=update").read()
   adVal = 100
   pass

def setADF1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/primus2000/sc840/nav1ptr?value=2&submit=update").read()
   adVal = 100
   pass

def setFMS1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5555/instrumentation/primus2000/sc840/nav1ptr?value=3&submit=update").read()
   adVal = 100
   pass


root = Tk()
root.title("Flight Gear IOS")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

# resize stuff
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# buttons
ttk.Button(mainframe, text=" OFF", command=setOFF1).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="VOR1", command=setVOR1).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="ADF1", command=setADF1).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="FMS1", command=setFMS1).grid(column=1, row=4, sticky=W)

# slider
Slider_1 = Scale(root, command=setND, orient=HORIZONTAL, length=200, width=20, sliderlength=10, from_=0,to=100)
# this puts numbers on the bottom , tickinterval=5)
# not sure why grid isnt working correctly 
Slider_1.grid(column=1, row=5, sticky=W)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
