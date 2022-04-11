from tkinter import *
import re
import random
import src.constants as const
from src.timer import Timer
from customTk.MyButton import MyButton
from customTk.MyLabel import MyLabel
import csv

class Game(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        
        self.dictNameLabel = MyLabel(self, text=const.CURRDICT, fontType=1, fg='#c17b9f')
        self.dictNameLabel.pack()
        
        self.infoFrame = Frame(self, bg='pink')
        self.infoFrame.pack(side=TOP, fill=X, padx=90, pady=10)
        self.infoFrame.grid_columnconfigure(1, weight=1)

        self.timer = Timer(self.infoFrame, controller)

        self.definition = MyLabel(self, text="", width=200)
        self.definition.pack(pady=25)

        self.underscores = MyLabel(self, text="",width=200)
        self.underscores.pack(pady=2)

        self.wordValue = StringVar()
        self.wordValue.trace('w', self.limitInputLength)
        valCommand = (self.register(self.isText), '%S')
        self.entry = Entry(self, font=("Georgia", 17), validate="all", validatecommand=valCommand, textvariable=self.wordValue, justify='center')
        self.entry.bind("<Return>", self.checkEntry)
        self.entry.pack()
        
        self.statusLabel = MyLabel(self, text="", width=90, fg='red')
        self.statusLabel.pack()

        self.checkButton = MyButton(self, text="Check", width=10, command=self.checkEntry, colorLevel=1, fontSize=16)
        self.checkButton.pack(pady=10)

        self.scoreLabel = MyLabel(self.infoFrame, text="")
        self.scoreLabel.grid(row=0, column=0, pady=10)

        self.playAgainButton = MyButton(self, width=20, text="Play Again", command=self.newGame, colorLevel=0)
        self.playAgainButton.pack(pady=10)
        self.dictListButton = MyButton(self, width=20, text="Return to List", command=self.master.master.showDictList, colorLevel=0)
        self.dictListButton.pack(pady=10)

        self.newGame()

    def checkEntry(self, *args):
        if self.entry.get().lower() == self.currKey.lower():
            # correct answer
            self.statusLabel.configure(text="")
            self.entry.delete(0, END)
            self.updateScore()
            if (len(self.remainingKeys) == 0) :
                self.gameEnd(True)
            else:
                self.randomKey()
        else:
            # wrong answer
            if (len(self.remainingKeys) != 0) :            
                self.statusLabel.configure(text="try again")
            if (self.currKey != "") :            
                self.statusLabel.configure(text="try again")
        

    def randomKey(self):
        self.currKey = random.choice(self.remainingKeys)
        self.remainingKeys.remove(self.currKey)
        self.definition.configure(text=self.dictionary[self.currKey])
        underscores = ""
        for char in self.currKey:
            if char in  " -'.":
                underscores += char + " "
            else:
                underscores += "_ "
        self.underscores.configure(text=underscores)
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
        self.scoreLabel.configure(text="Score: " + str(self.score))


    def newGame(self):
        # call this from other scenes before switching to this scene
        self.dictNameLabel.configure(text=const.CURRDICT)
        self.dictionary = const.Db.getDict(const.CURRDICT)
        self.remainingKeys = list(self.dictionary)
        self.currKey = ""
        self.score = 0

        self.timer.destroy()
        self.timer = Timer(self.infoFrame, self.controller)
        self.timer.startTimer(0, len(self.remainingKeys)*const.SECS_PER_WORD)
        
        self.checkButton["state"] = "normal"
        
        self.statusLabel.configure(fg='red')
        self.statusLabel.configure(text="")
        self.scoreLabel.configure(text="Score: " + str(self.score))
        self.scoreLabel.configure(fg='grey')
        self.timer.configFG('grey')
        
        self.playAgainButton.pack_forget()
        self.dictListButton.pack_forget()
        
        self.randomKey()


    def gameEnd(self, won):
        self.definition.configure(text="")
        self.underscores.configure(text="")
        self.currKey = ""

        self.timer.stopTimer()
        self.scoreLabel.configure(fg='black')
        self.timer.configFG('black')

        if won:
            self.statusLabel.configure(fg='green')
            self.statusLabel.configure(text="you win!")
            with open('past_scores.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((const.CURRDICT, self.score))            
        else:
            self.statusLabel.configure(text="game over...")
            with open('past_scores.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow((const.CURRDICT, self.score))            
        
        self.checkButton["state"] = "disabled"

        self.playAgainButton.pack(pady=10)
        self.dictListButton.pack(pady=10)
        
        # TODO save score 
