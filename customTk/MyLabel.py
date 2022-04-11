from tkinter import *
from tkinter.font import Font


class MyLabel(Label):
    
    def __init__(self, parent, text="", colorLevel=-1, fontSize=-1,height=-1, width=-1,command=None):
        Label.__init__(self, parent, text=text)
        
        
        colorLevel = ('pink')
        self.configure(bg=colorLevel)

        if fontSize == 0:
            textFont = Font(family="Georgia",size=15, slant="roman")
            self.configure(font=textFont)
        if fontSize == 1:
            titleFont = Font(family="Georgia",size=35, slant="roman")
            self.configure(font=titleFont)
        if fontSize == 2:
            titleslantFont = Font(family="Georgia",size=40, slant="italic")
            self.configure(font=titleslantFont)
            


        if height != -1:
            self.configure(height=height)

        if width != -1:
            self.configure(width=width)

        if command:
            self.configure(command=command)
