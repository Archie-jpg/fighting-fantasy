from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

from pathlib import Path

class AdventureCard(QWidget):
    adventure_chosen: Signal = Signal(Path)
    
    def __init__(self, folder_path: Path, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.folder_path: Path = folder_path
        
        title: str = folder_path.name
        title = title.replace("_", " ")
        title = title.capitalize()
        self.lbl_title = QLabel(title)
        self.lbl_title.setObjectName("title")
        self.main_layout.addWidget(self.lbl_title)
        
        self.lbl_description = QLabel()
        self.lbl_description.setWordWrap(True)
        self.main_layout.addWidget(self.lbl_description)        
        
    def mousePressEvent(self, event):
        self.adventure_chosen.emit(self.folder_path)
        
    def load_description(self):
        with open(f"{self.folder_path}/description.txt") as file:
            description: str = file.read()
            print(description)
            self.lbl_description.setText(description)