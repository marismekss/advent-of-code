sourceFile = open("/Users/marismekss/Documents/Advent of Code/2021/day11/11-test.txt","r")

class Grid:

    def __init__(self):
        self.grid = [] 

    def draw(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def incrementByOne(self):
        newGrid = []
        for row in range(len(self.grid)):
            newRow = list(map(lambda x: x + 1, self.grid[row]))
            #newRow = list(map(self.incrementAndCheck(),self.grid[row]))
            newGrid.append(newRow)
        self.grid = newGrid.copy()


    
    def initialize(self,source):
        for line in source:
            lineList = list(line.strip())
            row = []
            for each in lineList:
                num = int(each)
                row.append(num)
            self.grid.append(row)



#=======================================
## Put data into grid
grid = Grid()

steps = 1


grid.initialize(sourceFile)
grid.incrementByOne()
grid.draw()
    