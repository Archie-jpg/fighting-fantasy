import os
from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot
from classes.character import Character
from utils.flowlayout import FlowLayout
from utils.custom_widgets.adventure_card import AdventureCard
from dialogs.create_character import Create_Character

class ChooseAdventureScreen(QWidget):
    return_to_menu: Signal = Signal()
    adventure_chosen: Signal = Signal(Path, Character, str)
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.header = QLabel()
        self.header.setObjectName("title")
        self.header.setText("Choose adventure")
        self.main_layout.addWidget(self.header, alignment=(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop))
        
        self.adventures = FlowLayout()
        self.main_layout.addLayout(self.adventures)
        
        self.main_layout.addStretch()
        
        self.btn_return_to_menu: QPushButton = QPushButton("Return to menu")
        self.btn_return_to_menu.setFixedWidth(100)
        self.btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(self.btn_return_to_menu, alignment=(Qt.AlignmentFlag.AlignRight))
    
    @Slot(Path)
    @Slot(Character) 
    def start_new_adventure(self, file: Path, character: Character):
        self.adventure_chosen.emit(file, character, "0")
    
    @Slot(str)
    def create_character(self, file):
        create_character_dialog = Create_Character(file)
        create_character_dialog.start_adventure.connect(self.start_new_adventure)
        result = create_character_dialog.exec()
        create_character_dialog.deleteLater()
        
    def load_adventures(self):
        self.header.setText("Choose adventure to start")
        adventure_path = Path("./adventures")
        for adventure in adventure_path.iterdir():
            if adventure.is_dir():
                adventure_card = AdventureCard(adventure)
                adventure_card.load_description()
                adventure_card.adventure_chosen.connect(self.create_character)
                self.adventures.addWidget(adventure_card)
