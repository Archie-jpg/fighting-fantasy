from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.adventure_reader import AdventureReader

class OptionsContainter(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
    def load_options(self, options: list[str]):
        pass


class SectionDisplay(QWidget):
    adventure: AdventureReader
    lay_main: QVBoxLayout
    lbl_section_number: QLabel
    lbl_section_text: QLabel
    options_container: OptionsContainter
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QVBoxLayout()
        self.lbl_section_number = QLabel("0")
        self.lbl_section_number.setObjectName("title")
        self.lay_main.addWidget(self.lbl_section_number, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.lbl_section_text = QLabel("Description")
        self.lay_main.addWidget(self.lbl_section_text)
        self.lay_main.addStretch()
        self.options_container = OptionsContainter()
        self.lay_main.addWidget(self.options_container, alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.lay_main)
        
    def display_section(self, number: int, text: str):
        self.lbl_section_number.setText(str(number))
        self.lbl_section_text.setText(text)
        
    def load_adventure(self, adventure_file: str, section: int = 0):
        self.adventure = AdventureReader(adventure_file)
        if section == 0:
            text = self.adventure.load_intro()
        self.display_section(section, text)
