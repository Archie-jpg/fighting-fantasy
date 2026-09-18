from pathlib import Path
from typing import NoReturn

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.character import Character
from classes.section import Section, Option
from classes.adventure_player import AdventurePlayer
from utils.custom_widgets.option_button import QOptionButton

class OptionsContainter(QWidget):
    option_chosen: Signal = Signal(str)
    return_to_menu: Signal = Signal()
    try_again: Signal = Signal()
    
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
        return btn_option
    
    def load_win(self) -> NoReturn:
        """Creates a button to return to main menu"""
        btn_return_to_menu = QPushButton(text="Return to main menu")
        btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(btn_return_to_menu)
    
    def load_lose(self) -> NoReturn:
        """Creates a button to return to home screen and try the adventure again"""
        btn_try_again = QPushButton(text="Try Again")
        btn_try_again.clicked.connect(self.try_again.emit)
        self.main_layout.addWidget(btn_try_again)
        btn_return_to_menu = QPushButton(text="Return to main menu")
        btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(btn_return_to_menu)
        
    def clear(self):
        """Removes all options from it's layout
        """
        while self.main_layout.count() > 0:
            item = self.main_layout.takeAt(0)
            widget = item.widget()
            if widget is not None: widget.deleteLater()


class AdventureDisplay(QWidget):
    adventure: AdventurePlayer
    lay_main: QVBoxLayout
    lbl_section_number: QLabel
    lbl_section_text: QLabel
    options_container: OptionsContainter
    
    # Signals
    return_to_menu: Signal = Signal()
    retry_adventure: Signal = Signal(Path)
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QVBoxLayout()
        self.lbl_section_number = QLabel("0")
        self.lbl_section_number.setObjectName("title")
        self.lay_main.addWidget(self.lbl_section_number, alignment=Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignLeft)
        self.lbl_section_text = QLabel("Description")
        self.lbl_section_text.setWordWrap(True)
        self.lay_main.addWidget(self.lbl_section_text)
        self.lay_main.addStretch()
        self.options_container = OptionsContainter()
        self.options_container.option_chosen.connect(self.load_option_chosen)
        self.options_container.return_to_menu.connect(self.return_to_menu.emit)
        self.options_container.try_again.connect(self.start_again)
        self.lay_main.addWidget(self.options_container, alignment=Qt.AlignmentFlag.AlignBottom)
        self.setLayout(self.lay_main)
        
    def display_section(self, section: Section):
        self.options_container.clear()
        self.lbl_section_number.setText(section.number)
        self.lbl_section_text.setText(section.description)
        if section.type == "Win": self.options_container.load_win()
        elif section.type == "Lose": self.options_container.load_lose()
        else:
            for option in section.options:
                btn_option = self.options_container.load_option(option)
                if not(option.requirement == "" or self.adventure.requirement_met(option.requirement)):
                    btn_option.requirement_not_met()
        
    def load_adventure(self, adventure_file: Path, character: Character, section: str):
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
        
    def start_again(self):
        self.retry_adventure.emit(self.adventure.adventure_folder)
