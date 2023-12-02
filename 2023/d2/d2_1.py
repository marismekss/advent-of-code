"""AoC day 2 part 1"""
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-test.txt"
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

GAME_LIST = []
RESULT = []


class Game:
    """Class that defines the game with its sets and cubes"""
    def __init__(self, g_id):
        self.id = g_id
        self.sets = None
        self.invalidsets = 0

    def __str__(self):
        return self.id

    def check_sets(self):
        """Checks game sets and counts invalid sets"""
        for game_set in self.sets:
            cubes_in_set = {"red": 0, "green": 0, "blue": 0}

            cubes = game_set.split(', ')
            for cube in cubes:
                amount = int(cube.split()[0])
                color = cube.split()[1]

                existing_val = cubes_in_set[color]
                cubes_in_set[color] = existing_val + amount

            if cubes_in_set["red"] > 12 or cubes_in_set["green"] > 13 or cubes_in_set["blue"] > 14:
                self.invalidsets += 1


for line in content:
    line = line.split(': ')
    game_id = line[0].split()[1]
    sets = line[1].split('; ')

    game = Game(game_id)
    game.sets = sets
    GAME_LIST.append(game)

    game.check_sets()

    if game.invalidsets == 0:
        RESULT.append(int(game.id))


print(sum(RESULT))
