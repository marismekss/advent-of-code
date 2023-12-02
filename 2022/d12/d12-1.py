from myClasses import *
#https://www.youtube.com/watch?v=pVfj6mxhdMw


filePath = "/Users/marismekss/Documents/Advent of Code/2022/d12/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d3/prod-input.txt"


class Vertex:
    def __init__ (self, coordinate, letter, distance):
        self.coord = coordinate
        self.letter = letter
        self.height = self.get_height()
        self.distance = distance
        self.prevVert = None

    def __name__ (self):
        print (self.coord)
        return str(self.coord)


    def unvisited_neighbors (self):
        y = self.coord[0]
        x = self.coord[1]

        neighbor_coordinates = [[y-1,x], [y+1,x], [y,x-1], [y,x+1]]
        
        for each in neighbor_coordinates:
            ## remove all out-of-bounds neighbors
            if each[0] < 0 or each[0] > rowCount:
                neighbor_coordinates.remove(each)
            ## remove all out-of-bounds neighbors
            if each[1] < 0 or each[1] > colCount:
                neighbor_coordinates.remove(each)
            ## remove visited neighbors
            if each in visited:
                neighbor_coordinates.remove(each)
        
        neighbors = []
        for coord in neighbor_coordinates:
            neighbors.append(area.cell[coord[0]][coord[1]])

        return neighbors


    def get_height(self):
        abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        idx = abc.find(self.letter)

        if self.letter == 'S':
            idx = 0
        if self.letter == 'E':
            idx = 25
        
        return idx




with open(filePath, "r") as f:
    src = f.read().split('\n')


rowCount = len(src)
colCount = len(src[0])

visited = []
unvisited = []


area = Grid(rowCount, colCount, '0')
area.setInitalValues(src, 'string')
#area.draw()


# Fill grid with vertex objects
for r in range(rowCount):
    for c in range(colCount):
        value = area.cell[r][c]

        obj = Vertex([r,c], value, 0)
        area.cell[r][c] = obj
        unvisited.append([r,c])


#print(area.cell[4][4].__dict__)

# ====================================================
current = area.cell[0][0]



# loop through all unvisited (and remove from unvisited)

next = []


for neighbor in current.unvisited_neighbors(): #look at neighbors
    if neighbor.height - current.height in range(0,1): #look at which can be went to 
        next.append(neighbor)
        neighbor.distance += 1 #increase distance for those
        neighbor.prevVert = current

# mark visited previous vertice and remove from univisited
visited.append(current.coord)
unvisited.remove(current.coord)

    
#cleanup next[]


print(unvisited)
print('-----------')
print(visited)
print('===========================================')
