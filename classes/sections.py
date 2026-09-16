class Option():
    next_section: str
    text: str
    requirement: str
    
    def __init__(self, next_section: str, requirement: str, text: str):
        self.next_section = next_section
        self.requirement = requirement
        self.text = text
    
    @classmethod
    def create_from_file(cls, option: dict):
        return cls(next_section=option["section"], requirement=option["requirement"], text=option["text"])
        

class Section():
    number: str
    description: str
    items: list[str]
    items_lost: list[str]
    options: list[Option]

    def __init__(self, number: str, description: str, items: list[str], items_lost: list[str], options: list[dict["text": str, "requirement": str, "section": str]]):
        self.number = number
        self.description = description
        self.items = items
        self.items_lost = items_lost
        self.options = []
        for opt in options:
            self.options.append(Option.create_from_file(opt))

    @classmethod
    def create_from_file(cls, section: str, file: dict):
        if "items" not in file: file["items"] = []
        if "items_lost" not in file: file["items_lost"] = []
        return cls(section, file["text"], file["items"], file["items_lost"], file["options"])
    
