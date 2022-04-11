from tkinter import *
import src.constants as const
from customTk.MyButton import MyButton
from customTk.MyLabel import MyLabel
        
class DictList(Frame):
    '''
    This class is for showing players the dictionary list of the words and definitions
    and it can allow users to edit and create their own dictionaries 
    '''
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
    
        self.controller = controller

        topButtons = Frame(self, bg='pink')
        topButtons.pack()

        self.presetButton = MyButton(topButtons, text="Preset", command=lambda: self.showDicts(True), width=10, colorLevel=0)
        self.presetButton.pack(side=LEFT, pady=10)

        self.originalButton = MyButton(topButtons, text="Original", width=10, command=lambda: self.showDicts(False), colorLevel=0)
        self.originalButton.pack(side=LEFT, pady=10)

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

        label = MyLabel(frame, width=14, text=name)
        label.pack(side=LEFT, expand=1, fill=X)

        playButton = MyButton(frame, text="Play", width=7, colorLevel=1, command= lambda: self.playDict(name))
        playButton.pack(side=RIGHT)

        if not const.Db.checkIsPreset(name):
            editButton = MyButton(frame, text="Edit", width=7, command= lambda: self.editDict(name))
            editButton.pack(side=RIGHT)
        else:
            label.configure(width=14+7)

        pastScoresButton = MyButton(frame, text="Scores", width=7)# TODO command
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
            if len(dictNames) == 0:
                label = Label(self.scroll_frame, width=14, text="", bg='pink', font=("Garamond", 16))
                label.pack(side=LEFT, expand=1, fill=X)
            createDictButton = MyButton(self.scroll_frame, text="Make New", width=10, colorLevel=1, command= lambda: self.editDict(""))
            createDictButton.pack(pady=5)
            
            self.presetButton["state"] = "normal"
            self.originalButton["state"] = "disabled"
        else:
            self.presetButton["state"] = "disabled"
            self.originalButton["state"] = "normal"

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
