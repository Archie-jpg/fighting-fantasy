from PySide6.QtWidgets import *
from PySide6.QtCore import Signal
from classes.character import Character

from pathlib import Path

class Create_Character(QDialog):    
    start_adventure: Signal = Signal(Path, Character)
    
    def __init__(self, adventure: Path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Character")
        
        self.character: Character = Character()
        self.adventure = adventure
        
        self.main_layout: QGridLayout = QGridLayout()
        self.setLayout(self.main_layout)
        
        # Skill
        self.lbl_skill = QLabel("Skill:")
        self.main_layout.addWidget(self.lbl_skill, 0, 0)
        self.btn_roll_skill = QPushButton("Roll")
        self.btn_roll_skill.clicked.connect(self.roll_skill)
        self.main_layout.addWidget(self.btn_roll_skill, 0, 1)
        self.lbl_skill_value = QLabel("")
        self.lbl_skill_value.hide()
        self.main_layout.addWidget(self.lbl_skill_value, 0, 1)
        
        # Stamina
        self.lbl_stamina = QLabel("Stamina:")
        self.main_layout.addWidget(self.lbl_stamina, 1, 0)
        self.btn_roll_stamina = QPushButton("Roll")
        self.btn_roll_stamina.clicked.connect(self.roll_stamina)
        self.main_layout.addWidget(self.btn_roll_stamina, 1, 1)
        self.lbl_stamina_value = QLabel("")
        self.lbl_stamina_value.hide()
        self.main_layout.addWidget(self.lbl_stamina_value, 1, 1)
        
        # Luck
        self.lbl_luck = QLabel("Luck:")
        self.main_layout.addWidget(self.lbl_luck, 2, 0)
        self.btn_roll_luck = QPushButton("Roll")
        self.btn_roll_luck.clicked.connect(self.roll_luck)
        self.main_layout.addWidget(self.btn_roll_luck, 2, 1)
        self.lbl_luck_value = QLabel("")
        self.lbl_luck_value.hide()
        self.main_layout.addWidget(self.lbl_luck_value, 2, 1)
        
        # Bottom Buttons
        self.btn_cancel = QPushButton("Cancel")
        self.btn_cancel.clicked.connect(self.reject)
        self.main_layout.addWidget(self.btn_cancel, 3, 0)
        
        self.btn_start_adventure = QPushButton("Start Adventure")
        self.btn_start_adventure.setEnabled(False)
        self.skill_set = False
        self.stamina_set = False
        self.luck_set = False
        self.btn_start_adventure.clicked.connect(self.accept)
        self.main_layout.addWidget(self.btn_start_adventure, 3, 1)
        
    def roll_skill(self):
        skill = self.character.roll_skill()
        self.lbl_skill_value.setText(str(skill))
        self.lbl_skill_value.show()
        self.btn_roll_skill.hide()
        self.skill_set = True
        self.check_enable_start_adventure()
        
    def roll_stamina(self):
        stamina = self.character.roll_stamina()
        self.lbl_stamina_value.setText(str(stamina))
        self.lbl_stamina_value.show()
        self.btn_roll_stamina.hide()
        self.stamina_set = True
        self.check_enable_start_adventure()
        
    def roll_luck(self):
        luck = self.character.roll_luck()
        self.lbl_luck_value.setText(str(luck))
        self.lbl_luck_value.show()
        self.btn_roll_luck.hide()
        self.luck_set = True
        self.check_enable_start_adventure()
        
    def check_enable_start_adventure(self):
        if self.skill_set and self.stamina_set and self.luck_set:
            self.btn_start_adventure.setEnabled(True)
        
    def accept(self):
        super().accept()
        self.start_adventure.emit(self.adventure, self.character)