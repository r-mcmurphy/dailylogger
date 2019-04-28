from daily_logger import DailyLogger, LOG_FILE
from time_handler import TimeHandler
from trackable import Trackable
from validator import Validator
import datetime
import time
import sys
import os

logger = DailyLogger()
validator = Validator()
thandler = TimeHandler()

def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def home_view():
	while 1:
		clear()
		print("Daily Logger v.2.0\n")
		print("  Enter -->   go to the logger")
		print("  'n'   -->   create new trackable")
		print("  'd'   -->   delete existing trackable")
		print("  'e'   -->   edit existing trackable")
		print("  'l'   -->   list all trackables")
		print("  's'   -->   show log contents")
		print("  'q'   -->   exit\n")
		inp = input("What do you want? ").strip().lower()
		if inp == "":
			logger_menu_view()
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

def logger_menu_view():
	while 1:
		tday = thandler.today()
		clear()
		print("Logger Menu\n")
		print("    Enter    -->  log the passed day ({})".format(tday))
		print("    'YYMMDD' -->  log a particular date")
		print("    'num'    -->  2-digit-max timedelta between today and some point in past")
		print("    'h'      -->  go back home")
		print("    'q'      -->  quit\n")
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
			day = thandler.get_specific_date(inp)
		elif len(inp) <= 2:
			for i in inp:
				if not i.isdigit():
					break
			else:
				day = thandler.n_days_ago(inp)
		if day:
			logger_confirmation_view(day)

def logger_confirmation_view(day):
	while 1:
		clear()
		# print("Life Logger v.2.0\n")
		print("\n\n  You're about to log {}".format(day))
		print("    Enter   >  continue")
		print("    anychar >  abort\n")
		inp = input("Going on?: ").strip().lower()
		if inp == "":
			logger_user_input_view(day)
		else: break

def logger_user_input_view(day):
	entry = {}
	entry[day] = {}
	for t in logger.get_trackables():
		if thandler.check_date(day, t) == False:
			continue
		valid = False
		while not valid:
			clear()
			print("You are editing data on {}\n".format(day))
			answer = input("  " + t.question + " ")
			valid = validator.validate_answer_type(answer, t)
			if valid:
				valid = validator.validate_range(answer, t.low, t.high)
		answer = validator.process_answer(answer, t)
		entry[day][t.name] = t.get_answer_type()(answer)
	logger.log_day(entry)
	clear()
	print(day, "successfuly logged!")
	time.sleep(2)
	home_view()

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
		n = input("Creating new trackable\n\n  Enter name of the trackable: ")
		valid = validator.validate_name(n, logger.get_trackables())
	valid = False
	while not valid:
		clear()
		q = input("Creating new trackable\n\n  Enter question you want to be asked: ").strip()
		valid = validator.validate_question(q)
	valid = False
	while not valid:
		clear()
		a = input("Creating new trackable\n\n  Enter answer type (str/bool/int/float) (default str): ")
		valid = validator.validate_input_type(a)
	l, h = None, None
	if a == "int" or a == "float":
		clear()
		l = int(input("Creating new trackable\n\n  Enter lower bound: "))
		clear()
		h = int(input("Creating new trackable\n\n  Enter upper bound (inclusive): "))
	clear()
	p = input("Creating new trackable\n\n  How frequently the trackable should be tracked? (default: every day): ")
	clear()
	if a == "":
		a = "str"
	if p == "":
		p = "W1111111"
	if q[-1] != "?":
		q += "?"
	logger.create_trackable(n, q, a, l, h, p)
	clear()
	print("\n\n  New trackable created!")
	time.sleep(1)

def list_view():
	clear()
	print("Your trackables:\n")
	trackables = logger.get_trackables()
	for t in trackables:
		print("  - {}".format(t.get_beautiful_name()))
	input("\nPress Enter")

def deletion_view():
	clear()
	trackables = logger.get_trackables()
	d = { i+1 : t for i, t in enumerate(trackables)}
	print("Deletion Menu\n")
	for i in range(1, len(trackables)+1):
		print("  {} - {}".format(i, d[i].get_beautiful_name()))
	code = input("\nEnter trackable's code to delete this trackable: ")
	deletion_confirmation_view(d[int(code)])

def deletion_confirmation_view(trackable):
	clear()
	print("\n\nWARNING!\n  You are about to delete '{}' trackable.".format(trackable.get_beautiful_name()))
	inp = input("  Are you sure you want to proceed (y/n)? ")
	if inp == "y" or inp == "Y" or inp == "":
		logger.delete_trackable(trackable)
		clear()
		print("\n\n  Trackable '{}' is deleted".format(trackable.get_beautiful_name()))
		time.sleep(1.5)
	else:
		clear()
		print("\n\n  No changes made")
		time.sleep(1.5)

def edit_view():
	pass