"""AoC day 1 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d1/tst-input.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d1/prod-input.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n\n')



HIGHEST = 0

for elf in content:
    elf = elf.split('\n')
    elf = list(map(int,elf))

    calories = sum(elf)
    if calories > HIGHEST:
        HIGHEST = calories


print('Result:',HIGHEST)
