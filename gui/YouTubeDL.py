from tkinter import *
from tkinter import ttk
import os
import itertools
import sys

### class ConsoleText(tk.Text):
###     '''A Tkinter Text widget that provides a scrolling display of console
###     stderr and stdout.'''
### 
###     class IORedirector(object):
###         '''A general class for redirecting I/O to this Text widget.'''
###         def __init__(self,text_area):
###             self.text_area = text_area
### 
###     class StdoutRedirector(IORedirector):
###         '''A class for redirecting stdout to this Text widget.'''
###         def write(self,str):
###             self.text_area.write(str,False)
### 
###     class StderrRedirector(IORedirector):
###         '''A class for redirecting stderr to this Text widget.'''
###         def write(self,str):
###             self.text_area.write(str,True)
### 
###     def __init__(self, master=None, cnf={}, **kw):
###         '''See the __init__ for Tkinter.Text for most of this stuff.'''
### 
###         tk.Text.__init__(self, master, cnf, **kw)
### 
###         self.started = False
###         self.write_lock = threading.Lock()
### 
###         self.tag_configure('STDOUT',background='white',foreground='black')
###         self.tag_configure('STDERR',background='white',foreground='red')
### 
###         self.config(state=tk.DISABLED)
### 
###     def start(self):
### 
###         if self.started:
###             return
### 
###         self.started = True
### 
###         self.original_stdout = sys.stdout
###         self.original_stderr = sys.stderr
### 
###         stdout_redirector = ConsoleText.StdoutRedirector(self)
###         stderr_redirector = ConsoleText.StderrRedirector(self)
### 
###         sys.stdout = stdout_redirector
###         sys.stderr = stderr_redirector
### 
###     def stop(self):
### 
###         if not self.started:
###             return
### 
###         self.started = False
### 
###         sys.stdout = self.original_stdout
###         sys.stderr = self.original_stderr
### 
###     def write(self,val,is_stderr=False):
### 
###         #Fun Fact:  The way Tkinter Text objects work is that if they're disabled,
###         #you can't write into them AT ALL (via the GUI or programatically).  Since we want them
###         #disabled for the user, we have to set them to NORMAL (a.k.a. ENABLED), write to them,
###         #then set their state back to DISABLED.
### 
###         self.write_lock.acquire()
###         # self.config(state=tk.NORMAL)
### 
###         self.insert('end',val,'STDERR' if is_stderr else 'STDOUT')
###         self.see('end')
### 
###         # self.config(state=tk.DISABLED)
###         self.write_lock.release()
        
        

def setCRS1():
    name = urlName.get()
    one = "youtube-dl --extract-audio --audio-format mp3 -o \"%(title)s.%(ext)s\" \""
    two = "\""
    
    combined = one + name + two
    print(combined)
    os.system( combined )
    pass

#youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=p6j2edNPMXc&t=929s"

root = Tk()
root.title("YouTubeDL")

urlName = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

# resize stuff
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# buttons
ttk.Button(mainframe, text="YT Link", command=setCRS1).grid(column=2, row=3, sticky=W)
# entry
entry_1 = Entry(mainframe, width=25, textvariable=urlName).grid(column=3, row=3, sticky=W)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# keep on top
root.wm_attributes("-topmost", 1)
root.mainloop()
