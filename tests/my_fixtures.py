from unittest.mock import MagicMock, patch

from pytest import fixture
from pytest_mock import MockFixture
from classes.character import Character

@fixture
def new_character() -> Character:
    return Character()

# @pytest.fixture
# def middling_character(new_character: Character) -> Character:
#     new_character.skill == 9
#     new_character.stamina == 18
#     new_character.luck == 9
#     return new_character

@fixture
def mock_roll_once(mocker: MockFixture) -> MagicMock:
    mocked = mocker.patch('utils.d6.roll_once')
    return mocked