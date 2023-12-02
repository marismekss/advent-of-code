#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d8/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d8/prod-input.txt"


src = open(filePath, "r").read().split('\n')


def createGrid(rows, cols, fill):
    arr = [[fill]*cols]*rows
    return arr

def drawGrid(arr):
    for row in arr:
        tmp = ''.join(row)
        print(tmp) 

def initSourceGrid(inp):
    out = []
    for row in inp:
        out.append(list(row))
    return out

def checkVisibility(r,c, arr):
    hidden = 0
    tree = int(arr[r][c])
    #print('Tree',tree)

    #LEFT
    for i in range(0,c):
        #print('i=',i)
        #print('Val:',arr[r][i])
        if int(arr[r][i]) >= tree:
            hidden += 1
            break

    #RIGHT
    for i in range(c+1,colCount):
        if int(arr[r][i]) >= tree:
            hidden += 1
            break
    #UP
    for i in range(0,r):
        if int(arr[i][c]) >= tree:
            hidden += 1
            break
    #DOWN
    for i in range(r+1,rowCount):
        if int(arr[i][c]) >= tree:
            hidden += 1
            break

    #print('Hidden: ',hidden)
    if hidden != 4:
        #print('---Visible')
        return 1
    else:
        #print('---Not visible')
        return 0

##################################

rowCount = len(src)
colCount = len(src[0])
innerVisible = 0
outterVisible = colCount * 2 + (rowCount - 2) * 2




visibilityGrid = createGrid(rowCount, colCount, None)
trees = initSourceGrid(src)





for i in range(1, rowCount-1):
    for j in range(1, colCount-1):
        innerVisible += checkVisibility(i,j,trees)

total = innerVisible + outterVisible
print('Visible: ',total)





