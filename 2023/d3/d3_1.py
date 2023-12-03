"""AoC day 3 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d3/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d3/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


class Grid:
    """Class that represents grid and methods to parse it"""
    def __init__ (self, fill, source):
        self.row_count = len(source)
        self.column_count = len(source[0])
        self.fill = fill
        self.cell = []


        for r in range(self.row_count):
            line = ''
            for c in range(self.column_count):
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



def get_number(r, c, max_c):
    """Get full number and length of it"""
    num = ''
    while c < max_c and grid.cell[r][c].isdigit():
        num += grid.cell[r][c]
        c += 1

    return num, len(num)


def find_numbers(source, max_c):
    """Go through the grid and find numbers. Register that in result list"""
    r = 0
    c = 0
    while r in range(len(source)):
        while c in range(len(source[0])):
            value = grid.cell[r][c]

            if value.isdigit():
                num, num_length = get_number(r, c, max_c)
                ALL_NUMBERS.append({"number": num, "length": num_length, "idx_r": r, "idx_c": c})
                c += num_length
            else:
                c += 1

        c = 0
        r += 1



def find_neighbors(num, max_r, max_c):
    """Looks at adjacent cells and looks for simbols"""
    found_chars = 0

    for r in range(num["idx_r"]-1, num["idx_r"]+2):
        for c in range(num["idx_c"]-1, num["idx_c"] + num["length"]+1):

            if not out_of_bounds(r, c, max_r, max_c):
                if (grid.cell[r][c].isalpha() is False and
                    grid.cell[r][c].isdigit() is False and
                    grid.cell[r][c] != '.'):
                    found_chars += 1

    if found_chars > 0:
        RESULT.append(int(num["number"]))



def out_of_bounds(r, c, max_r, max_c):
    """Simple check to see if value is not out of grid"""
    if r in range(0, max_r) and c in range(0, max_c):
        return False

    return True


###################################################

ALL_NUMBERS = []
RESULT = []
MAX_ROW = len(content)
MAX_COL = len(content[0])

grid = Grid('.', content)
grid.set_initial_values(content, "string")
find_numbers(content, MAX_COL)

for number in ALL_NUMBERS:
    find_neighbors(number, MAX_ROW, MAX_COL)

print(sum(RESULT))
