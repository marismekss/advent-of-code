"""AoC day 1 part 2"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d1/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


digits_as_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
CALIBRATION_SUM = 0


def match_first_digit(line_l, i):
    """Finds the first digit looking from the beginning of string"""
    # if index is digit, there is no point further to search
    if line_l[i].isdigit():
        return line_l, True

    for word in digits_as_words:
        if word == line_l[i:i+len(word)]:
            line_l = line_l[:i] + str(digits_as_words.index(word)) + line_l[i+len(word):]
            return line_l, True
    return line_l, False


def match_last_digit(line_l, i):
    """Finds the first digit looking from back of string"""
    # if index is digit, there is no point further to search
    if line_l[i].isdigit():
        return line_l, True

    for word in digits_as_words:
        if word == line_l[i-len(word)+1:i+1]:
            line_l = line_l[:i-len(word)+1] + str(digits_as_words.index(word)) + line_l[i+1:]
            return line_l, True
    return line_l, False



for line in content:
    digits = []

    # Search for first digit
    for idx in range(0,len(line)):
        res, found = match_first_digit(line, idx)
        if found:
            line = res
            break

    # Search for last digit
    for idx in range(len(line)-1,0, -1):
        res, found = match_last_digit(line, idx)
        if found:
            line = res
            break

    # goes through string and puts all digits in list
    for char in line:
        if char.isdigit():
            digits.append(char)

    CALIBRATION_VALUE = str(digits[0]) + str(digits[-1])
    CALIBRATION_SUM += int(CALIBRATION_VALUE)


print('Result:', CALIBRATION_SUM)
