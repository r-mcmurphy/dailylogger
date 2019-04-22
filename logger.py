class DailyLogger():
	def __init__(self):			# I decided to get rid of schedule here. Instead, logger recounts trackables
		self.trackables = []	# for a particular day of interest. So we don't have to think about
								# how to store this information.
	def log_day(self):
		# Create list of trackackables for the day of interest
		day_of_interest = self.get_day()
		to_log = []
		for trackable in self.trackables:
			if trackable.on_schedule(day_of_interest):
				to_log.append(trackable)
		# Now we need to create the log entry
		entry = {}
		for trackable in to_log:
			entry[trackable.id] = self.request_input(trackable)
		# Now let's save this data in some form: JSON of database - depends on save()
		self.save(entry)

	def get_day(self):
		pass

	def request_input(self, trackable):
		pass

	def save(self, entry):
		pass


class Trackable():
	"""docstring for Trackable"""
	_ID = 0
	def __init__(self):
		# self.question = question
		self.id = self._ID
		self.__class__._ID += 1

t = Trackable()
t1 = Trackable()
t2 = Trackable()
t3 = Trackable()
print(t.id)
print(t1.id)
print(t2.id)
print(t3.id)
print(Trackable._ID)