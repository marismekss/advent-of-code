#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d2/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d2/prod-input.txt"

file = open(filePath, "r").read()
src = file.split('\n')


mapping = [
    ['A X', 4],
    ['A Y', 8],
    ['A Z', 3],
    ['B X', 1],
    ['B Y', 5],
    ['B Z', 9],
    ['C X', 7],
    ['C Y', 2],
    ['C Z', 6],
]

myScore = 0

for each in mapping: 
    myScore += src.count(each[0]) * each[1]

print(myScore)