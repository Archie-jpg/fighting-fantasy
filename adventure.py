from utils import read_adventure
from section import Section
from people.character import Character


class Adventure:

    def __init__(self, title):
        self.data = read_adventure(title)
        self.current_section = None
        self.current_pos = ''
        self.character = Character()

    def start_adventure(self):
        self.character.new_character(int(self.data["gold"]), int(self.data["provisions"]), self.data["equipment"])
        self.go_to("0")

    def go_to(self, section_number):
        if section_number == "-1":
            self.current_section = Section({"text": self.current_section.get_attribute("killed"), "type": "lose"})
        self.current_pos = section_number
        section_data = self.data["sections"][section_number]
        self.current_section = Section(section_data)
