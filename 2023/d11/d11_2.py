from itertools import permutations, combinations
"""AoC day 11 part 2"""
#FILEPATH = "./2023/d11/source-test.txt"
FILEPATH = "./2023/d11/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


class Grid:
    """Class that represents grid and methods to parse it"""
    def __init__ (self, fill, r_len, c_len):
        self.row_count = r_len
        self.column_count = c_len
        self.fill = fill
        self.cell = []


        for _ in range(self.row_count):
            line = ''
            for _ in range(self.column_count):
                line += fill
            (self.cell).append(list(line))


    def draw(self):
        """Draw grid on the screen"""
        for r in range(self.row_count):
            line = ''

            for c in range(self.column_count):
                line += str(self.cell[r][c])
            print(line)


    def set_initial_values(self,source_data,data_type):
        """Fills grid with source data values"""
        # dataType = string/integer
        for r in range(self.row_count):
            for c in range(self.column_count):
                if data_type == 'integer':
                    self.cell[r][c] = int(source_data[r][c])
                else:
                    self.cell[r][c] = source_data[r][c]

    
    def get_xy_for_stars(self):
        tmp_list = []
        for r in range(self.row_count):
            for c in range(self.column_count):
                if self.cell[r][c] == '#':
                    tmp_list.append({'r': r, 'c': c})

        return tmp_list
    

def calculate_raw_distance():
    for each in list(star_combinations):
        r_dist = each[0]['r'] - each[1]['r']
        c_dist = each[0]['c'] - each[1]['c']
        dist = abs(r_dist) + abs(c_dist)
        rays.append({'coordinates': each, 'raw_distance': dist})

def empty_line(direction, idx):
    state = True
    if direction == 'column':
        for i in range(0, MAX_ROW):
            if grid.cell[i][idx] != '.':
                state = False
    if direction == 'row':
        for i in range(0, MAX_COL):
            if grid.cell[idx][i] != '.':
                state = False

    return state


def find_galaxy_increase(line, increase):
    increaser = 0
    if line[0]['r'] > line[1]['r']:
        max_r = line[0]['r']
        min_r = line[1]['r']
    else:
        max_r = line[1]['r']
        min_r = line[0]['r']

    if line[0]['c'] > line[1]['c']:
        max_c = line[0]['c']
        min_c = line[1]['c']
    else:
        max_c = line[1]['c']
        min_c = line[0]['c']


    for r in range(min_r+1, max_r):
        if empty_line('row', r):
            increaser += increase
    for c in range(min_c+1, max_c):
        if empty_line('column', c):
            increaser += increase

    return increaser

###################################################

MAX_ROW = len(content)
MAX_COL = len(content[0])

grid = Grid('.', MAX_ROW, MAX_COL)
grid.set_initial_values(content, "string")

rays = []
stars = grid.get_xy_for_stars()
star_combinations = list(combinations(stars, 2))
calculate_raw_distance()


results = []

for idx, each in enumerate(rays):
    increment = find_galaxy_increase(each['coordinates'], 999999)
    real_dist = each['raw_distance'] + increment
    results.append(real_dist)


print(sum(results))
