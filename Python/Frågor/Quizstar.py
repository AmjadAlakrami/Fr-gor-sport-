#Importera olika biblotek
from tkinter import * 
import tkinter as tk
from tkinter import font  as tkfont
import requests
import random

#namn, storlek, bakgrundfärg på tk fönstret
root = Tk()
root.title("Quizstar")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)#så att det inte går att ändra storleken på fönstret

#skapar listor
Answer=[] 
Right_Answers = [] 
User_Answer = []
QuestionList=[]

# Skickar en get request till urlen, och ändra det till json fill
r = requests.get('https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple')
res = r.json ()
f = 0
#Hämtar data från dictionary .. lagra de i olika variabler .. lagra variablerna i olika listor 
for data in res['results']:
    Question = (data['question'])
    Incorrect = (data['incorrect_answers'])
    Correct= (data['correct_answer'])
    QuestionList.append(Question)
    Answer.append(Incorrect)
    Answer[f].append(Correct)
    Right_Answers.append(Correct)
    f += 1 
    random.shuffle(Answer[f-1]) # blanda Answer lista

#En function som tar bort de komponenterna som finns på fönstret efter att vi har kört programmet
#då får vi ett tomt fönster som vi sedan kan skriva frågora på genom att köra Start_Quiz functionen
def Go():
    Image_Label.destroy()
    Text_Label.destroy()
    Start_Mess.destroy()
    Instruction_Label.destroy()
    Start_Button.destroy()
    Start_Quiz()
    
#En function som räknar hur många pöäng man får för varje rättt fråga 
#Den jämför User_Answer listan med Right_Answers, och för varje element som är samma så lägger den 5 i score variabel
#Sen kör den Show_Result och skickar argumenten score 
def Calculate():
    Score = 0
    rand = range(10)
    for i in rand: 
        if User_Answer[i] == Right_Answers[i]:
            Score = Score + 5
    Show_Result(Score)

ques = 0

def Show_Result(Score):
    #tar bort komponenter
    Question_Label.destroy()
    Select1.destroy()
    Select2.destroy()
    Select3.destroy()
    Select4.destroy()
    # Skapar två Label
    Image_Label = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    Image_Label.pack(pady=(50,30))
    Resule_Label = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    Resule_Label.pack()
    FinScore = ("Your Score are: " +str(Score) +" /50")
    #Sätta en bild på image_Label och en text på Resule_Label beronde på värdet på Score
    if Score >= 20:
        img = PhotoImage(file="great.png")
        Image_Label.configure(image=img)
        Image_Label.image = img
        Resule_Label.configure(text="You Are Excellent !!")
        la = tk.Label(root, text=FinScore)
        la.pack()
    elif (Score >= 10 and Score < 20):
        img = PhotoImage(file="ok.png")
        Image_Label.configure(image=img)
        Image_Label.image = img
        Resule_Label.configure(text="You Can Be Better !!")
        la = tk.Label(root, text=FinScore)
        la.pack()
    else:
        img = PhotoImage(file="bad.png")
        Image_Label.configure(image=img)
        Image_Label.image = img
        Resule_Label.configure(text="You Should Work Hard !!")
        la = tk.Label(root, text=FinScore)
        la.pack()

def selected():
    
    global Select1, Select2, Select3, Select4, Question_Label, ques #globala variabler som används från functionen Start_Quiz

    #Hämtar AnserVar värdet som är Radiobutton variabel
    # varje Radiobutton har en variabel som definer vilket av de fyra kompnenterna det är 
    # vi lagrar det värdet i x  
    x = AnswerVar.get()
    AnswerVar.set(-1)#Radiobutton vi valde sist checkas bort 

    
    #läger användarens svar i User_Answer lista beroende på värdet på x
    #Alltså vilket Radiobutton användaren valde 
    if x == 0:
           User_Answer.append(Answer[ques][0])
    elif x == 1:
           User_Answer.append(Answer[ques][1])
    elif x == 2:
           User_Answer.append(Answer[ques][2])
    elif x == 3:
        User_Answer.append(Answer[ques][3])
    
    ques += 1

    # Om ques är mindre än 10, så  ändras texten på Question _Label och Radiobutton komponeneter 
    #Annars så kör den Calculate function
    if ques < 10:
        Question_Label.config(text= QuestionList[ques])
        Select1['text'] = Answer[ques][0]
        Select2['text'] = Answer[ques][1]
        Select3['text'] = Answer[ques][2]
        Select4['text'] = Answer[ques][3]
    else:
        Calculate()

#functionen som skapar Radiobutton komponenter och Question_Label 
def Start_Quiz():
    
    global Select1, Select2, Select3, Select4, Question_Label

 
    Question_Label = Label(
        root, #vilket fänster
        text = QuestionList[0], #vad för text
        font = ("Consolas", 16), #vilken font och vilken storlek 
        justify = "center", #centrera 
        wraplength = 400, #bredden
        background = "#ffffff", #bakgrunds färg
    )
    Question_Label.pack(pady=(100,30)) 
    
    global AnswerVar
   
    AnswerVar = IntVar()
    AnswerVar.set(-1)

    Select1 = Radiobutton(
        root,
        text = Answer[0][0],
        font = ("Times", 12),
        value = 0,
        variable = AnswerVar,
        command = selected, #vilken function som ska köras när man trycker på den komponenten 
        background = "#ffffff",
    )
    Select1.pack(pady=5)

    Select2 = Radiobutton(
        root,
        text = Answer[0][1],
        font = ("Times", 12),
        value = 1,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select2.pack(pady=5)
    
    Select3 = Radiobutton(
        root,
        text = Answer[0][2],
        font = ("Times", 12),
        value = 2,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select3.pack(pady=5)

    Select4 = Radiobutton(
        root,
        text = Answer[0][3],
        font = ("Times", 12),
        value = 3,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select4.pack(pady=5)

img1 = PhotoImage(file="Brain.png")

Image_Label = Label(
    root,
    image = img1,
    background = "#ffffff",
)
Image_Label.pack()

Text_Label = Label(
    root,
    text = "Welcome to Multiple choices Quize",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
Text_Label.pack()
        
img2 = PhotoImage(file="Frame.png")

Start_Button = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    background = "#ffffff",
    command = Go,
)
Start_Button.pack()

Start_Mess = Label(
    root,
    text = "Click Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
Start_Mess.pack(pady=(10,100))

Instruction_Label = Label(
    root,
    text = "This quiz contains 10 questions\nOnce you answer, that will be a final choice\nthink carefully before you select\nGood Luck!",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
Instruction_Label.pack()


root.mainloop()
