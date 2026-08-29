import json
from pathlib import Path

class Option():
    next_section: str
    text: str
    
    def __init__(self, next_section: str, text: str):
        self.next_section = next_section
        self.text = text
        
    def __init__(self, option: dict):
        self.next_section = option["section"]
        self.text = option["text"]
    

class Section():
    number: str
    description: str
    options: list[Option]
    
    def __init__(self, number: str, description: str, options: list[dict["text": str, "section": str]]):
        self.number = number
        self.description = description
        self.options = []
        for opt in options: 
            self.options.append(Option(opt))
    
    @classmethod        
    def create_from_file(cls, section: str, file: dict):
        return cls(section, file["text"], file["options"])


class AdventureReader():
    def __init__(self, adventure_folder: Path):
        self.adventure_folder = adventure_folder
        
    def load_intro(self) -> str:
        """Gets the introduction to the adventure
        
        Returns:
            (str): A paragraph introducing the adventure
        """
        with open(f"{self.adventure_folder}/introduction.txt", "r") as file:
            intro: str = file.read()
            first_option: dict = {"text": "Begin Adventure", "section": "1"}
            return Section("0", intro, [first_option])
        
    def load_section(self, section_number: str) -> str:
        with open(f"{self.adventure_folder}/{section_number}.json", "r") as file:
            return Section.create_from_file(section_number, json.load(file))
            
            
