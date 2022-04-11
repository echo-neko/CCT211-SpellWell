from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image
from customTk.MyButton import MyButton
from customTk.MyLabel import MyLabel


class MainMenu(Frame):
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        
        
        #displays title of the game
        self.title = MyLabel(self, text="Welcome To", width=20, fontType=1)
        self.title2 = MyLabel(self, text="*･｡*☆Spell Well!☆*･｡*･", width=20, fontType=0)

        '''
        src: https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
        '''

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("images/spellwell.png"))

        # Create a Label Widget to display the Image
        self.imglabel = Label(self, image = self.img, bg='pink', width=300)
    
        #nav links
        playButton= MyButton(self, text="Play", height=2, width=19, colorLevel=0, fontSize=20, command=self.master.master.showDictList)
        aboutButton= MyButton(self, text="About", height=2, width=19, colorLevel=0, fontSize=20, command=self.master.master.showAbout)
        
        # pack widgets
        self.title.pack(padx=6)
        self.title2.pack(padx=6)
        self.imglabel.pack(padx=0)
        playButton.pack(pady=3)
        aboutButton.pack(pady=3)
        
        self.controller = controller
        
