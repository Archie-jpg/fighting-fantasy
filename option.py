class Option:

    def __init__(self, data):
        self.text = data["text"]
        self.section = data["section"]
        try:
            self.requirement = data["requirement"]
            return
        except KeyError:
            self.requirement = None
        try:
            self.cost = int(data["cost"])
        except KeyError:
            self.cost = 0
