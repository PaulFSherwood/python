import sys
from tkinter import *
def mHello():
    mlabel = Label(mGui, text='Hello World').pack()
mGui = Tk()

# if geometry is removed the whole screen is shrunk down
mGui.geometry("450x450+200+200")
mGui.title("My Youtube Tkinter")

mlabel = Label(mGui, text='My Label').pack()

mButton = Button(mGui,text ='OK',command = mHello, fg = 'red',bg = 'blue').pack()


mGui.mainloop()
