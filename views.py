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
		inp = input("What should I do? ").strip().lower()
		if inp == "":
			logger_view()
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

def logger_view():
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
		print("Life Logger v.2.0\n")
		print("  You're about to log {}".format(day))
		print("    Enter  >  continue")
		print("    'l'    >  back to logger menu")
		print("    'q'    >  quit\n")
		inp = input("So?: ").strip().lower()
		if inp == "":
			logger_user_input_view(day)
		elif inp == "l":
			break
		elif inp == "q":
			clear()
			sys.exit()
		else: pass

def logger_user_input_view(day):
	entry = {}
	entry[day] = {}
	for t in logger.get_trackables_of_day(day):
		valid = False
		while not valid:
			clear()
			print("You are editing data on {}".format(day))
			answer = input(t.question + " ")
			valid = validator.validate_answer(answer, t)
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
	input("\n\nPress Enter to quit")
	clear()
	sys.exit()

def creation_view():	
	clear()
	n = input("Creating new trackable\n\n  Enter name of the trackable: ")
	clear()
	q = input("Creating new trackable\n\n  Enter question you want to be asked: ")
	valid = False
	while not valid:
		clear()
		a = input("Creating new trackable\n\n  Enter answer type (str/bool/int/float) (default str): ")
		valid = validator.validate_type_input(a)
	clear()
	p = input("Creating new trackable\n\n  How frequently the trackable should be tracked? (default: every day): ")
	clear()
	if a == "":
		a = "str"
	if p == "":
		p = None
	logger.create_trackable(n, q, a, p)
	clear()
	print("\n\n  New trackable successfuly created!")
	time.sleep(1)
	home_view()

def list_view():
	clear()
	print("Your trackables:\n")
	trackables = logger.get_trackables()
	for t in trackables:
		print("  - {}".format(t.get_beautiful_name()))
	input("\nPress Enter to get back")

def deletion_view():
	pass

def edit_view():
	pass


home_view()