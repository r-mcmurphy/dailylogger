
import os
import sys
import time
import datetime

from trackable import Trackable
from validator import Validator
from time_manager import TimeManager
from log_manager import LogManager, LOG_FILE

log_mgr = LogManager()
time_mgr = TimeManager()
validator = Validator()

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def home_view():
	while 1:
		clear()
		print("Daily Logger v.2.0\n")
		print("  Press Enter to log a day\n")
		print("  n  >  create new trackable")
		print("  d  >  delete existing trackable")
		# print("  e  >  edit existing trackable") # Coming soon
		print("  l  >  list trackables")
		print("  s  >  show log")
		print("  q  >  exit\n")
		inp = input("What do you want? ").strip().lower()
		if inp == "":
			log_mgr_menu_view()
		elif inp == "n":
			creation_view()
		elif inp == "d":
			deletion_view()
		elif inp == "e":
			edit_view()
		elif inp == "l":
			list_view()
		elif inp == "s":
			show_log_view()
		elif inp == "q":
			clear()
			sys.exit()
		else:
			pass

def log_mgr_menu_view():
	while 1:
		tday = time_mgr.today()
		clear()
		print("Logger Menu\n")
		print("  Enter   >  log the passed day ({})".format(tday))
		print("  YYMMDD  >  log a particular date")
		print("  num     >  2-digit-max timedelta between today and some point in past")
		print("  h       >  go back home")
		print("  q       >  quit\n")
		inp = input("Specify the day: ").strip().lower()
		day = None
		if inp == "":
			day = tday
		elif inp == "h":
			break
		elif inp == "q":
			clear()
			sys.exit()
		elif len(inp) >= 6:
			day = time_mgr.get_specific_date(inp)
		elif len(inp) <= 2:
			for i in inp:
				if not i.isdigit():
					break
			else:
				day = time_mgr.n_days_ago(inp)
		if day:
			log_mgr_confirmation_view(day)
			break

def log_mgr_confirmation_view(day):
	while 1:
		clear()
		# print("Life Logger v.2.0\n")
		print("\n  You're about to log {}".format(day))
		print("  Enter   >  continue")
		print("  anychar >  abort\n")
		inp = input("Going on?: ").strip().lower()
		if inp == "":
			log_mgr_user_input_view(day)
			break
		else: break

def log_mgr_user_input_view(day):
	entry = {}
	entry[day] = {}
	for t in log_mgr.get_trackables():
		if time_mgr.check_date(day, t) == False:
			continue
		valid = False
		while not valid:
			clear()
			print("You are logging {}\n".format(day))
			answer = input("  " + t.question + " ")
			valid = validator.validate_answer_type(answer, t)
			if valid:
				valid = validator.validate_range(answer, t.low, t.high)
		answer = validator.process_answer(answer, t)
		entry[day][t.name] = t.get_answer_type()(answer)
	log_mgr.log_day(entry)
	clear()
	print(day, "successfuly logged!")
	time.sleep(2)
	clear()

def show_log_view():
	clear()
	print("Your log:")
	with open (LOG_FILE, "r") as f:
		for line in f:
			print(line, end="")
	input("\n\nPress Enter")

def creation_view():	
	valid = False
	while not valid:
		clear()
		n = input("Creating new trackable\n\n  Enter trackable's name: ")
		valid = validator.validate_name(n, log_mgr.get_trackables())
	valid = False
	while not valid:
		clear()
		q = input("Creating new trackable\n\n  Enter the question you want to be asked: ").strip()
		valid = validator.validate_question(q)
	valid = False
	while not valid:
		clear()
		t = input("Creating new trackable\n\n  Enter the answer type (str/bool/int/float) (default str): ").strip().lower()
		valid = validator.validate_input_type(t)
	l, h = None, None
	if t == "int" or t == "float":
		clear()
		l = int(float(input("Creating new trackable\n\n  Enter lower bound (int): ")))
		clear()
		h = int(float(input("Creating new trackable\n\n  Enter upper bound (int, inclusive): ")))
	clear()
	p = input("Creating new trackable\n\n  How frequently the trackable should be tracked? (default: every day): ")
	clear()
	if t == "":
		t = "str"
	if p == "":
		p = "W1111111"
	if q[-1] != "?":
		q += "?"
	q = q.capitalize()
	log_mgr.create_trackable(n,q,t,l,h,p)
	clear()
	print("\n  New trackable created!")
	time.sleep(1)

def list_view():
	clear()
	trackables = log_mgr.get_trackables()
	if len(trackables) == 0:
		print("\n  You have nothing to track yet\n")
	else:
		print("Your trackables:\n")
	for t in trackables:
		print("  - {}".format(t.get_beautiful_name()))
		print("      question: {}".format(t.question))
		print("      type: {}".format(t.answer_type))
		if t.low != None:
			print("      lower: {}".format(t.low))
			print("      upper: {}".format(t.high))
		print("      period: {}\n".format(t.period))
	print("  {} trackables at all\n".format(len(trackables)))
	input("Press Enter")

def deletion_view():
	clear()
	trackables = log_mgr.get_trackables()
	d = { i+1 : t for i, t in enumerate(trackables)}
	print("Deletion Menu\n")
	for i in range(1, len(trackables)+1):
		print("  {} - {}".format(i, d[i].get_beautiful_name()))
	code = input("\nEnter code to delete trackable \nType anything else to abort: ")
	
	if int(code) in d:
		deletion_confirmation_view(d[int(code)])

def deletion_confirmation_view(trackable):
	clear()
	print("\n\nWARNING!\n  You are about to delete '{}' trackable.".format(trackable.get_beautiful_name()))
	inp = input("  Are you sure you want to proceed (y/n)? ")
	if inp == "y" or inp == "Y" or inp == "":
		log_mgr.delete_trackable(trackable)
		clear()
		print("\n  Trackable '{}' is deleted".format(trackable.get_beautiful_name()))
		time.sleep(1.5)
	else:
		clear()
		print("\n\n  No changes made")
		time.sleep(1.5)

def edit_view(): # To edit trackables' names, questions, ranges, and periods
	pass 		 # We don't edit ans_type because it would affect log consistency