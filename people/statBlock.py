from utils import roll_once, roll_twice


class StatBlock:
    # This is used as a standard for things like monsters, characters and npcs, as they all have a standard set of
    # traits

    def __init__(self):
        self.SKILL = "skill"
        self.STAMINA = "stamina"
        self.LUCK = "luck"
        self.name = ""
        self.skill = 0
        self.stamina = 0

    def roll_combat(self):
        return self.skill + roll_twice()

    def damage(self, amount):
        """Reduces the stat blocks health by amount"""
        self.stamina -= amount
        if self.stamina < 0:
            self.stamina = 0
        return self.stamina == 0

    def test_skill(self):
        return roll_twice() < self.skill

    def combat_wound(self):
        self.damage(2)
