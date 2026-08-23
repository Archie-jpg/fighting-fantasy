from PySide6.QtWidgets import QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout, QGridLayout, QWidget, QLabel
from PySide6.QtCore import QMargins, Qt

class HomeScreen(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.lay_main: QGridLayout = QGridLayout()
        self.lay_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.lay_main)
        
        self.lay_menu: QVBoxLayout = QVBoxLayout()
        self.lay_menu.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lay_main.addLayout(self.lay_menu, 1, 1)
        
        self.title: QLabel = QLabel("Fighting Fantasy")
        self.title.setObjectName("menu_title")
        self.lay_main.addWidget(self.title, 0, 1)
        
        self.btn_play: QPushButton = QPushButton("Play")
        self.btn_play.clicked.connect(self.show_play_options)
        self.btn_play.setObjectName("menu_btn")
        self.lay_menu.addWidget(self.btn_play)
        
        self.btn_create: QPushButton = QPushButton("Create")
        self.btn_create.setObjectName("menu_btn")
        self.btn_create.clicked.connect(self.show_create_options)
        self.lay_menu.addWidget(self.btn_create)
        
        self.btn_settings: QPushButton = QPushButton("Settings")
        self.btn_settings.setObjectName("menu_btn")
        self.btn_settings.setDisabled(True)
        self.lay_menu.addWidget(self.btn_settings)
        
        self.hidden_options: QVBoxLayout = QVBoxLayout()
        self.lay_main.addLayout(self.hidden_options, 1, 2)
        
        self.hidden_play_spacer = QSpacerItem(0, 0)
        self.hidden_options.addSpacerItem(self.hidden_play_spacer)
        
        self.lay_play_options: QVBoxLayout = QVBoxLayout()
        self.play_options = QWidget()
        self.play_options.setLayout(self.lay_play_options)
        self.play_options.hide()
        self.hidden_options.addWidget(self.play_options)
        
        self.btn_play_new: QPushButton = QPushButton("New")
        self.btn_play_new.setObjectName("menu_btn")
        self.lay_play_options.addWidget(self.btn_play_new)
        
        self.btn_play_continue: QPushButton = QPushButton("Continue")
        self.btn_play_continue.setObjectName("menu_btn")
        self.lay_play_options.addWidget(self.btn_play_continue)
        
        self.lay_create_options: QVBoxLayout = QVBoxLayout()
        self.create_options = QWidget()
        self.create_options.hide()
        self.create_options.setLayout(self.lay_create_options)
        self.hidden_options.addWidget(self.create_options)
        
        self.btn_create_new: QPushButton = QPushButton("New")
        self.btn_create_new.setObjectName("menu_btn")
        self.lay_create_options.addWidget(self.btn_create_new)
        
        self.btn_create_continue: QPushButton = QPushButton("Continue")
        self.btn_create_continue.setObjectName("menu_btn")
        self.lay_create_options.addWidget(self.btn_create_continue)
        
        self.hidden_create_spacer = QSpacerItem(0, 0)
        self.hidden_options.addSpacerItem(self.hidden_create_spacer)
        
    def show_play_options(self):
        self.hidden_create_spacer.changeSize(0, self.btn_create.height())
        self.hidden_play_spacer.changeSize(0, 0)
        self.create_options.hide()
        self.play_options.show()
        
    def show_create_options(self):
        self.hidden_create_spacer.changeSize(0, 0)
        self.hidden_play_spacer.changeSize(0, self.btn_play.height())
        self.play_options.hide()
        self.create_options.show()
