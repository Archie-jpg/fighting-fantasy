from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from combat import CURRENT_MONSTER_WIDTH, Monster


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
