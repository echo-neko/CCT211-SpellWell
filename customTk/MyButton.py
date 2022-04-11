from tkinter import *
from tkinter.font import Font


class MyButton(Button):
    
    def __init__(self, parent, text="", colorLevel=-1, fontSize=-1, height=-1, width=-1, command=None):
        Button.__init__(self, parent, text=text)
        
        bgColors = ['#cca0bb', 
                    '#c17b9f', 
                    'brown3', 
                    'pink'] # default
        if colorLevel >= len(bgColors):
            self.configure(highlightbackground=bgColors[-1], bg=bgColors[-1])
        else:
            self.configure(highlightbackground=bgColors[colorLevel], bg=bgColors[colorLevel])
        
        buttonFont = Font(family="Georgia")
        if fontSize != -1:
            buttonFont = Font(family="Georgia", size=20)
        self.configure(font=buttonFont)

        if height != -1:
            self.configure(height=height)

        if width != -1:
            self.configure(width=width)

        if command:
            self.configure(command=command)
