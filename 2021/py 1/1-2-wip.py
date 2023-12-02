#f = open('/Users/marismekss/Documents/Advent of Code/2021/day1/1-test.txt',"r")
f = open('/Users/marismekss/Documents/Advent of Code/2021/day1/1-prod.txt',"r")


## Get all depth from file
depthList = []
for item in f:
    depthList.append(item.rstrip())
f.close()


## Get group sums
sumDepthList = []
for i in range(len(depthList) - 2):
    groupSum = int(depthList[i]) + int(depthList[i+1]) + int(depthList[i+2])
    sumDepthList.append(groupSum)


## Check how many increase in depth
counter = 0
prevDepth = sumDepthList[0]
for depth in sumDepthList:
    if int(depth) > int(prevDepth):
        counter += 1
        prevDepth = depth

print(counter)
    

