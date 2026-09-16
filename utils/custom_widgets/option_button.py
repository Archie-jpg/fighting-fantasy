from PySide6.QtWidgets import *
from PySide6.QtCore import Signal, Slot

from classes.sections import Option

class QOptionButton(QPushButton):
    clicked: Signal = Signal(str)
    section: str
    
    def __init__(self, option: Option):
        super().__init__()
        self.option = option
        self.setText(option.text)
        self.section = option.next_section
    
    def requirement_not_met(self):
        self.setText(f"{self.option.text} (Requires {self.option.requirement})")
        self.setDisabled(True)
    
    def mousePressEvent(self, event):
        self.clicked.emit(self.section)