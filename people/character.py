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
        self.name = "character"
        self.skill = roll_twice()
        self.stamina = 12 + roll_twice()
        self.luck = 6 + roll_once()
        self.gold = gold
        self.provisions = provisions
        self.equipment = equipment.split(",")

    # Takes in a string for an item, and adds it to the characters equipment
    def gain_item(self, item):
        if not (item in self.equipment):
            self.equipment.append(item)

    def test_skill(self):
        return roll_twice() < self.skill

    def test_luck(self):
        if self.luck < 2:
            return False
        self.luck -= 1
        return roll_twice() < self.luck + 1
