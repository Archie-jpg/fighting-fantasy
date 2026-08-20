from PySide6.QtWidgets import QWidget, QLabel

class HomeWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.title = QLabel("Home", parent=self)
