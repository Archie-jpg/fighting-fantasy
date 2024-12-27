from copy import copy

from people.statBlock import StatBlock
from utils import roll_once, roll_twice


class Character(StatBlock):
    # This is used for the players character, which has a standard set of traits. There should only be one of these per
    # adventure
    def __init__(self):
        super().__init__()
        self._initial_skill = None
        self._initial_stamina = None
        self._initial_luck = None
        self.luck = 0
        self.gold = 0
        self.provisions = 0
        self.equipment = []

    def new_character(self, gold: int, provisions: int, equipment: str):
        """Creates a new character, using things given from the adventure."""
        self.name = "character"
        self.skill = roll_twice()
        self._initial_skill = copy(self.skill)
        self.stamina = 12 + roll_twice()
        self._initial_stamina = copy(self.stamina)
        self.luck = 6 + roll_once()
        self._initial_luck = copy(self.luck)
        self.gold = gold
        self.provisions = provisions
        self.equipment = equipment.split(",")

    def gain_item(self, item):
        """Adds the given item to the players equipment if they do not already have it"""
        if not (item in self.equipment):
            self.equipment.append(item)

    def test_luck(self):
        """Begins by reducing the characters luck by 1, then tests their luck by the previous value. The test is
        automatically failed if the characters luck is below 2"""
        if self.luck < 2:
            return False
        self.luck -= 1
        return roll_twice() < self.luck + 1

    def eat_provision(self):
        self.increase_stat(4, self.STAMINA)
        self.provisions -= 1

    def get_gold(self, amount):
        self.gold += amount

    def restore_stat(self, stat):
        match stat:
            case self.STAMINA: self.stamina = copy(self._initial_stamina)
            case self.SKILL: self.skill = copy(self._initial_skill)
            case self.LUCK: self.luck = copy(self._initial_luck)

    def increase_stat(self, amount, stat, above_initial=False):
        def increase(current, initial):
            current += amount
            if current > initial and not above_initial:
                current = copy(initial)
            else:
                initial = copy(current)
        match stat:
            case self.STAMINA: increase(self.stamina, self._initial_stamina)
            case self.SKILL: increase(self.skill, self._initial_skill)
            case self.LUCK: increase(self.luck, self._initial_luck)
