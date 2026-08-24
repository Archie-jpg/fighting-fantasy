from PySide6.QtWidgets import *
from PySide6.QtCore import Signal

class AdventureCard(QWidget):
    adventure_chosen: Signal = Signal()
    
    def __init__(self, file_name: str, description, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.file: str = file_name
        
        title = file_name.replace("_", " ")
        title = title.replace(".csv", "")
        title = title.capitalize()
        self.lbl_title = QLabel(title)
        self.lbl_title.setStyleSheet("font-size: 15px")
        self.main_layout.addWidget(self.lbl_title)
        
        self.lbl_description = QLabel(description)
        self.lbl_description.setWordWrap(True)
        self.main_layout.addWidget(self.lbl_description)        
        
    def mousePressEvent(self, event):
        self.adventure_chosen.emit()