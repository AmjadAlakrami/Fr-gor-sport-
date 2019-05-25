import requests
from tkinter import * 

class Defec:

    def __init__(self, name):
        self.name = name 
        deflist.append(self)
        defname.append(name)

def getdef ():
    for s in deflist:
        if s.name == selecteddef.get():
            name.set(s.name)

        

def s ():
    r = requests.get('https://opentdb.com/api.php?amount=10&difficulty='+ str(name))# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
    res = r.json ()
    for data in res ['results']:
        print(data["question"])

master = Tk()

deflist =[]
defname = []
Defec("easy")
Defec("medium")
Defec("hard")

selecteddef = StringVar(master)
selecteddef.set(defname[0])
defmen = OptionMenu(master, selecteddef, *defname)
defmen.pack()

Button= Button(master, text="Select", command=s)
Button.pack()
name = StringVar()

master.mainloop()