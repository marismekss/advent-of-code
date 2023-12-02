#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d5/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d5/prod-input.txt"

src = open(filePath, "r").read().split('\n\n')


COLUMN_COUNT = 9
warehouse = []
INCR = 1


## Prepare data of stacks
for i in range(1,COLUMN_COUNT+1):
    stack = []

    for line in src[0].split('\n'):
        if line[INCR] != ' ' and line[INCR].isnumeric() != True :
            stack.append(line[INCR])

    stack = list(reversed(stack))
    INCR += 4
    warehouse.append(stack)



## Start moving crates
for line in src[1].split('\n'):
    line = line.split()
    qnt = int(line[1])
    mvFrom = int(line[3])
    mvTo = int(line[5])

    for i in range(1,qnt+1):
        crate = warehouse[mvFrom-1].pop()
        warehouse[mvTo-1].append(crate)


## Get results
result = []
for stack in warehouse:
    crate = stack.pop()
    result.append(crate)

print(''.join(result))
