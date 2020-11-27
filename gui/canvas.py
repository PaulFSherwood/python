from tkinter import *
import time

mGui = Tk()

mGui.geometry('450x600+300+100')
mGui.title('Canvas test')

# Canvas
canvas_1 = Canvas(mGui, height = 300, width = 300, bg='#123456')

canvas_1.create_line(0,0,300,300)

canvas_1.create_oval(100,100,200,200)

canvas_1.create_rectangle(25,24,50,50)

canvas_1.pack()
y = 1
x = 1
mGui.mainloop()
while (x < 90):
    canvas_1.create_line(x,y,200,200).pack()
    time.sleep(1)
    x+=1
    y+=1

