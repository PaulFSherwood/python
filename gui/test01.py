import sys
from tkinter import *

mGui = Tk()

# if geometry is removed the whole screen is shrunk down
mGui.geometry("450x450+200+200")
mGui.title("My Youtube Tkinter")

mlabel = Label(text='My Label',fg='red',bg='blue')
# exact location
# mlabel.place(x=200,y=200)
# grid placement
# mlabel.grid(row=0,column=0)
# grid placement (Left adjusted)
mlabel.grid(row=0,column=0, sticky=W)# N E S W(north, east, south, west)

mlabel2 = Label(text='My 2 Label',fg='red',bg='blue')
mlabel2.grid(row=1, column=0)

mlabel3 = Label(text='My 3rd Labelcommand',fg='red',bg='blue')
mlabel3.grid(row=2, column=1,sticky=W)

mGui.mainloop()
