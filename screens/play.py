from pathlib import Path
from typing import NoReturn

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot
from classes.character import Character
from utils.custom_widgets import character_display, section_display

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
        
    def load_adventure(self, adventure_folder: Path):
        """Create a new instance of an AdventureReader, and set it as the screens adventure_reader
        
        Args:
            adventure_folder (Path): Path to the folder hte adventure is saved in
        """
        print(f"Loading {adventure_folder.name}")
        
    def load_adventure_intro(self) -> NoReturn:
        """Load the introduction of the adventure into the section display"""
        print(f"Loading adventure")
        
    def load_character(self, character: Character) -> NoReturn:
        """Populate the character display with the adventures character
        
        Args:
            character (Character): Character to be loaded
        """
        self.character_widget.load_character(character)
        
    