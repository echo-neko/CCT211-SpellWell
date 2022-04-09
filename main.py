from tkinter import *
from src.game import Game
from src.mainmenu import MainMenu
from src.constants import DB

'''source: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter'''

class SpellWellApp(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Spell Well")

        DB.create_database()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        parent = Frame(self, width=640, height=480)
        
        parent.pack(side="top", fill="both", expand=True)
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, Game):
            page_name = F.__name__
            frame = F(parent=parent, controller=self, width=460, height=480)
            
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            frame.pack_propagate(0)

        self.show_frame("MainMenu")


        def showMainMenu():
            self.show_frame("MainMenu")

        def showGame():
            self.show_frame("Game")
            self.frames["Game"].newGame()

        menubar = Menu(self)
        actionsMenu = Menu(menubar, tearoff=0)
        actionsMenu.add_command(label="MainMenu", command=showMainMenu)
        actionsMenu.add_command(label="Game", command=showGame)
        menubar.add_cascade(label="Menu", menu=actionsMenu)

        self.config(menu=menubar) 

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SpellWellApp()
    app.mainloop()