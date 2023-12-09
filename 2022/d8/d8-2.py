#filePath = "./2022/d8/tst-input.txt"
filePath = "./2022/d8/prod-input.txt"


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
    l_dis = 0
    r_dis = 0
    u_dis = 0
    d_dis = 0

    tree = int(arr[r][c])
    #print('Tree',tree)

    #LEFT
    for i in reversed(range(0,c)):
        #print('Val:',arr[r][i])
        if int(arr[r][i]) >= tree:
            l_dis += 1
            break
        else:
            l_dis += 1

    #RIGHT
    for i in range(c+1,colCount):
        #print('Val:',arr[r][i])
        if int(arr[r][i]) >= tree:
            r_dis += 1
            break
        else:
            r_dis += 1

    #UP
    for i in reversed(range(0,r)):
        #print('Val:',arr[i][c])
        if int(arr[i][c]) >= tree:
            u_dis += 1
            break
        else:
            u_dis += 1

    #DOWN
    for i in range(r+1,rowCount):
        #print('Val:',arr[i][c])
        if int(arr[i][c]) >= tree:
            d_dis += 1
            break
        else:
            d_dis += 1


    score = l_dis * r_dis * u_dis * d_dis
    #print('L|R = ',l_dis,'|',r_dis,'    U|D = ',u_dis,'|',d_dis )
    #print('Distance: ', score)
    return score

##################################

rowCount = len(src)
colCount = len(src[0])


visibilityGrid = createGrid(rowCount, colCount, None)
trees = initSourceGrid(src)



bestSpot = 0

for i in range(0, rowCount):
    for j in range(0, colCount):
        view = checkVisibility(i,j,trees)
        if view > bestSpot:
            bestSpot = view


print('Best view: ',bestSpot)





