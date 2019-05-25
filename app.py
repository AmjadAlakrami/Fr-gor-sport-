from tkinter import * #importera allt from tkinter
import tkinter as tk
from tkinter import font  as tkfont
import requests

root = Tk()

def GET():
    global r 
    r = requests.get('https://opentdb.com/api.php?amount='+TextINP1.get()+'&difficulty='+DefultVar.get().lower()+'&type=boolean')# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
    res = r.json ()
    for data in res ['results']:
        g = data["question"]
        print(g)
        createLabels(g)
    if  w.get() = resulte["correct_answer"] 
    print("hejj")

def createLabels(fraga):
    print(25*"ـ")
    label = tk.Label(root, text= fraga)
    label.grid(column=1)
    w = Entry(root)
    w.grid(column=3, sticky=W )





label1 = Label( root, text="How many questions? ") #skapar en taxtrutta, lägger in det i topframe som vi skapade 
label1.grid(row=0, sticky=E)#lägger den på rad 0 "första raden", så nära komponenten som ligger höger om textruttan
label2 = Label( root, text="Select difficulty :")
label2.grid(row=1, sticky=E)
TextINP1= Entry(root) #skapar en text input
TextINP1.grid(row=0, column=1, sticky=W )# rad 0 kolumn 1 
#skapar en dropdown menu
Level = [ "Easy","Medium","Hard"] #en dictionary på de variabler vi vill ha i menyn
DefultVar = StringVar(root) #skapar en string variabel 
DefultVar.set(Level[0])#sätter variabeln till den första namnet i dictionary
popupMenu = OptionMenu(root, DefultVar, *Level)#skapar en variabel och definerar den som en dropdown menu "OptionMenu", och vi säger att det ska var i topfram, strat värdet ska var string variabel vi skapade och den ska innehålla dictionaryt vi skapade 
popupMenu.grid(row=1, column=1, sticky=W)#positioner 
knapp = tk.Button(root, text="Submit", command= GET)  #skapar en knapp
knapp.grid(row=4, column=1, sticky=W)


root.mainloop()