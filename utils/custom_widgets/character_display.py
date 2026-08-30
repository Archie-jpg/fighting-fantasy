from typing import NoReturn

from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot

from classes.character import Character


class StatsWidget(QWidget):
    lbl_init_skill: QLabel
    lbl_curr_skill: QLabel
    lbl_init_stamina: QLabel
    lbl_curr_skill: QLabel
    lbl_init_luck: QLabel
    lbl_curr_luck: QLabel
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QGridLayout()
        self.setLayout(self.lay_main)
        
        self.lbl_init = QLabel("Initial")
        self.lay_main.addWidget(self.lbl_init, 0, 1)
        self.lbl_current = QLabel("Current")
        self.lay_main.addWidget(self.lbl_current, 0, 2)
        
        self.lbl_skill = QLabel("Skill")
        self.lay_main.addWidget(self.lbl_skill, 1, 0)
        self.lbl_init_skill = QLabel()
        self.lay_main.addWidget(self.lbl_init_skill, 1, 1)
        self.lbl_curr_skill = QLabel()
        self.lay_main.addWidget(self.lbl_curr_skill, 1, 2)
        
        self.lbl_stamina = QLabel("Stamina")
        self.lay_main.addWidget(self.lbl_stamina, 2, 0)
        self.lbl_init_stamina = QLabel()
        self.lay_main.addWidget(self.lbl_init_stamina, 2, 1)
        self.lbl_curr_stamina = QLabel()
        self.lay_main.addWidget(self.lbl_curr_stamina, 2, 2)
        
        self.lbl_luck = QLabel("Luck")
        self.lay_main.addWidget(self.lbl_luck, 3, 0)
        self.lbl_init_luck = QLabel()
        self.lay_main.addWidget(self.lbl_init_luck, 3, 1)
        self.lbl_curr_luck = QLabel()
        self.lay_main.addWidget(self.lbl_curr_luck, 3, 2)
        
    def load_init_skill(self, init_skill: int):
        """Display given value in lbl_init_skill"""
        self.lbl_init_skill.setText(str(init_skill))
        
    def load_curr_skill(self, skill: int):
        """Display given value in lbl_curr_skill"""
        self.lbl_curr_skill.setText(str(skill))
        
    def load_init_stamina(self, init_stamina: int):
        """Display given value in lbl_init_stamina"""
        self.lbl_init_stamina.setText(str(init_stamina))
        
    def load_curr_stamina(self, stamina: int):
        """Display given value in lbl_curr_stamina"""
        self.lbl_curr_stamina.setText(str(stamina))
        
    def load_init_luck(self, init_luck: int):
        """Display given value in lbl_init_luck"""
        self.lbl_init_luck.setText(str(init_luck))
        
    def load_curr_luck(self, luck: int):
        """Display given value in lbl_curr_luck"""
        self.lbl_curr_luck.setText(str(luck))
        
    def load_stats(self, init_skill: int, skill: int, init_stamina: int, stamina: int, init_luck: int, luck):
        """Display given values as both initial and current"""
        self.load_init_skill(init_skill)
        self.load_curr_skill(skill)
        self.load_init_stamina(init_stamina)
        self.load_curr_stamina(stamina)
        self.load_init_luck(init_luck)
        self.load_curr_luck(luck)
        
class ProvisionsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QHBoxLayout()
        self.setLayout(self.lay_main)
        self.lbl_provisions_remaining = QLabel("Provisions")
        self.lay_main.addWidget(self.lbl_provisions_remaining)
        self.lbl_provisions_remaining = QLabel()
        self.lay_main.addWidget(self.lbl_provisions_remaining)
        self.btn_eat_provisions = QPushButton("Eat")
        self.lay_main.addWidget(self.btn_eat_provisions)
        
    def set_current_provs(self, provisions: int):
        self.lbl_provisions_remaining.setText(str(provisions))
        

class PotionWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QHBoxLayout()
        self.setLayout(self.lay_main)
        self.lbl_potion = QLabel("Potion")
        self.lay_main.addWidget(self.lbl_potion)
        self.lbl_potion_type = QLabel()
        self.lay_main.addWidget(self.lbl_potion_type)
        self.btn_drink_potion = QPushButton("Drink")
        self.lay_main.addWidget(self.btn_drink_potion)
        
    def set_potion(self, potion: str):
        self.lbl_potion_type.setText(potion)
        
        
class EquipmentWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QVBoxLayout()
        self.setLayout(self.lay_main)
        
        self.title = QLabel("Equipment")
        self.title.setObjectName("title")
        self.lay_main.addWidget(self.title)
        
        self.equipment = QLabel()
        self.lay_main.addWidget(self.equipment)
        
    def set_equipment(self, equipment: list[str]):
        equipment_text = ""
        for item in equipment: equipment_text += f"{item}\n"
        self.equipment.setText(equipment_text)


class CharacterDisplay(QWidget):
    character: Character
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QVBoxLayout()
        self.setLayout(self.lay_main)
        
        self.stats_widget = StatsWidget()
        self.lay_main.addWidget(self.stats_widget)
        
        self.provisons_widget = ProvisionsWidget()
        self.lay_main.addWidget(self.provisons_widget)
        
        self.potion_widget = PotionWidget()
        self.lay_main.addWidget(self.potion_widget)
        
        self.equipment_widget = EquipmentWidget()
        self.lay_main.addWidget(self.equipment_widget)
        
        self.lay_main.addStretch()
        
    def update_stats(self):
        """Display characters current stats"""
        self.stats_widget.load_stats(self.character.init_skill, self.character.skill, 
                                    self.character.init_stamina, self.character.stamina,
                                    self.character.init_luck, self.character.luck)
        
    def update_provisions(self):
        """Display the characters current number of provisions"""
        self.provisons_widget.set_current_provs(self.character.provisions)
        
    def update_potion(self):
        """Display the characters current potion"""
        self.potion_widget.set_potion("Stamina")
    
    def update_equipment(self):
        """Display the character current equipment"""
        self.equipment_widget.set_equipment(self.character.equipment)
        
    def load_character(self, character: Character):
        """Display stats about the given character"""    
        self.character = character
        self.update_stats()
        self.update_provisions()
        self.update_potion()
        self.update_equipment()
    
    def add_items(self, items: list[str]) -> NoReturn:
        """Add items to characters equipment, and then update displayed equipment

        Args:
            items (list[str]): The items to be added
        """
        self.character.add_items(items)
        self.update_equipment()
        
        
    
        