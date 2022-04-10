
from tkinter.font import Font
from tkinter import *

class About(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.parent = parent


        # Define Fonts
        textFont = Font(
	family="Georgia",
	size=18,
        slant="roman",
	underline=0,
	overstrike=0)

        titleFont = Font(
	family="Georgia",
	size=40,
        slant="roman",
	underline=0,
	overstrike=0)

        buttonFont = Font(
	family="Georgia",
	size=20,
        slant="roman",
	underline=0,
	overstrike=0)
        
        self.about_title = Label(self,text="About", bg="pink", font=titleFont)
        self.about_title.pack(pady=20)

        self.about_desc = Label(self, text="Spell Well is a game for learning new words along \n with their definitions. We want to help out all kinds \n of people learning new words or even students \n who need to memorize complicated vocabulary \n for their courses by providing them with a fun way \n of practicing their spelling",  bg="pink", font=textFont)
        self.about_desc.pack(pady=10, padx=10)

        self.how_title = Label(self,text="How to Play", bg="pink", font=titleFont)
        self.how_title.pack(pady=20)

        self.how_desc = Label(self,text="The game is played by answering words \n that match with the definition shown on screen. \n The player’s goal is to guess all the right \n  words in the time provided!",bg="pink", font=textFont)
        self.how_desc.pack(pady=10, padx=10)

        self.preset_desc = Label(self,text="We provide a few preset dictionaries to play with, \n but players have the ability to create unique \n dictionaries with their own terms and definitions as well.",bg="pink", font=textFont)
        self.preset_desc.pack(pady=10, padx=10)

        self.score_desc = Label(self,text="The score will be calculated based on the time spent on each word." , bg="pink", font=textFont)
        self.preset_desc.pack(pady=10, padx=10)
  
        button2= Button(self, text="Play", height=2, width=8,highlightbackground='pink', fg="black", font= buttonFont, command=self.parent.master.showDictList)
        button2.pack(padx=10)

