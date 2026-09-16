import json
from pathlib import Path

from classes.sections import Section
from classes.character import Character

from PySide6.QtCore import QObject, Signal

class AdventurePlayer(QObject):
    adventure_folder: str
    character: Character
     
    def __init__(self, adventure_folder: Path, character: Character):
        super().__init__()
        self.adventure_folder = adventure_folder
        self.character = character
        
    def load_section(self, section_number: str) -> Section:
        with open(f"{self.adventure_folder}/{section_number}.json", "r") as file:
            section = Section.create_from_file(section_number, json.load(file))
            self.character.add_items(section.items)
            return section
        
    def character_has_item(self, item: str) -> bool:
        """Checks whether or not character has the given item
        
        Args:
            item (str): Name of item to check for
            
        Returns:
            bool: True if character has item, false otherwise
        """
        return item in self.character.equipment
            
