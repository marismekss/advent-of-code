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
           # print(self.cell[r])
            for c in range(self.column_count):
                line += str(self.cell[r][c])
            print(line)


    def setInitalValues(self,sourceData,dataType):
        """Fills grid with source data values"""
        ## dataType = string/integer
        for r in range(self.row_count):
            for c in range(self.column_count):
                if dataType == 'integer':
                    self.cell[r][c] = int(sourceData[r][c])
                else:
                    self.cell[r][c] = sourceData[r][c]
