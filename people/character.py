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

    def gain_item(self, item):
        if not (item in self.equipment):
            self.equipment.append(item)

    def test_skill(self):
        if roll_twice() < self.skill:
            return True
        else:
            return False

    def test_luck(self):
        self.luck -= 1
        if roll_twice() < self.luck + 1:
            return True
        else:
            return False
