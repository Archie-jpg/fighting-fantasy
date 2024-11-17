from option import Option


class Section():
    def __init__(self, data):
        self.type = data["type"]
        self.text = data["text"]
        self.options = []
        if self.type == "win" or self.type == "lose":
            return
        if self.type == "item":
            self.item = data["item"]
        for option in data["options"].values():
            self.options.append(Option(option))
