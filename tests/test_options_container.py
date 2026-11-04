import sys
from unittest.mock import Mock
from PySide6.QtWidgets import QApplication, QCheckBox

from pytest import fixture
from PySide6.QtTest import QSignalSpy, QTest
from PySide6.QtCore import SIGNAL

from utils.custom_widgets.OptionsContainter import OptionsContainer

@fixture(autouse=True)
def setup():
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