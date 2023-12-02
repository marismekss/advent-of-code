filePath = "/Users/marismekss/Documents/Advent of Code/2022/d10/tst-input.txt"
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d10/prod-input.txt"


src = open(filePath, "r").read().split('\n')


register = 1
cycle = 0
pointer = 0

crtLine = []
sprite = [0,1,2]


def prepareCRTLine ():
    for i in range(0,240):
        crtLine.append('_')

def drawCRT():
    values = [40,80,120,160,200,240]
    line = ''
    for i in range(len(crtLine)):
        if i in values:
            print(line)
            line = ''
        line += str(crtLine[i])
    print(line)



def doStep (steps):
    global cycle
    global pointer

    for i in range(steps):
        if cycle in sprite:
            crtLine[pointer] = '#'
        else:   
            crtLine[pointer] = '.'

        print('Cycle: ', cycle, ' | Sprite: ', sprite, ' | Pointer: ', pointer)
        
        cycle += 1
        pointer += 1

        if cycle == 40:
            cycle = 0


    return cycle, pointer

###################################

prepareCRTLine()

for line in src:
    line = line.split()
    instruction = line[0]
    

    if instruction == 'noop':
        doStep(1)


    elif instruction == 'addx':
        value = int(line[1])
        doStep(2)
        register += value
        sprite = [register-1,register,register+1]



drawCRT()
