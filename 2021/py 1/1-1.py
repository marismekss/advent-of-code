#f = open('2021/py 1/1-test.txt',"r")
f = open('2021/py 1/1-prod.txt',"r")


prevDepth = f.readline().rstrip()

## Get all depth from file
depthList = []
for item in f:
    depthList.append(item.rstrip())
f.close()

counter = 0

for depth in depthList:
    if int(depth) > int(prevDepth):
        counter += 1

    prevDepth = depth

print("Result is: ",counter)
    

