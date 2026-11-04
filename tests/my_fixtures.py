from unittest.mock import MagicMock, patch

from pytest import fixture
from pytest_mock import MockFixture
from classes.character import Character
from classes.section import Section

@fixture
def new_character() -> Character:
    """Creates a character with no attributes set"""
    return Character()

@fixture
def blank_section() -> Section:
    """Creates a section with it's attributes set to the following
    number = 1
    description = "test"
    type = "Main"
    items = []
    items_lost = []
    stats = {}
    options = []
    
    Returns:
        Section: With all values set to blank or default values"""
    return Section(number=1, description="test")

@fixture
def mock_roll_once(mocker: MockFixture) -> MagicMock:
    mocked = mocker.patch('utils.d6.roll_once')
    return mocked