from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.adventure_reader import AdventureReader, Section, Option
from utils.custom_widgets.option_button import QOptionButton

class OptionsContainter(QWidget):
    option_chosen: Signal = Signal(str)
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
    @Slot(str)
    def choose_option(self, next_section: str):
        self.option_chosen.emit(next_section)
        
    def load_options(self, options: list[Option]):
        for option in options:
            btn_option = QOptionButton(f"{option.text}", option.next_section)
            btn_option.clicked.connect(self.choose_option)
            self.main_layout.addWidget(btn_option)
    
    def clear(self):
        while self.main_layout.count() > 0:
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None: widget.deleteLater()


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
        self.options_container.option_chosen.connect(self.load_next_section)
        self.lay_main.addWidget(self.options_container, alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.lay_main)
        
    def display_section(self, section: Section):
        self.options_container.clear()
        self.lbl_section_number.setText(section.number)
        self.lbl_section_text.setText(section.description)
        self.options_container.load_options(section.options)
        
    def load_adventure(self, adventure_file: str, section: int = 0):
        self.adventure = AdventureReader(adventure_file)
        if section == 0:
            section: Section = self.adventure.load_intro()
        self.display_section(section)
    
    @Slot(str)
    def load_next_section(self, section_number: str):
        section = self.adventure.load_section(section_number)
        self.display_section(section)
