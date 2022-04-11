from tkinter import *
import src.constants as const
from tkinter.font import Font

        
class DictList(Frame):
    '''
    This class is for showing players the dictionary list of the words and definitions
    and it can allow users to edit and create their own dictionaries 
    '''
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
    
        self.controller = controller

        self.presetButton = Button(self, text="Preset", command=lambda: self.showDicts(True), width=10, highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.presetButton.pack(pady=3)

        self.originalButton = Button(self, text="Original", width=10, command=lambda: self.showDicts(False), highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.originalButton.pack(pady=5)

        canvas = Canvas(self, bg='pink')
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scroll_frame = Frame(canvas, bg='pink')
        scrollbar.pack(side="right", fill="y")
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)


    def listADict(self, name):
        label = Label(self.scroll_frame, text=name, bg='pink', font=("Garamond", 18))
        label.pack(pady=3)
        playButton = Button(self.scroll_frame, text="Play", width=10, command= lambda: self.playDict(name), highlightbackground='pink', bg='pink', fg="black", font=("Georgia", 16))
        playButton.pack()
        if not const.Db.checkIsPreset(name):
            editButton = Button(self.scroll_frame, text="Edit", width=10, command= lambda: self.editDict(name), highlightbackground='pink', bg='pink', fg="black", font=("Georgia", 16))
            editButton.pack()
        pastScoresButton = Button(self.scroll_frame, text="Past Scores", width=10, highlightbackground='#c17b9f', bg='#c17b9f', fg="black", font=("Georgia", 16))# TODO command
        pastScoresButton.pack()


    def showDicts(self, preset):
        self.scroll_frame.destroy()
        self.scroll_frame = Frame(self.scroll_frame.master, bg='pink')
        self.scroll_frame.bind(
            "<Configure>",
            lambda e: self.scroll_frame.master.configure(
                scrollregion=self.scroll_frame.master.bbox("all")
            )
        )
        self.scroll_frame.master.create_window((0, 0), window=self.scroll_frame, anchor="nw")

        dictNames = const.Db.getDictNames(preset)
        for name in dictNames:
            self.listADict(name)
        if not preset:
            createDictButton = Button(self.scroll_frame, text="Make New", width=10, command= lambda: self.editDict(""))
            createDictButton.pack()

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
