import json
from pathlib import Path

from classes.sections import Section
    

class AdventureReader():
    def __init__(self, adventure_folder: Path):
        self.adventure_folder = adventure_folder
        
    def load_intro(self) -> Section:
        """Gets the introduction to the adventure
        
        Returns:
            (str): A paragraph introducing the adventure
        """
        with open(f"{self.adventure_folder}/introduction.txt", "r") as file:
            intro: str = file.read()
            first_option: dict = {"text": "Begin Adventure", "section": "1"}
            return Section("0", intro, [], [first_option])
        
    def load_section(self, section_number: str) -> Section:
        with open(f"{self.adventure_folder}/{section_number}.json", "r") as file:
            return Section.create_from_file(section_number, json.load(file))
            
            
