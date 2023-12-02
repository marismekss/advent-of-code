file = open("/Users/marismekss/Documents/Advent of Code/2016/day2/2-test.txt", "r")
file = open("/Users/marismekss/Documents/Advent of Code/2016/day2/2-prod.txt", "r")

keypad = [[1,2,3],[4,5,6],[7,8,9]]
combination = []

currY = 1
currX = 1


for line in file:
    line = list(line)

    for elem in line:
        if elem == 'U':
            if currY > 0:
                currY -= 1
        
        if elem == 'D':
            if currY < 2:
                currY += 1

        if elem == 'R':
            if currX < 2:
                currX += 1

        if elem == 'L':
            if currX > 0:
                currX -= 1
    
    combination.append(keypad[currY][currX])

print(combination)
