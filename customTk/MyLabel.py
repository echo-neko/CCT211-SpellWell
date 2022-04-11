from tkinter import *
from tkinter.font import Font


class MyLabel(Label):
    
    def __init__(self, parent, text="", fontType=-1, fg='black', height=-1, width=-1, textvariable=None, anchor=None, wraplength=None):
        Label.__init__(self, parent, text=text)
        
        self.configure(bg='pink')

        fonts = [Font(family="Georgia",size=40, slant="italic"), 
                Font(family="Georgia",size=35), 
                Font(family="Georgia",size=15)] # default         
        self.configure(font=fonts[fontType])

        self.configure(fg=fg)

        if height != -1:
            self.configure(height=height)

        if width != -1:
            self.configure(width=width)
        
        if textvariable:
            self.configure(textvariable=textvariable)
        
        if anchor:
            self.configure(anchor=anchor)

        if wraplength:
            self.configure(wraplength=wraplength)
