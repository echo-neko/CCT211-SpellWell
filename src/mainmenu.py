from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image





class MainMenu(Frame):
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        #self.statusLabel = tkinter.Label(parent, text="", width= 20)
        #self.statusLabel.grid()
        self.parent = parent

        
        # Define Fonts

        mainFont_i = Font(
	family="Georgia",
	size=35,
        slant="italic",
	underline=0,
	overstrike=0)
        
        mainFont = Font(
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
        

        #displays title of the game
        self.title = Label(self, text="Welcome To", width=20,bg="pink", font= mainFont_i)
        self.title2 = Label(self, text="*･｡*☆Spell Well!☆*･｡*･", width=20,bg="pink", font= mainFont)

        '''
        src: https://www.tutorialspoint.com/how-to-place-an-image-into-a-frame-in-tkinter
        '''

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(Image.open("images/spellwell.png"))

        # Create a Label Widget to display the Image
        self.imglabel = Label(self, image = self.img, bg='pink', width=380 , height=360)
    
        
        

 
        #nav links
        button1= Button(self, text="About", height=1, width=5,  highlightbackground='#2f073b', bg='#2f073b', fg="white", font= buttonFont, command=self.parent.master.showAbout)
        

        button2= Button(self, text="Play", height=1, width=5,highlightbackground='#2f073b', bg='#2f073b', fg="white", font= buttonFont, command=self.parent.master.showDictList)
        

        button3= Button(self, text="View High Scores", height=1, width=19, highlightbackground='#2f073b', bg='#2f073b', fg="white", font= buttonFont, command=self.parent.master.showScore)
        
        
        self.title.pack(padx=6) #adds padding
        self.title2.pack(padx=6)
        self.imglabel.pack(padx=0)

        #pack buttons
        button1.pack(padx=20, side=LEFT)
        
        button2.pack(padx=10 , side=LEFT)
        
        button3.pack(padx=20, side=LEFT)

        
        self.controller = controller
        
