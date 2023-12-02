
#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d1/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d1/prod-input.txt"

file = open(filePath, "r").read()
src = file.split('\n\n')


highest = 0

for elf in src:
    elf = elf.split('\n')
    elf = list(map(int,elf))

    calories = sum(elf)
    if calories > highest: 
        highest = calories


print(highest)