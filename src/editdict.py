from tkinter import *
import re
import src.constants as const

class EditDict(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        
        self.definition = Label(self, text="", bg='pink')
        self.definition.pack()

        self.wordValue = StringVar()
        valCommand = (self.register(self.isText), '%S')
        self.wordEntry = Entry(self, validate="all", validatecommand=valCommand, textvariable=self.wordValue)
        self.wordEntry.pack()

        self.defValue = StringVar()
        self.defEntry = Entry(self, validate="all", validatecommand=valCommand, textvariable=self.defValue)
        self.defEntry.pack()
        
        self.button = Button(self, text="Add", bg='pink' ,width=10, command=self.checkEntry)
        self.button.pack()

        self.statusLabel = Label(self, text="",bg='pink', width=20)
        self.statusLabel.pack()


    def checkEntry(self):
        if self.wordEntry.get().lower() == self.currKey.lower():
            # correct answer
            self.statusLabel.configure(text="", bg='pink')
            self.wordEntry.delete(0, END)
            self.updateScore()
            if (len(self.remainingKeys) == 0) :
                self.gameEnd(True)
            else:
                self.randomKey()
        else:
            # wrong answer
            if (len(self.remainingKeys) != 0) :            
                self.statusLabel.configure(text="try again",bg='pink')


    def isText(self, text):
        alphabetRule = re.compile("[a-zA-Z -']+")
        if (re.match(alphabetRule, text)):
            return True
        else:
            return False 
