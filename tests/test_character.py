from unittest.mock import patch

from pytest import fixture
from pytest_mock import MockFixture
from classes.character import Character
from tests.my_fixtures import *


class TestNewCharacter:
    @fixture(autouse=True)
    def setup():
        pass
    
    def test_initial_provisions(self, new_character: Character):
        """New characters start with 10 provisions"""
        assert new_character.provisions == 10, "A character should start off with 10 rations"
    
    def test_initial_equipment(self, new_character: Character):
        """New characters start with no equipment"""
        assert new_character.equipment == [], "A character should start off with no equipment"
        
    def test_roll_skill(self, new_character: Character, mocker: MockFixture):
        """When a characters skill is rolled, the value is roll + 6 and both initial_skill and skill are set to this value"""
        mock_roll_once = mocker.patch('utils.d6.roll_once')
        mock_roll_once.return_value = 6
        skill = new_character.roll_skill()
        assert skill == 12, "Skill should be roll + 6"
        assert new_character.skill == skill, "Characters skill should be set to the value of skill"
        assert new_character.init_skill == skill, "Characters initial skill should be set to the value of skill"
        
    def test_roll_stamina(self, new_character: Character, mocker: MockFixture):
        """When a characters stamina is rolled, the value is two rolls + 12 and both initial_stamina and stamina are set to this value"""
        mock_roll_once = mocker.patch('utils.d6.roll_once')
        mock_roll_once.return_value = 6
        stamina = new_character.roll_stamina()
        assert stamina == 24, "stamina should be two rolls + 12"
        assert new_character.stamina == stamina, "Characters stamina should be set to the value of stamina"
        assert new_character.init_stamina == stamina, "Characters initial stamina should be set to the value of stamina"
    
    def test_roll_luck(self, new_character: Character, mocker: MockFixture):
        """When a characters luck is rolled, the value is roll + 6 and both initial_luck and luck are set to this value"""
        mock_roll_once = mocker.patch('utils.d6.roll_once')
        mock_roll_once.return_value = 6
        luck = new_character.roll_luck()
        assert luck == 12, "luck should be roll + 6"
        assert new_character.luck == luck, "Characters luck should be set to the value of luck"
        assert new_character.init_luck == luck, "Characters initial luck should be set to the value of luck"
        
        
class TestAbilityChecks:
    @fixture(autouse=True)
    def setup(self, new_character: Character, mock_roll_once: MagicMock):
        mock_roll_once.return_value = 4
        self.new_character = new_character
    
    def test_successful_skill_check(self):
        self.new_character.skill = 12
        assert self.new_character.check_skill() == True, "If roll is less than skill, true should be returned"
        self.new_character.skill = 8
        assert self.new_character.check_skill() == True, "If roll is equal to skill, true should be returned"
    
    def test_failing_skill_check(self):
        self.new_character.skill = 7
        assert self.new_character.check_skill() == False, "If roll is greater than skill, false should be returned"
        
    def test_successful_stamina_check(self):
        self.new_character.stamina = 12
        assert self.new_character.check_stamina() == True, "If roll is less than stamina, true should be returned"
        self.new_character.stamina = 8
        assert self.new_character.check_stamina() == True, "If roll is equal to stamina, true should be returned"
        
    def test_failing_stamina_check(self):
        self.new_character.stamina = 7
        assert self.new_character.check_stamina() == False, "If roll is greater than stamina, false should be returned"
        
    def test_successful_luck_check(self):
        self.new_character.luck = 12
        assert self.new_character.check_luck() == True, "If roll is less than luck, true should be returned"
        self.new_character.luck = 8
        assert self.new_character.check_luck() == True, "If roll is equal to luck, true should be returned"
        
    def test_failing_luck_check(self):
        self.new_character.luck = 7
        assert self.new_character.check_luck() == False, "If roll is greater than luck, false should be returned"
        
    def test_luck_reduced(self):
        self.new_character.luck = 10
        self.new_character.check_luck()
        assert self.new_character.luck == 9, "When a luck check is performed, luck should be reduced by 1"
    
    
        