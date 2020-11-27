import sys
from tkinter import *
def mHello():
    # get the value stored in ment
    mtext = ment.get()
    # pass the text to the label
    mlabel2 = Label(mGui,text=mtext).pack()
    return

mGui = Tk()
ment = StringVar()

mGui.geometry("450x450+200+200")
mGui.title("My Youtube Tkinter")

mlabel = Label(mGui, text='My Label').pack()

mButton = Button(mGui,text ='OK',command = mHello, fg = 'red',bg = 'blue').pack()

mEntry = Entry(mGui, textvariable=ment).pack()

mGui.mainloop()
