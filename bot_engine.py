from Tkinter import *
import time
import sys
import re
from  bot_gui import BotGUI
import datetime

try:
	from mechanize import Browser
except ImportError:
	print "Unable to import the Mechanize module"
try:
	from bs4 import BeautifulSoup
except ImportError:
	print "Unable to import BeautifulSoup"



class BotEngine(object):
	
	def __init__(self):
		#the data is fake, should be changed to real one, later will be added gui to insert and validation
		self.personal_info = {'officeId':'556', 'firstName' :'MOO', 'lastName' : 'GOO', 'permitNum' : 'Y123456', 'birthdate':('09', '06', '1956'), 'phone':('510', '525', '9178')}
		self.response = None
		self.br = None


	def get_option(self, date):
		dt = datetime.datetime.strptime(date, '%m/%d/%Y')
		info  = self.tryReserve(self.personal_info)
		info_dt = datetime.datetime.strptime(info, '%B %d %Y %H:%M')
		print info_dt
		if info_dt.date() < dt.date():
			return info_dt.strftime('%m/%d/%Y %H:%M"')
		else:
			print info_dt.strftime('%m/%d/%Y %H:%M"')
			return None


	def accept(self, date):
		#TO BE CHANGED LATER
		for form in self.br.forms():
    			if form.attrs['id'] == 'ApptForm':
        			self.br.form = form
        			break
		print self.br.form
		#self.response = self.br.submit()
		link = self.br.find_link(name="foaHomeBtn")
                self.response = self.br.follow_link(link)
                print self.response.geturl()

	



	def tryReserve(self, data):
		info = ""

		self.br = Browser()
		self.br.set_handle_robots(False)
		self.br.addheaders = [('User-agent', 'Firefox')]

		self.br.open("https://www.dmv.ca.gov/foa/clear.do?goTo=driveTest&Submit=Behind-the-Wheel+Driving+Test+Appointment")

		self.br.select_form(name='ApptForm')

		self.br.form['firstName'] = data['firstName']
		self.br.form['lastName'] = data['lastName'] 
		self.br.form.set_value(['DT'],name='requestedTask')

		control = self.br.form.find_control("officeId")    
		for item in control.items:
			if item.name == data['officeId']:
				item.selected = True
		self.br.form['dlNumber'] = data['permitNum']
		self.br.form['birthMonth'] = data['birthdate'][0]
		self.br.form['birthDay'] = data['birthdate'][1]
		self.br.form['birthYear'] = data['birthdate'][2]
		self.br.form['telArea'] = data['phone'][0]
		self.br.form['telPrefix'] = data['phone'][1]
		self.br.form['telSuffix'] = data['phone'][2]

		self.response = self.br.submit()


		soup = BeautifulSoup(self.response.read())
		all_alerts = soup.find_all(class_='alert')
		info += all_alerts[1].text 
		res = info.replace(',', "").split(" ")
		res = res[1] + ' '+ res[2]+ ' ' + res[3] + ' ' + res[5]
		return res





