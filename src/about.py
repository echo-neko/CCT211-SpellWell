
from tkinter import *

class About(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        
        about_title = Label(Frame,text="About", bg="pink")
        self.about_title.pack()

        about_desc = Label(Frame, text="Spell Well is a game for learning new words along with their definitions.We want to help out all kinds of people learning new words or even students who need to memorize complicated vocabulary for their courses by providing them with a fun way of practicing their spelling")
        self.about_desc.pack()

        how_title = Label(Frame,text="How to Play", bg="pink")
        self.how_title.pack()

        how_desc = Label(Frame,text="The game is played by answering words that match with the definition shown on screen. The player’s goal is to guess all the right words in the time provided!",bg="pink")
        self.how_desc.pack()

        preset_desc = Label(Frame,text="We provide a few preset dictionaries to play with, but players have the ability to create unique dictionaries with their own terms and definitions as well.",bg="pink")
        self.preset_desc.pack()

        score_desc = Label(Frame,text="The score will be calculated based on the time spent on each word." , bg="pink")
        self.preset_desc.pack()
  
    
