import re
"""AoC day 4 part 1"""
#FILEPATH = "./2023/d6/source-test.txt"
FILEPATH = "./2023/d6/source-prod.txt"

with open(FILEPATH, "r", encoding="UTF8") as file:
    content = file.read().split('\n')

# Process text data
time = re.findall(r'\b\d+\b', content[0])
distance = re.findall(r'\b\d+\b', content[1])
races = []
for i, time in enumerate(time):
    races.append([int(time), int(distance[i])])




def driven_distance(btn_press, total_time):
    drive_time = total_time - btn_press
    drive_distance = drive_time * btn_press

    return drive_distance

def winner_time(dst, record):
    if dst > record:
        return True


######################################
winner_list = []


for race in races:
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
