import sys
from unittest.mock import Mock
from PySide6.QtWidgets import QApplication, QPushButton

from pytest import fixture
from PySide6.QtTest import QSignalSpy
from PySide6.QtCore import SIGNAL

from utils.custom_widgets.OptionsContainter import OptionsContainer
from classes.section import Option
from utils.custom_widgets.option_button import QOptionButton

@fixture(autouse=True, scope="module")
def create_application():
    app = QApplication(sys.argv)
    yield
    app.shutdown()

class TestChooseOption:
    def test_section_emitted(self):
        options_container = OptionsContainer()
        spy: QSignalSpy = QSignalSpy(options_container.option_chosen)
        options_container.choose_option("2")
        signal = spy.at(0)
        assert signal[0] == "2"


class TestLoadOption:
    @fixture(autouse=True)
    def setup(self):
        self.options_container = OptionsContainer()
        self.option = Option(next_section="1", requirement="", text="test section")

    def test_btn_added(self):
        """When an option is loaded, a button for it is added to the options container"""
        option_btn: QOptionButton = self.options_container.load_option(self.option)
        added_item = self.options_container.main_layout.itemAt(0).widget()
        assert option_btn == added_item

    def test_click_btn(self):
        """Clicking the button should cause its section to be loaded"""
        spy: QSignalSpy = QSignalSpy(self.options_container.option_chosen)
        option_btn = self.options_container.load_option(self.option)
        option_btn.mousePressEvent(None)
        signal = spy.at(0)
        assert signal[0] == "1"


class TestLoadWin:
    @fixture(autouse=True)
    def setup(self):
        self.options_container = OptionsContainer()

    def test_btn_return_to_menu_added(self):
        """When the player wins, a button to return to the main menu is provided"""
        self.options_container.load_win()
        win_button: QPushButton = self.options_container.main_layout.itemAt(0).widget()
        assert win_button.text() == "Return to main menu"

    def test_return_to_menu(self):
        """When return to main menu button is clicked, signal is emitted"""
        spy: QSignalSpy = QSignalSpy(self.options_container.return_to_menu)
        self.options_container.load_win()
        win_button: QPushButton = self.options_container.main_layout.itemAt(0).widget()
        win_button.click()
        assert spy.count() == 1
