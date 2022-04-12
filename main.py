##############################################
# Authors: Hana Dowe, Jasmine Bittu, & Savannah Simmonds
# Professor Micheal Nixon
# Class: CCT 211, Winter 2022
# Programming Assignment #3
# 4/11/2022
##############################################

'''
There are some issues (ex: scrollbar) where some features of tkinter do not work
on mac as they do on windows.

This link refers to the problems mac users are having with tkinter
Therefore it is best to experience this on a windows desktop

Link :https://www.reddit.com/r/Python/comments/q2rpmp/tkinter_for_python_310_broken_on_macos/

'''

from tkinter import *
from src.game import Game
from src.editdict import EditDict
from src.mainmenu import MainMenu
from src.dictlist import DictList
from src.about import About
from src.scores import Scores


'''source: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter'''

class SpellWellApp(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Spell Well")
        
        self.resizable(False, False)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        parent = Frame(self, width=640, height=500)

        
        parent.pack(side="top", fill="both", expand=True)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, Game, EditDict, DictList, About, Scores):
            page_name = F.__name__
            frame = F(parent=parent, controller=self, width=490, height=630)
            
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            frame.pack_propagate(0)
            frame.configure(bg='pink')

        self.show_frame("MainMenu")

        #links for each menu item
        menubar = Menu(self)
        actionsMenu = Menu(menubar, tearoff=0)
        actionsMenu.add_command(label="Main Menu", command=self.showMainMenu)
        actionsMenu.add_command(label="Dictionary List", command=self.showDictList)
        actionsMenu.add_command(label="About", command=self.showAbout)
        menubar.add_cascade(label="Menu", menu=actionsMenu)

        self.config(menu=menubar) 

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def showMainMenu(self):
        #redirects player to the main menu
        self.show_frame("MainMenu")

    def showGame(self):
        #shows the game frame/window
        self.show_frame("Game")
        self.frames["Game"].newGame()

    def showEditDict(self):
        #shows the dictionary edit frame/window
        self.show_frame("EditDict")
        self.frames["EditDict"].startNew()
    
    def showDictList(self):
        # shows the list of games 
        self.show_frame("DictList")
        self.frames["DictList"].showDicts(preset=True)
    
    def showScores(self):
        self.show_frame("Scores")

    def showAbout(self):
        #shows the about frame/window
        self.show_frame("About")

if __name__ == "__main__":
    app = SpellWellApp()
    app.mainloop()
