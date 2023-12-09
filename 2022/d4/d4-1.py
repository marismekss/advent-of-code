#filePath = "./2022/d4/tst-input.txt"
filePath = "./2022/d4/prod-input.txt"

src = open(filePath, "r").read().split('\n')

result = 0

for line in src:

    pair1 = line.split(',')[0].split('-')
    pair2 = line.split(',')[1].split('-')

    p1List = []
    p2List = []

    for i in range(int(pair1[0]),int(pair1[1])+1):
        p1List.append(str(i))
    for i in range(int(pair2[0]),int(pair2[1])+1):
        p2List.append(str(i))

    diff1 = len(set(p1List).difference(p2List))
    diff2 = len(set(p2List).difference(p1List))

    if diff1 == 0 or diff2 == 0:
        result += 1

    
print(result)
    
