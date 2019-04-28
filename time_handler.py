import datetime

class TimeHandler():
	def __init__(self):
		pass
		
	def today(self):
		td = datetime.datetime.now()
		year, month, day = td.year, td.month, td.day-1
		if td.hour < 7:
			td = datetime.datetime(year, month, day)
		datestr = td.strftime("%Y-%m-%d")
		return datestr

	def get_specific_date(self, datestr):
		str_res = ""
		for c in datestr:
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

	def n_days_ago(self, n):
		n = int(n)
		return (datetime.datetime.strptime(self.today(),"%Y-%m-%d")-datetime.timedelta(n)).strftime("%Y-%m-%d")

	def check_date(self, day, trackable):
		day = datetime.datetime.strptime(day, "%Y-%m-%d")
		timestmp = trackable.period
		if timestmp[0] == "W":
			for d, ch in enumerate(timestmp[1:]):
				if ch == "1" and day.weekday() == d:
					return True
			else:
				return False
		elif timestmp[0] == "M":
			pass
		elif timestmp[0] == "Y":
			pass
		elif timestmp[0] == "P":
			pass
