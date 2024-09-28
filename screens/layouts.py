from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QLabel, QGridLayout

from adventure_classes import Section
from custom_widgets import QSectionButton


class layoutAdventure(QVBoxLayout):
    sig_section_changed = Signal(str)  # str = next section number

    def __init__(self):
        super().__init__()
        self.section_text = QLabel()
        self.options = QVBoxLayout()

        self.addWidget(self.section_text)
        self.addStretch(1)
        self.addLayout(self.options)

    def update_contents(self, section: Section):
        self.section_text.setText(section.text)
        self.clear_options()
        for option in section.options:
            btn_option = QSectionButton(option, section.options[option])
            btn_option.clicked.connect(lambda: self.next_section(btn_option.section))
            self.options.addWidget(btn_option)

    def next_section(self, section):
        self.sig_section_changed.emit(section)

    def clear_options(self):
        for i in reversed(range(self.options.count())):
            self.options.itemAt(i).widget().setParent(None)


class layoutCharacter(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.stats = QGridLayout()