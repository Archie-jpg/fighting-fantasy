from PySide6.QtWidgets import QPushButton


class QTestButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.stat = None
        self.success = None
        self.fail = None

    def set_test(self, test):
        self.stat = test["stat"]
        self.setText(f"Test {self.stat}")
        self.success = test["success"]
        self.fail = test["fail"]

    def get_section(self, success):
        if success:
            return self.success
        else:
            return self.fail
