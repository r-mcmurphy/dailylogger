class Validator():

	def __init__(self):
		self.types = ["int", "float", "str", "bool", ""]
		self.falses = ["no", "false", "nope", "0", "never", "noway", "n"]

	def validate_type_input(self, inp):
		if inp not in self.types:
			return False
		return True

	def validate_answer(self, ans, trackable):
		"""Returns False if answer is of incorrect type."""
		try:
			answer_type = trackable.get_answer_type()
			ans = answer_type(ans)
			return True
		except ValueError:
			return False

	def process_answer(self, ans, trackable):
		if trackable.get_answer_type() == bool:
			if ans.strip().lower() in self.falses:
				return False
			else:
				return True
		else:
			return ans