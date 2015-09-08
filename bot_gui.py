__author__ = ''

from Tkinter import *
import botFrame
import tkMessageBox



class BotGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title("DMV_BOT")
        self.root.resizable(0, 0)
	self.root.protocol('WM_DELETE_WINDOW', lambda: tkMessageBox.showwarning("Warning!", "Close program through the tray"))
        self.botFrame = botFrame.botFrame(self.root)
        self.botFrame.pack()


    def show(self): 
        self.root.mainloop()


if __name__ == "__main__":
	bg = BotGUI()
	bg.show()
 
