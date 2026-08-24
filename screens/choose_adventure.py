import os

from PySide6.QtWidgets import *
from PySide6.QtCore import QRect, Qt, Signal, Slot
from PySide6.QtGui import QGuiApplication
from classes.character import Character
from utils.flowlayout import FlowLayout
from utils.custom_widgets.adventure_card import AdventureCard
from dialogs.create_character import Create_Character

class ChooseAdventureScreen(QWidget):
    return_to_menu: Signal = Signal()
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.header = QLabel()
        self.header.setObjectName("menu_title")
        self.header.setText("Choose adventure")
        self.main_layout.addWidget(self.header, alignment=(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop))
        
        self.adventures = FlowLayout()
        self.main_layout.addLayout(self.adventures)
        
        self.main_layout.addStretch()
        
        self.btn_return_to_menu: QPushButton = QPushButton("Return to menu")
        self.btn_return_to_menu.setFixedWidth(100)
        self.btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(self.btn_return_to_menu, alignment=(Qt.AlignmentFlag.AlignRight))
    
    @Slot(str)
    @Slot(Character) 
    def start_adventure(self, file: str, character: Character):
        print(file)
        print(character)
    
    @Slot(str)
    def create_character(self, file):
        create_character_dialog = Create_Character(file)
        create_character_dialog.start_adventure.connect(self.start_adventure)
        result = create_character_dialog.exec()
        create_character_dialog.deleteLater()
        
    def play_new_adventure(self):
        self.header.setText("Choose adventure to start")
        for file in os.scandir("./adventures"):
            if file.is_file():
                adventure = AdventureCard(file.name, "This is an adventure with multiple lines in it's description to make sure that looks correct")
                adventure.adventure_chosen.connect(self.create_character)
                self.adventures.addWidget(adventure)
