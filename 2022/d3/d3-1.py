#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d3/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d3/prod-input.txt"

src = open(filePath, "r").read().split('\n')

abc = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0



for rucksack in src:
    compartment_1 = rucksack[0:int(len(rucksack) / 2)]
    compartment_2 = rucksack[int(len(rucksack) / 2):]

    match = ''
    for i in compartment_1:
        for j in compartment_2:
            if i == j:
                match = i
                index = abc.find(match) + 1
                
    result += index


print(result)