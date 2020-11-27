import sys
from tkinter import *
from tkinter import messagebox

def mhello():
    mtext=ment.get()
    mlabel2 = Label(mGui,text=mtext).pack()
    return
def mNew():
    mlabel3 = Label(mGui,text="You Clicked New").pack()
    return
def mAbout():
	# messagebox.showinfo(title="About", message = "This is my About Box")
	# messagebox.showwarning(title="About", message = "This is my About Box")
	messagebox.showerror(title="About", message = "This is my About Box")
	return
def mQuit():
    mExit = messagebox.askyesno(title="Quit", message="Do you want to Quit")
    if mExit > 0:
        mGui.destroy()
        return
mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
mGui.title('My Youtube Tkinter')

mlabel = Label(mGui, text='My Label').pack()

mbutton = Button(mGui, text='OK', command=mhello, fg='red', bg='blue').pack()

mEntry = Entry(mGui, textvariable=ment).pack()

# Menu Construction
# menubar object
menubar=Menu(mGui)

# our list name
filemenu = Menu(menubar, tearoff=0)
# making a list of what will be in the drop down
filemenu.add_command(label="New",command=mNew)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save As..")
filemenu.add_command(label="Exit",command=mQuit)
# adding our list to the file button
menubar.add_cascade(label="File", menu=filemenu)

# Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label="Help Docs")
helpmenu.add_command(label="About",command=mAbout)
# adding our list to the file button
menubar.add_cascade(label="Help", menu=helpmenu)

# add file menu to the screen
mGui.config(menu=menubar)


mGui.mainloop()
