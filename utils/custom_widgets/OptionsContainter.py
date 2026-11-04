from classes.section import Option
from utils.custom_widgets.option_button import QOptionButton


from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


from typing import NoReturn


class OptionsContainer(QWidget):
    option_chosen: Signal = Signal(str)
    return_to_menu: Signal = Signal()
    try_again: Signal = Signal()

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

    @Slot(str)
    def choose_option(self, next_section: str):
        self.option_chosen.emit(next_section)

    def load_option(self, option: Option):
        btn_option = QOptionButton(option)
        btn_option.clicked.connect(self.choose_option)
        self.main_layout.addWidget(btn_option)
        return btn_option

    def load_win(self) -> NoReturn:
        """Creates a button to return to main menu"""
        btn_return_to_menu = QPushButton(text="Return to main menu")
        btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(btn_return_to_menu)

    def load_lose(self) -> NoReturn:
        """Creates a button to return to home screen and try the adventure again"""
        btn_try_again = QPushButton(text="Try Again")
        btn_try_again.clicked.connect(self.try_again.emit)
        self.main_layout.addWidget(btn_try_again)
        btn_return_to_menu = QPushButton(text="Return to main menu")
        btn_return_to_menu.clicked.connect(self.return_to_menu.emit)
        self.main_layout.addWidget(btn_return_to_menu)

    def clear(self):
        """Removes all options from it's layout
        """
        item = self.main_layout.takeAt(0)
        while item != None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            item = self.main_layout.takeAt(0)