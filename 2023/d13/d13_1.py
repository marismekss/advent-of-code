"""AoC day 13 part 1"""
FILEPATH = "./2023/d13/source-test.txt"
#FILEPATH = "./2023/d13/source-prod.txt"

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

    def look_vertical(self, l, r):
        
        row = 0

        while  
        #print(self.cell[row][l], ' ',self.cell[row][r])




##############################
MAX_ROW = len(content)
MAX_COL = len(content[0])

grid = Grid('.', MAX_ROW, MAX_COL)
grid.set_initial_values(content, "string")

grid.look_vertical(0,1)


