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
        
    # def load_intro(self) -> Section:
    #     """Gets the introduction to the adventure
        
    #     Returns:
    #         (str): A paragraph introducing the adventure
    #     """
    #     with open(f"{self.adventure_folder}/introduction.txt", "r") as file:
    #         intro: str = file.read()
    #         first_option: dict = {"text": "Begin Adventure", "section": "1"}
    #         return Section("0", intro, [], [first_option])
        
    def load_section(self, section_number: str) -> Section:
        with open(f"{self.adventure_folder}/{section_number}.json", "r") as file:
            section = Section.create_from_file(section_number, json.load(file))
            for opt in section.options: 
                if opt.requirement != "" and opt.requirement not in self.character.equipment:
                    opt.requirement_met = False
            self.character.add_items(section.items)
            return section
            
