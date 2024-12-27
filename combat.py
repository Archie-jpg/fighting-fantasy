from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QWidget, QGridLayout
from people.statBlock import StatBlock
CURRENT_MONSTER_WIDTH = 100


class Combat:
    def __init__(self, data):
        self.monsters = []
        for monster in data["monsters"]:
            new_monster = Monster(monster)
            new_monster.set_stats(data["monsters"][monster])
            self.monsters.append(new_monster)


class Monster(StatBlock):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def set_stats(self, data):
        self.skill = int(data['skill'])
        self.stamina = int(data['stamina'])


class QCombatWidget(QWidget):
    sig_damage_player = Signal()
    sig_win = Signal()

    def __init__(self):
        super().__init__()
        self.combat = None
        self.character = None
        self.current_monster = QMonsterDisplay()
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        # This button is used to attack the current monster
        self.btn_attack_monster = QPushButton("Attack")
        self.btn_attack_monster.clicked.connect(self.attack_monster)
        self.other_monsters = QHBoxLayout()
        self.btn_change_target = QPushButton("Change target")
        self.btn_change_target.clicked.connect(self.change_target)
        self.current_monster.sig_died.connect(self.monster_killed)

        # Add things to the layout
        self.layout.addWidget(QLabel("Current Monster"), 0, 0)
        self.layout.addWidget(self.current_monster, 1, 0)
        self.layout.addWidget(self.btn_attack_monster, 2, 0)
        self.layout.addLayout(self.other_monsters, 1, 1)

        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setColumnStretch(1, 1)
        self.btn_attack_monster.setFixedWidth(CURRENT_MONSTER_WIDTH)
        self.setVisible(False)

    def set_combat(self, data):
        self.combat = Combat(data)
        self.current_monster.set_monster(self.combat.monsters[0])
        for monster in self.combat.monsters[1:]:
            monster_layout = QMonsterDisplay()
            monster_layout.set_monster(monster)
            self.other_monsters.addWidget(monster_layout)
        if self.other_monsters.isEmpty():
            self.btn_change_target.hide()

    def attack_monster(self):
        player_roll = self.character.roll_combat()
        monster_roll = self.current_monster.monster.roll_combat()
        if player_roll > monster_roll:
            self.current_monster.hit()
        else:
            self.sig_damage_player.emit()
        #TODO The other monsters in the combat should also fight back

    def monster_killed(self):
        if self.other_monsters.isEmpty():
            self.sig_win.emit()
        else:
            # noinspection PyUnresolvedReferences
            self.current_monster.set_monster(self.other_monsters.itemAt(0).widget().monster)
            self.other_monsters.itemAt(0).widget().deleteLater()
            if self.other_monsters.isEmpty():
                self.btn_change_target.hide()

    def change_target(self):
        pass
        # TODO Make it so the player can change the monster they are attacking

class QMonsterDisplay(QWidget):
    sig_died = Signal()

    def __init__(self):
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.monster = None
        self.lbl_name = QLabel("Name")
        self.lbl_skill = QLabel("Skill")
        self.lbl_stamina = QLabel("Stamina")
        self.setFixedWidth(CURRENT_MONSTER_WIDTH)

        # Add things to the layout
        self.layout().addWidget(self.lbl_name)
        self.layout().addWidget(self.lbl_skill)
        self.layout().addWidget(self.lbl_stamina)

    def set_monster(self, monster: Monster):
        self.monster = monster
        self.lbl_name.setText(f"{monster.name}")
        self.lbl_skill.setText(f"skill: {monster.skill}")
        self.lbl_stamina.setText(f"stamina: {monster.stamina}")

    def hit(self):
        self.monster.combat_wound()
        self.lbl_stamina.setText(f"stamina: {self.monster.stamina}")
        if self.monster.stamina <= 0:
            self.sig_died.emit()
