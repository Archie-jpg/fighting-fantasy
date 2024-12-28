from PySide6.QtWidgets import QPushButton


class QOptionButton(QPushButton):
    def __init__(self, option):
        super().__init__()
        self.section = option.section
        self.setText(f"{option.text}, turn to {self.section}")
