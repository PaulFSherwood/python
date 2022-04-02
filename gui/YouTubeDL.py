from tkinter import *
from tkinter import ttk
import os
import itertools
import sys

def DLVideo():
    name = urlName.get()
    one = "youtube-dl --extract-audio --audio-format mp3 -o \"%(title)s.%(ext)s\" \""
    two = "\""
    
    combined = one + name + two
    print(combined)
    os.system( combined )
    pass

#youtube-dl --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" "https://www.youtube.com/watch?v=-A06ELwbRcY"

root = Tk()
root.title("YouTubeDL")

urlName = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0)

# resize stuff
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# buttons
ttk.Button(mainframe, text="YT Link", command=DLVideo).grid(column=2, row=3, sticky=W)
# entry
entry_1 = Entry(mainframe, width=25, textvariable=urlName).grid(column=3, row=3, sticky=W)

# wrap everything in a padding
# so fields arent pressed against each other
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# keep on top
root.wm_attributes("-topmost", 1)
root.mainloop()
