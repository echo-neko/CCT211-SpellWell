from tkinter import *
import re
import random
import src.constants as const
from src.timer import Timer

class Game(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        self.timer = Timer(self, controller)
        
        self.definition = Label(self, text="", bg='pink', font=("Garamond", 18))
        self.definition.pack(pady=25)

        self.underscores = Label(self, text="", bg='pink', font=("Garamond", 25))
        self.underscores.pack(pady=2)

        self.wordValue = StringVar()
        self.wordValue.trace('w', self.limitInputLength)
        valCommand = (self.register(self.isText), '%S')
        self.entry = Entry(self, validate="all", validatecommand=valCommand, textvariable=self.wordValue, justify='center')
        self.entry.pack()
        
        self.button = Button(self, text="Check", width=10, command=self.checkEntry,highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))

        self.button.pack(pady=10)

        self.statusLabel = Label(self, text="",width=20, bg='pink', font=("Garamond", 18))
        self.statusLabel.pack()

        self.scoreLabel = Label(self, text="", width=20, bg='pink', font=("Garamond", 18))
        self.scoreLabel.pack()

        self.newGame()

    def checkEntry(self):
        if self.entry.get().lower() == self.currKey.lower():
            # correct answer
            self.statusLabel.configure(text="", bg='pink', font=("Garamond", 18))
            self.entry.delete(0, END)
            self.updateScore()
            if (len(self.remainingKeys) == 0) :
                self.gameEnd(True)
            else:
                self.randomKey()
        else:
            # wrong answer

            if (len(self.remainingKeys) != 0) :            
                self.statusLabel.configure(text="try again",bg='pink', font=("Garamond", 18))

            if (self.currKey != "") :            
                self.statusLabel.configure(text="try again",bg='pink')

        

    def randomKey(self):
        self.currKey = random.choice(self.remainingKeys)
        self.remainingKeys.remove(self.currKey)
        self.definition.configure(text=self.dictionary[self.currKey])
        self.underscores.configure(text="_ "*len(self.currKey))
        self.limitInputLength()
        self.startMin = int(self.timer.minute.get())
        self.startSec = int(self.timer.second.get())


    def isText(self, text):
        alphabetRule = re.compile("[a-zA-Z -']+")
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

    def updateScore(self):
        secsUsed = (self.startMin*60 + self.startSec) - (int(self.timer.minute.get())*60 + int(self.timer.second.get())) 
        self.score +=  round((const.SECS_PER_WORD / secsUsed) * 10)
        self.scoreLabel.configure(text="Score: " + str(self.score),bg='pink', font=("Garamond", 18))

    def newGame(self):
        # call this from other scenes before switching to this scene
        self.dictionary = const.Db.getDict(const.CURRDICT)
        self.remainingKeys = list(self.dictionary)
        self.timer.destroy()
        self.timer = Timer(self, self.controller)
        self.timer.startTimer(0, len(self.remainingKeys)*const.SECS_PER_WORD)
        self.currKey = ""
        self.score = 0
        self.button["state"] = "normal"
        self.statusLabel.configure(text="",bg='pink', font=("Garamond", 18))
        self.scoreLabel.configure(text="Score: " + str(self.score), font=("Garamond", 18))
        self.randomKey()

    def gameEnd(self, won):
        self.definition.configure(text="", bg='pink', font=("Garamond", 18))
        self.underscores.configure(text="", bg='pink', font=("Garamond", 18))
        self.definition.configure(text="")
        self.underscores.configure(text="")
        self.currKey = ""

        self.timer.stopTimer()
        if won:
            self.statusLabel.configure(text="you win!",bg='pink', font=("Garamond", 18))
        else:
            self.statusLabel.configure(text="game over...",bg='pink', font=("Garamond", 18))
        self.button["state"] = "disabled"
        # TODO save score 
