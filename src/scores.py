from tkinter import *
from customTk.MyButton import MyButton
from customTk.MyLabel import MyLabel

class Scores(Frame):
    '''
    This class is for the scores page, the about page entails the decription about the game and how to play it
    '''

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)

        self.about_title = MyLabel(self, text="Scores...", fontType=1)
        self.about_title.pack(pady=8)

        self.about_desc = MyLabel(self, text="Matplotlib and tkinter did not blend well together... please run the plot.py file in the scores folder to create/update images of graphs in the scores folder for each dictionary.", wraplength=450)
        self.about_desc.pack()

        playButton= MyButton(self, text="Return to List", height=2, colorLevel=1, command=self.master.master.showDictList)
        playButton.pack(pady=5)
