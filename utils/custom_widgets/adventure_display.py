from pathlib import Path

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.character import Character
from classes.section import Section
from classes.adventure_player import AdventurePlayer
from utils.custom_widgets.OptionsContainter import OptionsContainer

class AdventureDisplay(QWidget):
    adventure: AdventurePlayer
    lay_main: QVBoxLayout
    lbl_section_number: QLabel
    lbl_section_text: QLabel
    options_container: OptionsContainer
    
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
        self.options_container = OptionsContainer()
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

    def display_character_death(self):
        death_section = Section("Death", "You have died, thus failing your adventure", "Lose", [], [], {}, [])
        self.display_section(death_section)