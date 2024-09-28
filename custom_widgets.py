from PySide6.QtWidgets import QPushButton


class QSectionButton(QPushButton):
    def __init__(self, text: str, section: str):
        super().__init__()
        self.setText(text)
        self.section = section
