from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.character import Character
from classes.sections import Section, Option
from classes.adventure_player import AdventurePlayer
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
        
    def load_option(self, option: Option):
        btn_option = QOptionButton(option)
        btn_option.clicked.connect(self.choose_option)
        self.main_layout.addWidget(btn_option)
    
    def clear(self):
        """Removes all options from it's layout
        """
        while self.main_layout.count() > 0:
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None: widget.deleteLater()


class SectionDisplay(QWidget):
    adventure: AdventurePlayer
    lay_main: QVBoxLayout
    lbl_section_number: QLabel
    lbl_section_text: QLabel
    options_container: OptionsContainter
    
    # Signals
    
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
        self.options_container.option_chosen.connect(self.load_option_chosen)
        self.lay_main.addWidget(self.options_container, alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.lay_main)
        
    def display_section(self, section: Section):
        self.options_container.clear()
        self.lbl_section_number.setText(section.number)
        self.lbl_section_text.setText(section.description)
        for option in section.options:
            self.options_container.load_option(option)
        
    def load_adventure(self, adventure_file: str, character: Character, section: str):
        self.adventure = AdventurePlayer(adventure_file, character)
        self.load_next_section(section)
        
    def load_next_section(self, section_number: str):
        """Displays the section associated with the given number
        
        Args:
            section_number: Reference number of the section
        """
        section: Section = self.adventure.load_section(section_number)
        self.display_section(section)
    
    @Slot(str)
    def load_option_chosen(self, section_number: str):
        """Load the section specified by the option chosen

        Args:
            section_number (str): Section to move to
        """
        self.load_next_section(section_number)
