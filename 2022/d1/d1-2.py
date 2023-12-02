
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d1/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d1/prod-input.txt"

file = open(filePath, "r").read()
src = file.split('\n\n')

calories = []


for elf in src:
    elf = elf.split('\n')
    elf = list(map(int,elf))

    calories.append(sum(elf))

sortedList = sorted(calories)
length = len(sortedList)

result = sortedList[length-1] + sortedList[length-2] + sortedList[length-3] 

print(result)




