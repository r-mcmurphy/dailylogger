class Trackable():

	def __init__(self, name, question, answer_type, low=None, high=None, period=None):
		self.name = name.strip().lower().replace(" ", "_")
		self.question = question.strip()
		self.period = period
		self.answer_type = answer_type
		self.low = low
		self.high = high

	def get_answer_type(self):
		if self.answer_type == "bool":
			return bool
		elif self.answer_type == "int":
			return int
		elif self.answer_type == "str":
			return str
		elif self.answer_type == "float":
			return float

	def get_beautiful_name(self):
		words = self.name.split("_")
		return " ".join(words).capitalize()