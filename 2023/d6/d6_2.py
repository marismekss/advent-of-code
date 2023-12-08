import re
"""AoC day 4 part 1"""
#FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d6/source-test.txt"
FILEPATH = "/Users/marismekss/Documents/Advent of Code/2023/d6/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')


# Process text data
time = int(content[0].replace(' ','').split(':')[1])
distance = int(content[1].replace(' ','').split(':')[1])
race = [time, distance]


def driven_distance(btn_press, total_time):
    drive_time = total_time - btn_press
    drive_distance = drive_time * btn_press

    return drive_distance

def winner_time(dst, record):
    if dst > record:
        return True



######################################
winner_list = []


won_drives = 0
for button_press_time in range(race[0]+1):
    distance = driven_distance(button_press_time, race[0])
    if winner_time(distance, race[1]):
        won_drives += 1

if won_drives > 0:
    winner_list.append(won_drives)


# Multiply all won races
result = 1
for each in winner_list:
    result = result * each


print(result)
