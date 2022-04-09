from tkinter import *
from src.game import Game
from src.mainmenu import MainMenu
from src.about import About

'''source: https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter'''

class SpellWellApp(Tk):
    
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title("Spell Well")
        

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
            frame.configure(bg='pink')

        self.show_frame("MainMenu")


        def showMainMenu():
            #redirects player to the main menu
            self.show_frame("MainMenu")

        def showGame():
            #shows the game frame/window
            self.show_frame("Game")
            self.frames["Game"].newGame()

        def showScore():
            pass

        def showAbout():
            #shows the about frame/window
            self.show_frame("About")


        menubar = Menu(self)
        actionsMenu = Menu(menubar, tearoff=0)
        actionsMenu.add_command(label="Main Menu", command=showMainMenu)
        actionsMenu.add_command(label="Play", command=showGame)
        actionsMenu.add_command(label="High Scores", command=showScore)
        actionsMenu.add_command(label="About", command=showAbout)
        menubar.add_cascade(label="Menu", menu=actionsMenu)



        self.config(menu=menubar) 

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = SpellWellApp()
    app.mainloop()
