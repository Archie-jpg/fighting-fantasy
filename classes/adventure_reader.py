from pathlib import Path


class AdventureReader():
    def __init__(self, adventure_folder: Path):
        self.adventure_folder = adventure_folder
        
    def load_intro(self) -> str:
        """Gets the introduction to the adventure
        
        Returns:
            (str): A paragraph introducing the adventure
        """