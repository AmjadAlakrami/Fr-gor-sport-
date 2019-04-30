from tkinter import *
import tkinter as ttk
from ttk import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label( topFrame, text="Välj antal frågor :")
label1.grid(row=0, sticky=E)

label2 = Label( topFrame, text="Välj svårighetsgraden :")
label2.grid(row=1, sticky=E)

label3 = Label( topFrame, text="Välj Katigorien :")
label3.grid(row=2, sticky=E )

TextINP1= Entry(topFrame, )
TextINP1.grid(row=0, column=1 )

# Checkbox1= Checkbutton(topFrame, text="Medium")
# Checkbox1.grid(row=1, column=1, sticky=E)
# Checkbox2= Checkbutton(topFrame, text="Easy" )
# Checkbox2.grid(row=1, column=1, sticky=W
# Checkbox3= Checkbutton(topFrame, text="Hard" )
# Checkbox3.grid(row=1, column=2, sticky=W)
# Checkbox4= Checkbutton(topFrame, text="Random" )
# Checkbox4.grid(row=1, column=3, sticky=W)

TextINP3= Entry(topFrame, )
TextINP3.grid(row=2, column=1 )

knapp = Button(bottomFrame, text="Submit")
knapp.pack()
# Create a Tkinter variable

choices = [ "dasds","Medium","Hard"]
tkvar = StringVar()
tkvar.set(choices[1])
popupMenu = OptionMenu(root, tkvar, *choices)
popupMenu.pack()
root.mainloop()