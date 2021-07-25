from tkinter import Toplevel, Label, Tk, Button, Entry, Checkbutton, Frame, StringVar, DISABLED
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
        self.window.title("Lista zadań")
        Button(self.window, text="Nowe zadanie", command=self.newTask).pack(pady=20, padx=100)
        self.frame = Frame(self.window, height=50)
        self.frame.pack(pady=20)
        Frame(self.window).pack(pady=10)
        fileList = Read.readFile()
        for task in fileList:
            var = StringVar()
            var.set(task)
            self.addTask(var)

    def newTask(self):
        def addTask():
            self.addTask(task)
            ntw.destroy()

        ntw = Toplevel()
        task = StringVar()
        Label(ntw, text="Wpisz zadanie do wykonania").pack(pady=10)
        entryBox = Entry(ntw, width=40, textvariable=task)
        entryBox.pack(pady=10, padx=10)
        Button(ntw, text="Dodaj zadanie", command=addTask).pack(pady=20)

    def addTask(self, task):
        def doneThread():
            checkButt["state"] = DISABLED
            Thread(target=self.doneTask, args=(checkButt, task)).start()

        def edit(event):
            self.editTask(task)

        if task != "":
            checkButt = Checkbutton(self.frame, textvariable=task, command=doneThread)
            checkButt.bind("<Button-3>", edit)
            checkButt.pack(pady=2)
            self.strVarList.append(task)
            Save.saveFile(self.strVarList)

    def doneTask(self, checkButt, task):
        checkButt.configure(fg='gray')
        sleep(1)
        checkButt.destroy()
        self.strVarList.remove(task)
        Save.saveFile(self.strVarList)

    def editTask(self, task):
        editWindow = Toplevel()
        Label(editWindow, text="Edytuj zadanie").pack(pady=10)
        entryBox = Entry(editWindow, width=40, textvariable=task)
        entryBox.pack(pady=10, padx=10)
        editWindow.wait_window()
        Save.saveFile(self.strVarList)
