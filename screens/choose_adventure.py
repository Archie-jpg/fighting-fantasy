from PySide6.QtWidgets import *
from PySide6.QtCore import QRect, Qt, Signal
from PySide6.QtGui import QGuiApplication
from utils.flowlayout import FlowLayout

class ChooseAdventureScreen(QWidget):
    retun_to_menu: Signal
    
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.header = QLabel()
        self.header.setObjectName("menu_title")
        self.header.setText("Choose adventure")
        self.main_layout.addWidget(self.header, alignment=(Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop))
        
        self.adventures = FlowLayout()
        self.main_layout.addLayout(self.adventures)
        
        self.main_layout.addStretch()
        
        self.btn_return_to_menu: QPushButton = QPushButton("Return to menu")
        self.btn_return_to_menu.setFixedWidth(100)
        self.btn_return_to_menu.clicked.connect(self.retun_to_menu.emit)
        self.main_layout.addWidget(self.btn_return_to_menu, alignment=(Qt.AlignmentFlag.AlignRight))
        
    def play_new_adventure(self):
        print("starting new adventure")
        self.header.setText("Choose adventure to start")
        for i in range(20):
            adventure = QWidget()
            adventure.setFixedWidth(100)
            adventure.setFixedHeight(10)
            adventure.setStyleSheet("background-color: blue")
            self.adventures.addWidget(adventure)