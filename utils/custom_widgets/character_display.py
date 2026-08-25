from PySide6.QtWidgets import *
from PySide6.QtCore import Qt, Signal, Slot


class StatsWidget(QWidget):
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
   
        
class ProvisionsWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QHBoxLayout()
        self.setLayout(self.lay_main)
        self.lbl_provisions = QLabel("Provisions")
        self.lay_main.addWidget(self.lbl_provisions)
        self.lbl_provisions_remaining = QLabel()
        self.lay_main.addWidget(self.lbl_provisions_remaining)
        self.btn_eat_provisions = QPushButton("Eat")
        self.lay_main.addWidget(self.btn_eat_provisions)
        

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
        
        
class EquipmentWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main = QVBoxLayout()
        self.setLayout(self.lay_main)
        
        self.title = QLabel("Equipment")
        self.title.setObjectName("title")
        self.lay_main.addWidget(self.title)


class CharacterDisplay(QWidget):
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
        