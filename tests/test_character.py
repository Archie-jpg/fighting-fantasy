from unittest.mock import Mock, patch

from pytest import fixture
from pytest_mock import MockFixture
from classes.character import Character
from tests.my_fixtures import *


class TestNewCharacter:
    def test_initial_provisions(self, new_character: Character):
        """New characters start with 10 provisions
        
        Args:
            new_character (Character): An empty character object
        """
        assert new_character.provisions == 10, "A character should start off with 10 rations"
    
    def test_initial_equipment(self, new_character: Character):
        """New characters start with no equipment
        
        Args:
            new_character (Character): An empty character object
        """
        assert new_character.equipment == [], "A character should start off with no equipment"
        
    def test_roll_skill(self, new_character: Character, mocker: MockFixture):
        """When a characters skill is rolled, the value is roll + 6 and both initial_skill and skill are set to this value
        
        Args:
            new_character (Character): An empty character object
        """
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


class TestAdjustStat:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.skill = 10
        self.character.init_skill = 12

    def test_increase_stat(self):
        """Increase the skill value by 1"""
        self.character._adjust_stat("skill", 1)
        assert self.character.skill == 11, "Adjust stat should increase skill by 1"

    def test_increase_stat_above_initial(self):
        """A characters skill cannot be increased past it's initial value"""
        self.character._adjust_stat("skill", 3)
        assert self.character.skill == 12, "Value of skill cannot go above inital"
    
    def test_decrease_stat(self):
        """Adjust skill decreases skill when adjustment is negative"""
        self.character._adjust_stat("skill", -1)
        assert self.character.skill == 9, "Adjust skill should decrease skill by 1 when adjustment is -1"

    def test_decrease_stat_below_0(self):
        """A characters skill cannot be below 0"""
        self.character._adjust_stat("skill", -11)
        assert self.character.skill == 0, "Value of skill cannot go below 0"


class TestAdjustSkill:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.skill = 10
        self.character.init_skill = 12

    def test_increase_skill(self):
        """Adjust skill increases skill when adjustment is positive"""
        self.character.adjust_skill(1)
        assert self.character.skill == 11, "Adjust skill should increase skill by 1 when adjustment is 1"

    def test_decrease_skill(self):
        """Adjust skill decreases skill when adjustment is negative"""
        self.character.adjust_skill(-1)
        assert self.character.skill == 9, "Adjust skill should decrease skill by 1 when adjustment is -1"


class TestAdjustStamina:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.stamina = 10
        self.character.init_stamina = 12

    def test_increase_stamina(self):
        """Adjust stamina increases stamina when adjustment is positive"""
        self.character.adjust_stamina(1)
        assert self.character.stamina == 11, "Adjust stamina should increase stamina by 1 when adjustment is 1"

    def test_decrease_stamina(self):
        """Adjust stamina decreases stamina when adjustment is negative"""
        self.character.adjust_stamina(-1)
        assert self.character.stamina == 9, "Adjust stamina should decrease stamina by 1 when adjustment is -1"


class TestAdjustLuck:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.luck = 10
        self.character.init_luck = 12

    def test_increase_luck(self):
        """Adjust luck increases luck when adjustment is positive"""
        self.character.adjust_luck(1)
        assert self.character.luck == 11, "Adjust luck should increase luck by 1 when adjustment is 1"

    def test_decrease_luck(self):
        """Adjust luck decreases luck when adjustment is negative"""
        self.character.adjust_luck(-1)
        assert self.character.luck == 9, "Adjust luck should decrease luck by 1 when adjustment is -1"

        
class TestAbilityChecks:
    @fixture(autouse=True)
    def setup(self, new_character: Character, mock_roll_once: MagicMock):
        mock_roll_once.return_value = 4
        self.new_character = new_character
    
    def test_successful_luck_check(self):
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
        

class TestComplete:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.new_character = new_character
        
    def test_character_complete(self):
        """If all required things are filled, complete returns true"""
        self.new_character.init_skill = 1
        self.new_character.skill = 1
        self.new_character.init_stamina = 1
        self.new_character.stamina = 1
        self.new_character.init_luck = 1
        self.new_character.luck = 1
        assert self.new_character.complete() == True
        
    def test_character_stats_not_filled(self):
        """If the characters are not set, complete returns False"""
        assert self.new_character.complete() == False

        
