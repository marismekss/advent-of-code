#2022-d8
def createGrid(rows, cols, fill):
    arr = [[fill]*cols]*rows
    return arr


#2022-d8
def drawGrid(arr):
    for row in arr:
        tmp = ''.join(row)
        print(tmp) 


#2022-d8
def initSourceGrid(inp):
    out = []
    for row in inp:
        out.append(list(row))
    return out