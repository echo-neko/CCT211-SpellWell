from tkinter.font import Font
from tkinter import *
from customTk.MyButton import MyButton

class About(Frame):
    '''
    This class is for the about page, the about page entails the decription about the game and how to play it
    '''

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)

        # Define Fonts
        textFont = Font(
	family="Georgia",
	size=15,
        slant="roman",
	underline=0,
	overstrike=0)

        titleFont = Font(
	family="Georgia",
	size=37,
        slant="roman",
	underline=0,
	overstrike=0)
        
        self.about_title = Label(self,text="About", bg="pink", font=titleFont)
        self.about_title.pack(pady=8)

        self.about_desc = Label(self, text="Spell Well is a game for learning new words along with their definitions. We want to help out all kinds of people learning new words or even students who need to memorize complicated vocabulary for their courses by providing them with a fun way of practicing their spelling", wraplength=450, bg="pink", font=textFont)
        self.about_desc.pack()

        self.how_title = Label(self,text="How to Play", bg="pink", font=titleFont)
        self.how_title.pack(pady=8)

        self.how_desc = Label(self,text="The game is played by answering words that match with the definition shown on screen. The player’s goal is to guess all the right words in the time provided!", wraplength=450, bg="pink", font=textFont)
        self.how_desc.pack()

        self.preset_desc = Label(self,text="We provide a few preset dictionaries to play with, but players have the ability to create unique dictionaries with their own terms and definitions as well. The score will be calculated based on the time spent on each word.", wraplength=450, justify="center", bg="pink", font=textFont)
        self.preset_desc.pack()

        playButton= MyButton(self, text="Play", height=2, width=8, colorLevel=1, command=self.master.master.showDictList)
        playButton.pack(pady=3)

