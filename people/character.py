from people.statBlock import StatBlock
from utils import roll_once, roll_twice


class Character(StatBlock):
    # This is used for the players character, which has a standard set of traits. There should only be one of these per
    # adventure
    def __init__(self):
        super().__init__()
        self.luck = 0
        self.gold = 0
        self.provisions = 0
        self.equipment = []

    def new_character(self, gold: int, provisions: int, equipment: str):
        """Creates a new character, using things given from the adventure."""
        self.name = "character"
        self.skill = roll_twice()
        self.stamina = 12 + roll_twice()
        self.luck = 6 + roll_once()
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
        self.stamina += 4
        self.provisions -= 1
