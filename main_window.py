from screens.choose_adventure import ChooseAdventureScreen
from screens.home import HomeScreen
from screens.play import PlayAdventureScreen

from utils.screen_utils import center_window

from PySide6.QtWidgets import QMainWindow, QStackedWidget
from PySide6.QtCore import Slot


class MainWindow(QMainWindow):
    home_screen: HomeScreen
    choose_adventure_screen: ChooseAdventureScreen

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(800, 600)
        center_window(self)

        self.screens = QStackedWidget()
        self.setCentralWidget(self.screens)

        # Add Home Screen
        self.home_screen = HomeScreen()
        self.home_screen.start_new_adventure.connect(self.choose_new_adventure)
        self.screens.addWidget(self.home_screen)
        # self.home_screen.set_up()

        # Add Choose Adventure Screen
        self.choose_adventure_screen = ChooseAdventureScreen()
        self.screens.addWidget(self.choose_adventure_screen)

        # Add Play Adventure Screen
        self.play_adventure_screen = PlayAdventureScreen()
        self.screens.addWidget(self.play_adventure_screen)
        
        self.screens.setCurrentWidget(self.home_screen)

    def choose_new_adventure(self):
        self.screens.setCurrentWidget(self.choose_adventure_screen)
        self.choose_adventure_screen.adventure_chosen.connect(self.play_adventure)
        self.choose_adventure_screen.load_adventures()
        
    @Slot(str)
    def play_adventure(self, adventure_file: str):
        self.screens.setCurrentWidget(self.play_adventure_screen)
        self.play_adventure_screen.load_adventure(adventure_file)