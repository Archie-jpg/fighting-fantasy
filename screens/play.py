from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot
from classes.character import Character
from utils.custom_widgets import character_display, section_display

class PlayAdventureScreen(QWidget):
    # Signals
    
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
        
    def load_adventure(self, adventure_file: str):
        print(f"Loading {adventure_file}")
        
    def load_character(self, character: Character):
        print(character)
    