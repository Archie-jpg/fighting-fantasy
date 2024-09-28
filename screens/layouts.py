from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QGridLayout

from adventure import Section
from custom_widgets import QSectionButton
from character import Character


class layoutAdventure(QVBoxLayout):
    sig_section_changed = Signal(str)  # str = next section number

    def __init__(self):
        super().__init__()
        self.section_text = QLabel()
        self.options = QVBoxLayout()

        self.addWidget(self.section_text)
        self.addStretch(1)
        self.addLayout(self.options)

    def update_contents(self, section: Section):
        self.section_text.setText(section.text)
        self.clear_options()
        for option in section.options:
            btn_option = QSectionButton(option, section.options[option])
            btn_option.clicked.connect(lambda: self.next_section(btn_option.section))
            self.options.addWidget(btn_option)

    def next_section(self, section):
        self.sig_section_changed.emit(section)

    def clear_options(self):
        for i in reversed(range(self.options.count())):
            self.options.itemAt(i).widget().setParent(None)


class layoutCharacter(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(QLabel("Character"))
        self.addSpacing(15)
        self.stats = QGridLayout()
        self.skill = QLabel("0")
        self.new_stat(self.skill, "Skill ", 1)
        self.stamina = QLabel("0")
        self.new_stat(self.stamina, "Stamina ", 2)
        self.luck = QLabel("0")
        self.new_stat(self.luck, "Luck ", 3)
        self.gold = QLabel("0")
        self.new_stat(self.gold, "Gold ", 4)
        self.provisions = QLabel("0")
        self.new_stat(self.provisions, "Provisions", 5)
        self.addLayout(self.stats)
        self.addSpacing(10)
        self.addWidget(QLabel("Equipment:"))
        self.equipment = QLabel()
        self.addWidget(self.equipment)
        self.addStretch(5)

    def new_stat(self, stat, name, row):
        self.stats.addWidget(QLabel(name), row, 0)
        self.stats.addWidget(stat, row, 1)

    def update_contents(self, character: Character):
        self.skill.setText(str(character.skill))
        self.stamina.setText(str(character.stamina))
        self.luck.setText(str(character.luck))
        self.gold.setText(str(character.gold))
        self.provisions.setText(str(character.provisions))
        items = "\n".join(character.equipment)
        self.equipment.setText(items)

