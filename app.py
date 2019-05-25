from tkinter import * #importera allt from tkinter
import requests

def GET (event):
    Antal = TextINP1.get()
    r = requests.get('https://opentdb.com/api.php?amount='+ str(Antal))# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
    res = r.json ()
    for data in res ['results']:
        print(data["question"])


root = Tk()
root.title("Quize") #Namner på Tk fönstret


topFrame = Frame(root)#skapar en  variabel och definerar den som en frame 
topFrame.pack()#packar in det alltså lägger in det i vårt fönser
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


label1 = Label( topFrame, text="How many questions? ") #skapar en taxtrutta, lägger in det i topframe som vi skapade 
label1.grid(row=0, sticky=E)#lägger den på rad 0 "första raden", så nära komponenten som ligger höger om textruttan

label2 = Label( topFrame, text="Select difficulty :")
label2.grid(row=1, sticky=E)

label3 = Label( topFrame, text="Select Category :")
label3.grid(row=2, sticky=E )

TextINP1= Entry(topFrame) #skapar en text input
TextINP1.bind("<Return>", GET)
TextINP1.grid(row=0, column=1, sticky=W )# rad 0 kolumn 1 


#skapar en dropdown menu
Level = [ "Easy","Medium","Hard", "Random"] #en dictionary på de variabler vi vill ha i menyn
DefultVar = StringVar(root) #skapar en string variabel 
DefultVar.set(Level[0])#sätter variabeln till den första namnet i dictionary
popupMenu = OptionMenu(topFrame, DefultVar, *Level)#skapar en variabel och definerar den som en dropdown menu "OptionMenu", och vi säger att det ska var i topfram, strat värdet ska var string variabel vi skapade och den ska innehålla dictionaryt vi skapade 

popupMenu.grid(row=1, column=1, sticky=W)#positioner 


Category = [ "Entertainmetn: Music","Entertainmetn: Video Games","Entertainmetn: Film", "Science: Mathematic", "Science: Computers", "Sport", "General knowledge", "Random"]
DefultVar2 = StringVar(root)
DefultVar2.set(Category[0])
popupMenu2 = OptionMenu(topFrame, DefultVar2, *Category)
popupMenu2 .grid(row=2, column=1, sticky=W )

knapp = Button(bottomFrame, text="Submit")#skapar en knapp
knapp.grid(row=11)



root.mainloop()#kör programmet helt tiden till vi breakar loopen. 