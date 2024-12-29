from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QGridLayout, QPushButton

from adventure import Adventure
from customWidgets.QOptionButton import QOptionButton
from customWidgets.QCombatWidget import QCombatWidget
from customWidgets.QTestButton import QTestButton
from people.character import Character


class layoutAdventure(QVBoxLayout):
    sig_section_changed = Signal()
    sig_return_to_main = Signal()
    sig_update_character = Signal()

    def __init__(self):
        super().__init__()
        self.adventure = None
        self.character = Character()
        self.section = None

        self.section_text = QLabel()
        self.extra_text = QLabel()
        self.test_button = QTestButton()
        self.test_button.clicked.connect(self.test_stat)
        self.killed_button = QPushButton()
        self.killed_button.clicked.connect(self.character_killed)
        self.killed_button.hide()
        self.eat_provisions_button = QPushButton("Eat provisions")
        self.eat_provisions_button.clicked.connect(self.eat_provision)
        self.combat_layout = QCombatWidget()
        self.combat_layout.sig_damage_player.connect(self.character_hit)
        self.combat_layout.sig_win.connect(self.win_combat)
        self.combat_layout.sig_escape.connect(self.escape_combat)
        self.options = QVBoxLayout()

        self.addWidget(self.section_text)
        self.addSpacing(20)
        self.addWidget(self.extra_text)
        self.addWidget(self.combat_layout)
        self.addStretch(1)
        self.addWidget(self.test_button)
        self.addWidget(self.eat_provisions_button)
        self.addWidget(self.killed_button)
        self.addLayout(self.options)

    def new_adventure(self, title):
        self.adventure = Adventure(title)
        self.adventure.start_adventure()
        self.character = self.adventure.character
        self.combat_layout.character = self.adventure.character
        return self.character

# The most important method
    def update_contents(self):
        self.section = self.adventure.current_section
        self.section_text.setText(self.section.text)
        self.clear_options()
        match self.section.type:
            case "simple": self.add_options()
            case "intro": self.add_options()
            case "win": self.end_section(win=True)
            case "lose": self.end_section(win=False)
            case "test": self.test_section()
            case "damage": self.damage_section()
            case "combat": self.combat_section()
            case "reward": self.reward_section()
            case _: raise Exception(f"This kind of section is not supported \n"
                                    f"Section number: {self.adventure.current_pos} \n"
                                    f"Section type: {self.section.type}")

# Used for all sections
    def next_section(self, section_number):
        self.adventure.go_to(section_number)
        self.sig_section_changed.emit()

    def add_options(self):
        """If a section has multiple paths to go down, this adds them to the gui"""
        options = self.section.get_options()
        for option in options:
            btn_option = QOptionButton(option)
            btn_option.clicked.connect(self.select_section)
            if option.requirement is not None and option.requirement not in self.character.equipment:
                btn_option.setEnabled(False)
                btn_option.setText(f"Requires [{option.requirement}]")
                btn_option.setStyleSheet("background-color: grey")
            elif option.cost > 0:
                btn_option.clicked.connect(self.option_cost)
                if self.character.gold < option.cost:
                    btn_option.setEnabled(False)
                    btn_option.setText(f"Costs {option.cost} gold")
                    btn_option.setStyleSheet("background-color: grey")
            self.options.addWidget(btn_option)

    def option_cost(self):
        self.character.spend_gold(self.sender().cost)
        self.next_section(self.sender().section)

    def select_section(self):
        self.next_section(self.sender().section)

    def clear_options(self):
        self.extra_text.setText("")
        self.test_button.hide()
        self.eat_provisions_button.hide()
        for i in reversed(range(self.options.count())):
            self.options.itemAt(i).widget().setParent(None)

# Used to handle specific types of section
    def end_section(self, win):
        self.killed_button.hide()
        btn_return_to_menu = QPushButton("Return to main menu")
        btn_return_to_menu.clicked.connect(self.sig_return_to_main.emit)
        self.options.addWidget(btn_return_to_menu)
        if not win:
            btn_try_again = QPushButton("Try again")
            btn_try_again.clicked.connect(self.restart_adventure)
            self.options.addWidget(btn_try_again)

    def item_section(self):
        """Used for any section that gives the character an item"""
        item = self.section.get_attribute("item")
        self.extra_text.setText(f"You found a {item}")
        self.character.gain_item(item)
        self.add_options()

    def test_section(self):
        test = self.section.get_attribute("test")
        self.test_button.set_test(test)
        self.test_button.show()

    def damage_section(self):
        """Used for any section that does damage to the character"""
        damage = int(self.section.get_attribute("damage"))
        self.extra_text.setText(f"You suffer {damage} points of damage")
        dead = self.character.damage(damage)
        if dead:
            self.killed_button.show()
            return
        self.add_options()

    def combat_section(self):
        self.combat_layout.setVisible(True)
        monsters = self.section.get_attribute("combat")
        self.combat_layout.set_combat(monsters)

    def reward_section(self):
        section = self.section
        items = section.get_attribute("items")
        gold = section.get_attribute("gold")
        if section.get_attribute("provisions") != "false":
            self.add_provisions_option()
        if items != "":
            for item in items.split(","):
                self.character.gain_item(item)
        if gold != "":
            self.character.gain_gold(int(gold))
        self.reward_stat("skill")
        self.reward_stat("stamina")
        self.reward_stat("luck")
        self.add_options()

# Other useful methods
    def test_stat(self):
        if self.test_button.stat == "luck":
            section = self.test_button.get_section(self.character.test_luck)
        else:
            section = self.test_button.get_section(self.character.test_skill())
        self.next_section(section)

    def restart_adventure(self):
        self.adventure.start_adventure()
        self.sig_section_changed.emit()

    def character_killed(self):
        """For when the character is killed during the adventure"""
        self.clear_options()
        self.removeWidget(self.combat_layout)
        try:
            self.section_text.setText(self.section.get_attribute("killed_text"))
        finally:
            self.extra_text.setText("You have died")
            self.end_section(False)

    def add_provisions_option(self):
        self.eat_provisions_button.show()
        self.add_options()

    def eat_provision(self):
        self.character.eat_provision()
        self.sig_update_character.emit()
        self.eat_provisions_button.hide()

    def character_hit(self):
        self.character.combat_wound()
        self.sig_update_character.emit()
        if self.character.stamina <= 0:
            self.lose_combat()

    def win_combat(self):
        self.combat_layout.setVisible(False)
        self.next_section(self.section.get_attribute("win_section"))

    def lose_combat(self):
        self.combat_layout.setVisible(False)
        self.character_killed()

    def escape_combat(self):
        self.combat_layout.setVisible(False)
        self.character_hit()
        self.next_section(self.section.get_attribute("escape_section"))

    def reward_stat(self, stat: str):
        stat_value = self.section.get_attribute(stat)
        if stat_value == "":
            return
        elif stat_value == "restore":
            self.character.restore_stat(stat)
        else:
            self.character.increase_stat(int(stat_value), stat)




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

    def update_stamina(self):
        self.stamina.setText(str(self.character.stamina))

