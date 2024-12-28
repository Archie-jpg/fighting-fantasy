from people.statBlock import StatBlock
CURRENT_MONSTER_WIDTH = 100


class Combat:
    def __init__(self, data):
        self.monsters = []
        self.round = 0
        self.escape_round = int(data["escape"])
        for monster in data["monsters"]:
            new_monster = Monster(monster)
            new_monster.set_stats(data["monsters"][monster])
            self.monsters.append(new_monster)

    def next_round(self):
        self.round += 1

    def can_escape(self):
        if self.escape_round == -1:
            return False
        elif self.escape_round <= self.round:
            return True
        return False


class Monster(StatBlock):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def set_stats(self, data):
        self.skill = int(data['skill'])
        self.stamina = int(data['stamina'])


