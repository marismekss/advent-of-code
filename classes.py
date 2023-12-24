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

    
    def flip(self,orientation):
        tmp_grid = Grid('.', MAX_ROW, MAX_COL)

        for r in range(self.row_count):
            for c in range(self.column_count):

                if orientation == 'clockwise':
                    tmp_grid.cell[c][self.row_count-1-r] = self.cell[r][c]

                if orientation == 'counterclockwise':
                    tmp_grid.cell[self.column_count-1-c][r] = self.cell[r][c]


        # update existing grid with flipped values
        for r in range(self.row_count):
            for c in range(self.column_count):
                self.cell[r][c] = tmp_grid.cell[r][c]
    
    def out_of_bounds(self, r, c, max_r, max_c):
        """Simple check to see if value is not out of grid"""
        if r in range(0, max_r) and c in range(0, max_c):
            return False

        return True