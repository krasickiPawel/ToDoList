from tkinter import StringVar, Tk, Entry, Label

if __name__ == '__main__':
    window = Tk()
    varList = []
    var1 = StringVar()
    var1.set("dupa")
    varList.append(var1)
    var2 = StringVar()
    var2.set("cipa")
    varList.append(var2)
    print([var.get() for var in varList])

    var1.set("kutas")
    print([var.get() for var in varList])

    Entry(window, textvariable=var1).pack()
    Label(window, textvariable=var1).pack()
    window.mainloop()


    def readFile():
        try:
            with open("C:\\Users\\Paweł\\Documents\\ToDoList\\xd.txt", 'r') as fileObject:
                fileList = fileObject.readlines()
            return fileList
        except FileNotFoundError:
            return "Plik nie istnieje"

    print()
    print(readFile())
