import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from utils.screen_utils import center_window
from screens.home import HomeScreen
from screens.choose_adventure import ChooseAdventureScreen

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
        self.home_screen.start_new_adventure.connect(self.start_new_adventure)
        self.screens.addWidget(self.home_screen)
        # self.home_screen.set_up()
        
        # Add Choose Adventure Screen
        self.choose_adventure_screen = ChooseAdventureScreen()
        self.screens.addWidget(self.choose_adventure_screen)

        self.screens.setCurrentWidget(self.home_screen)
        
    def start_new_adventure(self):
        self.screens.setCurrentWidget(self.choose_adventure_screen)
        self.choose_adventure_screen.play_new_adventure()

def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    # Grab app styles
    with open("styles.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()