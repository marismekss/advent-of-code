"""AoC day 2 part 1"""
#FILEPATH = "./2022/d2/tst-input.txt"
FILEPATH = "./2022/d2/prod-input.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


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


MY_SCORE = 0

for each in mapping:
    MY_SCORE += content.count(each[0]) * each[1]

print(MY_SCORE)
