from tkinter import *
import tkinter as ttk
from ttk import *

root = Tk()
root.title("Tk dropdown example")
tkvar = StringVar(root)
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set("aasas")
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.pack()
root.mainloop()