"""AoC day 16 part 1"""
FILEPATH = "./2023/d16/source-test.txt"
#FILEPATH = "./2023/d16/source-prod.txt"

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

    def out_of_bounds(self, r, c):
        """Simple check to see if value is not out of grid"""
        if r in range(0, self.row_count) and c in range(0, self.column_count):
            return False

        return True
    

mapping = {
    r'\W': ['N'],
    r'\S': ['E'],
    r'\E': ['S'],
    r'\N': ['W'],
    '/W': ['S'],
    '/S': ['W'],
    '/E': ['N'],
    '/N': ['E'],
    '-W': ['W'],
    '-S': ['W', 'E'],
    '-E': ['E'],
    '-N': ['W', 'E'],
    '|N': ['N'],
    '|W': ['N', 'S'],
    '|S': ['S'],
    '|E': ['N', 'S'],
    '.W': ['W'],
    '.S': ['S'],
    '.E': ['E'],
    '.N': ['N'],
}

def get_next_coordinates(loc_pov, loc_r, loc_c):
    if loc_pov == 'E':
        loc_c += 1
    elif loc_pov == 'W':
        loc_c -= 1
    elif loc_pov == 'N':
        loc_r -= 1
    elif loc_pov == 'S':
        loc_r += 1

    return loc_r, loc_c
##############################
MAX_ROW = len(content)
MAX_COL = len(content[0])

grid = Grid('.', MAX_ROW, MAX_COL)
grid.set_initial_values(content, "string")

paths = []

pov = 'E'
r = 0
c = 0 
#start outside of grid

path = []
print (r,c)
val = grid.cell[r][c]
print(val)
pov = mapping[val+pov]

#foreach path in paths: 

#check if more paths
if len(pov) == 1:
    r, c = get_next_coordinates(pov[0], r, c)
    path.append(str(r) + '|' + str(c))
else:
    # if pov splits into two
    #1
    r, c = get_next_coordinates(pov[0], r, c)
    path.append(str(r) + '|' + str(c))
    #2
    r, c = get_next_coordinates(pov[0], r, c)
    paths.append([str(r) + '|' + str(c)])
    
    pass
print(pov)



print(r,c)
    



