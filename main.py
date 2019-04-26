from logger import *
import time


def clear():
	if os.name == 'nt':
		_ = os.system('cls')
	else:
		_ = os.system('clear')

def show_options():
	print()
	print("YYYYMMDD - to pick specific data")
	print("number - n days ago")
	print("'new' to create new trackable")
	print("'q' to exit")
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

def request_trackable_input():
	clear()
	name = input("Enter name of the trackable: ")
	clear()
	question = input("Enter question you want to be asked: ")
	clear()
	answer_type = input("Enter data type of the answer (default str): ")
	clear()
	period = input("How frequently the trackable should be tracked? (default: every day): ")
	clear()
	if answer_type == "":
		answer_type = "str"
	if period == "":
		period = None
	return name, question, answer_type, period

def main():
	logger = DailyLogger()
	entry = {}
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
			n, q, a, p = request_trackable_input()
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
			day = n_days_ago(inp)

	entry[day] = {}
	for t in logger.get_trackables_of_day(day):
		clear()
		print("You are editing data on {}".format(day))
		answer = input(t.question + " ")
		## VALIDATION GOES HERE
		entry[day][t.name] = t.get_type()(answer)
	logger.log_day(entry)
	clear()
	print(day, "successfuly logged!")
	time.sleep(2)
	clear()


main()