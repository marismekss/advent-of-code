#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d10/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d10/prod-input.txt"


src = open(filePath, "r").read().split('\n')


def doStep (steps):
    global cycle

    for i in range(steps):
        cycle += 1

        if cycle in cycleValues:
            print(cycle,'th - Register:', register)
            values.append(register * cycle)
    
##########################################################
register = 1
cycle = 0
values = []
cycleValues = [20,60,100,140,180,220]

for line in src:
    instruction = line.split()[0]
    
    if instruction == 'noop':
        doStep(1)

    elif instruction == 'addx':
        value = int(line.split()[1])
        doStep(2)
        register += value

cycle += 1


print('Result:', sum(values))
