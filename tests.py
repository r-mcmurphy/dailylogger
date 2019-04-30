import datetime
from time_manager import TimeManager

class DummyTrackable():
	def __init__(self, period):
		self.period = period

day1 = "2019-04-29"	# Monday
day2 = "2019-04-30"	# Tuesday
day3 = "2019-05-01"	# Wednesday
day4 = "2019-05-02"	# Thursday
day5 = "2019-05-03"	# Friday
day6 = "2019-05-04"	# Saturday
day7 = "2019-05-05"	# Sunday

dummy_w1 = DummyTrackable("W1111111")
dummy_w2 = DummyTrackable("W0000000")
dummy_w3 = DummyTrackable("W1000000")
dummy_w4 = DummyTrackable("W0100000")
dummy_w5 = DummyTrackable("W0010000")
dummy_w6 = DummyTrackable("W0001000")
dummy_w7 = DummyTrackable("W0000100")
dummy_w8 = DummyTrackable("W0000010")
dummy_w9 = DummyTrackable("W0000001")

dummy_m1 = DummyTrackable("M29300102030405")
dummy_m2 = DummyTrackable("M29")
dummy_m3 = DummyTrackable("M30")
dummy_m4 = DummyTrackable("M01")
dummy_m5 = DummyTrackable("M02")
dummy_m6 = DummyTrackable("M03")
dummy_m7 = DummyTrackable("M04")
dummy_m8 = DummyTrackable("M05")

dummy_y1 = DummyTrackable("Y0429043005010502050305040505")
dummy_y2 = DummyTrackable("Y0429")
dummy_y3 = DummyTrackable("Y0430")
dummy_y4 = DummyTrackable("Y0501")
dummy_y5 = DummyTrackable("Y0502")
dummy_y6 = DummyTrackable("Y0503")
dummy_y7 = DummyTrackable("Y0504")
dummy_y8 = DummyTrackable("Y0505")

days = [day1, day2, day3, day4, day5, day6, day7]
dummies_w = [dummy_w1, dummy_w2, dummy_w3, dummy_w4, dummy_w5, dummy_w6, dummy_w7, dummy_w8, dummy_w9]
dummies_m = [dummy_m1, dummy_m2, dummy_m3, dummy_m4, dummy_m5, dummy_m6, dummy_m7, dummy_m8]
dummies_y = [dummy_y1, dummy_y2, dummy_y3, dummy_y4, dummy_y5, dummy_y6, dummy_y7, dummy_y8]
thandler = TimeManager()

def perform_weekday_test():
	for dummy_w in dummies:
		print(dummy_w.period)
		for i, day in enumerate(days):
			print(i, thandler.check_date(day, dummy_w))
		print()

def perform_monthday_test():
	for dummy_m in dummies_m:
		print(dummy_m.period)
		for day in days:
			print(day, thandler.check_date(day, dummy_m))
		print()

def perform_yearday_test():
	for dummy_y in dummies_y:
		print(dummy_y.period)
		for day in days:
			print(day, thandler.check_date(day, dummy_y))
		print()

testing = 0
if testing:
	perform_weekday_test()

testing = 0
if testing:
	perform_monthday_test()

testing = 0
if testing:
	perform_yearday_test()