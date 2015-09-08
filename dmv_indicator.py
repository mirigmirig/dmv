import gtk
import pygtk
import appindicator
import os
import subprocess
import signal
import time

class LinuxTray(object):

	def __init__(self):
		self.indicator = appindicator.Indicator("dmv-bot-indicator", gtk.STOCK_EXECUTE, appindicator.CATEGORY_APPLICATION_STATUS)
    		self.indicator.set_status(appindicator.STATUS_ACTIVE)
		self.menu =  gtk.Menu()
		self.build_menu(self.menu)
    		self.indicator.set_menu(self.menu)

	def run_indicator(self):
		gtk.main()

	def quit(self, widget):
		if hasattr(self, 'proc'):
                        #os.killpg(self.proc.pid, signal.SIGTERM)
			self.proc.terminate()
                gtk.main_quit()
	
	def start_bot(self, widget):
		self.start_item.set_sensitive(False)
		self.proc = subprocess.Popen(["python", "bot_gui.py"])

	def build_menu(self, menu):
		menuTitle = "Start Bot"
                self.start_item = gtk.MenuItem(menuTitle)
                menu.append(self.start_item)
                self.start_item.connect("activate", self.start_bot)
		self.start_item.set_sensitive(True)
                self.start_item.show()


		menuTitle = "Quit"
                quit_item = gtk.MenuItem(menuTitle)
		menu.append(quit_item)
                quit_item.connect("activate", self.quit)
		quit_item.show()
                

	






		
