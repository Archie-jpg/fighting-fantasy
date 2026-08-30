from pathlib import Path
from typing import NoReturn

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot
from classes.character import Character
from utils.custom_widgets import character_display, section_display
from classes.adventure_reader import AdventureReader

class PlayAdventureScreen(QWidget):
    # Signals
    
    # Attributes
    adventure_widget: section_display.SectionDisplay
    character_widget: character_display.CharacterDisplay   
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        
        # Adventure Half
        self.adventure_widget = section_display.SectionDisplay()
        self.main_layout.addWidget(self.adventure_widget, 0, 0, 1, 2)
        
        # Character Half
        self.character_widget = character_display.CharacterDisplay()
        self.main_layout.addWidget(self.character_widget, 0, 2)
        
        self.adventure_widget.gain_items.connect(self.give_character_items)
        
    def load_adventure(self, adventure_folder: Path):
        """Create a new instance of an AdventureReader, and set it as the screens adventure_reader
        
        Args:
            adventure_folder (Path): Path to the folder hte adventure is saved in
        """
        self.adventure_widget.load_adventure(adventure_folder)
        
    def load_character(self, character: Character) -> NoReturn:
        """Populate the character display with the adventures character
        
        Args:
            character (Character): Character to be loaded
        """
        self.character_widget.load_character(character)
        
    @Slot(list)
    def give_character_items(self, items: list[str]):
        """Give the character a set of items

        Args:
            items (list[str]): The items to give to the character
        """
        self.character_widget.add_items(items)
    