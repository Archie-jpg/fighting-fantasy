import random
import json


def roll_once():
    return random.randint(1, 6)


def roll_twice():
    return random.randint(1, 6) + random.randint(1, 6)


def read_adventure(title):
    file_path = title.replace(" ", "_") + ".json"
    with open(file_path):
        data = json.load(file_path)
    return data
