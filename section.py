from option import Option


class Section:
    def __init__(self, data):
        # Creates a section of a specified type
        self._data = data
        self.type = data["type"]
        self.text = data["text"]

    def get_options(self):
        options = []
        for option in self._data["options"].values():
            options.append(Option(option))
        return options

    def get_item(self):
        return self._data["item"]

    def get_test(self):
        return self._data["test"]
