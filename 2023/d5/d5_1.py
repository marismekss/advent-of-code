"""AoC day 5 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d5/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d5/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n\n')



class Seed:
    """Class represents seed with its parameters"""
    def __init__(self, seed_id):
        self.id = int(seed_id)
        self.soil = None
        self.fertilizer = None
        self.water = None
        self.light = None
        self.temperature = None
        self.humidity = None
        self.location = None

    def __repr__(self):
        return str(self.id)



def check_range(inp, mapping_name):
    """Inputs source value and gets mapped value"""
    if inp in mapping[mapping_name]["src"]:
        idx = mapping[mapping_name]["src"].index(inp)
        outp = mapping[mapping_name]["dst"][idx]
    else:
        outp = inp

    return outp


def check_range (payload, inp):
    numbers = payload.split('\n')[1:]

    for line in numbers:
        src = int(line.split()[1])
        dst = int(line.split()[0])
        length = int(line.split()[2])

        outp = 0
        if inp in range(src, src + length):
            delta = inp - src
            outp = dst + delta
            return outp

    if outp == 0:
        outp = inp

    return outp


#########################################################

seed_objects = []
result = []
seeds = content[0][6:].split()


for seed_id in seeds:
    seed = Seed(seed_id)

    seed.soil = check_range(content[1], seed.id)
    seed.fertilizer = check_range(content[2], seed.soil)
    seed.water = check_range(content[3], seed.fertilizer)
    seed.light = check_range(content[4], seed.water)
    seed.temperature = check_range(content[5], seed.light)
    seed.humidity = check_range(content[6], seed.temperature)
    seed.location = check_range(content[7], seed.humidity)
    seed_objects.append(seed)

    result.append(seed.location)

print(min(result))
