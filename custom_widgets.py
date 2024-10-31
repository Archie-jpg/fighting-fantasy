from PySide6.QtWidgets import QPushButton
from adventure import Option


class QSectionButton(QPushButton):
    def __init__(self, option: Option):
        super().__init__()
        self.setText(option.text)
        self.section = option.section
