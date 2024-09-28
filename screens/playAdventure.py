from PySide6.QtWidgets import QHBoxLayout

from utils import read_adventure, roll_once, roll_twice


class screenPlayAdventure(QHBoxLayout):

    def __init__(self):
        super().__init__()
        self.adventure = None
        self.character = None

    def new_adventure(self, title):
        self.adventure = read_adventure()
