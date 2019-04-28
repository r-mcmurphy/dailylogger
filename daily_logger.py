import os
import json
import datetime
from trackable import Trackable


TRACKABLES_FILE = "trackables.json"
LOG_FILE = "daily_log.json"

class DailyLogger():
	def __init__(self):
		self.check_files()
		self.trackables = []
		for t in self.restore_trackables():
			self.trackables.append(Trackable(t["name"], t["question"], t["answer_type"], t["low"], t["high"], t["period"]))

	def check_files(self):
		if TRACKABLES_FILE not in os.listdir():
			data = {"trackables":[]}
			with open(TRACKABLES_FILE, "w") as f:
				json.dump(data, f)
		if LOG_FILE not in os.listdir():
			data = {}
			with open(LOG_FILE, "w") as f:
				json.dump(data, f)

	def restore_trackables(self):
		with open(TRACKABLES_FILE) as f:
			data = json.load(f)
		return data["trackables"]

	def get_trackables(self):
		return self.trackables

	def save_trackables(self):
		with open(TRACKABLES_FILE) as f:
			data = json.load(f)
		data["trackables"] = []
		for t in self.trackables:
			data["trackables"].append({"name":t.name, "question":t.question, "answer_type":t.answer_type, "low":t.low, "high":t.high, "period":t.period})
		with open(TRACKABLES_FILE, "w") as f:
			json.dump(data, f, indent=2, sort_keys=True)

	def create_trackable(self, name, question, answer_type="str", low=None, high=None,  period=None):
		t = Trackable(name, question, answer_type, low, high, period)
		self.trackables.append(t)
		self.save_trackables()

	def delete_trackable(self, t):
		self.trackables.remove(t)
		self.save_trackables()

	def get_trackables_of_day(self, day):
		"""Returns trackables for a specified day"""
		to_log = []
		for trackable in self.trackables:
			to_log.append(trackable)
		return to_log

	def get_log_data(self):
		with open(LOG_FILE) as f:
			data = json.load(f)
		return data

	def save_log_data(self, data):
		with open(LOG_FILE, "w") as f:
			json.dump(data, f, indent=2, sort_keys=True)

	def log_day(self, entry):
		data = self.get_log_data()
		day = list(entry.keys())[0]
		if day not in data:
			data[day] = entry[day]
		else:
			for k in entry[day].keys():
				data[day][k] = entry[day][k]
		self.save_log_data(data)