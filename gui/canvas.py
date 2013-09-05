from tkinter import *

mGui = Tk()

mGui.geometry('450x600+300+100')
mGui.title('Canvas test')

# Canvas
canvas_1 = Canvas(mGui, height = 300, width = 300, bg='#123456').pack()

mGui.mainloop()
