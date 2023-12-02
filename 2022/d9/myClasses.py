class Grid:
    def __init__ (self, rowCount, columnCount, fill):
        self.rowCount = rowCount
        self.columnCount = columnCount
        self.fill = fill
        self.cell = [] 


        for r in range(self.rowCount):
            line = ''
            for c in range(self.columnCount):
                line += fill
            (self.cell).append(list(line))


    def draw(self):
        for r in range(self.rowCount):
            line = ''
           # print(self.cell[r])
            for c in range(self.columnCount):
                line += str(self.cell[r][c])
            print(line)
        
        
    def setInitalValues(self,sourceData,dataType):
        ## dataType = string/integer
        for r in range(self.rowCount):
            for c in range(self.columnCount):
                if dataType == 'integer':
                    self.cell[r][c] = int(sourceData[r][c])
                else:
                    self.cell[r][c] = sourceData[r][c]