import os
import signal

from PySide6.QtCore import QSize, Signal
from PySide6.QtWidgets import QGridLayout, QPushButton


class screenChooseAdventure(QGridLayout):
    adventure_selected = Signal(str)  # Str = Title

    def __init__(self):
        super().__init__()
        adventures = os.listdir("./adventureFiles")
        for title in adventures:
            title = title.replace(".json", "")
            btn_adventure = QPushButton(title)
            btn_adventure.setMaximumSize(QSize(300, 40))
            btn_adventure.clicked.connect(self.adventure_chosen)
            self.addWidget(btn_adventure)

    def adventure_chosen(self):
        title = self.sender().text()
        self.adventure_selected.emit(title)
