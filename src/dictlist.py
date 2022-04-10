from tkinter import *

import src.constants as const


from tkinter.font import Font

        
class DictList(Frame):
    '''
    This class is for showing players the dictionary list of the words and definitions
    and it can allow users to edit and create their own dictionaries 
    '''
   
    currList = []

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
    
        self.controller = controller

        self.presetButton = Button(self, text="Preset", command=lambda: self.showDicts(True), width=10, highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.presetButton.pack(pady=3)


        self.originalButton = Button(self, text="Original", width=10, command=lambda: self.showDicts(False), highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.originalButton.pack(pady=5)


    def listADict(self, name):
        label = Label(self, text=name, bg='pink', font=("Garamond", 18))
        label.pack(pady=3)
        self.currList.append(label)
        playButton = Button(self, text="Play", width=10, command= lambda: self.playDict(name), highlightbackground='pink', bg='pink', fg="black", font=("Georgia", 16))
        playButton.pack()
        self.currList.append(playButton)
        if not const.Db.checkIsPreset(name):
            editButton = Button(self, text="Edit", width=10, command= lambda: self.editDict(name), highlightbackground='pink', bg='pink', fg="black", font=("Georgia", 16))
            editButton.pack()
            self.currList.append(editButton)
        pastScoresButton = Button(self, text="Past Scores", width=10, highlightbackground='#c17b9f', bg='#c17b9f', fg="black", font=("Georgia", 16))# TODO command
        pastScoresButton.pack()
        self.currList.append(pastScoresButton)

        

    def showDicts(self, preset):
        for widget in self.currList:
            widget.destroy()
        dictNames = const.Db.getDictNames(preset)
        for name in dictNames:
            self.listADict(name)
        if not preset:
            createDictButton = Button(self, text="Make New", width=10, command= lambda: self.editDict(""))
            createDictButton.pack()
            self.currList.append(createDictButton)

    def playDict(self, name):
        '''
        Alows player to play with the dictionary 
        '''
        const.CURRDICT = name
        self.master.master.showGame()

    def editDict(self, name):
        '''
        Alows player to edit the dictionary  
        '''
        const.CURRDICT = name
        self.master.master.showEditDict()
