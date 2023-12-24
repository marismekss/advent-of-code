"""AoC day 15 part 1"""
#FILEPATH = "./2023/d15/source-test.txt"
FILEPATH = "./2023/d15/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split(',')


def get_hash(input_val):
    current_val = 0
    for char_val in input_val:
        current_val += ord(char_val)
        current_val *= 17
        current_val = current_val % 256

    return current_val


result = []
for each in content:
    result.append(get_hash(each))


print(sum(result))
