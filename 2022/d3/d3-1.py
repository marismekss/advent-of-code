"""AoC day 3 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d3/tst-input.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2022/d3/prod-input.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

ABC = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0



for rucksack in content:
    compartment_1 = rucksack[0:int(len(rucksack) / 2)]
    compartment_2 = rucksack[int(len(rucksack) / 2):]

    match = ''
    for i in compartment_1:
        for j in compartment_2:
            if i == j:
                match = i
                idx = ABC.find(match) + 1
                 
    result += idx


print(result)
