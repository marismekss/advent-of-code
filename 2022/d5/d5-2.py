#filePath = "./2022/d5/tst-input.txt"
filePath = "./2022/d5/prod-input.txt"

src = open(filePath, "r").read().split('\n\n')


columnCount = 9


warehouse = []
incr = 1


## Prepare data of stacks
for i in range(1,columnCount+1):
    stack = []
    
    for line in src[0].split('\n'):
        if line[incr] != ' ' and line[incr].isnumeric() != True :
            stack.append(line[incr])
    
    stack = list(reversed(stack))
    incr += 4 
    warehouse.append(stack)
    


## Start moving crates
for line in src[1].split('\n'):
    line = line.split()
    qnt = int(line[1])
    mvFrom = int(line[3])
    mvTo = int(line[5])


    tmpStack = []
    for i in range(1,qnt+1):
        crate = warehouse[mvFrom-1].pop()
        tmpStack.append(crate)

    for i in range(1,qnt+1):
        crate = tmpStack.pop()
        warehouse[mvTo-1].append(crate)
  
        

## Get results
result = []
for stack in warehouse:
    crate = stack.pop()
    result.append(crate)

print(''.join(result))