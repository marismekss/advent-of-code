"""AoC day 10 part 1"""
#FILEPATH = "./2023/d10/source-test.txt"
FILEPATH = "./2023/d10/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

directions = {
    '|': 'NS',
    '-': 'WE',
    'J': 'NW',
    '7': 'WS',
    'F': 'SE',
    'L': 'NE'
}
change_io = {
    'N': 'S',
    'S': 'N',
    'E': 'W',
    'W': 'E'
}



class Grid:
    """Class that represents grid and methods to parse it"""
    def __init__ (self, fill, source):
        self.row_count = len(source)
        self.column_count = len(source[0])
        self.fill = fill
        self.cell = []
        self.paths = {'N': [], 'E': [], 'S': [], 'W': []}


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

    def find_start_point(self, start_char):
        for r in range(self.row_count):
            for c in range(self.column_count):
                if self.cell[r][c] == start_char:
                    return r,c


def out_of_bounds(r, c, max_r, max_c):
    """Simple check to see if value is not out of grid"""
    if r in range(0, max_r) and c in range(0, max_c):
        return False

    return True


def next_move_coordinates(r, c, point_to):
    if point_to == 'N':
        return r-1, c
    elif point_to == 'E':
        return r, c+1
    elif point_to == 'S':
        return r+1, c
    elif point_to == 'W':
        return r, c-1


def process_cell(inp_dir, r, c):
    symb = grid.cell[r][c]

    if symb != 'X':
        out_dir = directions[symb].replace(inp_dir, '')
        in_next = change_io[out_dir]

        outp = {
            'input_direction': inp_dir,
            'row': r,
            'column': c,
            'symbol': symb,
            'output_direction': out_dir,
            'input_for_next': in_next
        }
    else:
        outp = {
            'input_direction': inp_dir,
            'row': r,
            'column': c,
            'symbol': symb,
            'output_direction': None,
            'input_for_next': None
        }
    return outp


def check_initial_possible_paths(idx_r, idx_c):
    outp = []
    # N
    if grid.cell[idx_r-1][idx_c] in ['|', '7', 'F'] and not out_of_bounds(idx_r-1, idx_c, MAX_ROW, MAX_COL):
        val = process_cell('S', idx_r-1, idx_c)
        outp.append(val)
    # E
    if grid.cell[idx_r][idx_c+1] in ['-', '7', 'J'] and not out_of_bounds(idx_r, idx_c+1, MAX_ROW, MAX_COL):
        val = process_cell('W', idx_r, idx_c+1)
        outp.append(val)
    # S
    if grid.cell[idx_r+1][idx_c] in ['|', 'J', 'L'] and not out_of_bounds(idx_r+1, idx_c, MAX_ROW, MAX_COL):
        val = process_cell('N', idx_r+1, idx_c)
        outp.append(val)
    # W
    if grid.cell[idx_r][idx_c-1] in ['-', 'F', 'L'] and not out_of_bounds(idx_r, idx_c-1, MAX_ROW, MAX_COL):
        val = process_cell('E', idx_r, idx_c-1)
        outp.append(val)

    return outp

#############################################################

MAX_ROW = len(content)
MAX_COL = len(content[0])

grid = Grid('.', content)
grid.set_initial_values(content, "string")

START_R, START_C = grid.find_start_point('S')

grid.cell[START_R][START_C] = 'X'
paths = check_initial_possible_paths(START_R, START_C)


i = 0
r = paths[0]['row']
c = paths[0]['column']
inp_dir = paths[0]['input_direction']


symb = 'A'

while symb != 'X':
    cell_values = process_cell(inp_dir, r, c)
    symb = cell_values['symbol']

    if symb != 'X':
        next_coord = next_move_coordinates(r, c, cell_values['output_direction'])
        r = next_coord[0]
        c = next_coord[1]
        inp_dir = cell_values['input_for_next']

    i += 1

print(i/2)
