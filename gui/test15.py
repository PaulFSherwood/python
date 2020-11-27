import sys
from tkinter import *

mGui = Tk()

# if geometry is removed the whole screen is shrunk down
mGui.geometry("450x450+200+200")
mGui.title("My Youtube Tkinter")

mlabel = Label(text='My Label',fg='red',bg='blue')


# Canvas
canvas_1 = Canvas(mGui, height=300, width=300,bg="white").pack()


mGui.mainloop()

