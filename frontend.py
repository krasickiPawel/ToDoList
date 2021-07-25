from tkinter import PhotoImage, Toplevel, Label, Tk, Button, Entry, Checkbutton, Frame, StringVar
from time import sleep
from threading import Thread
from backend import Save, Read


class Main:
    def __init__(self):
        self.window = Tk()
        self.frame = None
        self.strVarList = []
        self.createWindow()

    def run(self):
        self.window.mainloop()

    def createWindow(self):
        Button(self.window, text="Nowe zadanie", command=self.newTask).pack(pady=20, padx=100)
        self.frame = Frame(self.window, height=50)
        self.frame.pack(pady=20)
        fileList = Read.readFile()
        for task in fileList:
            var = StringVar()
            var.set(task)
            self.strVarList.append(var)

    def done(self, checkButt, task):
        checkButt.configure(fg='gray')
        sleep(1)
        checkButt.destroy()
        self.strVarList.remove(task)
        Save.saveFile(self.strVarList)

    def addTask(self, ntw, task):
        def doneThread():
            Thread(target=self.done, args=(checkButt, task)).start()

        def edit(event):
            self.editTask(task)
            Save.saveFile(self.strVarList)

        if task != "":
            checkButt = Checkbutton(self.frame, textvariable=task, command=doneThread)
            checkButt.bind("<Button-3>", edit)
            checkButt.pack(pady=5)
            self.strVarList.append(task)
            Save.saveFile(self.strVarList)
        ntw.destroy()

    @staticmethod
    def editTask(task):
        editWindow = Toplevel()
        Label(editWindow, text="Edytuj zadanie").pack(pady=10)
        entryBox = Entry(editWindow, width=40, textvariable=task)
        entryBox.pack(pady=10, padx=10)

    def newTask(self):
        def addTask():
            self.addTask(ntw, task)

        ntw = Toplevel()
        task = StringVar()
        Label(ntw, text="Wpisz zadanie do wykonania").pack(pady=10)
        entryBox = Entry(ntw, width=40, textvariable=task)
        entryBox.pack(pady=10, padx=10)
        Button(ntw, text="Dodaj zadanie", command=addTask).pack(pady=20)
