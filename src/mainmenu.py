from tkinter import *
from tkinter.font import Font
from PIL import ImageTk, Image





class MainMenu(Frame):
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        #self.statusLabel = tkinter.Label(parent, text="", width= 20)
        #self.statusLabel.grid()
        self.parent = parent

        


        # Define Font

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
	size=40,
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

        # Create a Label Widget to display the text or Image
        self.imglabel = Label(self, image = self.img, bg='pink', width=500 , height=480)
        

        #adds padding
        
        self.title.pack(pady=10)
        self.title2.pack(pady=10)
        self.imglabel.pack()


        #links
       # button1= Button(self, text="About", width=20, bg="pink",font= buttonFont, command=self.parent.master.showAbout())
       # button1.pack(pady=10)

        button2= Button(self, text="Play", width=20, bg="pink",font= buttonFont, command=self.parent.master.showGame())
        button2.pack(pady=10)

        #button2= Button(self, text="View High Scores", width=20, bg="pink",font= buttonFont, command= self.parent.master.showScore())
       # button2.pack(pady=10)
        self.controller = controller
