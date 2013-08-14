import sys
from tkinter import *

mGui = Tk()

mGui.geometry("450x450+200+200")
mGui.title("My Youtube Tkinter")

mlabel = Label(text='My Label',fg='red',bg='blue')
# exact location
# mlabel.place(x=200,y=200)
# grid placement
mlabel.grid(row=0,column=0)
# mlabel2 = Label(text='My 2 Label',fg='red',bg='blue').pack()

mGui.mainloop()
