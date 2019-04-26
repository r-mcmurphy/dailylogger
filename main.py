from dailylogger import DailyLogger
from trackable import Trackable, Validator
import datetime
import time
import sys
import os


def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def show_options():
	print()
	print("    <YYYYMMDD> - to pick specific data")
	print("    <number> - n days ago")
	print("    <'new'>  - to create new trackable")
	print("    <'del'>  - to delete existing trackable")
	print("    <'q'>    - to exit")
	print()

def today():
	td = datetime.datetime.now()
	year, month, day = td.year, td.month, td.day-1
	if td.hour < 7:
		td = datetime.datetime(year, month, day)
	datestr = td.strftime("%Y-%m-%d")
	return datestr

def get_specific_date(inp):
	str_res = ""
	for c in inp:
		if c.isdigit():
			str_res += c
	if len(str_res) == 8:
		year = str_res[:4]
		month = str_res[4:6] if str_res[4]!="0" else str_res[5]
		day = str_res[6:8] if str_res[6]!="0" else str_res[7]
		return datetime.datetime(int(year), int(month), int(day)).date().strftime("%Y-%m-%d")
	elif len(str_res) == 6:
		year = "20"+str_res[:2]
		month = str_res[2:4] if str_res[2]!="0" else str_res[3]
		day = str_res[4:6] if str_res[4]!="0" else str_res[5]
		return datetime.datetime(int(year), int(month), int(day)).date().strftime("%Y-%m-%d")
	else: return None

def n_days_ago(n):
	n = int(n)
	return (datetime.datetime.strptime(today(),"%Y-%m-%d")-datetime.timedelta(n)).strftime("%Y-%m-%d")

def request_trackable_creation_input(validator):
	clear()
	name = input("Enter name of the trackable: ")
	clear()
	question = input("Enter question you want to be asked: ")
	validated = False
	while not validated:
		clear()
		answer_type = input("Enter data type of the answer (default str): ")
		validated = validator.validate_type_input(answer_type)
	clear()
	period = input("How frequently the trackable should be tracked? (default: every day): ")
	clear()
	if answer_type == "":
		answer_type = "str"
	if period == "":
		period = None
	return name, question, answer_type, period

def log_day(day, logger):
	entry = {}
	entry[day] = {}
	for t in logger.get_trackables_of_day(day):
		valid = False
		while not valid:
			clear()
			print("You are editing data on {}".format(day))
			answer = input(t.question + " ")
			valid = t.validator.validate_answer(answer)
		answer = t.validator.process_answer(answer)
		entry[day][t.name] = t.get_type()(answer)
	logger.log_day(entry)
	clear()
	print(day, "successfuly logged!")
	time.sleep(2)

def main():
	logger = DailyLogger()
	validator = Validator()

	day = None
	clear()
	print("Welcome to Life Logger v.2.0!")
	while not day:
		print("Press Enter to track {}.".format(today()))
		inp = input("Type 'help' to see the options: ").strip().lower()
		if inp == "help":
			show_options()
		elif inp == "q":
			sys.exit()
		elif inp == "new":
			n, q, a, p = request_trackable_creation_input(validator)
			logger.create_trackable(n, q, a, p)
			clear()
			print("New trackable successfuly created!")
			time.sleep(1)
			clear()
		elif inp == "":
			day = today()
		elif len(inp) >= 6:
			day = get_specific_date(inp)
		elif len(inp) <= 2:
			for i in inp:
				if not i.isdigit():
					clear()
					break
			else:
				day = n_days_ago(inp)
	log_day(day, logger)
	clear()


main()