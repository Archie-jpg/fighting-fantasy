from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, Slot

class QOptionButton(QPushButton):
    clicked: Signal = Signal(str)
    section: str
    
    def __init__(self, text: str, section: str):
        super().__init__()
        self.setText(text)
        self.section = section
    
    def mousePressEvent(self, event):
        self.clicked.emit(self.section)