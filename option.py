class Option:

    def __init__(self, data):
        self.text = data["text"]
        self.section = data["section"]
        try:
            self.requirement = data["requirement"]
        except KeyError:
            # If the option does not have a requirement, it is just set to none
            self.requirement = None