class TestAddItems:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.new_character = new_character
    
    def test_add_item(self):
        """When an item is added, it appears in teh characters equipment"""
        self.new_character.add_items(["Bag"])
        assert "Bag" in self.new_character.equipment
        
    def test_add_multiple_items(self):
        """When multiple items are added, each one appears in characters equipment"""
        self.new_character.add_items(["Bag", "Sock"])
        assert "Bag" in self.new_character.equipment
        assert "Sock" in self.new_character.equipment
        
    def test_add_more_items(self):
        """If there is already an item in characters equipment, it is still there when items are added"""
        self.new_character.equipment = ["Sock"]
        self.new_character.add_items(["Bag"])
        assert "Bag" in self.new_character.equipment
        assert "Sock" in self.new_character.equipment

        
class TestRemoveItems:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.new_character = new_character
        
    def test_remove_item(self):
        """When an item is removed, it no longed appears in characters equipments"""
        self.new_character.equipment = ["Bag"]
        self.new_character.remove_items(["Bag"])
        assert "Bag" not in self.new_character.equipment
    
    def test_remove_item_not_in_equipment(self):
        """If removed item is not in characters equipment, nothing happens"""
        self.new_character.equipment = ["Sock"]
        self.new_character.remove_items(["Bag"])
        assert self.new_character.equipment == ["Sock"]
        
    def test_remove_multiple_items(self):
        """If multiple items are to be removed, all should be removed"""
        self.new_character.equipment = ["Sock", "Bag"]
        self.new_character.remove_items(["Bag", "Sock"])
        assert "Sock" not in self.new_character.equipment
        assert "Bag" not in self.new_character.equipment
        
    def test_remove_item_does_not_effect_others(self):
        """If an item is removed, it should not effect other items"""
        self.new_character.equipment  = ["Sock", "Bag"]
        self.new_character.remove_items(["Sock"])
        assert "Sock" not in self.new_character.equipment
        assert "Bag" in self.new_character.equipment
        

class TestHasItem:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.new_character = new_character
        self.new_character.equipment = ["Sock"]
        
    def test_does_have_item(self):
        """If item in characters equipment, function returns True"""
        assert self.new_character.has_item("Sock") == True
        
    def test_does_not_have_item(self):
        """If character does not have the item, function returns False"""
        assert self.new_character.has_item("Bag") == False


class TestAdjustProvisions:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.provisions = 10

    def test_increase_provisions(self):
        """If adjusment is positive, the characters provisions are increased by that number"""
        self.character.adjust_provisions(1)
        assert self.character.provisions == 11

    def test_decrease_provisions(self):
        """If adjustment is negative, the characters provisions are decreased by that number"""
        self.character.adjust_provisions(-1)
        assert self.character.provisions == 9

    def test_emits_all_provisions_used(self):
        """If provisions reaches 0 or less, the all_provisions_used signal needs to be emitted"""
        all_provisions_used_emitted = Mock()
        self.character.all_provisions_used.connect(all_provisions_used_emitted)
        self.character.adjust_provisions(-10)
        all_provisions_used_emitted.assert_called_once()

    def test_only_emits_all_provisions_used_if_needed(self):
        """If provisions have not reached 0, all_provisions_used is not emitted"""
        all_provisions_used_emitted = Mock()
        self.character.all_provisions_used.connect(all_provisions_used_emitted)
        self.character.adjust_provisions(0)
        all_provisions_used_emitted.assert_not_called()


class TestEatProvisions:
    @fixture(autouse=True)
    def setup(self, new_character: Character):
        self.character = new_character
        self.character.provisions = 10
        self.character.init_stamina = 12
        self.character.stamina = 4

    def test_provisions_reduced(self):
        """When character eats provisions, their number of provisions is reduced by 1"""
        self.character.eat_provision()
        assert self.character.provisions == 9

    def test_stamina_increased(self):
        """When character earts provisions, their current stamina is increased by 4"""
        self.character.eat_provision()
        assert self.character.stamina == 8

    def test_only_eat_provisions_if_avalible(self):
        """If the character has no provisions left, nothing should happen"""
        self.character.provisions = 0
        self.character.eat_provision()
        assert self.character.provisions == 0
        assert self.character.stamina == 4