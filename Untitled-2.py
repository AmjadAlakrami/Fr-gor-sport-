from tkinter import *
import requests
master = Tk()

def callback():
    r = requests.get('https://opentdb.com/api.php?amount='+ str(a) )# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
    res = r.json ()
    for data in res ['results']:
        print(data["question"])

b = Button(master, text="OK", command=callback)
b.pack()
a = Entry(master)
a.pack()

mainloop()