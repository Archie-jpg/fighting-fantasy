from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout
from screens.layouts import layoutAdventure, layoutCharacter


class screenPlayAdventure(QGridLayout):
    sig_main_menu = Signal()
    def __init__(self):
        super().__init__()
        self.setColumnMinimumWidth(0, 600)
        self.setColumnMinimumWidth(1, 200)
        self.adventure_display = layoutAdventure()
        self.character_display = layoutCharacter()
        self.adventure_display.sig_section_changed.connect(self.update_screen)
        self.adventure_display.sig_return_to_main.connect(self.return_to_main)

        self.addLayout(self.adventure_display, 0, 0)
        self.addLayout(self.character_display, 0, 1)

    def new_adventure(self, title):
        character = self.adventure_display.new_adventure(title)
        self.set_character(character)
        self.update_screen()

    def set_character(self, character):
        self.character_display.set_character(character)

    def update_screen(self):
        self.adventure_display.update_contents()
        self.character_display.update_contents()

    def return_to_main(self):
        self.sig_main_menu.emit()
