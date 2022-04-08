from tkinter import *
import tkinter
import re
import random
from constants import CURRDICT, DICTS

class Game(Frame):

    dictionary = DICTS[CURRDICT]
    remainingKeys = list(dictionary)
    currKey = "cat"
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        
        self.definition = tkinter.Label(self, text="")
        self.definition.pack()

        self.wordValue = StringVar()
        self.wordValue.trace('w', self.limitInputLength)
        valCommand = (self.register(self.isText), '%S')
        self.entry = tkinter.Entry(self, validate="all", validatecommand=valCommand, textvariable=self.wordValue)
        self.entry.pack()
        
        self.button = tkinter.Button(self, text="Check", width=10, command=self.checkEntry)
        self.button.pack()

        self.statusLabel = tkinter.Label(self, text="", width= 20)
        self.statusLabel.pack()

        self.randomKey()

    def checkEntry(self):
        if self.entry.get().lower() == self.currKey.lower():
            self.statusLabel.configure(text="")
            self.entry.delete(0, END)
            self.randomKey()
        else:
            self.statusLabel.configure(text="try again")
        

    def randomKey(self):
        self.currKey = random.choice(self.remainingKeys)
        self.remainingKeys.remove(self.currKey)
        self.definition.configure(text=self.dictionary[self.currKey])
        self.limitInputLength()


    def isText(self, text):
        alphabetRule = re.compile("[a-zA-Z]+")
        if (re.match(alphabetRule, text)):
            return True
        else:
            return False 

    # source : https://stackoverflow.com/questions/33518978/python-how-to-limit-an-entry-box-to-2-characters-max
    def limitInputLength(self, *args):
        value = self.wordValue.get()
        i = len(self.currKey)
        if len(value) > i: 
            self.wordValue.set(value[:i])