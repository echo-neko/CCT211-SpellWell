from tkinter import *
from tkinter import ttk
import re
import src.constants as const
from customTk.MyButton import MyButton
from customTk.MyLabel import MyLabel

class EditDict(Frame):

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller

        self.dict = {}
        self.selected_i = -1

        valCommand = (self.register(self.isText), '%S')

        nameEntryFrame = Frame(self, bg='pink')
        nameEntryFrame.pack()
        nameEntryLabel = MyLabel(nameEntryFrame, text="Dictionary Name: ",fontSize=0)
        nameEntryLabel.pack(side=LEFT)
        self.nameEntry = Entry(nameEntryFrame, width=24, validate="all", validatecommand=valCommand, font=("Georgia",15))
        self.nameEntry.pack(side=LEFT)

        self.table_frame = Frame(self, width=30, bg='pink')
        self.table_frame.pack()
        self.dictTable = ttk.Treeview(self.table_frame)
        self.dictTable.pack()
        
        self.currIID = 0

        wordEntryFrame = Frame(self, bg='pink')
        wordEntryFrame.pack()
        wordEntryLabel = Label(wordEntryFrame, text="Word: ", width=8, anchor=E, bg='pink', font=("Georgia",15))
        wordEntryLabel.pack(side=LEFT)
        self.wordEntry = Entry(wordEntryFrame, width=30, validate="all", validatecommand=valCommand, font=("Georgia"))
        self.wordEntry.pack(side=LEFT, pady=2)

        defEntryFrame = Frame(self, bg='pink')
        defEntryFrame.pack()
        defEntryLabel = Label(defEntryFrame, text="Definition: \n\n\n", width=8, anchor=E, bg='pink', font=("Georgia",15))
        defEntryLabel.pack(side=LEFT)
        self.defEntry = Text(defEntryFrame, width = 30, height= 5, font=("Georgia"))
        self.defEntry.pack(side=LEFT, pady=4)
        
        addDelWordFrame = Frame(self, bg='pink')
        addDelWordFrame.pack()
        self.delWordButton = MyButton(addDelWordFrame, text="Delete" ,width=10, command=self.delEntry, colorLevel=2)
        self.delWordButton.pack(side=LEFT, pady=5, padx=2)
        self.addWordButton = MyButton(addDelWordFrame, text="Add" ,width=10, command=self.addEntry, colorLevel=1)
        self.addWordButton.pack(side=RIGHT, pady=5, padx=2)

        self.statusLabel = Label(self, text="", highlightbackground='pink', bg='pink', fg="red", font=("Georgia"))
        self.statusLabel.pack()

        self.saveButton = MyButton(self, text="Save and Return to List", command=self.saveReturn, width=25, colorLevel=0)
        self.saveButton.pack(pady=5)

        self.delDictButton = MyButton(self, text="Delete Dictionary",command=self.deleteReturn, width=25, colorLevel=2)
        self.delDictButton.pack(pady=5)


    def addEntry(self):
        if self.wordEntry.get() == "":
            self.statusLabel.configure(text="Word cannot be empty")
            return

        if self.defEntry.get("1.0",'end-1c') == "":
            self.statusLabel.configure(text="Definition cannot be empty")
            return

        if self.isText(self.wordEntry.get()):
            if self.selected_i != -1:
                # if editing
                self.dict.pop(self.dictTable.item(self.selected_i)['values'][0])
                self.dictTable.item(self.selected_i, values=(self.wordEntry.get(), self.defEntry.get("1.0", 'end-1c')))
            else:
                # if new word
                self.addRow(self.wordEntry.get(), self.defEntry.get("1.0",'end-1c'))

            self.dict[self.wordEntry.get()] = self.defEntry.get("1.0",'end-1c')
            self.setText("", "")
            self.delWordButton.pack_forget()
            self.statusLabel.configure(text="")
            for item in self.dictTable.selection():
                self.dictTable.selection_remove(item)
            self.selected_i = -1
        else:
            self.statusLabel.configure(text="Invalid characters in word")
            return

    def delEntry(self):
        # selected_ should always be -1 when delete button visible
        self.dict.pop(self.dictTable.item(self.selected_i)['values'][0])
        self.dictTable.delete(self.selected_i)
        self.setText("", "")
        self.delWordButton.pack_forget()
        self.statusLabel.configure(text="")
        for item in self.dictTable.selection():
            self.dictTable.selection_remove(item)
        self.selected_i = -1

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


    def tableClick(self, event):
        self.selected_i = self.dictTable.focus()
        if self.selected_i:
            row = self.dictTable.item(self.selected_i)['values']
            self.setText(row[0], row[1])
        self.delWordButton.pack(side=LEFT, pady=5, padx=2)


    def setText(self, word, definition):
        self.wordEntry.delete(0, END)
        self.wordEntry.insert(0, word)
        self.defEntry.delete("1.0", END)
        self.defEntry.insert("1.0", definition)


    def startNew(self):
        self.dictTable.destroy()

        self.dictTable = ttk.Treeview(self.table_frame)

        self.dictTable['columns'] = ('word', 'definition')

        self.dictTable.column("#0", width=0,  stretch=NO)
        self.dictTable.column("word",anchor=CENTER, width=180)
        self.dictTable.column("definition",anchor=CENTER,width=280)

        self.dictTable.heading("#0",text="",anchor=CENTER)
        self.dictTable.heading("word",text="Word", anchor=CENTER)
        self.dictTable.heading("definition", text="Definition", anchor=CENTER)
        
        # source: https://www.pythontutorial.net/tkinter/tkinter-theme/
        style = ttk.Style(self)
        # set ttk theme to "clam" which support the fieldbackground option
        style.theme_use("clam")
        style.configure("Treeview", rowheight=20, background="#c17b9f", 
                        fieldbackground="#c17b9f", foreground="white", font=("Georgia"))
        style.configure("Treeview.Heading", font=("Garamond"))

        self.dictTable.pack(padx=4)
        self.dictTable.bind("<Double-1>", self.tableClick)

        self.currIID = 0

        self.nameEntry.delete(0, END)
        self.setText("", "")

        self.delWordButton.pack_forget()

        if (const.CURRDICT != ""):
            # editing existing 
            self.dict = const.Db.getDict(const.CURRDICT)
            for key in list(self.dict):
                self.addRow(key, self.dict[key])
            self.nameEntry.insert(0, const.CURRDICT)
        else:
            # creating new
            self.nameEntry.insert(0, "")


    def saveReturn(self):
        # check dict name
        if self.nameEntry.get() == "":
            self.statusLabel.configure(text="Dictionary name cannot be empty")
            return
        if len(self.nameEntry.get()) > 16:
            self.statusLabel.configure(text="Dictionary name cannot exceed 16 characters")
            return
        if not self.isText(self.nameEntry.get()):
            self.statusLabel.configure(text="Invalid characters in dictionary name")
            return

        if const.CURRDICT != self.nameEntry.get():
            # if new name
            # check name does not exist already
            if self.nameEntry.get() not in const.Db.getDictNames(preset=False) and \
                self.nameEntry.get() not in const.Db.getDictNames(preset=True):
                # delete old dict 
                if const.CURRDICT != "":
                    const.Db.deleteDict(const.CURRDICT)
                const.CURRDICT = self.nameEntry.get()
            else: 
                self.statusLabel.configure(text="Dictionary name already exists")
                return
        
        if len(list(self.dict)) == 0:
            self.statusLabel.configure(text="Dictionary is empty")
            return

        const.Db.saveDict(const.CURRDICT, self.dict)
        self.master.master.showDictList()


    def deleteReturn(self):
        if const.CURRDICT != "":
            const.Db.deleteDict(const.CURRDICT)
        self.master.master.showDictList()
