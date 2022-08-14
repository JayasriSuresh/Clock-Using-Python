from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('time')

def time():
    string = strftime('%I:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000,time)
lbl = Label(root, font = ('arial',24),
            background = 'black',
            foreground = 'lime')
lbl.pack(anchor = 'center')

time()
mainloop()
