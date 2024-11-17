from utils import read_adventure
from section import Section

data = read_adventure("test adventure")
section = Section(data["sections"]["1"])
print(data["equipment"].split(","))

