from tkinter import *
from tkinter import ttk
import re
import src.constants as const

class EditDict(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller

        self.dict = {}

        valCommand = (self.register(self.isText), '%S')

        self.nameEntry = Entry(self, validate="all", validatecommand=valCommand)
        self.nameEntry.pack()

        self.table_frame = Frame(self)
        self.table_frame.pack(side=LEFT)
        
        self.currIID = 0
        
        self.definition = Label(self, text="", bg='pink')
        self.definition.pack()

        self.wordEntry = Entry(self, validate="all", validatecommand=valCommand)
        self.wordEntry.pack()

        self.defEntry = Text(self, width = 50 , bg='pink' )
        self.defEntry.pack()
        
        self.wordButton = Button(self, text="Add", bg='pink' ,width=10, command=self.addEntry)
        self.wordButton.pack()

        self.saveButton = Button(self, text="Save and Return to List", command=self.saveReturn,  highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.saveButton.pack()

        self.noSaveButton = Button(self, text="Return to List without Saving",command=self.noSaveReturn, highlightbackground='#cca0bb', bg='#cca0bb', fg="black", font=("Georgia", 16))
        self.noSaveButton.pack()

        self.statusLabel = Label(self, text="", width=20, highlightbackground='pink', bg='pink', fg="black", font=("Georgia", 16))
        self.statusLabel.pack()


    def addEntry(self):
        if self.wordEntry.get() == "":
            self.statusLabel.configure(text="Word cannot be empty")
            return

        if self.defEntry.get("1.0",'end-1c') == "":
            self.statusLabel.configure(text="Definition cannot be empty")
            return

        if self.isText(self.wordEntry.get()):
            if self.wordEntry.get() in list(map(lambda x: x.lower(), list(self.dict))):
                self.a = 0
            else:
                self.dict[self.wordEntry.get()] = self.defEntry.get("1.0",'end-1c')
                self.addRow(self.wordEntry.get(), self.defEntry.get("1.0",'end-1c'))
                self.setText("", "")
                self.statusLabel.configure(text="")
        else:
            self.statusLabel.configure(text="Invalid characters in word")


    def isText(self, text):
        alphabetRule = re.compile("[a-zA-Z -'.]+")
        if (re.match(alphabetRule, text)):
            return True
        else:
            return False 

    def addRow(self, word, definition):
        self.dictTable.insert(parent='',index='end',iid=self.currIID,text='',
                                values=(word, definition))
        self.currIID += 1

    def setText(self, word, definition):
        self.wordEntry.delete(0, END)
        self.wordEntry.insert(0, word)
        self.defEntry.delete("1.0", END)
        self.defEntry.insert("1.0", definition)

    def startNew(self):

        if (self.currIID != 0):
            self.dictTable.destroy()

        self.dictTable = ttk.Treeview(self.table_frame)

        self.dictTable['columns'] = ('word', 'definition')

        self.dictTable.column("#0", width=0,  stretch=NO)
        self.dictTable.column("word",anchor=CENTER, width=80)
        self.dictTable.column("definition",anchor=CENTER,width=80)

        self.dictTable.heading("#0",text="",anchor=CENTER)
        self.dictTable.heading("word",text="Word",anchor=CENTER)
        self.dictTable.heading("definition",text="Definition",anchor=CENTER)
        
        self.dictTable.pack()

        self.currIID = 0

        self.nameEntry.delete(0, END)
        self.setText("", "")

        if (const.CURRDICT != ""):
            # editing existing 
            self.dict = const.Db.getDict(const.CURRDICT)
            for key in list(self.dict):
                self.addRow(key, self.dict[key])
            self.nameEntry.insert(0, const.CURRDICT)
            self.nameEntry['state'] = 'disabled'
        else:
            # creating new
            self.nameEntry.insert(0, "")


    def saveReturn(self):
        if self.nameEntry.get() == "":
            self.statusLabel.configure(text="Dictionary name cannot be empty")
            return

        if not self.isText(self.nameEntry.get()):
            self.statusLabel.configure(text="Invalid characters in dictionary name")
            return

        if const.CURRDICT != self.nameEntry.get():
            # if new name
            # check name does not exist already in user created dicts
            if self.nameEntry.get() not in const.Db.getDictNames(preset=False):
                # delete old dict 
                const.Db.deleteDict(const.CURRDICT)
                const.CURRDICT = self.nameEntry.get()
            else: 
                self.statusLabel.configure(text="Dictionary name already exists")
        const.Db.saveDict(const.CURRDICT, self.dict)
        self.noSaveReturn()

    def noSaveReturn(self):
        self.master.master.showDictList()
