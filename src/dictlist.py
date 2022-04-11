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
        frame = Frame(self.scroll_frame, pady=5, bg='pink')
        frame.pack(fill=X, expand=1)

        label = Label(frame, width=14, text=name, bg='pink', font=("Garamond", 16))
        label.pack(side=LEFT, expand=1, fill=X)

        playButton = Button(frame, text="Play", width=7, command= lambda: self.playDict(name), highlightbackground='#c17b9f', bg='#c17b9f', fg="black", font=("Georgia"))
        playButton.pack(side=RIGHT)

        if not const.Db.checkIsPreset(name):
            editButton = Button(frame, text="Edit", width=7, command= lambda: self.editDict(name), highlightbackground='pink', bg='pink', fg="black", font=("Georgia"))
            editButton.pack(side=RIGHT)
        else:
            label.configure(width=14+7)

        pastScoresButton = Button(frame, text="Scores", width=7, highlightbackground='pink', bg='pink', fg="black", font=("Georgia"))# TODO command
        pastScoresButton.pack(side=RIGHT)
        


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

        self.scroll_frame.master.bind_all('<MouseWheel>', lambda event: self.on_vertical(event, numDict=len(dictNames)))

        if not preset:
            createDictButton = Button(self.scroll_frame, text="Make New", width=10, command= lambda: self.editDict(""),  highlightbackground='#c17b9f', bg='#c17b9f', fg="black", font=("Georgia"))
            createDictButton.pack(pady=5)

    def on_vertical(self, event, numDict=0):
        if numDict > 9:
            self.scroll_frame.master.yview_scroll(-1 * event.delta, 'units')

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
