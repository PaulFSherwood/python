from tkinter import *

mGui = Tk()

mGui.geometry('450x600+300+100')
mGui.title('Canvas test')

# Canvas
canvas_1 = Canvas(mGui, height = 300, width = 300, bg='#123456')

canvas_1.create_line(0,0,300,300)

canvas_1.pack()

mGui.mainloop()
