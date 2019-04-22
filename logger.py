import datetime
import json

CONFIG_FILE = "config.json"
LOG_FILE = "daily_log.json"

class DailyLogger():
	def __init__(self):
		self.trackables = []
		self.get_trackables()

	def get_trackables(self):
		with open(CONFIG_FILE) as f:
			data = json.load(f)
		for t in data["trackables"]:
			self.trackables.append(Trackable(t["name"], t["question"], t["period"]))

	def log_day(self):
		day = self.get_day()
		to_log = []
		for trackable in self.trackables:
			if trackable.on_schedule(day): # Maybe this can be changed - let logger cares about scheduling
				to_log.append(trackable)

		entry = {}
		for trackable in to_log:
			entry[trackable.id] = self.request_input(trackable)
		self.save(day, entry)

	def get_day(self): # This can be improved - think of all possible use cases
		td = datetime.datetime.now()
		datestr = td.strftime("%Y-%m-%d")
		return datestr

	def request_input(self, trackable):
		answer = input(trackable.question)
		if trackable.answer_valid(answer):
			return answer
		else:
			return False

	def get_data():
		with open(LOG_FILE) as f:
			data = json.load(f)
		return data

	def save_data(data):
		with open(LOG_FILE, "w") as f:
			json.dump(data, f, indent=2, sort_keys=True)

	def save(self, day, entry):
		data = self.get_data()
		data[day] = entry
		self.save_data(data)

	def add_trackable(self):
		pass


class Trackable():
	
	# Maybe a good way is to save this data in JSON, alongside all the trackables info.
	# This would allow us to keep all trackable info in one place and it would guarantee
	# that we'll be able to keep incrementing ids after program's restart.
	# Or maybe even better idea - create a separate config file where to store all the
	# data on trackables. It can be JSON as well.

	def __init__(self, name, question, period=None):
		self.name = name
		self.question = question
		self.period = period

	def on_schedule(self, day):
		pass

	def set_period(self, period):
		pass