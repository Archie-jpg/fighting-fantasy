from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

class HomeScreen(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.main_layout)
        
        self.title = QLabel("Fighting Fantasy")
        self.title.setObjectName("title")
        self.title.font().setPointSize(40)
        self.main_layout.addWidget(self.title)
