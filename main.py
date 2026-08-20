import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from windows.home import HomeWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.screens = QStackedWidget(parent=self)
        # Add Home Screen
        self.home_screen = HomeWindow()
        self.screens.addWidget(self.home_screen)

        self.screens.setCurrentWidget(self.home_screen)

def main():
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()