from PySide6.QtWidgets import QGridLayout

from adventure import Section, Adventure
from screens.layouts import layoutAdventure, layoutCharacter
from character import Character


class screenPlayAdventure(QGridLayout):

    def __init__(self):
        super().__init__()
        self.adventure = None
        self.character = Character()
        self.setColumnMinimumWidth(0, 600)
        self.setColumnMinimumWidth(1, 200)
        self.adventure_display = layoutAdventure()
        self.character_display = layoutCharacter()
        self.adventure_display.sig_section_changed.connect(self.next_section)

        self.addLayout(self.adventure_display, 0, 0)
        self.addLayout(self.character_display, 0, 1)

    def new_adventure(self, title):
        self.adventure = Adventure(title, "0")
        self.update_adventure_display()
        self.character.new_character(self.adventure.data["gold"], self.adventure.data["provisions"], self.adventure.data["equipment"])
        self.update_character_display()

    def next_section(self, section):
        self.adventure.update_section(section)
        current_section = self.adventure.section
        self.update_adventure_display()
        if current_section.type == "item":
            self.equipment_section(current_section.data["item"])

    def equipment_section(self, item):
        self.character.gain_item(item)
        self.adventure_display.item_section(item)
        self.update_character_display()

    def update_adventure_display(self):
        self.adventure_display.update_contents(self.adventure.section, self.character.equipment)

    def update_character_display(self):
        self.character_display.update_contents(self.character)
