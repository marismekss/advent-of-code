from myClasses import *

##################################


#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/tst-input-2.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/prod-input.txt"
src = open(filePath, "r").read().split('\n')



def moveTail (xDiff, yDiff, head, tail, last):
    #print('Difference:    Y:', yDiff, '  X:', xDiff)
    #print('BEFORE:    Head:', head, '  Tail:', tail)
    
    while abs(yDiff) > 1 or abs(xDiff) > 1:

        ## HORIZONTAL/VERTICAL movement
        if xDiff == 0 or yDiff == 0:
            # N
            if yDiff > 0:
                #print('---N')
                tail[0] += 1 
            # E
            elif xDiff > 0:
                #print('---E')
                tail[1] += 1
            # S
            elif yDiff < 0:
                #print('---S')
                tail[0] -= 1
            # W
            elif xDiff < 0:
                #print('---W')
                tail[1] -= 1

            if last == True:
                traveled.append(str(tail[0]) + ',' + str(tail[1]))
            else:
                allTraveled.append(str(tail[0]) + ',' + str(tail[1]))



        ## DIAGONAL MOVEMENT
        else:
            #print('Needs diagonal movement')
            # NE
            if yDiff > 0 and xDiff > 0:
                #print('---NE')
                tail[0] += 1
                tail[1] += 1
            # SW
            elif yDiff < 0 and xDiff < 0:
                #print('---SW')
                tail[0] -= 1
                tail[1] -= 1
            # NW
            elif yDiff > 0 and xDiff < 0:
                #print('---NW')
                tail[0] += 1  # +=1 
                tail[1] -= 1  # -=1
            # SE
            elif yDiff < 0 and xDiff > 0:
                #print('---SE')
                tail[0] -= 1  # -=1
                tail[1] += 1  # +=1

            if last == True:
                traveled.append(str(tail[0]) + ',' + str(tail[1]))
            else:
                allTraveled.append(str(tail[0]) + ',' + str(tail[1]))


        #clearGrid()
        #drawCurrent()
        #space.draw()
        
        xDiff = head[1] - tail[1]
        yDiff = head[0] - tail[0]
    
    return tail

    #print('AFTER:     Head:', head, '  Tail:', tail)


def moveHead (instr,head):
    #print('--------------------')
    prev = [head[0],head[1]]
    dir = instr.split()[0]
    dist = int(instr.split()[1])

    if dir == 'R':
        head[1] += dist
    
    elif dir == 'L':
        head[1] -= dist
    
    elif dir == 'U':
        head[0] += dist

    elif dir == 'D':
        head[0] -= dist

    allTraveled.append(str(head[0]) + ',' + str(head[1]))

    return head


x = 11  #11
y = 5   #5


allTraveled = [str(y) + ',' + str(x)]
traveled = [str(y) + ',' + str(x)]
#knots = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

knots = [[y,x],[y,x],[y,x],[y,x],[y,x],[y,x],[y,x],[y,x],[y,x],[y,x]]

def countDimensions ():
    maxX = 0
    maxY = 0

    for knot in knots:
        if knot[0] > maxY:
            maxY = knot[0]
        if knot[1] > maxX:
            maxX = knot[1]

    print('Y:', maxY, ' | X:', maxX)

maxY = 21
maxX = 26

space = Grid(maxY,maxX,'.')

def clearGrid():
    for r in range(maxY):
        for c in range(maxX):
            space.cell[r][c] = '.'


def drawTailTrail ():
    for i in traveled:

        r = (maxY - 1) - int(i.split(',')[0])
        c = int(i.split(',')[1])
        space.cell[r][c] = '#'



def drawCurrent ():
    for i in reversed(range(10)):
        r = (maxY - 1) - knots[i][0]
        c = knots[i][1]
        if i == 0:
            space.cell[r][c] = 'H'
        else:
            space.cell[r][c] = str(i)


    



for instruction in src:

    inst = instruction.split()
    for i in range(1,int(inst[1])+1):
        instruct = str(inst[0]) + ' 1'

        tmpHead = moveHead(instruct,knots[0])
        knots[0][0] = tmpHead[0]
        knots[0][1] = tmpHead[1]


        for i in range(1,10):
            #print('---',i)
            xDiff = knots[i-1][1] - knots[i][1]
            yDiff = knots[i-1][0] - knots[i][0]

            if i == 9:
                flag = True
            else: 
                flag = False


            knots[i] = moveTail(xDiff, yDiff, knots[i-1], knots[i], flag)
                
        
        #clearGrid()
        #drawCurrent()
        #space.draw()
        #print('----------------')

#clearGrid()
#drawTailTrail()
#space.draw()

#countDimensions()

result = len(set(traveled))
print('Result:', result)



# Tried 2680 - too low
