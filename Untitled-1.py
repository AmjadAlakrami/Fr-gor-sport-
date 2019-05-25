from tkinter import  * 

class Student: 

    def __init__(self, name, age):
        self.name = name
        self.age = age
        studentList.append(self)
        studentName.append(name)
 
def getAge():
    for s in studentList:
        if s.name == selectedStudent.get():
            age.set(s.age)

master = Tk()
 
studentList = []
studentName = []
Student("Amjad", "Easy")
Student("Walid", "Medium")
Student("Alaa", "Hard")

selectedStudent = StringVar(master)
selectedStudent.set(studentName[0])
studentmenu= OptionMenu(master, selectedStudent, *studentName)
studentmenu.pack()

Button= Button(master, text="Select", command=getAge)
Button.pack()

age = StringVar()

agela = Label(master, textvariable=age)
agela.pack()
master.mainloop()