"""AoC day 1 part 2"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d1/tst-input.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d1/prod-input.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n\n')


calories = []

for elf in content:
    elf = elf.split('\n')
    elf = list(map(int,elf))

    calories.append(sum(elf))

sorted_list = sorted(calories)
length = len(sorted_list)

result = sorted_list[length-1] + sorted_list[length-2] + sorted_list[length-3]

print("Result:", result)
