from tkinter import *
from tkinter import ttk
import urllib.request
import itertools
import sys


def setND(val):
   # geting the variable
   currentAddress = "http://127.0.0.1:5500/props/instrumentation/nd?submit=set&range%5B0%5D=" + format(str(val))
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen(currentAddress)
   pass
# SC840 Navigation Control Panel (is that right?)
def setOFF1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5500/instrumentation/primus2000/sc840/nav1ptr?value=0&submit=update").read()
   adVal = 10
   pass

def setVOR1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5500/props/instrumentation/primus2000/sc840/nav1ptr?value=1&submit=update").read()
   adVal = 100
   pass

def setADF1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5500/props/instrumentation/primus2000/sc840/nav1ptr?value=2&submit=update").read()
   adVal = 100
   pass

def setFMS1():
   # access the flight gear webserver and send it the value we want.
   urllib.request.urlopen("http://127.0.0.1:5500/props/instrumentation/primus2000/sc840/nav1ptr?value=3&submit=update").read()
   adVal = 100
   pass

def setAP1():
    urllib.request.urlopen("http://127.0.0.1:5500/props/autopilot/locks/AP-status?value=AP1&submit=update").read()
    pass

def setAP2():
    urllib.request.urlopen("http://127.0.0.1:5500/props/autopilot/locks/AP-status?value=&submit=update").read()
    pass
def setCRS1():
    crsVal = course.get()
    one = "http://127.0.0.1:5500/props/instrumentation/nav/radials/selected-deg?value="
    two = "&submit=update"
    
    combined = one + crsVal + two
    urllib.request.urlopen( combined ).read()
    pass
def setHDG1():
    hdgVal = heading.get()
    one = "http://127.0.0.1:5500/props/autopilot/settings/heading-bug-deg?value="
    two = "&submit=update"
    
    combined = one + hdgVal + two
    urllib.request.urlopen( combined ).read()
    pass

root = Tk()
root.title("Flight Gear IOS")

course = StringVar()
heading = StringVar()

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

# autopilot
### testVar = 1
### if testVar == 2:
###     ttk.Button(mainframe, text="AP1/ON", command=setAP1()).grid(column=2, row=1, sticky=W)
###     testVar = 2
###     print("main 1:", testVar)
### else:
###     ttk.Button(mainframe, text="AP1/ON", command=setAP2()).grid(column=2, row=1, sticky=W)
###     testVar = 1
###     print("main 2:", testVar)
ttk.Button(mainframe, text="AP1/ON", command=setAP1).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text="AP1/OFF", command=setAP2).grid(column=2, row=2, sticky=W)

# slider
Slider_1 = Scale(root, command=setND, orient=HORIZONTAL, length=200, width=20, sliderlength=10, from_=0,to=100)
# this puts numbers on the bottom , tickinterval=5)
# not sure why grid isnt working correctly 
Slider_1.grid(column=1, row=5, sticky=W)

# entry
entry_1 = Entry(mainframe, width=10, textvariable=course).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="CRS", command=setCRS1).grid(column=3, row=3, sticky=W)
entry_2 = Entry(mainframe, width=10, textvariable=heading).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="HDG", command=setHDG1).grid(column=3, row=4, sticky=W)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# keep on top
root.wm_attributes("-topmost", 1)

root.mainloop()
