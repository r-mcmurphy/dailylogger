class Validator():

    def __init__(self):
        self.types = ["int", "float", "str", "bool", ""]
        self.falses = ["no", "false", "nope", "0", "never", "noway", "n"]

    def validate_input_type(self, inp):
        if inp not in self.types:
            return False
        return True

    def validate_range(self, inp, low, high):
        if low == None and high == None:
            return True
        if float(inp) < low or float(inp) > high:
            return False
        else:
            return True

    def validate_name(self, name, trackables):
        if name == "":
            return False
        for t in trackables:
            if t.name == name:
                return False
        else:
            return True

    def validate_question(self, question):
        if question == "":
            return False
        else:
            return True

    def validate_answer_type(self, ans, trackable):
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