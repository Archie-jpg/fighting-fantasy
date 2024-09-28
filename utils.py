import random
import json


def roll_once():
    return random.randint(1, 6)


def roll_twice():
    return random.randint(1, 6) + random.randint(1, 6)


def read_adventure(title):
    file_path = "adventureFiles/" + title.replace(" ", "_") + ".json"
    with open(file_path) as json_data:
        data = json.load(json_data)
    return data
