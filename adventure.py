from utils import read_adventure

class Adventure():
    def __init__(self, title, section):
        self.data = read_adventure(title)
        self.section_number = section
        self.section_data = self.data[self.section_number]