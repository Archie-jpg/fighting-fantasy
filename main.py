import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from utils import center_window
from screens.home import HomeScreen

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.resize(800, 600)
        center_window(self)
        
        self.screens = QStackedWidget(parent=self)
        # Add Home Screen
        self.home_screen = HomeScreen()
        self.screens.addWidget(self.home_screen)

        self.screens.setCurrentWidget(self.home_screen)

def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()