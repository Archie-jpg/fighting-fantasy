class Option():
    next_section: str
    text: str
    
    def __init__(self, next_section: str, text: str):
        self.next_section = next_section
        self.text = text
        
    def __init__(self, option: dict):
        self.next_section = option["section"]
        self.text = option["text"]
        

class Section():
    number: str
    description: str
    items: list[str]
    options: list[Option]

    def __init__(self, number: str, description: str, items: list[str], options: list[dict["text": str, "section": str]]):
        self.number = number
        self.description = description
        self.items = items
        self.options = []
        for opt in options:
            self.options.append(Option(opt))

    @classmethod
    def create_from_file(cls, section: str, file: dict):
        return cls(section, file["text"], file["items"], file["options"])
    
