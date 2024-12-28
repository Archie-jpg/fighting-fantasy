from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QHBoxLayout, QLabel

from combat import CURRENT_MONSTER_WIDTH, Combat
from customWidgets.QMonsterDisplay import QMonsterDisplay


class QCombatWidget(QWidget):
    sig_damage_player = Signal()
    sig_win = Signal()
    sig_escape = Signal()

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
        self.current_monster.sig_died.connect(self.monster_killed)
        self.btn_escape = QPushButton("Escape")
        self.btn_escape.hide()
        self.btn_escape.clicked.connect(lambda: self.sig_escape.emit())

        # Add things to the layout
        self.layout.addWidget(QLabel("Current Monster"), 0, 0)
        self.layout.addWidget(self.current_monster, 1, 0)
        self.layout.addWidget(self.btn_attack_monster, 2, 0)
        self.layout.addWidget(self.btn_escape, 3, 0)
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

    def attack_monster(self):
        player_roll = self.character.roll_combat()
        monster_roll = self.current_monster.monster.roll_combat()
        if player_roll > monster_roll:
            self.current_monster.hit()
        else:
            self.sig_damage_player.emit()
        # Check if the player can escape the combat
        self.combat.next_round()
        if self.combat.can_escape():
            self.btn_escape.show()

    def monster_killed(self):
        if self.other_monsters.isEmpty():
            self.sig_win.emit()
        else:
            # noinspection PyUnresolvedReferences
            self.current_monster.set_monster(self.other_monsters.itemAt(0).widget().monster)
            self.other_monsters.itemAt(0).widget().deleteLater()
            if self.other_monsters.isEmpty():
                self.btn_change_target.hide()
