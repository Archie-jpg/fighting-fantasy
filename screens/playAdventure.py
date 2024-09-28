from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QGridLayout

from utils import roll_once, roll_twice
from adventure_classes import Section, Adventure
from custom_widgets import QSectionButton
from screens.layouts import layoutAdventure, layoutCharacter


class screenPlayAdventure(QGridLayout):

    def __init__(self):
        super().__init__()
        self.adventure = None
        self.character = None
        self.setColumnMinimumWidth(0, 600)
        self.setColumnMinimumWidth(1, 200)
        self.setSizeConstraint(QFir)
        self.adventure_display = layoutAdventure()
        self.character_display = layoutCharacter()
        self.adventure_display.sig_section_changed.connect(self.next_section)

        self.addLayout(self.adventure_display, 0, 0)
        self.addLayout(self.character_display, 0, 1)

    def new_adventure(self, title):
        self.adventure = Adventure(title, "0")
        self.update_adventure_display()

    def next_section(self, section):
        self.adventure.update_section(section)
        self.update_adventure_display()

    def update_adventure_display(self):
        self.adventure_display.update_contents(self.adventure.section)

    def update_character_display(self):
        self.character_display.update_contents(self.character)