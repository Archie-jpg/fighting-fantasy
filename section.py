from option import Option


class Section:
    def __init__(self, data):
        # Creates a section of a specified type
        self.data = data
        self.type = data["type"]
        self.text = data["text"]
        self.options = []
        try:
            for option in data["options"].values():
                self.options.append(Option(option))
        except KeyError:
            pass

    def get_item(self):
        return self.data["item"]
