from myClasses import *

##################################


#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d9/prod-input.txt"
src = open(filePath, "r").read().split('\n')



def moveTail (xDiff, yDiff):
    #print('Difference:    Y:', yDiff, '  X:', xDiff)
    #print('BEFORE:    Head:', head, '  Tail:', tail)
    
    while abs(yDiff) > 1 or abs(xDiff) > 1:

        ## HORIZONTAL/VERTICAL movement
        if xDiff == 0 or yDiff == 0:
            # N
            if yDiff > 0:
                print('---N')
                tail[0] += 1 
            # E
            elif xDiff > 0:
                print('---E')
                tail[1] += 1
            # S
            elif yDiff < 0:
                print('---S')
                tail[0] -= 1
            # W
            elif xDiff < 0:
                print('---W')
                tail[1] -= 1

            traveled.append(str(tail[0]) + ',' + str(tail[1]))



        ## DIAGONAL MOVEMENT
        else:
            #print('Needs diagonal movement')
            # NE
            if yDiff > 0 and xDiff > 0:
                print('---NE')
                tail[0] += 1
                tail[1] += 1
            # SW
            elif yDiff < 0 and xDiff < 0:
                print('---SW')
                tail[0] -= 1
                tail[1] -= 1
            # NW
            elif yDiff > 0 and xDiff < 0:
                print('---NW')
                tail[0] += 1
                tail[1] -= 1
            # SE
            elif yDiff < 0 and xDiff > 0:
                print('---SE')
                tail[0] -= 1
                tail[1] += 1

            traveled.append(str(tail[0]) + ',' + str(tail[1]))


        xDiff = head[1] - tail[1]
        yDiff = head[0] - tail[0]

    #print('AFTER:     Head:', head, '  Tail:', tail)


def moveHead (instr):
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

    #print('Prev:', prev, 'Head:', head)

    ## Calculate distances between tail and head
    xDiff = head[1] - tail[1]
    yDiff = head[0] - tail[0]

    ## Move tail if too far away
    if abs(xDiff) > 1 or abs(yDiff) > 1:
        #print('Tail needs moving')
        moveTail(xDiff, yDiff)




traveled = ['0,0']
head = [0,0]
tail = [0,0]


for instruction in src:
    moveHead(instruction)


result = len(set(traveled))
print('Result:', result)
