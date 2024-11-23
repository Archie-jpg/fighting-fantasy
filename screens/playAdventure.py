from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout
from screens.layouts import layoutAdventure, layoutCharacter


class screenPlayAdventure(QGridLayout):
    sig_main_menu = Signal()  # Emitted when the adventure needs to go back to the start screen

    def __init__(self):
        # Sets up the screen with two columns, one for the adventure and the other for the character gui. It then
        # creates instances of both of these, and adds them to the gui,
        super().__init__()
        self.setColumnMinimumWidth(0, 600)
        self.setColumnMinimumWidth(1, 200)
        self.adventure_display = layoutAdventure()
        self.character_display = layoutCharacter()
        self.adventure_display.sig_section_changed.connect(self.update_screen)  # When the adventure moves on, gets both
        # screens to update
        self.adventure_display.sig_return_to_main.connect(self.return_to_main)  # For when the adventure file wants to
        #back to the main screen
        self.addLayout(self.adventure_display, 0, 0)
        self.addLayout(self.character_display, 0, 1)

    def new_adventure(self, title):
        # For when a player starts a new adventure, from the start, with a new character
        character = self.adventure_display.new_adventure(title)
        self.set_character(character)
        self.update_screen()

    def set_character(self, character):
        # Sets the character of the character gui to the specified instance (Needs to be the same as the one in the
        # adventure
        self.character_display.set_character(character)

    def update_screen(self):
        # Gets the two screens to update their graphics
        self.adventure_display.update_contents()
        self.character_display.update_contents()

    def return_to_main(self):
        # Used to return to the main menu
        self.sig_main_menu.emit()
