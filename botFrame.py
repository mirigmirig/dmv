__author__ = ''
from Tkinter import *
import tkMessageBox
import sys
import time
import bot_engine
import re

class botFrame(Frame):
    def __init__(self, root, **options):
        Frame.__init__(self, root, options)
        self.root = root
        self.grid()
        self.date_format = StringVar()
        self.date_format.set('Date format mm/dd/yyyy')
        self.frequency = StringVar()
        self.frequency.set('30')
        self.add_elements()
        self.data = {'date': None, 'frequency': None}
        self.bot_engine = bot_engine.BotEngine()


    def add_elements(self):
	#add enries for text and a button to submit
        self.date_label = Label(self, text="Enter the limit date:")
        self.date_label.config(font=('times', 16), justify="right")
        self.date_label.grid(row=2, column=0, columnspan=3)

        self.date_entry = Entry(self, textvariable=self.date_format, width=40, font=30, justify="left")
        self.date_entry.bind('<Button-1>', self.handleEvent)
        self.date_entry.grid(row=5, column=0, columnspan=3)

        self.frequency_label = Label(self, text="Enter the frequency (in minutes):")
        self.frequency_label.config(font=('times', 16))
        self.frequency_label.grid(row=8, column=0, columnspan=3)

        self.frequency_entry = Entry(self, textvariable=self.frequency, width=40, font=30, justify="left")
        self.frequency_entry.grid(row=11, column=0, columnspan=3)

        self.go_button = Button(self, text="GO", padx=15, pady=15, width=15, bd=5, relief=RAISED, fg='black')
        self.go_button.grid(row=16, column=1)
        self.go_button.config(command=lambda: self.run(self.date_format.get(), self.frequency.get()))

    def run(self, date_format, frequency):
        self.data['date'] = date_format
        self.data['frequency'] = frequency
	#do validation: check date format and check that frequency is integer
        res = self.validate(self.data)
        if res:
            tkMessageBox.showerror("ERROR", "The given data is not valid. Reenter,please")
        else:
            self.root.wm_withdraw()
            while True:
		#get the available option
                option = self.bot_engine.get_option(self.data['date'])
                if option != None:
		    result = tkMessageBox.askyesno("Accept?", 'Date : ' + option)
                    #result = ctypes.windll.user32.MessageBoxA(0, 'Date : ' + option, "Accept?", 1)
                    if result == True:
			#if option is accepted apply
                        self.bot_engine.accept(option)
                        self.root.destroy()
                        sys.exit(0)

                time.sleep(int(self.data['frequency']) * 60)

    #clear entry text on click
    def handleEvent(self, event):
        self.date_entry.delete(0, END)

    def validate(self, data):
        model = r'^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/[12]\d\d\d$'
        res = re.compile(model)
        if (res.search(data['date'])) and data['frequency'].isdigit():
            return 0
        return 1





