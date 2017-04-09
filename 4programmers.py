# -*- coding: utf-8 -*-
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog

class GUI:
    def __init__(self, root):
        self.root = root
        self.filePath = StringVar()
        self.filePath.set("Nie wczytano żadnego pliku")
        self.charLength = StringVar()
        self.charLength.set(0)
        self.digitsLength = StringVar()
        self.digitsLength.set(0)
        self.spacesLength = StringVar()
        self.spacesLength.set(0)
        self.entersLength = StringVar()
        self.entersLength.set(0)

        root.title("Program zliczający znaki w zadanym pliku")
        
        topFrame1 = Frame(root)
        topFrame1.pack( side = TOP )
        Label(topFrame1, text="Liczba znaków: ").pack( side = LEFT )
        lblCharLength = Label(topFrame1, textvariable=self.charLength)
        lblCharLength.pack( side = RIGHT )
        
        topFrame2 = Frame(root)
        topFrame2.pack( side = TOP )
        Label(topFrame2, text="Liczba cyfr: ").pack( side = LEFT )
        lblDigitsLength = Label(topFrame2, textvariable=self.digitsLength)
        lblDigitsLength.pack( side = RIGHT )
        
        topFrame3 = Frame(root)
        topFrame3.pack( side = TOP )
        Label(topFrame3, text="Liczba spacji: ").pack( side = LEFT )
        lblSpacesLength = Label(topFrame3, textvariable=self.spacesLength)
        lblSpacesLength.pack( side = RIGHT )
        
        topFrame4 = Frame(root)
        topFrame4.pack( side = TOP )
        Label(topFrame4, text="Liczba enterów: ").pack( side = LEFT )
        lblEntersLength = Label(topFrame4, textvariable=self.entersLength)
        lblEntersLength.pack( side = RIGHT )
        
        bottomFrame = Frame(root)
        bottomFrame.pack( side = BOTTOM )
        
        lblFileName = Label(bottomFrame, textvariable=self.filePath)
        lblFileName.pack( side = LEFT )
        
        btnReadFile = Button(
                bottomFrame,
                text="Wczytaj plik",
                fg="black",
                command=self.importFile)
        btnReadFile.pack( side = RIGHT )
    
    def importFile(self):
        self.filePath.set(tkFileDialog.askopenfilename())
        
        s = open(self.filePath.get()).read()
        self.charLength.set(len(s))
        self.digitsLength.set(sum(c.isdigit() for c in s))
        self.spacesLength.set(sum(c.isspace() for c in s))
        self.entersLength.set(sum(c == "\n" for c in s))
        self.root.update()

root = Tk()
gui = GUI(root)
root.mainloop()
