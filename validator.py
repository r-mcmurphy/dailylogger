class Validator:
    def __init__(self):
        self.types = ["int", "float", "str", "bool", ""]
        self.falses = ["no", "false", "nope", "0", "never", "noway", "n"]
        self.truths = ['yes', 'yep', '1', 'true', 't', 'ok', 'good', 'sure']

    def validate_input_type(self, inp):
        if inp not in self.types:
            return False
        return True

    @staticmethod
    def validate_range(inp, low, high):
        if low is None and high is None:
            return True
        if float(inp) < low or float(inp) > high:
            return False
        else:
            return True

    @staticmethod
    def validate_name(name, trackables):
        if name == "":
            return False
        for t in trackables:
            if t.name == name:
                return False
        else:
            return True

    @staticmethod
    def validate_question(question):
        if question == "":
            return False
        else:
            return True

    @staticmethod
    def validate_answer_type(ans, trackable):
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
