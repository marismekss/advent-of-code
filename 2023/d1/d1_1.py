"""AoC day 1"""
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-test.txt"
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    src = file.read().split('\n')


CALIBRATION_SUM = 0


for line in src:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)

    CALIBRATION_VALUE = str(digits[0]) + str(digits[-1])
    CALIBRATION_SUM += int(CALIBRATION_VALUE)


print(CALIBRATION_SUM)
