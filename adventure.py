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
        self.go_to("0")
        self.character.new_character(self.data["gold"], self.data["provisions"], self.data["equipment"])

    def go_to(self, section_number):
        self.current_pos = section_number
        section_data = self.data["sections"][section_number]
        self.current_section = Section(section_data)
