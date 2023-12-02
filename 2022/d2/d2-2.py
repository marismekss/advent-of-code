#filePath = "/Users/marismekss/Documents/Advent of Code/2022/d2/tst-input.txt"
filePath = "/Users/marismekss/Documents/Advent of Code/2022/d2/prod-input.txt"

src = open(filePath, "r").read().split('\n')


mapping = [
    ['A X', 3],
    ['A Y', 4],
    ['A Z', 8],
    ['B X', 1],
    ['B Y', 5],
    ['B Z', 9],
    ['C X', 2],
    ['C Y', 6],
    ['C Z', 7],
]

myScore = 0

for each in mapping: 
    myScore += src.count(each[0]) * each[1]

print(myScore)