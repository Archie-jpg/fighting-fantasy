from pathlib import Path
from typing import NoReturn

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot
from classes.character import Character
from dialogs.create_character import Create_Character
from utils.custom_widgets import adventure_display, character_display
from classes.adventure_player import AdventurePlayer

class PlayAdventureScreen(QWidget):
    # Signals
    return_to_menu: Signal = Signal()
    
    # Attributes
    adventure_widget: adventure_display.AdventureDisplay
    character_widget: character_display.CharacterDisplay   
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        
        # Adventure Half
        self.adventure_widget = adventure_display.AdventureDisplay()
        self.adventure_widget.return_to_menu.connect(self.return_to_menu.emit)
        self.adventure_widget.retry_adventure.connect(self.retry_adventure)
        self.main_layout.addWidget(self.adventure_widget, 0, 0, 1, 2)
        
        # Character Half
        self.character_widget = character_display.CharacterDisplay()
        self.main_layout.addWidget(self.character_widget, 0, 2)
        
    def create_new_character(self, adventure_folder: str):
        create_character_dialog = Create_Character(adventure_folder)
        result = create_character_dialog.exec()
        if result == 1:
            create_character_dialog.deleteLater()
            self.load(adventure_folder, create_character_dialog.character, "0")
        
    def load(self, adventure_folder: Path, character: Character, start_section: str):
        """Create a new instance of an AdventureReader, and set it as the screens adventure_reader
        
        Args:
            adventure_folder (Path): Path to the folder hte adventure is saved in
        """
        self.adventure_widget.load_adventure(adventure_folder, character, start_section)
        self.character_widget.load_character(character)
        
    @Slot(Path)
    def retry_adventure(self, adventure_folder: Path):
        """Starts the given adventure again

        Args:
            adventure_folder (Path): Where the required adventure is stored
        """
        self.create_new_character(adventure_folder)