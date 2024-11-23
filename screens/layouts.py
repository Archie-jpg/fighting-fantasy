from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QGridLayout, QPushButton

from adventure import Adventure
from customWidgets import QOptionButton, QTestButton
from people.character import Character


class layoutAdventure(QVBoxLayout):
    sig_section_changed = Signal()
    sig_return_to_main = Signal()

    def __init__(self):
        super().__init__()
        self.adventure = None
        self.character = Character()

        self.section_text = QLabel()
        self.item_text = QLabel()
        self.options = QVBoxLayout()

        self.addWidget(self.section_text)
        self.addSpacing(20)
        self.addWidget(self.item_text)
        self.addStretch(1)
        self.addLayout(self.options)

    def new_adventure(self, title):
        self.adventure = Adventure(title)
        self.adventure.start_adventure()
        self.character = self.adventure.character
        return self.character

# The most important method
    def update_contents(self):
        section = self.adventure.current_section
        self.section_text.setText(section.text)
        self.clear_options()
        match section.type:
            case "win":
                self.end_game(win=True)
            case "lose":
                self.end_game(win=False)
            case "item":
                self.item_section(section.get_item())
            case "test":
                self.test_section(section.data)
        for option in section.options:
            btn_option = QOptionButton(option)
            btn_option.clicked.connect(self.selected_section)
            if option.requirement is not None and option.requirement not in self.character.equipment:
                btn_option.setEnabled(False)
                btn_option.setText(f"Requires [{option.requirement}]")
                btn_option.setStyleSheet("background-color: grey")
            self.options.addWidget(btn_option)

# Used for all sections
    def next_section(self, section):
        self.adventure.go_to(section)
        self.sig_section_changed.emit()

    def clear_options(self):
        self.item_text.hide()
        for i in reversed(range(self.options.count())):
            self.options.itemAt(i).widget().setParent(None)

# Used to handle specific types of section
    def selected_section(self):
        self.next_section(self.sender().section)

    def item_section(self, item):
        self.item_text.show()
        self.item_text.setText(f"You found a {item}")
        self.character.gain_item(item)

    def test_section(self, section):
        btn_test = QTestButton(section["stat"], section["success"], section["fail"])
        btn_test.clicked.connect(self.test_stat)
        self.options.addWidget(btn_test)

    def test_stat(self):
        button = self.sender()
        if button.stat == "luck":
            section = button.get_section(self.character.test_luck())
        else:
            section = button.get_section(self.character.test_skill())
        self.next_section(section)

# Used for the end of the game
    def end_game(self, win):
        btn_return_to_menu = QPushButton("Return to main menu")
        btn_return_to_menu.clicked.connect(self.sig_return_to_main.emit)
        self.options.addWidget(btn_return_to_menu)
        if not win:
            btn_try_again = QPushButton("Try again")
            btn_try_again.clicked.connect(self.restart_adventure)
            self.options.addWidget(btn_try_again)

    def restart_adventure(self):
        self.adventure.start_adventure()
        self.sig_section_changed.emit()


class layoutCharacter(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.character = None

        self.name = QLabel("Name")
        self.addWidget(self.name)
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

    def set_character(self, character: Character):
        self.character = character
        self.name = character.name
        self.update_contents()

    def update_contents(self):
        self.skill.setText(str(self.character.skill))
        self.stamina.setText(str(self.character.stamina))
        self.luck.setText(str(self.character.luck))
        self.gold.setText(str(self.character.gold))
        self.provisions.setText(str(self.character.provisions))
        items = "\n".join(self.character.equipment)
        self.equipment.setText(items)

