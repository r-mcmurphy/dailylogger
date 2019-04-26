class Trackable():

	def __init__(self, name, question, answer_type, period=None):
		self.name = name.strip().lower().replace(" ", "_")
		self.question = question.strip()
		self.period = period
		self.answer_type = answer_type
		self.validator = Validator(self)

	def get_type(self):
		if self.answer_type == "bool":
			return bool
		elif self.answer_type == "int":
			return int
		elif self.answer_type == "str":
			return str
		elif self.answer_type == "float":
			return float

	def set_period(self, period):
		pass


class Validator():

	def __init__(self, trackable=None):
		self.trackable = trackable
		self.types = ["int", "float", "str", "bool", ""]
		self.falses = ["no", "false", "nope", "0", "never", "noway", "n"]

	def validate_type_input(self, inp):
		if inp not in self.types:
			return False
		return True

	def validate_answer(self, ans):
		"""Returns False if answer is of incorrect type."""
		try:
			answer_type = self.trackable.get_type()
			ans = answer_type(ans)
			return True
		except ValueError:
			return False

	def process_answer(self, ans):
		if self.trackable.get_type() == bool:
			if ans.strip().lower() in self.falses:
				return False
			else:
				return True
		else:
			return ans