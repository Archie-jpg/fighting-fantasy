from utils import roll_once, roll_twice


class Character:
    def __init__(self):
        self.skill = 0
        self.stamina = 0
        self.luck = 0
        self.gold = 0
        self.provisions = 0
        self.equipment = []

    def new_character(self, gold: int, provisions: int, equipment: str):
        self.skill = roll_twice()
        self.stamina = 12 + roll_twice()
        self.luck = 6 + roll_once()
        self.gold = gold
        self.provisions = provisions
        self.equipment = equipment.split(",")
        print(equipment)
