import sys
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

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

def mColor():
    mycolor = colorchooser.askcolor()
    mlabel4 = Label(mGui,text=mycolor).pack()
    return

def mOpen():
    myopen = filedialog.askopenfile()
    mlabel4 = Label(mGui,text=myopen).pack()
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
filemenu.add_command(label = "New",   command = mNew)
filemenu.add_command(label = "Open",  command = mOpen)
filemenu.add_command(label = "Save As..")
filemenu.add_command(label = "Color", command = mColor)
filemenu.add_command(label = "Exit",  command = mQuit)
# adding our list to the file button
menubar.add_cascade(label="File", menu=filemenu)

# SetUp 
setupmenu = Menu(menubar, tearoff = 0)
setupmenu.add_checkbutton(label = "Auto")
menubar.add_cascade(label="SetUp", menu = setupmenu)

# Help Menu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Help Docs")
helpmenu.add_command(label = "About", command = mAbout)
# adding our list to the file button
menubar.add_cascade(label  = "Help",  menu    = helpmenu)

# radio buttons
#                                      what gets changed         affected group
#                               name        index                grouping
Radio_1=Radiobutton(mGui, text= "Option 1", value = 1, variable = 'g_1').pack()
Radio_2=Radiobutton(mGui, text= "Option 2", value = 1, variable = 'g_1').pack()
Radio_3=Radiobutton(mGui, text= "Option 3", value = 3, variable = 'g_1').pack()

Radio_4=Radiobutton(mGui, text= "Option 4", value = 4, variable = 'g_2').pack()
Radio_5=Radiobutton(mGui, text= "Option 5", value = 5, variable = 'g_2').pack()
Radio_6=Radiobutton(mGui, text= "Option 6", value = 6, variable = 'g_2').pack()

# Spin box
spinbox1 = Spinbox(mGui, from_ = 5, to = 10, state = NORMAL).pack()

# List box
List1 = Listbox(mGui)
List1.insert(1,'Python')
List1.insert(3,'PHP')
List1.insert(2,'C++')
List1.insert(4,'Perl')
List1.pack()


# add file menu to the screen
mGui.config(menu=menubar)


mGui.mainloop()

