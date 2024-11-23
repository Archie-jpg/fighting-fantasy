from PySide6.QtWidgets import QPushButton


class QOptionButton(QPushButton):
    def __init__(self, option):
        super().__init__()
        self.section = option.section
        self.setText(option.text)


class QTestButton(QPushButton):
    def __init__(self, stat, success, fail):
        super().__init__()
        self.stat = stat
        self.setText(f"Test {stat}")
        self.success = success
        self.fail = fail

    def get_section(self, success):
        if success:
            return self.success
        else:
            return self.fail
