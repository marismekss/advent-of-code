"""AoC day 2"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-prod.txt"

with open(FILEPATH, "r", encoding="utf8") as file:
    content = file.read().split('\n')


class Game:
    """Class represents single game with sets of blocks"""

    def __init__(self, g_id):
        self.id = g_id
        self.sets = None
        self.invalidsets = 0
        self.fewest_blocks = {"red": 0, "green": 0, "blue": 0}


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

                if (cubes_in_set["red"] > 12 or
                    cubes_in_set["green"] > 13 or
                    cubes_in_set["blue"] > 14):
                    self.invalidsets += 1


    def check_fewest(self):
        """Checks the fewest amount of colored cubes"""
        for game_set in self.sets:

            cubes = game_set.split(', ')
            for cube in cubes:
                amount = int(cube.split()[0])
                color = cube.split()[1]

                highest_value= self.fewest_blocks[color]
                if amount > highest_value:
                    self.fewest_blocks[color] = amount


    def get_power(self):
        """Gets multiplication of all color blocks"""
        return self.fewest_blocks["red"] * self.fewest_blocks["green"] * self.fewest_blocks["blue"]



RESULT = 0

for line in content:
    line = line.split(': ')
    cube_id = line[0].split()[1]
    sets = line[1].split('; ')

    game = Game(cube_id)
    game.sets = sets

    game.check_fewest()
    RESULT += game.get_power()


print('Result:', RESULT)
