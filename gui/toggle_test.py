''' tk_button_toggle6.py
using itertools.cycle() to create a Tkinter toggle button
'''
import itertools
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
def toggle(icycle=itertools.cycle([False, True])):
    state = next(icycle)
    t_btn['text'] = str(state)
root = Tk()

t_btn = Button(text="True", width=12, command=toggle)
t_btn.pack(pady=5)
root.mainloop()
