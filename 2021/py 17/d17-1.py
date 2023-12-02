#filePath = "/Users/marismekss/Documents/Advent of Code/2021/py 17/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2021/py 17/prod-input.txt"


src = open(filePath, "r").read()



def doStep():
    global probe
    global velocity
    global maxY

    probe[0] += velocity[0]
    probe[1] += velocity[1]

    if probe[1] > maxY:
        maxY = probe[1]

    if velocity[0] > 0:
        velocity[0] -= 1  # X
    velocity[1] -= 1  # Y


def overshot():
    global probe
    global boxX2
    global boxY2

    if probe[0] > boxX2 and probe[1] < boxY2:
        return True
    else:
        return False

def bullseye():
    global boxX
    global boxY
    global probe

    if probe[0] in boxX and probe[1] in boxY:
        return True
    else:
        return False



#############################




boxX1 = int(src.split()[2].split('..')[0][2:])
boxX2 = int(src.split()[2].split('..')[1][:-1])
boxY1 = int(src.split()[3].split('..')[0][2:])
boxY2 = int(src.split()[3].split('..')[1])


boxX = range(boxX1, boxX2)
boxY = range(boxY1, boxY2)
heights = []



for x in range(boxX2):
    for y in range(100):
        aim = [x,y]
        probe = [0,0]
        velocity = aim.copy()
        maxY = 0
        #print('Aim: ', aim)

        for i in range(1,1000):
            doStep()
            
            if overshot():
                #print('OVERSHOT at velocity ',aim)
                break

            if bullseye():
                #print('BULLSEYE at velocity ', aim)
                heights.append(maxY)
                #print('   maxY:', maxY)
                break

            #print('Step ', i, ' | Probe:', probe, ' | Velocity: ', velocity)

        #print('--- Max Y:', maxY)
        

print(sorted(heights))



