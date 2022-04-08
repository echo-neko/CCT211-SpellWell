from tkinter import *

class MainMenu(Frame):
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        #self.statusLabel = tkinter.Label(parent, text="", width= 20)
        #self.statusLabel.grid()
        self.title = Label(self, text="Spell Well", width= 20)
        self.title.pack()
        self.controller = controller
