from tkinter import * #importera allt from tkinter
import tkinter as tk
from tkinter import font  as tkfont
import requests
import random



root = Tk()
root.title("Quizstar")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

Answer=[
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
] 

a =(random.sample(range(0 , 4), 4))

Right_Answers = [] 
User_Answer = []

r = requests.get('https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple')# använder get request för att hämta värden från  den urlen, och sedan lagrar de i variabel r
res = r.json ()


def Go():
    Image_Label.destroy()
    Text_Label.destroy()
    Start_Mess.destroy()
    Instruction_Label.destroy()
    Start_Button.destroy()
    Start_Quiz()


def Calculate():
    global User_Answer, Right_Answers
    Score = 0
    if User_Answer[0] == Right_Answers[0]:
            Score = Score + 5
    if User_Answer[1] == Right_Answers[1]:
            Score = Score + 5
    if User_Answer[2] == Right_Answers[2]:
            Score = Score + 5
    if User_Answer[3] == Right_Answers[3]:
            Score = Score + 5
    if User_Answer[4] == Right_Answers[4]:
            Score = Score + 5
    if User_Answer[5] == Right_Answers[5]:
            Score = Score + 5
    if User_Answer[6] == Right_Answers[6]:
            Score = Score + 5
    if User_Answer[7] == Right_Answers[7]:
            Score = Score + 5 
    if User_Answer[8] == Right_Answers[8]:
            Score = Score + 5
    if User_Answer[9] == Right_Answers[9]:
            Score = Score + 5            
    Show_Result(Score)
    print(User_Answer)
    print(Right_Answers)

    
ques = 1
Place = 0

def Show_Result(Score):
    Question_Label.destroy()
    Select1.destroy()
    Select2.destroy()
    Select3.destroy()
    Select4.destroy()
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
    
    global AnswerVar,User_Answer, Right_Answers
    global Select1, Select2, Select3, Select4, Question_Label
    global UserAns1, UserAns2, UserAns3, UserAns4 
    global ques, Place
    x = AnswerVar.get()
    AnswerVar.set(-1)
    b = res['results'][Place]['incorrect_answers'][0],
    c = res['results'][Place]['incorrect_answers'][1],
    d = res['results'][Place]['incorrect_answers'][2],
    e = res['results'][Place]['correct_answer'],

    Answer[Place].append(b)
    Answer[Place].append(c)
    Answer[Place].append(d)
    Answer[Place].append(e)
    Right_Answers.append(e)

    UserAns1 = Answer[Place][a[0]]
    UserAns2 = Answer[Place][a[1]]
    UserAns3 = Answer[Place][a[2]]
    UserAns4 = Answer[Place][a[3]]

    if x == 0:
        User_Answer.append(UserAns1)
    elif x == 1:
        User_Answer.append(UserAns2)
    elif x == 2:
        User_Answer.append(UserAns3)
    elif x == 3:
        User_Answer.append(UserAns4)
    if ques < 10:
        Question_Label.config(text= res['results'][Place]['question'])
        Select1['text'] = UserAns1,
        Select2['text'] = UserAns2,
        Select3['text'] = UserAns3,
        Select4['text'] = UserAns4,
        ques += 1
        Place +=1
        print(x)
    else:
        Calculate()
    
    


def Start_Quiz():
    
    global Select1, Select2, Select3, Select4, Question_Label
    
    Question_Label = Label(
        root,
        text = res['results'][Place]['question'],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    Question_Label.pack(pady=(100,30))

    global AnswerVar
   
    AnswerVar = IntVar()
    AnswerVar.set(-1)
    global UserAns1, UserAns2, UserAns3, UserAns4 
    UserAns1 = StringVar()
    UserAns2 = StringVar()
    UserAns3 = StringVar()
    UserAns4 = StringVar()
   
    Select1 = Radiobutton(
        root,
        text = UserAns1,
        font = ("Times", 12),
        value = 0,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select1.pack(pady=5)

    Select2 = Radiobutton(
        root,
        text = UserAns2,
        font = ("Times", 12),
        value = 1,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select2.pack(pady=5)

    Select3 = Radiobutton(
        root,
        text = UserAns3,
        font = ("Times", 12),
        value = 2,
        variable = AnswerVar,
        command = selected,
        background = "#ffffff",
    )
    Select3.pack(pady=5)

    Select4 = Radiobutton(
        root,
        text = UserAns4,
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
    text = "This quiz contains 10 questions\nOnce you Right_Answers, that will be a final choice\nthink carefully before you select\nGood Luck!",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
Instruction_Label.pack()


root.mainloop()
