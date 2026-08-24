from utils import d6

class Character():
    init_skill: int
    skill: int
    init_stamina: int
    stamina: int
    init_luck = int
    luck: int
    rations: int
    equipment: list[str]
    
    def __init__(self):
        super().__init__()
        self.rations = 10
        self.equipment = []
        
    def roll_skill(self) -> int:
        """Generates a random number for characters skill, setting this to self.skill

        Returns:
            int: Skill score generated
        """
        self.init_skill = d6.roll_once() + 6
        self.skill = self.init_skill
        return self.skill
        
    def roll_stamina(self) -> int:
        """Randomly generates the characters stamina score, and sets this to self.stamina
        
        Returns: 
            int: Stamina scorce generated
        """
        self.init_stamina = d6.roll_twice() + 12
        self.stamina = self.init_stamina
        return self.stamina
    
    def roll_luck(self) -> int:
        """Randomly generates the characters luck score, and sets this to self.luck
        
        Returns: 
            int: Luck scorce generated
        """
        self.init_luck = d6.roll_once() + 6
        self.luck = self.init_luck
        return self.luck
        
    def test_skill(self) -> bool:
        """Rolls two dice, and checks if it is less than or equal to the characters current skill

        Returns:
            bool: True if test was succeeded, False otherwise
        """
        return d6.roll_twice() <= self.skill
    
    def test_stamina(self) -> bool:
        """Rolls two dice, and checks if it is less than or equal to the characters current stamina

        Returns:
            bool: True if test was succeeded, False otherwise
        """
        return d6.roll_twice() <= self.stamina
    
    def test_luck(self) -> bool:
        """Rolls two dice, and checks if it is less than or equal to the characters current luck. Then reduces the charactes luck by 1

        Returns:
            bool: True if test was succeeded, False otherwise
        """
        roll = d6.roll_twice()
        result = roll <= self.luck
        self.luck -= 1
        return result
        
        