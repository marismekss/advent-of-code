"""AoC day 2"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-prod.txt"

file = open(FILEPATH, "r", encoding="utf8").read()
src = file.split('\n')


RESULT = 0


class Game:
    """Class represents single game with sets of blocks"""

    def __init__(self, id):
        self.id = id
        self.sets = None
        self.invalidsets = 0
        self.fewest_blocks = {"red": 0, "green": 0, "blue": 0}

    def __str__(self):
        return self.id


    def check_sets(self):
        """Checks game sets and counts invalid sets"""

        for set in self.sets:
            cubes_in_set = {"red": 0, "green": 0, "blue": 0}

            cubes = set.split(', ')
            for cube in cubes:
                amount = int(cube.split()[0])
                color = cube.split()[1]

                existing_val = cubes_in_set[color]
                cubes_in_set[color] = existing_val + amount

                if cubes_in_set["red"] > 12 or cubes_in_set["green"] > 13 or cubes_in_set["blue"] > 14:
                    self.invalidsets += 1


  
    def check_fewest(self):
        for set in self.sets:

            cubes = set.split(', ')
            for cube in cubes:
                amount = int(cube.split()[0])
                color = cube.split()[1]

                highest_value= self.fewest_blocks[color]
                if amount > highest_value:
                    self.fewest_blocks[color] = amount


    def get_power(self):
        """Gets multiplication of all color blocks"""
        return self.fewest_blocks["red"] * self.fewest_blocks["green"] * self.fewest_blocks["blue"]



for line in src:
    line = line.split(': ')
    cube_id = line[0].split()[1]
    sets = line[1].split('; ')

    game = Game(cube_id)
    game.sets = sets

    game.check_fewest()
    RESULT += game.get_power()


print('Result:', RESULT)
