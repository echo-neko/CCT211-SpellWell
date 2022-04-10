from tkinter import *
from tkinter import ttk
import re
import src.constants as const

class EditDict(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller

        self.dict = {}

        self.table_frame = Frame(self)
        self.table_frame.pack(side=LEFT)
        
        self.currIID = 0
        
        self.definition = Label(self, text="", bg='pink')
        self.definition.pack()

        valCommand = (self.register(self.isText), '%S')
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
        if self.isText(self.wordEntry.get()):
            if self.wordEntry.get() not in list(map(lambda x: x.lower(), list(self.dict))):
                self.dict[self.wordEntry.get()] = self.defEntry.get("1.0",'end-1c')
                self.addRow(self.wordEntry.get(), self.defEntry.get("1.0",'end-1c'))
                self.setText("", "")
            else:
                self.statusLabel.configure(text="word is already in dictionary")
        else:
            self.statusLabel.configure(text="invalid characters in word")


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

        if (const.CURRDICT != ""):
            self.dict = const.Db.getDict(const.CURRDICT)
        for key in list(self.dict):
            self.addRow(key, self.dict[key])


    def saveReturn(self):
        const.Db.saveDict(const.CURRDICT, self.dict)
        self.noSaveReturn()

    def noSaveReturn(self):
        self.master.master.showDictList()
