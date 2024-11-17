from PySide6.QtWidgets import QPushButton

class QSectionButton(QPushButton):
    def __init__(self, option):
        super().__init__()
        self.option = option
        self.setText(option.text)

    def get_section(self):
        return self.option.section
