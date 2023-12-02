filePath = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-test.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2023/d2/source-prod.txt"

file = open(filePath, "r").read()
src = file.split('\n')

game_list = []
result = []


class Game:
    def __init__(self, id):
        self.id = id
        self.blue = 0
        self.red = 0
        self.green = 0
        self.sets = None
        self.invalidsets = 0

    def __str__(self):
        return self.id
  
    def check_sets(self):
        for set in self.sets:
            cubes_in_set = {"red": 0, "green": 0, "blue": 0}

            cubes = set.split(', ')
            for cube in cubes:
                amount = int(cube.split()[0])
                color = cube.split()[1]

                existing_val = cubes_in_set[color]
                cubes_in_set[color] = (existing_val + amount)
            
            if cubes_in_set["red"] > 12 or cubes_in_set["green"] > 13 or cubes_in_set["blue"] > 14:
                self.invalidsets += 1
        
            

for line in src:
    line = line.split(': ')
    id = line[0].split()[1]
    sets = line[1].split('; ')

    game = Game(id)
    game.sets = sets
    game_list.append(game)

    game.check_sets()

    if game.invalidsets == 0:
        result.append(int(game.id))


print(sum(result))
