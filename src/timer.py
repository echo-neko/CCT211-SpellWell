from cgitb import text
from tkinter import *
from customTk.MyLabel import MyLabel
from tkinter.font import Font

# source: https://www.geeksforgeeks.org/create-countdown-timer-using-python-tkinter/

class Timer(Frame):

    stop = False

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=50)
        self.controller = controller
        
        # Declaration of variables
        self.minute=StringVar()
        self.second=StringVar()
        
        # setting the default value as 0
        self.minute.set("00")
        self.second.set("00")
        
        # Use of Entry class to take input from the user
        minuteLabel = MyLabel(self.master, textvariable=self.minute)
        minuteLabel.grid(row=0, column=2, padx=5)
        
        textLabel = MyLabel(self.master, text=":")
        textLabel.grid(row=0, column=3)

        secondLabel = MyLabel(self.master, textvariable=self.second)
        secondLabel.grid(row=0, column=4, padx=5)

        self.labels = [minuteLabel, textLabel, secondLabel]


    def setTimer(self):
        if self.temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(self.temp,60)
    
            # using format () method to store the value up to
            # two decimal places
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))
            # updating the GUI window 
            self.update()

            self.temp -= 1

            if not self.stop:
                self.after(1000, self.setTimer)
        elif (not self.stop):
            self.master.master.gameEnd(False)


    def startTimer(self, minute, second):
        self.stop = False
        self.temp =  int(minute)*60 + int(second)
        self.setTimer()

    def stopTimer(self):
        self.stop = True
        
    def configFG(self, color):
        for label in self.labels:
            label.configure(fg=color)