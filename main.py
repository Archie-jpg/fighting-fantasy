import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

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