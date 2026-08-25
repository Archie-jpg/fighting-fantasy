from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

class OptionsContainter(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
    def load_options(self, options: list[str]):
        pass


class SectionDisplay(QWidget):
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
        
    def load_adventure(self, adventure_file: str, section: int = 0):
        pass
