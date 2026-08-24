import random

def roll_once() -> int:
    """Roll a d6, and return the result

    Returns:
        int: A random number between 1 and 6 inclusive
    """
    return random.randint(1, 6)

def roll_twice() -> int:
    """Roll 2 d6 and return the total of the two results

    Returns:
        int: A random number between 2 and 12 inclusive
    """
    return roll_once() + roll_once()