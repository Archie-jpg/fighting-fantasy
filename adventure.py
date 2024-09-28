from utils import read_adventure


class Adventure:
    def __init__(self, title, section):
        self.data = read_adventure(title)
        self.section = Section(self.data[section])

    def update_section(self, new_section):
        self.section = Section(self.data[new_section])


class Section:
    def __init__(self, data):
        self.data = data
        self.type = data["type"]
        self.text = data["text"]
        options_data = data["options"]
        self.options = {}
        for opt in options_data:
            print(opt)
            # TODO: Options with requirements
            self.options[opt] = options_data[opt]["section"]