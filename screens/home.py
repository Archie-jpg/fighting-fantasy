from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel

class HomeScreen(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        self.title = QLabel("Home")
        self.main_layout.addWidget(self.title)
