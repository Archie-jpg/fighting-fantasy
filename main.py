import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from utils import center_window
from screens.home import HomeScreen

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(800, 600)
        center_window(self)
        
        self.screens = QStackedWidget()
        self.setCentralWidget(self.screens)
        # Add Home Screen
        self.home_screen = HomeScreen()
        self.screens.addWidget(self.home_screen)
        # self.home_screen.set_up()

        self.screens.setCurrentWidget(self.home_screen)

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